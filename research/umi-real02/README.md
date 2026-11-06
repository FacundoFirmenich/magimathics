# MGM-UMI-REAL-02 — Constant-Signal Internal-Model Closure

**Authority:** `MAGIMATICS / REAL UMI TRIBUNAL`  
**Verdict:** `PASS_CROSS_DOMAIN_UMI / PASS_UNIQUE_RELATIONAL_CLASS / NO_UNIQUE_MATERIAL_CARRIER`

## Candidate

The second real candidate is not a molecule, a node list or one fixed graph. It is the relational equivalence class

\[
\mathcal U_{\rm RPA}=\text{constant-signal internal-model closure}.
\]

Its critical relations are:

1. regulated output -> sensing/comparison;
2. error -> persistent memory integration;
3. memory -> corrective plant actuation;
4. stable closed-loop realization.

Its frozen semantic signature is robust perfect adaptation: following a persistent step, the output detects the disturbance and returns to the same setpoint despite admissible changes in plant parameters and disturbance magnitude.

## Exact results

For

\[
\dot y=-ay+bz+d,\qquad \dot z=k(r-y),
\]

any stable equilibrium satisfies

\[
y^*=r,\qquad z^*=(ar-d)/b.
\]

Proportional control alone gives

\[
y^*-r=(d-ar)/(a+bK_p),
\]

and therefore does not robustly perfect-adapt.

For the antithetic realization

\[
\dot z_1=\mu-\eta z_1z_2,\qquad
\dot z_2=\theta y-\eta z_1z_2,
\]

subtracting yields

\[
\frac{d}{dt}(z_1-z_2)=\mu-\theta y,
\]

so a stable equilibrium satisfies \(y^*=\mu/\theta\), independently of the plant.

## Frozen tribunal

- **Substitution:** first-order plant, second-order plant, nonlinear chemotaxis-like loop and antithetic controller all pass.
- **Parameter substitution:** 108/108 deterministic plant/controller/disturbance combinations pass.
- **Ablation:** removing sensing, integration or actuation destroys the signature.
- **Rewiring:** sign flip, disturbance sensing, constant sensing and proportional-only controls fail.
- **Minimality:** only the full sensor-integrator-actuator carrier passes all eight relation-subset tests.
- **Transport:** the relation is realized in natural bacterial chemotaxis, synthetic bacterial regulation, cell-free TXTL, mammalian circuits and engineered integral controllers.

## Cross-domain result

UMI-R1 preserved sustained oscillation. UMI-R2 preserves robust perfect adaptation. The same preregistered substitution–rewiring–ablation–transport tribunal identifies a minimal invariant relational carrier in both unrelated functions.

\[
\boxed{\texttt{PASS\_CROSS\_DOMAIN\_UMI}}
\]

This promotes the UMI from a domain-local concept to a candidate operational unit for general systems theory. It is an equivalence class of relational conformations, not a new material atom or ontology.

## Claim boundary

Established antecedents include integral control, the internal model principle, chemotaxis adaptation, antithetic feedback and general RPA basis modules. Magimatics does not claim discovery of those structures. Its candidate contribution is the cross-domain adjudication protocol and the concept of a minimal invariant relational carrier.

## Remaining holds

- empirical multifractality;
- public priority of the complete tribunal;
- blind third-domain adjudication;
- external review before arXiv submission.
