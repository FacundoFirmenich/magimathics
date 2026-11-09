# HGMF-HG36 — Formal core

## 1. Magnetic observation decomposition

For loop n:

h_obs,n = mu_n + delta_n + epsilon_n,

where:
- mu_n is physical exchange bias;
- delta_n is bounded field-axis discretization/systematic error;
- epsilon_n is repeated-voltage sampling error.

The raw-voltage bootstrap quantifies epsilon_n. The source field spacing bounds delta_n.

For the trained-state null:

mu_n = 0, n=2,...,5.

If |h_obs,n| <= Delta_n, then delta_n=h_obs,n is admissible and the stochastic residual is zero.

Hence an HEB-summary likelihood with independently profiled bounded delta_n reaches its observational peak under the null. No e-value >1 can be obtained from HEB alone against that class.

## 2. Vycor reference nonidentifiability

The network observation map is

V = Vs Q + (1-Q) Vc,

so

Q = (Vc-V)/(Vc-Vs).

For fixed V and Vc, every admissible Q in (0,1] determines

Vs = [V-(1-Q)Vc]/Q.

Without an external film-reference constraint, Vs and Q are not point-identified.

The Bethe scan inverse is algebraic:

alpha = (Qminus-Qplus)/(1-Qplus),
y = (1-alpha)^(1/z),
q = (1-y)/[1-(1-Qplus)y^(z-1)].

Therefore set-valued Q induces set-valued q.

## 3. Distinct no-go mechanisms

Magnetism:
sampling noise is small, but bounded field-axis nuisance destroys summary-level power.

Adsorption:
the topology core is defined, but the observation map is underidentified because Vs is external.

These are not equivalent failure modes and require different future interventions.
