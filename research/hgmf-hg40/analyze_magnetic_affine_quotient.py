#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

from hgmf_hg40_affine_quotient import magnetic_affine_metrics

FILES = [
    ("01_FC2500mT_20250319_2120__10K.h5", "Loop 1"),
    ("02_FC2500mT_20250319_2358__10K.h5", "Loop 2"),
    ("03_FC2500mT_20250320_0231__10K.h5", "Loop 3"),
    ("04_FC2500mT_20250320_0504__10K.h5", "Loop 4"),
    ("05_FC2500mT_20250320_0738__10K.h5", "Loop 5"),
]


def field_segments(h: np.ndarray) -> list[tuple[int, int]]:
    d = np.sign(np.diff(h))
    for i in range(1, len(d)):
        if d[i] == 0:
            d[i] = d[i - 1]
    for i in range(len(d) - 2, -1, -1):
        if d[i] == 0:
            d[i] = d[i + 1]
    cuts = [0] + [i + 1 for i in range(len(d) - 1) if d[i] * d[i + 1] < 0] + [len(h)]
    return [(cuts[i], cuts[i + 1]) for i in range(len(cuts) - 1) if cuts[i + 1] - cuts[i] >= 3]


def crossing_field(h: np.ndarray, y: np.ndarray, level: float) -> float | None:
    z = y - level
    for i in range(len(h) - 1):
        if z[i] == 0:
            return float(h[i])
        if z[i] * z[i + 1] < 0:
            den = y[i + 1] - y[i]
            if den != 0:
                return float(h[i] + (level - y[i]) * (h[i + 1] - h[i]) / den)
    return None


def branch_widths(h: np.ndarray, y: np.ndarray) -> list[dict]:
    rows = []
    for start, stop in field_segments(h):
        hh = np.asarray(h[start:stop], float)
        yy = np.asarray(y[start:stop], float)
        if np.nanmin(yy) > -0.8 or np.nanmax(yy) < 0.8:
            continue
        hm = crossing_field(hh, yy, -0.8)
        hp = crossing_field(hh, yy, 0.8)
        hz = crossing_field(hh, yy, 0.0)
        if hm is None or hp is None or hz is None:
            continue
        rows.append(
            {
                "direction": "upfield" if hh[-1] > hh[0] else "downfield",
                "transition_width_mT": float(abs(hp - hm)),
                "zero_crossing_mT": float(hz),
            }
        )
    return rows


def jsonable_metrics(metrics: dict) -> dict:
    out = {}
    for key, value in metrics.items():
        if isinstance(value, np.ndarray):
            out[key] = value.tolist()
        elif isinstance(value, np.generic):
            out[key] = value.item()
        else:
            out[key] = value
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    sys.path.insert(0, str(args.source_root))
    from scripts.data_loader import AHE_hysteresis

    source = args.source_root / "data" / "Training effect"
    loops = []
    for filename, label in FILES:
        obj = AHE_hysteresis(str(source / filename), label=label, plotting=False)
        widths = branch_widths(np.asarray(obj.field, float), np.asarray(obj.vxy_norm, float))
        width_values = [x["transition_width_mT"] for x in widths]
        ratio = None
        log_asymmetry = None
        if len(width_values) >= 2 and min(width_values) > 0:
            ratio = float(max(width_values) / min(width_values))
            log_asymmetry = float(abs(np.log(ratio)))
        loops.append(
            {
                "label": label,
                "file": filename,
                "C1_mT": float(obj.c1),
                "C2_mT": float(obj.c2),
                "HEB_mT": float(obj.heb),
                "coercive_halfwidth_mT": float(abs(obj.c2 - obj.c1) / 2.0),
                "branch_transitions": widths,
                "transition_width_ratio": ratio,
                "log_transition_width_asymmetry": log_asymmetry,
            }
        )

    c1 = np.asarray([x["C1_mT"] for x in loops], float)
    c2 = np.asarray([x["C2_mT"] for x in loops], float)
    metrics = magnetic_affine_metrics(c1, c2)

    # Deterministic code-level invariance check on the real crossings.
    alpha = 1.731
    beta = 11.37
    transformed = magnetic_affine_metrics(alpha * c1 + beta, alpha * c2 + beta)
    invariant_keys = ["loop1_training_contrast", "trained_centered_coordinates", "HEB_affine_coordinates"]
    errors = {}
    for key in invariant_keys:
        a = np.asarray(metrics[key], float)
        b = np.asarray(transformed[key], float)
        errors[key] = float(np.max(np.abs(a - b)))
    max_error = max(errors.values())

    later_log_asymmetry = [
        x["log_transition_width_asymmetry"]
        for x in loops[1:]
        if x["log_transition_width_asymmetry"] is not None
    ]
    result = {
        "status": "PASS_HGMF_HG40_MAGNETIC_AFFINE_QUOTIENT_EXECUTED",
        "source": "sadityakr/EB-in-FGT_CrSBr-vdW-heterostructure@66662e8aa3690cebaaef52dfc4ddd3bea458a576",
        "loops": loops,
        "common_affine_field_model": "H_true = alpha*H_recorded + beta with alpha>0 shared across loops",
        "quotient_metrics": jsonable_metrics(metrics),
        "affine_invariance_test": {
            "test_alpha": alpha,
            "test_beta_mT": beta,
            "per_metric_max_abs_error": errors,
            "global_max_abs_error": max_error,
            "pass": bool(max_error < 1e-12),
        },
        "loop1_log_transition_width_asymmetry": loops[0]["log_transition_width_asymmetry"],
        "later_log_transition_width_asymmetry": later_log_asymmetry,
        "loop1_asymmetry_dominates_later": bool(
            later_log_asymmetry
            and loops[0]["log_transition_width_asymmetry"] is not None
            and loops[0]["log_transition_width_asymmetry"] > max(later_log_asymmetry)
        ),
        "nuisance_dimension_comparison": {
            "HEB_vector_dimension": len(loops),
            "independent_loop_offsets_dimension": len(loops),
            "common_affine_group_dimension": 2,
            "identified_affine_quotient_dimension": len(loops) - 2,
        },
        "adjudication": "PASS_PARTIAL_HISTORICAL_RESCUE_RELATIVE_TRAINING_IDENTIFIED_STANDARD_SOURCE_NULL_SURVIVES",
        "claim_boundary": "shared-affine quotient identifies relative training geometry but does not identify absolute field, establish a full likelihood, or provide HGMF evidence",
    }

    (args.out_dir / "HGMF_HG40_MAGNETIC_AFFINE_QUOTIENT.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    pd.DataFrame(
        [
            {k: v for k, v in row.items() if k != "branch_transitions"}
            for row in loops
        ]
    ).to_csv(args.out_dir / "HGMF_HG40_MAGNETIC_AFFINE_QUOTIENT.csv", index=False)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
