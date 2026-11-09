# HGMF‑HG29 — Tests confirmatorios ejecutables y exclusión de nuisance congelada

**Fecha:** 9 de noviembre de 2026  
**Autoridad:** EXECUTABLE TESTS / HOLDOUT ONLY / STRICT REPLICATION / FINITE NUISANCE ENVELOPE

## Veredicto

PASS_EXECUTABLE_CAUSAL_TEST  
PASS_EXECUTABLE_MODAL_ALIGNMENT_TEST  
PASS_EXECUTABLE_NODAL_BRACKET_IUT  
PASS_FROZEN_NUISANCE_ENVELOPE_IUT  
PASS_EXECUTABLE_ORDER_SIGN_TEST  
PASS_MACHINE_ADJUDICATOR_CORE  
PASS_STRICT_REPLICATION_INTEGRATION  

FAIL_UNRESTRICTED_STANDARD_PHYSICS_EXCLUSION  
FAIL_NUISANCE_EXCLUSION_BY_BEST_FIT_ONLY  

ABSTAIN_NUISANCE_FAMILY_ADAPTERS_UNTIL_IMPLEMENTED  
ABSTAIN_EMPIRICAL_ADJUDICATION  
HOLD_PHYSICAL_PROTOGEOMETRY

## Resultado rector

HG29 convierte los nodos C, M, N, X y O de HG28 en tests preespecificables.

### C — causal

Con vector holdout de celdas \(y\), matriz de rectángulos \(D\), covariance \(\Sigma_y\) y template training-only \(w_C\):

\[
I=Dy,\qquad \Sigma_I=D\Sigma_yD^\top,
\]

\[
Z_C=\frac{w_C^\top I}{\sqrt{w_C^\top\Sigma_Iw_C}},
\qquad
p_C=1-\Phi(Z_C).
\]

### M — modal

Para predicción modal training-frozen \(r_M\):

\[
Z_M=\frac{r_M^\top\Sigma_M^{-1}m}{\sqrt{r_M^\top\Sigma_M^{-1}r_M}},
\qquad
p_M=1-\Phi(Z_M).
\]

El nodo confirma alignment modal, no unicidad ontológica del kernel.

### N — nodal

Cada nodo se representa por dos flancos holdout con signos preregistrados. Para una conjunción de todos los flancos:

\[
p_N=\max_{\ell}p_\ell.
\]

No se necesita inventar una tolerancia de distancia nodal; la distancia queda como diagnóstico secundario.

### X — nuisance envelope

Para una envolvente congelada \(\mathcal N^\star=\{N_1,\dots,N_K\}\), cada familia entrega un p-value predictivo calibrado \(p_k\) en holdout. El null es la unión “al menos una familia nuisance explica los datos”:

\[
\boxed{p_X=\max_k p_k.}
\]

Sólo si **todas** las familias son rechazadas puede avanzar el nodo X.

La claim resultante es:

CANDIDATE_OUTSIDE_FROZEN_STANDARD_NUISANCE_ENVELOPE

y no “standard physics excluded”.

### O — orden

HG29 endurece el módulo HG28 y adopta un sign test exacto one-sided sobre ocho pares holdout, con dirección congelada en training. El mínimo p-value es \(1/256\), suficiente frente a \(\alpha_j=1/140\).

## Frontera

Una clase nuisance irrestricta que contenga una representación saturada de todos los distributions admisibles no puede ser falsada por esos mismos datos. Process tensors sin cota son suficientemente generales como para que “excluir toda dinámica estándar” no sea una claim autorizada.

## Próxima frontera

HGMF‑HG30 — Adaptadores nuisance físicos, covariance receipts y dry-run end-to-end sin datos empíricos.
