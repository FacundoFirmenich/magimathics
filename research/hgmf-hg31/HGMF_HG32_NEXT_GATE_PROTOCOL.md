# HGMF‑HG32 — Complexity-cap selection, likelihood bridge y power audit universal

## Objetivo

Convertir los upper-bound methods HG31 en nulls físicamente sellados y auditar si conservan potencia suficiente con 24 holdout cells.

## Gate A — kernel caps

Derivar ranges físicos o instrumentales preregistrables para \(m^2,\alpha,\tau\). No usar wave 3.

## Gate B — HMM caps

Fijar \(K_{\max}\), mean boxes y variance floor/ceiling desde límites físicos/instrumentales o coverage-valid training procedure.

## Gate C — process-tensor observation bridge

Elegir una ruta:

1. RAW outcome likelihood; o
2. summary likelihood con covariance receipts.

## Gate D — PT outer bound

Implementar un convex outer profile-likelihood oracle o certificado equivalente.

## Gate E — ancilla bridge

Definir observation density y certified upper-bound oracle.

## Gate F — e-value power

Auditar, sin usar datos reales, cuánto slack introducen los upper bounds y qué likelihood ratio sería necesario para alcanzar \(E=140\).

## Gate G — fail-closed seal

Sólo adapters con caps y bound authority completos entran a X.

## Resultados autorizados

- PASS_PHYSICAL_COMPLEXITY_CAPS
- PASS_PROCESS_TENSOR_LIKELIHOOD_BRIDGE
- PASS_ANCILLA_LIKELIHOOD_BRIDGE
- PASS_UNIVERSAL_EVALUE_POWER_BUDGET
- FAIL_BOUND_TOO_LOOSE_FOR_CONFIRMATION
- ABSTAIN_CAPS_NOT_PHYSICALLY_JUSTIFIED
- HOLD_PHYSICAL_PROTOGEOMETRY
