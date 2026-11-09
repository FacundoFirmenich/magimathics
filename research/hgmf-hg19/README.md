# HGMF‑HG19 — Métrica operacional de contexto, coste de acción y acoplamiento dimensional

**Veredicto:** `PASS_OPERATIONAL_CONTEXT_METRIC_CONDITIONAL / PASS_STANDARD_ACTION_TRANSGRESSION / PASS_BURES_SELECTION_CONDITIONAL / FAIL_NONZERO_HGMF_COUPLING / FAIL_STANDARD_GEOMETRY_EXCLUSION`.

## Resultado rector

Para una familia pura generada unitariamente:

\[
h^{\rm act}_{ij}
=\frac12\langle\{\Delta G_i,\Delta G_j\}\rangle
=\frac14\operatorname{Tr}\{G_i^{\min},G_j^{\min}\}
=\hbar^2g^Q_{ij}.
\]

La forma de área operacional es

\[
dA_{\rm act}=\hbar^2dA_Q,
\]

y la curvatura estándar satisface

\[
\mathcal F=\frac{2\chi_Q}{\hbar^2}dA_{\rm act}.
\]

HG19 selecciona una unidad física de acción², pero una corrección residual sólo puede escribirse como

\[
\delta\mathcal F=\frac{c_{\rm HG}}{\hbar^2}dA_{\rm act},
\]

con `c_HG` todavía no determinado.

## Mixed states

La monotonicidad no selecciona una métrica única: SLD, Wigner–Yanase y BKM difieren en tangentes no conmutativos. Si se añade el principio de mínima acción entre purificaciones, queda seleccionada condicionalmente la geometría Bures/SLD:

\[
h_B=\hbar^2g_B.
\]

## Cross-carrier

- isometrías constantes preservan exactamente la métrica de acción;
- canales accesibles contraen la métrica Bures;
- una ancilla oculta dependiente del parámetro puede inflar la geometría pura total sin cambiar el estado accesible.

Por tanto, el transporte debe definirse sobre el álgebra accesible, no sobre una purificación arbitraria.

## Auditoría

- error máximo `h_action - hbar^2 g_Q`: `1.11e-15`;
- error de covarianza: `1.33e-15`;
- error gauge QGT: `2.50e-16`;
- embedding qubit→qutrit: error `0`;
- contracción Bures: error `1.39e-16`;
- hidden ancilla: razón de áreas `sqrt(5)`;
- holdout formal: error relativo máximo `1.13e-14`.

## Portfolio

- Paper A: `EXPERIMENT_READY_UMI17_UNCHANGED`.
- Paper B: `FORMAL_CORE_SUBSTANTIALLY_COMPLETE_UMI22_ABSTENTION`.
- Paper C: `OPERATIONAL ACTION METRIC + STANDARD DIMENSIONAL TRANSGRESSION PASS; HGMF COUPLING + STANDARD EXCLUSION FAIL/HOLD`.

## Next gate

`HGMF‑HG20 — Selección del acoplamiento adimensional y tribunal residual transcarrier`.
