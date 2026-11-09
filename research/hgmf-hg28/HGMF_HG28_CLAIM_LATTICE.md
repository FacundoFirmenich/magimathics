# HGMF‑HG28 — Lattice confirmatoria de claims

## Nivel 0

NO_ADMISSIBLE_DATA / ABSTAIN.

## Nivel 1 — carrier-specific

Un carrier pasa un efecto, el otro no:

CARRIER_SPECIFIC_SIGNAL.

No es replicación HGMF.

## Nivel 2 — causal replicado

\(C_j\) pasa en 2/2 carriers:

DUAL_CARRIER_CAUSAL_COMPONENT.

## Nivel 3 — modal replicado

\(M_j\) pasa después de \(C_j\):

DUAL_CARRIER_MODAL_TRANSFER.

## Nivel 4 — nodal replicado

\(N_j\) pasa:

DUAL_CARRIER_NODAL_TRANSFER.

## Nivel 5 — residual fuera de nuisance

\(X_j\) pasa:

CANDIDATE_BEYOND_STANDARD_COMPONENT_SIGNATURE.

## Nivel 6 — orden

Si además \(O_j\) pasa:

ORDER_SENSITIVE_CANDIDATE_SIGNATURE.

## Multicomponente

Si dos o más componentes alcanzan el mismo nivel, puede informarse MULTICOMPONENT_<LEVEL> como resumen lógico de claims ya controladas. No se crea una nueva prueba por promedio.

## Prohibición

Ninguno de estos niveles autoriza por sí solo PHYSICAL_PROTOGEOMETRY_CONFIRMED. Esa claim requiere replicación externa independiente y cierre de atribución física.
