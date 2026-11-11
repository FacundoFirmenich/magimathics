# HGMF‑HG44 — Formal core: conformational evidence dynamics

## 1. Filtration and conformation

Let

F_0 subseteq F_1 subseteq ... 

be the admitted information filtration.

A scientific conformation K_t is a complete configuration containing:

- quotient chart and measure;
- calibration/reference epoch;
- candidate-density algorithm;
- null-family upper-density algorithms;
- selected carrier and local cell;
- claim semantics;
- aggregation rule;
- quarantine state;
- stopping/recalibration policy.

K_t must be F_(t-1)-measurable. This is the formal meaning of **future-only**.

## 2. Conditional quotient e-factor theorem

For every null P in H_0, let q_(P,t)(x | F_(t-1),K_t) be the conditional density of the next admitted quotient observation X_t with respect to the frozen measure mu_(K_t).

Let g_t be a proper conditional candidate density and U_t satisfy

U_t(x | F_(t-1),K_t)
>=
sup_(P in H_0) q_(P,t)(x | F_(t-1),K_t).

Define

e_t
=
g_t(X_t | F_(t-1),K_t) /
U_t(X_t | F_(t-1),K_t),

with e_t=0 where U_t=0.

Then

E_P[e_t | F_(t-1)] <= 1.

Therefore

M_t = product_(i=1)^t e_i,
M_0=1,

is a nonnegative supermartingale under every P in H_0.

## 3. Evidence conservation law

For every bounded stopping time tau,

E_P[M_tau] <= 1.

By nonnegative convergence/optional-stopping extension, M_tau is an e-value for every stopping time for which the stopped process is defined.

A predictable transition may redistribute betting strategy, model weight or acquisition effort, but it cannot increase expected evidence under the null.

This is the **conformational conservation law**:

> admissible changes of scientific conformation preserve null-expected capital.

## 4. Predictable switching theorem

Suppose a family of candidate factors e_(k,t) satisfies

E_P[e_(k,t) | F_(t-1)] <= 1

for every k.

If K_t is selected using only F_(t-1), then

e_t = e_(K_t,t)

is conditionally valid.

Thus the experiment may change:

- carrier;
- cell;
- predictive model;
- calibration epoch;
- acquisition allocation;

based on all admitted past information.

It may not choose the factor after observing X_t.

## 5. Predictable mixture theorem

Let w_(k,t) be F_(t-1)-measurable, nonnegative and sum to one.

Then

e_t = sum_k w_(k,t)e_(k,t)

satisfies

E_P[e_t | F_(t-1)] <= 1.

This provides a lawful conformational portfolio over candidate predictive laws. The portfolio may adapt after each past outcome, but the weights scoring X_t must be frozen before X_t.

## 6. No-retroactive-rewrite theorem

Let X be fair Bernoulli and define

e_0(X)=2 1_{X=0},
e_1(X)=2 1_{X=1}.

Both are valid e-values:

E[e_0]=E[e_1]=1.

If the factor is chosen after observing X,

e_*(X)=max(e_0(X),e_1(X))=2,

so

E[e_*]=2>1.

Therefore same-step outcome-dependent model selection can manufacture evidence from the null.

Any modification of chart, null family, candidate family, cell or claim that changes the score already assigned to an observed outcome is a retroactive rewrite and is forbidden.

## 7. Epoch concatenation theorem

Let tau_1<tau_2<... be stopping times marking recalibration events.

Within epoch j, use factors e_t^(j) whose conditional validity is certified by receipt R_j and the information available before X_t.

If the new epoch configuration is selected at tau_j and applies only to t>tau_j, then the full product across epochs remains a supermartingale.

Recalibration is therefore a phase transition in the future conditional law, not an edit to past evidence.

## 8. Predictable quarantine theorem

Let A_t in {0,1} be F_(t-1)-measurable and define

e'_t
=
1-A_t + A_t e_t.

Then

E[e'_t | F_(t-1)] <= 1.

Thus an epoch known in advance to be inadmissible may be quarantined with neutral factor one.

If A_t is selected after observing X_t, the theorem does not apply. Selective deletion of adverse observations is a retroactive rewrite.

## 9. Adaptive allocation theorem

Let J_t be an F_(t-1)-measurable choice of next carrier or local cell. If the selected factor is conditionally valid for every possible J_t, adaptive allocation preserves validity.

Validity and semantic completeness are distinct:

- one may adaptively collect more data in weak cells;
- one may not abandon a preregistered cell and retain a conjunction claim that requires it.

## 10. Claim lattice

Represent a conjunction claim by the set S of required cells.

Define its evidence at time t by

E_S(t)=min_(j in S) E_j(t).

If S subseteq S', then

E_(S')(t) <= E_S(t).

Strengthening the claim cannot increase evidence.

Moving after outcomes from S' to a weaker S may increase evidence and is a claim-selection operation. It requires a preregistered claim family and multiplicity-safe rule; it is not a harmless narrative rewrite.

## 11. Null-envelope monotonicity

If the admitted standard-null class expands from H_0 to H'_0 superset H_0, its upper density can be updated conservatively so that

U'_t >= U_t.

Then

e'_t = g_t/U'_t <= g_t/U_t = e_t.

Adding a newly recognized standard competitor can only reduce future evidence.

Removing a null family after observing data can increase evidence and is forbidden unless the contraction rule was frozen before outcomes and independently justified.

## 12. Anytime-valid stopping

For alpha in (0,1), define

tau_alpha = inf{t: M_t >= 1/alpha}.

Ville's inequality gives

sup_(P in H_0)
P_P(sup_t M_t >= 1/alpha)
<= alpha.

Stopping because evidence crossed the threshold, resources ended, recalibration was triggered or an external event occurred does not invalidate the test, provided all factors were conditionally valid.

## 13. Conjunction anytime validity

Suppose the program alternative requires every cell j in S, so the composite null is the union of cell-specific nulls.

For each P in the union, at least one j(P) is null and E_j is an e-process under P.

Because

min_j E_j(t) <= E_(j(P))(t),

the minimum process is an e-process under the union null in the stopping-time sense:

E_P[min_j E_j(tau)] <= 1.

## 14. State irreversibility

Authorized state transitions form a directed acyclic scientific history:

PROTOCOL_FROZEN_UNARMED
-> ARMED_FUTURE_ONLY
-> ACQUIRING_EPOCH
-> PAUSED_RECALIBRATION
-> ACQUIRING_EPOCH
-> TERMINAL_PASS / TERMINAL_FAIL / TERMINAL_ABSTAIN.

A transition may add a receipt, start a new epoch or stop the process. It may not change an earlier event, factor, hash or conformation.

The hash chain supplies syntactic irreversibility; predictable-factor validity supplies statistical irreversibility.

## 15. Narrative-deductive consequence

The scientific narrative is no longer composed after results. It is generated sequentially by the unique admissible path through:

1. prior conformation;
2. admitted event;
3. verified transition;
4. conditional factor;
5. updated evidence capital;
6. next conformation.

The resulting narrative is deductive and auditable: every statement about why the experiment changed state has a prior information set, a transition rule and a receipt hash.
