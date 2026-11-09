# HGMF‑HG37 — External-calibration rescue versus prospective pivot

**Date:** 2026-11-09

## Verdict

PASS_PUBLIC_RECORD_RESCUE_AUDIT  
PASS_MAGNETIC_RESCUE_THRESHOLD_THEOREM  
PASS_CALIBRATION_OBSERVABILITY_THEOREM  
PASS_VYCOR_ALTERNATIVE_STANDARD_ROUTE_EXISTS  
PASS_PROSPECTIVE_PIVOT_PROTOCOL  

FAIL_MAGNETIC_PUBLIC_CALIBRATION_RESCUE  
FAIL_CIMINO_VYCOR_REFERENCE_RESCUE  
FAIL_HISTORICAL_DATA_CONFIRMATORY_IDENTIFIABILITY  
FAIL_BEYOND_STANDARD_RETROSPECTIVE_CLAIM  

ABSTAIN_MASON_CONFIRMATORY_IMPLEMENTATION  
ABSTAIN_HG31_UNIVERSAL_X_ON_HISTORICAL_CARRIERS  
HOLD_PHYSICAL_PROTOGEOMETRY

## Executive result

HG37 asks whether the historical public-data route can be rescued by independent calibration objects.

### Magnetism

The source paper explicitly states that the quoted approximately ±5 mT HEB uncertainty is the hysteresis field-step size. The public repository exposes a field conversion factor but the calibration audit finds no independent field-axis accuracy certificate, Hall-probe trace, readback uncertainty or calibration receipt.

The exact vector set-membership break threshold is:

\[
\Delta_H < \max_{n=2,\ldots,5}|H_{EB,n}| = 4.0754321208\ \mathrm{mT}.
\]

Current public bound:

\[
\Delta_H = 4.2932274337\ \mathrm{mT}.
\]

Only a 0.217795313 mT (5.073%) tightening would make the trained zero-bias vector non-saturating, but that tightening is not supported by a public calibration object.

For every trained loop to become individually nonabsorbable:

\[
\Delta_H < \min_{n=2,\ldots,5}|H_{EB,n}| = 0.8838269371\ \mathrm{mT}.
\]

### Adsorption

The Brown/NIST repository contains no external nonporous Xe/silica film-reference isotherm or independently calibrated FHH/surface-area reference that would point-identify the Cimino \(V_s\to Q\to q\) bridge.

However Mason (1988) applied a Bethe-tree network model directly to the same Brown Xe/Vycor 151 K scanning benchmark and explicitly states that his correlation method does not require separating capillary condensation from surface adsorption.

Therefore:

- failure of the Cimino reference rescue is **not** failure of standard network physics;
- the historical standard-null denominator remains incomplete;
- no retrospective beyond-standard claim is authorized.

## Strategic closure

The historical route is exhausted **for confirmatory HGMF attribution with currently available public calibration objects**, not exhausted as a source of standard-physics modeling.

HG37 therefore pivots to prospective measurements that acquire the missing calibration variables directly.

## Next gate

HGMF‑HG38 — Prospective calibration cartridge and future-only acquisition seal.
