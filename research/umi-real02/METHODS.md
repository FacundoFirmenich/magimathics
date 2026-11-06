# MGM-UMI-REAL-02 — Frozen methods

## Jurisdiction

Function: robust perfect adaptation (RPA) to constant disturbances or references.

Admissible systems:
- finite-dimensional deterministic closed loops;
- stable equilibrium after a persistent step;
- visible transient response before adaptation;
- feedback/internal-memory branch.

This jurisdiction does not claim to cover every feedforward RPA topology.

## Frozen semantic signature

A run passes when:
1. the step creates a detectable output deviation;
2. terminal deviation from the pre-step output is below 10^-3 of peak deviation;
3. the trajectory remains bounded and reaches a terminal regime.

## Critical relations

- `S`: regulated output -> sensor/error;
- `I`: error -> persistent integrator memory;
- `A`: memory -> corrective plant actuation.

All 2^3 relation subsets are tested.

## Substitutions

- first-order LTI plant;
- second-order LTI plant;
- nonlinear chemotaxis-like loop;
- antithetic integral feedback.

A deterministic 108-case grid varies plant decay, actuation gain, integral gain and disturbance magnitude.

## Frozen rewires

- feedback sign flip;
- sensor moved from output to disturbance;
- output dependence replaced by a constant source;
- proportional-only control.

## Evidence hierarchy

- `P1`: direct experiment;
- `P2`: physical intervention/mutant;
- `P3`: distinct physical substrate;
- `M1`: explicit mechanistic model;
- `T1`: exact theorem.

Model counterfactuals are never presented as empirical data.

## Software

Python 3.13.5; NumPy 2.3.5; SciPy 1.17.0; pandas 2.2.3; SymPy 1.14.0; LSODA with rtol 1e-10 and atol 1e-12.
