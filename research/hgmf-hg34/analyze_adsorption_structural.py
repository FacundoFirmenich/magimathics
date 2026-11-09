#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, re
from pathlib import Path
import numpy as np
import pandas as pd

RUNS=(5,8,9,10)

def monotonic_reversals(x):
    x=np.asarray(x,float)
    d=np.sign(np.diff(x))
    # carry through zero increments
    for i in range(1,len(d)):
        if d[i]==0:d[i]=d[i-1]
    for i in range(len(d)-2,-1,-1):
        if d[i]==0:d[i]=d[i+1]
    rev=[i+1 for i in range(len(d)-1) if d[i]*d[i+1]<0]
    return rev

def return_point_audit(run, p, y):
    rev=monotonic_reversals(p)
    idx=[0]+rev+[len(p)-1]
    step=float(np.median(np.abs(np.diff(p)))) if len(p)>1 else 0.0
    tol=max(step*1.5,(float(np.max(p))-float(np.min(p)))*1e-4)
    span=max(float(np.max(y)-np.min(y)),1e-12)
    rows=[]
    for a in range(len(idx)):
        for b in range(a+2,len(idx)):
            ia,ib=idx[a],idx[b]
            dp=abs(float(p[ia]-p[ib]))
            if dp<=tol:
                dy=abs(float(y[ia]-y[ib]))
                rows.append({
                  "run_id":run,"endpoint_a":ia,"endpoint_b":ib,
                  "p_a":float(p[ia]),"p_b":float(p[ib]),"pressure_error":dp,
                  "y_a":float(y[ia]),"y_b":float(y[ib]),
                  "return_error_mg":dy,
                  "return_error_fraction_span":dy/span,
                  "tol_pressure":tol,
                  "reversal_separation":b-a
                })
    return rows

def parse_limits(desc):
    # Extract pressure coordinate from first two '(pressure, adsorption...)' tuples after 'limits'.
    if "limit" not in desc.lower():
        return None
    vals=re.findall(r"\(\s*([0-9]+(?:\.[0-9]+)?)\s*,",desc)
    if len(vals)<2:return None
    a,b=float(vals[0]),float(vals[1])
    return tuple(sorted((round(a,4),round(b,4))))

def monotonic_segment(g):
    p=g.pressure.to_numpy(float)
    if len(p)<2:return 0
    d=np.sign(np.diff(p))
    nz=d[d!=0]
    if len(nz)==0:return 0
    if np.all(nz>0):return 1
    if np.all(nz<0):return -1
    return 0

def interp_rmse(g1,g2,grid_n=101):
    p1=g1.pressure.to_numpy(float); y1=g1.adsorption.to_numpy(float)
    p2=g2.pressure.to_numpy(float); y2=g2.adsorption.to_numpy(float)
    o1=np.argsort(p1); o2=np.argsort(p2); p1,y1=p1[o1],y1[o1]; p2,y2=p2[o2],y2[o2]
    lo=max(float(p1.min()),float(p2.min())); hi=min(float(p1.max()),float(p2.max()))
    if hi<=lo:return None
    grid=np.linspace(lo,hi,grid_n)
    z1=np.interp(grid,p1,y1); z2=np.interp(grid,p2,y2)
    diff=z1-z2
    return {
      "overlap_lo":lo,"overlap_hi":hi,
      "rmse_mg":float(np.sqrt(np.mean(diff**2))),
      "mae_mg":float(np.mean(np.abs(diff))),
      "max_abs_mg":float(np.max(np.abs(diff))),
      "mean_signed_mg":float(np.mean(diff))
    }

def congruency_audit(df):
    rows=[]
    for run in RUNS:
        d=df[df.run_id==run]
        groups={}
        for sid,g in d.groupby("segment_id",sort=True):
            desc=str(g.segment_description.iloc[0])
            lim=parse_limits(desc)
            direction=monotonic_segment(g)
            if lim is None or direction==0:continue
            key=(lim,direction)
            groups.setdefault(key,[]).append((int(sid),g))
        for (lim,direction),items in groups.items():
            if len(items)<2:continue
            for i in range(len(items)):
                for j in range(i+1,len(items)):
                    ans=interp_rmse(items[i][1],items[j][1])
                    if ans is None:continue
                    ans.update({
                      "run_id":run,"limit_lo":lim[0],"limit_hi":lim[1],
                      "direction":"adsorption" if direction>0 else "desorption",
                      "segment_a":items[i][0],"segment_b":items[j][0]
                    })
                    rows.append(ans)
    return rows

