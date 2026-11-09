#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, re
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import least_squares, brentq
from sklearn.isotonic import IsotonicRegression

BOUNDARY_RUN=15
CALIBRATION_RUN=1
HOLDOUT_RUNS=(5,8,9,10)
DIGIT_SCALE_MG=0.01

def fhh(p,A,m):
    p=np.asarray(p,float)
    return A*np.power(-np.log(np.clip(p,1e-8,1-1e-10)),-1.0/m)

def fit_vs_candidates(boundary):
    a=boundary[boundary.branch=="A"].sort_values("pressure")
    # Exhaust all observed prefixes ending at or below 0.5, with >=5 points.
    ends=[i for i,p in enumerate(a.pressure.to_numpy(float)) if p<=0.5000001 and i+1>=5]
    out=[]
    for end in ends:
        g=a.iloc[:end+1]
        p=g.pressure.to_numpy(float); y=g.adsorption.to_numpy(float)
        def resid(t):
            A=math.exp(t[0]); m=math.exp(t[1])
            return fhh(p,A,m)-y
        fit=least_squares(resid,[math.log(8.0),math.log(2.0)],bounds=([-10,math.log(.2)],[10,math.log(10)]),max_nfev=100000)
        A=math.exp(fit.x[0]); m=math.exp(fit.x[1])
        pred=fhh(p,A,m)
        out.append({
          "kind":"FHH_PREFIX","end_pressure":float(p[-1]),"n_fit":len(p),
          "A":A,"m":m,"rmse_mg":float(np.sqrt(np.mean((pred-y)**2)))
        })
    return out

def fit_vc_candidates(boundary):
    d=boundary[boundary.branch=="D"].sort_values("pressure",ascending=False)
    p=d.pressure.to_numpy(float); y=d.adsorption.to_numpy(float)
    # The published rule extrapolates the reversible upper plateau.
    # Exhaust all prefixes whose final point is still above the sharp evaporation drop (>=0.5446 in Brown run 15).
    ends=[i for i,x in enumerate(p) if x>=0.5445 and i+1>=5]
    out=[]
    for end in ends:
        pp=p[:end+1]; yy=y[:end+1]
        X=np.column_stack([np.ones(len(pp)),pp-1.0])
        beta=np.linalg.lstsq(X,yy,rcond=None)[0]
        pred=X@beta
        out.append({
          "kind":"UPPER_PLATEAU_LINEAR_PREFIX","end_pressure":float(pp[-1]),"n_fit":len(pp),
          "intercept_at_p1":float(beta[0]),"slope_mg_per_relP":float(beta[1]),
          "rmse_mg":float(np.sqrt(np.mean((pred-yy)**2)))
        })
    return out

def vs_eval(c,p):
    return fhh(np.asarray(p,float),c["A"],c["m"])

def vc_eval(c,p):
    p=np.asarray(p,float)
    return c["intercept_at_p1"]+c["slope_mg_per_relP"]*(p-1.0)

def q_fraction(v,p,vs,vc):
    den=vc-vs
    return (vc-v)/den

def references_admissible(boundary,vs,vc):
    # Evaluate only the hysteresis-support interval covered by both branches.
    rows=boundary[(boundary.pressure>=0.45)&(boundary.pressure<=0.85)]
    p=rows.pressure.to_numpy(float); v=rows.adsorption.to_numpy(float)
    lo=vs_eval(vs,p); hi=vc_eval(vc,p)
    if np.any(hi-lo<=0.25): return False
    # Last-digit uncertainty envelope plus 0.02 mg rounding guard.
    u=rows.uncertainty.fillna(0).to_numpy(float)*DIGIT_SCALE_MG+0.02
    return bool(np.all(v>=lo-u) and np.all(v<=hi+u))

def parse_start(desc):
    m=re.search(r"starting from\s*\(\s*([0-9.]+)\s*,\s*([0-9.]+)",str(desc),re.I)
    if not m:return None
    return float(m.group(1)),float(m.group(2))

def q_from_alpha(alpha,Qplus,z):
    if not (0<=alpha<=1 and 0<=Qplus<1): return None
    y=(1-alpha)**(1/z)
    den=1-(1-Qplus)*(y**(z-1))
    if abs(den)<1e-14:return None
    q=(1-y)/den
    return float(q) if -1e-10<=q<=1+1e-10 else None

