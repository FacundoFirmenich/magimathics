# HGMF‑HG31 — Universal e-values, likelihood upper bounds y calibración finito-muestral

**Fecha:** 9 de noviembre de 2026

## Veredicto

PASS_FINITE_SAMPLE_UNIVERSAL_EVALUE_THEOREM  
PASS_UNION_NUISANCE_EVALUE  
PASS_KERNEL_CERTIFIED_LIKELIHOOD_BOUND_METHOD  
PASS_BOUNDED_HMM_LIKELIHOOD_UPPER_BOUND  
PASS_LIKELIHOOD_BOUND_RECEIPT_PROFILE  
PASS_NUMERICAL_SLACK_CONSERVATIVITY  

FAIL_UNBOUNDED_NUISANCE_CONFIRMATORY_ADMISSIBILITY  
FAIL_PLUG_IN_PREDICTIVE_PVALUE_AS_DEFAULT  

ABSTAIN_KERNEL_PARAMETER_CAPS_UNSEALED  
ABSTAIN_HMM_EMISSION_CAPS_UNSEALED  
ABSTAIN_PROCESS_TENSOR_OBSERVATION_LIKELIHOOD  
ABSTAIN_ANCILLA_OBSERVATION_LIKELIHOOD  
ABSTAIN_EMPIRICAL_ADJUDICATION  

HOLD_PHYSICAL_PROTOGEOMETRY

## Resultado rector

Sea \(T\) el training y \(H\) el holdout. Training congela una densidad predictiva alternativa normalizada

\[
g_T(H).
\]

Para cada nuisance family \(N_k\), sea \(U_k(H)\) una cota certificada:

\[
U_k(H)\ge \sup_{\theta\in\Theta_k} f_{k,\theta}(H\mid T).
\]

Para la unión nuisance:

\[
U_\cup(H)=\max_k U_k(H).
\]

Defina:

\[
\boxed{
E_X(H)=\frac{g_T(H)}{U_\cup(H)}.
}
\]

Bajo cualquier miembro verdadero de la nuisance envelope:

\[
\mathbb E[E_X\mid T]\le1.
\]

Por Markov:

\[
\Pr(E_X\ge1/\alpha_j)\le\alpha_j.
\]

Con

\[
\alpha_j=1/140,
\]

el threshold confirmatorio es

\[
\boxed{E_X\ge140.}
\]

Y el p-value compatible con HG29 es:

\[
\boxed{
p_X=\min(1,E_X^{-1}).
}
\]

Esto da validez finito-muestral sin regularidad asintótica, siempre que la densidad candidata esté normalizada y las cotas nuisance sean realmente upper bounds.

## Estado por nuisance

- drift/control: exacto ya desde HG30;
- standard kernels: upper-bound method implementado, pero faltan parameter caps sellados;
- bounded HMM: analytic emission-envelope upper bound implementado, pero faltan emission/variance caps sellados;
- process tensor: falta likelihood observacional o un certified likelihood upper-bound oracle;
- ancilla/control geometry: misma frontera.

## Próxima frontera

HGMF‑HG32 — Complexity-cap selection, likelihood bridge for process tensors/ancillas y universal-evalue power audit.
