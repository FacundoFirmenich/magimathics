# HGMF‑HG32 — Presupuesto de potencia por celda

Wave 3 contiene \(n=24\) celdas por carrier.

El threshold es:

\[
\log E_X\ge\log140=4.941642422609304.
\]

Sin slack, la ventaja media necesaria es:

\[
\boxed{
4.941642422609304/24
=
0.205901767608721
\text{ nats/celda}.
}
\]

Equivale a aproximadamente:

\[
0.297053459039374
\text{ bits/celda}.
\]

Si el upper bound introduce slack total \(\delta\):

\[
\bar d_{\rm req}
=
\frac{\log140+\delta}{24}.
\]

| slack \(\delta\) | nats/celda requeridos | bits/celda |
|---:|---:|---:|
| 0 | 0.205902 | 0.297053 |
| 1 | 0.247568 | 0.357166 |
| 2 | 0.289235 | 0.417278 |
| 5 | 0.414235 | 0.597615 |
| 10 | 0.622568 | 0.898176 |

## Generalización

Para una ventaja media esperada \(d\) nats/celda:

\[
n_{\min}
=
\left\lceil
\frac{\log140+\delta}{d}
\right\rceil.
\]

Esto permite comparar el costo del conservadurismo del null con el tamaño real del holdout antes de ejecutar el experimento.
