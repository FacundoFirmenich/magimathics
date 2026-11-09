# HGMF‑HG30 — Covariance receipts, nuisance adapters y dry-run end-to-end

**Fecha:** 9 de noviembre de 2026

## Veredicto

PASS_COVARIANCE_RECEIPT_PROFILE  
PASS_PREDICTIVE_RECEIPT_PROFILE  
PASS_EXACT_LINEAR_DRIFT_CONTROL_ADAPTER  
PASS_STANDARD_KERNEL_ADAPTER_IMPLEMENTATION  
PASS_FINITE_HIDDEN_STATE_ADAPTER_IMPLEMENTATION  
PASS_EXTERNAL_BOUNDED_PROCESS_TENSOR_ADAPTER_CONTRACT  
PASS_EXTERNAL_ANCILLA_CONTROL_GEOMETRY_ADAPTER_CONTRACT  
PASS_CALIBRATION_AUTHORITY_LATTICE  
PASS_FAIL_CLOSED_END_TO_END_DRY_RUN  

FAIL_ALL_NUISANCE_FAMILIES_CONFIRMATORY_READY  
FAIL_UNBOUNDED_PROCESS_TENSOR_ADMISSIBILITY  

ABSTAIN_BOUNDED_PROCESS_TENSOR_CALIBRATION  
ABSTAIN_HIDDEN_ANCILLA_CALIBRATION  
ABSTAIN_EMPIRICAL_ADJUDICATION  

HOLD_PHYSICAL_PROTOGEOMETRY

## Resultado rector

HG30 separa definitivamente:

\[
\text{adapter implementado}
\neq
\text{p-value confirmatoriamente autorizado}.
\]

Cada predictor nuisance debe emitir un predictive receipt con training ancestry, complexity bound, predictive object, holdout cell keys, discrepancy congelada, calibration authority y code/environment hashes.

El nodo X sólo acepta adapters con autoridad confirmatoria explícita.

## Covariance receipts

Las covariances de celdas y bloques modales dejan de ser objetos implícitos. Cada receipt declara labels, units, covariance artifact, rank, PSD tolerance, extraction parents, transform ancestry y regularization.

No se autoriza reemplazar una covariance desconocida por diagonalidad.

## Adapters

1. Drift/control: modelo lineal Gaussiano training-only con predictive F-test finito-muestral bajo sus supuestos.
2. Alternative kernels: identity/Green/screened/fractional/heat con fit training-only y predictive covariance propagada.
3. Finite hidden state: Gaussian HMM bounded-K con EM training-only y predictive sampler; implementado, pero su calibration family-level no se concede automáticamente.
4. Bounded process tensor: adapter de integración para predictions emitidas por un engine PT-MPO con memory/bond caps preregistrados. No se finge un solver PT dentro de HG30.
5. Hidden ancilla/control geometry: adapter de integración para predictive receipts de un engine bounded/regularized externo.

## Dry-run

El dry-run sólo usa fixtures algebraicos y estados vacíos para comprobar PSD/rank, receipt closure, calibration gates, missing-adapter abstention y machine adjudicator fail-closed.

No genera outcomes experimentales y no produce evidencia.

## Resultado actual del nodo X

drift_control: IMPLEMENTED / EXACT-CONDITIONAL  
alternative_standard_kernels: IMPLEMENTED / CALIBRATION-CONDITIONAL  
finite_hidden_state: IMPLEMENTED / CALIBRATION-HOLD  
bounded_process_tensor: INTERFACE IMPLEMENTED / ENGINE+CALIBRATION HOLD  
hidden_ancilla_control_geometry: INTERFACE IMPLEMENTED / ENGINE+CALIBRATION HOLD  

X CONFIRMATORY READY = FALSE

## Próxima frontera

HGMF‑HG31 — Finite-sample calibration de nuisance compleja, complexity caps y simulación bajo null auditada.
