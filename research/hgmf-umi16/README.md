# HGMF‑UMI‑16 — Counterbalanced Identifiability and Discrete State Law

**Date:** 8 November 2026  
**Verdict:** `PASS_DISCRETE_ONLY / FAIL_FIELD_HISTORY_SEPARATION / HOLD_REPLICATION`

## Scientific closure

The public corpus does not instantiate the frozen `3×3×5×3` factorial, so UMI‑16 does not claim a universal continuous constitutive law. It closes four stricter results:

1. A positive reset reproducibly restores a fresh state on Device A within 5% for span, signed HEB magnitude and coercive width.
2. At fixed `200 mT`, one complete loop produces a replicated multicomponent fresh→trained transition: HEB and coercive-width envelopes are disjoint, while span envelopes overlap.
3. History shifts the operational resolved-manifestation threshold. Under the declared crossing/SNR gate:
   - fresh: `H* ∈ (125.362241, 150.262960] mT`;
   - trained: `H* ∈ (49.801438, 74.702157] mT`;
   - reduction: `50.660084–100.461522 mT`.
   This is an operational switching/manifestation threshold, not the programme's radius of non-circularity.
4. The current same-device support occupies 7 unique factorial cells and has design rank 7. A main-effects plus all two-way interaction model requires rank 29. The minimum rank-completing augmentation therefore needs 22 additional unique cells.

## Supported state law

\[
R_+\to F_+,\qquad R_-\to F_-,
\]

\[
F_+\xrightarrow{\text{one complete loop at 200 mT}}T,
\]

\[
K=K(H,Z),\qquad H_*^T<H_*^F.
\]

The continuous law

\[
\mathbf s_{t+1}=\mathcal U(\mathbf s_t,H_t,r_t)
\]

remains unidentified.

## Reset result

At equal field on Device B, PF+ and PF− differ in span by only `0.308%`, while HEB changes sign with a `2.796%` antisymmetry residual. The reset therefore restores an orientation subspace more robustly than the full vector state. Full-state reset restoration fails universally in the current corpus.

## Exact design deficit

- full factorial cells: `45`;
- pairwise-model rank: `29`;
- current unique cells/rank: `7/7`;
- minimum new unique cells for pairwise closure: `22`;
- saturated three-replicate bridge: `87` loop blocks;
- full three-replicate factorial: `135` loop blocks.

## Next gate

`HGMF‑UMI‑17 — Minimal Counterbalanced Bridge Experiment` freezes the 22-cell rank-completing augmentation before committing to the full factorial.

No novelty is claimed for established exchange-bias training phenomena. Independent derivation and internal closure remain valid programme outputs and reusable inputs for later research.
