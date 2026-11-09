# HGMF‑HG28 — Lattice confirmatorio de claims

## Level 0 — NO_CONFIRMATORY_CAUSAL_SIGNAL

Ninguno de los 14 claims replicados pasa Holm.

## Level 1 — REPLICATED_SYMMETRIC_CAUSAL_COMPONENT[j]

Requiere:
- same-direction effect in both carriers;
- directional 2/2 p-value;
- Holm rejection.

Independientemente, REPLICATED_ORDER_EFFECT_COMPONENT[j] requiere el order module y el mismo gate estadístico.

## Level 2 — REPLICATED_CAUSAL_MODAL_STRUCTURE[j]

Requiere Level 1 symmetric +:
- frozen modal map;
- held-out modal transfer;
- sign agreement;
- nodal tolerance;
- no holdout refit.

## Level 3 — CROSS_CARRIER_KERNEL_NODAL_LAW[j]

Requiere Level 2 +:
- same kernel family in both carriers;
- held-out predictive margin over alternatives;
- parameter estimate outside declared model-intersection boundaries;
- no carrier-specific kernel refit.

## Level 4 — CANDIDATE_NONSTANDARD_CROSS_CARRIER_RESPONSE[j]

Requiere Level 3 +:
- frozen nuisance tribunal fails to absorb the residual;
- provenance and holdout seals intact;
- outcome-unit mapping frozen;
- carrier transport preregistered.

## Level 5 — HGMF_COMPATIBLE_PHYSICAL_CANDIDATE

Puede usarse sólo como descripción de compatibilidad si al menos un componente alcanza Level 4 y el patrón coincide con una predicción HGMF preregistrada.

No autoriza PHYSICAL_PROTOGEOMETRY.

Para ese claim se exige ulterior evidencia: tercer carrier, intervención mecanística exclusiva o predicción cuantitativa externa no usada en calibración.

## Downgrades

- one carrier only → CARRIER_SPECIFIC_ONLY;
- causal pass, modal fail → REPLICATED_CAUSAL_ONLY;
- modal pass, kernel ambiguous → REPLICATED_CAUSAL_MODAL_STRUCTURE;
- kernel pass, nuisance absorbed → STANDARD_COMPATIBLE_RESPONSE;
- holdout contaminated → EXPLORATORY_ONLY.
