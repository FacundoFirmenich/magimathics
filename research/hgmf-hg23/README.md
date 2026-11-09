# HGMF‑HG23 — Potenciales relacionales triaxiales, normalización de fuente y protocolo nodal empírico

**Veredicto:** `PASS_OPERATIONAL_POTENTIAL_DERIVATION_CONDITIONAL / PASS_HODGE_EXTRACTION / PASS_DIRICHLET_AND_VECTOR_NORMALIZATION / PASS_DIAGONAL_TRANSVERSALITY / FAIL_CAUSAL_INTERACTION_IDENTIFICATION / FAIL_PHYSICAL_GAMMA / FAIL_KERNEL_PHYSICAL_SELECTION / ABSTAIN_EMPIRICAL_NODAL_EXECUTION`.

## Core result

Given preregistered interventional response one-forms,

\[
\omega_V=da_V+\delta\beta_V+h_V,
\qquad
\omega_H=db_H+\delta\beta_H+h_H,
\]

the operational potentials are the unique mean-zero Hodge exact projections:

\[
\mathcal L a_V=d^\dagger\omega_V,
\qquad
\mathcal L b_H=d^\dagger\omega_H.
\]

The diagonal geometric source is

\[
\boxed{s_D=*(da_V\wedge db_H)}.
\]

It measures oriented transversality of the potential gradients. It does not, by itself, identify causal interaction.

## Normalization

Scalar Dirichlet normalization:

\[
\widehat s_D=\frac{s_D}{\sqrt{E_VE_H}},
\qquad E_V=\int|da_V|^2dA,
\quad E_H=\int|db_H|^2dA,
\]

preserves zero flux and removes shifts and positive affine unit choices.

For multicomponent potentials, Dirichlet-Gram whitening yields a matrix source

\[
\mathbf S_D=*(d\widehat{\mathbf a}_V\wedge d\widehat{\mathbf b}_H^\top).
\]

Under invertible channel reparameterizations it changes only by left/right orthogonal rotations. Singular values, rank and Frobenius norm are canonical. No vector-state mean is authorized.

The local orientation index

\[
\chi_D=\frac{s_D}{|da_V||db_H|}
\]

is invariant under separate monotone reparameterizations on the regular set, but is not used as a curvature source because local normalization need not preserve exactness or zero flux.

## Causal no-go

For

\[
a_V(v,h)=v,
\quad b_H(v,h)=h,
\quad m(v,h)=v^2+\sin h,
\]

one has

\[
s_D=1,
\qquad
m_{11}-m_{10}-m_{01}+m_{00}=0.
\]

Thus a nonzero diagonal source can coexist with exact absence of causal interaction.

## Exact witness

A contaminated torus response field recovers its exact Hodge potentials with maximum errors

- vertical: `8.88e-16`;
- horizontal: `6.66e-16`;
- source: `1.34e-14`.

The source flux is `2.66e-17`; affine-normalization error is `1.21e-15`; monotone orientation-index error is `2.35e-13`; whitened source singular values are invariant to `9.12e-16`.

## Kernel tribunal

On one retained meridian, the same source produces distinct nodes:

| Kernel | Nodes |
|---|---|
| Identity | `2.819842`, `5.961435` |
| Green | `2.446854`, `5.588447` |
| Screened | `2.651635`, `5.793228` |
| Fractional | `2.656543`, `5.798136` |
| Heat | `2.772101`, `5.913694` |

Nodes therefore falsify the frozen potential–source–kernel triple. Green remains physically conditional on the minimum Dirichlet action.

## Empirical protocol

For the magnetic preset `-`, UMI‑17+22 already contains the 100/150 mT cycles 1–5 and 200 mT cycles 1–8 in three waves. Completing a `3 fields × 8 cycles × 3 waves` grid requires 18 additional loops. The combined magnetic programme becomes 156 loops, with a 72-loop HG23 grid.

A homologous adsorption carrier requires `3 controls × 8 reversal depths × 3 waves = 72 runs`. It has not been executed.

```text
EMPIRICAL PROTOCOL = COMPLETE
EMPIRICAL NODAL EXECUTION = ABSTAIN
```

## Portfolio

- Paper A: unchanged; HG23 is an optional extension separate from UMI‑17.
- Paper B: antiaggregative normalization and potential/QGT transport boundary added.
- Paper C: operational potentials and normalized diagonal source pass conditionally; causal diagonal interaction, response amplitude, physical kernel and empirical validation remain open.

## Next gate

`HGMF‑HG24 — Interacción causal diagonal, normalización de respuesta y ejecución dual-carrier`.
