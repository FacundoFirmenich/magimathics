#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, re
from pathlib import Path
import numpy as np
import pandas as pd

BOUNDARY_RUN=15
CALIBRATION_RUN=1
AUDIT_RUNS=(1,5,8,9,10)
DIGIT_SCALE_MG=0.01

def fit_vc_candidates(boundary):
    d=boundary[boundary.branch=="D"].sort_values("pressure",ascending=False)
    p=d.pressure.to_numpy(float); y=d.adsorption.to_numpy(float)
    ends=[i for i,x in enumerate(p) if x>=0.5445 and i+1>=5]
    out=[]
    for end in ends:
        pp=p[:end+1]; yy=y[:end+1]
        X=np.column_stack([np.ones(len(pp)),pp-1.0])
        beta=np.linalg.lstsq(X,yy,rcond=None)[0]
        pred=X@beta
        out.append({
          "end_pressure":float(pp[-1]),"n_fit":len(pp),
          "intercept_at_p1":float(beta[0]),"slope":float(beta[1]),
          "rmse_mg":float(np.sqrt(np.mean((pred-yy)**2)))
        })
    return out

def vc_eval(c,p):
    p=np.asarray(p,float)
    return c["intercept_at_p1"]+c["slope"]*(p-1.0)

def lower_closure_anchor(boundary):
    a=boundary[(boundary.branch=="A")&(boundary.pressure<=0.45)]
    d=boundary[(boundary.branch=="D")&(boundary.pressure<=0.45)]
    best=None
    for _,ra in a.iterrows():
        for _,rd in d.iterrows():
            dp=abs(float(ra.pressure-rd.pressure))
            dy=abs(float(ra.adsorption-rd.adsorption))
            score=dp/0.01+dy/0.1
            if best is None or score<best[0]:
                best=(score,ra,rd)
    if best is None: raise RuntimeError("no lower closure anchor")
    _,ra,rd=best
    return {
      "p":float((ra.pressure+rd.pressure)/2),
      "V":float((ra.adsorption+rd.adsorption)/2),
      "A_point":[float(ra.pressure),float(ra.adsorption)],
      "D_point":[float(rd.pressure),float(rd.adsorption)]
    }

def interp_adsorption(boundary,p):
    a=boundary[boundary.branch=="A"].sort_values("pressure")
    x=a.pressure.to_numpy(float); y=a.adsorption.to_numpy(float)
    return np.interp(np.asarray(p,float),x,y)

def reference_Q_interval(boundary,vc_candidates,p,v):
    p=float(p); v=float(v)
    anchor=lower_closure_anchor(boundary)
    # With no external nonporous reference, only order constraints are warranted:
    # film adsorption is monotone, so above lower closure Vs >= V(A);
    # and film contribution cannot exceed the observed adsorption boundary.
    vs_lo=anchor["V"] if p>=anchor["p"] else float(interp_adsorption(boundary,[p])[0])
    vs_hi=float(interp_adsorption(boundary,[p])[0])
    vals=[]
    for vc in vc_candidates:
        vc0=float(vc_eval(vc,[p])[0])
        for vs0 in (vs_lo,vs_hi):
            den=vc0-vs0
            if den<=0:continue
            q=(vc0-v)/den
            if -0.05<=q<=1.05:
                vals.append(float(np.clip(q,0,1)))
    if not vals:return None
    return {"Q_lo":min(vals),"Q_hi":max(vals),"width":max(vals)-min(vals),"Vs_lo":vs_lo,"Vs_hi":vs_hi}

def parse_start(desc):
    m=re.search(r"starting from\s*\(\s*([0-9.]+)\s*,\s*([0-9.]+)",str(desc),re.I)
    return (float(m.group(1)),float(m.group(2))) if m else None

def q_from_Q(Qp,Qm,z):
    if not (0<=Qp<1 and Qp<=Qm<=1):return None
    alpha=(Qm-Qp)/(1-Qp)
    if not 0<=alpha<=1:return None
    y=(1-alpha)**(1/z)
    den=1-(1-Qp)*y**(z-1)
    if abs(den)<1e-14:return None
    q=(1-y)/den
    return float(q) if -1e-9<=q<=1+1e-9 else None

