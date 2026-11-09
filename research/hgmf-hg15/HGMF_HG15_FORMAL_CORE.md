# HGMF‑HG15 — Núcleo formal

## 1. Sistema–reloj

Sea

\[
\mathcal H_{CS}=\mathcal H_C\otimes\mathcal H_S,
\]

con constraint global

\[
(H_C+H_S+H_{CS}^{\rm int})|\Psi\rangle=0.
\]

Para un POVM covariante de reloj \(E_\tau\), el estado condicional es

\[
\rho_S(\tau)=
\frac{\operatorname{Tr}_C[(E_\tau\otimes I)|\Psi\rangle\langle\Psi|]}
{\operatorname{Tr}[(E_\tau\otimes I)|\Psi\rangle\langle\Psi|]}.
\]

En el límite ideal no interactuante recupera la evolución de Schrödinger.

## 2. Gauge del reloj

Una re-fase de la base temporal

\[
|\tau\rangle\mapsto e^{i\alpha(\tau)}|\tau\rangle
\]

transforma el vector condicional por la fase opuesta y no cambia su rayo ni su matriz densidad.

## 3. Teorema de equivalencia reloj–fase

Si

\[
i\hbar\partial_\tau\psi=[a(\tau)H_0+b(\tau)I]\psi,
\qquad a(\tau)>0,
\]

defina

\[
s(\tau)=\int_0^\tau a(u)du,
\qquad
\widetilde\psi(s)=
\exp\left[\frac{i}{\hbar}\int_0^\tau b(u)du\right]\psi(\tau).
\]

Entonces

\[
i\hbar\partial_s\widetilde\psi=H_0\widetilde\psi.
\]

Por tanto, un shift identidad y una distorsión uniforme de velocidad de reloj no constituyen una corrección física distintiva.

## 4. Smearing temporal escalar

Para una medida de tiempo relacional \(\mu\):

\[
\mathcal T_\mu(\rho)=\int U_\tau\rho U_\tau^\dagger d\mu(\tau).
\]

En la base de energía:

\[
(\mathcal T_\mu\rho)_{mn}
=\Gamma((E_m-E_n)/\hbar)\rho_{mn},
\]

\[
\Gamma(\omega)=\int e^{-i\omega\tau}d\mu(\tau).
\]

Para energías equiespaciadas, la matriz de coherencias es Toeplitz, positiva semidefinida y de diagonal uno.

## 5. Teorema de no-identificabilidad monogap

Para todo \(c=re^{-i\phi}\) con \(|c|\le1\),

\[
\mu_c=
\frac{1+r}{2}\delta_{\phi/\omega}
+
\frac{1-r}{2}\delta_{(\phi+\pi)/\omega}
\]

satisface

\[
\int e^{-i\omega\tau}d\mu_c(\tau)=c.
\]

Una única medición compleja de fase/visibilidad nunca excluye un modelo de smearing temporal escalar.

## 6. Tribunal multigap

Una única \(\mu\) impone compatibilidad simultánea entre todos los gaps. En un espectro equiespaciado:

\[
C_{m,m+1}=C_{n,n+1}
\]

para todos los gaps adyacentes iguales, y las matrices Toeplitz finitas deben ser positivas semidefinidas.

La violación falsifica smearing temporal escalar, pero no la mecánica cuántica estándar: una matriz de dephasing PSD no Toeplitz puede provenir de un entorno ordinario.

## 7. No-go de dilatación

Toda dinámica CPTP reducida admite una dilatación unitaria estándar sobre un espacio ampliado. Por tanto, fase, visibilidad, decoherencia o memoria observadas en el sistema reducido no identifican HGMF sin restricciones adicionales sobre la clase de entornos y relojes admisibles.

## 8. Condición de distintividad HGMF

Una corrección protogeométrica físicamente atribuible debe proporcionar simultáneamente:

1. funcional no nulo derivado;
2. covariancia de gauge y de quantum reference frame;
3. escala dimensional;
4. ley de dependencia en gap, reloj, historia o contexto;
5. patrón no absorbible por clock calibration, Hamiltonian renormalization o la clase ambiental congelada;
6. falsador experimental preregistrado.

HG15 no deriva todavía ese funcional.