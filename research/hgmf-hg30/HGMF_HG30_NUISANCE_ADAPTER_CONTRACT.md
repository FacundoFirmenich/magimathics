# HGMF‑HG30 — Contrato de adapters nuisance

## Interface común

Todo adapter debe separar:

1. fit training-only;
2. complexity cap;
3. predictive object para wave 3;
4. discrepancy frozen;
5. p-value/calibration statement;
6. provenance;
7. calibration authority.

## Estado por familia

| Familia | Engine | Predictive object | Autoridad actual |
|---|---|---|---|
| drift/control | in-repo linear Gaussian | exact finite-sample F | EXACT_FINITE_SAMPLE |
| alternative kernels | in-repo spectral nonlinear fit | Gaussian mean/cov via delta propagation | ASYMPTOTIC_THEOREM_PENDING_REGIME_AUDIT |
| finite hidden state | in-repo bounded Gaussian HMM | predictive sampler | FROZEN_PREDICTIVE_ONLY / family-level HOLD |
| bounded process tensor | external bounded PT engine adapter | engine-specific | HOLD |
| hidden ancilla/control geometry | external bounded engine adapter | engine-specific | HOLD |

## Process tensor bounds

Un adapter PT debe declarar como mínimo:

- number of time steps;
- memory cutoff;
- local system dimension;
- maximum MPO bond dimension;
- compression tolerance;
- tomography/fit algorithm;
- training-only ancestry;
- predictive distribution construction.

Una declaración “process tensor” sin estos bounds queda:

ABSTAIN_UNBOUNDED_NUISANCE_MODEL.

La bond dimension posee interpretación operacional como memoria ancilla efectiva en representaciones MPO del process tensor; por tanto es un cap científico, no sólo computacional.

## Hidden state

El HMM implementado es un nuisance concreto, no “todos los hidden-state models”. Debe fijar K antes del holdout. Elegir K mirando wave 3 invalida el adapter.

## Kernel

Los candidates son identity, Green, screened, fractional y heat. El fit nonlinear produce parameter uncertainty propagada por Jacobian. Esa aproximación necesita auditoría de régimen antes de autoridad confirmatoria.

## Ancilla/control geometry

HG30 no inventa un solver. El adapter sólo acepta predictive receipts de un engine bounded/regularized con latent-dimension cap, map family y split correcto.
