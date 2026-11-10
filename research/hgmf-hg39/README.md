# HGMF‑HG39 — Commissioning dossier and arming preflight

**Fecha:** 10 de noviembre de 2026

## Veredicto

PASS_COMMISSIONING_ROUTE_CLOSURE  
PASS_MAGNETIC_TRACEABILITY_ROUTE  
PASS_ADSORPTION_REFERENCE_ROUTE  
PASS_INDEPENDENT_TOPOLOGY_ROUTE  
PASS_FITNESS_RULE_COMPILER  
PASS_COMMISSIONING_EVIDENCE_SCHEMA  
PASS_FAIL_CLOSED_PREARMING_VALIDATOR  
PASS_LOCAL_AND_NATIONAL_CAPABILITY_DISCOVERY  

ABSTAIN_REAL_MAGNETIC_CALIBRATION_RECEIPT  
ABSTAIN_REAL_ADSORPTION_REFERENCE_RECEIPT  
ABSTAIN_REAL_TOPOLOGY_RECEIPT  
ABSTAIN_SIGNED_SCOPE_CONFIRMATIONS  
ABSTAIN_NUMERIC_FITNESS_LIMITS  
ABSTAIN_HG38_ARMING  

HOLD_ACQUISITION  
HOLD_PROSPECTIVE_OUTCOMES  
HOLD_PHYSICAL_PROTOGEOMETRY

## Resultado rector

HG39 closes the commissioning route but does not fabricate commissioning.

The gate distinguishes four evidence levels:

1. `CAPABILITY_DISCOVERY`;
2. `ACCREDITED_SCOPE`;
3. `SIGNED_SERVICE_CONFIRMATION`;
4. `ACTUAL_MEASUREMENT_RESULT`.

Only level 4 can satisfy a real HG38 receipt. A laboratory website, an accreditation number, a catalogue specification or a quotation cannot be silently promoted to a traceable result.

## Magnetic route

The preferred route is:

1. calibrated Hall/field reference instrument from an ISO/IEC 17025 magnetic laboratory or national metrology institute;
2. transfer calibration at the actual sample position and final cryostat geometry;
3. pre/post, ascending/descending, full-range sweeps;
4. covariance-bearing map from command/readback to sample field;
5. independently frozen fitness rule;
6. full `Vxy(H_reference)` acquisition.

Candidate capability routes are frozen in `HGMF_HG39_COMMISSIONING_ROUTE_MATRIX.csv`. They remain candidates until signed scope and actual result receipts exist.

## Adsorption route

The reference cartridge requires:

- nonporous silica reference matched in surface chemistry and pretreatment;
- same Xe lot, pressure system and temperature protocol as the porous sample;
- traceable pressure, temperature and mass results;
- interleaved reference/sample/reference acquisition;
- full-domain `Vs`, `Vc` and covariance;
- independent topology characterization.

NIST BET/SAXS reference materials may validate instrument performance. They do not replace the matched nonporous `Vs` specimen.

## Current authority

```text
DOSSIER_FROZEN_UNCOMMISSIONED
NO_ARMING_AUTHORITY
NO_ACQUISITION_AUTHORITY
```

## Próxima frontera

HGMF‑HG40 — Signed service scopes, real commissioning measurements and HG38 arming decision.
