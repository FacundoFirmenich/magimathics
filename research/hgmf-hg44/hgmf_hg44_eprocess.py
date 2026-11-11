#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from typing import Iterable, Mapping, Sequence

import numpy as np


STATES = {
    "PROTOCOL_FROZEN_UNARMED",
    "ARMED_FUTURE_ONLY",
    "ACQUIRING_EPOCH",
    "PAUSED_RECALIBRATION",
    "TERMINAL_PASS",
    "TERMINAL_FAIL",
    "TERMINAL_ABSTAIN",
}

ALLOWED_TRANSITIONS = {
    "PROTOCOL_FROZEN_UNARMED": {"ARMED_FUTURE_ONLY", "TERMINAL_FAIL", "TERMINAL_ABSTAIN"},
    "ARMED_FUTURE_ONLY": {"ACQUIRING_EPOCH", "TERMINAL_FAIL", "TERMINAL_ABSTAIN"},
    "ACQUIRING_EPOCH": {
        "PAUSED_RECALIBRATION", "TERMINAL_PASS",
        "TERMINAL_FAIL", "TERMINAL_ABSTAIN",
    },
    "PAUSED_RECALIBRATION": {"ACQUIRING_EPOCH", "TERMINAL_FAIL", "TERMINAL_ABSTAIN"},
    "TERMINAL_PASS": set(),
    "TERMINAL_FAIL": set(),
    "TERMINAL_ABSTAIN": set(),
}


def canonical_json_hash(obj: Mapping) -> str:
    payload = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def chained_event_hash(prior_hash: str | None, event_body: Mapping) -> str:
    payload = {
        "prior_event_hash": prior_hash,
        "event_body": event_body,
    }
    return canonical_json_hash(payload)


def e_factor(candidate_density: float, null_upper_density: float) -> float:
    g = float(candidate_density)
    u = float(null_upper_density)
    if not (math.isfinite(g) and math.isfinite(u)) or g < 0 or u < 0:
        raise ValueError("finite nonnegative densities required")
    if u == 0:
        return 0.0
    return g / u


def predictable_mixture(factors: Iterable[float], weights: Iterable[float]) -> float:
    e = np.asarray(list(factors), dtype=float)
    w = np.asarray(list(weights), dtype=float)
    if e.ndim != 1 or w.shape != e.shape or e.size == 0:
        raise ValueError("shape mismatch")
    if np.any(e < 0) or np.any(w < 0) or not np.all(np.isfinite(e)) or not np.all(np.isfinite(w)):
        raise ValueError("finite nonnegative values required")
    if not np.isclose(w.sum(), 1.0):
        raise ValueError("weights must sum to one")
    return float(w @ e)


def predictable_quarantine(factor: float, active: bool) -> float:
    e = float(factor)
    if e < 0 or not math.isfinite(e):
        raise ValueError("finite nonnegative factor required")
    return e if bool(active) else 1.0


def capital_path(factors: Iterable[float], initial: float = 1.0) -> np.ndarray:
    e = np.asarray(list(factors), dtype=float)
    if np.any(e < 0) or not np.all(np.isfinite(e)) or initial < 0:
        raise ValueError("finite nonnegative capital inputs required")
    return float(initial) * np.cumprod(e)


def stopping_time_crossing(factors: Iterable[float], threshold: float, initial: float = 1.0) -> int | None:
    if threshold <= 0:
        raise ValueError("positive threshold required")
    for t, value in enumerate(capital_path(factors, initial), 1):
        if value >= threshold:
            return t
    return None


def claim_evidence(cell_evalues: Mapping[str, float], required_cells: Sequence[str]) -> float:
    if not required_cells:
        raise ValueError("nonempty claim required")
    vals = []
    for cell in required_cells:
        if cell not in cell_evalues:
            raise ValueError(f"missing cell {cell}")
        value = float(cell_evalues[cell])
        if value < 0 or not math.isfinite(value):
            raise ValueError("finite nonnegative evidence required")
        vals.append(value)
    return float(min(vals))


def null_expansion_factor(candidate: float, old_upper: float, expanded_upper: float) -> dict:
    if expanded_upper < old_upper:
        raise ValueError("expanded null must not reduce upper density")
    old = e_factor(candidate, old_upper)
    new = e_factor(candidate, expanded_upper)
    return {
        "old_factor": old,
        "expanded_factor": new,
        "monotone": bool(new <= old + 1e-15),
    }


def transition_allowed(from_state: str, to_state: str) -> bool:
    if from_state not in STATES or to_state not in STATES:
        return False
    return to_state in ALLOWED_TRANSITIONS[from_state]


