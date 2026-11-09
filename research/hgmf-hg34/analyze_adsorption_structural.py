#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re
from pathlib import Path
import numpy as np
import pandas as pd

RUNS=(5,8,9,10)
DIGIT_SCALE_MG=0.01

def monotonic_reversals(x):
    x=np.asarray(x,float)
    d=np.sign(np.diff(x))
    for i in range(1,len(d)):
        if d[i]==0:d[i]=d[i-1]
    for i in range(len(d)-2,-1,-1):
        if d[i]==0:d[i]=d[i+1]
    return [i+1 for i in range(len(d)-1) if d[i]*d[i+1]<0]

def interpolate_crossing(p,y,u,target):
    p=np.asarray(p,float); y=np.asarray(y,float); u=np.asarray(u,float)
    for i in range(len(p)-1):
        a,b=float(p[i]),float(p[i+1])
        if target==a:
            return float(y[i]),float(u[i])*DIGIT_SCALE_MG,i,0.0
        if (a-target)*(b-target)<=0 and a!=b:
            t=(target-a)/(b-a)
            if -1e-12<=t<=1+1e-12:
                yy=(1-t)*y[i]+t*y[i+1]
                # Conservative propagation of quoted absolute last-digit uncertainty.
                uu=(1-t)*u[i]+t*u[i+1]
                return float(yy),float(uu)*DIGIT_SCALE_MG,i,float(t)
    if len(p) and target==float(p[-1]):
        return float(y[-1]),float(u[-1])*DIGIT_SCALE_MG,len(p)-1,0.0
    return None

def immediate_rpm_closures(run,p,y,u):
    p=np.asarray(p,float); y=np.asarray(y,float); u=np.asarray(u,float)
    rev=monotonic_reversals(p)
    span=max(float(np.max(y)-np.min(y)),1e-12)
    rows=[]
    # A genuine immediate closure is reversal r_i -> reversal r_{i+1} -> crossing back through p[r_i]
    # before the next reversal.
    for i in range(len(rev)-1):
        r0=rev[i]; r1=rev[i+1]
        r2=rev[i+2] if i+2<len(rev) else len(p)-1
        target=float(p[r0])
        seg_p=p[r1:r2+1]
        if len(seg_p)<2 or target < float(np.min(seg_p))-1e-12 or target > float(np.max(seg_p))+1e-12:
            continue
        hit=interpolate_crossing(seg_p,y[r1:r2+1],u[r1:r2+1],target)
        if hit is None:continue
        yret,uret,j,t=hit
        err=abs(yret-float(y[r0]))
        u0=float(u[r0])*DIGIT_SCALE_MG
        # Include one final-digit rounding unit across the two compared values.
        envelope=u0+uret+DIGIT_SCALE_MG
        rows.append({
          "run_id":run,
          "reversal_index":int(r0),"inner_reversal_index":int(r1),
          "return_segment_stop":int(r2),
          "return_pressure":target,
          "y_at_reversal_mg":float(y[r0]),"y_on_return_mg":yret,
          "closure_error_mg":err,
          "closure_error_fraction_span":err/span,
          "quoted_uncertainty_reversal_mg":u0,
          "quoted_uncertainty_return_mg":uret,
          "compatibility_envelope_mg":envelope,
          "within_quoted_uncertainty_envelope":bool(err<=envelope+1e-12)
        })
    return rows

def parse_limits(desc):
    if "limit" not in desc.lower(): return None
    vals=re.findall(r"\(\s*([0-9]+(?:\.[0-9]+)?)\s*,",desc)
    if len(vals)<2:return None
    a,b=float(vals[0]),float(vals[1])
    return tuple(sorted((round(a,4),round(b,4))))

def monotonic_segment(g):
    p=g.pressure.to_numpy(float)
    if len(p)<2:return 0
    d=np.sign(np.diff(p)); nz=d[d!=0]
    if len(nz)==0:return 0
    if np.all(nz>0):return 1
    if np.all(nz<0):return -1
    return 0

def interp_curve(g,grid):
    p=g.pressure.to_numpy(float); y=g.adsorption.to_numpy(float)
    o=np.argsort(p)
    return np.interp(grid,p[o],y[o])

