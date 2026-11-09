# HGMF‑HG31 — Teorema universal de exclusión nuisance

Sea \(H\) el holdout y \(T\) el training. Sea \(g_T\) una densidad predictiva normalizada, fijada usando sólo \(T\). Sea

\[
\mathcal H_0=\bigcup_{k=1}^K\{f_{k,\theta}:\theta\in\Theta_k\}.
\]

Suponga que para cada family existe una función computable \(U_k\) tal que

\[
U_k(H)\ge\sup_{\theta\in\Theta_k}f_{k,\theta}(H\mid T).
\]

Defina:

\[
E_X=
\frac{g_T(H)}
{\max_k U_k(H)}.
\]

Entonces:

\[
\boxed{
\sup_{P\in\mathcal H_0}
\mathbb E_P[E_X\mid T]\le1.
}
\]

Consecuentemente:

\[
\boxed{
p_X=\min(1,E_X^{-1})
}
\]

es un p-value finito-muestral válido para la unión nuisance.

Con \(\alpha_j=1/140\), \(E_X\ge140\) es condición suficiente para rechazar la frozen nuisance envelope en un carrier. La replicación dual-carrier exige el threshold en ambos carriers.

La cota \(U_k\) puede provenir de maximización exacta, bound analítico, certified branch-and-bound, convex outer relaxation, interval arithmetic u otra cota demostrada.

Un optimizer que sólo devuelve un lower bound del maximum likelihood no es admisible.
