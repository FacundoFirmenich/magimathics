# HGMF‑HG33 — Carrier-specific standard-null tribunal

## Objective

Replace generic nuisance placeholders with real physical competitor families for the two present empirical carriers.

## Gate A — magnetic metadata

Recover or preregister:

- material/composition;
- geometry;
- field waveform and rate;
- temperature;
- measured observable;
- calibration/noise floor.

## Gate B — magnetic models

Implement training-only adapters and holdout likelihood upper bounds for:

1. Preisach/generalized Preisach;
2. Jiles–Atherton/Duhem;
3. additional Play/Prandtl–Ishlinskii or dynamic model if jurisdiction requires.

## Gate C — adsorption metadata

Recover or preregister:

- adsorbate;
- substrate/material;
- pore regime/geometry;
- temperature;
- pressure definition;
- equilibrium protocol.

## Gate D — adsorption models

Implement the physically applicable subset of:

1. classical DFT/lattice-gas;
2. NLDFT/QSDFT;
3. capillary-condensation/pore-blocking/cavitation;
4. pore-network models.

## Gate E — likelihood jurisdiction

Every model must produce or upper-bound a likelihood on the exact holdout observation space. A merely qualitative curve is not a confirmatory nuisance adapter.

## Gate F — universal e-values

Plug carrier-specific upper bounds into the HG31 union-null denominator and audit slack against:

\[
\log E\ge4.941642.
\]

## Gate G — no false closure

If material/adsorbate metadata are insufficient to choose the standard family:

ABSTAIN_CARRIER_MODEL_JURISDICTION.

## Authorized outcomes

- PASS_MAGNETIC_STANDARD_NULL_TRIBUNAL
- PASS_ADSORPTION_STANDARD_NULL_TRIBUNAL
- PASS_CARRIER_SPECIFIC_NUISANCE_ENVELOPE
- FAIL_BOUND_TOO_LOOSE_FOR_CONFIRMATION
- ABSTAIN_CARRIER_MODEL_JURISDICTION
- HOLD_PHYSICAL_PROTOGEOMETRY
