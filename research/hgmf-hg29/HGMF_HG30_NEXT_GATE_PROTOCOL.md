# HGMF‑HG30 — Adaptadores nuisance físicos, covariance receipts y dry-run end-to-end

## Objetivo

Completar la última capa técnica antes de adquisición real.

## Gate A — covariance receipts

Definir cómo cada extractor de componentes produce:

- estimate;
- standard error;
- covariance entre celdas;
- covariance entre modal blocks;
- calibration ancestry.

## Gate B — drift/control adapter

Implementar predictive distribution y split-predictive discrepancy.

## Gate C — hidden-state adapter

Implementar un modelo finito/regularizado entrenado sólo con waves 1–2.

## Gate D — bounded process-tensor adapter

Fijar complejidad, memoria, algoritmo y predictive check antes del holdout.

## Gate E — alternative-kernel adapter

Congelar la familia estándar de kernels y su predictive distribution.

## Gate F — hidden-ancilla/control-geometry adapter

Implementar el último null de la nuisance envelope.

## Gate G — end-to-end dry run

Ejecutar schemas, tests y adjudicator usando únicamente artefactos formales de validación, nunca outcomes empíricos inventados.

## Resultados autorizados

- PASS_COVARIANCE_RECEIPT_PROFILE
- PASS_ALL_NUISANCE_ADAPTERS
- PASS_END_TO_END_PIPELINE
- FAIL_CALIBRATED_PREDICTIVE_CHECK
- ABSTAIN_UNBOUNDED_NUISANCE_MODEL
- HOLD_PHYSICAL_PROTOGEOMETRY
