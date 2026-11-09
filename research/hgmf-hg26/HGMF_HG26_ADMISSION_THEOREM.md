# HGMF‑HG26 — Teorema de admisión estratificada

Sea \(r\) una unidad experimental y sean:

- \(B(r)\): integridad de bytes;
- \(S(r)\): conformidad de schema;
- \(P(r)\): closure de provenance;
- \(C(r)\): calibración válida;
- \(A(r)\): ancestry/reset/prefix válido;
- \(Q(r)\): quality control;
- \(H(r)\): conformidad con analysis seal.

La admisión es:

\[
\operatorname{Admit}(r)
=
B(r)\land S(r)\land P(r)\land C(r)\land A(r)\land Q(r)\land H(r).
\]

No existe compensación entre capas. En general:

\[
B\nRightarrow P,
\quad P\nRightarrow C,
\quad C\nRightarrow A,
\quad A\nRightarrow Q,
\quad Q\nRightarrow H.
\]

## Estados

- `ADMITTED`: todos los predicados pasan;
- `QUARANTINED`: existe un fallo verificable;
- `ABSTAIN_INCOMPLETE_RECEIPT`: falta evidencia necesaria;
- `DUPLICATE_CELL`: múltiples receipts sin contrato de réplica;
- `ORPHAN_DERIVATION`: parents ausentes;
- `HOLDOUT_CONTAMINATED`: seal mismatch o uso durante training.
