# HGMF‑HG27 — Adquisición secuencial, stopping rules y presupuesto de evidencia

## Objetivo

Optimizar la adquisición real sin optional stopping ni pérdida de identificabilidad.

## Gate A — ordering

Derivar un orden de adquisición que maximice:

- rectangles completed per loop;
- prefix closure;
- wave independence;
- calibration reuse;
- safety and instrument constraints.

## Gate B — blinded variance

Permitir reestimación de variance sólo desde QC blinded/component-neutral, sin leer signos causales ni outcomes de holdout.

## Gate C — stopping

Congelar:

- success boundaries;
- futility boundaries;
- safety/QC stops;
- maximum sample size;
- alpha spending o evidence thresholds.

Ningún stop puede depender de inspección visual no registrada.

## Gate D — evidence budget

Distribuir loops/runs entre:

- causal rectangles;
- modal blocks;
- nodal precision;
- carrier transfer;
- nuisance discrimination.

## Gate E — holdout preservation

Wave 3 permanece sellada. Toda decisión adaptativa usa waves 1–2 o summaries blinded.

## Gate F — receipts

Cada adquisición y decisión de stopping genera un receipt y actualiza el provenance DAG.

## Gate G — resultados autorizados

- `PASS_SEQUENTIAL_ACQUISITION_PLAN`
- `PASS_BLINDED_VARIANCE_REESTIMATION`
- `PASS_PREREGISTERED_STOPPING_RULE`
- `FAIL_EVIDENCE_BUDGET`
- `ABSTAIN_NO_RESOURCE_CONSTRAINTS`
