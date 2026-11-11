# HGMF‑HG44 — Conformational state machine

## States

### PROTOCOL_FROZEN_UNARMED

The sequential constitution exists, but HG43 has not supplied real receipts, density certificates and power certificates.

### ARMED_FUTURE_ONLY

All HG43 arming conditions pass. No holdout outcome has been accessed.

### ACQUIRING_EPOCH

One calibration/reference epoch is active. Every admitted outcome receives exactly one factor determined by the prior conformation.

### PAUSED_RECALIBRATION

Acquisition is paused by a preregistered trigger. No efficacy factor is produced while the epoch is quarantined.

### TERMINAL_PASS

The authorized claim crossed its threshold under the frozen claim semantics.

### TERMINAL_FAIL

A protocol-integrity condition failed or a forbidden rewrite/leakage occurred.

### TERMINAL_ABSTAIN

The process ended without authority for a pass or fail claim—for example, insufficient receipts, unresolved calibration or exhausted resources.

## Allowed transitions

- PROTOCOL_FROZEN_UNARMED -> ARMED_FUTURE_ONLY
- ARMED_FUTURE_ONLY -> ACQUIRING_EPOCH
- ACQUIRING_EPOCH -> PAUSED_RECALIBRATION
- PAUSED_RECALIBRATION -> ACQUIRING_EPOCH
- ACQUIRING_EPOCH -> TERMINAL_PASS
- ACQUIRING_EPOCH -> TERMINAL_ABSTAIN
- PAUSED_RECALIBRATION -> TERMINAL_ABSTAIN
- any nonterminal state -> TERMINAL_FAIL on integrity violation

## Forbidden transitions

- unarmed -> acquiring;
- terminal -> nonterminal;
- epoch j -> epoch j-1;
- rewriting an earlier conformation;
- deleting an earlier adverse factor;
- changing claim semantics after threshold inspection;
- recalibration that silently re-scores previous outcomes.

## Epoch invariant

A new epoch must have:

- a new epoch ID;
- calibration/reference receipt hashes;
- a conformation hash;
- an event hash linked to the previous event;
- a start timestamp later than the previous epoch close;
- no outcome admitted before the epoch was activated.
