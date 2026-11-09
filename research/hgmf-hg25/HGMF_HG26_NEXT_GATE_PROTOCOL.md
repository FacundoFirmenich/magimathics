# HGMF‑HG26 — Receipts de adquisición y primera adjudicación empírica dual-carrier

## Objetivo

Ingresar únicamente datos reales con procedencia, hashes y contratos de intervención verificables, y ejecutar el análisis congelado de HG25.

## Gate A — receipts

Cada unidad debe declarar:

- carrier;
- wave;
- preset/control;
- field/depth;
- cycle;
- reset;
- timestamp;
- instrument;
- raw-file hash.

## Gate B — completeness

- magnetic: 72/72 target-grid loops;
- second carrier: 72/72 homologous runs;
- no missing rectangle corners.

## Gate C — component extraction

Preservar \((A,B,C,K,E,Q,Z)\), incertidumbres y `ABSTAIN`.

## Gate D — training

Fit de waves 1–2 solamente.

## Gate E — holdout

Wave 3 puntuada una sola vez.

## Gate F — transport

Carrier map frozen before second-carrier holdout.

## Gate G — attribution

Process-tensor and alternative-kernel nuisance tribunal.

## Authorized outcomes

- `PASS_FIRST_EMPIRICAL_CAUSAL_MODAL_CLOSURE`
- `PASS_DUAL_CARRIER_TRANSFER`
- `PASS_KERNEL_SELECTION`
- `FAIL_CAUSAL_COLOCALIZATION`
- `FAIL_CROSS_CARRIER_TRANSFER`
- `FAIL_STANDARD_RESPONSE_EXCLUSION`
- `ABSTAIN_INCOMPLETE_RECEIPTS`
- `HOLD_PHYSICAL_PROTOGEOMETRY`
