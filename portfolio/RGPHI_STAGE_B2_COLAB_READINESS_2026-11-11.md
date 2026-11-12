# RGΦ Stage B2 — Drive/Colab readiness

Google Drive storage has been restored and a persistent Stage-B2 execution surface now exists. The exact runner, full checkpoint validator, smoke tests, deterministic test and a Colab notebook with production disabled by default are archived in the canonical RGΦ repository.

## Ready

- Drive base, checkpoint, work, receipt and notebook folders;
- canonical 128-bucket hash manifest;
- exact C++/Python external-memory engine;
- full structural validator;
- exact `185→186` pilot mode;
- transactional restart semantics.

## Still blocked

The exact raw Stage-A frontier at time 185 has not been located in Drive or Library:

- 2,462,600,671 states;
- 128 buckets;
- 19,700,805,368 bytes;
- manifest SHA-256 `dbd2f4adda52315e05261b9328c03f8a44d2a31b8e293f3dd3ff7b80b3d2a6b7`.

The historical depth-85 checkpoint found in custody is valid historical evidence but is not a substitute and is explicitly rejected as Stage-B2 input.

## Authority

The canonical interval remains `186 <= tau5 <= 212`. Storage readiness and notebook deployment do not change any scientific claim. Production becomes admissible only after all 128 hashes and full structural checks pass.
