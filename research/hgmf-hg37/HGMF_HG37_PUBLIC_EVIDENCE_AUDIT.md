# HGMF-HG37 — Public evidence audit

## FGT/CrSBr

Public source paper:
Kumar et al., Small 21, e06284 (2025), DOI 10.1002/smll.202506284.

Relevant published statements:
- magnetotransport was performed in a variable-temperature-insert cryostat capable of fields up to 12 T;
- AHE used a Keithley 6221 current source and Keithley 2182A nanovoltmeter;
- the approximately ±5 mT uncertainty reported for HEB corresponds to the magnetic-field step size used in the hysteresis measurements.

Public repository:
sadityakr/EB-in-FGT_CrSBr-vdW-heterostructure@66662e8aa3690cebaaef52dfc4ddd3bea458a576.

HDF5 metadata expose:
- Magnetic_Field unit = Ampere;
- Conversion_factor_AtoT = 0.08586;
- field orientation and sweep/wait settings.

The repository audit finds no independent:
- Hall-probe calibration;
- field-axis accuracy/uncertainty certificate;
- traceable field readback calibration receipt.

The conversion factor therefore cannot be assigned an uncertainty smaller than the published step bound without additional evidence.

## Brown Xe/Vycor

Public dataset:
NIST-ISODB/AJBrownThesisIsotherms@17a48e5d3c00e97387d0dfb1e280d8d6bf103d40.

Repository audit finds no:
- nonporous Xe/silica film-reference isotherm;
- FHH parameter set;
- independently calibrated surface area suitable to point-identify (V_s).

NIST documents that the digital release preserves the Brown dissertation tables and scanning isotherms.

## Alternative standard route

Mason, Proc. R. Soc. A 415, 453–486 (1988), DOI 10.1098/rspa.1988.0023:
- applied a Bethe-tree cavity/window network model directly to Brown Xe/Vycor scanning isotherms at 151 K;
- states that the correlation method does not require separating capillary condensation from surface adsorption;
- uses the desorption scans to infer cavity/window distributions and connectivity.

Thus the absence of a Cimino (V_s) reference does not exhaust standard network explanations.
