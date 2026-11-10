#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

from hgmf_hg40_affine_quotient import affine_coordinates, cross_ratio

ROOT = Path(__file__).resolve().parent
GENERATED = ROOT / "generated"

mag = json.loads((GENERATED / "HGMF_HG40_MAGNETIC_AFFINE_QUOTIENT.json").read_text())
ads = json.loads((GENERATED / "HGMF_HG40_ADSORPTION_REFERENCE_FREE.json").read_text())

assert mag["status"] == "PASS_HGMF_HG40_MAGNETIC_AFFINE_QUOTIENT_EXECUTED"
assert mag["affine_invariance_test"]["pass"] is True
assert mag["affine_invariance_test"]["global_max_abs_error"] < 1e-12
assert mag["nuisance_dimension_comparison"]["identified_affine_quotient_dimension"] == 3
assert mag["loop1_asymmetry_dominates_later"] is True

assert ads["status"] == "PASS_HGMF_HG40_ADSORPTION_REFERENCE_FREE_EXECUTED"
check = ads["bethe_no_passing_theorem_numerical_check"]
assert check["nonnegative_on_closed_grid"] is True
assert check["strictly_positive_interior"] is True
assert ads["affine_quotient_audit"]["rows"] > 0
assert ads["affine_quotient_audit"]["distinct_pressures"] > 0
assert ads["affine_quotient_audit"]["total_identified_quotient_degrees"] > 0

# Re-check affine invariance on an actual Brown-data snapshot emitted by the audit.
snapshot = ads["affine_quotient_audit"]["representative_real_snapshot"]
y = np.asarray(snapshot["adsorption_values_mg"], float)
r0 = affine_coordinates(y, 0, len(y) - 1)
alpha = -2.37
beta = 14.2
r1 = affine_coordinates(alpha * y + beta, 0, len(y) - 1)
assert np.max(np.abs(r0 - r1)) < 1e-12
assert np.max(np.abs(r0 - np.asarray(snapshot["affine_coordinates"], float))) < 1e-12

if len(y) >= 4:
    c0 = cross_ratio(y[0], y[1], y[-2], y[-1])
    c1 = cross_ratio(alpha * y[0] + beta, alpha * y[1] + beta, alpha * y[-2] + beta, alpha * y[-1] + beta)
    assert abs(c0 - c1) < 1e-12

print("PASS_HGMF_HG40_EXACT")
print(f"magnetic_training_contrast={mag['quotient_metrics']['loop1_training_contrast']}")
print(f"magnetic_quotient_dimension={mag['nuisance_dimension_comparison']['identified_affine_quotient_dimension']}")
print(f"adsorption_scans={ads['simple_desorption_scans']}")
print(f"adsorption_pairwise_points={ads['pairwise_order_audit']['evaluation_points']}")
print(f"adsorption_strict_order_violations={ads['pairwise_order_audit']['strict_violation_points']}")
print(f"adsorption_quotient_pressures={ads['affine_quotient_audit']['distinct_pressures']}")
print(f"adsorption_quotient_degrees={ads['affine_quotient_audit']['total_identified_quotient_degrees']}")
print("reference_free_partial_identifiability=PASS")
print("absolute_calibration_identifiability=false")
print("carrier_specific_universal_evalue_ready=false")
print("empirical_hgmf_claim=false")
print("physical_protogeometry=HOLD")