def run8_rejoin_audit(df):
    d=df[df.run_id==8]
    # Map explicitly numbered adsorption scanning curves to source segments.
    targets={}
    for sid,g in d.groupby("segment_id",sort=True):
        desc=str(g.segment_description.iloc[0])
        m=re.search(r"Adsorption Scanning Curve\s+(\d+)",desc,re.I)
        if m and "from" in desc.lower():
            targets[int(m.group(1))]=g
    rows=[]
    for sid,g in d.groupby("segment_id",sort=True):
        desc=str(g.segment_description.iloc[0])
        m=re.search(r"returning to Adsorption Scanning Curve\s+(\d+)",desc,re.I)
        if not m:continue
        target=int(m.group(1))
        if target not in targets:continue
        lim=parse_limits(desc)
        if lim is None:continue
        upper=lim[1]
        # after the loop closes at the upper reversal, compare continuation to target curve.
        gg=g[g.pressure>=upper-1e-12].copy()
        if len(gg)<2:continue
        ans=interp_rmse(gg,targets[target])
        if ans is None:continue
        ans.update({"run_id":8,"segment_id":int(sid),"target_curve":target,"return_upper_pressure":upper})
        rows.append(ans)
    return rows

def summarize(rows,key):
    if not rows:return {"n":0}
    a=np.array([r[key] for r in rows],float)
    return {"n":len(rows),"mean":float(a.mean()),"median":float(np.median(a)),"max":float(a.max()),"min":float(a.min())}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--csv",type=Path,required=True); ap.add_argument("--out-dir",type=Path,required=True)
    a=ap.parse_args(); a.out_dir.mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(a.csv)
    d=df[df.run_id.isin(RUNS)].copy()
    ret=[]
    for run,g in d.groupby("run_id",sort=True):
        ret.extend(return_point_audit(int(run),g.pressure.to_numpy(float),g.adsorption.to_numpy(float)))
    cong=congruency_audit(d)
    rejoin=run8_rejoin_audit(d)
    pd.DataFrame(ret).to_csv(a.out_dir/"HGMF_HG34_ADSORPTION_RETURN_POINTS.csv",index=False)
    pd.DataFrame(cong).to_csv(a.out_dir/"HGMF_HG34_ADSORPTION_CONGRUENCY.csv",index=False)
    pd.DataFrame(rejoin).to_csv(a.out_dir/"HGMF_HG34_ADSORPTION_REJOIN.csv",index=False)
    per_run={}
    for run in RUNS:
        rr=[x for x in ret if x["run_id"]==run]
        per_run[str(run)]={
          "points":int((d.run_id==run).sum()),
          "return_pairs":len(rr),
          "return_error_fraction_span":summarize(rr,"return_error_fraction_span"),
          "return_error_mg":summarize(rr,"return_error_mg")
        }
    result={
      "status":"PASS_HGMF_HG34_ADSORPTION_STRUCTURAL_AUDIT_EXECUTED",
      "source":"NIST-ISODB/AJBrownThesisIsotherms@17a48e5d3c00e97387d0dfb1e280d8d6bf103d40",
      "runs":list(RUNS),
      "per_run":per_run,
      "return_points_global_fraction_span":summarize(ret,"return_error_fraction_span"),
      "return_points_global_mg":summarize(ret,"return_error_mg"),
      "congruency_pairs":len(cong),
      "congruency_rmse_mg":summarize(cong,"rmse_mg"),
      "run8_explicit_rejoin_tests":len(rejoin),
      "run8_rejoin_rmse_mg":summarize(rejoin,"rmse_mg"),
      "exact_digitized_RPM":"FAIL" if any(r["return_error_mg"]>0.0100001 for r in ret) else ("PASS" if ret else "ABSTAIN"),
      "noise_aware_RPM":"ABSTAIN_NO_STATISTICAL_UNCERTAINTY_MODEL",
      "congruency_claim":"DESCRIPTIVE_ONLY_NO_PREREGISTERED_NOISE_TOLERANCE",
      "wiping_out_rejoin_claim":"DESCRIPTIVE_ONLY_NO_PREREGISTERED_NOISE_TOLERANCE",
      "claim_boundary":"digitized exact identities can be tested; physical IDT rejection requires a measurement/noise model or a model-specific likelihood"
    }
    (a.out_dir/"HGMF_HG34_ADSORPTION_STRUCTURAL_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":main()
