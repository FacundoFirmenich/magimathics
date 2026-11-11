# HGMF‑HG43 — Claim semantics, dependence and local power

## Carrier-local claims

Report each carrier e-value separately. Do not manufacture a program-level aggregate.

## Mixture or screening claims

A preregistered weighted mean is valid under arbitrary dependence:

E_mix = sum_k w_k E_k.

This claim means evidence may be supplied by one or several carriers. It does not mean every carrier passed.

## Program conjunction

If the claim requires all carriers or all preregistered cells:

E_all = min_k E_k.

The minimum is a valid e-value and directly encodes the conjunction.

Cellwise power budgets beta_k must satisfy:

sum_k beta_k <= 1 - pi_global.

## Sequential accumulation

Products are permitted only for conditionally valid e-factors under a frozen filtration. Raw multiplication of carrier or cell e-values is forbidden.

## Local power certificate

Each cell must provide training-only certified bounds m_k and v_k for log e-increments and enough independent clusters to meet its assigned target. Global averages do not repair a cell with zero local growth or unidentified covariance.
