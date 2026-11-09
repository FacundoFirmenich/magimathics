# HGMF‑HG28 — Subdiseño sparse de orden causal

## 1. Unidades

En cada contexto seleccionado se adquieren, desde el mismo reset root:

\[
V\to H,
\qquad
H\to V.
\]

Baseline y singles proceden del grid base cuando son admisibles.

## 2. Training

Por carrier:

- 3 contextos pareados;
- 6 adquisiciones ordered-joint.

Se usan para dirección, estabilidad y selección, no para el p-value final.

Si las tres diferencias de training no permiten congelar dirección según la regla preregistrada: ABSTAIN_DIRECTION_UNSTABLE.

## 3. Holdout

Por carrier:

- 8 contextos pareados de wave 3;
- 16 adquisiciones ordered-joint.

La selección de contexts usa únicamente geometry/source/modal features de training y se sella antes de abrir wave 3.

## 4. Test exacto

Con dirección precongelada, se usa un sign-flip/randomization test one-sided sobre los ocho pares.

Con presupuesto local

\[
\alpha_j=1/140,
\]

el menor p-value posible con \(n\) pares es \(2^{-n}\).

\[
2^{-7}=1/128>1/140,
\]

\[
2^{-8}=1/256<1/140.
\]

Por tanto:

\[
\boxed{n_{holdout}^{min}=8.}
\]

## 5. Coste

Por carrier:

\[
(3+8)\times2=22.
\]

Dos carriers:

\[
\boxed{B_{order}=44.}
\]

Presupuesto máximo sparse:

\[
\boxed{144+44=188.}
\]

Ahorro frente a reverse-grid completo:

\[
\boxed{288-188=100.}
\]

## 6. Trigger

El holdout order module sólo se ejecuta si, tras training:

- existe al menos una cadena causal no futile;
- la dirección es congelable;
- el mapa carrier/orientación es admisible;
- el protocolo ordenado es físicamente realizable.

La decisión queda receipted antes de wave 3.
