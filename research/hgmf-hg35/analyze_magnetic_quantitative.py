#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, sys
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares

FILES=[
 ("01_FC2500mT_20250319_2120__10K.h5","Loop 1"),
 ("02_FC2500mT_20250319_2358__10K.h5","Loop 2"),
 ("03_FC2500mT_20250320_0231__10K.h5","Loop 3"),
 ("04_FC2500mT_20250320_0504__10K.h5","Loop 4"),
 ("05_FC2500mT_20250320_0738__10K.h5","Loop 5"),
]

def binek_predict(h1, hinf, gamma, n=5):
    vals=[float(h1)]
    for _ in range(1,n):
        h=vals[-1]
        nxt=h-gamma*(h-hinf)**3
        if not math.isfinite(nxt) or abs(nxt)>1e8:
            return np.full(n,np.nan)
        vals.append(nxt)
    return np.asarray(vals,float)

def fit_binek(h):
    h=np.asarray(h,float)
    def resid(theta):
        hinf=float(theta[0]); gamma=math.exp(float(theta[1]))
        pred=binek_predict(h[0],hinf,gamma,len(h))
        if not np.all(np.isfinite(pred)):
            return np.full(len(h)-1,1e9)
        return pred[1:]-h[1:]
    x0=np.array([float(np.mean(h[1:])), math.log(1e-5)])
    fit=least_squares(resid,x0,bounds=([-200,-30],[200,0]),max_nfev=100000)
    hinf=float(fit.x[0]); gamma=float(math.exp(fit.x[1]))
    pred=binek_predict(h[0],hinf,gamma,len(h))
    rmse=float(np.sqrt(np.mean((pred[1:]-h[1:])**2)))
    return {"Hinf_mT":hinf,"Gamma_mT_minus2":gamma,"prediction_mT":pred.tolist(),"rmse_loops2_5_mT":rmse,"converged":bool(fit.success)}

def fit_one_shot(h):
    h=np.asarray(h,float)
    hinf=float(np.mean(h[1:]))
    pred=np.array([h[0]]+[hinf]*(len(h)-1),float)
    return {"H1_mT":float(h[0]),"Hinf_mT":hinf,"prediction_mT":pred.tolist(),"rmse_loops2_5_mT":float(np.sqrt(np.mean((pred[1:]-h[1:])**2)))}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-root",type=Path,required=True)
    ap.add_argument("--out-dir",type=Path,required=True)
    a=ap.parse_args(); a.out_dir.mkdir(parents=True,exist_ok=True)
    sys.path.insert(0,str(a.source_root))
    from scripts.data_loader import AHE_hysteresis

    source=a.source_root/"data"/"Training effect"
    loops=[]
    for fn,label in FILES:
        obj=AHE_hysteresis(str(source/fn),label=label,plotting=False)
        h=float(obj.heb); d=float(obj.heb_err)
        loops.append({
          "label":label,"file":fn,"HEB_mT":h,"abs_HEB_mT":abs(h),
          "field_resolution_bound_mT":d,
          "interval_lo_mT":h-d,"interval_hi_mT":h+d,
          "zero_in_interval":bool((h-d)<=0<=(h+d))
        })

    h=np.array([z["HEB_mT"] for z in loops],float)
    d=np.array([z["field_resolution_bound_mT"] for z in loops],float)
    interval_pass=(not loops[0]["zero_in_interval"]) and all(z["zero_in_interval"] for z in loops[1:])
    one=fit_one_shot(h)
    binek=fit_binek(h)

    # Resolution-normalized residual diagnostic only; field step is NOT treated as a sigma.
    later_norm=(h[1:]/d[1:]).tolist()
    result={
      "status":"PASS_HGMF_HG35_MAGNETIC_QUANTITATIVE_AUDIT_EXECUTED",
      "source":"sadityakr/EB-in-FGT_CrSBr-vdW-heterostructure@66662e8aa3690cebaaef52dfc4ddd3bea458a576",
      "loops":loops,
      "source_interval_null":{
        "definition":"loop1 true HEB nonzero; loops2-5 true HEB zero; field resolution used as deterministic interval bound, not Gaussian sigma",
        "pass":bool(interval_pass),
        "loop1_zero_excluded":bool(not loops[0]["zero_in_interval"]),
        "loops2_5_zero_included":bool(all(z["zero_in_interval"] for z in loops[1:])),
        "max_abs_later_over_resolution":float(np.max(np.abs(h[1:]/d[1:])))
      },
      "one_shot_training_model":one,
      "binek_recursive_diagnostic":binek,
      "later_resolution_normalized_HEB":later_norm,
      "likelihood_authority":"NONE_INTERVAL_SET_MEMBERSHIP_ONLY",
      "full_Vxy_likelihood_bridge":"FAIL_NOT_PRESENT_IN_SOURCE_THEORY_ASSETS",
      "claim_boundary":"quantitative source-summary compatibility does not imply unique mechanism or a confirmatory likelihood"
    }
    (a.out_dir/"HGMF_HG35_MAGNETIC_QUANTITATIVE_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__": main()
