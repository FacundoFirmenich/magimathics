#!/usr/bin/env python3
import math
import numpy as np
from hgmf_hg35_bethe_network import bethe_primary, bethe_scan, qc_bethe

assert abs(qc_bethe(6.6)-1/5.6)<1e-15
assert abs(qc_bethe(7.2)-1/6.2)<1e-15
assert 0.1612 < qc_bethe(7.2) < 0.1614
assert 0.1785 < qc_bethe(6.6) < 0.1787

for z in (6.6,7.2):
    qc=qc_bethe(z)
    # Below threshold the minimal Bethe solution must give zero (numerically tiny) percolating fraction.
    for q in np.linspace(0,max(qc-1e-4,0),25):
        assert abs(bethe_primary(float(q),z)["Qp"]) < 1e-8
    for qp in (0.0,0.12,0.34):
        prev=-1.0
        for q in np.linspace(0,1,101):
            s=bethe_scan(float(q),qp,z)
            assert 0 <= s["alpha"] <= 1+1e-12
            assert qp-1e-12 <= s["Qminus"] <= 1+1e-12
            assert s["Qminus"]+1e-12 >= prev
            prev=s["Qminus"]

print("PASS_HGMF_HG35_EXACT")
print(f"qc_z6p6={qc_bethe(6.6)}")
print(f"qc_z7p2={qc_bethe(7.2)}")
print("bethe_primary_threshold=PASS")
print("bethe_scan_bounds_monotonicity=PASS")
print("empirical_hgmf_claim=false")
