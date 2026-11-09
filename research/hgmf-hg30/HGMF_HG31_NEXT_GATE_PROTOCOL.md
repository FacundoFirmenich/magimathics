# HGMF‑HG31 — Finite-sample calibration de nuisance compleja, complexity caps y null simulation auditada

## Objetivo

Elevar HMM, kernels, process tensor y ancilla desde implementation/predictive status a confirmatory authority o rechazarlos como no calibrables bajo el presupuesto actual.

## Gate A — kernel calibration

Auditar cobertura/tamaño del predictive check nonlinear en el régimen 48-train/24-holdout y alpha/7.

## Gate B — HMM calibration

Fijar K, emission family, training algorithm y discrepancy. Derivar o verificar una calibrated split/conditional test con error control compatible con alpha/7.

## Gate C — PT complexity cap

Congelar memory steps, local dimension, bond dimension, compression tolerance y tomography algorithm.

## Gate D — PT calibration

Usar un engine real bounded PT/PT-MPO; no surrogate. Evaluar holdout predictive p-value con calibration authority explícita.

## Gate E — ancilla/control geometry

Congelar latent dimension/rank y engine real. Auditar predictive calibration.

## Gate F — calibration error budget

Si la validez es aproximada, cuantificar un bound epsilon para:

\[
\sup_{H_0}P(p\le t)\le t+\epsilon.
\]

El error de calibración debe incorporarse al presupuesto confirmatorio, no ignorarse.

## Gate G — null simulation receipts

Toda simulación bajo null debe portar model hash, seed, code/environment, parameter source, complexity cap y output hashes. Es validación estadística, no evidencia empírica.

## Resultados autorizados

- PASS_KERNEL_FINITE_SAMPLE_CALIBRATION
- PASS_HMM_CONFIRMATORY_CALIBRATION
- PASS_BOUNDED_PT_CONFIRMATORY_ADAPTER
- PASS_ANCILLA_CONFIRMATORY_ADAPTER
- FAIL_CALIBRATION_AT_ALPHA_OVER_7
- ABSTAIN_RESOURCE_INSUFFICIENT_FOR_CALIBRATION
- HOLD_PHYSICAL_PROTOGEOMETRY
