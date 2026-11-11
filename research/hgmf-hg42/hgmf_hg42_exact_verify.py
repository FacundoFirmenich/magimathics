#!/usr/bin/env python3
import copy
import json
from pathlib import Path

import numpy as np

from hgmf_hg42_core import (
    calibration_augmented_discrete_evalue,
    dependent_product_counterexample,
    gaussian_common_mean_profile_loglik,
    intersection_min_evalue,
    linear_operator_covariance,
    minimum_replicates_full_covariance,
    pushforward_discrete_mass,
    validate_prospective_seal,
    weighted_e_mean,
)

ROOT = Path(__file__).resolve().parent

fixture = calibration_augmented_discrete_evalue(
    [0.05, 0.15, 0.25, 0.55],
    np.array([[0.20, 0.30, 0.30, 0.20], [0.40, 0.20, 0.10, 0.30]]),
)
assert fixture["valid"]
assert np.max(fixture["null_expectations"]) <= 1.0 + 1e-12

labels = [0, 0, 1, 1]
_, g_comp = pushforward_discrete_mass([0.05, 0.15, 0.25, 0.55], labels)
q_comp = np.vstack([pushforward_discrete_mass(row, labels)[1] for row in np.array([[0.20,0.30,0.30,0.20],[0.40,0.20,0.10,0.30]])])
compressed = calibration_augmented_discrete_evalue(g_comp, q_comp)
assert compressed["valid"]

counter = dependent_product_counterexample()
assert abs(counter["E1_expectation"] - 1.0) < 1e-12
assert abs(counter["E2_expectation"] - 1.0) < 1e-12
assert counter["product_expectation"] == 2.0
assert counter["mean_expectation"] == 1.0
assert counter["min_expectation"] == 1.0
assert weighted_e_mean([0.0, 2.0]) == 1.0
assert intersection_min_evalue([4.0, 0.25, 3.0]) == 0.25

assert minimum_replicates_full_covariance(3, 1) == 4
x3 = np.array([[0.0,0.0,0.0],[1.0,0.0,0.0],[0.0,1.0,0.0]])
x4 = np.array([[0.0,0.0,0.0],[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0]])
p3 = gaussian_common_mean_profile_loglik(x3)
p4 = gaussian_common_mean_profile_loglik(x4)
assert not p3["finite_supremum"]
assert p4["finite_supremum"]

S = np.diag([1.0, 4.0, 9.0])
A = np.array([[0.5,0.5,0.0],[0.0,0.5,0.5]])
G = np.array([[1.0,-1.0]])
SQ = linear_operator_covariance(S,A,G)
assert SQ.shape == (1,1)
assert SQ[0,0] > 0

seal = json.loads((ROOT/"HGMF_HG42_CURRENT_SEAL.json").read_text())
adj = validate_prospective_seal(seal)
assert adj["status"] == "ABSTAIN_REAL_REPLICATES_OR_DENSITY_PROOFS_MISSING"
assert not adj["authorized"]
assert not adj["errors"]

bad = copy.deepcopy(seal)
bad["combination"]["rule"] = "raw_product_of_marginal_evalues"
bad_adj = validate_prospective_seal(bad)
assert "UNSAFE_AGGREGATION_RULE" in bad_adj["errors"]

fake = copy.deepcopy(seal)
fake["stage"] = "ARMED_FUTURE_ONLY"
fake["acquisition_authorized"] = True
fake_adj = validate_prospective_seal(fake)
assert not fake_adj["authorized"]
assert fake_adj["blockers"]

results = json.loads((ROOT/"HGMF_HG42_RESULTS.json").read_text())
assert results["historical_readiness"]["magnetism"]["minimum_full_covariance_replicates"] == 4
assert results["historical_readiness"]["magnetism"]["available_independent_quotient_vectors"] == 1
assert results["historical_readiness"]["adsorption"]["joint_stochastic_history_replicates"] == 1
assert not results["actual_quotient_evalue_computed"]
assert results["physical_protogeometry"] == "HOLD"

print("PASS_HGMF_HG42_EXACT")
print(f"joint_evalue_max_null_expectation={np.max(fixture['null_expectations'])}")
print("frozen_compression_evalue=PASS")
print("dependent_marginal_product_expectation=2")
print("weighted_mean_expectation=1")
print("intersection_min_expectation=1")
print(f"quotient_d3_min_full_covariance_replicates={minimum_replicates_full_covariance(3,1)}")
print("n3_full_covariance_profile=UNBOUNDED")
print("n4_full_covariance_profile=FINITE")
print(f"interpolation_quotient_variance={SQ[0,0]}")
print(f"current_seal_status={adj['status']}")
print("unsafe_product_rejected=PASS")
print("fake_arming_fail_closed=PASS")
print("actual_quotient_evalue_computed=false")
print("physical_protogeometry=HOLD")
