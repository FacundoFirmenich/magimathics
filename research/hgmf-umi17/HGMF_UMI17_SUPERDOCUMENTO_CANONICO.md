# HGMF‑UMI‑17 — Sequentially Admissible Robust Bridge

**Date:** 8 November 2026  
**Authority:** `EXACT DESIGN / SEQUENTIAL EXECUTABILITY / ANTI-AGGREGATION`  
**Verdict:** `PASS_DESIGN_CLOSURE / RECOMMEND_99_LOOP_ROBUST_BRIDGE / HOLD_EXPERIMENTAL_EXECUTION`

## 0. Central correction

The previous 22-cell augmentation treated cycle-specific observations as independently executable treatment cells. They are not.

If cycle \(k\) represents the \(k\)-th consecutive hysteresis loop after reset, then observing cycle \(k\) requires:

\[
1\to2\to\cdots\to k.
\]

The design must therefore be prefix-closed within every preset–field block.

The UMI‑16 matrix had 29 unique rows and full algebraic rank, but its physical sequential closure contains 41 cells. With three replicates, its executable cost is 123 loop blocks, not 87.

## 1. Sequential lower-bound theorem

The pairwise model has 29 parameters. Preset×field requires all nine preset-field combinations at cycle 1. For each nonbaseline cycle, the incremental parameter block has dimension five: intercept plus two preset and two field contrasts. Therefore at least five preset-field blocks must continue to each of cycles 2–5.

\[
N\ge9+4(5)=29.
\]

The bound is attainable. Exactly 81 five-block subsets possess the required additive rank.

\[
\boxed{N_{\min}^{\rm sequential}=29.}
\]

## 2. Saturated bridge

A condition-optimal saturated representative continues the five blocks

\[
\{(-,200),(0,100),(0,150),(0,200),(+,200)\}
\]

through cycle 5, while all nine blocks contribute cycle 1.

- 29 cells;
- rank 29;
- 87 loop blocks with three waves;
- zero cell-mean lack-of-fit degrees of freedom;
- no robustness to losing one cycle-2–5 continuation block.

## 3. Recommended robust bridge

The six long blocks are

\[
\{(-,100),(-,150),(0,100),(0,200),(+,150),(+,200)\}.
\]

The omitted long blocks

\[
\{(-,200),(0,150),(+,100)\}
\]

form one permutation diagonal. Every preset and field appears in exactly two long blocks.

- 33 unique cells;
- 99 loop blocks;
- four cell-mean lack-of-fit degrees of freedom;
- rank 29 after removing cycles 2–5 from any one selected long block;
- condition number 8.707 versus 11.783 for the saturated bridge;
- minimum normalized information eigenvalue 0.01369 versus 0.00824.

There are six symmetry-equivalent balanced robust bridges.

## 4. Executable cost

| Design | Executable cells | Three-wave loops | New loops using legacy |
|---|---:|---:|---:|
| UMI‑16 after prefix closure | 41 | 123 | 118 |
| saturated UMI‑17 | 29 | 87 | 80 |
| robust UMI‑17 | 33 | 99 | 93 |
| full factorial | 45 | 135 | 130 |

The robust bridge adds 12 loops over the saturated design and saves 36 relative to the full factorial.

## 5. Experimental unit

The unit is a reset-defined preset–field block:

- short block: reset + cycle 1;
- long block: reset + cycles 1–5 consecutively.

Cycles cannot be randomized inside a block. The frozen three-wave schedule includes every preset-field combination in each wave, with six long and three short blocks.

## 6. Analysis contract

The state remains

\[
\mathbf s=(A,B,C,K,E,Q,Z).
\]

- retain every replicate;
- never collapse the vector to a scalar mean;
- score HEB/coercivity only when two crossings exist;
- otherwise return `ABSTAIN` for those components while retaining span, area, crossing count and noise;
- validate by leaving one complete wave out;
- preserve cells, components and tails;
- no three-way claim.

## 7. Verdict

```text
PASS_SEQUENTIAL_ADMISSIBILITY_THEOREM
PASS_EXACT_29_CELL_LOWER_BOUND
PASS_SATURATED_PREFIX_CLOSED_BRIDGE
PASS_ONE_CONTINUATION_BLOCK_ROBUST_BRIDGE
PASS_COUNTERBALANCED_EXECUTION_SCHEDULE
PASS_EXACT_COST_CORRECTION

FAIL_UMI16_CELLWISE_EXECUTABILITY
HOLD_EMPIRICAL_PAIRWISE_VECTOR_LAW
```

Paper A is now `DESIGN_COMPLETE / EMPIRICAL_EXECUTION_PENDING`. The next active gate advances Paper B while the experiment remains pending.
