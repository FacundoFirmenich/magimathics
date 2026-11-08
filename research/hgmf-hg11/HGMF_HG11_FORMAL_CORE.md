# HGMF‑HG11 — Núcleo formal

## Teorema 1 — Identidad de peso uno

Para un proyector ortogonal \(P\) y \(\psi\neq0\):

\[
1-q_\psi(P)
=
\frac{\|(I-P)\psi\|^2}{\|\psi\|^2}.
\]

Luego:

\[
q_\psi(P)=1
\iff
P\psi=\psi.
\]

## Corolario 1 — Distancia

Para \(\widehat\psi=\psi/\|\psi\|\):

\[
\operatorname{dist}(\widehat\psi,\operatorname{Ran}P)
=
\sqrt{1-q_\psi(P)}.
\]

Así \(q_n\to1\) equivale a aproximación métrica, mientras \(q=1\) equivale a pertenencia exacta.

## Teorema 2 — Atomicidad

Si \(P\) tiene rango uno, \(q_\psi(P)=1\) determina un único rayo. Si \(\operatorname{rank}P>1\), el conjunto de rayos compatibles es \(\mathbb P(\operatorname{Ran}P)\), generalmente no singleton.

## Definición — Carrier probabilístico degenerado

Una medida \(\mu\) es `sin probabilística` respecto de la jurisdicción declarada cuando

\[
|\operatorname{supp}\mu|=1.
\]

Equivale a una medida delta en el espacio atómico declarado.

## Definición — Singlete transicional tipado

Dados

\[
\Pi_\lambda:\mathcal P_{RV}\to\Omega_\lambda,
\qquad
\Delta(y)=\delta_y,
\]

un par \((r_*,\mu_*)\) es singlete transicional si

\[
\Delta(\Pi_\lambda(r_*))=\mu_*=\delta_{y_*},
\]

y \(y_*\) es un átomo del álgebra de eventos.

## Teorema 3 — No-go de actuality

Las condiciones anteriores implican certeza representacional del evento, pero no la existencia de un token de medición ni la ocurrencia efectiva de un outcome.

## Teorema 4 — Endpoint insuficiente para Born

Sean \(f,g:[0,1]\to[0,1]\) continuas con

\[
f(0)=g(0)=0,
\qquad
f(1)=g(1)=1.
\]

Pueden diferir arbitrariamente en \((0,1)\). Por tanto, el comportamiento en el borde no selecciona la ley interior.
