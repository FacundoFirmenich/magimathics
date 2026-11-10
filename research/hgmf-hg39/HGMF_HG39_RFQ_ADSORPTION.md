# HGMF‑HG39 — Adsorption reference commissioning request specification

## Custom measurement capability

1. Confirm Xe measurement at the preregistered temperature and pressure domain.
2. Confirm a matched nonporous silica film reference.
3. Confirm same Xe lot, pretreatment, pressure system and thermal protocol.
4. Confirm interleaved `REFERENCE → SAMPLE → REFERENCE` scheduling.
5. Confirm full raw-data delivery.

## Metrology

6. Pressure calibration chain, range and uncertainty.
7. Temperature calibration chain, stability, gradients and uncertainty.
8. Mass result and uncertainty.
9. Surface-area result and uncertainty.
10. Dead-volume and buoyancy corrections.
11. equilibrium criterion and timeout policy.
12. blank/leak tests.

## Required outputs

13. `Vs(p,T)` on the entire scanning domain.
14. `Vc(p,T)` on the entire scanning domain.
15. covariance across curves and between reference/sample blocks.
16. drift/interleaving analysis.
17. machine-readable receipt and hashes.

## Instrument validation

A BET or controlled-pore reference material may be used to validate instrument performance, but it may not replace the matched nonporous scientific reference.
