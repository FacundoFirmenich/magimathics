# SC43-M — Material Hyperaccess Qualification

**Jurisdiction:** `HX-Q4-SIGN`  
**Parent:** `SC43-HXG`  
**Status:** `MATERIAL_PROTOCOL_FROZEN / QPU_SUBMISSION_AWAITING_EXPLICIT_CONFIRMATION`

## Material witness

The hardware-minimal program replaces the full 17-outcome CP4 program by a pair-only SWAP-parity postselection that preserves exactly

[
Pr(C=pm1mid A)=rac{1pmmu^2}{2}.
]

For (a=4/13,b=1/13):

[
q_{m pair}=rac{24}{169},qquad
s_F=rac{193}{208},qquad
q_{m pair}s_F=rac{579}{4394}.
]

The material design point is frozen at

[
oxed{mu_M=0.31}.
]

At this point:

[
P_{m marginal}=P(0.31^3)=rac{36151873}{48250000}approx0.7492616166<rac34,
]

[
P_{m enriched}=P(0.31)=rac{14797}{19300}approx0.7666839378>rac34,
]

[
E[C]=0.31^2=0.0961 < rac1{24(0.31)}=rac{25}{186}.
]

## Circuit

Reference implementation: 12 qubits.

- two 2-qubit auxiliary Q4 registers;
- one 2-qubit main Q4 register;
- three purification qubits;
- SWAP-parity sign ancilla;
- filter-acceptance ancilla;
- one reusable workspace.

The sign/output relation is preserved coherently. The marginal arm applies the instrument sign action and erases its use; the enriched arm uses the recorded sign again before the inverse-QFT4 phase reader.

All eight (mu=0.31) QASM2 circuits validate through qBraid. Pre-transpilation depth: 52–58; logical gate count: 78–99.

## Independent statevector receipt

For every phase (n=0,1,2,3):

```text
program acceptance      = 0.142011834319525
filter acceptance       = 0.927884615384616
combined acceptance     = 0.131770596267638
branch mean E[C]        = 0.096100000000003
marginal phase success  = 0.749261616580311
enriched phase success  = 0.766683937823834
```

The cubic phase targets are (3nmod4=(0,3,2,1)).

## Binding sequential evidence

Familywise (alpha=0.05), split (0.025+0.025); each promotion e-value threshold is 40.

1. Enriched accepted outputs: test (H_0:ple3/4) against fixed (p_1=P(0.31)).
2. Program-sign events: test (H_0:E[C]ge25/186) against fixed (E[C]=0.0961).

A first cohort is frozen as 60,000 raw shots: 40,000 enriched and 20,000 marginal.

## Frozen device cohort

Primary: `openquantum:ionq:qpu:forte-1` — 36-qubit trapped-ion, fully connected, QASM2/QASM3, 100–5000 shots/job.

Secondary: `openquantum:aqt:qpu:ibex-q1` — 12-qubit trapped-ion, fully connected, QASM2/QASM3, 1–2000 shots/job.

No QPU job has yet been submitted.

```text
SC43_M_CIRCUIT_COMPILED  = PASS
SC43_M_QASM_VALIDATED    = PASS
SC43_M_IDEAL_REPLAY      = PASS_INDEPENDENT_QBRAID
SC43_M_STATISTICS_FROZEN = PASS
SC43_M_DEVICE_SELECTED   = PASS
SC43_M_QPU_SUBMISSION    = AWAITING_EXPLICIT_CONFIRMATION
```
