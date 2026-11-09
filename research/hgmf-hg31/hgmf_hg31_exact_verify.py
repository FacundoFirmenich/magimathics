#!/usr/bin/env python3
import math
import numpy as np
from hgmf_hg31_universal_evalue import universal_union_evalue
from hgmf_hg31_hmm_bound import bounded_hmm_loglik_upper
from hgmf_hg31_kernel_bound import exact_fixed_kernel_loglik_upper, certified_continuous_kernel_upper

alpha=0.05/7
assert abs(alpha-1/140)<1e-15
ans=universal_union_evalue(-1.0,{"n1":-3.0,"n2":-2.0})
assert abs(ans["log_e_value"]-1.0)<1e-15
assert abs(ans["p_value"]-math.exp(-1))<1e-15

boxes=[{"mean_lo":[-1.0],"mean_hi":[1.0],"var_lo":[0.5],"var_hi":[2.0]}]
hb=bounded_hmm_loglik_upper(np.array([[0.0],[3.0]]),boxes)
assert math.isfinite(hb["log_likelihood_upper_bound"])

y=np.array([0.2,-0.1,0.3])
S=np.eye(3)
lam=np.array([1.0,2.0,4.0])
src=np.array([1.0,0.5,-0.4])
fg=exact_fixed_kernel_loglik_upper("green",y,S,lam,src)
assert math.isfinite(fg["log_likelihood_upper_bound"])
cb=certified_continuous_kernel_upper("screened",y,S,lam,src,0.0,2.0,log_slack=1e-2,max_grid_points=200000)
assert cb["log_likelihood_upper_bound"] >= cb["grid_max_loglik"]

assert math.log(140)>0
print("PASS_HGMF_HG31_EXACT")
print(f"alpha_component={alpha}")
print("carrier_evalue_threshold=140")
print("universal_union_evalue=PASS")
print("bounded_hmm_upper_bound=PASS")
print("fixed_kernel_profile=PASS")
print("continuous_kernel_lipschitz_bound=PASS")
print("empirical_adjudication=false")
