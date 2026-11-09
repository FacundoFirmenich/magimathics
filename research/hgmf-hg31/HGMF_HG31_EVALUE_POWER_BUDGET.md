# HGMF‑HG31 — Presupuesto de potencia del e-value universal

Para un carrier:

\[
\log E_X
=
\log g_T(H)
-
\log U_\cup(H).
\]

El umbral es:

\[
\boxed{
\log E_X
\ge
\log 140
=
4.941642422609304.
}
\]

## Slack de upper bound

Sea \(L_\cup^\star\) el verdadero profile likelihood máximo del union null y suponga:

\[
\log U_\cup
=
\log L_\cup^\star+\delta,
\qquad
\delta\ge0.
\]

Entonces:

\[
\log E_{\rm certified}
=
\log E_{\rm ideal}-\delta.
\]

Cada unidad de slack en log-likelihood consume exactamente una unidad de evidence growth.

Por tanto, para confirmar:

\[
\log g_T-\log L_\cup^\star
\ge
\log140+\delta.
\]

## Kernel

El Lipschitz-grid certifier declara explícitamente su mathematical slack. Puede reducirse aumentando grid density, sin afectar type-I error.

## HMM

El emission-envelope bound ignora transition consistency y puede tener un slack mucho mayor. Su utilidad debe auditarse antes de adquisición real.

## Process tensor outer relaxation

El profile likelihood sobre la clase convexa completa de process tensors físicos puede ser muy superior al profile del bounded PT-MPO null. La diferencia es slack de power, no error de calibración.

## Replicación

La claim X requiere el threshold en ambos carriers. No se suman log-e-values para rescatar un carrier débil porque HG28 exige replicación 2/2.
