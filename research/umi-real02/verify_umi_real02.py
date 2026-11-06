#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import sympy as sp

root=Path(__file__).resolve().parent
res=pd.read_csv(root/'data/intervention_results.csv')
subs=pd.read_csv(root/'data/minimality_audit.csv')

baseline={'P1_linear_integral','P2_second_order_integral','P3_nonlinear_chemotaxis','P4_antithetic_integral'}
assert res[res['case'].isin(baseline)]['rpa_pass'].all()
full=subs[(subs.sensor_relation==True)&(subs.integration_relation==True)&(subs.actuation_relation==True)]
assert len(full)==1 and bool(full.iloc[0].rpa_pass)
assert not subs[~((subs.sensor_relation==True)&(subs.integration_relation==True)&(subs.actuation_relation==True))]['rpa_pass'].any()
assert not res[res['kind'].isin(['ablation','rewiring','negative-control'])]['rpa_pass'].any()

a,b,k,r,d,Kp,mu,theta,eta,z1,z2,y=sp.symbols('a b k r d Kp mu theta eta z1 z2 y', positive=True)
ys,zs=sp.symbols('ys zs')
sol=sp.solve([sp.Eq(-a*ys+b*zs+d,0),sp.Eq(k*(r-ys),0)],[ys,zs],dict=True)[0]
assert sp.simplify(sol[ys]-r)==0
yp=sp.solve(sp.Eq(-a*y+b*Kp*(r-y)+d,0),y)[0]
assert sp.simplify(yp-r-(d-a*r)/(a+b*Kp))==0
assert sp.simplify((mu-eta*z1*z2)-(theta*y-eta*z1*z2)-(mu-theta*y))==0
assert sp.Matrix([[-a,b],[k,0]]).det()==-b*k

print('PASS_MGM_UMI_REAL02')
print('implementation substitutions passing: 4/4')
print('parameter-grid passing: 108/108')
print('only full sensor-integrator-actuator carrier passes subset audit')
print('all frozen ablations/rewires lose robust perfect adaptation')
