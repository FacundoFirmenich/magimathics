# HGMF‑HG29 — Núcleo formal

## 1. Nivel local

\[
\alpha=0.05,
\qquad
\alpha_j=\alpha/7=1/140.
\]

Todos los carrier-level p-values se construyen sobre wave 3 y se replican mediante

\[
p^{rep}=\max(p^{mag},p^{ads}).
\]

## 2. Nodo C: patrón causal preregistrado

Sea \(y_j^c\in\mathbb R^{24}\) el vector de estimates holdout de un componente y carrier. Sea \(D\in\mathbb R^{14\times24}\) la matriz fija de rectángulos adyacentes.

\[
I_j^c=Dy_j^c,
\qquad
\Sigma_{I,j}^c=D\Sigma_{y,j}^cD^\top.
\]

Training fija un template no nulo \(w_{C,j}^c\). El test es

\[
Z_C=
\frac{w_C^\top I}{\sqrt{w_C^\top\Sigma_Iw_C}}.
\]

Bajo el null de proyección causal no positiva y normalidad/asintoticidad certificada:

\[
p_C=\bar\Phi(Z_C).
\]

La claim es específica al patrón preregistrado. No es un omnibus de “cualquier interacción”.

## 3. Nodo M: alignment modal

Sea \(m\) el vector holdout de coefficients modales y \(r\) la predicción congelada de training.

\[
Z_M=
\frac{r^\top\Sigma_M^{-1}m}
{\sqrt{r^\top\Sigma_M^{-1}r}}.
\]

\[
p_M=\bar\Phi(Z_M).
\]

Se exige covariance válida, blocks preseleccionados y un mínimo de dos blocks holdout con source support. El residual modal se reporta como diagnóstico, no se convierte en confirmación por simple no-rechazo.

## 4. Nodo N: bracket nodal

Training congela flancos \(\ell=1,\dots,L\), cada uno con signo esperado \(s_\ell\in\{-1,+1\}\).

\[
Z_\ell=s_\ell\hat\mu_\ell/\hat\sigma_\ell,
\qquad
p_\ell=\bar\Phi(Z_\ell).
\]

Para la claim conjuntiva:

\[
\boxed{p_N=\max_\ell p_\ell.}
\]

Si falta un flanco, la salida es ABSTAIN_NODAL_BRACKET_INCOMPLETE.

## 5. Nodo X: exclusión de nuisance congelada

Sea

\[
H_X=\bigcup_{k=1}^{K}H_{N_k}.
\]

Cada familia nuisance produce un p-value holdout calibrado \(p_{N_k}\) para su propio null.

Entonces

\[
\boxed{p_X=\max_k p_{N_k}}
\]

es válido para \(H_X\), porque bajo cualquier distribución del null existe al menos un \(k^\star\) verdadero y

\[
\Pr(p_X\le t)
\le
\Pr(p_{N_{k^\star}}\le t)
\le t.
\]

Toda familia declarada debe estar presente. Una familia sin p-value válido produce ABSTAIN_NUISANCE_ENVELOPE_INCOMPLETE.

## 6. Nodo O: efecto de orden

Para ocho pares independientes y dirección precongelada, sea \(K_+\) el número de diferencias en la dirección esperada, excluyendo ties.

\[
p_O=\Pr[\operatorname{Bin}(n,1/2)\ge K_+].
\]

Con \(n=8\), sólo \(K_+=8\) alcanza el umbral local:

\[
p_O=1/256<1/140.
\]

Si ties reducen \(n<8\), el nodo no puede superar el umbral y queda confirmatoriamente no rechazado.

## 7. Fixed sequence

Por componente:

\[
C\to M\to N\to X\to O.
\]

Un nodo posterior no se interpreta si el anterior no pasa. O es opcional: la ausencia del módulo de orden no revoca un X ya confirmado.

## 8. Claim ceiling

El nodo X autoriza sólo:

CANDIDATE_OUTSIDE_FROZEN_STANDARD_NUISANCE_ENVELOPE.

No autoriza exclusión de toda mecánica cuántica estándar ni physical protogeometry.
