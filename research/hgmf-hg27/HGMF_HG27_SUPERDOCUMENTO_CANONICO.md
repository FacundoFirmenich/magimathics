# HGMF‑HG27 — Adquisición secuencial, stopping rules y presupuesto de evidencia

**Fecha:** 9 de noviembre de 2026  
**Autoridad:** `EXACT COMBINATORICS / PROSPECTIVE DESIGN / NO-IMPUTATION / HOLDOUT PRESERVATION`

## Veredicto

```text
PASS_RECTANGLE_PREFIX_OPTIMAL_SCHEDULE
PASS_SWITCH_PARETO_SCHEDULE
PASS_BLINDED_VARIANCE_REESTIMATION_CONDITIONAL
PASS_PREREGISTERED_STOPPING_RULE
PASS_STRUCTURAL_EVIDENCE_BUDGET
PASS_HOLDOUT_PRESERVATION
PASS_RECEIPTED_ADAPTATION_CONTRACT

FAIL_ORDER_COMMUTATOR_IDENTIFIABILITY_FROM_BASE_GRID
FAIL_NUMERIC_SAMPLE_EXPANSION_WITHOUT_THRESHOLDS
FAIL_EARLY_SUCCESS_AUTHORIZATION

ABSTAIN_RESOURCE_CONSTRAINED_TOTAL
ABSTAIN_EMPIRICAL_ACQUISITION
HOLD_PHYSICAL_PROTOGEOMETRY
```

## 1. Optimalidad combinatoria

Para prefijos \((\ell,m,r)\):

\[
R=[\min(\ell,m)-1]_++[\min(m,r)-1]_+.
\]

\[
N_{\min}(0)=0,\quad N_{\min}(1)=4,
\]

\[
\boxed{N_{\min}(q)=\left\lceil\frac{3q}{2}\right\rceil+3}\quad(2\le q\le14).
\]

El schedule HG27 alcanza cada mínimo. La utilidad acumulada máxima es \(148\), y se requieren al menos 13 cambios de eje para alcanzarla.

## 2. Mirroring y holdout

Las waves 1–2 usan prioridades laterales opuestas. La prioridad de wave 3 y el orden entre carriers se derivan de un hash anterior a los datos. La secuencia es nuisance registrada, no un estimando causal.

## 3. Presupuesto

\[
B_{core}=72_{mag}+72_{ads}=144,
\]

\[
B_{train}=96,\qquad B_{holdout}=48.
\]

El commutator de orden no está incluido. Un reverse grid completo añadiría hasta 144 unidades:

\[
B_{full\ order}=288.
\]

## 4. Look ciego

Después de wave 1 puede reestimarse precisión con nuisance summaries:

\[
W_{req}=\left\lceil\left[\frac{2(z_{1-\alpha/2}+z_{1-\beta})\widehat\sigma}{\Delta^\star}\right]^2\right\rceil.
\]

No se inspeccionan signos, contrastes, nodos ni kernel scores. No hay expansión numérica autorizada porque no están sellados \(\Delta^\star\), half-width, multiplicity rule y \(N_{max}\).

## 5. Stopping

- QC/safety: anytime.
- Precision futility: wave 1.
- Structural futility: waves 1–2.
- Early success: prohibido.
- Final: one-shot tras wave 3 en ambos carriers.

Si se quisiera monitoring de efectos, sería obligatorio migrar a confidence sequences, e-processes o un design group-sequential explícito.

## 6. No-go del orden

El grid base contiene outcomes por nivel y profundidad, pero no ambas composiciones ordenadas:

\[
I_{ord}=\tfrac12[m(\Phi_H\Phi_Vx)-m(\Phi_V\Phi_Hx)].
\]

Sin ambos joint outcomes, \(I_{ord}\) no está identificado. No puede recuperarse del orden administrativo de adquisición.

## 7. Evidencia

No hay receipts admitidos. HG27 no afirma interacción, kernel, nodos, transferencia ni protogeometría. Su producto es un diseño secuencial protegido frente a optional stopping.

## 8. Próximo gate

`HGMF‑HG28 — Diseño de orden causal, gatekeeping multicomponente y decisión confirmatoria`.
