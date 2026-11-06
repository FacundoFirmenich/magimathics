# SC43-M — Device plan

Frozen 2026-11-06 before QPU acquisition.

## Primary

`openquantum:ionq:qpu:forte-1`

- IonQ Forte 1 via OpenQuantum;
- 36 trapped-ion qubits;
- fully connected;
- QASM2/QASM3;
- 100–5000 shots/job;
- direct access;
- listed qBraid price at freeze: 0 credits.

Chosen because controlled swaps and nonlocal controls make connectivity strategically important.

## Secondary

`openquantum:aqt:qpu:ibex-q1`

- 12 trapped-ion qubits;
- fully connected;
- QASM2/QASM3;
- 1–2000 shots/job;
- exactly fits the 12-qubit reference circuit.

## Comparator

`openquantum:iqm:qpu:garnet`

- 20 superconducting qubits;
- clipped square-lattice;
- live calibration read at freeze: median readout error ~0.0234, median CZ error ~0.00421.

The topology implies additional routing for the present all-to-all logical circuit.
