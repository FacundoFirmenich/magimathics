# HGMF-HG37 — External-calibration rescue versus prospective-pivot theorem

## Objective

Determine whether the historical public-data route can be made confirmatory by obtaining independent calibration objects, or whether the program should stop investing inference effort in these carriers and move to a prospective acquisition designed for identifiability.

## Gate A — magnetic field-axis calibration

Search the source repository/publication for:
- magnet calibration records;
- field-controller accuracy/specification;
- Hall-probe or independent field reference;
- shared systematic structure across loops.

If an independently justified bound much smaller than the trained HEB offsets exists, rebuild the magnetic summary likelihood.

## Gate B — whole-curve magnetic route

If field-axis calibration is insufficient, construct a model for the complete Vxy(H) curve with a shared field-warp nuisance rather than independent crossing offsets.

## Gate C — Xe/silica film reference

Search Brown thesis, associated NIST material and same-origin literature for:
- nonporous Xe/silica reference isotherm;
- independently calibrated surface area;
- FHH parameters with provenance and uncertainty.

## Gate D — set-valued power theorem

If no external film reference exists, compute a certified upper bound showing whether the current Vs/Q/q uncertainty makes any network rejection impossible.

## Gate E — prospective pivot

If either carrier remains non-identifiable, freeze a prospective minimal measurement that supplies the missing calibration:
- magnetism: finer/independently calibrated field axis plus raw repeated voltages;
- adsorption: film-reference measurement plus boundary/scanning runs.

## Authorized outcomes

PASS_MAGNETIC_CALIBRATION_RESCUE  
PASS_VYCOR_REFERENCE_RESCUE  
PASS_CARRIER_SPECIFIC_X_DENOMINATOR  
FAIL_HISTORICAL_DATA_IDENTIFIABILITY  
PASS_PROSPECTIVE_PIVOT_PROTOCOL  
ABSTAIN_EXTERNAL_REFERENCE_UNAVAILABLE  
HOLD_PHYSICAL_PROTOGEOMETRY
