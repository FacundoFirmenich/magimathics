# HGMF‑UMI‑20 — Empirical Cross‑Carrier Semantic Spectrum

**Date:** 8 November 2026  
**Authority:** `EMPIRICAL / POSITIVE-q / FINITE-SIZE / SURROGATE`  
**Verdict:** `PASS_MULTISCALE_ONLY / FAIL_TRANSPORT_INVARIANCE / FAIL_SURROGATE_TRIBUNAL`

## 0. Portfolio status

- **Paper A:** unchanged; experiment-ready after UMI‑17 and awaiting the 99-loop bridge.
- **Paper B:** formal characterization survives, but this corpus does not supply a transport-stable empirical multifractal UMI.
- **Paper C:** receives no empirical support from this gate; no bridge to HGMF or the geometric constants is authorized.

## 1. Frozen empirical measure

The corpus is the archived UMI‑11 whole-loop held-out residual ledger: four magnetic loops and four adsorption runs.

Let \(e_0\) be memoryless loss, \(e_H\) branch loss, \(e_D\) the predeclared domain history shell (`fading` for magnetism; `RPM` for adsorption), and \(e_V\) the grain-context selector.

\[
H=e_0-\min(e_0,e_H),
\]
\[
D=\min(e_0,e_H)-\min(e_0,e_H,e_D),
\]
\[
V=\min(e_0,e_H,e_D)-\min(e_0,e_H,e_D,e_V),
\]
\[
T=H+D+V.
\]

All masses are nonnegative and derived from held-out predictions fixed before spectrum inspection.

## 2. Scales and moments

Nested sequence covers:

\[
2,4,8,16,32\ \text{boxes}.
\]

Positive moments only:

\[
q\in\{0.5,1,2,3,4\}.
\]

No negative-q claim is made.

## 3. Multiscale result

For the total witness \(T\):

| Carrier | Candidate runs | Full surrogate passes | Width range |
|---|---:|---:|---:|
| Adsorption | 4/4 | 0/4 | 0.133–0.380 |
| Magnetism | 0/4 | 0/4 | −0.016–0.018 |

Adsorption is genuinely nonuniform across retained scales, but its apparent spectral width does not survive the block-preserving surrogate tribunal. Magnetism is effectively monofractal at this resolution.

Therefore:

```text
PASS_MULTISCALE_ONLY
FAIL_EMPIRICAL_SCALE-RICH_MULTIFRACTALITY
```

## 4. Surrogate tribunal

Three stochastic nulls were frozen:

1. full shuffle;
2. regime-preserving shuffle within direction/reversal/phase strata;
3. contiguous-block permutation.

A deterministic finite-strata surrogate replaced values by within-stratum medians.

The strongest adsorption candidates exceed full and regime shuffles, but not the block surrogate. Thus the curvature can be explained by organized finite blocks/regimes rather than an asymptotic multifractal cascade.

## 5. Transport failure

The total generalized-dimension vectors \((D_{0.5},D_1,D_2,D_3,D_4)\) were compared using an exact 4-versus-4 permutation test.

\[
E_{\mathrm{obs}}=0.505312869527,
\qquad
p_{\mathrm{exact}}=0.014285714286=1/70.
\]

The observed domain separation is the largest among the 70 labelings.

\[
\boxed{\texttt{FAIL\_TRANSPORT\_INVARIANCE}}
\]

The shared history UMI does not entail a shared multifractal spectrum.

## 6. Operational triaxial coupling

A rank-copula diagnostic compared the joint H/D/V cloud with independently permuted axes.

- Magnetism: 4/4 loops pass.
- Adsorption: 1/4 runs pass.

Thus:

```text
PASS_OPERATIONAL_TRIAXIAL_COUPLING_MAGNETIC
FAIL_CROSS-CARRIER_TRIAXIAL_TRANSPORT
```

This is a measure-dependent operational result, not a unique decomposition of semantic synergy.

## 7. Scientific closure

The formal UMI‑19 class remains valid. What fails is its empirical universalization to this particular pair of carriers and this particular frozen measure.

The correct result is not “no multifractality anywhere.” It is:

1. adsorption contains multiscale organization;
2. magnetism does not share its spectrum on the retained scales;
3. block organization explains the adsorption width;
4. the triaxial coupling diagnostic is carrier-specific;
5. no empirical UMI dual is promoted.

## 8. Gate adjudication

```text
PASS_FOUR_PLUS_SCALES
PASS_POSITIVE-q_DISCIPLINE
PASS_ADSORPTION_MULTISCALE
PASS_OPERATIONAL_MAGNETIC_COUPLING

FAIL_SURROGATE_TRIBUNAL
FAIL_TRANSPORT_INVARIANCE
FAIL_CROSS-CARRIER_TRIAXIALITY
FAIL_EMPIRICAL_DUAL_UMI_CURRENT_CORPUS
```
