# HGMF‑HG39 — Real metrological commissioning and pre-outcome arming

## Objective

Transform the HG38 protocol from `UNARMED` to `ARMED` without acquiring or opening any confirmatory holdout outcome.

## Gate A — magnetic commissioning

Obtain a real reference-field calibration at the sample position, including:

- traceability chain;
- pre/post bidirectional sweeps;
- map covariance;
- drift;
- full-range bracketing;
- frozen numeric fitness limit;
- full-curve field grid.

## Gate B — adsorption reference commissioning

Measure a nonporous matched silica reference and porous sample using the same Xe lot, pressure system and temperature protocol. Produce `Vs`, `Vc` and covariance over the full domain.

## Gate C — topology commissioning

Obtain independent pore-size/connectivity characterization before holdout and freeze its admissible model family.

## Gate D — training freeze

Use only calibration/training data to freeze:

- field likelihood;
- `Vs/Vc/q` observation map;
- topology model;
- equilibrium criteria;
- holdout paths;
- decision rules;
- numeric fitness limits.

## Gate E — arming seal

Issue `hgmf-hg38-arming-seal/1.0`, verify all hashes, confirm an empty holdout access log, and set the first permissible holdout timestamp.

## Authorized outcomes

- PASS_REAL_MAGNETIC_CALIBRATION
- PASS_REAL_ADSORPTION_REFERENCE
- PASS_REAL_TOPOLOGY_RECEIPT
- PASS_FITNESS_FOR_PURPOSE
- PASS_ARMED_FUTURE_ONLY
- FAIL_CALIBRATION_FITNESS
- FAIL_REFERENCE_DOMAIN_COVERAGE
- ABSTAIN_RECEIPTS_INCOMPLETE
- HOLD_PHYSICAL_PROTOGEOMETRY
