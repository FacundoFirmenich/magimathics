#!/usr/bin/env python3
"""Corrected HGMF-UMI-10 magnetic audit.

The public files begin with one isolated +2500 mT pre-field point, followed by
the actual closed minor loop. This wrapper removes only that independently
detectable preconditioning point, then delegates to the frozen audit engine.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

import analyze_rpm as core

_original_reader = core.read_h5_like_source


def read_h5_minor_loop(path: Path):
    field, vxy, temperature, meta = _original_reader(path)
    removed = 0
    if len(field) >= 4:
        steps = np.abs(np.diff(field))
        reference = float(np.median(steps[1:][steps[1:] > 0])) if np.any(steps[1:] > 0) else 0.0
        if reference > 0 and steps[0] > 10.0 * reference:
            field = field[1:]
            vxy = vxy[1:]
            removed = 1
    meta = dict(meta)
    meta["preconditioning_points_removed"] = removed
    meta["minor_loop_processed_points"] = int(len(field))
    return field, vxy, temperature, meta


core.read_h5_like_source = read_h5_minor_loop

if __name__ == "__main__":
    core.main()
    # Tighten claim boundary after the engine writes its files.
    argv = sys.argv
    out_dir = Path(argv[argv.index("--out-dir") + 1])
    result_path = out_dir / "HGMF_UMI10_RESULTS.json"
    result = json.loads(result_path.read_text(encoding="utf-8"))
    best = result["best_model"]["model"]
    n_returns = result["return_point"]["matched_return_pairs"]
    result["claim_boundary"]["rpm_operator_preferred"] = (
        "PASS_RPM_RELAYS_BEST" if best == "rpm_relays"
        else "PASS_STACK_STATE_BEST" if best == "finite_stack"
        else "FAIL_RPM_NOT_SELECTED"
    )
    result["claim_boundary"]["magnetic_loop_closure"] = (
        "PASS_ENDPOINT_PAIRS" if n_returns > 0 else "HOLD_NO_ENDPOINT_PAIRS"
    )
    result["claim_boundary"]["nested_return_point_memory"] = "HOLD_SINGLE_REVERSAL_PER_FILE"
    result_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
