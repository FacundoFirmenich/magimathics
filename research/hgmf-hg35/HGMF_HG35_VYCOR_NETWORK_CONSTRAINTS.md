# HGMF-HG35 — Xe/Vycor standard network constraints

## Direct Brown benchmark

Mason (1988), Proc. R. Soc. A 415, 453–486, applied a cavity/window Bethe-tree network directly to A. J. Brown's Xe/Vycor scanning isotherms at 151 K.

The model is parameterized by:
- cavity-size distribution;
- window-size distribution;
- number of windows per cavity.

Mason reports that adsorption scans support the theory with some systematic residuals, while desorption scans are especially informative for extracting pore interconnectivity.

## Modernized percolation benchmark

Cimino et al. (2013), Colloids Surf. A 437, 76–89, formulate Bethe and 3D-cubic percolation models for scanning desorption.

For Vycor:
- two scanning curves gave effective coordination numbers z=6.6 and 7.2;
- Bethe qc values are approximately 0.18 and 0.16;
- a chosen z=6.6 produced good agreement with experimental scanning desorption, except the lowest scan.

This yields an externally frozen topology range:

z in [6.6,7.2],
qc in [0.1613,0.1786].

## Material-class constraints

Modern Vycor reviews report approximately:
- porosity ~28%;
- mean pore diameter ~50 Å;
- relatively narrow pore diameter distribution, often around ±10%;
- strongly interconnected void space.

These values characterize typical Vycor, not necessarily Brown's exact 61.6 mg specimen. They are sensitivity bounds, not exact sample parameters.

## Claim boundary

The topology/connectivity class is physically constrained. The remaining missing objects are the Brown-sample observation bridge Vs, Vc and q(p), not network existence itself.
