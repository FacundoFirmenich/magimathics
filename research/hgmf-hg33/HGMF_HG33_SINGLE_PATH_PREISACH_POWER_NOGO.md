# HGMF‑HG33 — No-go de potencia para Preisach sobre un único loop simple

## 1. Monotone path

Sea una trayectoria estrictamente monótona:

\[
x_1<x_2<\cdots<x_T.
\]

Los relays con threshold de subida situado entre \(x_{k-1}\) y \(x_k\), iniciados en \(-1\), generan step functions independientes.

Con el intercept, esas step functions generan:

\[
\mathbb R^T.
\]

Por tanto:

\[
\operatorname{rank}(X_R)=T.
\]

## 2. Single-reversal path

Considere:

\[
x_1<\cdots<x_m>x_{m+1}>\cdots>x_T
\]

con cruces de threshold no degenerados.

Un relay puede activar en un crossing de subida \(i\) y desactivar en un crossing de bajada \(j\), generando un interval indicator que cruza el turning point.

La familia de esos interval indicators, junto con el intercept, genera diferencias independientes a ambos lados del turning point. En el caso genérico:

\[
\operatorname{rank}(X_R)=T.
\]

## 3. Consecuencia likelihood

El outer span alcanza cualquier vector observable:

\[
\operatorname{col}(X_R)=\mathbb R^T.
\]

Entonces el Gaussian profile likelihood del outer null alcanza el peak saturado:

\[
\sup_{\mu\in\operatorname{col}(X_R)}L(y;\mu,\Sigma)
=
L(y;y,\Sigma).
\]

Ninguna candidate density con la misma observation measure puede superar ese peak:

\[
E_X\le1.
\]

Así:

\[
\boxed{
\texttt{FAIL_SINGLE_PATH_PREISACH_CONFIRMATORY_POWER}.
}
\]

## 4. Qué sí puede falsar Preisach/IDT

Hace falta usar propiedades que acoplan múltiples historias o restringen la family:

- return-point memory;
- wiping-out;
- congruency;
- Everett-function consistency;
- shared density across multiple independently held-out histories;
- parametric/smooth density con complejidad physically justified.

Esto conecta directamente con UMI‑10: los whole-loop/RPM tribunals eran científicamente más informativos que un unconstrained single-path likelihood fit.
