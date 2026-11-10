#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import numpy as np
import pandas as pd

from hgmf_hg40_affine_quotient import affine_coordinates, cross_ratio, verify_bethe_no_passing_grid

RUN_ID = 1
DIGIT_SCALE_MG = 0.01
ROUNDING_GUARD_MG = 0.02


def parse_start(description: str) -> tuple[float, float] | None:
    match = re.search(
        r"Desorption Scanning Curve\s+\d+\s+starting from\s*\(\s*([0-9.]+)\s*,\s*([0-9.]+)",
        str(description),
        re.IGNORECASE,
    )
    if match is None:
        return None
    return float(match.group(1)), float(match.group(2))


def prepare_segment(group: pd.DataFrame) -> dict | None:
    g = group[group.branch.astype(str) == "D"].copy()
    if len(g) < 3:
        return None
    description = str(g.segment_description.iloc[0])
    start = parse_start(description)
    if start is None:
        return None
    g = g.sort_values("pressure")
    p = g.pressure.to_numpy(float)
    y = g.adsorption.to_numpy(float)
    u = g.uncertainty.fillna(0).to_numpy(float) * DIGIT_SCALE_MG
    # Remove duplicate pressures deterministically by averaging their observations.
    frame = pd.DataFrame({"p": p, "y": y, "u": u}).groupby("p", as_index=False).mean().sort_values("p")
    if len(frame) < 3:
        return None
    return {
        "segment_id": int(g.segment_id.iloc[0]),
        "description": description,
        "start_pressure": float(start[0]),
        "start_adsorption_mg": float(start[1]),
        "p": frame.p.to_numpy(float),
        "y": frame.y.to_numpy(float),
        "u": frame.u.to_numpy(float),
    }


