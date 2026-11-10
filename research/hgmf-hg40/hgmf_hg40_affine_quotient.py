#!/usr/bin/env python3
from __future__ import annotations

import math
from typing import Iterable

import numpy as np
from scipy.optimize import brentq


def affine_coordinates(values: Iterable[float], anchor_a: int, anchor_b: int) -> np.ndarray:
    """Maximal affine coordinates relative to two labelled anchors.

    For y' = alpha + beta*y, beta != 0, these coordinates are unchanged.
    """
    y = np.asarray(list(values), dtype=float)
    if y.ndim != 1 or y.size < 3:
        raise ValueError("need a one-dimensional configuration with at least three values")
    if not (0 <= anchor_a < y.size and 0 <= anchor_b < y.size) or anchor_a == anchor_b:
        raise ValueError("invalid anchors")
    den = float(y[anchor_b] - y[anchor_a])
    if den == 0:
        raise ValueError("anchor values must be distinct")
    return (y - y[anchor_a]) / den


def cross_ratio(a: float, b: float, c: float, d: float) -> float:
    """Affine/projective cross-ratio, defined when denominators are nonzero."""
    den = (a - d) * (b - c)
    if den == 0:
        raise ValueError("degenerate cross-ratio")
    return float(((a - c) * (b - d)) / den)


def magnetic_affine_metrics(c1: Iterable[float], c2: Iterable[float]) -> dict:
    """Common-affine-field invariants for a loop family."""
    x1 = np.asarray(list(c1), dtype=float)
    x2 = np.asarray(list(c2), dtype=float)
    if x1.shape != x2.shape or x1.ndim != 1 or x1.size < 3:
        raise ValueError("coercive arrays must be aligned one-dimensional vectors")
    h = (x1 + x2) / 2.0
    w = np.abs(x2 - x1) / 2.0
    if np.any(w <= 0):
        raise ValueError("positive coercive half-widths required")
    later_h = h[1:]
    later_w = w[1:]
    hbar = float(np.mean(later_h))
    wbar = float(np.mean(later_w))
    return {
        "HEB": h,
        "halfwidth": w,
        "trained_mean_HEB": hbar,
        "trained_mean_halfwidth": wbar,
        "loop1_training_contrast": float((h[0] - hbar) / wbar),
        "trained_centered_coordinates": ((later_h - hbar) / wbar),
        "HEB_affine_coordinates": affine_coordinates(h, 0, 1),
        "quotient_dimension": int(h.size - 2),
    }


def _bethe_y(q: float, qplus: float, z: float) -> float:
    if not (0.0 <= q <= 1.0 and 0.0 <= qplus < 1.0 and z > 2.0):
        raise ValueError("invalid Bethe parameters")

    def f(y: float) -> float:
        return (1.0 - q) + q * (1.0 - qplus) * y ** (z - 1.0) - y

    if q == 0.0:
        return 1.0
    if qplus > 0.0:
        return float(brentq(f, 0.0, 1.0, xtol=1e-14, rtol=1e-14))
    qc = 1.0 / (z - 1.0)
    if q <= qc:
        return 1.0
    if q >= 1.0:
        return 0.0
    ycrit = (1.0 / (q * (z - 1.0))) ** (1.0 / (z - 2.0))
    return float(brentq(f, 0.0, ycrit, xtol=1e-14, rtol=1e-14))


def bethe_scan_state(q: float, qplus: float, z: float) -> dict:
    """Bethe scanning-desorption state and dQminus/dQplus on the stable branch."""
    y = _bethe_y(q, qplus, z)
    qminus = 1.0 - (1.0 - qplus) * y**z
    stability = 1.0 - q * (1.0 - qplus) * (z - 1.0) * y ** (z - 2.0)
    if stability <= 0.0:
        raise RuntimeError("non-stable Bethe branch")
    dy_dqplus = -q * y ** (z - 1.0) / stability
    derivative = y**z - (1.0 - qplus) * z * y ** (z - 1.0) * dy_dqplus
    return {
        "y": float(y),
        "Qminus": float(qminus),
        "stability": float(stability),
        "dQminus_dQplus": float(derivative),
    }


def verify_bethe_no_passing_grid() -> dict:
    closed_minimum = math.inf
    interior_minimum = math.inf
    closed_count = 0
    interior_count = 0
    for z in np.linspace(6.6, 7.2, 7):
        for q in np.linspace(0.0, 1.0, 101):
            for qplus in np.linspace(0.01, 0.95, 48):
                ans = bethe_scan_state(float(q), float(qplus), float(z))
                derivative = ans["dQminus_dQplus"]
                closed_minimum = min(closed_minimum, derivative)
                closed_count += 1
                if 0.0 < q < 1.0:
                    interior_minimum = min(interior_minimum, derivative)
                    interior_count += 1
    return {
        "closed_grid_points": closed_count,
        "interior_grid_points": interior_count,
        "minimum_dQminus_dQplus_closed": float(closed_minimum),
        "minimum_dQminus_dQplus_interior": float(interior_minimum),
        "nonnegative_on_closed_grid": bool(closed_minimum >= -1e-13),
        "strictly_positive_interior": bool(interior_minimum > 0.0),
    }
