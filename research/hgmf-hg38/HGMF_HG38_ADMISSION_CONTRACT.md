# HGMF‑HG38 — Admission and arming contract

## Current state

`PROTOCOL_FROZEN_UNARMED`.

## Arming requirements

The validator authorizes holdout acquisition only when all of the following pass:

1. protocol self-hash;
2. arming-seal self-hash;
3. exact protocol-hash linkage;
4. empty pre-arming holdout access log;
5. real magnetic calibration receipt;
6. magnetic uncertainty and drift fitness;
7. calibration validity covering acquisition;
8. real adsorption film-reference receipt;
9. full pressure-domain coverage;
10. real independent topology receipt;
11. frozen design artifacts;
12. frozen analysis environment;
13. first holdout timestamp strictly after arming.

Missing values are never imputed.

A missing receipt, null numeric limit, expired calibration, domain gap, hash mismatch or premature holdout access produces:

`FAIL_CLOSED_NOT_ARMED`.

## Current adjudication

Because no real commissioning receipts exist:

`ABSTAIN_NOT_ARMED_MISSING_REAL_RECEIPTS`.
