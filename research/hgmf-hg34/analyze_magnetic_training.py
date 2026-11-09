#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
import numpy as np

FILES=[
 ("01_FC2500mT_20250319_2120__10K.h5","Loop 1"),
 ("02_FC2500mT_20250319_2358__10K.h5","Loop 2"),
 ("03_FC2500mT_20250320_0231__10K.h5","Loop 3"),
 ("04_FC2500mT_20250320_0504__10K.h5","Loop 4"),
 ("05_FC2500mT_20250320_0738__10K.h5","Loop 5"),
]

def field_segments(h):
    h=np.asarray(h,float)
    d=np.sign(np.diff(h))
    for i in range(1,len(d)):
        if d[i]==0:d[i]=d[i-1]
    for i in range(len(d)-2,-1,-1):
        if d[i]==0:d[i]=d[i+1]
    cuts=[0]+[i+1 for i in range(len(d)-1) if d[i]*d[i+1]<0]+[len(h)]
    return [(cuts[i],cuts[i+1]) for i in range(len(cuts)-1) if cuts[i+1]-cuts[i]>=3]

def crossing_field(h,y,level):
    z=y-level
    xs=[]
    for i in range(len(h)-1):
        if z[i]==0:xs.append(float(h[i]))
        elif z[i]*z[i+1]<0:
            den=y[i+1]-y[i]
            if den!=0:
                xs.append(float(h[i]+(level-y[i])*(h[i+1]-h[i])/den))
    if not xs:return None
    return xs[0]

def branch_transition_metrics(h,y):
    rows=[]
    for a,b in field_segments(h):
        hh=np.asarray(h[a:b],float); yy=np.asarray(y[a:b],float)
        if np.nanmin(yy)>-0.8 or np.nanmax(yy)<0.8:continue
        hm=crossing_field(hh,yy,-0.8); hp=crossing_field(hh,yy,0.8); hz=crossing_field(hh,yy,0.0)
        if hm is None or hp is None or hz is None:continue
        direction="upfield" if hh[-1]>hh[0] else "downfield"
        rows.append({
          "direction":direction,"start":a,"stop":b,
          "h_minus_0p8":hm,"h_plus_0p8":hp,"h_zero":hz,
          "transition_width_mT":abs(hp-hm)
        })
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-root",type=Path,required=True)
    ap.add_argument("--out-dir",type=Path,required=True)
    a=ap.parse_args(); a.out_dir.mkdir(parents=True,exist_ok=True)
    sys.path.insert(0,str(a.source_root))
    from scripts.data_loader import AHE_hysteresis
    source=a.source_root/"data"/"Training effect"
    rows=[]
    for fn,label in FILES:
        p=source/fn
        if not p.exists(): raise FileNotFoundError(p)
        obj=AHE_hysteresis(str(p),label=label,plotting=False)
        bm=branch_transition_metrics(obj.field,obj.vxy_norm)
        widths=[x["transition_width_mT"] for x in bm]
        asym=(max(widths)/min(widths)) if len(widths)>=2 and min(widths)>0 else None
        log_asym=float(abs(np.log(asym))) if asym is not None else None
        rows.append({
          "label":label,"file":fn,"T_K":float(obj.T),
          "HEB_mT":float(obj.heb),"abs_HEB_mT":float(abs(obj.heb)),
          "HEB_err_mT":float(obj.heb_err),"C1_mT":float(obj.c1),"C2_mT":float(obj.c2),
          "coercive_halfwidth_mT":float(obj.w),
          "branch_transitions":bm,
          "transition_widths_mT":widths,
          "width_ratio":float(asym) if asym is not None else None,
          "log_width_asymmetry":log_asym
        })
    first=rows[0]; later=rows[1:]
    later_heb=[r["abs_HEB_mT"] for r in later]
    later_asym=[r["log_width_asymmetry"] for r in later if r["log_width_asymmetry"] is not None]
    result={
      "status":"PASS_HGMF_HG34_MAGNETIC_TRAINING_AUDIT_EXECUTED",
      "source":"sadityakr/EB-in-FGT_CrSBr-vdW-heterostructure@66662e8aa3690cebaaef52dfc4ddd3bea458a576",
      "loops":rows,
      "loop1_abs_HEB_mT":first["abs_HEB_mT"],
      "later_abs_HEB_mT":later_heb,
      "loop1_HEB_dominates_all_later":bool(first["abs_HEB_mT"]>max(later_heb)),
      "HEB_drop_ratio_max_later_over_first":float(max(later_heb)/first["abs_HEB_mT"]) if first["abs_HEB_mT"]>0 else None,
      "loop1_log_width_asymmetry":first["log_width_asymmetry"],
      "later_log_width_asymmetry":later_asym,
      "loop1_width_asymmetry_dominates_all_later":bool(first["log_width_asymmetry"] is not None and later_asym and first["log_width_asymmetry"]>max(later_asym)),
      "structural_source_prediction":"first loop after +2.5 T preset is uniquely exchange-biased/asymmetric; subsequent loops lose EB and become gradual/symmetric",
      "claim_boundary":"descriptive structural audit of public training-effect data; not an HGMF effect test"
    }
    (a.out_dir/"HGMF_HG34_MAGNETIC_TRAINING_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n")
    import pandas as pd
    flat=[]
    for r in rows:
        flat.append({k:v for k,v in r.items() if k not in ("branch_transitions","transition_widths_mT")})
    pd.DataFrame(flat).to_csv(a.out_dir/"HGMF_HG34_MAGNETIC_TRAINING_SUMMARY.csv",index=False)
    print(json.dumps(result,indent=2))

if __name__=="__main__":main()
