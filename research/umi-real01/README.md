# MGM‑UMI‑REAL‑01 — Repressilator publication gate

## Identification of a real relational unit
### The repressilator core under substitution, rewiring, ablation and cross-substrate transport

**Date:** 2026-11-06  
**Authority:** `MAGIMATICS / EXPERIMENTAL PUBLICATION GATE`  
**Candidate:** `UMI‑R1 — closed three-node cyclic repression unit`  
**Verdict:** `PASS_REAL_RELATIONAL_UMI_CORE / HOLD_MULTIFRACTAL_QUALIFIER`

## 1. Precise candidate

The candidate is **not** the set {LacI, TetR, cI} and is not any one molecule. It is the closed signed relation

\[
\mathcal U_R=(V,E^-,\Theta),
\]

where

\[
V=\{\mathrm{LacI},\mathrm{TetR},\mathrm{cI}\},
\]

\[
E^-=\{\mathrm{cI}\dashv\mathrm{LacI},
\mathrm{LacI}\dashv\mathrm{TetR},
\mathrm{TetR}\dashv\mathrm{cI}\},
\]

and \(\Theta\) is the admissible gain/delay/decay jurisdiction that supports the oscillatory attractor.

The inclusion of \(\Theta\) is mandatory: topology alone does not determine the dynamical repertoire of a small gene circuit. The proposed UMI carrier is therefore a **signed cyclic relation under a declared dynamical jurisdiction**, not a bare graph motif.

## 2. Semantic signature

\[
\Sigma_R=\{
\text{self-sustained limit cycle},
\text{cyclic phase order},
\text{approximately one-third phase separation},
\text{recoverable oscillator identity},
\text{transportable signed-relation class}
\}.
\]

In the curated BioModels regime, the mean protein period is 125.345 min. The three mean phase lags are

\[
(41.800, 41.773, 41.773)\ \mathrm{min},
\]

equivalent to

\[
(0.333478, 0.333261, 0.333261)
\]

of one period. No individual repressor contains the phase cycle.

## 3. Substitution test

The cyclic transformation

\[
X\to Y,\qquad Y\to Z,\qquad Z\to X
\]

with the same permutation applied to the state preserves the numerical trajectory:

\[
\varepsilon_{\rm rel}=1.508\times10^{-18},
\qquad
\varepsilon_{\rm max}=1.137\times10^{-13}.
\]

The invariant is the relation, not the label.

Published biological variants and an electronic implementation also sustain the oscillatory class when the cyclic inhibitory relation and an admissible nonlinear/delay regime are preserved. Period and waveform need not be numerically identical.

**Result:** `PASS_SUBSTITUTION_T2`.

## 4. Relational ablation

Every single-edge deletion in the curated model destroys sustained oscillation and converges to a fixed point. Experimentally, IPTG deactivates LacI and eliminates the \(x\to y\) inhibitory edge; the altered topology admits a stable fixed point. Removing the perturbation permits the oscillator to resume.

**Result:** `PASS_ABLATION`.

## 5. Rewiring

Two cardinality-preserving counterfactuals were tested:

1. replacing \(\mathrm{LacI}\dashv\mathrm{TetR}\) by a duplicate \(\mathrm{cI}\dashv\mathrm{TetR}\) input;
2. changing \(\mathrm{LacI}\dashv\mathrm{TetR}\) from repression to activation.

Both lose the oscillatory signature. Under the frozen parameter regime, only the fully inhibitory three-cycle oscillates among the eight possible sign assignments.

**Result:** `PASS_REWIRING_SENSITIVITY`.

## 6. Component reduction

A one-node self-repressor and a two-node mutual-repression reduction, instantiated with the same kinetic family, converge to fixed points. Three nodes and three critical relations are inclusion-minimal for the declared signature in this jurisdiction.

**Result:** `PASS_MINIMALITY_WITHIN_JURISDICTION`.

## 7. Cross-substrate transport

An electronic analog preserving the cyclic inhibitory architecture physically reproduced key repressilator dynamics.

- `T1`: signed topology preserved — PASS;
- `T2`: qualitative dynamical function preserved — PASS;
- `T3`: quantitative conjugacy of all observables — HOLD.

