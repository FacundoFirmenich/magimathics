# HGMF‑UMI‑16 — Counterbalanced Reset × Field × Cycle

## Objective

Identify a causal vector constitutive law while breaking the remaining field–history confounding.

## Gate A — factorial protocol

On the same device/sample:

- preset sign: `+`, `-`, `0`;
- at least three field amplitudes;
- at least five cycles;
- randomized field order;
- explicit reset between blocks;
- at least three independent replications per cell.

## Gate B — vector state

\[
\mathbf s=(A,B,C,K,E,Q).
\]

A scalar collapse is forbidden.

## Gate C — causal contrasts

Estimate separately:

- preset-sign effect;
- completed-loop effect;
- field effect;
- field×history interaction;
- reset restoration;
- sample/instrument drift.

## Gate D — frozen forecast

\[
\mathbf s_{t+1}\in\widehat{\mathcal U}(\mathbf s_t,u_t,r_t)
\]

must be frozen before observing cycle `t+1`.

## Gate E — grain and tails

Preserve every cycle, component and branch, together with q50/q90/q95/max, crossing completeness, uncertainty and abstention.

## Authorized outcomes

- `PASS_VECTOR_CONSTITUTIVE_LAW`
- `PASS_DISCRETE_ONLY`
- `FAIL_RESET_RESTORATION`
- `FAIL_FIELD_HISTORY_SEPARATION`
- `HOLD_REPLICATION`
