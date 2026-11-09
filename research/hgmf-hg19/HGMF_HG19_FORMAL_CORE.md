# HGMF‑HG19 — Núcleo formal

## 1. Familia unitaria y generadores locales

Sea

\[
|\psi(\lambda)\rangle=U(\lambda)|\psi_0\rangle
\]

y sean \(G_i\) generadores hermitianos tales que

\[
\partial_i|\psi\rangle=-\frac{i}{\hbar}G_i|\psi\rangle.
\]

Entonces

\[
Q_{ij}=\hbar^{-2}\langle\Delta G_i\Delta G_j\rangle.
\]

## 2. Métrica de acción

\[
h^{\rm act}_{ij}
:=\frac12\langle\{\Delta G_i,\Delta G_j\}\rangle
=\hbar^2g^Q_{ij}.
\]

Para los generadores horizontales mínimos:

\[
h^{\rm act}_{ij}
=\frac14\operatorname{Tr}\{G_i^{\min},G_j^{\min}\}.
\]

La métrica es invariante frente a

\[
G_i\mapsto G_i+c_iI+K_i,
\qquad K_i|\psi\rangle=0,
\]

mientras los costes completos del actuador no lo son.

## 3. Forma de área de acción

En dimensión contextual dos:

\[
dA_{\rm act}=\hbar^2dA_Q.
\]

Como

\[
\mathcal F=2\chi_QdA_Q,
\]

se sigue

\[
\mathcal F=\frac{2\chi_Q}{\hbar^2}dA_{\rm act}.
\]

## 4. Residual HGMF

Un término residual local proporcional al área de acción se escribiría

\[
\delta\mathcal F
=\lambda_{\rm HG}dA_{\rm act}
=\frac{c_{\rm HG}}{\hbar^2}dA_{\rm act}.
\]

El análisis dimensional fija la unidad \(\hbar^{-2}\), pero no fija \(c_{\rm HG}\).

## 5. Mixed states

La clase de métricas monotónicas de Petz no es singleton.

Si se adopta el principio de mínima acción de purificación:

\[
g_B(\dot\rho,\dot\rho)
=\inf_{\dot\Psi\mapsto\dot\rho}
g_{FS}(\dot\Psi,\dot\Psi),
\]

entonces

\[
h_B=\hbar^2g_B.
\]

La selección es condicional a ese principio adicional.

## 6. Transporte

- Isometrías constantes preservan \(Q\) y \(h^{\rm act}\).
- Canales accesibles contraen la geometría Bures.
- Una purificación dependiente del parámetro puede cambiar la geometría total sin cambiar el estado reducido.

Por tanto, el contrato transcarrier debe fijar el álgebra accesible y la reducción operacional.

## 7. Claim boundary

HG19 deriva una métrica de acción estándar y su unidad física. No deriva un acoplamiento HGMF no nulo, una nueva escala, una corrección experimental ni una exclusión de la geometría cuántica estándar.
