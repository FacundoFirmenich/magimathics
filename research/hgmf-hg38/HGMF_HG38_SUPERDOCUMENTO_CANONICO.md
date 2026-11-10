# HGMF‑HG38 — Prospective identifiability cartridge

## Veredicto

PASS_TWO_STAGE_PROSPECTIVE_SEAL  
PASS_MAGNETIC_CALIBRATION_RECEIPT_CONTRACT  
PASS_ADSORPTION_FILM_REFERENCE_RECEIPT_CONTRACT  
PASS_INDEPENDENT_TOPOLOGY_RECEIPT_CONTRACT  
PASS_HASH_CHAINED_ACQUISITION_CONTRACT  
PASS_FAIL_CLOSED_ARMING_VALIDATOR  
PASS_FUTURE_ONLY_INFORMATION_BARRIER  
PASS_METROLOGICAL_TRACEABILITY_REQUIREMENTS  

ABSTAIN_REAL_CALIBRATION_AND_REFERENCE_RECEIPTS  
ABSTAIN_NUMERIC_FITNESS_FOR_PURPOSE_LIMITS  
ABSTAIN_CARTRIDGE_ARMING  
HOLD_PROSPECTIVE_OUTCOMES  
HOLD_PHYSICAL_PROTOGEOMETRY

## 1. Strategic closure

HG37 showed that the historical route is not confirmatorily identifiable. HG38 responds by freezing the missing measurement structure before any new outcome.

## 2. Two-stage authority

The Stage-0 protocol seal is now frozen and hash-addressed. It specifies what may be measured, calibrated, trained and adjudicated.

The Stage-1 arming seal does not exist yet. It requires real receipts and numeric fitness limits.

Therefore the protocol is complete while acquisition authority remains absent.

## 3. Magnetic design

The primary observable becomes the full `Vxy(H_ref)` curve. A traceable reference-field map, covariance, drift, raw voltage repeats and a shared systematic model are mandatory. `HEB` is retained only as a secondary summary.

The 0.80 mT value is an engineering planning ceiling derived before prospective acquisition. It is explicitly non-confirmatory and must be replaced by a real fitness-for-purpose limit in the arming seal.

## 4. Adsorption design

Point identification is created experimentally rather than inferred retrospectively:

- independent nonporous silica film reference;
- matched surface chemistry and pretreatment;
- same Xe lot;
- traceable temperature, pressure, mass and surface area;
- full-domain `Vs` and `Vc` covariance;
- independent pore topology receipt;
- interleaved reference/sample order.

## 5. Future-only custody

After arming, thresholds, families, code and holdout design are frozen. Acquisition events form a hash chain. Premature access, expired calibration or missing receipts fail closed.

## 6. Current state

`PROTOCOL_FROZEN_UNARMED`  
`NO_ACQUISITION_AUTHORITY`  
`NO_PROSPECTIVE_OUTCOMES_ADMITTED`

## 7. Next gate

HGMF‑HG39 — obtain real calibration/reference receipts, freeze numeric decision limits and issue the first valid arming seal.
