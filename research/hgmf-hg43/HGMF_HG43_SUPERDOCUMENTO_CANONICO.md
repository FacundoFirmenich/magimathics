# HGMF‑HG43 — Receipt-conditioned quotient laws, local maximin power and arming sufficiency

## Verdict

PASS_RECEIPT_CONDITIONED_ARMING_THEOREM  
PASS_INDEPENDENCE_CLUSTER_ADMISSION  
PASS_STRUCTURED_COVARIANCE_FINITE_SUPREMUM_THEOREM  
PASS_NULL_UNION_UPPER_DENSITY_RULE  
PASS_CLAIM_LOGIC_AGGREGATION  
PASS_CANTELLI_LOCAL_POWER_CERTIFICATE  
PASS_CONJUNCTION_FAMILYWISE_POWER_BOUND  
PASS_FAIL_CLOSED_ARMING_VALIDATOR  

FAIL_CURRENT_RECEIPT_ADMISSION  
FAIL_CURRENT_MAGNETIC_QUOTIENT_LAW  
FAIL_CURRENT_ADSORPTION_QUOTIENT_LAW  
FAIL_CURRENT_LOCAL_MAXIMIN_POWER  
FAIL_CURRENT_ARMING  

ABSTAIN_REAL_RECEIPTS_MISSING  
ABSTAIN_PROPER_CANDIDATE_DENSITIES_MISSING  
ABSTAIN_CERTIFIED_NULL_UPPER_DENSITIES_MISSING  
ABSTAIN_NUMERIC_POWER_CERTIFICATES_MISSING  

HOLD_ACQUISITION  
HOLD_PROSPECTIVE_OUTCOMES  
HOLD_PHYSICAL_PROTOGEOMETRY

## Core result

HG43 completes the logical arming tribunal that HG42 left open.

A carrier can enter the confirmatory quotient test only if:

1. its chart and dominating measure are frozen;
2. admitted observations form certified independent clusters rather than pseudoreplicates;
3. the covariance likelihood has a finite supremum;
4. the candidate density is proper on the frozen measure;
5. every carrier-standard null family has a certified upper density;
6. the e-value combination rule matches the scientific claim;
7. every preregistered local cell passes an explicit power lower bound;
8. code, environment, model, design and split hashes are frozen;
9. no holdout outcome has been exposed.

The current dossier contains none of the real prospective receipts required by these conditions. It therefore remains scientifically clean but unarmed.

## Formal closure

For each carrier, freeze a quotient chart and measure, a proper training-only candidate density, a certified standard-null upper density, a replicate-admission certificate, a covariance certificate and local power certificates. If all hashes predate holdout, the split is disjoint, the measures match and every local rank/fitness test passes, the dossier is sufficient for an arming decision. The theorem is conditional and does not create the receipts it requires.

The effective sample size is the number of certified independent acquisition clusters, not rows, field points, interpolation nodes or repeated instrument readings. For unrestricted d-dimensional covariance after a rank-r mean fit, the generic necessary condition is n_clusters >= d+r.

A structured Gaussian covariance family has finite profile supremum only after certifying a bounded parameter domain and a uniform positive eigenvalue floor. Without that floor, covariance collapse can make the supremum diverge.

For a union of standard-null families, the carrier denominator can be certified by U_union=max_k U_k. The maximum need not normalize: it is a likelihood envelope, not a probability density.

Claim semantics are binding. Weighted means are valid for mixture/screening claims; the minimum is required for a conjunction claim; products require conditional e-factor validity under a frozen filtration.

For one local cell, if independent cluster-level log e-increments satisfy E[L_i]>=m>0 and Var(L_i)<=v, then for n clusters and threshold tau:

P(sum_i L_i >= log tau) >= (n m-log tau)^2/[n v+(n m-log tau)^2]

whenever n m>log tau. For conjunction claims, cellwise failure budgets beta_j yield global power at least 1-sum_j beta_j.

## Current exact adjudication

The current dossier is internally valid but incomplete. It contains no real replicate receipts, candidate-density proofs, null-upper certificates, local power certificates or frozen arming hashes.

Therefore the only authorized result is:

ABSTAIN_REAL_RECEIPTS_DENSITIES_OR_POWER_MISSING.

No acquisition or prospective outcome evaluation is authorized.
