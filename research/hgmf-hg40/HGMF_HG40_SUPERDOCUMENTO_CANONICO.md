# HGMF‑HG40 — Superdocumento canónico

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

## 1. La corrección conceptual

HG36–HG39 cerraron correctamente la no-identificabilidad absoluta:

- el campo magnético carece de calibración independiente suficiente;
- Brown no contiene una film reference que point-identifique \(V_s,Q,q\).

Pero de ello no se sigue que toda información histórica desaparezca.

Si varias observaciones comparten una nuisance afín, el cociente por esa nuisance conserva la geometría relativa.

Esta es la corrección de HG40:

```text
ABSOLUTE IDENTIFICATION = FAIL
RELATIVE QUOTIENT IDENTIFICATION = PASS
```

## 2. Magnetismo

Con una calibración común:

\[
H'=\alpha H+\beta,
\qquad \alpha>0,
\]

se transforman:

\[
H'_{EB,n}=\alpha H_{EB,n}+\beta,
\qquad
W'_n=\alpha W_n.
\]

Por tanto sobreviven diferencias normalizadas, ratios de widths y coordenadas afines entre loops.

### Datos reales

\[
H_{EB}=(-48.4257,\;0.8838,\;-4.0754,\;3.3383,\;1.3417)\;\mathrm{mT}.
\]

Half-widths coercivos:

\[
(83.8065,\;39.4570,\;44.8482,\;38.4276,\;42.7192)\;\mathrm{mT}.
\]

El trained-state medio es:

\[
\bar H_{EB,2:5}=0.37208\;\mathrm{mT},
\]

\[
\bar W_{2:5}=41.3630\;\mathrm{mT}.
\]

El contraste de training afín-invariante es:

\[
\boxed{
\frac{H_{EB,1}-\bar H_{EB,2:5}}
     {\bar W_{2:5}}
=-1.1797446
}.
\]

Las coordenadas afines del vector HEB, usando loops 1 y 2 como anchors, son:

\[
(0,\;1,\;0.89943,\;1.04978,\;1.00929).
\]

Un control numérico con:

\[
H' = 1.731H+11.37\;\mathrm{mT}
\]

produce error máximo:

\[
2.22\times10^{-16}.
\]

Para cinco loops, el grupo afín elimina dos grados y deja:

\[
\boxed{3}
\]

grados relativos identificables.

### Adjudicación física

La asimetría de switching del primer loop sigue siendo extraordinariamente distinta:

\[
|\log R_1|=3.61165,
\]

mientras los loops posteriores alcanzan como máximo:

\[
0.03250.
\]

Esto robustece el patrón de training del mecanismo estándar FGT/CrSBr. No crea un residuo HGMF.

## 3. Adsorción

A presión y temperatura fijas:

\[
V_h=V_c-(V_c-V_s)Q_h.
\]

Con dos historias anchor:

\[
\rho_h
=
\frac{V_h-V_a}{V_b-V_a}
=
\frac{Q_h-Q_a}{Q_b-Q_a}.
\]

Así \(V_s\) y \(V_c\) desaparecen exactamente del observable cociente.

### Tribunal real

Se utilizaron los cinco desorption scans simples de run 1 a 150.73 K:

| Segmento | presión inicial | adsorción inicial |
|---:|---:|---:|
| 1 | 0.4490 | 12.72 mg |
| 2 | 0.5835 | 17.90 mg |
| 3 | 0.6564 | 22.44 mg |
| 4 | 0.6863 | 24.96 mg |
| 5 | 0.7054 | 26.95 mg |

El teorema Bethe de no-passing predice que un scan que parte de un estado más lleno no debe caer por debajo de uno que parte de un estado menos lleno, a presión común.

Resultados:

- 10 pares de histories;
- 713 nodos locales;
- 51 diferencias negativas en point estimates;
- 6 de 10 pares con al menos una inversión cruda;
- peor inversión: \(-0.054525\) mg;
- 0 inversiones que superen la envolvente conservadora de incertidumbre;
- máxima fracción de tolerancia consumida: 0.31977.

Por tanto:

```text
EXACT RAW POINTWISE ORDER = FAIL
NO-PASSING REJECTION AT CURRENT UNCERTAINTY = FAIL
STANDARD BETHE ORDER NULL = SURVIVES
```

## 4. Geometría de cociente de adsorción

Se obtuvieron:

- 63 presiones no degeneradas;
- hasta 5 histories simultáneas;
- 242 coordenadas etiquetadas;
- 116 grados independientes de cociente.

En un snapshot real a:

\[
p=0.4164,
\]

las adsorciones fueron:

\[
(11.92463,\;12.21955,\;12.39323,\;12.49573,\;12.61000)\;\mathrm{mg},
\]

con coordenadas afines:

\[
(0,\;0.43031,\;0.68372,\;0.83327,\;1).
\]

Existen 11 coordenadas crudas fuera de \([0,1]\), con máximo 1.08533. Esas salidas corresponden a pequeñas inversiones de point estimates y no exceden la tolerancia conservadora.

## 5. Qué queda rescatado

### Sí

- training relativo magnético;
- branch-asymmetry ratios;
- geometría relativa de HEB;
- ordering y coordenadas cross-history de adsorción;
- restricciones de no-passing;
- toda claim expresable en el maximal invariant afín.

### No

- campo absoluto;
- \(Q(p)\) o \(q(p)\) absolutos;
- comparaciones de escala entre presiones distintas;
- likelihood físico completo;
- HG31 universal e-value carrier-specific;
- evidencia protogeométrica.

## 6. Resultado epistemológico

HG40 no rescata una anomalía. Rescata un **espacio de preguntas**.

Los datos históricos pueden seguir juzgando nulls estándar que vivan en el cociente, aunque no puedan identificar magnitudes absolutas.

En ambos carriers, la primera ejecución favorece o conserva física estándar:

- FGT/CrSBr training/domain null: sobrevive;
- Bethe no-passing: no rechazado.

## 7. Próxima frontera

HGMF‑HG41 deberá construir likelihoods directamente sobre maximal invariants y conectarlos a HG31:

\[
\boxed{
\text{quotient-space likelihood}
+
\text{finite-sample universal e-value}
}.
\]

El objetivo será testar nulls relativos sin reinstalar las calibraciones absolutas que el cociente eliminó.
