# HGMF‑HG27 — Teorema de adquisición rectangle-prefix óptima

En una wave, sea

\[
(\ell,m,r)\in\{0,\ldots,8\}^3
\]

el prefijo adquirido. El número de rectángulos causales completos es

\[
R(\ell,m,r)=[\min(\ell,m)-1]_++[\min(m,r)-1]_+.
\]

## Mínimo de loops

\[
N_{\min}(0)=0,\qquad N_{\min}(1)=4,
\]

y, para \(2\le q\le14\),

\[
\boxed{N_{\min}(q)=\left\lceil\frac{3q}{2}\right\rceil+3.}
\]

La prueba distribuye \(q=q_L+q_R\) entre los dos pares. Para \(q_L,q_R>0\), los prefijos mínimos son \(q_L+1,q_R+1,\max(q_L,q_R)+1\); el coste se minimiza balanceando ambos lados.

## Schedule simultáneamente óptimo

La secuencia acumulada HG27 es:

```text
0,0,0,1,1,2,2,3,4,4,5,6,6,7,8,8,9,10,10,11,12,12,13,14
```

Alcanza cada \(N_{\min}(q)\) en el primer instante posible.

## Pareto de switches

Para

\[
U=\sum_{t=1}^{24}R_t,
\]

la utilidad máxima exacta es \(148\). Una enumeración dinámica demuestra que se necesitan al menos 13 cambios de eje para alcanzarla. El schedule persistido alcanza \((U,S)=(148,13)\).
