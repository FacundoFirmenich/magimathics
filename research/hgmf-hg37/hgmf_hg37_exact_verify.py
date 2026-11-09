#!/usr/bin/env python3
import json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parent
AUD=ROOT/"generated"/"HGMF_HG37_PUBLIC_CALIBRATION_AUDIT.json"
x=json.loads(AUD.read_text())

assert x["status"]=="PASS_HGMF_HG37_PUBLIC_CALIBRATION_AUDIT_EXECUTED"
m=x["magnetic"]
a=x["adsorption"]

step=m["current_field_step_bound_mT"]
global_break=m["global_set_membership_break_threshold_mT"]
all_break=m["all_loops_nonabsorbable_threshold_mT"]

assert step > global_break > all_break > 0
assert abs(global_break-4.075432120767836) < 1e-12
assert abs(all_break-0.8838269371443452) < 1e-12
assert m["explicit_independent_field_calibration_found"] is False
assert a["external_nonporous_film_reference_found_in_Brown_repo"] is False
assert a["Mason_1988_alternative_route"].startswith("PUBLICATION_EXISTS")
assert x["historical_confirmatory_rescue"]=="FAIL_PUBLICLY_AVAILABLE_CALIBRATION_OBJECTS"
assert x["prospective_pivot_required"] is True

print("PASS_HGMF_HG37_EXACT")
print(f"current_field_step_bound_mT={step}")
print(f"global_null_break_threshold_mT={global_break}")
print(f"all_trained_loops_nonabsorbable_threshold_mT={all_break}")
print(f"relative_improvement_to_global_break={m['relative_improvement_needed']}")
print(f"gaussian_E140_heuristic_field_bound_mT={m['Gaussian_bootstrap_heuristic_not_confirmatory']['field_nuisance_bound_for_E140_mT']}")
print("public_independent_field_calibration_found=false")
print("Brown_external_film_reference_found=false")
print("Mason_alternative_standard_route_exists=true")
print("historical_confirmatory_rescue=false")
print("prospective_pivot_required=true")
print("physical_protogeometry=HOLD")
