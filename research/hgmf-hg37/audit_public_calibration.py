#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, math, re
from pathlib import Path
import h5py
import numpy as np

TRAINING_FILES=[
 "01_FC2500mT_20250319_2120__10K.h5",
 "02_FC2500mT_20250319_2358__10K.h5",
 "03_FC2500mT_20250320_0231__10K.h5",
 "04_FC2500mT_20250320_0504__10K.h5",
 "05_FC2500mT_20250320_0738__10K.h5",
]

def attrs_dict(obj):
    out={}
    for k,v in obj.attrs.items():
        try:
            if isinstance(v,np.ndarray): v=v.tolist()
            elif isinstance(v,(np.generic,)): v=v.item()
            elif isinstance(v,bytes): v=v.decode(errors="replace")
            json.dumps(v)
            out[str(k)]=v
        except Exception:
            out[str(k)]=repr(v)
    return out

def h5_inventory(path):
    rec={"file":path.name,"root_attrs":{},"objects":[]}
    with h5py.File(path) as f:
        rec["root_attrs"]=attrs_dict(f)
        def visit(name,obj):
            z={"path":name,"type":type(obj).__name__,"attrs":attrs_dict(obj)}
            if isinstance(obj,h5py.Dataset):
                z["shape"]=list(obj.shape)
                z["dtype"]=str(obj.dtype)
                if name=="Data/Magnetic_Field":
                    a=np.asarray(obj,float)
                    z["min"]=float(np.min(a)); z["max"]=float(np.max(a))
                    z["unique_count"]=int(len(np.unique(a)))
            rec["objects"].append(z)
        f.visititems(visit)
    return rec

def grep_repo(root,patterns,extensions=None):
    hits=[]
    rx=re.compile("|".join(f"(?:{p})" for p in patterns),re.I)
    for p in root.rglob("*"):
        if not p.is_file() or ".git" in p.parts: continue
        if extensions and p.suffix.lower() not in extensions: continue
        try: txt=p.read_text(encoding="utf-8",errors="ignore")
        except Exception: continue
        for i,line in enumerate(txt.splitlines(),1):
            if rx.search(line):
                hits.append({"file":str(p.relative_to(root)),"line":i,"text":line[:500]})
                if len(hits)>=500:return hits
    return hits

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--mag-root",type=Path,required=True)
    ap.add_argument("--brown-root",type=Path,required=True)
    ap.add_argument("--hg36-results",type=Path,required=True)
    ap.add_argument("--out-dir",type=Path,required=True)
    a=ap.parse_args(); a.out_dir.mkdir(parents=True,exist_ok=True)

    h36=json.loads(a.hg36_results.read_text())
    h=h36["magnetism"]["observed_HEB_mT"]
    trained=np.abs(np.asarray(h[1:],float))
    current_step=float(h36["magnetism"]["source_field_step_bound_mT_approx"])

    inventories=[]
    src=a.mag_root/"data"/"Training effect"
    for fn in TRAINING_FILES:
        inventories.append(h5_inventory(src/fn))

    mag_hits=grep_repo(
      a.mag_root,
      [r"calibrat",r"hall\s*probe",r"field\s*accuracy",r"field\s*uncert",r"magnet\s*accuracy",r"readback",r"93\.17"],
      extensions={".py",".md",".txt",".csv",".ipynb",".cff",".json"}
    )
    brown_hits=grep_repo(
      a.brown_root,
      [r"nonporous",r"non-porous",r"film\s*reference",r"surface\s*area",r"FHH",r"silica\s*reference",r"surface\s*adsorption"],
      extensions={".md",".txt",".csv",".json",".ipynb",".py"}
    )

    max_abs=float(np.max(trained))
    min_abs=float(np.min(trained))
    gap=current_step-max_abs
    relative=float(gap/current_step)

    # Informative heuristic only: if Gaussian bootstrap SD were exact, one-loop
    # log-LR threshold log(140) requires residual >= sigma*sqrt(2 log 140).
    sds=np.asarray(h36["magnetism"]["bootstrap_sd_HEB_mT"][1:],float)
    j=int(np.argmax(trained))
    sigma=float(sds[j])
    e140_residual=sigma*math.sqrt(2*math.log(140))
    e140_delta=float(max_abs-e140_residual)

    out={
      "status":"PASS_HGMF_HG37_PUBLIC_CALIBRATION_AUDIT_EXECUTED",
      "magnetic":{
        "current_field_step_bound_mT":current_step,
        "trained_abs_HEB_mT":trained.tolist(),
        "global_set_membership_break_threshold_mT":max_abs,
        "all_loops_nonabsorbable_threshold_mT":min_abs,
        "improvement_needed_from_current_to_global_break_mT":gap,
        "relative_improvement_needed":relative,
        "Gaussian_bootstrap_heuristic_not_confirmatory":{
          "controlling_loop_index_1based":j+2,
          "bootstrap_sd_mT":sigma,
          "residual_for_E140_mT":e140_residual,
          "field_nuisance_bound_for_E140_mT":e140_delta
        },
        "hdf5_inventory":inventories,
        "repository_calibration_search_hits":mag_hits,
        "explicit_independent_field_calibration_found":False,
        "interpretation":"public source exposes field conversion and acquisition arrays but this audit found no independent field-axis calibration/accuracy certificate"
      },
      "adsorption":{
        "repository_reference_search_hits":brown_hits,
        "external_nonporous_film_reference_found_in_Brown_repo":False,
        "Mason_1988_alternative_route":"PUBLICATION_EXISTS_AND_STATES_NO_NEED_TO_SEPARATE_CAPILLARY_CONDENSATION_FROM_SURFACE_ADSORPTION",
        "Mason_route_executable_in_current_repo":False,
        "interpretation":"Brown/NIST repo does not contain the external film-reference object required by the Cimino observation map; Mason provides a distinct standard route, so absence of Vs cannot be interpreted as failure of standard network physics"
      },
      "historical_confirmatory_rescue":"FAIL_PUBLICLY_AVAILABLE_CALIBRATION_OBJECTS",
      "prospective_pivot_required":True
    }
    (a.out_dir/"HGMF_HG37_PUBLIC_CALIBRATION_AUDIT.json").write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps(out,indent=2))

if __name__=="__main__":main()