**Result:** `PASS_CROSS_SUBSTRATE_TRANSPORT_T2`.

## 8. Relation-first adjudication

| Test | Result | Strongest evidence |
|---|---|---|
| substitution | PASS | exact cyclic conjugacy; biological/electronic implementation changes |
| rewiring | PASS sensitivity | same cardinality, changed relation, lost signature |
| ablation | PASS necessity | all model edges; physical IPTG edge deletion |
| transport | PASS T2 | independent electronic physical analog |

\[
\text{same components + altered relation}
\Rightarrow
\text{different system-level form},
\]

whereas

\[
\text{different components/substrate + preserved relation class}
\Rightarrow
\text{preserved dynamical form class}.
\]

That is the operational content of “the unit gains its unitary value in the relation”.

## 9. Exact promotion boundary

### Promoted

\[
\boxed{
\text{a real minimal invariant relational unit candidate}
}
\]

within cyclic synthetic oscillators.

### Held

The word **multifractal** is not yet empirically earned. The evidence is multiscale—molecular, cellular, lineage/population and electronic—but no multifractal spectrum or non-affine scaling law has been demonstrated.

`PASS_REAL_UMI_CORE / HOLD_MULTIFRACTAL_QUALIFIER`.

## 10. Established antecedents

The carrier is already known as a network motif, cyclic negative-feedback ring, minimal synthetic gene oscillator and dynamical module under appropriate kinetics. Magimatics does not claim discovery of the motif. The proposed contribution is the operational UMI identification protocol combining substitution, rewiring, ablation, transport and semantic-signature preservation.

## 11. Methods

The computational tribunal uses the curated deterministic repressilator model BIOMD0000000012. It has six states—three mRNAs and three proteins—with the cyclic repression relations \(P_Z\dashv X\), \(P_X\dashv Y\), and \(P_Y\dashv Z\).

- solver: SciPy LSODA 1.17.0;
- interval: 0–2000 min;
- reporting step: 0.1 min;
- relative tolerance: \(10^{-10}\);
- absolute tolerance: \(10^{-12}\);
- transient discarded: first 500 min.

A run is classified oscillatory when at least five peaks remain after transient removal and the 95th–5th percentile amplitude is at least 5% of the baseline amplitude. The rule is frozen across interventions.

## 12. Evidence classes

- `P1`: direct physical experiment;
- `P2`: physical intervention series;
- `P3`: independent physical substrate;
- `M1`: curated mechanistic model;
- `T1`: exact graph/symmetry result.

Model counterfactuals are never presented as wet-lab data.

## 13. Publication gate

**Working title:** *Minimal Invariant Relational Units: Substitution, Rewiring, Ablation and Cross-Substrate Transport in a Synthetic Gene Oscillator*

```text
CONCEPT_AND_METHODS = STRONG
REAL_WORKED_CASE = PASS
COMPUTATIONAL_REPRODUCIBILITY = PASS
PHYSICAL_EVIDENCE_SYNTHESIS = PASS
MULTIFRACTAL_QUALIFIER = HOLD
SECOND_REAL_DOMAIN = REQUIRED_FOR_GENERALITY
PREPRINT_STATUS = STRONG_DRAFT_NOT_FINAL
```

Before arXiv:

1. apply the frozen tribunal to a second non-oscillator real system;
2. compare explicitly with network motifs, dynamical modules, causal states, bisimulation and minimal realization;
3. obtain systems-biology and general-systems specialist review;
4. close novelty/genealogy language;
5. avoid universal or ontological promotion.

Suggested primary category: `q-bio.MN`, with possible cross-list to `nlin.AO` or `physics.bio-ph`, subject to final emphasis and moderation.

## 14. Next gate — MGM‑UMI‑REAL‑02

The second candidate must be from a different function class, preferably robust perfect adaptation, biochemical memory/switching, control engineering or error correction. The same frozen tests must be applied without modifying their logic after inspecting the system.

Possible outputs:

- `PASS_CROSS_DOMAIN_UMI`;
- `PASS_DOMAIN_LOCAL_ONLY`;
- `NO_UNIQUE_MINIMAL_CARRIER`;
- `FAIL_RELATIONAL_IDENTITY`.
