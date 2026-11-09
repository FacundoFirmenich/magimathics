# HGMF‑HG30 — Covariance receipts, nuisance adapters y dry-run end-to-end

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

## 1. Resultado científico

HG30 cierra la genealogía de incertidumbre y la interfaz predictiva de la nuisance envelope. El punto crítico es que implementación, capacidad predictiva y calibración confirmatoria son propiedades distintas.

\[
\boxed{\text{implemented}\not\Rightarrow\text{confirmatory valid}}
\]

## 2. Covariance como evidencia

Cada vector de estimates lleva una covariance receipt con labels, units, matrix artifact, rank, PSD tolerance, regularization y parents. Para cualquier transformación lineal:

\[
\Sigma' = A\Sigma A^\top.
\]

Una covariance singular es admisible sólo dentro de su support. Una covariance desconocida no puede reemplazarse por diagonalidad implícita.

## 3. Drift/control

El modelo Gaussian linear frozen en training produce un predictive F-statistic exacto:

\[
F=
\frac{e_H^\top V_H^{-1}e_H}{m s_T^2}
\sim F_{m,\nu}.
\]

Éste es el único adapter HG30 que recibe autoridad EXACT_FINITE_SAMPLE en este corte.

## 4. Kernel

El adapter espectral implementa identity, Green, screened, fractional y heat. El fit training-only propaga parameter covariance por Jacobian al holdout.

La implementación pasa, pero su p-value Gaussian nonlinear se clasifica:

ASYMPTOTIC_THEOREM_PENDING_REGIME_AUDIT.

No recibe aún autoridad a \(\alpha/7\).

## 5. Hidden state

Se implementa Gaussian HMM bounded-K con Baum–Welch/EM y predictive sampler. El Monte Carlo check prueba el frozen predictor. No convierte automáticamente ese predictor en un family-level exact test del null hidden-state composite.

Estado:

FROZEN_PREDICTIVE_ONLY_NOT_FAMILY_CONFIRMATORY.

## 6. Process tensor

No se introduce un surrogate y no se afirma haber escrito tomography PT-MPO. El adapter exige a un engine real:

- memory steps;
- local dimension;
- bond-dimension cap;
- compression/tomography algorithm;
- training-only ancestry;
- wave-3 predictive object.

La bond dimension representa una cota explícita de la memoria efectiva en la representación MPO. Sin cap, la nuisance deja de ser una hipótesis falsable útil.

## 7. Ancilla/control geometry

Se adopta la misma política: interface real y fail-closed, sin fingir un solver. Latent dimension, map family y regularization deben estar congelados.

## 8. Calibration authority

Jerarquía:

1. EXACT_FINITE_SAMPLE;
2. EXACT_CONDITIONAL_RANDOMIZATION;
3. ASYMPTOTIC_THEOREM;
4. EMPIRICAL_CALIBRATION_ONLY;
5. UNPROVEN.

Sólo los niveles autorizados por seal entran al nodo X.

## 9. Resolución Monte Carlo

Para

\[
p=(1+b)/(B+1)
\]

y

\[
\alpha_j=1/140,
\]

la mera posibilidad discreta de rechazar exige:

\[
\boxed{B\ge139.}
\]

No es una garantía de calibración.

## 10. Dry-run

El dry-run no contiene outcomes físicos, reales ni sintéticos. Sólo valida identidades matriciales, schemas, caps, imports y failure-closed behavior.

Resultado esperado:

ABSTAIN_NUISANCE_ENVELOPE_INCOMPLETE.

## 11. Estado de Paper C

La nuisance envelope existe ya como arquitectura ejecutable, pero no como test confirmatorio completo. Drift/control está listo; kernels, HMM, PT y ancilla necesitan calibration authority adicional.

## 12. Próxima frontera

HGMF‑HG31 — Finite-sample calibration de nuisance compleja, complexity caps y null simulation auditada.
