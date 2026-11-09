# Dual-update protocol

Every scientific advance is persisted twice, without duplicating evidence.

## 1. Specialized repository first

The authoritative repository receives:

- code and exact outcomes;
- proofs or certificates;
- checker results;
- claim-ledger changes;
- manuscript changes;
- the next frozen gate.

The specialized commit is merged and its immutable SHA is recorded.

## 2. Magimathics second

`magimathics` receives only a compact programme receipt containing:

- repository and immutable commit;
- gate and status;
- claims changed;
- next gate;
- release or DOI, when one exists;
- cross-project consequences.

## Transaction order

1. close and verify the specialized gate;
2. merge the specialized commit;
3. capture the exact SHA;
4. update the corresponding `projects/*/POINTER.json`;
5. update registries and portfolio tables in one Magimathics commit.

`magimathics` never becomes an alternative source of mutable scientific evidence.
