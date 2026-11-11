#!/usr/bin/env python3
from __future__ import annotations

import math
from typing import Iterable, Sequence

import numpy as np


SAFE_RULES = {
    "carrier_local",
    "weighted_mean",
    "intersection_min",
    "sequential_conditional_product",
}


def union_upper_density(component_upper_values: Iterable[float]) -> float:
    x = np.asarray(list(component_upper_values), dtype=float)
    if x.ndim != 1 or x.size == 0 or np.any(x < 0) or not np.all(np.isfinite(x)):
        raise ValueError("finite nonnegative component bounds required")
    return float(np.max(x))


def evalue_from_upper(candidate_density: float, null_upper: float) -> float:
    g = float(candidate_density)
    u = float(null_upper)
    if not math.isfinite(g) or not math.isfinite(u) or g < 0 or u < 0:
        raise ValueError("finite nonnegative values required")
    if u == 0:
        return 0.0
    return g / u


def covariance_certificate(covariance: np.ndarray, eigenvalue_floor: float) -> dict:
    s = np.asarray(covariance, dtype=float)
    floor = float(eigenvalue_floor)
    if s.ndim != 2 or s.shape[0] != s.shape[1] or not np.all(np.isfinite(s)):
        raise ValueError("finite square covariance required")
    if floor <= 0:
        raise ValueError("positive eigenvalue floor required")
    s = (s + s.T) / 2.0
    eig = np.linalg.eigvalsh(s)
    minimum = float(np.min(eig))
    maximum = float(np.max(eig))
    passed = bool(minimum >= floor)
    condition = math.inf if minimum <= 0 else maximum / minimum
    return {
        "dimension": int(s.shape[0]),
        "minimum_eigenvalue": minimum,
        "maximum_eigenvalue": maximum,
        "condition_number": float(condition),
        "eigenvalue_floor": floor,
        "passed": passed,
    }


def minimum_clusters_full_covariance(quotient_dimension: int, mean_design_rank: int = 1) -> int:
    d = int(quotient_dimension)
    r = int(mean_design_rank)
    if d < 1 or r < 0:
        raise ValueError("invalid dimensions")
    return d + r


def admit_replicate_receipts(
    receipts: Sequence[dict],
    quotient_dimension: int,
    mean_design_rank: int,
    covariance_model: str,
    structured_covariance_proof_hash: str | None = None,
) -> dict:
    errors: list[str] = []
    blockers: list[str] = []
    ids, hashes = set(), set()
    clusters: dict[str, str] = {}

    for item in receipts:
        rid = item.get("replicate_id")
        ah = item.get("acquisition_hash")
        cid = item.get("independent_cluster_id")
        cert = item.get("independence_certificate_hash")
        ancestry = item.get("ancestry_hash")
        if not rid or rid in ids:
            errors.append("DUPLICATE_OR_MISSING_REPLICATE_ID")
        else:
            ids.add(rid)
        if not ah or ah in hashes:
            errors.append("DUPLICATE_OR_MISSING_ACQUISITION_HASH")
        else:
            hashes.add(ah)
        if item.get("holdout_values_accessed_before_arming") is True:
            errors.append("HOLDOUT_LEAKAGE")
        if not ancestry:
            blockers.append(f"MISSING_ANCESTRY_HASH_{rid}")
        if not cid:
            blockers.append(f"MISSING_CLUSTER_ID_{rid}")
        elif not cert:
            blockers.append(f"MISSING_CLUSTER_INDEPENDENCE_CERTIFICATE_{cid}")
        else:
            previous = clusters.get(cid)
            if previous is not None and previous != cert:
                errors.append(f"INCONSISTENT_CLUSTER_CERTIFICATE_{cid}")
            clusters[cid] = cert

    n_clusters = len(clusters)
    if covariance_model == "unrestricted_full":
        need = minimum_clusters_full_covariance(quotient_dimension, mean_design_rank)
        if n_clusters < need:
            blockers.append(f"REPLICATE_RANK_DEFICIT_{n_clusters}_LT_{need}")
    elif covariance_model == "structured":
        need = None
        if not structured_covariance_proof_hash:
            blockers.append("MISSING_STRUCTURED_COVARIANCE_PROOF")
    elif covariance_model == "known":
        need = None
    else:
        need = None
        errors.append("INVALID_COVARIANCE_MODEL")

    status = (
        "FAIL_INVALID_REPLICATE_RECEIPTS"
        if errors
        else ("ABSTAIN_REPLICATE_ADMISSION_INCOMPLETE" if blockers else "PASS_REPLICATE_ADMISSION")
    )
    return {
        "status": status,
        "errors": sorted(set(errors)),
        "blockers": sorted(set(blockers)),
        "rows_submitted": len(receipts),
        "independent_clusters": n_clusters,
        "minimum_clusters_required": need,
        "admitted": not errors and not blockers,
    }