def bethe_alpha(q,Qplus,z):
    q=float(np.clip(q,0,1))
    def f(y): return (1-q)+q*(1-Qplus)*(y**(z-1))-y
    if q==0:return 0.0
    # Qplus>0 for proper scans: unique crossing [0,1].
    if Qplus>1e-12:
        y=brentq(f,0,1,xtol=1e-13,rtol=1e-13)
    else:
        qc=1/(z-1)
        if q<=qc:return 0.0
        if q>=1:return 1.0
        yc=(1/(q*(z-1)))**(1/(z-2))
        y=brentq(f,0,yc,xtol=1e-13,rtol=1e-13)
    return float(np.clip(1-y**z,0,1))

def calibrate_q(scans,vs,vc,z):
    d=scans[scans.run_id==CALIBRATION_RUN].copy()
    rows=[]
    for sid,g in d.groupby("segment_id",sort=True):
        if str(g.branch.iloc[0])!="D": continue
        start=parse_start(g.segment_description.iloc[0])
        if start is None: continue
        p0,v0=start
        vsv=float(vs_eval(vs,[p0])[0]); vcv=float(vc_eval(vc,[p0])[0])
        if vcv-vsv<=0:return None
        Qp=float(q_fraction(v0,p0,vsv,vcv))
        if not (0<=Qp<0.999):continue
        for _,r in g.iterrows():
            p=float(r.pressure); v=float(r.adsorption)
            vsi=float(vs_eval(vs,[p])[0]); vci=float(vc_eval(vc,[p])[0])
            Qm=float(q_fraction(v,p,vsi,vci))
            alpha=(Qm-Qp)/(1-Qp)
            q=q_from_alpha(alpha,Qp,z)
            if q is not None and 0<=q<=1:
                rows.append((p,q))
    if len(rows)<8:return None
    pp=np.array([r[0] for r in rows]); qq=np.array([r[1] for r in rows])
    # q grows as pressure falls in desorption => isotonic decreasing in p.
    iso=IsotonicRegression(y_min=0,y_max=1,increasing=False,out_of_bounds="clip")
    iso.fit(pp,qq)
    pred=iso.predict(pp)
    return {
      "iso":iso,"n":len(pp),
      "calibration_rmse_q":float(np.sqrt(np.mean((pred-qq)**2))),
      "pmin":float(pp.min()),"pmax":float(pp.max())
    }

