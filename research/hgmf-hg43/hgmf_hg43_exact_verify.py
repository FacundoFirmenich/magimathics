#!/usr/bin/env python3
import copy
import json
from pathlib import Path

import numpy as np

from hgmf_hg43_core import (
    admit_replicate_receipts,
    aggregate_evalues,
    cantelli_power_lower,
    conjunction_power_lower,
    covariance_certificate,
    evalue_from_upper,
    minimum_clusters_cantelli,
    union_upper_density,
    validate_arming_dossier,
)

ROOT = Path(__file__).resolve().parent

# 1. Null-union upper density and e-value fixture.
candidate = np.array([0.5, 0.3, 0.2])
nulls = np.array([
    [0.4, 0.4, 0.2],
    [0.6, 0.1, 0.3],
])
upper = np.max(nulls, axis=0)
e = np.array([evalue_from_upper(g, u) for g, u in zip(candidate, upper)])
expectations = nulls @ e
assert np.all(expectations <= 1 + 1e-12)
assert union_upper_density([0.4, 0.6]) == 0.6

# 2. Structured covariance certificate.
S = np.array([[1.0, 0.2], [0.2, 0.7]])
cert = covariance_certificate(S, 0.5)
assert cert["passed"]
bad = covariance_certificate(np.diag([1.0, 0.0]), 0.1)
assert not bad["passed"]

# 3. Replicate clusters: five rows but only four independent clusters.
receipts = []
for i, cluster in enumerate(["A", "A", "B", "C", "D"]):
    receipts.append({
        "replicate_id": f"R{i}",
        "acquisition_hash": f"acq-{i}",
        "independent_cluster_id": cluster,
        "independence_certificate_hash": f"cert-{cluster}",
        "ancestry_hash": f"anc-{i}",
        "holdout_values_accessed_before_arming": False,
    })
admission = admit_replicate_receipts(receipts, 3, 1, "unrestricted_full")
assert admission["rows_submitted"] == 5
assert admission["independent_clusters"] == 4
assert admission["admitted"]

deficient = admit_replicate_receipts(receipts[:4], 3, 1, "unrestricted_full")
assert deficient["independent_clusters"] == 3
assert not deficient["admitted"]

# 4. Claim logic.
assert aggregate_evalues([200.0, 150.0], "intersection_min") == 150.0
assert aggregate_evalues([200.0, 0.0], "weighted_mean", [0.5, 0.5]) == 100.0
try:
    aggregate_evalues([2.0, 2.0], "sequential_conditional_product")
    raise AssertionError("unsafe product accepted")
except ValueError:
    pass

# 5. Cantelli finite-sample power and exact minimum integer check.
m, v, target, threshold = 0.4, 1.2, 0.8, 140.0
n = minimum_clusters_cantelli(m, v, target, threshold)
assert cantelli_power_lower(m, v, n, threshold) >= target
if n > 1:
    assert cantelli_power_lower(m, v, n - 1, threshold) < target

# 6. Conjunction familywise lower bound.
joint = conjunction_power_lower([0.95, 0.97])
assert abs(joint - 0.92) < 1e-12

# 7. Current dossier must abstain cleanly.
dossier = json.loads((ROOT / "HGMF_HG43_CURRENT_DOSSIER.json").read_text())
current = validate_arming_dossier(dossier)
assert current["status"] == "ABSTAIN_REAL_RECEIPTS_DENSITIES_OR_POWER_MISSING"
assert not current["authorized"]
assert not current["errors"]
assert "MISSING_CHART_DEGENERACY_THRESHOLD" in current["blockers"]
assert not dossier["prospective_outcomes_present"]
assert not dossier["acquisition_authorized"]

# 8. Fake arming must fail closed.
fake = copy.deepcopy(dossier)
fake["stage"] = "ARMED_FUTURE_ONLY"
fake["acquisition_authorized"] = True
fake_result = validate_arming_dossier(fake)
assert not fake_result["authorized"]
assert fake_result["status"] != "PASS_ARMED_RECEIPT_CONDITIONED_QUOTIENT_EVALUE"

(ROOT / "HGMF_HG43_CURRENT_ADJUDICATION.json").write_text(
    json.dumps(current, indent=2) + "\n"
)

print("PASS_HGMF_HG43_EXACT")
print(f"null_union_max_expectation={float(np.max(expectations))}")
print(f"structured_covariance_min_eigenvalue={cert['minimum_eigenvalue']}")
print("structured_covariance_singular_rejected=PASS")
print(f"replicate_rows={admission['rows_submitted']}")
print(f"independent_clusters={admission['independent_clusters']}")
print("pseudoreplication_collapse=PASS")
print(f"cantelli_min_clusters_fixture={n}")
print(f"cantelli_power_at_min={cantelli_power_lower(m,v,n,threshold)}")
print(f"conjunction_power_lower_fixture={joint}")
print(f"current_status={current['status']}")
print(f"current_blockers={len(current['blockers'])}")
print("fake_arming_fail_closed=PASS")
print("acquisition_authorized=false")
print("prospective_outcomes_present=false")
print("physical_protogeometry=HOLD")
