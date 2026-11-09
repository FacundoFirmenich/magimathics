# HGMF‑HG25 — Espectroscopia causal modal y ejecución nodal dual-carrier

## Objetivo

Ejecutar el primer cierre empírico de la arquitectura HG23–HG24.

## Gate A — magnetic completion

Ejecutar los 18 loops faltantes del preset `-` y conservar `(A,B,C,K,E,Q,Z)`.

## Gate B — causal rectangles

Estimar por wave y componente:

\[
I_{VH},\qquad I_{sym},\qquad I_{ord}.
\]

## Gate C — modal training

Proyectar fuente e interacción sobre al menos cuatro bloques espectrales no degenerados. Congelar kernel y gamma con waves 1–2.

## Gate D — magnetic holdout

Predecir en wave 3 amplitudes modales, nodos, signos, flujos parciales e interacción de orden.

## Gate E — second carrier

Ejecutar 72 runs homólogos de adsorción o un carrier alternativo que pase UMI+QGT.

## Gate F — carrier transfer

Transportar potenciales, fuente, eigenblocks, kernel y response scale sin reajuste.

## Gate G — attribution

Comparar contra drift, hidden-state models, process tensors, control geometry, alternative kernels y outcome rescalings.

## Salidas autorizadas

- `PASS_CAUSAL_MODAL_SPECTROSCOPY`
- `PASS_KERNEL_PHYSICAL_SELECTION`
- `PASS_DUAL_CARRIER_NODAL_EXECUTION`
- `FAIL_CAUSAL_COLOCALIZATION`
- `FAIL_CROSS_CARRIER_TRANSFER`
- `FAIL_STANDARD_RESPONSE_EXCLUSION`
- `ABSTAIN_INSUFFICIENT_EXECUTION`
- `HOLD_PHYSICAL_PROTOGEOMETRY`
