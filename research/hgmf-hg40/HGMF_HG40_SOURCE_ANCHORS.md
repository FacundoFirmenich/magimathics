# HGMF‑HG40 — Source and literature anchors

## Magnetic carrier

- Public source repository: `sadityakr/EB-in-FGT_CrSBr-vdW-heterostructure`, pinned at commit `66662e8aa3690cebaaef52dfc4ddd3bea458a576`.
- The source analysis exposes coercive crossings, exchange bias, transition widths and the five-loop training series used by HG40.
- HG40 uses only common-affine-field invariants; it does not infer an absolute field calibration.

## Adsorption carrier

- Public source repository: `NIST-ISODB/AJBrownThesisIsotherms`, pinned at commit `17a48e5d3c00e97387d0dfb1e280d8d6bf103d40`.
- Run 1 contains five simple primary desorption scans at 150.73 K with distinct reversal pressures.
- HG40 compares histories only at common pressure and temperature, so the pointwise film and condensed references cancel algebraically.

## Formal anchors

- One-dimensional affine group actions remove two degrees from a labelled nondegenerate configuration.
- Preisach/return-point-memory no-passing and Bethe scanning monotonicity motivate the order tribunal.
- These anchors support quotient observables and standard-null criticism; they do not establish HGMF or physical protogeometry.
