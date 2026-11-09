#!/usr/bin/env python3
import math
import numpy as np

tol=1e-12
gA=np.diag([1.0,4.0])
gB=np.diag([4.0,1.0])
area=lambda g: math.sqrt(np.linalg.det(g))
AA,AB,AAB=area(gA),area(gB),area(gA+gB)
assert abs(AA-2.0)<tol
assert abs(AB-2.0)<tol
assert abs(AAB-5.0)<tol
assert abs(AAB-(AA+AB)-1.0)<tol

for c in [0.0,1.0,-2.5]:
    lhs=c*AAB
    rhs=c*(AA+AB)
    if abs(c)<tol:
        assert abs(lhs-rhs)<tol
    else:
        assert abs(lhs-rhs)>tol

for m in range(-20,21):
    c=2*m
    val=c*math.sqrt(5)/2
    if abs(val-round(val))<tol:
        assert m==0

assert abs((2.0*math.pi)/(2*math.pi)-1.0)<tol
assert abs((2.0*math.pi*math.sqrt(5))/(2*math.pi)-math.sqrt(5))<tol
assert abs((2/math.sqrt(5))*math.pi/(2*math.pi)-1/math.sqrt(5))<tol

candidates=[math.pi/6,math.pi/18,4*math.pi/9,4*math.sqrt(math.pi)/3]
for c in candidates:
    assert abs(c/2-round(c/2))>1e-6

theta=np.linspace(0,math.pi,1000001)
integral=2*math.pi*np.trapz(np.cos(theta)*0.25*np.sin(theta),theta)
assert abs(integral)<1e-10

print("PASS_HGMF_HG20_EXACT")
print(f"area_A={AA}")
print(f"area_B={AB}")
print(f"area_composite={AAB}")
print(f"composition_defect={AAB-AA-AB}")
print("common_nonzero_topological_c=false")
print("same_bundle_constant_mode=excluded")
print(f"zero_flux_cos_theta_integral={integral}")
