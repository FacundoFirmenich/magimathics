#!/usr/bin/env python3
from __future__ import annotations

import copy
import itertools
import json
from pathlib import Path

import numpy as np

from hgmf_hg44_eprocess import (
    capital_path,
    chained_event_hash,
    claim_evidence,
    null_expansion_factor,
    predictable_mixture,
    predictable_quarantine,
    validate_constitution,
    validate_history,
)

ROOT = Path(__file__).resolve().parent


def e0(x: int) -> float:
    return 1.5 if x == 0 else 0.5


def e1(x: int) -> float:
    return 0.5 if x == 0 else 1.5


def predictable_path_capital(path):
    factors = []
    for t, x in enumerate(path):
        k = 0 if t == 0 else path[t - 1]
        factors.append(e0(x) if k == 0 else e1(x))
    return float(capital_path(factors)[-1]), factors


# 1. Predictable switching conserves null-expected capital exactly in this fixture.
for horizon in (1, 2, 4, 8):
    caps = [predictable_path_capital(path)[0] for path in itertools.product((0, 1), repeat=horizon)]
    assert abs(float(np.mean(caps)) - 1.0) < 1e-15

# 2. Same-step outcome-dependent factor selection manufactures evidence.
same_step = np.mean([max(e0(x), e1(x)) for x in (0, 1)])
assert abs(float(same_step) - 1.5) < 1e-15

# 3. Predictable mixture may depend on past but not on current outcome.
for previous in (0, 1):
    weights = (0.8, 0.2) if previous == 0 else (0.2, 0.8)
    conditional_mean = np.mean([
        predictable_mixture([e0(x), e1(x)], weights)
        for x in (0, 1)
    ])
    assert abs(float(conditional_mean) - 1.0) < 1e-15

# 4. Predictable quarantine remains neutral.
for active in (False, True):
    conditional_mean = np.mean([
        predictable_quarantine(e0(x), active)
        for x in (0, 1)
    ])
    assert abs(float(conditional_mean) - 1.0) < 1e-15

# 5. Finite-horizon Ville check for the predictable switching process.
horizon = 10
threshold = 4.0
crosses = 0
for path in itertools.product((0, 1), repeat=horizon):
    _, factors = predictable_path_capital(path)
    if np.max(capital_path(factors)) >= threshold:
        crosses += 1
crossing_probability = crosses / (2 ** horizon)
assert crossing_probability <= 1.0 / threshold + 1e-15

# 6. Null expansion can only reduce the next factor.
expanded = null_expansion_factor(0.3, 0.2, 0.5)
assert expanded["monotone"]
assert expanded["expanded_factor"] <= expanded["old_factor"]

# 7. Stronger conjunction claim cannot increase evidence.
cell = {"M": 200.0, "A": 80.0, "T": 150.0}
weak = claim_evidence(cell, ["M"])
strong = claim_evidence(cell, ["M", "A", "T"])
assert strong <= weak
assert weak == 200.0 and strong == 80.0

# 8. Valid conformational history and hash chain.
events = []
previous_hash = None

def add_event(from_state, to_state, event_type, event_id, extra=None):
    global previous_hash
    body = {
        "event_id": event_id,
        "timestamp": f"2026-11-11T20:00:0{len(events)}+01:00",
        "prior_event_hash": previous_hash,
        "from_state": from_state,
        "to_state": to_state,
        "event_type": event_type,
        "prior_information_hash": f"info-{event_id}",
        "transition_rule_hash": f"rule-{event_id}",
        "new_conformation_hash": f"conf-{event_id}",
        "outcome_used_to_select_same_step_factor": False,
    }
    if extra:
        body.update(extra)
    event_hash = chained_event_hash(previous_hash, body)
    event = dict(body)
    event["event_hash"] = event_hash
    events.append(event)
    previous_hash = event_hash

add_event(
    "PROTOCOL_FROZEN_UNARMED", "ARMED_FUTURE_ONLY", "ARM", "E0",
    {"hg43_arming_receipt_hash": "hg43-real-receipt"},
)
add_event(
    "ARMED_FUTURE_ONLY", "ACQUIRING_EPOCH", "START_EPOCH", "E1",
    {"epoch_receipt_hashes": ["cal-1", "reference-1"]},
)
add_event(
    "ACQUIRING_EPOCH", "PAUSED_RECALIBRATION", "PAUSE_RECALIBRATION", "E2",
)
add_event(
    "PAUSED_RECALIBRATION", "ACQUIRING_EPOCH", "RESUME_NEW_EPOCH", "E3",
    {"epoch_receipt_hashes": ["cal-2", "reference-2"]},
)
add_event(
    "ACQUIRING_EPOCH", "TERMINAL_ABSTAIN", "TERMINAL_ABSTAIN", "E4",
)

history = validate_history(events)
assert history["valid"]
assert history["final_state"] == "TERMINAL_ABSTAIN"

tampered = copy.deepcopy(events)
tampered[1]["new_conformation_hash"] = "rewritten-after-outcome"
tampered_history = validate_history(tampered)
assert not tampered_history["valid"]
assert any("EVENT_HASH_MISMATCH" in x or "EVENT_HASH_CHAIN_BREAK" in x for x in tampered_history["errors"])

# 9. Current constitution must abstain cleanly.
constitution = json.loads((ROOT / "HGMF_HG44_CURRENT_CONSTITUTION.json").read_text())
current = validate_constitution(constitution)
assert current["status"] == "ABSTAIN_HG43_NOT_ARMED"
assert not current["authorized"]
assert not current["errors"]
assert "HG43_NOT_ARMED" in current["blockers"]
assert not constitution["acquisition_authorized"]
assert not constitution["prospective_outcomes_present"]

# 10. Fake arming without receipts/factors remains unauthorized.
fake = copy.deepcopy(constitution)
fake["state"] = "ARMED_FUTURE_ONLY"
fake["acquisition_authorized"] = True
fake_result = validate_constitution(fake)
assert not fake_result["authorized"]

(ROOT / "HGMF_HG44_CURRENT_ADJUDICATION.json").write_text(
    json.dumps(current, indent=2) + "\n"
)

print("PASS_HGMF_HG44_EXACT")
print("predictable_switching_expected_capital=1")
print(f"same_step_outcome_selection_expectation={same_step}")
print("predictable_mixture_conditional_expectation=1")
print("predictable_quarantine_conditional_expectation=1")
print(f"finite_horizon_crossing_probability={crossing_probability}")
print(f"ville_upper_bound={1.0/threshold}")
print(f"null_expansion_old_factor={expanded['old_factor']}")
print(f"null_expansion_new_factor={expanded['expanded_factor']}")
print(f"weak_claim_evidence={weak}")
print(f"strong_claim_evidence={strong}")
print("valid_epoch_history=PASS")
print("retroactive_hash_rewrite_detected=PASS")
print(f"current_status={current['status']}")
print(f"current_blockers={len(current['blockers'])}")
print("fake_arming_fail_closed=PASS")
print("anytime_evidence_execution=false")
print("acquisition_authorized=false")
print("prospective_outcomes_present=false")
print("physical_protogeometry=HOLD")
