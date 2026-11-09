# HGMF‑HG25 — Núcleo formal de ejecutabilidad

## 1. Grid magnético

Sea

\[
\mathcal G_M
=
\{100,150,200\}
\times
\{1,\ldots,8\}
\times
\{1,2,3\}.
\]

Entonces:

\[
|\mathcal G_M|=72.
\]

Cada unidad es un bloque reset–field–cycle dentro de una wave identificada.

## 2. Rectángulo causal

Para campos adyacentes \(f_0<f_1\), ciclos adyacentes \(c_0<c_1\) y wave \(w\), el contraste es:

\[
I_{f,c,w}
=
Y_{f_1,c_1,w}
-
Y_{f_1,c_0,w}
-
Y_{f_0,c_1,w}
+
Y_{f_0,c_0,w}.
\]

### Teorema de cuatro esquinas

Sin una de las cuatro esquinas, \(I_{f,c,w}\) no queda identificado no paramétricamente. Cualquier valor exige una hipótesis de modelo o imputación.

Por tanto:

```text
MISSING CORNER => ABSTAIN_RECTANGLE
```

## 3. Conteo

Con tres campos, ocho ciclos y tres waves:

\[
N_{\rm rectangles}
=
(3-1)(8-1)3
=
42.
\]

El diseño condicional posterior a UMI‑17+22 contiene por wave:

- 100 mT: ciclos 1–5;
- 150 mT: ciclos 1–5;
- 200 mT: ciclos 1–8.

Así identifica 8 rectángulos por wave y 24 en total. Los ciclos 6–8 en 100/150 mT añaden 6 rectángulos por wave, 18 en total.

## 4. Transferencia modal

Sea

\[
\mathcal L\phi_n=\lambda_n\phi_n,
\]

y sean:

\[
s_n=\langle s,\phi_n\rangle,
\qquad
i_n=\langle i,\phi_n\rangle.
\]

Para un kernel espectral:

\[
i_n=\gamma\kappa(\lambda_n;\vartheta)s_n.
\]

La identificabilidad local exige que el Jacobiano respecto de:

\[
(\gamma,\vartheta)
\]

tenga rango completo en los modos de training con \(s_n\neq0\).

Para una familia de dos parámetros totales, dos modos pueden interpolar exactamente pero no aportan falta de ajuste. Tres modos proporcionan el primer grado de libertad de contraste. Un holdout adicional permite falsación; dos holdouts aportan robustez.

```text
BARE MINIMUM = 3 training + 1 holdout
RECOMMENDED = 3 training + 2 holdout
```

## 5. Precisión simbólica

Si las cuatro estimaciones de celda poseen varianza independiente común \(\sigma^2\), entonces:

\[
\operatorname{Var}(I_w)=4\sigma^2.
\]

Promediando \(W\) waves:

\[
\operatorname{SE}(\bar I)=\frac{2\sigma}{\sqrt W}.
\]

Para \(\alpha=0.05\) bilateral y potencia 0.8:

\[
\operatorname{MDE}
=
(z_{0.975}+z_{0.8})
\frac{2\sigma}{\sqrt W}.
\]

Esto produce aproximadamente:

- \(3.962\sigma\) con dos waves de training;
- \(3.235\sigma\) con tres waves.

La cantidad \(\sigma\) es la incertidumbre de estimación del componente de loop, no la dispersión punto a punto sin procesar.

## 6. Holdout

Wave 3 permanece completamente retenida. El análisis debe congelar en waves 1–2:

- Hodge/QGT;
- source construction;
- whitening;
- kernel family;
- parameters;
- gamma;
- node tolerance;
- nuisance class.

Wave 3 sólo puede ser puntuada. No puede recalibrar.

## 7. Frontera

El gate cierra:

- ejecutabilidad;
- conteo;
- rank conditions;
- no-imputation;
- scoring contract.

No cierra:

- causal effects;
- kernel selection;
- nodal transport;
- physical attribution.
