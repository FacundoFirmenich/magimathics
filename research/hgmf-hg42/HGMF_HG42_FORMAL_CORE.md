# HGMF‑HG42 — Formal core

## 1. Calibration-augmented quotient universal e-value

Let D_T be training data and let the evaluation object be

X=(C,Z),

where C contains calibration/reference measurements and Z=T(Y_H) is the frozen quotient representation of holdout outcomes.

For every null law P in H0, suppose X has density q_P(c,z) with respect to one fixed measure

nu_C x mu_Q.

Let g_T(c,z) be any proper joint density selected using training only, or a pre-specified proper kernel construction. Let

U_0(c,z) >= sup_{P in H0} q_P(c,z).

Then

E(c,z)=g_T(c,z)/U_0(c,z)

on U_0>0, and zero otherwise, satisfies

sup_{P in H0} E_P[E(C,Z) | D_T] <= 1.

Proof:

E_P[E | D_T]
= integral g_T/U_0 * q_P d(nu_C x mu_Q)
<= integral g_T d(nu_C x mu_Q)
=1.

This includes calibration data in the confirmatory likelihood. It does not replace calibration uncertainty with a plug-in estimate.

## 2. Proper conditional candidate construction

A proper candidate may factor as

g_T(c,z)=h_T(c) k_T(z|c),

provided h_T is a proper calibration density and k_T(.|c) is a proper conditional quotient density for every c.

The algorithm generating k_T from c must be frozen before evaluation. This permits calibration-conditioned prediction without allowing holdout adaptation.

## 3. Frozen compression theorem

Let S:Z->W be a measurable compression frozen using training only. If g_T^W and q_P^W are the pushforwards of proper quotient laws, and

U_0^W(w) >= sup_P q_P^W(w),

then

E_W(w)=g_T^W(w)/U_0^W(w)

is a valid e-value.

Compression can lower dimension and replicate burden. By data processing, it cannot recover distinctions destroyed by S. No basis, feature subset or pressure window may be selected after holdout.

## 4. Dependence firewall

Let E_1,...,E_K be marginal e-values for a common null.

### Always valid under arbitrary dependence

For nonnegative weights summing to one,

E_mean=sum_k w_k E_k

is an e-value.

Also,

E_intersection=min_k E_k

is an e-value because it is bounded above by every E_k. This is suitable when every preregistered cell must independently carry evidence.

### Not generally valid

The raw product

prod_k E_k

need not be an e-value when the factors are dependent.

Counterexample: under a fair Bernoulli X, let

E_1=E_2=2 1{X=1}.

Each factor has expectation one, but the product has expectation two.

### Valid sequential product

A product is authorized only when, for a frozen filtration F_k,

E[E_k | F_{k-1}] <= 1.

Then the running product is an e-process.

Interpolation nodes, pressure points and curve features may not be multiplied as if independent unless this conditional factorization is part of the sealed model.

## 5. Full-covariance replicate-rank theorem

Let Z_1,...,Z_n be d-dimensional quotient replicate vectors. After fitting a mean design of rank r, residual scatter rank is at most n-r.

For an unrestricted positive-definite covariance, the Gaussian profile likelihood is finite only if residual scatter has rank d. Therefore a necessary generic condition is

n-r >= d,

or

n >= d+r.

For a common unknown mean, r=1 and the minimum is d+1 independent replicate vectors.

If n-r<d, covariance can collapse in a residual-free direction and the likelihood supremum is infinite.

This is an algebraic lower bound, not a power recommendation.

## 6. Structured covariance alternative

A structured covariance model can reduce replicate requirements only if, before holdout, it supplies:

- a positive-definite parameterization;
- an identified parameter map;
- a proof or certificate that the null likelihood supremum is finite;
- a training-only fitting rule;
- a frozen model complexity;
- a certified upper density for the full carrier-standard null.

Merely declaring a low-rank, diagonal or Gaussian-process covariance is insufficient.

## 7. Interpolation covariance theorem

Let raw observations have covariance Sigma_raw. Let A be the frozen interpolation or resampling operator and G the quotient Jacobian.

Then

Sigma_Q = G A Sigma_raw A^T G^T.

Shared raw nodes create off-diagonal covariance. Treating interpolated nodes as independent replaces the actual observation measure and can manufacture evidence.

A further frozen linear compression B yields

Sigma_compressed = B Sigma_Q B^T.

## 8. Prospective split seal

Before holdout, the seal must fix:

- quotient measure ID;
- labelled anchors and orientation;
- anchor degeneracy rule;
- calibration/training/holdout IDs;
- quotient dimension;
- replicate definition;
- covariance family;
- candidate density proof;
- null upper density proof;
- dependence-combination rule;
- code and environment hashes;
- acquisition authority.

Missing real replicates or density proofs produces abstention. An unsafe aggregation rule or holdout leakage produces failure.

## 9. Historical readiness audit

### Magnetism

The HG41 magnetic quotient has dimension d=3 and only one historical independent quotient vector. An unrestricted covariance with common mean needs at least four independent vectors.

### Adsorption

HG40 produced 242 quotient coordinates from one correlated historical history ensemble. Treating coordinates as replicates is prohibited. An unrestricted 242-dimensional covariance would require at least 243 independent history vectors. A lower-dimensional structured route remains possible only after a training-frozen compression or structured covariance receipt.

## 10. Claim boundary

HG42 proves how a prospective quotient e-value can be valid and when its noise law is estimable. It does not fit a real carrier noise law, compute E=140, authorize acquisition, reject carrier-standard physics or support physical protogeometry.
