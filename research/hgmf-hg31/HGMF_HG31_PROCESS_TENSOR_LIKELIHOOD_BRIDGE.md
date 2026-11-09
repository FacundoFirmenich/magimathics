# HGMF‑HG31 — Puente de likelihood para process tensors y ancillas

## 1. Requisito de observación

Un process tensor no entra al nodo X sólo por producir una dinámica. Debe especificar una probabilidad o densidad sobre **el objeto realmente observado**.

Dos rutas son admisibles.

### Ruta RAW

Si el experimento conserva outcomes de medición discretos/control sequences, el process tensor Choi \(\Upsilon\) induce probabilidades lineales:

\[
p_i(\Upsilon)=\operatorname{Tr}(M_i\Upsilon).
\]

El log-likelihood es:

\[
\ell(\Upsilon)=\sum_i n_i\log p_i(\Upsilon).
\]

El conjunto completo de process tensors físicos para un número fijo de pasos/dimensiones está definido por:

- \(\Upsilon\succeq0\);
- constraints afines de causalidad.

Maximizar una log-likelihood cóncava sobre este conjunto convexo produce un profile likelihood del outer null.

### Ruta SUMMARY

Si sólo se usan componentes extraídos \((A,B,C,K,E,Q,Z)\), debe existir un observation model preregistrado:

\[
Y\mid\Upsilon \sim q(\cdot\mid m(\Upsilon),\Sigma(\Upsilon)).
\]

No puede inventarse después del holdout.

## 2. Outer relaxation

Sea \(\mathcal P_{\chi,L}\) una clase PT-MPO bounded por bond dimension/memory y \(\mathcal P_{\rm phys}\) la clase convexa completa de process tensors físicos con los mismos slots.

Como:

\[
\mathcal P_{\chi,L}\subseteq\mathcal P_{\rm phys},
\]

se tiene:

\[
\sup_{\Upsilon\in\mathcal P_{\chi,L}}L(\Upsilon)
\le
\sup_{\Upsilon\in\mathcal P_{\rm phys}}L(\Upsilon).
\]

El profile sobre \(\mathcal P_{\rm phys}\) puede usarse como likelihood upper bound conservador.

## 3. Power boundary

La relajación completa puede ser demasiado flexible y volver \(E_X\) pequeño. Eso reduce potencia pero no invalida el test.

## 4. Estado actual

El repositorio todavía no posee un observation-likelihood bridge de process tensor a los componentes/receipts HG25–HG30.

Por tanto:

ABSTAIN_PROCESS_TENSOR_OBSERVATION_LIKELIHOOD.

## 5. Ancilla/control geometry

La misma regla aplica. Un latent/control engine debe inducir una densidad sobre los observables realmente puntuados y entregar profile likelihood o upper bound certificado.
