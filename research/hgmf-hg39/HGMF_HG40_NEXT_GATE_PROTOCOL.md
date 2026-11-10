# HGMF‑HG40 — Signed scopes, real commissioning and arming decision

## Objective

Convert the HG39 dossier from `UNCOMMISSIONED` to either:

- `COMMISSIONED_READY_FOR_ARMING`; or
- a documented fail/abstention with no holdout access.

## Gate A — provider scope confirmation

Obtain signed confirmations for the exact magnetic, adsorption and topology work packages.

## Gate B — magnetic result

Execute sample-plane/full-geometry calibration and issue a real `hgmf-magnetic-calibration-receipt/1.0`.

## Gate C — adsorption references

Execute the matched nonporous reference campaign and issue a real `hgmf-adsorption-reference-receipt/1.0`.

## Gate D — topology

Complete independent characterization and issue a real `hgmf-topology-receipt/1.0`.

## Gate E — fitness limits

Freeze numeric limits using real uncertainty budgets and the preregistered scientific decision rule.

## Gate F — arming

Run HG39/HG38 validators. If all receipts and limits pass and no holdout access exists, emit the HG38 arming seal.

## Authorized outcomes

- PASS_SIGNED_SCOPE_CONFIRMATIONS
- PASS_REAL_MAGNETIC_CALIBRATION
- PASS_REAL_ADSORPTION_REFERENCE
- PASS_REAL_TOPOLOGY_RECEIPT
- PASS_FITNESS_FOR_PURPOSE
- PASS_ARMED_FUTURE_ONLY
- FAIL_PROVIDER_SCOPE_MISMATCH
- FAIL_CALIBRATION_FITNESS
- ABSTAIN_RECEIPTS_INCOMPLETE
- HOLD_PROSPECTIVE_OUTCOMES
- HOLD_PHYSICAL_PROTOGEOMETRY
