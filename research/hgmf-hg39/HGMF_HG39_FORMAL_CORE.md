# HGMF‑HG39 — Formal commissioning core

## 1. Evidence hierarchy

Let \(E\) denote commissioning evidence.

### Capability discovery

A facility or vendor states that a method exists.

\[
E\in\mathcal E_{\rm discovery}.
\]

This supports route discovery only.

### Accredited scope

An accreditation body or national metrology institute confirms competence for a stated class of calibration.

\[
E\in\mathcal E_{\rm scope}.
\]

This supports provider qualification, not traceability of the future HGMF result.

### Signed service confirmation

A provider confirms the exact measurand, geometry, range, method, deliverables and anticipated uncertainty.

\[
E\in\mathcal E_{\rm service}.
\]

This supports procurement and commissioning design.

### Actual measurement result

A completed result contains value, uncertainty, method, traceability chain, environmental conditions and artifacts.

\[
E\in\mathcal E_{\rm result}.
\]

Only this level can populate a real receipt.

Thus:

\[
\mathcal E_{\rm discovery}
\not\Rightarrow
\mathcal E_{\rm scope}
\not\Rightarrow
\mathcal E_{\rm service}
\not\Rightarrow
\mathcal E_{\rm result}.
\]

## 2. Magnetic measurement model

Let the sample field be

\[
B_s=f(B_c,B_r,d,T,x,t;\theta)+\epsilon,
\]

where:

- \(B_c\): commanded field;
- \(B_r\): instrument readback;
- \(d\): sweep direction;
- \(T\): temperature;
- \(x\): probe/sample position;
- \(t\): time;
- \(\theta\): calibrated map parameters.

For a frozen field grid, the covariance is propagated as:

\[
\Sigma_{B_s}
=
J_\theta\Sigma_\theta J_\theta^\top
+
\Sigma_{\rm repeat}
+
\Sigma_{\rm position}
+
\Sigma_{\rm drift}
+
\Sigma_{\rm hysteresis}.
\]

The expanded uncertainty is:

\[
U_B=k\sqrt{\operatorname{diag}(\Sigma_{B_s})}.
\]

A magnetic receipt passes only when:

- full experimental range is bracketed;
- reversal regions are included;
- pre/post and both sweep directions exist;
- the covariance artifact is present;
- the preregistered numeric limit is met;
- field calibration is transferred to the final sample geometry.

## 3. Adsorption observation map

\[
Q=
\frac{V_c-V}{V_c-V_s}.
\]

Let:

\[
D=V_c-V_s.
\]

The Jacobian with respect to \(x=(V,V_s,V_c)\) is:

\[
\nabla Q
=
\left(
-\frac1D,\;
\frac{Q}{D},\;
\frac{1-Q}{D}
\right).
\]

Therefore:

\[
u_Q^2
=
\nabla Q^\top
\Sigma_x
\nabla Q
\]

before pressure, temperature, mass and surface-area terms are added.

For Bethe scan inversion:

\[
\alpha=\frac{Q_--Q_+}{1-Q_+},
\qquad
y=(1-\alpha)^{1/z},
\]

\[
q=
\frac{1-y}
{1-(1-Q_+)y^{z-1}}.
\]

HG39 uses a numerical Jacobian to propagate the covariance of \((Q_+,Q_-,z)\) to \(q\).

## 4. Reference materials

An instrument-performance standard can test a measurement system.

It cannot replace a matched reference specimen when the scientific observation model requires surface chemistry, pretreatment, adsorbate lot and temperature equivalence.

Thus:

\[
\text{SRM validation}
\not\equiv
V_s(p,T)\text{ reference}.
\]

## 5. Topology receipt

Independent topology requires at least:

1. a size/surface method with calibration and uncertainty;
2. a connectivity-sensitive method or a justified set-valued connectivity constraint;
3. a resolution-adequacy statement;
4. sample identity and split ancestry;
5. completion before holdout.

Gas adsorption alone is not treated as independent topology for the same adsorption null.

## 6. Arming theorem

Let \(R_m,R_a,R_t\) denote real magnetic, adsorption and topology receipts, and let \(L\) denote frozen numeric fitness limits.

HG38 arming is authorized only if:

\[
R_m\land R_a\land R_t\land L
\]

and every artifact/hash/time/holdout condition passes.

Provider discovery without results leaves:

\[
\boxed{\texttt{ABSTAIN\_REAL\_COMMISSIONING\_NOT\_COMPLETE}.}
\]