def aggregate_evalues(
    evalues: Iterable[float],
    rule: str,
    weights: Iterable[float] | None = None,
    conditional_factor_proof: bool = False,
) -> float:
    e = np.asarray(list(evalues), dtype=float)
    if e.ndim != 1 or e.size == 0 or np.any(e < 0) or not np.all(np.isfinite(e)):
        raise ValueError("finite nonnegative e-values required")
    if rule not in SAFE_RULES:
        raise ValueError("unsafe aggregation rule")
    if rule == "carrier_local":
        if e.size != 1:
            raise ValueError("carrier_local accepts one e-value")
        return float(e[0])
    if rule == "intersection_min":
        return float(np.min(e))
    if rule == "weighted_mean":
        if weights is None:
            w = np.full(e.size, 1.0 / e.size)
        else:
            w = np.asarray(list(weights), dtype=float)
            if w.shape != e.shape or np.any(w < 0) or not np.isclose(w.sum(), 1.0):
                raise ValueError("weights must be nonnegative and sum to one")
        return float(w @ e)
    if not conditional_factor_proof:
        raise ValueError("conditional e-factor proof required")
    return float(np.prod(e))


def cantelli_power_lower(
    mean_log_increment_lower: float,
    variance_log_increment_upper: float,
    independent_clusters: int,
    threshold: float = 140.0,
) -> float:
    m = float(mean_log_increment_lower)
    v = float(variance_log_increment_upper)
    n = int(independent_clusters)
    tau = float(threshold)
    if m <= 0 or v < 0 or n < 1 or tau <= 1:
        raise ValueError("invalid power inputs")
    gap = n * m - math.log(tau)
    if gap <= 0:
        return 0.0
    return float(gap * gap / (n * v + gap * gap))


def minimum_clusters_cantelli(
    mean_log_increment_lower: float,
    variance_log_increment_upper: float,
    target_power: float,
    threshold: float = 140.0,
) -> int:
    m = float(mean_log_increment_lower)
    v = float(variance_log_increment_upper)
    p = float(target_power)
    tau = float(threshold)
    if m <= 0 or v < 0 or not (0 < p < 1) or tau <= 1:
        raise ValueError("invalid planning inputs")
    a = math.log(tau)
    kappa = p / (1.0 - p)
    c = math.sqrt(kappa * v)
    root = (c + math.sqrt(c * c + 4.0 * m * a)) / (2.0 * m)
    n = max(1, int(math.ceil(root * root)))
    while cantelli_power_lower(m, v, n, tau) < p:
        n += 1
    while n > 1 and cantelli_power_lower(m, v, n - 1, tau) >= p:
        n -= 1
    return n


def conjunction_power_lower(cell_power_lowers: Iterable[float]) -> float:
    p = np.asarray(list(cell_power_lowers), dtype=float)
    if p.ndim != 1 or p.size == 0 or np.any((p < 0) | (p > 1)):
        raise ValueError("cell powers must lie in [0,1]")
    return float(max(0.0, 1.0 - np.sum(1.0 - p)))


