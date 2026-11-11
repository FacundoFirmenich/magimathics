# HGMF‑HG42 — Magnetic quotient noise-law contract

## Observation object

The confirmatory magnetic object is the replicated full curve under a shared calibrated field map, not HEB alone.

Each independent replicate must preserve:

- commanded field;
- reference field;
- sweep direction;
- pre/post calibration epoch;
- raw repeated Vxy;
- loop identity and order;
- temperature and timing;
- calibration receipt hash;
- acquisition-event hash ancestry.

## Quotient chart

The seal must freeze:

- labelled curve anchors;
- orientation;
- anchor-degeneracy threshold;
- curve alignment rule;
- feature/interpolation operator;
- quotient measure ID.

## Joint likelihood

The evaluation density is joint in calibration/reference observations C and magnetic quotient holdout Z_M.

Calibration parameters remain in the null model and are profiled or bounded jointly. They are not plugged in as known constants.

## Covariance

The noise law must include:

- repeated-voltage covariance;
- field-map covariance;
- non-affine residual field error;
- cross-loop covariance;
- anchor covariance;
- covariance induced by interpolation/alignment.

If the quotient dimension is d_M and covariance is unrestricted with a common mean, at least d_M+1 independent replicate quotient vectors are necessary for a finite Gaussian profile likelihood.

For the historical d_M=3 chart, the algebraic minimum is four independent replicate vectors. The historical record supplies one.

## Candidate density

The candidate quotient density may be fit on training only. It must be proper on the sealed quotient measure.

## Null upper density

The denominator must upper-bound every admitted carrier-standard magnetic null, including the source-specific trained-state/domain mechanism and every additional registered competitor.

## Combination

Cross-loop or cross-cell factors may be multiplied only under a sealed conditional e-factor model. Otherwise use a preregistered weighted mean or minimum.

## Current status

ABSTAIN_REAL_MAGNETIC_REPLICATES_MISSING.
