# HGMF‑HG32 — HMM: noise floor, bounded likelihood y no-go de potencia saturada

## 1. Measurement-noise floor

Suponga que para cada observación \(t\), toda emission covariance observable satisface

\[
C_{z,t}\succeq R_t\succ0,
\]

donde \(R_t\) proviene del instrumento/extraction covariance receipt.

Para cualquier mean \(\mu\):

\[
\mathcal N(x_t;\mu,C_{z,t})
\le
(2\pi)^{-d/2}
\det(R_t)^{-1/2}.
\]

Luego cualquier HMM, independientemente de su matriz de transición, satisface:

\[
\boxed{
L_{\rm HMM}(x_{1:T})
\le
\prod_t
(2\pi)^{-d/2}\det(R_t)^{-1/2}.
}
\]

Así un variance floor físicamente certificado elimina la degeneración \(\sigma\to0\) sin inventar mean boxes.

## 2. Saturation no-go

Si la family permite:

- \(K\ge T\);
- arbitrary state means;
- deterministic transitions;
- emission covariance igual al noise floor;

puede asignar un estado distinto a cada observación y alcanzar el envelope puntual.

Para cualquier candidate density sometida al mismo measurement-noise floor:

\[
g_T(x_{1:T})
\le
U_{\rm sat}(x_{1:T}),
\]

por lo que:

\[
\boxed{E_X\le1.}
\]

No puede alcanzarse \(E_X=140\).

## 3. Consecuencia

El noise floor basta para **validez**, pero no para **potencia**.

Hace falta una restricción de complejidad temporal —por ejemplo \(K_{\max}<T\), transition structure, smoothness o physical state count— para que hidden-state sea una nuisance falsable con potencia.

Ese cap no puede elegirse mirando wave 3.
