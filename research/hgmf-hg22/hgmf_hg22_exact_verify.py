#!/usr/bin/env python3
import math
import numpy as np

beta=1/18
gamma=7/5

def f(x,y,z):
    return gamma*((z*z-y*y)/6 + beta*z/2)

roots=np.roots([12,1,-6])
assert np.allclose(sorted(roots),[-3/4,2/3],atol=1e-14)
for z in [-3/4,2/3]:
    y=math.sqrt(1-z*z)
    assert abs(f(0,y,z))<1e-14

obs=f(0,1,0)
unit=(-1/6)
gfit=obs/unit
assert abs(gfit-gamma)<1e-14

ks=[(1,1),(1/8,1/24),(1/16,1/32),(1/math.sqrt(8),1/math.sqrt(24)),(math.exp(-.24),math.exp(-.72))]
rootsets=[]
for k1,k2 in ks:
    r=beta*k1/k2
    rootsets.append(tuple(np.round(np.sort(np.roots([2,r,-1])),12)))
assert len(set(rootsets))==len(rootsets)

for x in np.linspace(0,2*math.pi,17,endpoint=False):
    for y in np.linspace(0,2*math.pi,19,endpoint=False):
        sA=math.cos(x)*math.cos(y)
        sB=math.sin(x)*math.sin(y)
        sint=-math.cos(x)*math.sin(y)-math.sin(x)*math.cos(y)
        stot=math.cos(x-y)-math.sin(x+y)
        assert abs(sA+sB+sint-stot)<1e-13

print('PASS_HGMF_HG22_EXACT')
print('nodes_z=-0.75,0.6666666666666666')
print(f'gamma_fit={gfit}')
print(f'kernel_node_sets={rootsets}')
print('composition_identity=true')
print('physical_source_fields_selected=false')
print('general_kernel_unique=false')
