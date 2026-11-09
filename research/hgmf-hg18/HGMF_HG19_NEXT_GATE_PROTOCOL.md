# HGMF‑HG19 — Operational Context Metric, Action Cost and Dimensional Coupling

## Objective

Determine whether a physical context-area form with units and normalization can be derived from intervention cost, action or control dynamics, and whether it selects one HGMF coupling across non-isomorphic carriers.

## Gate A — control metric

Derive a tensor `h_ij` from physical action cost, control energy and duration, clock resolution or causal sensitivity. It may not be chosen to fit holonomy.

## Gate B — QGT compatibility

Compare

\[
dA_h
\quad\text{and}\quad
dA_Q.
\]

Determine whether they are proportional and what fixes the dimensionful proportionality factor.

## Gate C — dimensional transgression

Audit

\[
\mathcal F=\mathcal F_{std}+\lambda_{HG}dA_h.
\]

Derive or reject a dimensionful `lambda_HG`.

## Gate D — mixed-state metric

Select a monotone metric through an additional physical principle or return `FAIL_METRIC_UNIQUENESS`.

## Gate E — cross-carrier law

The same `lambda_HG` must predict two non-isomorphic carriers under a preregistered UMI transport.

## Gate F — future-only test

Freeze calibration patches and predict held-out loops, logarithm branches and new physical areas.

## Gate G — standard nuisance

Exclude standard Berry curvature, quantum metric, control holonomy, hidden ancillas, mixed-state metric choice and process-tensor effects.

## Authorized outcomes

- `PASS_OPERATIONAL_CONTEXT_METRIC`
- `PASS_DIMENSIONAL_COUPLING_SELECTION`
- `PASS_CROSS_CARRIER_CURVATURE_DENSITY`
- `FAIL_METRIC_UNIQUENESS`
- `FAIL_STANDARD_GEOMETRY_EXCLUSION`
- `HOLD_PHYSICAL_PROTOGEOMETRY`
