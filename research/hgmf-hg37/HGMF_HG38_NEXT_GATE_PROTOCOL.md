# HGMF-HG38 — Prospective calibration cartridge and future-only acquisition seal

## Objective

Turn the HG37 pivot into executable acquisition contracts.

## Gate A — magnetic calibration receipt

Schema must require:
- commanded field;
- measured/readback field;
- calibration method/device;
- calibration uncertainty;
- calibration date;
- traceability;
- shared calibration ID across a loop/wave;
- raw Hall-voltage repeats.

## Gate B — magnetic crossing contract

Freeze:
- crossing estimator;
- interpolation model;
- allowed field-warp nuisance;
- calibration-bound admission rule.

The future confirmatory effect threshold must be specified independently of the historical outcome.

## Gate C — adsorption film-reference receipt

Schema must require:
- nonporous reference identity and chemistry;
- adsorbate;
- temperature;
- mass/surface-area normalization;
- pressure grid;
- uncertainty;
- reference age/calibration;
- mapping to the Vycor run.

## Gate D — network-topology receipt

Freeze independent connectivity information or a training-only topology estimator.

## Gate E — Mason branch

Either:
1. fully implement and verify the Mason Brown-specific direct network method; or
2. keep it as an unresolved standard null that blocks beyond-standard attribution.

## Gate F — future-only seal

Historical outcomes may initialize design but may not contribute to confirmatory test statistics.

## Gate G — acquisition readiness

Authorized outcomes:
- PASS_MAGNETIC_CALIBRATION_RECEIPT
- PASS_ADSORPTION_REFERENCE_RECEIPT
- PASS_FUTURE_ONLY_CALIBRATION_SEAL
- PASS_PROSPECTIVE_IDENTIFIABILITY
- FAIL_CALIBRATION_BOUND_TOO_LARGE
- ABSTAIN_MASON_IMPLEMENTATION
- HOLD_PHYSICAL_PROTOGEOMETRY
