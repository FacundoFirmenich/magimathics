# HGMF‑HG24 — Interacción causal diagonal, normalización de respuesta y selección modal del kernel

**Veredicto:** `PASS_CAUSAL_DIAGONAL_ESTIMAND / PASS_GEOMETRIC_CAUSAL_INDEPENDENCE / PASS_ORDER_DECOMPOSITION / PASS_MODAL_KERNEL_IDENTIFIABILITY_CONDITIONAL / FAIL_UNIVERSAL_PHYSICAL_GAMMA / FAIL_UNCONDITIONAL_KERNEL_SELECTION / ABSTAIN_DUAL_CARRIER_EXECUTION`.

## Core result

The geometric source

\[
s_D=*(da_V\wedge db_H)
\]

and the causal joint-intervention contrast

\[
I_{VH}=m_{11}-m_{10}-m_{01}+m_{00}
\]

are logically independent. Exact witnesses realize geometric-only, causal-only, both and neither.

For ordered continuous interventions, the average of the two rectangles converges to the symmetrized mixed derivative, while their difference converges to the intervention commutator. This separates interaction from history/order effects.

## Response amplitude

For frozen predictor \(r_K=\mathcal K\widehat s_D\):

\[
\widehat\gamma=\frac{\langle r_K,\iota_D\rangle_W}{\langle r_K,r_K\rangle_W}.
\]

This is a unique training estimator, but outcome rescaling multiplies \(\widehat\gamma\). Alignment and relative residual remain invariant. Geometry therefore does not select a universal physical gamma.

## Kernel tribunal

Modal gains

\[
g_n=\frac{\langle\iota_D,\phi_n\rangle}{\langle\widehat s_D,\phi_n\rangle}
\]

are fit only on training modes and tested on held-out modes. An exact screened-kernel witness with \(\gamma=2.4\), \(m^2=3\) is recovered with zero held-out error. General physical kernel selection remains conditional because candidate families intersect.

## Execution

- magnetic extension required: `18 loops`;
- complete magnetic grid: `72 loops`;
- homologous adsorption design: `72 runs`;
- neither execution is currently complete.

```text
PASS_DUAL_CARRIER_PROTOCOL
ABSTAIN_DUAL_CARRIER_EXECUTION
```

## Portfolio

- Paper A: unchanged; HG24 extension optional.
- Paper B: causal–geometric boundary added.
- Paper C: causal/modal tribunal passes formally; gamma, kernel, execution and attribution remain open.

## Next gate

`HGMF‑HG25 — Espectroscopia causal modal y ejecución nodal dual-carrier`.
