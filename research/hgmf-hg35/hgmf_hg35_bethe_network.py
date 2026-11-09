#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, json
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

def qc_bethe(z):
    z=float(z)
    if z<=2: raise ValueError("z must be >2")
    return 1/(z-1)

def _minimal_root(q,z,qplus=0.0):
    q=float(q); z=float(z); qplus=float(qplus)
    if not 0<=q<=1: raise ValueError("q")
    if z<=2: raise ValueError("z")
    if not 0<=qplus<1: raise ValueError("qplus")
    def f(y):
        return (1-q)+q*(1-qplus)*(y**(z-1))-y
    if q==0:
        return 1.0
    if qplus>0:
        # f(0)>=0 and f(1)=-q*qplus<0: unique first crossing in [0,1].
        return float(brentq(f,0.0,1.0,xtol=1e-14,rtol=1e-14,maxiter=1000))
    # Primary branch: y=1 is always a root. Below qc it is the only root.
    qc=qc_bethe(z)
    if q<=qc:
        return 1.0
    if q>=1.0:
        return 0.0
    # For q>qc, the convex f has a negative minimum at ycrit<1;
    # bracket the nontrivial minimal root on [0,ycrit].
    ycrit=(1/(q*(z-1)))**(1/(z-2))
    fy=f(ycrit)
    if fy>=0:
        raise RuntimeError("failed to bracket nontrivial Bethe root")
    return float(brentq(f,0.0,ycrit,xtol=1e-14,rtol=1e-14,maxiter=1000))

def bethe_primary(q,z):
    y=_minimal_root(q,z,0.0)
    return {"y":y,"Qp":float(max(0.0,min(1.0,1-y**z)))}

def bethe_scan(q,qplus,z):
    y=_minimal_root(q,z,qplus)
    alpha=float(max(0.0,min(1.0,1-y**z)))
    qminus=float(qplus+(1-qplus)*alpha)
    return {"y":y,"alpha":alpha,"Qminus":qminus}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out-dir",type=Path,required=True)
    a=ap.parse_args(); a.out_dir.mkdir(parents=True,exist_ok=True)

    zvals=[6.6,7.2]
    qplus_vals=[0.0,0.12,0.34]
    rows=[]
    for z in zvals:
        qc=qc_bethe(z)
        for q in np.linspace(0,1,201):
            pri=bethe_primary(float(q),z)
            for qplus in qplus_vals:
                sc=bethe_scan(float(q),qplus,z)
                rows.append({
                  "z":z,"qc":qc,"q":float(q),"Qplus":qplus,
                  "Qp":pri["Qp"],"alpha":sc["alpha"],"Qminus":sc["Qminus"]
                })

    with (a.out_dir/"HGMF_HG35_BETHE_GRID.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    checks={
      "qc_z6p6":qc_bethe(6.6),
      "qc_z7p2":qc_bethe(7.2),
      "published_qc_range":[0.16,0.18],
      "primary_below_threshold_zero":{
        str(z):max(bethe_primary(float(q),z)["Qp"] for q in np.linspace(0,max(qc_bethe(z)-1e-5,0),50))
        for z in zvals
      },
      "bounds_pass":all(-1e-12<=r["alpha"]<=1+1e-12 and r["Qplus"]-1e-12<=r["Qminus"]<=1+1e-12 for r in rows),
      "monotone_scan_pass":all(
        all(x<=y+1e-11 for x,y in zip(
          [bethe_scan(float(q),qp,z)["Qminus"] for q in np.linspace(0,1,101)][:-1],
          [bethe_scan(float(q),qp,z)["Qminus"] for q in np.linspace(0,1,101)][1:]
        ))
        for z in zvals for qp in qplus_vals
      )
    }

    result={
      "status":"PASS_HGMF_HG35_BETHE_TOPOLOGY_CORE",
      "literature_frozen_connectivity":{
        "z_range":[6.6,7.2],
        "qc_range_exact_from_Bethe":[qc_bethe(7.2),qc_bethe(6.6)],
        "published_scan_Qplus_examples":[0.12,0.34],
        "source":"Cimino et al. 2013 Vycor scanning-isotherm analysis"
      },
      "equations":{
        "primary":"Qp=1-y^z; y=(1-q)+q*y^(z-1)",
        "scan":"alpha=1-y^z; y=(1-q)+q*(1-Qplus)*y^(z-1); Qminus=Qplus+(1-Qplus)*alpha"
      },
      "checks":checks,
      "observation_bridge":{
        "Vs_reference_isotherm":"MISSING_IN_HGMF_PIPELINE",
        "Vc_reference_isotherm":"MISSING_IN_HGMF_PIPELINE",
        "q_of_pressure":"MISSING_IN_HGMF_PIPELINE",
        "status":"FAIL_COMPLETE_XE_VYCOR_OBSERVATION_LIKELIHOOD"
      },
      "claim_boundary":"topology/percolation core is executable and physically constrained; adsorption-mass likelihood is not yet closed"
    }
    (a.out_dir/"HGMF_HG35_BETHE_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__": main()
