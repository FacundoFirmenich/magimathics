# HGMF‑HG12 — Núcleo formal

## Espacio de rayos y bundle de fase

Sea \(\mathcal H\) un espacio de Hilbert complejo, \(S(\mathcal H)\) su esfera unitaria y \(\mathbb P(\mathcal H)\) el espacio proyectivo. La proyección

\[
\pi:S(\mathcal H)\to\mathbb P(\mathcal H),\qquad \psi\mapsto[\psi],
\]

es un bundle principal \(U(1)\).

## Trayectoria transicional

Para un evento atómico \(P_*=|u\rangle\langle u|\):

\[
q(t)=|\langle u|\psi(t)\rangle|^2,
\qquad
d_{\rm FS}([\psi(t)],[u])=\arccos\sqrt{q(t)}.
\]

Así \(q(t)\to1\) fija la distancia radial al rayo, no la trayectoria completa.

## No-identificabilidad por q

En un qubit:

\[
\psi(t)=e^{i\chi(t)}\left[\cos\frac{\theta(t)}2|0\rangle+e^{i\phi(t)}\sin\frac{\theta(t)}2|1\rangle\right],
\]

\[
q(t)=\cos^2\frac{\theta(t)}2.
\]

\(q\) no contiene \(\phi\) ni \(\chi\). Por tanto, deja libres winding relativo, longitud proyectiva, holonomía y lift de fase.

## Conexión y drift vertical

Para una conexión \(A\) y coordenada de fibra \(\chi\):

\[
\nu_A(t)=\dot\chi(t)+A_{\gamma(t)}(\dot\gamma(t)).
\]

Bajo \(\chi'=\chi-\eta\), \(A'=A+d\eta\), se conserva \(\nu_{A'}=\nu_A\).

Dado un métrico de base, un lift \(A\)-helicoidal de pitch constante satisface:

\[
v_B(t)>0,\qquad \nu_A(t)=\kappa v_B(t),\qquad \kappa\neq0.
\]

La condición es gauge-invariante una vez fijada \(A\), pero no es independiente de la conexión ni de la dinámica.

## Holonomía

Para un loop cerrado \(\gamma\), el lift horizontal puede satisfacer:

\[
\widetilde\gamma(T)=\operatorname{Hol}_A(\gamma)\widetilde\gamma(0).
\]

Un loop cerrado en la base no obliga a un lift cerrado.

## Monodromía y winding

Un lift cerrado en una fibra \(U(1)\) posee winding entero. Una holonomía genérica es un elemento de \(U(1)\) y no tiene por qué ser un winding entero. Para trayectorias abiertas hacia el singlete, la monodromía requiere una clausura o un problema relativo adicional.

## Frontera de spin

La holonomía de fase no identifica spin. Spin físico requiere una representación de rotaciones espaciales, generadores, Casimir y dinámica.
