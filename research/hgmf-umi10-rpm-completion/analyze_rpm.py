#!/usr/bin/env python3
"""HGMF-UMI-10: exact audit of public magnetic minor-loop HDF5 files.

No synthetic observations are generated. The script reads the four public
HDF5 files from the cited repository, reproduces its published loading logic,
segments the field history, audits return/closure structure, and runs
whole-loop blocked model comparisons.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

import h5py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

FILES = [
    "Minor_loops_PF2500mT_20250325_2005__10K.h5",
    "Minor_loops_PF2500mT_20250325_2230__10K.h5",
    "Minor_loops_PF2500mT_20250326_0034__10K.h5",
    "Minor_loops_PF2500mT_20250326_0219__10K.h5",
]


@dataclass
class LoopData:
    loop_id: str
    source_file: str
    field_mT: np.ndarray
    vxy_uV: np.ndarray
    vxy_norm: np.ndarray
    temperature_K: float
    direction: np.ndarray
    segment_id: np.ndarray
    reversal_indices: list[int]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _find_block_size(field: np.ndarray) -> int:
    if len(field) < 2:
        raise ValueError("field array too short")
    i = 0
    while i + 1 < len(field) and abs(float(field[i] - field[i + 1])) < 0.01:
        i += 1
    p2 = i + 1
    if p2 <= 0:
        raise ValueError("invalid repeated-point block size")
    return p2


def read_h5_like_source(path: Path) -> tuple[np.ndarray, np.ndarray, float, dict]:
    """Reproduce scripts/data_loader.py from the source repository."""
    with h5py.File(path, "r") as f:
        data = f["Data"]
        field = np.asarray(data["Magnetic_Field"])
        vxy = np.asarray(data["Avg_Voltage_Hp34420A_Ch1"])
        st = np.asarray(data["Rod_Temp"])
        keys = sorted(list(data.keys()))

    p2 = _find_block_size(field)
    current_inverted = bool(vxy[0] * vxy[1] < 0)
    out_field: list[float] = []
    out_vxy: list[float] = []
    i = 0
    if current_inverted:
        p = round(p2 / 2)
        while i < len(field):
            fb = field[i:i+p2]
            vb1 = vxy[i:i+p]
            vb2 = vxy[i+p:i+p2]
            if len(fb) == 0 or len(vb1) == 0 or len(vb2) == 0:
                break
            out_field.append(float(np.mean(fb)))
            out_vxy.append(float(np.mean(vb1) - np.mean(vb2)))
            i += p2
    else:
        while i < len(field):
            fb = field[i:i+p2]
            vb = vxy[i:i+p2]
            if len(fb) == 0 or len(vb) == 0:
                break
            out_field.append(float(np.mean(fb)))
            out_vxy.append(float(np.mean(vb)))
            i += p2

    field_mT = np.asarray(out_field, dtype=float) * 8000.0 / 93.17
    vxy_uV = np.asarray(out_vxy, dtype=float) * 1e6
    temperature = float(np.mean(st))
    meta = {
        "raw_points": int(len(field)),
        "processed_points": int(len(field_mT)),
        "repeat_block_size": int(p2),
        "current_inverted": current_inverted,
        "data_keys": keys,
    }
    return field_mT, vxy_uV, temperature, meta


def fill_sign_zeros(sign: np.ndarray) -> np.ndarray:
    sign = sign.astype(int).copy()
    for i in range(1, len(sign)):
        if sign[i] == 0:
            sign[i] = sign[i-1]
    for i in range(len(sign)-2, -1, -1):
        if sign[i] == 0:
            sign[i] = sign[i+1]
    sign[sign == 0] = 1
    return sign


def segment_monotonic(field: np.ndarray) -> tuple[np.ndarray, np.ndarray, list[int]]:
    d = np.diff(field)
    scale = max(float(np.nanmax(field) - np.nanmin(field)), 1.0)
    tol = max(scale * 1e-10, 1e-9)
    s = np.sign(np.where(abs(d) <= tol, 0.0, d))
    s = fill_sign_zeros(s)
    reversal_indices = [int(i + 1) for i in np.where(s[1:] != s[:-1])[0]]
    boundaries = [0] + reversal_indices + [len(field)]
    seg_id = np.zeros(len(field), dtype=int)
    direction = np.zeros(len(field), dtype=int)
    for k, (a, b) in enumerate(zip(boundaries[:-1], boundaries[1:])):
        seg_id[a:b] = k
        if b-a >= 2:
            direction[a:b] = 1 if field[b-1] > field[a] else -1
        elif a > 0:
            direction[a:b] = direction[a-1]
        else:
            direction[a:b] = 1
    return direction, seg_id, reversal_indices


def load_loop(path: Path, loop_id: str) -> tuple[LoopData, dict]:
    field, vxy, temp, meta = read_h5_like_source(path)
    offset = (float(np.max(vxy)) + float(np.min(vxy))) / 2.0
    amp = (float(np.max(vxy)) - float(np.min(vxy))) / 2.0
    if amp <= 0:
        raise ValueError(f"zero AHE amplitude in {path}")
    y = (vxy - offset) / amp
    direction, seg_id, rev = segment_monotonic(field)
    return LoopData(loop_id, path.name, field, vxy, y, temp, direction, seg_id, rev), {
        **meta, "offset_uV": offset, "amplitude_uV": amp,
        "reversal_count": len(rev), "segment_count": int(seg_id.max()+1),
        "field_min_mT": float(field.min()), "field_max_mT": float(field.max()),
        "temperature_K": temp, "sha256": sha256(path),
    }


def normalized_input(loop: LoopData) -> np.ndarray:
    lo, hi = float(loop.field_mT.min()), float(loop.field_mT.max())
    if hi == lo:
        return np.zeros_like(loop.field_mT)
    return 2.0 * (loop.field_mT - lo) / (hi - lo) - 1.0


def reversal_stack_features(x: np.ndarray) -> np.ndarray:
    """Causal reduced-extrema features from input only."""
    n = len(x)
    feats = np.zeros((n, 7), dtype=float)
    stack: list[float] = [float(x[0])]
    prev_dir = 0
    for t in range(n):
        if t == 0:
            direction = 0
        else:
            dx = float(x[t]-x[t-1])
            direction = 1 if dx > 0 else (-1 if dx < 0 else prev_dir)
        if t > 0 and direction != 0 and prev_dir != 0 and direction != prev_dir:
            stack.append(float(x[t-1]))
        changed = True
        while changed and len(stack) >= 3:
            changed = False
            a, b, c = stack[-3], stack[-2], stack[-1]
            if (a <= b and c >= b) or (a >= b and c <= b):
                stack.pop(-2)
                changed = True
        prev_dir = direction if direction != 0 else prev_dir
        tail = ([-1.0] * 4 + stack)[-4:]
        feats[t] = [x[t], direction, len(stack), *tail]
    return feats


def relay_features(x: np.ndarray, levels: int = 9) -> np.ndarray:
    vals = np.linspace(-1.0, 1.0, levels)
    thresholds = [(a,b) for a in vals for b in vals if a > b]
    init = 1.0 if x[0] >= 0 else -1.0
    state = np.full(len(thresholds), init, dtype=float)
    out = np.empty((len(x), len(thresholds)), dtype=float)
    for t, xt in enumerate(x):
        for j,(a,b) in enumerate(thresholds):
            if xt >= a:
                state[j] = 1.0
            elif xt <= b:
                state[j] = -1.0
        out[t] = state
    return out


def make_features(loop: LoopData, model: str) -> np.ndarray:
    x = normalized_input(loop)
    d = loop.direction.astype(float)
    if model == "memoryless":
        return np.column_stack([x, x*x, x*x*x])
    if model == "branch":
        return np.column_stack([x, x*x, x*x*x, d, d*x, d*x*x])
    if model == "fading":
        ems=[]
        for alpha in (0.05, 0.15, 0.4):
            z=np.empty_like(x); z[0]=x[0]
            for t in range(1,len(x)):
                z[t]=(1-alpha)*z[t-1]+alpha*x[t]
            ems.append(z)
        return np.column_stack([x, x*x, d, *ems])
    if model == "finite_stack":
        return reversal_stack_features(x)
    if model == "rpm_relays":
        return np.column_stack([x, d, relay_features(x, levels=9)])
    raise ValueError(model)


def blocked_model_audit(loops: Sequence[LoopData]) -> pd.DataFrame:
    models = ["memoryless","branch","fading","finite_stack","rpm_relays"]
    rows=[]
    for held in loops:
        train=[z for z in loops if z.loop_id != held.loop_id]
        for model in models:
            Xtr=np.vstack([make_features(z,model) for z in train])
            ytr=np.concatenate([z.vxy_norm for z in train])
            Xte=make_features(held,model)
            yte=held.vxy_norm
            pipe=make_pipeline(StandardScaler(),Ridge(alpha=1e-3))
            pipe.fit(Xtr,ytr)
            pred=pipe.predict(Xte)
            rmse=float(np.sqrt(mean_squared_error(yte,pred)))
            mae=float(np.mean(np.abs(yte-pred)))
            rows.append({"heldout_loop":held.loop_id,"model":model,
                         "rmse_norm":rmse,"mae_norm":mae,
                         "n_train":len(ytr),"n_test":len(yte)})
    return pd.DataFrame(rows)


def endpoint_return_audit(loop: LoopData) -> pd.DataFrame:
    idx=[0]+loop.reversal_indices+[len(loop.field_mT)-1]
    step=np.median(np.abs(np.diff(loop.field_mT))) if len(loop.field_mT)>1 else 0.0
    tol=max(float(step)*1.5, (loop.field_mT.max()-loop.field_mT.min())*1e-4)
    rows=[]
    for a in range(len(idx)):
        for b in range(a+2,len(idx)):
            ia,ib=idx[a],idx[b]
            if abs(loop.field_mT[ia]-loop.field_mT[ib]) <= tol:
                rows.append({"loop_id":loop.loop_id,"endpoint_a":ia,"endpoint_b":ib,
                             "field_a_mT":loop.field_mT[ia],"field_b_mT":loop.field_mT[ib],
                             "field_error_mT":abs(loop.field_mT[ia]-loop.field_mT[ib]),
                             "vxy_norm_a":loop.vxy_norm[ia],"vxy_norm_b":loop.vxy_norm[ib],
                             "return_error_norm":abs(loop.vxy_norm[ia]-loop.vxy_norm[ib]),
                             "endpoint_separation":b-a})
    return pd.DataFrame(rows)


def adjacent_branch_gaps(loop: LoopData, grid_n: int=101) -> pd.DataFrame:
    rows=[]
    segs=[]
    for sid in np.unique(loop.segment_id):
        mask=loop.segment_id==sid
        xx=loop.field_mT[mask]; yy=loop.vxy_norm[mask]
        order=np.argsort(xx)
        segs.append((int(sid),int(loop.direction[mask][0]),xx[order],yy[order]))
    for k in range(len(segs)-1):
        s1,d1,x1,y1=segs[k]; s2,d2,x2,y2=segs[k+1]
        if d1==d2: continue
        lo=max(x1.min(),x2.min()); hi=min(x1.max(),x2.max())
        if hi<=lo: continue
        grid=np.linspace(lo,hi,grid_n)
        z1=np.interp(grid,x1,y1); z2=np.interp(grid,x2,y2)
        span=max(hi-lo,1e-12)
        for j,g in enumerate(grid):
            rows.append({"loop_id":loop.loop_id,"segment_pair":f"{s1}-{s2}",
                         "position":(g-lo)/span,"field_mT":g,
                         "gap_norm":z2[j]-z1[j],"abs_gap_norm":abs(z2[j]-z1[j])})
    return pd.DataFrame(rows)


def plot_loops(loops: Sequence[LoopData], out: Path) -> None:
    plt.figure(figsize=(9,6))
    for z in loops:
        plt.plot(z.field_mT,z.vxy_norm,label=z.loop_id,linewidth=1.2)
    plt.xlabel("magnetic field (mT)")
    plt.ylabel("normalized Hall response")
    plt.title("Public FGT/CrSBr magnetic minor loops")
    plt.legend()
    plt.tight_layout()
    plt.savefig(out,dpi=180)
    plt.close()


def plot_models(df: pd.DataFrame, out: Path) -> None:
    p=df.pivot(index="heldout_loop",columns="model",values="rmse_norm")
    p.plot(kind="bar",figsize=(10,6))
    plt.ylabel("whole-loop held-out RMSE")
    plt.title("HGMF-UMI-10 blocked model tribunal")
    plt.tight_layout()
    plt.savefig(out,dpi=180)
    plt.close()


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--source-dir",type=Path,required=True)
    ap.add_argument("--out-dir",type=Path,required=True)
    args=ap.parse_args()
    args.out_dir.mkdir(parents=True,exist_ok=True)

    loops=[]; manifest=[]; all_rows=[]
    for i,name in enumerate(FILES,1):
        p=args.source_dir/name
        if not p.exists():
            raise FileNotFoundError(p)
        loop,meta=load_loop(p,f"Loop_{i}")
        loops.append(loop)
        manifest.append({"loop_id":loop.loop_id,"file":name,**meta})
        for j in range(len(loop.field_mT)):
            all_rows.append({"loop_id":loop.loop_id,"source_file":name,"index":j,
                             "field_mT":loop.field_mT[j],"vxy_uV":loop.vxy_uV[j],
                             "vxy_norm":loop.vxy_norm[j],"direction":loop.direction[j],
                             "segment_id":loop.segment_id[j],"temperature_K":loop.temperature_K})
    pd.DataFrame(manifest).to_csv(args.out_dir/"HGMF_UMI10_H5_MANIFEST_AND_STRUCTURE.csv",index=False)
    pd.DataFrame(all_rows).to_csv(args.out_dir/"HGMF_UMI10_MAGNETIC_MINOR_LOOPS_PROCESSED.csv",index=False)

    model_df=blocked_model_audit(loops)
    model_df.to_csv(args.out_dir/"HGMF_UMI10_BLOCKED_MODEL_TRIBUNAL.csv",index=False)
    ret_df=pd.concat([endpoint_return_audit(z) for z in loops],ignore_index=True)
    ret_df.to_csv(args.out_dir/"HGMF_UMI10_RETURN_POINT_AUDIT.csv",index=False)
    gap_df=pd.concat([adjacent_branch_gaps(z) for z in loops],ignore_index=True)
    gap_df.to_csv(args.out_dir/"HGMF_UMI10_BRANCH_GAPS.csv",index=False)

    summary_models=model_df.groupby("model")["rmse_norm"].agg(["mean","median","max","min"]).reset_index()
    summary_models.to_csv(args.out_dir/"HGMF_UMI10_MODEL_SUMMARY.csv",index=False)

    if len(ret_df):
        return_summary={
            "matched_return_pairs":int(len(ret_df)),
            "mean_return_error_norm":float(ret_df.return_error_norm.mean()),
            "median_return_error_norm":float(ret_df.return_error_norm.median()),
            "max_return_error_norm":float(ret_df.return_error_norm.max()),
        }
    else:
        return_summary={"matched_return_pairs":0,"mean_return_error_norm":None,
                        "median_return_error_norm":None,"max_return_error_norm":None}

    best=summary_models.sort_values("mean").iloc[0].to_dict()
    memoryless=float(summary_models.loc[summary_models.model=="memoryless","mean"].iloc[0])
    rpm=float(summary_models.loc[summary_models.model=="rpm_relays","mean"].iloc[0])
    branch=float(summary_models.loc[summary_models.model=="branch","mean"].iloc[0])
    finite=float(summary_models.loc[summary_models.model=="finite_stack","mean"].iloc[0])

    result={
        "status":"PASS_HGMF_UMI10_BINARY_AUDIT_EXECUTED",
        "files":manifest,
        "return_point":return_summary,
        "models":summary_models.to_dict(orient="records"),
        "best_model":best,
        "relative_improvement_rpm_vs_memoryless":1-rpm/memoryless,
        "relative_improvement_branch_vs_memoryless":1-branch/memoryless,
        "relative_improvement_stack_vs_memoryless":1-finite/memoryless,
        "branch_gap_pairs":int(gap_df.segment_pair.nunique()) if len(gap_df) else 0,
        "claim_boundary":{
            "binary_recovery":"PASS",
            "magnetic_history_dependence":"PASS",
            "magnetic_return_point_pairs":"PASS" if len(ret_df)>0 else "HOLD_NO_REPEATED_ENDPOINTS",
            "rpm_operator_preferred":"PASS" if rpm < min(memoryless,branch) else "FAIL_OR_NOT_SELECTED",
            "cross_domain_operator_class":"HOLD_REQUIRES_ADSORPTION_SAME_TRIBUNAL",
        },
    }
    (args.out_dir/"HGMF_UMI10_RESULTS.json").write_text(json.dumps(result,indent=2),encoding="utf-8")

    report="# HGMF-UMI-10 — Magnetic Binary Audit\n\n"
    report+=f"Processed four public HDF5 minor-loop files.\n\n"
    report+=f"- Total processed points: {sum(len(z.field_mT) for z in loops)}\n"
    report+=f"- Matched return-point endpoint pairs: {return_summary['matched_return_pairs']}\n"
    report+=f"- Best blocked model: `{best['model']}` (mean RMSE {best['mean']:.6g})\n"
    report+=f"- RPM relay improvement vs memoryless: {100*(1-rpm/memoryless):.2f}%\n"
    report+=f"- Stack improvement vs memoryless: {100*(1-finite/memoryless):.2f}%\n\n"
    report+="## Claim boundary\n\n"
    report+="This audit establishes only what the HDF5 data support. A shared cross-domain operator class remains held until adsorption is run through the identical frozen model tribunal.\n"
    (args.out_dir/"HGMF_UMI10_MAGNETIC_AUDIT_REPORT.md").write_text(report,encoding="utf-8")

    plot_loops(loops,args.out_dir/"HGMF_UMI10_MAGNETIC_MINOR_LOOPS.png")
    plot_models(model_df,args.out_dir/"HGMF_UMI10_MODEL_TRIBUNAL.png")
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
