# HGMF-HG36 — Observation bridges: identification frontier

## Veredicto

PASS_REAL_OBSERVATION_BRIDGE_EXECUTION  
PASS_RAW_VOLTAGE_NOISE_PROPAGATION  
PASS_MAGNETIC_FIELD_RESOLUTION_NUISANCE_THEOREM  
PASS_VYCOR_SET_VALUED_REFERENCE_AUDIT  
PASS_VYCOR_REFERENCE_NONIDENTIFIABILITY_THEOREM  
PASS_EXACT_BETHE_Q_INVERSION  

FAIL_HEB_SUMMARY_CONFIRMATORY_POWER  
FAIL_VYCOR_POINT_IDENTIFICATION  
FAIL_CARRIER_SPECIFIC_UNIVERSAL_EVALUE_DENOMINATOR  

ABSTAIN_MAGNETIC_EXACT_LIKELIHOOD_AUTHORITY  
ABSTAIN_VYCOR_NETWORK_LIKELIHOOD  
HOLD_PHYSICAL_PROTOGEOMETRY

## 1. Magnetic raw uncertainty

The source HDF5 data contain five raw nanovoltmeter samples per current-polarity source row. HG36 resamples these values directly and recomputes the complete HEB estimator.

HEB bootstrap SDs:
- L1 0.00653 mT;
- L2 0.00535 mT;
- L3 0.00627 mT;
- L4 0.01047 mT;
- L5 0.01411 mT.

The later offsets are therefore much larger than repeated-voltage noise.

However they remain smaller than one field step. The source summary should therefore not be described as “zero HEB statistically”; instead it is “unresolved from zero under the field-axis discretization allowed by the source acquisition”.

This yields a power no-go: if each loop receives an independent bounded field-axis nuisance, the trained-state null can reproduce every observed later HEB exactly.

## 2. Vycor reference frontier

Cimino-type network inference requires an external film reference Vs and a condensed-fluid reference Vc.

Brown supplies the porous Vycor boundary/scanning data but no external nonporous Xe/silica film isotherm.

Using only Brown-internal order information:
- Vc: eight admissible upper-plateau linear extrapolations;
- Vs: lower bound from the lower branch-closure loading and upper bound from the adsorption boundary.

The resulting intervals are not narrow:
- Q median width 0.28585; max 0.99660;
- q median width 0.21412; max 0.71584.

Thus the network state is constrained but not point-identified.

## 3. Consequence for HG31

Neither carrier now supplies the fully calibrated nuisance likelihood upper bound required for universal e-value X:

- magnetism: field-axis nuisance saturates HEB summary;
- adsorption: reference-film nonidentifiability leaves Q and q set-valued.

This is a clean no-go closure of the historical public-data route at the current observable resolution.

## 4. Strategic implication

Further progress requires new calibration information, not more flexible fitting.

Magnetism needs:
- independent field-axis calibration below the residual HEB scale, or
- a whole-curve Vxy(H) likelihood with shared field-systematic structure.

Adsorption needs:
- same-origin nonporous Xe/silica film reference, or
- independently calibrated surface area/FHH film model with uncertainty.

Without those objects, the honest result is HOLD/ABSTAIN rather than a beyond-standard claim.

## 5. Next gate

HGMF-HG37 — external-calibration rescue versus prospective-pivot theorem.
