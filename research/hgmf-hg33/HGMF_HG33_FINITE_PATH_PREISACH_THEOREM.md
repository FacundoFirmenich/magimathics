# HGMF‑HG33 — Teorema de Preisach sobre trayectoria finita

Sea una trayectoria finita

\[
x=(x_1,\ldots,x_T).
\]

Un relay elemental \(\gamma_{\alpha,\beta}\), con \(\alpha\ge\beta\), actualiza su estado sólo mediante las comparaciones

\[
x_t\ge\alpha,
\qquad
x_t\le\beta.
\]

## 1. Partición finita del espacio de thresholds

Sea

\[
U=\{u_1<\cdots<u_m\}
\]

el conjunto de inputs distintos observados.

Para cualquier threshold real, su efecto sobre todas las comparaciones con \(x_t\) depende únicamente de:

- si coincide exactamente con algún \(u_i\);
- en cuál intervalo abierto entre valores consecutivos cae;
- o si cae por debajo/encima de todos los valores observados.

Por tanto existen representantes finitos

\[
R=
\{u_i\}
\cup
\left\{\frac{u_i+u_{i+1}}{2}\right\}
\cup
\{u_1-\Delta,u_m+\Delta\},
\]

con \(\Delta>0\), tales que todo threshold real es comparison-equivalent a algún elemento de \(R\) sobre la trayectoria.

Para todo \((\alpha,\beta)\) real existe un par representativo \((a,b)\in R^2\), \(a\ge b\), que induce el mismo patrón de updates sobre \(x\). Incluyendo ambos estados iniciales \(\pm1\), el conjunto de patrones de relay distintos es finito y puede enumerarse exactamente.

## 2. Preisach / independent-domain family

Una salida scalar Preisach sobre esa trayectoria puede escribirse como

\[
\mu
=
c_0\mathbf 1
+
r(x)
+
\int_{\alpha\ge\beta}
w(\alpha,\beta)
\gamma_{\alpha,\beta}[x]\,
d\alpha\,d\beta,
\]

con \(w\ge0\) en el modelo físico clásico y \(r(x)\) un reversible term preregistrado.

Sobre una trayectoria finita, la integral es una combinación no negativa de los finitísimos patrones enumerados.

## 3. Outer relaxation

Sea \(X_R\) la matriz formada por:

- intercept;
- reversible basis preregistrada;
- todos los patrones relay distintos.

Entonces:

\[
\mathcal M_{\rm Preisach}
\subseteq
\operatorname{col}(X_R).
\]

Para una Gaussian likelihood con covariance positiva definida \(\Sigma\):

\[
\boxed{
\sup_{\mu\in\mathcal M_{\rm Preisach}}
L(y;\mu,\Sigma)
\le
\sup_{\beta\in\mathbb R^p}
L(y;X_R\beta,\Sigma).
}
\]

El lado derecho es un profile GLS exacto.

## 4. Saturation diagnostic

Si

\[
\operatorname{rank}(X_R)=T,
\]

el outer relaxation satura la trayectoria y no puede proporcionar potencia confirmatoria:

\[
\boxed{\texttt{ABSTAIN_PREISACH_OUTER_BOUND_SATURATED}.}
\]

Esto no invalida el bound; informa que es demasiado laxo.

## 5. Alcance

El theorem cubre scalar relay/Preisach shells y el core binario de independent-domain theory sobre la trayectoria observada.

No cubre:

- pore-network interactions;
- percolation;
- micromagnetics;
- un physical domain-wall model específico;
- dynamic rate effects no representables como scalar rate-independent Preisach.
