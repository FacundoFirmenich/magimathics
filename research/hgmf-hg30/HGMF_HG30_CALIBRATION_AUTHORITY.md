# HGMF‑HG30 — Autoridad de calibración

## Lattice

### EXACT_FINITE_SAMPLE

Existe distribución nula exacta para el statistic después del training especificado.

Confirmatory authority: YES.

### EXACT_CONDITIONAL_RANDOMIZATION

Bajo el diseño/randomization congelado, el rank/randomization p-value es super-uniform condicionalmente.

Confirmatory authority: YES.

### ASYMPTOTIC_THEOREM

Existe un teorema de calibración en un régimen explícito.

Confirmatory authority: CONDITIONAL. Requiere auditoría de regularity y régimen muestral.

### EMPIRICAL_CALIBRATION_ONLY

Uniformidad aproximada observada en benchmark/simulation.

Confirmatory authority: NO por sí sola.

### UNPROVEN

El adapter produce scores/predictions, pero no existe garantía de p-value.

Confirmatory authority: NO.

## Regla no compensatoria

Un buen RMSE no eleva un adapter de UNPROVEN a autoridad confirmatoria.

Un posterior predictive check convencional tampoco adquiere autoridad por producir un número entre 0 y 1; el double use del dato puede producir p-values no uniformes. Split/holdout predictive checks resuelven parte de este problema, pero su autoridad depende del teorema aplicable y del régimen muestral.

## Monte Carlo

El Monte Carlo rank p-value es exacto para draws exchangeable con el observado bajo una predictive distribution completamente especificada. No convierte automáticamente un plug-in predictor composite en un test exacto de toda su family.