def interp_rmse(g1,g2,grid_n=101):
    p1=g1.pressure.to_numpy(float); p2=g2.pressure.to_numpy(float)
    lo=max(float(p1.min()),float(p2.min())); hi=min(float(p1.max()),float(p2.max()))
    if hi<=lo:return None
    grid=np.linspace(lo,hi,grid_n)
    z1=interp_curve(g1,grid); z2=interp_curve(g2,grid)
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
            lim=parse_limits(desc); direction=monotonic_segment(g)
            if lim is None or direction==0:continue
            groups.setdefault((lim,direction),[]).append((int(sid),g))
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

def summarize(rows,key):
    if not rows:return {"n":0}
    a=np.array([r[key] for r in rows],float)
    return {"n":len(rows),"mean":float(a.mean()),"median":float(np.median(a)),"max":float(a.max()),"min":float(a.min())}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--csv",type=Path,required=True); ap.add_argument("--out-dir",type=Path,required=True)
    a=ap.parse_args(); a.out_dir.mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(a.csv)
    d=df[df.run_id.isin(RUNS)].copy()
    closures=[]
    for run,g in d.groupby("run_id",sort=True):
        closures.extend(immediate_rpm_closures(
          int(run),
          g.pressure.to_numpy(float),
          g.adsorption.to_numpy(float),
          g.uncertainty.fillna(0).to_numpy(float)
        ))
    cong=congruency_audit(d)
    pd.DataFrame(closures).to_csv(a.out_dir/"HGMF_HG34_ADSORPTION_RPM_CLOSURES.csv",index=False)
    pd.DataFrame(cong).to_csv(a.out_dir/"HGMF_HG34_ADSORPTION_CONGRUENCY.csv",index=False)
    per_run={}
    for run in RUNS:
        rr=[x for x in closures if x["run_id"]==run]
        compat=sum(bool(x["within_quoted_uncertainty_envelope"]) for x in rr)
        per_run[str(run)]={
          "points":int((d.run_id==run).sum()),
          "immediate_RPM_closures":len(rr),
          "quoted_uncertainty_compatible":compat,
          "quoted_uncertainty_incompatible":len(rr)-compat,
          "closure_error_fraction_span":summarize(rr,"closure_error_fraction_span"),
          "closure_error_mg":summarize(rr,"closure_error_mg")
        }
    incompatible=[x for x in closures if not x["within_quoted_uncertainty_envelope"]]
    result={
      "status":"PASS_HGMF_HG34_ADSORPTION_STRUCTURAL_AUDIT_EXECUTED",
      "source":"NIST-ISODB/AJBrownThesisIsotherms@17a48e5d3c00e97387d0dfb1e280d8d6bf103d40",
      "runs":list(RUNS),
      "per_run":per_run,
      "immediate_RPM_closures_total":len(closures),
      "quoted_uncertainty_compatible_total":len(closures)-len(incompatible),
      "quoted_uncertainty_incompatible_total":len(incompatible),
      "closure_error_fraction_span":summarize(closures,"closure_error_fraction_span"),
      "closure_error_mg":summarize(closures,"closure_error_mg"),
      "congruency_pairs":len(cong),
      "congruency_rmse_mg":summarize(cong,"rmse_mg"),
      "digitized_RPM_with_quoted_last_digit_uncertainty":"FAIL" if incompatible else ("PASS" if closures else "ABSTAIN_NO_CLOSURES"),
      "physical_IDT_RPM_rejection":"HOLD_UNCERTAINTY_IS_TABULAR_LAST_DIGIT_NOT_A_FULL_STOCHASTIC_MEASUREMENT_MODEL",
      "congruency_claim":"DESCRIPTIVE_ONLY_NO_PREREGISTERED_STOCHASTIC_NOISE_MODEL",
      "wiping_out_claim":"ABSTAIN_NO_COUNTERFACTUAL_PARENT_BRANCH_OBSERVED_AFTER_REJOIN",
      "claim_boundary":"only immediate reversal-return closures are treated as RPM constraints; no arbitrary equal-pressure extrema are classified as return points"
    }
    (a.out_dir/"HGMF_HG34_ADSORPTION_STRUCTURAL_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":main()
