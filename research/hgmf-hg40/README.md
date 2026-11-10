# HGMF‑HG40 — Identificabilidad por cociente afín

**Fecha:** 10 de noviembre de 2026

## Veredicto

```text
PASS_AFFINE_QUOTIENT_IDENTIFIABILITY_THEOREM
PASS_MAGNETIC_COMMON_AFFINE_NUISANCE_CANCELLATION
PASS_MAGNETIC_RELATIVE_TRAINING_GEOMETRY
PASS_ADSORPTION_REFERENCE_FREE_QUOTIENT
PASS_BETHE_NO_PASSING_THEOREM
PASS_NO_PASSING_NOT_REJECTED_AT_TABULATED_UNCERTAINTY
PASS_PARTIAL_HISTORICAL_IDENTIFIABILITY_RESCUE

FAIL_EXACT_POINTWISE_NO_PASSING_ON_RAW_POINT_ESTIMATES
FAIL_ABSOLUTE_FIELD_IDENTIFICATION
FAIL_ABSOLUTE_Q_q_IDENTIFICATION
FAIL_STANDARD_SOURCE_NULL_EXCLUSION

ABSTAIN_MODEL_SPECIFIC_QUOTIENT_LIKELIHOOD
ABSTAIN_HG31_UNIVERSAL_X
HOLD_PHYSICAL_PROTOGEOMETRY
```

## Resultado rector

HG36–HG39 demostraron que los observables absolutos no identifican el campo magnético ni los estados de red de Vycor sin calibraciones externas.

HG40 demuestra algo distinto:

\[
\boxed{
\text{no identificabilidad absoluta}
\not\Rightarrow
\text{ausencia de información relativa}
}
\]

Si una nuisance actúa afínmente sobre varias observaciones etiquetadas, el cociente por esa acción conserva \(m-2\) grados relativos.

### Magnetismo

Para cinco loops y una calibración común:

\[
H'=\alpha H+\beta,
\]

quedan tres grados de cociente identificables.

Resultado real:

- contraste loop 1 versus trained state: \(-1.1797446\) half-widths entrenados;
- dimensión identificada: 3;
- error máximo al aplicar una transformación afín de control: \(2.22\times10^{-16}\);
- asimetría logarítmica de loop 1: 3.61165;
- máxima asimetría posterior: 0.03250.

La geometría relativa de training sobrevive a una calibración común desconocida. Y favorece el mecanismo estándar FGT/CrSBr: no produce un residuo HGMF.

### Adsorción

A presión y temperatura fijas:

\[
V_h=V_c-(V_c-V_s)Q_h.
\]

Los cocientes entre historias eliminan exactamente \(V_s\) y \(V_c\).

Sobre los cinco scans simples de run 1 a 150.73 K:

- 10 pares de historias;
- 713 comparaciones locales;
- 63 presiones con cociente no degenerado;
- hasta 5 historias simultáneas;
- 116 grados de cociente identificados;
- 0 violaciones que excedan la envolvente conservadora de incertidumbre.

Los point estimates contienen 51 inversiones locales y 11 coordenadas fuera de \([0,1]\), pero ninguna inversión consume más del 31.98% de la tolerancia conservadora; la peor diferencia es \(-0.05453\) mg.

Por tanto el no-passing Bethe **no queda rechazado**.

## Corrección estratégica

El commissioning de HG38–HG39 sigue siendo necesario para claims absolutos y likelihoods físicos completos.

Pero deja de ser correcto afirmar que los datos históricos carecen de toda identificabilidad sin esa calibración. Existe una vía de cociente para claims relativos y nulls invariantes.

## Próxima frontera

HGMF‑HG41 — maximal-invariant likelihoods and quotient-space universal e-values.
