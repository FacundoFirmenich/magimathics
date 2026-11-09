# HGMF‑HG31 — Universal e-values, likelihood upper bounds y calibración finito-muestral

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

## 1. Salto metodológico

HG30 había separado implementación y calibration authority. HG31 elimina la necesidad de confiar por defecto en una distribución asintótica para nuisance irregulares.

Sea \(g_T(H)\) una density normalizada elegida con training y sea

\[
U_\cup(H)
=
\max_k
U_k(H)
\]

una cota certificada del máximo likelihood de todas las familias nuisance.

Entonces:

\[
E_X=g_T(H)/U_\cup(H)
\]

es un e-value finito-muestral bajo el union null.

## 2. Threshold

Con:

\[
\alpha_j=1/140,
\]

la regla carrier-level es:

\[
E_X\ge140.
\]

Equivalente:

\[
p_X=\min(1,1/E_X)\le1/140.
\]

La replicación sigue siendo 2/2 mediante el máximo de los p-values derivados.

## 3. Kernel

Para identity y Green, la amplitud \(\gamma\) se perfila exactamente.

Para screened, fractional y heat sobre intervals compactos sellados, HG31 deriva un upper bound de profile log-likelihood usando:

\[
|\ell_p'(\eta)|
\le
\|y\|_P^2
\frac{\|q'(\eta)\|_P}{\|q(\eta)\|_P}.
\]

Un grid con constant global \(L\) produce:

\[
\sup_\eta\ell_p(\eta)
\le
\max_{\eta_g}\ell_p(\eta_g)
+
Lh/2.
\]

La sobrecota es conservadora. Los ranges no están todavía sellados, por lo que el adapter no se activa confirmatoriamente.

## 4. HMM

Para un HMM bounded, cada emission density tiene un supremum analítico dentro de mean/variance boxes.

Si \(b_t\) es la máxima emission density posible en tiempo \(t\), entonces:

\[
L_{HMM}(x_{1:T})
=
\sum_{z_{1:T}}
P(z_{1:T})
\prod_tb_{z_t}(x_t)
\le
\prod_t b_t.
\]

La desigualdad vale para cualquier initial distribution y transition matrix porque las probabilities de paths suman uno.

Así se obtiene un upper bound exacto, aunque posiblemente conservador. Falta sellar mean/variance/state caps.

## 5. Process tensor

El process tensor Choi físico satisface positivity y affine causality constraints. Con raw quantum outcomes, probabilities son lineales en el Choi object y puede construirse un profile likelihood sobre un convex outer set.

Pero el programa actual puntúa components derivados \((A,B,C,K,E,Q,Z)\), y todavía no existe un observation-likelihood bridge desde \(\Upsilon\) hasta esos summaries.

Por tanto el bloqueo actual es semántico/observacional, no meramente computacional.

## 6. Ancilla

Misma frontera: dynamics sin observation density no entrega un null estadístico.

## 7. No-go de caps retrospectivos

Los complexity caps definen el null. No pueden elegirse mirando wave 3. Tampoco se permite construir caps training-derived sin una garantía de coverage que preserve el null original.

## 8. Estado científico

La arquitectura X gana ahora una ruta finito-muestral exacta para nuisance compuestos. No se ha excluido ninguna nuisance con datos reales; faltan caps y likelihood bridges.

## 9. Próxima frontera

HGMF‑HG32 — Complexity-cap selection, process-tensor/ancilla likelihood bridge y universal-evalue power audit.
