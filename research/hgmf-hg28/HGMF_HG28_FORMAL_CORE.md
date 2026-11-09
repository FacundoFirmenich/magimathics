# HGMF‑HG28 — Núcleo formal

## 1. Dos estimandos causales distintos

Para cada componente \(j\), carrier \(c\) y rectángulo/contexto \(r\):

### Interacción simétrica
\[
I^{sym}_{cjr}=m_{11}-m_{10}-m_{01}+m_{00}.
\]

### Efecto de orden
Para dos secuencias con el mismo estado inicial y endpoints físicos:
\[
I^{ord}_{cjr}
=
\frac12\left(Y_{H\to V}-Y_{V\to H}\right).
\]

Ninguno determina al otro.

## 2. Módulo sparse de orden

Se seleccionan antes de datos:

- ambos intervalos laterales;
- edges de historia \(1\to2,4\to5,7\to8\).

Así hay:
\[
2\times3=6
\]
contextos por wave y carrier.

Cada contexto contiene dos sequence blocks:
\[
H\to V,\qquad V\to H.
\]

El programa completo contiene:
\[
6\times2\times3\times2=72
\]
blocks.

## 3. Replicabilidad direccional 2/2

Para un estimando \(t\in\{sym,ord\}\), componente \(j\), y one-sided p-values válidos en magnetismo \(M\) y adsorción \(A\):
\[
p^+_{tj}=\max(p^+_{M,tj},p^+_{A,tj}),
\]
\[
p^-_{tj}=\max(p^-_{M,tj},p^-_{A,tj}).
\]

Como la dirección no está preregistrada:
\[
p^{rep}_{tj}
=
\min\left[1,2\min(p^+_{tj},p^-_{tj})\right].
\]

## 4. Multiplicidad

Se forman exactamente \(14\) p-values:
\[
\{p^{rep}_{sym,j},p^{rep}_{ord,j}:j\in(A,B,C,K,E,Q,Z)\}.
\]

Se aplica Holm step-down a nivel:
\[
\alpha=0.05.
\]

## 5. Antiagregación

No se usa un promedio escalar de componentes como gate confirmatorio. Cada componente conserva signo, incertidumbre, causalidad, modalidad, nodos y transferencia.

## 6. Gate causal-modal

Un componente sólo puede alcanzar REPLICATED_CAUSAL_MODAL_STRUCTURE si primero pasa el gate causal simétrico replicado y además, sin refit:

1. source support;
2. kernel freeze;
3. wave-3 modal prediction in both carriers;
4. sign agreement;
5. nodal tolerance;
6. QGT+UMI carrier-map gate.

## 7. Kernel

CROSS_CARRIER_KERNEL_NODAL_LAW requiere:

- same frozen kernel family in both carriers;
- held-out predictive superiority;
- parameters outside declared family intersections;
- node/sign/modal transfer;
- no carrier-specific kernel refit.

## 8. Nuisance

CANDIDATE_NONSTANDARD_CROSS_CARRIER_RESPONSE requiere además fracaso de la nuisance class congelada: drift, hidden-state, control geometry, alternative standard kernels, process tensor, outcome rescaling y carrier-map misspecification.

## 9. Claim boundary

Dos carriers no autorizan por sí solos PHYSICAL_PROTOGEOMETRY. El máximo resultado de HG28 es un candidato físico cross-carrier que requiere ulterior replicación o una predicción mecanística nueva.
