# HGMF‑HG44 — Recalibration and epoch contract

## Trigger classes

A recalibration trigger must be frozen before the outcome it governs. Examples include:

- elapsed-time limit;
- temperature excursion;
- reference residual outside a frozen confidence sequence;
- ancestry break;
- instrument replacement;
- calibration expiration;
- predeclared drift threshold.

## Transition

When a trigger fires:

1. close the current epoch;
2. preserve all prior factors and hashes;
3. enter PAUSED_RECALIBRATION;
4. acquire and validate a new calibration/reference receipt;
5. create a new conformation for future observations;
6. resume only after the new epoch is activated.

## Quarantine

Observations collected while no valid epoch exists receive no evidential interpretation.

The safe default is:

e_t = 1.

This neutralization must follow a trigger and interval rule that was fixed before observing the affected outcome. A result-dependent choice to quarantine only adverse observations is forbidden.

## Evidence continuity

Let M_tau be the capital at the epoch boundary. The new epoch starts from M_tau, not from one.

Resetting to one would discard past evidence; choosing the larger of the reset and continued capital would manufacture evidence.

## Null-family updates

- adding a standard competitor is conservative and may occur for future factors;
- removing a competitor requires a predeclared independent rule and cannot re-score the past;
- if the null changes so materially that the old and new claims are not comparable, terminate the old process and begin a separately labelled process. Their capitals cannot be multiplied without a conditional bridge proof.