def validate_event(event: Mapping, expected_prior_hash: str | None = None) -> dict:
    errors: list[str] = []
    blockers: list[str] = []

    required = (
        "event_id", "timestamp", "prior_event_hash", "from_state", "to_state",
        "event_type", "prior_information_hash", "transition_rule_hash",
        "new_conformation_hash", "outcome_used_to_select_same_step_factor",
    )
    for key in required:
        if key not in event:
            errors.append(f"MISSING_{key.upper()}")

    if errors:
        return {"valid": False, "errors": sorted(set(errors)), "blockers": []}

    if event["prior_event_hash"] != expected_prior_hash:
        errors.append("EVENT_HASH_CHAIN_BREAK")
    if not transition_allowed(event["from_state"], event["to_state"]):
        errors.append("FORBIDDEN_STATE_TRANSITION")
    if event["outcome_used_to_select_same_step_factor"] is not False:
        errors.append("SAME_STEP_OUTCOME_SELECTION")
    for key in ("event_id", "timestamp", "prior_information_hash", "transition_rule_hash", "new_conformation_hash"):
        if not isinstance(event.get(key), str) or not event.get(key):
            errors.append(f"INVALID_{key.upper()}")

    if event["event_type"] in {"START_EPOCH", "RESUME_NEW_EPOCH"}:
        receipts = event.get("epoch_receipt_hashes", [])
        if not isinstance(receipts, list) or len(receipts) == 0:
            blockers.append("MISSING_EPOCH_RECEIPT_HASHES")
    if event["event_type"] == "ARM" and event.get("hg43_arming_receipt_hash") in (None, ""):
        blockers.append("MISSING_HG43_ARMING_RECEIPT")

    return {
        "valid": not errors and not blockers,
        "errors": sorted(set(errors)),
        "blockers": sorted(set(blockers)),
    }


def validate_history(events: Sequence[Mapping], initial_state: str = "PROTOCOL_FROZEN_UNARMED") -> dict:
    errors: list[str] = []
    blockers: list[str] = []
    state = initial_state
    previous_hash = None
    computed_hashes: list[str] = []

    for i, event in enumerate(events):
        if event.get("from_state") != state:
            errors.append(f"STATE_CONTINUITY_BREAK_AT_{i}")
        check = validate_event(event, expected_prior_hash=previous_hash)
        errors.extend(check["errors"])
        blockers.extend(check["blockers"])
        body = {k: v for k, v in event.items() if k != "event_hash"}
        computed = chained_event_hash(previous_hash, body)
        if event.get("event_hash") != computed:
            errors.append(f"EVENT_HASH_MISMATCH_AT_{i}")
        previous_hash = computed
        computed_hashes.append(computed)
        state = event.get("to_state", state)

    return {
        "valid": not errors and not blockers,
        "errors": sorted(set(errors)),
        "blockers": sorted(set(blockers)),
        "final_state": state,
        "computed_hashes": computed_hashes,
    }


def validate_constitution(constitution: Mapping) -> dict:
    errors: list[str] = []
    blockers: list[str] = []

    if constitution.get("profile") != "hgmf-hg44-conformational-constitution/1.0":
        errors.append("PROFILE_MISMATCH")
    state = constitution.get("state")
    if state not in STATES:
        errors.append("INVALID_STATE")
    if constitution.get("prospective_outcomes_present") is True and state == "PROTOCOL_FROZEN_UNARMED":
        errors.append("OUTCOMES_PRESENT_WHILE_UNARMED")

    pre = constitution.get("hg43_precondition", {})
    if pre.get("passed") is not True:
        blockers.append("HG43_NOT_ARMED")

    conf = constitution.get("conformation", {})
    for key in (
        "chart_hash", "candidate_algorithm_hash", "null_envelope_hash",
        "claim_semantics", "aggregation_rule",
        "quarantine_rule_hash", "stopping_rule_hash",
    ):
        if conf.get(key) in (None, "", []):
            blockers.append(f"MISSING_{key.upper()}")

    evidence = constitution.get("evidence", {})
    if evidence.get("real_factors_admitted", 0) < 1:
        blockers.append("MISSING_REAL_CONDITIONAL_EFACTORS")
    if conf.get("epoch_id") in (None, ""):
        blockers.append("MISSING_REAL_CALIBRATION_EPOCH")

    history_check = validate_history(constitution.get("history", []))
    errors.extend(history_check["errors"])
    blockers.extend(history_check["blockers"])
    if history_check["final_state"] != state:
        errors.append("HISTORY_FINAL_STATE_MISMATCH")

    authority = constitution.get("acquisition_authorized") is True
    if authority and state not in {"ARMED_FUTURE_ONLY", "ACQUIRING_EPOCH", "PAUSED_RECALIBRATION"}:
        errors.append("AUTHORITY_WITH_INVALID_STATE")
    authorized = bool(not errors and not blockers and authority and state == "ARMED_FUTURE_ONLY")

    if errors:
        status = "FAIL_INVALID_CONFORMATIONAL_CONSTITUTION"
    elif blockers:
        status = "ABSTAIN_HG43_NOT_ARMED" if "HG43_NOT_ARMED" in blockers else "ABSTAIN_CONFORMATION_INCOMPLETE"
    elif state != "ARMED_FUTURE_ONLY":
        status = "ABSTAIN_COMPLETE_BUT_NOT_ARMED"
    elif not authority:
        status = "ABSTAIN_ARMED_WITHOUT_ACQUISITION_AUTHORITY"
    else:
        status = "PASS_ARMED_CONFORMATIONAL_EPROCESS"

    return {
        "profile": "hgmf-hg44-adjudication/1.0",
        "status": status,
        "authorized": authorized,
        "errors": sorted(set(errors)),
        "blockers": sorted(set(blockers)),
    }