def calibration_q_intervals(scans,boundary,vcs):
    d=scans[scans.run_id==CALIBRATION_RUN]
    rows=[]
    for sid,g in d.groupby("segment_id",sort=True):
        if str(g.branch.iloc[0])!="D":continue
        start=parse_start(g.segment_description.iloc[0])
        if start is None:continue
        p0,v0=start
        qp=reference_Q_interval(boundary,vcs,p0,v0)
        if qp is None:continue
        for idx,r in g.iterrows():
            qm=reference_Q_interval(boundary,vcs,float(r.pressure),float(r.adsorption))
            if qm is None:continue
            qs=[]
            for Qp in (qp["Q_lo"],qp["Q_hi"]):
                for Qm in (qm["Q_lo"],qm["Q_hi"]):
                    for z in (6.6,6.9,7.2):
                        q=q_from_Q(Qp,Qm,z)
                        if q is not None:qs.append(float(np.clip(q,0,1)))
            if qs:
                rows.append({
                  "segment_id":int(sid),"row_index":int(idx),"pressure":float(r.pressure),
                  "q_lo":min(qs),"q_hi":max(qs),"q_width":max(qs)-min(qs),
                  "Qp_lo":qp["Q_lo"],"Qp_hi":qp["Q_hi"],
                  "Qm_lo":qm["Q_lo"],"Qm_hi":qm["Q_hi"]
                })
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--boundary",type=Path,required=True)
    ap.add_argument("--scanning",type=Path,required=True)
    ap.add_argument("--out-dir",type=Path,required=True)
    a=ap.parse_args(); a.out_dir.mkdir(parents=True,exist_ok=True)
    b=pd.read_csv(a.boundary); s=pd.read_csv(a.scanning)
    boundary=b[b.run_id==BOUNDARY_RUN].copy()
    vcs=fit_vc_candidates(boundary)
    anchor=lower_closure_anchor(boundary)

    qrows=[]
    for run in AUDIT_RUNS:
        d=s[s.run_id==run]
        for idx,r in d.iterrows():
            p=float(r.pressure)
            if not (0.45<=p<=0.85):continue
            z=reference_Q_interval(boundary,vcs,p,float(r.adsorption))
            if z is None:continue
            z.update({"run_id":run,"row_index":int(idx),"pressure":p,"adsorption_mg":float(r.adsorption)})
            qrows.append(z)
    qdf=pd.DataFrame(qrows)
    qdf.to_csv(a.out_dir/"HGMF_HG36_VYCOR_Q_INTERVALS.csv",index=False)

    qr=calibration_q_intervals(s,boundary,vcs)
    qrd=pd.DataFrame(qr)
    qrd.to_csv(a.out_dir/"HGMF_HG36_VYCOR_q_INTERVALS_RUN1.csv",index=False)

    result={
      "status":"PASS_HGMF_HG36_SET_VALUED_REFERENCE_IDENTIFIABILITY_AUDIT",
      "boundary_source":"Brown Xe/Vycor boundary run 15, 150.73 K",
      "scan_source_runs":list(AUDIT_RUNS),
      "lower_closure_anchor":anchor,
      "Vc_candidate_count":len(vcs),
      "Vs_external_reference_available":false,
      "Vs_identification":"ORDER_BOUNDS_ONLY: monotone film contribution >= lower-closure loading and <= adsorption-boundary loading",
      "Q_points":int(len(qdf)),
      "Q_median_interval_width":float(qdf.width.median()) if len(qdf) else None,
      "Q_mean_interval_width":float(qdf.width.mean()) if len(qdf) else None,
      "Q_max_interval_width":float(qdf.width.max()) if len(qdf) else None,
      "run1_q_points":int(len(qrd)),
      "q_median_interval_width":float(qrd.q_width.median()) if len(qrd) else None,
      "q_mean_interval_width":float(qrd.q_width.mean()) if len(qrd) else None,
      "q_max_interval_width":float(qrd.q_width.max()) if len(qrd) else None,
      "reference_identifiability":"FAIL_POINT_IDENTIFICATION_WITH_BROWN_DATA_ALONE",
      "external_requirement":"nonporous same-origin Xe/silica film reference or independently calibrated surface-area/FHH reference; plus a stochastic reference-curve uncertainty model",
      "authority":"SET_VALUED_NONIDENTIFIABILITY_RESULT",
      "claim_boundary":"Brown boundary/scanning data alone constrain but do not point-identify Vs, hence Q and q remain set-valued; no adsorption-mass likelihood or HG31 e-value is authorized"
    }
    (a.out_dir/"HGMF_HG36_VYCOR_BRIDGE_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":main()
