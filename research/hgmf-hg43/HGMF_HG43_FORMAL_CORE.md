# HGMF‑HG43 — Formal core

## 1. Receipt-conditioned arming theorem

Let c index carriers and j index preregistered local cells.

For each carrier, freeze:

- a quotient chart T_c and dominating measure mu_c;
- a proper training-only candidate density g_c;
- a certified upper density U_c satisfying q_P <= U_c for every admitted standard null P;
- a replicate-admission certificate;
- a covariance certificate;
- local power certificates.

Let the program-level aggregation rule A be selected before holdout and be valid for the declared claim semantics.

If every receipt and proof hash is admitted before holdout, all candidate and null densities use the same measure, all local rank/fitness tests pass, the split is disjoint, and no holdout values are present, the dossier is sufficient for an arming decision.

The theorem is conditional. It does not create the receipts, densities or power that it requires.

## 2. Independence-cluster admission

Rows, field points, interpolation nodes and repeated instrument readings are not automatically independent replicates.

Each admitted replicate must carry:

- a unique replicate ID;
- an acquisition hash;
- an independent-cluster ID;
- an ancestry hash;
- calibration/reference receipt hashes;
- a certificate that different clusters are independent under the frozen design.

The effective replicate count is the number of certified independent clusters, not the number of rows.

For an unrestricted d-dimensional covariance after a rank-r mean fit, the necessary generic condition remains:

n_clusters >= d + r.

A thousand pseudoreplicated rows from one acquisition root still count as one cluster.

## 3. Structured covariance finite-supremum theorem

Consider a Gaussian family with covariance Sigma(psi), psi in Psi.

A finite profile likelihood is certified if:

1. Psi is compact or otherwise bounded by a proof certificate;
2. Sigma(psi) is continuous on Psi;
3. there is a certified lambda_floor > 0 such that

   Sigma(psi) >= lambda_floor I

   for every psi in Psi;
4. the mean family is finite on the admitted observations.

Then log det Sigma is bounded below and quadratic forms are finite, so the Gaussian log-likelihood has a finite supremum on the certified parameter set.

Without a positive eigenvalue floor, a covariance family may collapse onto the data and the likelihood supremum may diverge.

## 4. Union upper density theorem

Suppose H0 is the union of standard-null families H_k and U_k upper-bounds every density in H_k on one common measure.

Then

U_union(x) = max_k U_k(x)

upper-bounds every density in H0.

The maximum need not integrate to one. That is not required. It is a denominator envelope, not a probability density.

If g is proper, E=g/U_union is a valid e-variable under the union null.

The sum of the component upper densities is also valid but no tighter than the maximum.

## 5. Claim-logic aggregation

The aggregation rule must match the claim:

- carrier-local claim: report the carrier e-value without program aggregation;
- mixture or screening claim: a preregistered weighted mean is valid;
- conjunction claim requiring all carriers/cells: use the minimum;
- sequential accumulation: use a product only with a conditional e-factor proof and frozen filtration.

A weighted mean can be large because one carrier is strong while another is powerless. It cannot support a statement whose semantics require every carrier to pass.

## 6. Local Cantelli power certificate

For one cell, let L_i=log e_i be independent cluster-level log e-increments under a frozen planning alternative.

Assume certified bounds:

E[L_i] >= m > 0,
Var(L_i) <= v < infinity.

For n independent clusters:

E[L_n] >= n m,
Var(L_n) <= n v.

Let A=log tau. If n m > A, Cantelli's inequality gives:

P(L_n >= A)
>=
(n m - A)^2 /
[n v + (n m - A)^2].

This is finite-sample and does not require Gaussianity.

For target power p, define kappa=p/(1-p). A sufficient replicate count is obtained from:

m x^2 - sqrt(kappa v) x - A >= 0,
x=sqrt(n).

Thus:

x_* =
[sqrt(kappa v)+sqrt(kappa v+4mA)]/(2m),

n_min=ceil(x_*^2),

followed by an exact integer check.

No numerical n can be issued until m and v are estimated and frozen from calibration/training only.

## 7. Conjunction familywise power

For a conjunction claim with E_program=min_j E_j:

P(E_program >= tau)
=
P(all j: E_j >= tau).

If cell j has certified failure probability beta_j, the union bound yields:

P(E_program >= tau)
>=
1 - sum_j beta_j.

Therefore cellwise beta budgets must be allocated before holdout. A high average power cannot rescue a powerless cell.

## 8. Arming sufficiency

The dossier may be armed only when:

- chart and measure fields are complete;
- claim semantics and aggregation rule agree;
- every carrier has real admitted replicate clusters;
- every covariance model has a finite-supremum certificate;
- every candidate density has a properness proof;
- every standard-null union has an upper-density proof;
- every local cell has a power certificate;
- global conjunction beta allocation is valid when required;
- code, environment, design, model and split hashes are frozen;
- prospective outcomes are absent;
- the stage is explicitly changed to ARMED_FUTURE_ONLY.

Any missing object produces abstention. Any contradiction, leakage or false authority produces failure.
