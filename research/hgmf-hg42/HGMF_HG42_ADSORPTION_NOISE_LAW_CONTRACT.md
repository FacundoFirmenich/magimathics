# HGMF‑HG42 — Adsorption quotient noise-law contract

## Observation object

The confirmatory adsorption object is a joint reference/sample history ensemble with preserved raw acquisition ancestry.

Required components include:

- nonporous film reference;
- condensed-fluid reference;
- Vycor boundary history;
- preregistered scanning histories;
- reference/sample/reference interleaving;
- raw pressure, temperature and adsorption observations;
- mass and surface-area normalization;
- topology receipt;
- event and calibration hashes.

## Quotient chart

The seal must freeze:

- pressure-local labelled anchors;
- orientation;
- anchor-degeneracy threshold;
- pressure grid;
- interpolation operator A;
- quotient map and Jacobian G;
- optional training-only compression B;
- quotient measure ID.

## Covariance

The correct covariance is

Sigma_Q = G A Sigma_raw A^T G^T.

It must preserve:

- raw measurement covariance;
- shared interpolation nodes;
- pressure covariance;
- reference/sample drift;
- cross-history covariance;
- anchor covariance.

Interpolation nodes are not independent replicates.

## Replicate-rank consequence

HG40 contained 242 quotient coordinates but only one correlated historical history ensemble.

An unrestricted full covariance on that vector would need at least 243 independent history vectors after fitting a common mean. This route is not practically or historically available.

Authorized alternatives are:

1. a training-only frozen compression to lower dimension;
2. a structured positive-definite covariance family with a finite-supremum certificate;
3. sufficiently many genuine independent replicated histories.

## Model-specific nulls

The denominator must cover, where physically admitted:

- independent-domain/Preisach shell;
- network/percolation;
- pore blocking;
- cavitation;
- reference and topology uncertainty.

## Candidate density

The numerator must be a proper training-only density on exactly the same quotient measure as the denominator.

## Current status

ABSTAIN_REAL_ADSORPTION_REPLICATES_MISSING.
