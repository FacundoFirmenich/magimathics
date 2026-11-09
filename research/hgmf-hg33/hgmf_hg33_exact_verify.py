#!/usr/bin/env python3
import math
import numpy as np
from hgmf_hg33_preisach_outer import (
    threshold_representatives,
    relay_pattern,
    enumerate_unique_relay_patterns,
    preisach_outer_design,
    gaussian_outer_loglik_upper,
)

def key(p):
    return np.ascontiguousarray(p,dtype=np.int8).tobytes()

# 1. Exact finite-pattern coverage on an algebraic path.
x=np.array([-1.0,-0.2,0.7,1.0,0.4,-0.6,0.1,0.8])
enum=enumerate_unique_relay_patterns(x)
keys={key(enum["patterns"][:,j]) for j in range(enum["patterns"].shape[1])}
rng=np.random.default_rng(20261109)
for _ in range(500):
    a=float(rng.uniform(-3,3))
    b=float(rng.uniform(-3,3))
    if a<b:
        a,b=b,a
    for init in (-1.0,1.0):
        p=relay_pattern(x,a,b,init)
        assert key(p) in keys

# 2. Strictly monotone path saturates the unrestricted relay span.
xm=np.linspace(-1,1,12)
dm=preisach_outer_design(xm,reversible_degree=0)
assert dm["rank"]==len(xm)
assert dm["saturated"]

# 3. Generic single-reversal path also saturates in this exact finite-path construction.
xr=np.concatenate([np.linspace(-1,1,7),np.linspace(0.85,-0.9,6)])
dr=preisach_outer_design(xr,reversible_degree=0)
assert dr["rank"]==len(xr)
assert dr["saturated"]

# 4. Outer likelihood dominates the likelihood at a physical relay-mixture mean.
X=preisach_outer_design(x,reversible_degree=0)["X"]
beta=np.zeros(X.shape[1])
beta[0]=0.3
if X.shape[1]>3:
    beta[1]=0.8
    beta[2]=0.4
mu=X@beta
noise=np.array([0.02,-0.03,0.01,0.0,-0.01,0.02,-0.02,0.01])
y=mu+noise
S=np.diag(np.linspace(0.05,0.12,len(x))**2)
outer=gaussian_outer_loglik_upper(y,S,X)
P=np.linalg.inv(S)
sign,logdet=np.linalg.slogdet(S)
ll_at_physical=float(-0.5*(len(x)*math.log(2*math.pi)+logdet+(y-mu)@P@(y-mu)))
assert outer["log_likelihood_upper_bound"]+1e-10>=ll_at_physical

print("PASS_HGMF_HG33_EXACT")
print(f"finite_path_unique_patterns={enum['n_patterns']}")
print("random_threshold_pattern_coverage=PASS")
print(f"monotone_rank={dm['rank']}/{len(xm)}")
print(f"single_reversal_rank={dr['rank']}/{len(xr)}")
print("single_path_preisach_power_nogo=PASS")
print("outer_likelihood_dominance=PASS")
print("empirical_adjudication=false")
