# HGMF‑HG32 — Compactificación proyectiva de kernels

Considere:

\[
y\sim N(\gamma q_\eta,\Sigma),
\qquad
\gamma\in\mathbb R.
\]

Después de perfilar \(\gamma\), el likelihood depende sólo de la dirección proyectiva de \(q_\eta\).

## Screened

\[
q_m=\frac{s}{\lambda+m^2},
\qquad m^2\in[0,\infty).
\]

Al multiplicar por \(m^2\):

\[
m^2q_m
=
\frac{s}{1+\lambda/m^2}
\to s.
\]

Por tanto:

- \(m^2=0\): Green;
- \(m^2=\infty\): Identity.

La family perfilada tiene una extensión continua a \([0,\infty]\).

## Fractional

\[
q_\alpha=s\lambda^{-\alpha},
\qquad \alpha\in[0,\infty).
\]

Sea \(\lambda_0\) el menor eigenvalue con source support. Reescalando por \(\lambda_0^\alpha\):

\[
\lambda_0^\alpha q_\alpha
\to
P_{\lambda_0}s.
\]

## Heat

\[
q_\tau=s e^{-\tau\lambda},
\qquad \tau\in[0,\infty).
\]

Reescalando por \(e^{\tau\lambda_0}\):

\[
e^{\tau\lambda_0}q_\tau
\to
P_{\lambda_0}s.
\]

## Teorema

Las tres families, después de quotient por amplitud libre, poseen una closure compacta con endpoint \(\infty\). No requieren un cap físico finito para que el supremum de profile likelihood exista.

Así:

\[
\boxed{\text{KERNEL PARAMETER CAP REQUIRED FOR EXISTENCE}=FALSE.}
\]

Un parameter range finito puede seguir siendo una claim física más específica, pero no es necesario para la validez del union null más fuerte.