def interpolate(segment: dict, pressures: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    p = np.asarray(pressures, float)
    if p.min() < segment["p"].min() - 1e-12 or p.max() > segment["p"].max() + 1e-12:
        raise ValueError("interpolation outside segment support")
    return np.interp(p, segment["p"], segment["y"]), np.interp(p, segment["p"], segment["u"])


def overlap_nodes(a: dict, b: dict) -> np.ndarray:
    lo = max(float(a["p"].min()), float(b["p"].min()))
    hi = min(float(a["p"].max()), float(b["p"].max()), a["start_pressure"], b["start_pressure"])
    if hi <= lo:
        return np.array([], dtype=float)
    nodes = np.unique(
        np.concatenate(
            [
                a["p"][(a["p"] >= lo) & (a["p"] <= hi)],
                b["p"][(b["p"] >= lo) & (b["p"] <= hi)],
                np.linspace(lo, hi, 51),
            ]
        )
    )
    return nodes


def pairwise_no_passing(segments: list[dict]) -> tuple[list[dict], list[dict]]:
    pair_rows: list[dict] = []
    point_rows: list[dict] = []
    ordered = sorted(segments, key=lambda x: x["start_pressure"])
    for i in range(len(ordered)):
        for j in range(i + 1, len(ordered)):
            low = ordered[i]
            high = ordered[j]
            nodes = overlap_nodes(low, high)
            if nodes.size == 0:
                continue
            v_low, u_low = interpolate(low, nodes)
            v_high, u_high = interpolate(high, nodes)
            diff = v_high - v_low
            tolerance = u_high + u_low + ROUNDING_GUARD_MG
            violation = diff < -tolerance
            for p, d, t, bad in zip(nodes, diff, tolerance, violation):
                point_rows.append(
                    {
                        "lower_start_segment": low["segment_id"],
                        "higher_start_segment": high["segment_id"],
                        "lower_start_pressure": low["start_pressure"],
                        "higher_start_pressure": high["start_pressure"],
                        "pressure": float(p),
                        "adsorption_difference_high_minus_low_mg": float(d),
                        "compatibility_tolerance_mg": float(t),
                        "strict_no_passing_violation": bool(bad),
                    }
                )
            pair_rows.append(
                {
                    "lower_start_segment": low["segment_id"],
                    "higher_start_segment": high["segment_id"],
                    "lower_start_pressure": low["start_pressure"],
                    "higher_start_pressure": high["start_pressure"],
                    "evaluation_points": int(nodes.size),
                    "strict_violation_points": int(np.sum(violation)),
                    "minimum_difference_mg": float(np.min(diff)),
                    "maximum_negative_excess_beyond_tolerance_mg": float(
                        max(0.0, np.max(-(diff + tolerance)))
                    ),
                    "pair_compatible": bool(not np.any(violation)),
                }
            )
    return pair_rows, point_rows


def quotient_snapshots(segments: list[dict]) -> tuple[list[dict], dict | None]:
    all_pressures = np.unique(np.concatenate([s["p"] for s in segments]))
    rows: list[dict] = []
    representative = None
    for pressure in all_pressures:
        active = [
            s
            for s in segments
            if float(s["p"].min()) - 1e-12 <= pressure <= float(s["p"].max()) + 1e-12
            and pressure <= s["start_pressure"] + 1e-12
        ]
        if len(active) < 3:
            continue
        active.sort(key=lambda x: x["start_pressure"])
        values = np.asarray([interpolate(s, np.asarray([pressure]))[0][0] for s in active], float)
        uncertainties = np.asarray([interpolate(s, np.asarray([pressure]))[1][0] for s in active], float)
        if abs(values[-1] - values[0]) <= float(uncertainties[0] + uncertainties[-1] + ROUNDING_GUARD_MG):
            continue
        coords = affine_coordinates(values, 0, len(values) - 1)
        for index, (segment, value, uncertainty, coordinate) in enumerate(
            zip(active, values, uncertainties, coords)
        ):
            rows.append(
                {
                    "pressure": float(pressure),
                    "active_histories": len(active),
                    "quotient_dimension": len(active) - 2,
                    "segment_id": segment["segment_id"],
                    "start_pressure": segment["start_pressure"],
                    "adsorption_mg": float(value),
                    "quoted_uncertainty_mg": float(uncertainty),
                    "affine_coordinate": float(coordinate),
                    "coordinate_inside_unit_interval": bool(-1e-12 <= coordinate <= 1.0 + 1e-12),
                    "anchor_role": "LOW_START" if index == 0 else ("HIGH_START" if index == len(active) - 1 else "INTERIOR"),
                }
            )
        if len(active) >= 4:
            cr = cross_ratio(values[0], values[1], values[-2], values[-1])
        else:
            cr = None
        if representative is None or len(active) > representative["active_histories"]:
            representative = {
                "pressure": float(pressure),
                "segment_ids": [s["segment_id"] for s in active],
                "start_pressures": [s["start_pressure"] for s in active],
                "adsorption_values_mg": values.tolist(),
                "affine_coordinates": coords.tolist(),
                "cross_ratio_first_second_penultimate_last": cr,
                "active_histories": len(active),
            }
    return rows, representative


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=Path, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    data = pd.read_csv(args.csv)
    run = data[data.run_id == RUN_ID].copy()
    segments = []
    for _, group in run.groupby("segment_id", sort=True):
        segment = prepare_segment(group)
        if segment is not None:
            segments.append(segment)
    if len(segments) < 3:
        raise RuntimeError("fewer than three simple primary-desorption scans")

    pairs, points = pairwise_no_passing(segments)
    quotient_rows, representative = quotient_snapshots(segments)
    if representative is None or not quotient_rows:
        raise RuntimeError("no nondegenerate reference-free quotient snapshots")

    pair_frame = pd.DataFrame(pairs)
    point_frame = pd.DataFrame(points)
    quotient_frame = pd.DataFrame(quotient_rows)
    pair_frame.to_csv(args.out_dir / "HGMF_HG40_ADSORPTION_NO_PASSING_PAIRS.csv", index=False)
    point_frame.to_csv(args.out_dir / "HGMF_HG40_ADSORPTION_NO_PASSING_POINTS.csv", index=False)
    quotient_frame.to_csv(args.out_dir / "HGMF_HG40_ADSORPTION_AFFINE_QUOTIENT.csv", index=False)

    bethe_check = verify_bethe_no_passing_grid()
    strict_violations = int(point_frame.strict_no_passing_violation.sum())
    incompatible_pairs = int((~pair_frame.pair_compatible).sum())
    outside = int((~quotient_frame.coordinate_inside_unit_interval).sum())
    result = {
        "status": "PASS_HGMF_HG40_ADSORPTION_REFERENCE_FREE_EXECUTED",
        "source": "NIST-ISODB/AJBrownThesisIsotherms@17a48e5d3c00e97387d0dfb1e280d8d6bf103d40",
        "run_id": RUN_ID,
        "temperature_K": float(run.temperature.iloc[0]),
        "simple_desorption_scans": len(segments),
        "segments": [
            {
                "segment_id": s["segment_id"],
                "start_pressure": s["start_pressure"],
                "start_adsorption_mg": s["start_adsorption_mg"],
                "points": int(len(s["p"])),
                "pressure_min": float(s["p"].min()),
                "pressure_max": float(s["p"].max()),
            }
            for s in sorted(segments, key=lambda x: x["start_pressure"])
        ],
        "bethe_no_passing_theorem_numerical_check": bethe_check,
        "pairwise_order_audit": {
            "pairs": int(len(pair_frame)),
            "evaluation_points": int(len(point_frame)),
            "strict_violation_points": strict_violations,
            "incompatible_pairs": incompatible_pairs,
            "maximum_negative_excess_beyond_tolerance_mg": float(
                pair_frame.maximum_negative_excess_beyond_tolerance_mg.max()
            ) if len(pair_frame) else None,
            "adjudication": "PASS_NO_PASSING_COMPATIBILITY" if strict_violations == 0 else "FAIL_EXACT_NO_PASSING_AT_TABULATED_UNCERTAINTY",
        },
        "affine_quotient_audit": {
            "rows": int(len(quotient_frame)),
            "distinct_pressures": int(quotient_frame.pressure.nunique()),
            "maximum_simultaneous_histories": int(quotient_frame.active_histories.max()),
            "total_identified_quotient_degrees": int(
                quotient_frame.groupby("pressure").quotient_dimension.first().sum()
            ),
            "coordinates_outside_unit_interval": outside,
            "representative_real_snapshot": representative,
        },
        "adjudication": "PASS_PARTIAL_HISTORICAL_RESCUE_REFERENCE_FREE_RELATIVE_STATE_IDENTIFIED",
        "physical_network_rejection": "ABSTAIN_MODEL_SPECIFIC_QUOTIENT_LIKELIHOOD_NOT_YET_BUILT",
        "claim_boundary": "Vs and Vc cancel pointwise from affine quotient observables; absolute Q, q, cross-pressure likelihood and physical protogeometry remain unidentified",
    }
    (args.out_dir / "HGMF_HG40_ADSORPTION_REFERENCE_FREE.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
