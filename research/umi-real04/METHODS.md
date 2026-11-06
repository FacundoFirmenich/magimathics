# MGM‑UMI‑REAL‑04 — Frozen Methods

Ten family-level cases were fixed: five positives and five near-neighbour decoys. The ground-truth mapping was salted and SHA‑256 committed before prediction.

A case is positive iff all conditions hold:

- baseline signature passes;
- substitution pass rate ≥ 0.80;
- every critical ablation destroys the signature;
- at least half the frozen rewires destroy the signature;
- at least two transported implementations exist;
- exactly one minimal-carrier equivalence class remains.

Three semantic profiles were frozen: strict, moderate and weak. With incomplete evidence, observed hard failure gives `NEGATIVE`; otherwise incomplete evidence gives `ABSTAIN`; `POSITIVE` requires complete passing evidence.

This is an internally blinded mechanistic benchmark, not an independently curated external validation set.