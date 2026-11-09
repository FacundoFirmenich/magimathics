#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
import numpy as np
import h5py

FILES=[
 ("01_FC2500mT_20250319_2120__10K.h5","Loop 1"),
 ("02_FC2500mT_20250319_2358__10K.h5","Loop 2"),
 ("03_FC2500mT_20250320_0231__10K.h5","Loop 3"),
 ("04_FC2500mT_20250320_0504__10K.h5","Loop 4"),
 ("05_FC2500mT_20250320_0738__10K.h5","Loop 5"),
]

def coercive(field,vnorm):
    c=[]
    for i in range(len(field)-1):
        if vnorm[i]*vnorm[i+1] < 0:
            den=vnorm[i+1]-vnorm[i]
            c.append(float((field[i]*vnorm[i+1]-field[i+1]*vnorm[i])/den))
    return (c[0],c[1]) if len(c)>=2 else None

def load_blocks(path):
    with h5py.File(path) as f:
        field=np.asarray(f["Data"]["Magnetic_Field"],float)
        avg=np.asarray(f["Data"]["Avg_Voltage_Hp34420A_Ch1"],float)
        raw=np.asarray(f["Data"]["Voltage_Array_Hp34420A_Ch1"],float)
    if raw.ndim==1:
        raw=raw[:,None]
    i=0
    while i+1<len(field) and abs(field[i]-field[i+1])<0.01:
        i+=1
    p2=i+1
    curr_inverted=bool(avg[0]*avg[1]<0)
    p=round(p2/2) if curr_inverted else p2
    blocks=[]
    j=0
    while j+p2<=len(field):
        ff=field[j:j+p2]
        aa=avg[j:j+p2]
        rr=raw[j:j+p2]
        if curr_inverted:
            pos=rr[:p].reshape(-1)
            neg=rr[p:p2].reshape(-1)
            obs=float(np.mean(aa[:p])-np.mean(aa[p:p2]))
            raw_obs=float(np.mean(pos)-np.mean(neg))
            blocks.append({
              "field_raw_T":float(np.mean(ff)),
              "pos_raw_V":pos,
              "neg_raw_V":neg,
              "observed_avg_effective_V":obs,
              "observed_raw_effective_V":raw_obs
            })
        else:
            vals=rr.reshape(-1)
            obs=float(np.mean(aa))
            raw_obs=float(np.mean(vals))
            blocks.append({
              "field_raw_T":float(np.mean(ff)),
              "raw_V":vals,
              "observed_avg_effective_V":obs,
              "observed_raw_effective_V":raw_obs
            })
        j+=p2
    meta={
      "field_shape":list(field.shape),
      "avg_voltage_shape":list(avg.shape),
      "raw_voltage_array_shape":list(raw.shape),
      "repeat_block_P2":int(p2),
      "effective_repeat_count_P":int(p),
      "raw_samples_per_source_row":int(raw.shape[1]),
      "current_inverted":curr_inverted,
      "n_field_blocks":len(blocks),
      "max_abs_raw_vs_avg_effective_V":float(max(abs(b["observed_raw_effective_V"]-b["observed_avg_effective_V"]) for b in blocks))
    }
    return blocks,meta

def curve(blocks,rng=None,use_raw_mean=False):
    field=[]; vals=[]
    for b in blocks:
        field.append(b["field_raw_T"]*8000/93.17)
        if rng is None:
            v=b["observed_raw_effective_V"] if use_raw_mean else b["observed_avg_effective_V"]
        elif "pos_raw_V" in b:
            pos=b["pos_raw_V"]; neg=b["neg_raw_V"]
            v=float(np.mean(rng.choice(pos,size=len(pos),replace=True))-np.mean(rng.choice(neg,size=len(neg),replace=True)))
        else:
            x=b["raw_V"]
            v=float(np.mean(rng.choice(x,size=len(x),replace=True)))
        vals.append(v*1e6)
    field=np.asarray(field,float); v=np.asarray(vals,float)
    amp=(np.max(v)-np.min(v))/2
    if amp<=0:return None
    off=(np.max(v)+np.min(v))/2
    vn=(v-off)/amp
    c=coercive(field,vn)
    if c is None:return None
    c1,c2=c
    return {"c1":c1,"c2":c2,"heb":(c1+c2)/2,"width":(abs(c1)+abs(c2))/2}

