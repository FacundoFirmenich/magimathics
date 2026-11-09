#!/usr/bin/env python3
import math
import numpy as np
from hgmf_hg30_covariance import validate_covariance, propagate_linear, vector_in_support
from hgmf_hg30_predictive import minimum_mc_draws

alpha=0.05/7
assert abs(alpha-1/140)<1e-15
assert minimum_mc_draws(alpha)==139

S=np.array([[1.0,0.25],[0.25,2.0]])
info=validate_covariance(S)
assert info["rank"]==2
D=np.array([[1.0,-1.0]])
Sd=propagate_linear(D,S)
assert abs(Sd[0,0]-2.5)<1e-15

Ss=np.array([[1.0,1.0],[1.0,1.0]])
assert validate_covariance(Ss)["rank"]==1
assert vector_in_support(np.array([2.0,2.0]),Ss)
assert not vector_in_support(np.array([1.0,-1.0]),Ss)

print("PASS_HGMF_HG30_EXACT")
print(f"alpha_component={alpha}")
print("minimum_mc_draws=139")
print("covariance_rank_full=2")
print("propagated_rectangle_variance=2.5")
print("singular_support_check=PASS")
print("empirical_outcomes_generated=false")
