#!/usr/bin/env python3
from __future__ import annotations

import math
from typing import Iterable

import numpy as np


def calibration_augmented_discrete_evalue(candidate_joint_mass: Iterable[float], null_joint_masses: np.ndarray) -> dict:
    """Finite-space fixture for the calibration-augmented split e-value theorem."""
    g = np.asarray(list(candidate_joint_mass), dtype=float)
    q = np.asarray(null_joint_masses, dtype=float)
    if g.ndim != 1 or q.ndim != 2 or q.shape[1] != g.size:
        raise ValueError("shape mismatch")
    if np.any(g < 0) or np.any(q < 0):
        raise ValueError("negative mass")
    if not np.isclose(g.sum(), 1.0):
        raise ValueError("candidate must be proper")
    if not np.allclose(q.sum(axis=1), 1.0):
        raise ValueError("every null row must be proper")
    upper = np.max(q, axis=0)
    e = np.divide(g, upper, out=np.zeros_like(g), where=upper > 0)
    expectations = q @ e
    return {"candidate": g, "null_upper": upper, "evalue": e, "null_expectations": expectations, "valid": bool(np.all(expectations <= 1.0 + 1e-12))}


def weighted_e_mean(evalues: Iterable[float], weights: Iterable[float] | None = None) -> float:
    e = np.asarray(list(evalues), dtype=float)
    if e.ndim != 1 or e.size == 0 or np.any(e < 0):
        raise ValueError("nonnegative e-values required")
    if weights is None:
        w = np.full(e.size, 1.0 / e.size)
    else:
        w = np.asarray(list(weights), dtype=float)
        if w.shape != e.shape or np.any(w < 0) or not np.isclose(w.sum(), 1.0):
            raise ValueError("weights must be nonnegative and sum to one")
    return float(w @ e)


def intersection_min_evalue(evalues: Iterable[float]) -> float:
    e = np.asarray(list(evalues), dtype=float)
    if e.ndim != 1 or e.size == 0 or np.any(e < 0):
        raise ValueError("nonnegative e-values required")
    return float(np.min(e))


def sequential_product(e_factors: Iterable[float]) -> float:
    e = np.asarray(list(e_factors), dtype=float)
    if e.ndim != 1 or np.any(e < 0):
        raise ValueError("nonnegative factors required")
    return float(np.prod(e))


def dependent_product_counterexample() -> dict:
    probability = np.array([0.5, 0.5])
    e1 = np.array([0.0, 2.0])
    e2 = np.array([0.0, 2.0])
    return {"E1_expectation": float(probability @ e1), "E2_expectation": float(probability @ e2), "product_expectation": float(probability @ (e1 * e2)), "mean_expectation": float(probability @ ((e1 + e2) / 2.0)), "min_expectation": float(probability @ np.minimum(e1, e2))}


def gaussian_common_mean_profile_loglik(samples: np.ndarray, tol: float = 1e-12) -> dict:
    x = np.asarray(samples, dtype=float)
    if x.ndim != 2 or x.shape[0] < 1 or x.shape[1] < 1 or not np.all(np.isfinite(x)):
        raise ValueError("finite n x d sample matrix required")
    n, d = x.shape
    mu = np.mean(x, axis=0)
    r = x - mu
    scatter = r.T @ r
    rank = int(np.linalg.matrix_rank(scatter, tol))
    if rank < d:
        return {"n": n, "d": d, "residual_rank": rank, "finite_supremum": False, "profile_loglik": math.inf}
    sigma_hat = scatter / n
    sign, logdet = np.linalg.slogdet(sigma_hat)
    if sign <= 0:
        raise RuntimeError("positive definite scatter expected")
    ll = -0.5 * n * (d * (math.log(2.0 * math.pi) + 1.0) + logdet)
    return {"n": n, "d": d, "residual_rank": rank, "finite_supremum": True, "profile_loglik": float(ll), "mean_hat": mu, "covariance_hat": sigma_hat}


def minimum_replicates_full_covariance(quotient_dimension: int, mean_design_rank: int = 1) -> int:
    d = int(quotient_dimension); r = int(mean_design_rank)
    if d < 1 or r < 0:
        raise ValueError("invalid dimensions")
    return d + r


def linear_operator_covariance(raw_covariance: np.ndarray, interpolation_operator: np.ndarray, quotient_jacobian: np.ndarray) -> np.ndarray:
    s = np.asarray(raw_covariance, dtype=float); a = np.asarray(interpolation_operator, dtype=float); g = np.asarray(quotient_jacobian, dtype=float)
    if s.ndim != 2 or s.shape[0] != s.shape[1]: raise ValueError("raw covariance must be square")
    if a.ndim != 2 or a.shape[1] != s.shape[0]: raise ValueError("interpolation shape mismatch")
    if g.ndim != 2 or g.shape[1] != a.shape[0]: raise ValueError("quotient Jacobian shape mismatch")
    return g @ a @ s @ a.T @ g.T


