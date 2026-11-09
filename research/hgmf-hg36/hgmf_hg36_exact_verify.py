#!/usr/bin/env python3
import json, math
from pathlib import Path
import numpy as np
from scipy.optimize import brentq

ROOT=Path(__file__).resolve().parent
GEN=ROOT/"generated"
mag=json.loads((GEN/"HGMF_HG36_MAGNETIC_RAW_BOOTSTRAP.json").read_text())
vy=json.loads((GEN/"HGMF_HG36_VYCOR_BRIDGE_RESULTS.json").read_text())

assert mag["status"]=="PASS_HGMF_HG36_RAW_VOLTAGE_BOOTSTRAP_EXECUTED"
assert len(mag["loops"])==5
assert all(x["bootstrap_B_valid"]==5000 for x in mag["loops"])
assert all(x["raw_structure"]["raw_samples_per_source_row"]==5 for x in mag["loops"])
assert all(abs(x["abs_HEB_difference_raw_vs_source_mT"])<1e-15 for x in mag["loops"])

# Raw voltage noise is strictly positive but much smaller than one acquisition field step.
sds=[x["bootstrap_sd_HEB_mT"] for x in mag["loops"]]
assert all(0 < x < 0.02 for x in sds)

trained=[x["observed_source_avg"]["heb"] for x in mag["loops"][1:]]
field_step=4.2932274337233025
assert all(abs(x)<=field_step+1e-12 for x in trained)

# Profile-no-go construction: under mu=0 and |delta|<=Delta, choose delta=h_obs.
residuals=[h-h for h in trained]
assert max(abs(x) for x in residuals)==0.0

assert vy["status"]=="PASS_HGMF_HG36_SET_VALUED_REFERENCE_IDENTIFIABILITY_AUDIT"
assert vy["Vs_external_reference_available"] is False
assert vy["reference_identifiability"]=="FAIL_POINT_IDENTIFICATION_WITH_BROWN_DATA_ALONE"
assert vy["Q_points"]==614
assert vy["run1_q_points"]==89
assert 0 < vy["Q_median_interval_width"] < 1
assert 0 < vy["q_median_interval_width"] < 1

# Algebraic Bethe inverse check.
def scan_alpha(q,Qp,z):
    def f(y):
        return (1-q)+q*(1-Qp)*y**(z-1)-y
    y=brentq(f,0.0,1.0,xtol=1e-14,rtol=1e-14)
    return 1-y**z

def invert_q(Qp,Qm,z):
    alpha=(Qm-Qp)/(1-Qp)
    y=(1-alpha)**(1/z)
    return (1-y)/(1-(1-Qp)*y**(z-1))

Qp=0.2; q0=0.35; z=6.6
alpha=scan_alpha(q0,Qp,z)
Qm=Qp+(1-Qp)*alpha
q1=invert_q(Qp,Qm,z)
assert abs(q1-q0)<1e-12

print("PASS_HGMF_HG36_EXACT")
print("raw_voltage_bootstrap=PASS")
print(f"max_bootstrap_sd_HEB_mT={max(sds)}")
print("trained_HEB_within_field_step_bound=PASS")
print("HEB_summary_profile_residual=0")
print(f"Q_points={vy['Q_points']}")
print(f"Q_median_width={vy['Q_median_interval_width']}")
print(f"q_points={vy['run1_q_points']}")
print(f"q_median_width={vy['q_median_interval_width']}")
print("bethe_q_inversion=PASS")
print("carrier_specific_universal_evalue_ready=false")
print("physical_protogeometry=HOLD")
