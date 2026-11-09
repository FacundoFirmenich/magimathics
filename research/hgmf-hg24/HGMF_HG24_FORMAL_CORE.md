# HGMF‑HG24 — Núcleo formal

## 1. Estimando causal rectangular

Sea

\[
m(v,h)=\mathbb E[Y\mid do(V=v,H=h)].
\]

Para niveles preregistrados:

\[
I_{VH}=m(v_1,h_1)-m(v_1,h_0)-m(v_0,h_1)+m(v_0,h_0).
\]

## 2. Intervenciones como flujos

Sean \(X_V,X_H\) campos de intervención con flujos \(\Phi_V^\epsilon,\Phi_H^\eta\). Defina los rectángulos ordenados:

\[
I_{H\circ V}^{\epsilon,\eta}
=m\circ\Phi_H^\eta\circ\Phi_V^\epsilon
-m\circ\Phi_V^\epsilon
-m\circ\Phi_H^\eta+m,
\]

\[
I_{V\circ H}^{\epsilon,\eta}
=m\circ\Phi_V^\epsilon\circ\Phi_H^\eta
-m\circ\Phi_V^\epsilon
-m\circ\Phi_H^\eta+m.
\]

En el límite local:

\[
I_{sym}/(\epsilon\eta)\to\tfrac12(X_HX_V+X_VX_H)m,
\]

\[
I_{ord}/(\epsilon\eta)\to\tfrac12[X_H,X_V]m.
\]

## 3. Independencia geométrico-causal

La fuente \(s_D=*(da_V\wedge db_H)\) y el contraste causal son lógicamente independientes. Existen realizaciones exactas de las cuatro combinaciones \((s_D,I_{VH})\in\{0,1\}^2\).

## 4. Calibración de amplitud

Para predictor \(r_K=\mathcal K\widehat s_D\) y campo causal \(\iota_D\), con producto interno \(W\):

\[
\widehat\gamma_W
=\frac{\langle r_K,\iota_D\rangle_W}{\langle r_K,r_K\rangle_W}.
\]

Es el minimizador único de \(\|\iota_D-\gamma r_K\|_W^2\) si \(r_K\neq0\).

Bajo \(Y'=aY+b\):

\[
\widehat\gamma'_W=a\widehat\gamma_W.
\]

Por tanto, la geometría no selecciona una amplitud física universal.

## 5. Invariantes de ajuste

\[
\rho_{DI}
=\frac{\langle r_K,\iota_D\rangle_W}{\|r_K\|_W\|\iota_D\|_W},
\]

\[
\epsilon_{rel}
=\frac{\|\iota_D-\widehat\gamma r_K\|_W}{\|\iota_D\|_W}.
\]

Ambos son invariantes ante escalamiento positivo del outcome.

## 6. Transferencia modal

Si \(\mathcal K=\kappa(\mathcal L)\), entonces

\[
i_n=\gamma\kappa(\lambda_n)s_n.
\]

Los ratios entre modos eliminan \(\gamma\):

\[
\frac{i_n/s_n}{i_m/s_m}
=\frac{\kappa(\lambda_n)}{\kappa(\lambda_m)}.
\]

La identificación requiere modos distintos, soporte no nulo, una geometría congelada y holdout. Las intersecciones entre familias impiden una selección incondicional.

## 7. Contrato causal-nodal

`COLOCATED_TRIAXIAL_INTERACTION` exige interacción do-interventional, fuente no degenerada, kernel congelado, amplitud training-only, nodos/signos retenidos, transporte transcarrier y fracaso de la nuisance estándar.

## 8. Frontera

HG24 formaliza el estimando, la calibración y el diseño modal. No ejecuta los 18 loops ni los 72 runs y no deriva una gamma universal, un kernel físico o un origen HGMF.
