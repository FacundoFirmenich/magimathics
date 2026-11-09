# HGMF‑HG31 — Contrato de complexity caps

Los caps no son tuning posterior. Definen el null que se pretende falsar.

## Kernel

Cada family continua requiere intervalos sellados:

- screened: \(m^2\in[m^2_-,m^2_+]\);
- fractional: \(\alpha\in[\alpha_-,\alpha_+]\);
- heat: \(\tau\in[\tau_-,\tau_+]\).

Sin ellos:

ABSTAIN_KERNEL_PARAMETER_CAPS_UNSEALED.

## HMM

Cada state box requiere:

- \(K_{\max}\);
- mean bounds por dimensión;
- variance floor y ceiling;
- emission family;
- transition family.

El analytic likelihood bound HG31 es válido para cualquier transition matrix porque la suma de probabilities de paths es uno.

Sin emission/variance bounds:

ABSTAIN_HMM_EMISSION_CAPS_UNSEALED.

## Process tensor

Requiere:

- number of time slots;
- local dimension;
- memory cutoff si aplica;
- bond dimension cap si se usa PT-MPO;
- compression tolerance;
- tomography/likelihood engine;
- observation bridge.

## Ancilla/control geometry

Requiere:

- latent-dimension/rank cap;
- map family;
- regularization;
- observation bridge.

## No data-derived caps without coverage

Un cap estimado de training puede redefinir aleatoriamente el null. Sólo se admite si:

1. fue fijado antes de data; o
2. se deriva mediante un procedimiento con garantía de cobertura incorporada al test.

En este corte no se autoriza la opción 2.