def bootstrap_loop(path,B,seed):
    blocks,meta=load_blocks(path)
    obs_avg=curve(blocks,None,False)
    obs_raw=curve(blocks,None,True)
    if obs_avg is None or obs_raw is None: raise RuntimeError("observed coercivity failed")
    rng=np.random.default_rng(seed)
    a=[]
    for _ in range(B):
        z=curve(blocks,rng)
        if z is not None and np.isfinite(z["heb"]):
            a.append(z["heb"])
    x=np.asarray(a,float)
    if len(x)<max(100,int(0.9*B)): raise RuntimeError("too many bootstrap failures")
    q=np.quantile(x,[0.005,0.025,0.5,0.975,0.995])
    sd=float(np.std(x,ddof=1))
    skew=None if sd==0 else float(np.mean(((x-np.mean(x))/np.std(x,ddof=0))**3))
    return {
      "observed_source_avg":obs_avg,
      "observed_recomputed_raw_mean":obs_raw,
      "abs_HEB_difference_raw_vs_source_mT":float(abs(obs_raw["heb"]-obs_avg["heb"])),
      "bootstrap_B_requested":B,
      "bootstrap_B_valid":int(len(x)),
      "bootstrap_mean_HEB_mT":float(np.mean(x)),
      "bootstrap_sd_HEB_mT":sd,
      "bootstrap_quantiles_HEB_mT":{"q005":float(q[0]),"q025":float(q[1]),"q500":float(q[2]),"q975":float(q[3]),"q995":float(q[4])},
      "bootstrap_skewness":skew,
      "zero_in_95pct_percentile_interval":bool(q[1]<=0<=q[3]),
      "raw_structure":meta
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-root",type=Path,required=True)
    ap.add_argument("--out-dir",type=Path,required=True)
    ap.add_argument("--bootstrap",type=int,default=5000)
    ap.add_argument("--seed",type=int,default=36001109)
    a=ap.parse_args(); a.out_dir.mkdir(parents=True,exist_ok=True)
    source=a.source_root/"data"/"Training effect"
    loops=[]
    for i,(fn,label) in enumerate(FILES):
        z=bootstrap_loop(source/fn,a.bootstrap,a.seed+i)
        z.update({"label":label,"file":fn})
        loops.append(z)
    result={
      "status":"PASS_HGMF_HG36_RAW_VOLTAGE_BOOTSTRAP_EXECUTED",
      "source":"sadityakr/EB-in-FGT_CrSBr-vdW-heterostructure@66662e8aa3690cebaaef52dfc4ddd3bea458a576",
      "method":"nonparametric bootstrap of the five raw nanovoltmeter samples inside each current-polarity source row; positive/negative current halves resampled independently; full Vxy normalization and coercive interpolation recomputed per replicate",
      "loops":loops,
      "loop1_zero_excluded_95pct":bool(not loops[0]["zero_in_95pct_percentile_interval"]),
      "loops2_5_zero_included_95pct":[bool(x["zero_in_95pct_percentile_interval"]) for x in loops[1:]],
      "all_trained_loops_zero_compatible_95pct":bool(all(x["zero_in_95pct_percentile_interval"] for x in loops[1:])),
      "calibration_authority":"EMPIRICAL_NONPARAMETRIC_BOOTSTRAP_NOT_EXACT_FINITE_SAMPLE",
      "claim_boundary":"raw repeated-voltage bootstrap supplies a defensible empirical sampling distribution for HEB but does not itself provide exact HG31 e-value authority"
    }
    (a.out_dir/"HGMF_HG36_MAGNETIC_RAW_BOOTSTRAP.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":main()
