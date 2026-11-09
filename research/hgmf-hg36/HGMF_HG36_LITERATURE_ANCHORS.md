# HGMF-HG36 — Literature anchors

## Vycor observation map

Cimino et al. (2013), Colloids and Surfaces A 437, 76–89:
- measured sorption volume is decomposed into film reference Vs, condensed-fluid reference Vc and unfilled-pore fraction Q;
- Vs is tied to a nonporous reference of the same origin / film model;
- Vc is extrapolated from the reversible upper desorption plateau;
- Bethe/percolation inversion then uses Q+ and Q- to infer q and connectivity.

## Brown source

NIST AJBrownThesisIsotherms:
- Xe on Vycor scanning isotherms around 151 K;
- boundary run 15 at 150.73 K;
- no external nonporous film-reference isotherm is included in the Brown repository.

## Magnetic source

Kumar et al. FGT/CrSBr public data:
- HDF5 files contain raw voltage arrays and field samples;
- source loader averages current-reversed voltage measurements and interpolates coercive crossings;
- the raw voltage sampling error is therefore separately auditable from field-axis discretization.

These anchors establish the observation-bridge requirements. They do not establish HGMF.
