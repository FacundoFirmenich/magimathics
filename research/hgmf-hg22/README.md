# HGMF‑HG22 — Fuente relacional, selección modal y falsadores nodales transcarrier

**Fecha:** 9 de noviembre de 2026  
**Autoridad:** `FORMAL / ORIENTED SURFACE / SOURCE–RESPONSE / EXACT WITNESS`

## Veredicto

```text
PASS_RELATIONAL_JACOBIAN_SOURCE_CONDITIONAL
PASS_SOURCE_OPERATOR_UNIQUENESS_IN_DECLARED_CLASS
PASS_MINIMUM_ACTION_GREEN_RESPONSE_CONDITIONAL
PASS_MODAL_SUPPORT_SELECTION
PASS_COMPOSITION_INTERACTION_LAW
PASS_CROSS_CARRIER_NODAL_FALSIFIER_CONDITIONAL
PASS_FORMAL_FUTURE_ONLY_HOLDOUT

FAIL_RELATIONAL_POTENTIAL_UNIQUENESS
FAIL_GENERAL_KERNEL_UNIQUENESS
FAIL_STANDARD_RESPONSE_EXCLUSION
FAIL_EMPIRICAL_HGMF_SOURCE_IDENTIFICATION

HOLD_PHYSICAL_PROTOGEOMETRY
```

## Resultado rector

Dados dos potenciales relacionales preregistrados \(a,b\), la fuente

\[
\boxed{s_{HG}=*(da\wedge db)}
\]

es la única fuente escalar de primer orden, bilineal, alternante y natural dentro de la clase declarada. En una superficie cerrada tiene flujo total cero.

Si se añade el principio de mínima acción local, cuadrática, isotrópica y sin escala nueva:

\[
\boxed{\mathcal Lf_{HG}=\gamma s_{HG}.}
\]

La fuente selecciona el soporte modal; Green selecciona el peso \(1/\lambda\). La selección del par de potenciales y del principio dinámico sigue abierta.

## Testigo exacto

En la esfera QGT:

\[
a=x,
\qquad
b=y\left(z+\frac1{18}\right),
\]

\[
s=4\left(z^2-y^2+\frac{z}{18}\right),
\]

\[
f=\frac16(z^2-y^2)+\frac{z}{36}.
\]

En el meridiano \(x=0\), los nodos retenidos son:

\[
\boxed{z=\frac23,\qquad z=-\frac34.}
\]

Un embedding isométrico qubit→qutrit los transporta exactamente. La inversión de orientación cambia el signo, no los nodos.

## Kernel tribunal

Identity, Green, screened Green, fractional y heat responses producen nodos distintos sobre la misma fuente. La fuente canónica no basta para elegir la dinámica.

## Frontera científica

Poisson brackets, Green operators, Laplace spectral multipliers, nodal sets, functional maps y process tensors son ciencia establecida. HG22 aporta una integración formal y un contrato de falsación, no una identificación física de protogeometría.

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`; se añade frontera de transporte fuente/QGT.
- Paper C: `RELATIONAL SOURCE OPERATOR + NODAL FALSIFIER PASS CONDITIONAL; POTENTIALS, KERNEL AND ORIGIN FAIL/HOLD`.

## Próxima frontera

`HGMF‑HG23 — Potenciales relacionales triaxiales, normalización de fuente y protocolo nodal empírico`.
