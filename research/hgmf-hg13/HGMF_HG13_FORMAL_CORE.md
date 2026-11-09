# HGMF‑HG13 — Núcleo formal

## 1. Conexión canónica

En la esfera unitaria \(S(\mathcal H)\), para \(v\in T_\psi S(\mathcal H)\):

\[
\mathcal A_\psi(v)=-i\langle\psi,v\rangle.
\]

Satisface:

\[
\mathcal A_\psi(i\xi\psi)=\xi
\]

y es invariante bajo la acción unitaria.

### Teorema de unicidad

Para \(\dim_\mathbb C\mathcal H\ge2\), \(\mathcal A\) es la única conexión principal \(U(1)\) normalizada en la dirección vertical e invariante bajo todo \(U(\mathcal H)\).

Toda otra conexión es afín:

\[
\mathcal A'=\mathcal A+\pi^*\beta.
\]

La invariancia unitaria completa fuerza \(\beta=0\).

## 2. Familia de generadores de una trayectoria proyectiva

Sea \(\psi_h(t)\) el lift horizontal y

\[
\eta=(I-|\psi_h\rangle\langle\psi_h|)\dot\psi_h=\dot\psi_h.
\]

El generador mínimo es

\[
H_{\min}=i\hbar\left(|\eta\rangle\langle\psi_h|-|\psi_h\rangle\langle\eta|\right).
\]

Todo Hamiltoniano que produce la misma trayectoria de rayos tiene la forma

\[
H=H_{\min}+h(t)P+K(t),
\]

con

\[
P=|\psi_h\rangle\langle\psi_h|,
\quad h(t)\in\mathbb R,
\quad K=K^\dagger,
\quad K\psi_h=0.
\]

Además:

\[
\|H\|_{\rm HS}^2=2\hbar^2\|\eta\|^2+h^2+\|K\|_{\rm HS}^2.
\]

Por tanto, \(H_{\min}\) es el único minimizador Hilbert–Schmidt.

## 3. Velocidad y pitch

\[
v_{\rm FS}=\|\eta\|=\frac{\Delta H}{\hbar}.
\]

Para el lift físico de Schrödinger:

\[
\nu_{\mathcal A}=-\frac{\langle H\rangle}{\hbar}.
\]

Así:

\[
\kappa=\frac{\nu_{\mathcal A}}{v_{\rm FS}}=-\frac{\langle H\rangle}{\Delta H}.
\]

Si \(H\) es independiente del tiempo, \(\langle H\rangle\) y \(\Delta H\) son constantes y \(\kappa\) es constante.

Pero:

\[
H\mapsto H+cI
\]

no cambia la trayectoria proyectiva y transforma:

\[
\kappa\mapsto\kappa-\frac{c}{\Delta H}.
\]

El pitch no es un invariante intrínseco del rayo sin referencia externa de fase o de cero de energía.

## 4. Invariante no geodésico

\[
\mathcal E_{\rm proj}[\gamma]=L_{\rm FS}[\gamma]-d_{\rm FS}(\gamma(0),\gamma(T))\ge0.
\]

Es gauge-invariante, independiente de trivialización y reparametrización. Mide exceso respecto de la geodésica, no helicoidalidad única.

## 5. Holonomía y topología

En \(\mathbb{CP}^{n-1}\), loops contractibles pueden tener holonomía no trivial por curvatura. La monodromía topológica requiere defectos, degeneraciones removidas o topología adicional del espacio de parámetros.

## 6. Frontera de spin

La fase geométrica y el bundle de Hopf no bastan. Spin físico requiere representación de rotaciones espaciales, generadores, Casimir, acoplamiento y dinámica contrastable.
