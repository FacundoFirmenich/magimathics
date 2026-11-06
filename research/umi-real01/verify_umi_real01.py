#!/usr/bin/env python3
from pathlib import Path
import json
import pandas as pd

root = Path(__file__).resolve().parent
interventions = pd.read_csv(root / "data" / "intervention_results.csv")
signs = pd.read_csv(root / "data" / "sign_topology_audit.csv")
subs_phase = pd.read_csv(root / "data" / "substitution_and_phase.csv")
results = json.loads((root / "data" / "results.json").read_text())

baseline = interventions.loc[interventions.run == "baseline_closed_repression_cycle"].iloc[0]
assert bool(baseline.oscillatory)
for name in [
    "ablate_PZ_to_X",
    "ablate_PX_to_Y",
    "ablate_PY_to_Z",
    "rewire_PX_to_Y_as_PZ_to_Y",
    "flip_PX_to_Y_to_activation",
    "one_node_self_repression",
    "two_node_mutual_repression",
]:
    row = interventions.loc[interventions.run == name].iloc[0]
    assert not bool(row.oscillatory)

sub = subs_phase.loc[subs_phase.record_type == "substitution"].iloc[0]
assert float(sub.value_1) < 1e-12
phase = subs_phase.loc[subs_phase.record_type == "phase"]
assert (abs(phase.value_2.astype(float) - 1/3) < 0.002).all()

osc_signs = signs.loc[signs.oscillatory == True]
assert len(osc_signs) == 1
assert (osc_signs[["PZ_to_X", "PX_to_Y", "PY_to_Z"]] == "repression").all(axis=None)
assert results["verdict"] == "PASS_REAL_RELATIONAL_UMI_CORE_HOLD_MULTIFRACTAL_QUALIFIER"

print("PASS_MGM_UMI_REAL01")
print("baseline oscillates")
print("all frozen ablations/rewires/reductions lose the signature")
print("cyclic substitution preserves trajectory")
print("phase sectors are approximately one third of the period")
print("only all-repression sign topology oscillates in the curated regime")