def pushforward_discrete_mass(mass: Iterable[float], labels: Iterable[int]) -> tuple[np.ndarray, np.ndarray]:
    p = np.asarray(list(mass), dtype=float); lab = np.asarray(list(labels))
    if p.ndim != 1 or lab.shape != p.shape or np.any(p < 0): raise ValueError("invalid finite mass or labels")
    if not np.isclose(p.sum(), 1.0): raise ValueError("mass must be proper")
    unique = np.unique(lab)
    out = np.asarray([p[lab == u].sum() for u in unique], dtype=float)
    return unique, out


SAFE_AGGREGATION_RULES = {"weighted_mean", "intersection_min", "sequential_conditional_product"}


def validate_prospective_seal(seal: dict) -> dict:
    errors, blockers = [], []
    if seal.get("profile") != "hgmf-hg42-prospective-seal/1.0": errors.append("PROFILE_MISMATCH")
    if seal.get("stage") not in {"PROTOCOL_FROZEN_UNARMED", "ARMED_FUTURE_ONLY"}: errors.append("INVALID_STAGE")
    chart = seal.get("chart_seal", {})
    for key in ("measure_id", "anchor_labels", "orientation", "chart_transition_policy"):
        if chart.get(key) in (None, "", []): errors.append(f"MISSING_CHART_{key.upper()}")
    if chart.get("degeneracy_threshold") is None: blockers.append("MISSING_CHART_DEGENERACY_THRESHOLD")
    partitions = seal.get("partitions", {})
    train, hold, calib = set(partitions.get("training_ids", [])), set(partitions.get("holdout_ids", [])), set(partitions.get("calibration_ids", []))
    if train & hold or train & calib or hold & calib: errors.append("PARTITION_OVERLAP")
    if partitions.get("holdout_values_present_before_arming") is True: errors.append("HOLDOUT_LEAKAGE")
    measure_id = chart.get("measure_id")
    candidate, null = seal.get("candidate_density", {}), seal.get("null_upper_density", {})
    if candidate.get("measure_id") not in (None, measure_id): errors.append("CANDIDATE_MEASURE_MISMATCH")
    if null.get("measure_id") not in (None, measure_id): errors.append("NULL_MEASURE_MISMATCH")
    if not candidate.get("proper_density_proof_hash"): blockers.append("MISSING_PROPER_CANDIDATE_DENSITY")
    if not null.get("certified_upper_bound_proof_hash"): blockers.append("MISSING_NULL_UPPER_DENSITY")
    combination = seal.get("combination", {}); rule = combination.get("rule")
    if rule not in SAFE_AGGREGATION_RULES: errors.append("UNSAFE_AGGREGATION_RULE")
    if rule == "sequential_conditional_product" and not combination.get("filtration_proof_hash"): blockers.append("MISSING_CONDITIONAL_EFACTOR_PROOF")
    if rule == "weighted_mean" and combination.get("weights") is not None:
        w = np.asarray(combination["weights"], dtype=float)
        if np.any(w < 0) or not np.isclose(w.sum(), 1.0): errors.append("INVALID_EVALUE_WEIGHTS")
    for carrier in ("magnetism", "adsorption"):
        law = seal.get("noise_laws", {}).get(carrier, {})
        if not law.get("real_replicate_receipt_hash"): blockers.append(f"MISSING_{carrier.upper()}_REAL_REPLICATES")
        d, n, mean_rank, cov_model = law.get("quotient_dimension"), law.get("independent_replicates"), law.get("mean_design_rank", 1), law.get("covariance_model")
        if cov_model == "unrestricted_full":
            if not isinstance(d, int) or not isinstance(n, int): blockers.append(f"MISSING_{carrier.upper()}_REPLICATE_DIMENSIONS")
            else:
                need = minimum_replicates_full_covariance(d, mean_rank)
                if n < need: blockers.append(f"{carrier.upper()}_REPLICATE_RANK_DEFICIT_{n}_LT_{need}")
        if cov_model == "structured" and not law.get("structured_covariance_proof_hash"): blockers.append(f"MISSING_{carrier.upper()}_STRUCTURED_COVARIANCE_PROOF")
    armed = seal.get("stage") == "ARMED_FUTURE_ONLY"
    authorized = not errors and not blockers and armed and seal.get("acquisition_authorized") is True
    if seal.get("acquisition_authorized") is True and not armed:
        errors.append("AUTHORITY_WITHOUT_ARMING"); authorized = False
    status = "FAIL_INVALID_PROSPECTIVE_SEAL" if errors else ("ABSTAIN_REAL_REPLICATES_OR_DENSITY_PROOFS_MISSING" if blockers else ("ABSTAIN_NOT_ARMED" if not armed else "PASS_ARMED_QUOTIENT_EVALUE"))
    return {"profile": "hgmf-hg42-adjudication/1.0", "status": status, "authorized": authorized, "errors": errors, "blockers": blockers}
