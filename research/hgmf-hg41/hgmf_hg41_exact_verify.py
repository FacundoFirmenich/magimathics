#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
from hgmf_hg41_quotient import (
    affine_quotient,
    affine_reconstruct,
    quotient_inverse_jacobian_abs,
    quotient_gradient,
    magnetic_equal_trained_feasible,
    discrete_universal_evalue,
    support_only_pointwise_ceiling,
)

ROOT = Path(__file__).resolve().parent

y = np.array([-2.0, 3.0, 0.5, 7.0, -1.0])
rho, idx = affine_quotient(y, 0, 1)
for a, b in ((4.5, 2.3), (-8.0, -1.7), (0.0, 0.125)):
    rz, iz = affine_quotient(a + b*y, 0, 1)
    assert iz == idx
    assert np.max(np.abs(rho-rz)) < 1e-12

m = 5
u, v = 0.7, -2.4
q = np.array([0.2, -0.4, 1.3])
base = np.concatenate([[u, v], q])
def T(z):
    return affine_reconstruct(z[0], z[1], z[2:], m=m, r=0, s=1)
eps = 1e-6
J = np.column_stack([(T(base + eps*np.eye(m)[j]) - T(base - eps*np.eye(m)[j]))/(2*eps) for j in range(m)])
assert abs(abs(np.linalg.det(J)) - quotient_inverse_jacobian_abs(v,m)) < 1e-8

G, _ = quotient_gradient(y,0,1)
Gn = np.zeros_like(G)
for j in range(len(y)):
    e = np.zeros_like(y); e[j] = eps
    Gn[:,j] = (affine_quotient(y+e,0,1)[0] - affine_quotient(y-e,0,1)[0])/(2*eps)
assert np.max(np.abs(G-Gn)) < 1e-8

try:
    affine_quotient([1.0,1.0,2.0],0,1)
    raise AssertionError("degeneracy not rejected")
except ValueError as exc:
    assert "ANCHOR_DEGENERACY" in str(exc)

fixture = discrete_universal_evalue([0.5,0.3,0.2], np.array([[0.4,0.4,0.2],[0.6,0.1,0.3]]))
assert fixture["valid"]
assert np.max(fixture["null_expectations"]) <= 1 + 1e-12
assert support_only_pointwise_ceiling(True) == 1.0
assert 140.0 > support_only_pointwise_ceiling(True)

inp = json.loads((ROOT/"HGMF_HG41_HISTORICAL_INPUT.json").read_text())
mf = magnetic_equal_trained_feasible(
    inp["magnetism"]["observed_HEB_mT"],
    inp["magnetism"]["field_residual_halfwidth_mT"],
)
assert mf["feasible"]
assert abs(mf["common_trained_interval_lo"] + 0.954968076259938) < 1e-12
assert abs(mf["common_trained_interval_hi"] - 0.2177953129554666) < 1e-12

ad = inp["adsorption"]
assert ad["pairwise_evaluation_points"] == 713
assert ad["raw_negative_difference_points"] == 51
assert ad["strict_violation_points_beyond_conservative_tolerance"] == 0

res = json.loads((ROOT/"HGMF_HG41_RESULTS.json").read_text())
assert not res["actual_historical_quotient_evalue_computed"]
assert res["magnetism"]["support_only_evalue_ceiling"] == 1.0
assert res["adsorption"]["support_only_evalue_ceiling"] == 1.0
assert res["retrospective_confirmatory_authority"] == "ABSTAIN"
assert res["physical_protogeometry"] == "HOLD"

print("PASS_HGMF_HG41_EXACT")
print(f"quotient_dimension={len(rho)}")
print(f"inverse_chart_jacobian={quotient_inverse_jacobian_abs(v,m)}")
print("chart_invariance=PASS")
print("chart_gradient=PASS")
print("anchor_degeneracy_fail_closed=PASS")
print("quotient_universal_evalue_fixture=PASS")
print("support_only_pointwise_ceiling=1")
print(f"magnetic_common_interval=[{mf['common_trained_interval_lo']},{mf['common_trained_interval_hi']}]")
print("adsorption_strict_violations_beyond_tolerance=0")
print("historical_quotient_E140=FAIL")
print("retrospective_confirmatory_authority=ABSTAIN")
print("physical_protogeometry=HOLD")
