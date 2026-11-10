#!/usr/bin/env python3
from __future__ import annotations
import copy, json, math
from pathlib import Path
import numpy as np

from hgmf_hg39_commissioning_validator import canonical_hash, validate
from hgmf_hg39_fitness_compiler import (
    bethe_q,
    compile_fitness,
    propagate_bethe_q_uncertainty,
    propagate_q_uncertainty,
    q_jacobian,
    q_value,
)

ROOT = Path(__file__).resolve().parent
dossier = json.loads((ROOT / "HGMF_HG39_CURRENT_DOSSIER.json").read_text(encoding="utf-8"))
fitness_input = json.loads((ROOT / "HGMF_HG39_CURRENT_FITNESS_INPUT.json").read_text(encoding="utf-8"))

assert dossier["self_hash"] == canonical_hash(dossier)
adj = validate(dossier)
assert adj["status"] == "ABSTAIN_REAL_COMMISSIONING_NOT_COMPLETE"
assert adj["authorized_for_hg38_arming_review"] is False
assert adj["acquisition_authorized"] is False
assert len(adj["errors"]) == 0

# Tamper detection.
tampered = copy.deepcopy(dossier)
tampered["future_only"]["holdout_accessed"] = True
tamper_adj = validate(tampered)
assert "DOSSIER_SELF_HASH_MISMATCH" in tamper_adj["errors"]
assert "HOLDOUT_ACCESS_VIOLATION" in tamper_adj["errors"]

# Candidate scope cannot become a result receipt.
fake = copy.deepcopy(dossier)
for key in fake["work_packages"]:
    fake["work_packages"][key]["signed_service_confirmation"] = {"status": "TEST_FIXTURE"}
    fake["work_packages"][key]["actual_result_receipt"] = {
        "profile": "CAPABILITY_DISCOVERY_ONLY",
        "status": "NOT_A_RESULT",
        "self_hash": "0" * 64,
    }
fake["fitness"]["numeric_limits_frozen"] = True
fake["fitness"]["fitness_input_artifact"] = {"path": "TEST_FIXTURE"}
fake["fitness"]["fitness_output_artifact"] = {"path": "TEST_FIXTURE"}
fake["state"] = "COMMISSIONED_READY_FOR_ARMING"
fake["self_hash"] = canonical_hash(fake)
fake_adj = validate(fake)
assert fake_adj["authorized_for_hg38_arming_review"] is False
assert any("RECEIPT_PROFILE_MISMATCH" in x for x in fake_adj["errors"])

# Incomplete real fitness inputs must abstain.
compiled = compile_fitness(fitness_input)
assert compiled["status"] == "ABSTAIN_NUMERIC_FITNESS_INPUT_INCOMPLETE"
assert compiled["arming_eligible"] is False

# Algebraic software fixture: not an empirical result.
fit_fixture = {
    "profile": "hgmf-hg39-fitness-input/1.0",
    "magnetic": {
        "coverage_factor": 2.0,
        "maximum_expanded_uncertainty_mT": 0.8,
        "components_standard_uncertainty_mT": {
            "reference": 0.1,
            "map": 0.2,
            "position": 0.1,
            "repeatability": 0.05,
            "drift": 0.1,
            "hysteresis": 0.05,
        },
    },
    "adsorption": {
        "maximum_standard_uncertainty_Q": 0.03,
        "maximum_standard_uncertainty_q": 0.04,
    },
}
fit_out = compile_fitness(fit_fixture)
assert fit_out["status"] == "PASS_FITNESS_INPUT_COMPILED"
expected_uc = math.sqrt(0.1**2 + 0.2**2 + 0.1**2 + 0.05**2 + 0.1**2 + 0.05**2)
assert abs(fit_out["magnetic"]["combined_standard_uncertainty_mT"] - expected_uc) < 1e-15
assert fit_out["magnetic"]["pass"] is True

# Q Jacobian against centered finite differences.
V, Vs, Vc = 12.0, 4.0, 20.0
J = q_jacobian(V, Vs, Vc)
x = np.asarray([V, Vs, Vc], dtype=float)
Jfd = np.zeros(3)
for j in range(3):
    h = 1e-6
    xp, xm = x.copy(), x.copy()
    xp[j] += h
    xm[j] -= h
    Jfd[j] = (q_value(xp[0], xp[1], xp[2]) - q_value(xm[0], xm[1], xm[2])) / (2*h)
assert np.max(np.abs(J - Jfd)) < 1e-8

S = np.diag([0.01, 0.04, 0.09])
qprop = propagate_q_uncertainty(V, Vs, Vc, S)
assert qprop["standard_uncertainty_Q"] > 0

# Bethe inverse and covariance propagation.
Qp, q0, z = 0.2, 0.35, 6.6
# Forward relation for a scan.
def alpha_from_q(q, Qp, z):
    from scipy.optimize import brentq
    f = lambda y: (1-q) + q*(1-Qp)*y**(z-1) - y
    y = brentq(f, 0.0, 1.0)
    return 1-y**z

alpha = alpha_from_q(q0, Qp, z)
Qm = Qp + (1-Qp)*alpha
q1 = bethe_q(Qp, Qm, z)
assert abs(q1 - q0) < 1e-12
bprop = propagate_bethe_q_uncertainty(Qp, Qm, z, np.diag([1e-4, 1e-4, 1e-2]))
assert bprop["standard_uncertainty_q"] > 0

print("PASS_HGMF_HG39_EXACT")
print("dossier_self_hash=PASS")
print("current_state=ABSTAIN_REAL_COMMISSIONING_NOT_COMPLETE")
print("tamper_detection=PASS")
print("capability_not_promoted_to_result=PASS")
print("fitness_compiler=PASS")
print("Q_covariance_propagation=PASS")
print("Bethe_q_inversion_and_covariance=PASS")
print("arming_authorized=false")
print("acquisition_authorized=false")
print("prospective_outcomes_present=false")
print("empirical_hgmf_claim=false")
print("physical_protogeometry=HOLD")
