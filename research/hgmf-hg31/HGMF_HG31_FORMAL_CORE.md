# HGMF‑HG31 — Núcleo formal

## 1. Universal e-value conditional

Sea \(\mathcal F_T\) la información de training. Condicionalmente en \(\mathcal F_T\), \(g_T(h)\) es una densidad normalizada:

\[
\int g_T(h)\,dh=1.
\]

Para una nuisance family \(N_k\), suponga:

\[
U_k(h)\ge \sup_{\theta\in\Theta_k} f_{k,\theta}(h\mid \mathcal F_T).
\]

Para la unión:

\[
U_\cup(h)=\max_k U_k(h).
\]

Entonces:

\[
E(h)=g_T(h)/U_\cup(h).
\]

Si el true conditional distribution pertenece a cualquier \(N_{k^\star}\), para algún \(\theta^\star\),

\[
U_\cup(h)\ge U_{k^\star}(h)\ge f_{k^\star,\theta^\star}(h\mid\mathcal F_T).
\]

Por tanto:

\[
\mathbb E[E\mid\mathcal F_T]\le1.
\]

Así \(E\) es un e-value exacto finito-muestral.

## 2. p-value derivado

\[
p_E=\min(1,1/E).
\]

Entonces:

\[
\Pr(p_E\le\alpha)=\Pr(E\ge1/\alpha)\le\alpha.
\]

## 3. Numerical upper slack

Si \(\widetilde U_k\ge U_k\), entonces \(\widetilde E\le E\). Toda sobrecota numérica es conservadora. Una subcota es inadmisible.

## 4. Candidate density

El numerator puede ser cualquier predictive density normalizada y training-measurable. Su mala calidad reduce potencia, no validez.

## 5. Composite null irregular

La validez no usa Wilks ni limiting chi-square. El precio es disponer de likelihood evaluable, certified upper bound u otro e-value exacto.

## 6. Union envelope

No se combinan p-values de familias estimadas. Se testea directamente la unión nuisance mediante el máximo de sus likelihood upper bounds.

## 7. Frontera

Sin complexity caps o sin observation likelihood, una nuisance no puede entregar un upper bound informativo y el nodo X abstiene.
