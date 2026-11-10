# HGMF‑HG38 — Prospective identifiability cartridge and future-only seal

**Fecha:** 10 de noviembre de 2026

## Veredicto

PASS_TWO_STAGE_PROSPECTIVE_SEAL  
PASS_MAGNETIC_CALIBRATION_RECEIPT_CONTRACT  
PASS_ADSORPTION_FILM_REFERENCE_RECEIPT_CONTRACT  
PASS_INDEPENDENT_TOPOLOGY_RECEIPT_CONTRACT  
PASS_HASH_CHAINED_ACQUISITION_CONTRACT  
PASS_FAIL_CLOSED_ARMING_VALIDATOR  
PASS_FUTURE_ONLY_INFORMATION_BARRIER  
PASS_METROLOGICAL_TRACEABILITY_REQUIREMENTS  

ABSTAIN_REAL_MAGNETIC_CALIBRATION_RECEIPT  
ABSTAIN_REAL_ADSORPTION_REFERENCE_RECEIPT  
ABSTAIN_REAL_TOPOLOGY_RECEIPT  
ABSTAIN_NUMERIC_FITNESS_FOR_PURPOSE_LIMITS  
ABSTAIN_CARTRIDGE_ARMING  

HOLD_PROSPECTIVE_OUTCOMES  
HOLD_PHYSICAL_PROTOGEOMETRY

## Resultado rector

HG38 converts the prospective pivot of HG37 into an executable two-stage control system.

### Stage 0 — protocol seal

Frozen now. It defines:

- permitted calibration objects;
- receipt schemas;
- future-only split;
- hash custody;
- allowed training operations;
- fail-closed admission rules;
- one-shot holdout adjudication.

It does **not** authorize acquisition.

### Stage 1 — arming seal

Can only be produced after real metrological receipts exist and before the first holdout outcome is acquired.

The current state is therefore:

`PROTOCOL_FROZEN_UNARMED`.

No placeholder calibration values are inserted. Numeric fitness-for-purpose limits remain intentionally unset until they are selected and frozen with the actual instrument and scientific minimum effect, before outcomes.

## Magnetic cartridge

Primary observable: the complete traceable `Vxy(H)` curve. `HEB` remains secondary.

Required:

- independent field reference at the sample position;
- documented calibration chain and uncertainty budget;
- pre/post ascending and descending calibration sweeps;
- covariance of the field map;
- full-range bracketing;
- raw repeated voltages;
- shared field-systematic model;
- full-curve likelihood or certified likelihood upper bound.

The historical 0.80 mT planning ceiling is recorded only as an engineering target below the smallest historical trained-loop offset. It is not a prospective claim threshold.

## Adsorption cartridge

Required:

- nonporous silica film reference with matched surface chemistry and pretreatment;
- same Xe lot as the porous sample;
- full-domain `Vs(p,T)` and `Vc(p,T)` with covariance;
- traceable pressure, temperature, mass and surface-area results;
- independent topology characterization completed before holdout;
- interleaved reference/sample measurements;
- frozen scanning paths and equilibrium rule.

## Current authority

`NO_ACQUISITION_AUTHORITY`.

The validator returns:

`ABSTAIN_NOT_ARMED_MISSING_REAL_RECEIPTS`.

## Próxima frontera

HGMF‑HG39 — real metrological commissioning, receipt acquisition and pre-outcome arming.
