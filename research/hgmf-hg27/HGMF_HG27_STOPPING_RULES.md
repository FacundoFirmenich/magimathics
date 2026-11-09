# HGMF‑HG27 — Reglas de parada preregistradas

## STOP_QC

Pause/quarantine inmediato por calibration/reset failure, provenance failure, prefix break, safety o holdout contamination. No produce inferencia.

## STOP_PRECISION_FUTILITY

En el único look ciego de wave 1:

\[
W_{req}>W_{max}.
\]

No se inspecciona el efecto.

## STOP_STRUCTURAL_FUTILITY

Después de waves 1–2:

- menos de cinco eigenblocks útiles;
- source rank deficient;
- no admissible UMI+QGT carrier map;
- nuisance no congelable;
- training Jacobian sin rango completo.

## NO_EARLY_SUCCESS

Ninguna claim positiva HGMF, kernel, transfer o nodal puede detenerse antes de completar ambos holdouts.

## FINAL ONE-SHOT

Después de wave 3 en ambos carriers se aplica la decisión final congelada. No hay refit, cambio de kernel, movimiento nodal ni nueva calibración.

## Contingencia anytime-valid

Si se requiere monitoring de efectos, deberá sustituirse el modo fijo por confidence sequences, e-processes/always-valid p-values o un design group-sequential sellado. No se autoriza mezclar fixed-sample inference y optional stopping.
