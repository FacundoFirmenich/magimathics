#!/usr/bin/env python3
from __future__ import annotations
import numpy as np


def affine_quotient(y, r=0, s=1, tol=1e-12):
    x = np.asarray(list(y), dtype=float)
    if x.ndim != 1 or x.size < 3 or not np.all(np.isfinite(x)):
        raise ValueError("finite one-dimensional vector with m>=3 required")
    if r == s or not (0 <= r < x.size and 0 <= s < x.size):
        raise ValueError("invalid anchors")
    d = float(x[s] - x[r])
    if abs(d) <= tol:
        raise ValueError("ANCHOR_DEGENERACY")
    idx = [i for i in range(x.size) if i not in (r, s)]
    rho = np.asarray([(x[i] - x[r]) / d for i in idx], dtype=float)
    return rho, idx


def affine_reconstruct(u, v, rho, m, r=0, s=1, tol=1e-12):
    if m < 3 or r == s or not (0 <= r < m and 0 <= s < m):
        raise ValueError("invalid chart")
    if abs(v) <= tol:
        raise ValueError("ANCHOR_DEGENERACY")
    rho = np.asarray(list(rho), dtype=float)
    idx = [i for i in range(m) if i not in (r, s)]
    if rho.size != m - 2:
        raise ValueError("rho dimension mismatch")
    y = np.empty(m, dtype=float)
    y[r] = u
    y[s] = u + v
    for i, q in zip(idx, rho):
        y[i] = u + v * q
    return y


def quotient_inverse_jacobian_abs(v, m):
    if m < 3:
        raise ValueError("m>=3 required")
    return abs(float(v)) ** (m - 2)


def quotient_gradient(y, r=0, s=1, tol=1e-12):
    x = np.asarray(list(y), dtype=float)
    rho, idx = affine_quotient(x, r=r, s=s, tol=tol)
    d = float(x[s] - x[r])
    G = np.zeros((len(idx), len(x)), dtype=float)
    for row, (i, q) in enumerate(zip(idx, rho)):
        G[row, i] = 1.0 / d
        G[row, r] = (q - 1.0) / d
        G[row, s] = -q / d
    return G, idx


def quotient_covariance(y, covariance, r=0, s=1):
    x = np.asarray(list(y), dtype=float)
    S = np.asarray(covariance, dtype=float)
    if S.shape != (x.size, x.size):
        raise ValueError("covariance shape mismatch")
    G, _ = quotient_gradient(x, r=r, s=s)
    return G @ S @ G.T


def interval_intersection(centers, halfwidths):
    c = np.asarray(list(centers), dtype=float)
    h = np.asarray(list(halfwidths), dtype=float)
    if c.shape != h.shape or c.ndim != 1 or np.any(h < 0):
        raise ValueError("invalid intervals")
    lo = float(np.max(c - h))
    hi = float(np.min(c + h))
    return bool(lo <= hi), lo, hi


def magnetic_equal_trained_feasible(observed_heb, halfwidths, trained_indices=(1, 2, 3, 4)):
    h = np.asarray(list(observed_heb), dtype=float)
    d = np.asarray(list(halfwidths), dtype=float)
    idx = np.asarray(list(trained_indices), dtype=int)
    ok, lo, hi = interval_intersection(h[idx], d[idx])
    return {
        "feasible": ok,
        "common_trained_interval_lo": lo,
        "common_trained_interval_hi": hi,
        "common_trained_interval_width": hi - lo,
        "support_only_evalue_ceiling": 1.0 if ok else None,
    }


def discrete_universal_evalue(candidate_density, null_densities):
    g = np.asarray(list(candidate_density), dtype=float)
    Q = np.asarray(null_densities, dtype=float)
    if Q.ndim != 2 or Q.shape[1] != g.size:
        raise ValueError("shape mismatch")
    if np.any(g < 0) or np.any(Q < 0):
        raise ValueError("negative mass")
    if not np.isclose(g.sum(), 1.0):
        raise ValueError("candidate must be proper")
    if not np.allclose(Q.sum(axis=1), 1.0):
        raise ValueError("null rows must be proper")
    U = np.max(Q, axis=0)
    E = np.divide(g, U, out=np.zeros_like(g), where=U > 0)
    expectations = Q @ E
    return {
        "envelope": U,
        "evalue": E,
        "null_expectations": expectations,
        "valid": bool(np.all(expectations <= 1.0 + 1e-12)),
    }


def support_only_pointwise_ceiling(feasible):
    return 1.0 if feasible else None
