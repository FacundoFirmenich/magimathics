# HGMF‑HG27 — Adquisición secuencial, stopping rules y presupuesto de evidencia

**Veredicto:** `PASS_RECTANGLE_PREFIX_OPTIMAL_SCHEDULE / PASS_SWITCH_PARETO_SCHEDULE / PASS_BLINDED_VARIANCE_REESTIMATION_CONDITIONAL / PASS_PREREGISTERED_STOPPING_RULE / FAIL_ORDER_COMMUTATOR_IDENTIFIABILITY_FROM_BASE_GRID / ABSTAIN_NUMERIC_EXPANSION / ABSTAIN_EMPIRICAL_ACQUISITION`.

## Resultados

- Una wave tiene 24 unidades y 14 rectángulos causales adyacentes.
- El mínimo de loops para \(q\) rectángulos es
  \[
  N_{\min}(1)=4,\qquad
  N_{\min}(q)=\lceil3q/2\rceil+3,\;q\ge2.
  \]
- El schedule canónico alcanza todos esos mínimos.
- La utilidad acumulada máxima es `148`.
- El mínimo de cambios de eje que alcanza `148` es `13`.
- El grid dual-carrier base contiene `144` unidades: `96` training y `48` holdout.
- No hay early success. Wave 3 sólo se abre después de cerrar waves 1–2 de ambos carriers.
- Se autoriza un único look ciego de precisión tras wave 1.
- La expansión numérica queda en `ABSTAIN` porque faltan \(\Delta^\star\), half-width, multiplicity rule y \(N_{\max}\).
- El grid base identifica interacción factorial simétrica, pero no el commutator de orden.
- El full reverse-order design añadiría hasta `144` unidades.
- No existen datos admitidos; el resultado empírico sigue en `ABSTAIN`.

## Próximo gate

`HGMF‑HG28 — Diseño de orden causal, gatekeeping multicomponente y decisión confirmatoria`.