def _validate_density_certificate(cert: dict | None, carrier: str, measure_id: str, kind: str) -> list[str]:
    blockers: list[str] = []
    if not cert:
        return [f"MISSING_{carrier.upper()}_{kind.upper()}_CERTIFICATE"]
    if cert.get("measure_id") != measure_id:
        blockers.append(f"{carrier.upper()}_{kind.upper()}_MEASURE_MISMATCH")
    if not cert.get("proof_hash"):
        blockers.append(f"MISSING_{carrier.upper()}_{kind.upper()}_PROOF_HASH")
    if kind == "candidate_density" and cert.get("proper_density_certified") is not True:
        blockers.append(f"{carrier.upper()}_CANDIDATE_NOT_CERTIFIED_PROPER")
    if kind == "null_upper_density" and cert.get("upper_bound_certified") is not True:
        blockers.append(f"{carrier.upper()}_NULL_UPPER_NOT_CERTIFIED")
    if cert.get("training_only") is not True:
        blockers.append(f"{carrier.upper()}_{kind.upper()}_NOT_TRAINING_ONLY")
    return blockers


def validate_arming_dossier(dossier: dict) -> dict:
    errors: list[str] = []
    blockers: list[str] = []

    if dossier.get("profile") != "hgmf-hg43-arming-dossier/1.0":
        errors.append("PROFILE_MISMATCH")
    if dossier.get("stage") not in {"RECEIPT_CONDITIONED_UNARMED", "ARMED_FUTURE_ONLY"}:
        errors.append("INVALID_STAGE")
    if dossier.get("prospective_outcomes_present") is True:
        errors.append("PROSPECTIVE_OUTCOME_LEAKAGE")

    chart = dossier.get("chart", {})
    measure_id = chart.get("measure_id")
    for key in ("measure_id", "chart_hash", "orientation", "chart_transition_policy"):
        if chart.get(key) in (None, "", []):
            blockers.append(f"MISSING_CHART_{key.upper()}")
    anchors = chart.get("carrier_anchor_labels", {})
    for carrier in ("magnetism", "adsorption"):
        labels = anchors.get(carrier)
        if not isinstance(labels, list) or len(labels) != 2 or labels[0] == labels[1]:
            blockers.append(f"MISSING_OR_INVALID_{carrier.upper()}_ANCHORS")
    threshold = chart.get("degeneracy_threshold")
    if not isinstance(threshold, (int, float)) or threshold <= 0:
        blockers.append("MISSING_CHART_DEGENERACY_THRESHOLD")

    claim = dossier.get("claim", {})
    semantics = claim.get("semantics")
    rule = claim.get("aggregation_rule")
    if semantics not in {"carrier_local", "mixture_screening", "program_conjunction", "sequential"}:
        blockers.append("MISSING_CLAIM_SEMANTICS")
    if rule not in SAFE_RULES:
        blockers.append("MISSING_OR_UNSAFE_AGGREGATION_RULE")
    if semantics == "program_conjunction" and rule != "intersection_min":
        errors.append("CONJUNCTION_REQUIRES_INTERSECTION_MIN")
    if semantics == "mixture_screening" and rule != "weighted_mean":
        errors.append("MIXTURE_REQUIRES_WEIGHTED_MEAN")
    if semantics == "sequential" and rule != "sequential_conditional_product":
        errors.append("SEQUENTIAL_CLAIM_REQUIRES_CONDITIONAL_PRODUCT")
    if rule == "weighted_mean":
        w = np.asarray(claim.get("weights", []), dtype=float)
        if w.size == 0 or np.any(w < 0) or not np.isclose(w.sum(), 1.0):
            errors.append("INVALID_EVALUE_WEIGHTS")
    if rule == "sequential_conditional_product" and not claim.get("filtration_proof_hash"):
        blockers.append("MISSING_FILTRATION_PROOF")
    threshold_e = claim.get("threshold_evalue")
    if not isinstance(threshold_e, (int, float)) or threshold_e <= 1:
        blockers.append("MISSING_EVALUE_THRESHOLD")
    global_power_target = claim.get("global_power_target")
    if not isinstance(global_power_target, (int, float)) or not (0 < global_power_target < 1):
        blockers.append("MISSING_GLOBAL_POWER_TARGET")

    receipts = dossier.get("replicate_receipts", {})
    laws = dossier.get("carrier_laws", {})
    for carrier in ("magnetism", "adsorption"):
        law = laws.get(carrier, {})
        recs = receipts.get(carrier, [])
        admission = admit_replicate_receipts(
            recs,
            quotient_dimension=int(law.get("quotient_dimension", 1)),
            mean_design_rank=int(law.get("mean_design_rank", 1)),
            covariance_model=law.get("covariance_model", "invalid"),
            structured_covariance_proof_hash=law.get("structured_covariance_proof_hash"),
        )
        if not admission["admitted"]:
            blockers.extend(f"{carrier.upper()}_{x}" for x in admission["blockers"])
            errors.extend(f"{carrier.upper()}_{x}" for x in admission["errors"])
        blockers.extend(_validate_density_certificate(law.get("candidate_density"), carrier, measure_id, "candidate_density"))
        blockers.extend(_validate_density_certificate(law.get("null_upper_density"), carrier, measure_id, "null_upper_density"))
        if not law.get("covariance_finite_supremum_proof_hash"):
            blockers.append(f"MISSING_{carrier.upper()}_FINITE_SUPREMUM_PROOF")

    power = dossier.get("local_power", {})
    cells = power.get("cell_certificates", [])
    if not cells:
        blockers.append("MISSING_LOCAL_POWER_CERTIFICATES")
    else:
        beta_sum = 0.0
        for cell in cells:
            cid = cell.get("cell_id", "UNKNOWN")
            for key in ("mean_log_increment_lower", "variance_log_increment_upper", "independent_clusters", "target_power"):
                if cell.get(key) is None:
                    blockers.append(f"MISSING_POWER_FIELD_{cid}_{key.upper()}")
            if all(cell.get(key) is not None for key in ("mean_log_increment_lower", "variance_log_increment_upper", "independent_clusters", "target_power")):
                try:
                    p = cantelli_power_lower(
                        cell["mean_log_increment_lower"],
                        cell["variance_log_increment_upper"],
                        cell["independent_clusters"],
                        threshold_e if isinstance(threshold_e, (int, float)) and threshold_e > 1 else 140.0,
                    )
                    if p + 1e-12 < float(cell["target_power"]):
                        blockers.append(f"POWER_DEFICIT_{cid}")
                    beta_sum += 1.0 - float(cell["target_power"])
                except Exception:
                    errors.append(f"INVALID_POWER_CERTIFICATE_{cid}")
            if not cell.get("proof_hash"):
                blockers.append(f"MISSING_POWER_PROOF_HASH_{cid}")
        if semantics == "program_conjunction" and isinstance(global_power_target, (int, float)):
            if 1.0 - beta_sum + 1e-12 < global_power_target:
                blockers.append("CONJUNCTION_BETA_BUDGET_EXCEEDS_GLOBAL_TARGET")

    frozen = dossier.get("frozen_artifacts", {})
    for key in ("code_hash", "environment_hash", "design_hash", "model_hash", "split_hash"):
        if not frozen.get(key):
            blockers.append(f"MISSING_FROZEN_{key.upper()}")

    armed = dossier.get("stage") == "ARMED_FUTURE_ONLY"
    authority = dossier.get("acquisition_authorized") is True
    if authority and not armed:
        errors.append("AUTHORITY_WITHOUT_ARMING")
    complete = not errors and not blockers
    authorized = bool(complete and armed and authority)
    if errors:
        status = "FAIL_INVALID_ARMING_DOSSIER"
    elif blockers:
        status = "ABSTAIN_REAL_RECEIPTS_DENSITIES_OR_POWER_MISSING"
    elif not armed:
        status = "ABSTAIN_COMPLETE_BUT_NOT_ARMED"
    elif not authority:
        status = "ABSTAIN_ARMED_WITHOUT_ACQUISITION_AUTHORITY"
    else:
        status = "PASS_ARMED_RECEIPT_CONDITIONED_QUOTIENT_EVALUE"

    return {
        "profile": "hgmf-hg43-adjudication/1.0",
        "status": status,
        "authorized": authorized,
        "errors": sorted(set(errors)),
        "blockers": sorted(set(blockers)),
    }