def holdout_predictions(scans,vs,vc,z,cal):
    rows=[]
    for run in HOLDOUT_RUNS:
        d=scans[scans.run_id==run].copy()
        # Preserve global order for previous-segment start state.
        for sid,g in d.groupby("segment_id",sort=True):
            if str(g.branch.iloc[0])!="D":continue
            first_idx=g.index.min()
            prev=d.loc[d.index<first_idx].tail(1)
            if len(prev)!=1:continue
            pr=prev.iloc[0]
            # Require a reversal from adsorption into desorption.
            if str(pr.branch)!="A":continue
            p0=float(pr.pressure); v0=float(pr.adsorption)
            vsv=float(vs_eval(vs,[p0])[0]); vcv=float(vc_eval(vc,[p0])[0])
            if vcv-vsv<=0:continue
            Qp=float(q_fraction(v0,p0,vsv,vcv))
            if not (0<=Qp<0.999):continue
            for idx,r in g.iterrows():
                p=float(r.pressure)
                if not (cal["pmin"]<=p<=cal["pmax"]):continue
                q=float(cal["iso"].predict([p])[0])
                alpha=bethe_alpha(q,Qp,z)
                Qm=Qp+(1-Qp)*alpha
                vsi=float(vs_eval(vs,[p])[0]); vci=float(vc_eval(vc,[p])[0])
                vpred=vsi*Qm+(1-Qm)*vci
                rows.append({
                  "run_id":run,"segment_id":int(sid),"row_index":int(idx),
                  "pressure":p,"observed_mg":float(r.adsorption),"predicted_mg":float(vpred),
                  "quoted_uncertainty_mg":float(r.uncertainty if pd.notna(r.uncertainty) else 0)*DIGIT_SCALE_MG,
                  "z":z
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
    vses=fit_vs_candidates(boundary); vces=fit_vc_candidates(boundary)
    pairs=[]
    for i,vs in enumerate(vses):
        for j,vc in enumerate(vces):
            if references_admissible(boundary,vs,vc):
                pairs.append((i,j,vs,vc))
    if not pairs:
        raise RuntimeError("no admissible reference pairs")
    zgrid=np.linspace(6.6,7.2,13)
    ensemble=[]
    calibrations=[]
    for i,j,vs,vc in pairs:
        for z in zgrid:
            cal=calibrate_q(s,vs,vc,float(z))
            if cal is None:continue
            calibrations.append({"vs_id":i,"vc_id":j,"z":float(z),"n":cal["n"],"rmse_q":cal["calibration_rmse_q"]})
            ensemble.extend(holdout_predictions(s,vs,vc,float(z),cal))
    if not ensemble:
        raise RuntimeError("no holdout predictions")
    pred=pd.DataFrame(ensemble)
    key=["run_id","segment_id","row_index","pressure","observed_mg","quoted_uncertainty_mg"]
    agg=pred.groupby(key,as_index=False).predicted_mg.agg(["min","max","median"]).reset_index()
    agg["inside_reference_network_envelope"]=(agg.observed_mg>=agg["min"]-agg.quoted_uncertainty_mg-0.02)&(agg.observed_mg<=agg["max"]+agg.quoted_uncertainty_mg+0.02)
    agg["envelope_width_mg"]=agg["max"]-agg["min"]
    agg["distance_to_envelope_mg"]=np.where(
      agg.observed_mg<agg["min"],agg["min"]-agg.observed_mg,
      np.where(agg.observed_mg>agg["max"],agg.observed_mg-agg["max"],0.0)
    )
    agg.to_csv(a.out_dir/"HGMF_HG36_VYCOR_HOLDOUT_ENVELOPE.csv",index=False)
    pd.DataFrame(calibrations).to_csv(a.out_dir/"HGMF_HG36_VYCOR_CALIBRATIONS.csv",index=False)
    result={
      "status":"PASS_HGMF_HG36_VYCOR_SET_VALUED_BRIDGE_EXECUTED",
      "boundary_source":"xe_boundary_isotherms.csv run 15 at 150.73 K",
      "calibration_source":"xe_scanning_isotherms.csv run 1 at 150.73 K",
      "holdout_runs":list(HOLDOUT_RUNS),
      "holdout_temperature_K":[float(s[s.run_id==r].temperature.iloc[0]) for r in HOLDOUT_RUNS],
      "Vs_candidate_count":len(vses),"Vc_candidate_count":len(vces),
      "admissible_reference_pairs":len(pairs),
      "z_grid":[float(x) for x in zgrid],
      "calibrated_models":len(calibrations),
      "holdout_points_evaluated":int(len(agg)),
      "holdout_inside_envelope":int(agg.inside_reference_network_envelope.sum()),
      "holdout_outside_envelope":int((~agg.inside_reference_network_envelope).sum()),
      "holdout_coverage_fraction":float(agg.inside_reference_network_envelope.mean()),
      "median_envelope_width_mg":float(agg.envelope_width_mg.median()),
      "max_envelope_width_mg":float(agg.envelope_width_mg.max()),
      "max_distance_outside_envelope_mg":float(agg.distance_to_envelope_mg.max()),
      "reference_family":{
        "Vs":"FHH fits over every observed adsorption prefix with >=5 points and endpoint <=0.5",
        "Vc":"linear upper-plateau fits over every observed desorption prefix with >=5 points and endpoint >=0.5445",
        "filter":"references must bracket the Brown run-15 boundary data in 0.45<=p<=0.85 within last-digit uncertainty + 0.02 mg rounding guard"
      },
      "q_calibration":"run-1 desorption scans; exact algebraic inversion followed by isotonic q(p), decreasing with pressure",
      "authority":"SET_VALUED_RETROSPECTIVE_STANDARD_NULL_NOT_PROBABILISTIC_LIKELIHOOD",
      "temperature_transfer_caveat":"calibration/boundary 150.73 K versus heldout runs 151.06-151.12 K; no temperature correction fitted",
      "claim_boundary":"coverage keeps the network null alive; noncoverage cannot by itself reject it without a stochastic reference-curve/temperature model"
    }
    (a.out_dir/"HGMF_HG36_VYCOR_BRIDGE_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":main()
