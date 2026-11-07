# HGMF‑UMI‑17 — Minimal Counterbalanced Bridge Experiment

## Objective

Close the pairwise causal model with the smallest rank-complete design before committing to the full 135-loop factorial.

## Design A — saturated bridge

- 29 unique cells total;
- 7 legacy support cells;
- 22 new cells from `HGMF_UMI16_MINIMUM_RANK_COMPLETION_DESIGN.csv`;
- three independent replicates per selected cell;
- randomized block order;
- explicit reset before each cell;
- same device.

Total: 87 loop blocks, nominally 77 new if legacy runs are accepted.

## Design B — full protocol

\[
3\times3\times5\times3=135
\]

loop blocks.

## Mandatory state

\[
\mathbf s=(A,B,C,K,E,Q,Z).
\]

## Primary causal contrasts

- preset;
- field;
- cycle;
- preset×field;
- preset×cycle;
- field×cycle.

## Hard rules

- no global mean verdict;
- preserve every component and tail;
- predeclare resolution and crossing gates;
- randomize field order;
- block by reset and time;
- `ABSTAIN` for incomplete switching;
- no three-way claim from Design A.

## Authorized outcomes

- `PASS_PAIRWISE_VECTOR_LAW`
- `PASS_DISCRETE_ONLY`
- `FAIL_RESET_RESTORATION`
- `FAIL_FIELD_HISTORY_SEPARATION`
- `HOLD_REPLICATION`
