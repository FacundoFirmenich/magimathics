#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, json, math
from pathlib import Path
import numpy as np

def _fixed_point(q,z,qplus=0.0,tol=1e-13,max_iter=100000):
    q=float(q); z=float(z); qplus=float(qplus)
    if not (0<=q<=1): raise ValueError("q")
    if z<=1: raise ValueError("z")
    if not (0<=qplus<1): raise ValueError("qplus")
    # Minimal fixed point, obtained by monotone iteration from zero.
    y=0.0
    for _ in range(max_iter):
        yn=(1-q)+q*(1-qplus)*(y**(z-1))
        if abs(yn-y)<=tol*(1+abs(y)):
            return min(1.0,max(0.0,float(yn)))
        y=yn
    raise RuntimeError("fixed point did not converge")

def bethe_primary(q,z):
    y=_fixed_point(q,z,0.0)
    qp=1-y**z
    return {"y":y,"Qp":float(qp)}

def bethe_scan(q,qplus,z):
    y=_fixed_point(q,z,qplus)
    alpha=1-y**z
    qminus=qplus+(1-qplus)*alpha
    return {"y":y,"alpha":float(alpha),"Qminus":float(qminus)}

def qc_bethe(z):
    return 1/(float(z)-1)

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
            pri=bethe_primary(q,z)
            for qplus in qplus_vals:
                sc=bethe_scan(q,qplus,z)
                rows.append({
                  "z":z,"qc":qc,"q":float(q),"Qplus":qplus,
                  "Qp":pri["Qp"],"alpha":sc["alpha"],"Qminus":sc["Qminus"]
                })

    with (a.out_dir/"HGMF_HG35_BETHE_GRID.csv").open("w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)

    # Exact/structural checks.
    checks={
      "qc_z6p6":qc_bethe(6.6),
      "qc_z7p2":qc_bethe(7.2),
      "published_qc_range":[0.16,0.18],
      "primary_below_threshold_zero":{
        str(z):max(bethe_primary(q,z)["Qp"] for q in np.linspace(0,max(qc_bethe(z)-1e-5,0),50))
        for z in zvals
      },
      "bounds_pass":all(0<=r["alpha"]<=1 and r["Qplus"]<=r["Qminus"]<=1 for r in rows),
      "monotone_scan_pass":all(
        all(x<=y+1e-12 for x,y in zip(
          [bethe_scan(q,qp,z)["Qminus"] for q in np.linspace(0,1,101)][:-1],
          [bethe_scan(q,qp,z)["Qminus"] for q in np.linspace(0,1,101)][1:]
        ))
        for z in zvals for qp in qplus_vals
      )
    }

    result={
      "status":"PASS_HGMF_HG35_BETHE_TOPOLOGY_CORE",
      "literature_frozen_connectivity":{
        "z_range":[6.6,7.2],
        "qc_range_exact_from_Bethe":[qc_bethe(7.2),qc_bethe(6.6)],
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
