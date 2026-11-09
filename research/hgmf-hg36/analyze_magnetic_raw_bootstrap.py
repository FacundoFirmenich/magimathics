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
    if len(c)>=2:
        return c[0],c[1]
    return None

def aggregate_blocks(path):
    with h5py.File(path) as f:
        field=np.asarray(f["Data"]["Magnetic_Field"],float)
        avg=np.asarray(f["Data"]["Avg_Voltage_Hp34420A_Ch1"],float)
        raw=np.asarray(f["Data"]["Voltage_Array_Hp34420A_Ch1"])
    i=0
    while i+1<len(field) and abs(field[i]-field[i+1])<0.01:
        i+=1
    p2=i+1
    if p2<1: raise ValueError("invalid repeat block")
    curr_inverted=bool(avg[0]*avg[1]<0)
    p=round(p2/2) if curr_inverted else p2
    blocks=[]
    j=0
    while j<len(field):
        stop=min(j+p2,len(field))
        if stop-j < p2: break
        ff=field[j:stop]
        aa=avg[j:stop]
        if curr_inverted:
            eff=aa[:p]-aa[p:p2]
            if len(eff)!=p: raise ValueError("current inversion pairing")
        else:
            eff=aa.copy()
        blocks.append({
          "field_raw_T":float(np.mean(ff)),
          "effective_row_voltages_V":np.asarray(eff,float),
          "n_effective_rows":int(len(eff))
        })
        j+=p2
    return blocks, {
      "field_shape":list(field.shape),
      "avg_voltage_shape":list(avg.shape),
      "raw_voltage_array_shape":list(raw.shape),
      "repeat_block_P2":int(p2),
      "effective_repeat_count_P":int(p),
      "current_inverted":curr_inverted
    }

def curve_from_blocks(blocks, rng=None):
    field=[]; v=[]
    for b in blocks:
        vals=b["effective_row_voltages_V"]
        if rng is None:
            vv=float(np.mean(vals))
        else:
            vv=float(np.mean(rng.choice(vals,size=len(vals),replace=True)))
        field.append(b["field_raw_T"]*8000/93.17)
        v.append(vv*1e6)
    field=np.asarray(field,float); v=np.asarray(v,float)
    off=(np.max(v)+np.min(v))/2
    amp=(np.max(v)-np.min(v))/2
    if amp<=0:return None
    vn=(v-off)/amp
    c=coercive(field,vn)
    if c is None:return None
    c1,c2=c
    return {"c1":c1,"c2":c2,"heb":(c1+c2)/2,"width":(abs(c1)+abs(c2))/2}

def bootstrap_loop(path,B,seed):
    blocks,meta=aggregate_blocks(path)
    obs=curve_from_blocks(blocks,None)
    if obs is None: raise RuntimeError("observed coercivity failed")
    rng=np.random.default_rng(seed)
    vals=[]
    for _ in range(B):
        z=curve_from_blocks(blocks,rng)
        if z is not None and np.isfinite(z["heb"]):
            vals.append(z["heb"])
    a=np.asarray(vals,float)
    if len(a)<max(100,int(0.9*B)):
        raise RuntimeError("too many bootstrap failures")
    q=np.quantile(a,[0.005,0.025,0.5,0.975,0.995])
    return {
      "observed":obs,
      "bootstrap_B_requested":B,
      "bootstrap_B_valid":int(len(a)),
      "bootstrap_mean_HEB_mT":float(np.mean(a)),
      "bootstrap_sd_HEB_mT":float(np.std(a,ddof=1)),
      "bootstrap_quantiles_HEB_mT":{
        "q005":float(q[0]),"q025":float(q[1]),"q500":float(q[2]),"q975":float(q[3]),"q995":float(q[4])
      },
      "bootstrap_skewness":float(np.mean(((a-np.mean(a))/np.std(a,ddof=0))**3)),
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
      "method":"nonparametric resampling of repeated effective row-average Hall voltages inside each source-loader field block; coercive interpolation recomputed per replicate",
      "loops":loops,
      "loop1_zero_excluded_95pct":bool(not loops[0]["zero_in_95pct_percentile_interval"]),
      "loops2_5_zero_included_95pct":[bool(x["zero_in_95pct_percentile_interval"]) for x in loops[1:]],
      "all_trained_loops_zero_compatible_95pct":bool(all(x["zero_in_95pct_percentile_interval"] for x in loops[1:])),
      "calibration_authority":"EMPIRICAL_BOOTSTRAP_ONLY_NOT_EXACT_FINITE_SAMPLE",
      "claim_boundary":"bootstrap quantifies repeated-voltage uncertainty but does not create exact universal-evalue authority"
    }
    (a.out_dir/"HGMF_HG36_MAGNETIC_RAW_BOOTSTRAP.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":main()
