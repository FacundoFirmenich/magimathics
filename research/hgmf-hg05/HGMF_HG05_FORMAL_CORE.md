# HGMF‑HG05 — Núcleo formal

## Teorema A — familia multiplicativa

Sea `w:C->[0,infinity)` continua, fase-invariante, `w(1)=1`, `w(0)=0`, no idénticamente nula y multiplicativa. Defina

\[
g(t)=\log w(e^t).
\]

Entonces `g(t+s)=g(t)+g(s)`. Por continuidad, `g(t)=pt`, y continuidad en cero exige `p>0`. Así

\[
w(z)=|z|^p.
\]

## Teorema B — mixer equilibrado

Sea

\[
B=aH,\qquad H=\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
\]

Como `H^2=2I`, la condición `B^2=e^{i\chi}I` implica `|a|=1/sqrt(2)`.

Si

\[
W_p(z_1,z_2)=|z_1|^p+|z_2|^p
\]

y `W_p(Be_1)=W_p(e_1)`, entonces

\[
2^{1-p/2}=1,
\]

por tanto `p=2`.

## Teorema C — paralelogramo

En `l^p_2`, para `e_1,e_2`, el defecto de paralelogramo es

\[
\Delta_p=2^{1+2/p}-4.
\]

Para `p>0`, `Delta_p=0` si y sólo si `p=2`.

## Teorema D — tensorialidad no selecciona p

Para cualquier `p>0`:

\[
W_p(\psi\otimes\phi)=W_p(\psi)W_p(\phi).
\]

Por tanto, composición multiplicativa no distingue el exponente.

## Frontera

Estos teoremas seleccionan un peso cuadrático dentro de una familia de geometrías de amplitud. No interpretan ese peso como probabilidad.
