# HGMF‑HG38 — Formal prospective identifiability core

## 1. Two-stage seal

Let \(S_0\) be the protocol seal and \(S_1\) the arming seal.

\(S_0\) freezes the admissible procedures and algorithms. It contains no prospective outcomes and grants no acquisition authority.

\(S_1\) binds:

- real calibration receipts;
- numeric fitness-for-purpose limits;
- training-frozen models;
- holdout design;
- software environment;
- artifact hashes.

The first holdout event must satisfy:

\[
t_{\rm holdout,1}>t_{S_1}.
\]

## 2. Magnetic identifiability

The prospective measurement model is

\[
H_{\rm ref}=f(H_{\rm command},H_{\rm readback},d,T,\ldots),
\]

with parameter covariance and pre/post drift.

The full observation model is

\[
V_{xy}(H_{\rm ref})
\sim
P_{\theta,\eta},
\]

where \(\eta\) includes field calibration, drift, voltage noise and shared systematics.

The calibration receipt is fit for purpose only if its expanded uncertainty and drift are below limits frozen in \(S_1\). HG38 does not invent those limits.

## 3. Adsorption identifiability

The observation map is

\[
V(p,T)=V_s(p,T)Q(p,T)+[1-Q(p,T)]V_c(p,T).
\]

Prospective point identification requires independent measurement of \(V_s\) and \(V_c\), with covariance, under matched adsorbate, temperature and surface chemistry.

The topology receipt must be independent of holdout scanning outcomes.

## 4. Future-only information barrier

Calibration and training may determine numeric grids and model parameters only before holdout sealing.

After \(S_1\):

- no threshold changes;
- no model-family changes;
- no analysis-code changes except a fail-closed new protocol version;
- no early efficacy look;
- every acquisition event enters a hash chain.

## 5. Authority boundary

A protocol can be valid while unarmed.

Therefore:

\[
\texttt{PASS\_PROTOCOL}
\not\Rightarrow
\texttt{PASS\_ARMED}.
\]

The current HG38 result is the former only.
