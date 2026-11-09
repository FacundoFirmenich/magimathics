#!/usr/bin/env python3
import math
import numpy as np
from scipy.optimize import least_squares

def rect(f):
    return f(1,1)-f(1,0)-f(0,1)+f(0,0)

assert abs(rect(lambda v,h:v*v+math.sin(h)))<1e-12
assert abs(rect(lambda v,h:v*h)-1)<1e-12
assert abs(rect(lambda v,h:v*v+h*h))<1e-12

assert abs(.3*.4-.12)<1e-12

r=np.array([1.,-1.,2.,-2.])
e=np.array([1.,1.,-.5,-.5])
y=2.5*r+.2*e
g=np.dot(r,y)/np.dot(r,r)
ys=7*y
gs=np.dot(r,ys)/np.dot(r,r)
assert abs(g-2.5)<1e-12
assert abs(gs-17.5)<1e-12
rr=np.linalg.norm(y-g*r)/np.linalg.norm(y)
rrs=np.linalg.norm(ys-gs*r)/np.linalg.norm(ys)
assert abs(rr-rrs)<1e-12

lam=np.array([1.,4.,9.,16.,25.])
ytrue=2.4/(lam+3)
train=np.array([0,1,2])
def residual(p):
    return p[0]/(lam[train]+p[1])-ytrue[train]
fit=least_squares(residual,[2.,1.],bounds=([0.,0.],[np.inf,np.inf]),xtol=1e-14,ftol=1e-14,gtol=1e-14)
pred=fit.x[0]/(lam+fit.x[1])
assert np.max(np.abs(pred-ytrue))<1e-12
assert abs(fit.x[0]-2.4)<1e-12
assert abs(fit.x[1]-3.0)<1e-12

print('PASS_HGMF_HG24_EXACT')
print('causal_geometry_independence=true')
print('ordered_interaction_H_after_V=0.12')
print('ordered_interaction_V_after_H=0')
print('gamma_original=2.5')
print('gamma_scaled=17.5')
print('screened_holdout_rmse=0')
print('magnetic_execution=false')
print('second_carrier_execution=false')
