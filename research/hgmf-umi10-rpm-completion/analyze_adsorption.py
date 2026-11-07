#!/usr/bin/env python3
"""Apply the frozen HGMF-UMI-10 operator tribunal to complete NIST runs.

NIST defines a run as a continuous sequence of states and segments as pressure-
reversal objectives. The dynamic audit therefore holds out complete runs rather
than fragmenting history at segment boundaries.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

import analyze_rpm as core


def load_closed_runs(csv_path: Path) -> tuple[list[core.LoopData], pd.DataFrame]:
    df = pd.read_csv(csv_path)
    df["source_order"] = np.arange(len(df))
    desc = df["segment_description"].fillna("").astype(str)
    run_ids = sorted(df.loc[desc.str.contains("closed loop",case=False,regex=False),"run_id"].unique())
    loops: list[core.LoopData]=[]
    manifest=[]
    for run_id in run_ids:
        g=df[df.run_id==run_id].sort_values("source_order")
        x=g["pressure"].to_numpy(float)
        y=g["adsorption"].to_numpy(float)
        ok=np.isfinite(x)&np.isfinite(y)
        x=x[ok]; y=y[ok]
        if len(x)<10 or np.ptp(x)<=0 or np.ptp(y)<=0:
            continue
        yn=(y-(y.max()+y.min())/2)/((y.max()-y.min())/2)
        direction, seg_id, rev=core.segment_monotonic(x)
        lid=f"NIST_run_{int(run_id)}"
        temp=float(g["temperature"].dropna().mean())
        loops.append(core.LoopData(lid,csv_path.name,x,y,yn,temp,direction,seg_id,rev))
        descriptions=g["segment_description"].fillna("").astype(str)
        manifest.append({
            "loop_id":lid,"run_id":int(run_id),"run_description":str(g["run_description"].iloc[0]),
            "points":len(x),"source_segments":int(g.segment_id.nunique()),
            "closed_loop_segments":int(descriptions.str.contains("closed loop",case=False,regex=False).sum()),
            "reversal_count":len(rev),"derived_segment_count":int(seg_id.max()+1),
            "temperature_K":temp,"pressure_min":float(x.min()),"pressure_max":float(x.max()),
            "adsorption_min_mg":float(y.min()),"adsorption_max_mg":float(y.max()),
        })
    return loops,pd.DataFrame(manifest)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--csv",type=Path,required=True)
    ap.add_argument("--out-dir",type=Path,required=True)
    args=ap.parse_args(); args.out_dir.mkdir(parents=True,exist_ok=True)
    loops,manifest=load_closed_runs(args.csv)
    if len(loops)<2:
        raise RuntimeError(f"only {len(loops)} eligible complete runs")
    manifest.to_csv(args.out_dir/"HGMF_UMI10_ADSORPTION_MANIFEST.csv",index=False)

    rows=[]
    for z in loops:
        for i in range(len(z.field_mT)):
            rows.append({"loop_id":z.loop_id,"index":i,"relative_pressure":z.field_mT[i],
                         "adsorption_mg":z.vxy_uV[i],"adsorption_norm":z.vxy_norm[i],
                         "direction":z.direction[i],"segment_id":z.segment_id[i],
                         "temperature_K":z.temperature_K})
    pd.DataFrame(rows).to_csv(args.out_dir/"HGMF_UMI10_ADSORPTION_CLOSED_LOOPS.csv",index=False)

    model=core.blocked_model_audit(loops)
    model.to_csv(args.out_dir/"HGMF_UMI10_ADSORPTION_MODEL_TRIBUNAL.csv",index=False)
    summary=model.groupby("model")["rmse_norm"].agg(["mean","median","max","min"]).reset_index()
    summary.to_csv(args.out_dir/"HGMF_UMI10_ADSORPTION_MODEL_SUMMARY.csv",index=False)

    returns=pd.concat([core.endpoint_return_audit(z) for z in loops],ignore_index=True)
    returns.to_csv(args.out_dir/"HGMF_UMI10_ADSORPTION_RETURN_POINT_AUDIT.csv",index=False)
    gaps=pd.concat([core.adjacent_branch_gaps(z) for z in loops],ignore_index=True)
    gaps.to_csv(args.out_dir/"HGMF_UMI10_ADSORPTION_BRANCH_GAPS.csv",index=False)

    best=summary.sort_values("mean").iloc[0].to_dict()
    by={row["model"]:float(row["mean"]) for _,row in summary.iterrows()}
    result={
        "status":"PASS_HGMF_UMI10_ADSORPTION_TRIBUNAL_EXECUTED",
        "runs":len(loops),"points":sum(len(z.field_mT) for z in loops),
        "run_ids":[int(x) for x in manifest.run_id],
        "reversal_counts":{str(k):int(v) for k,v in manifest["reversal_count"].value_counts().sort_index().items()},
        "return_pairs":int(len(returns)),
        "mean_return_error_norm":float(returns.return_error_norm.mean()) if len(returns) else None,
        "median_return_error_norm":float(returns.return_error_norm.median()) if len(returns) else None,
        "best_model":best,"models":summary.to_dict(orient="records"),
        "improvement_best_vs_memoryless":1-float(best["mean"])/by["memoryless"],
        "rpm_improvement_vs_memoryless":1-by["rpm_relays"]/by["memoryless"],
        "stack_improvement_vs_memoryless":1-by["finite_stack"]/by["memoryless"],
        "claim_boundary":{
            "continuous_run_histories":"PASS",
            "history_model_selected":"PASS" if best["model"]!="memoryless" else "FAIL",
            "rpm_selected":"PASS" if best["model"]=="rpm_relays" else "FAIL_NOT_BEST",
            "nested_rpm_identifiable":"PASS" if manifest.reversal_count.max()>=3 else "HOLD_PROTOCOL_DEPTH",
        },
    }
    (args.out_dir/"HGMF_UMI10_ADSORPTION_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n")
    core.plot_loops(loops,args.out_dir/"HGMF_UMI10_ADSORPTION_LOOPS.png")
    core.plot_models(model,args.out_dir/"HGMF_UMI10_ADSORPTION_MODEL_TRIBUNAL.png")
    print(json.dumps(result,indent=2))

if __name__=="__main__": main()
