#!/usr/bin/env python3
import math
import numpy as np
from hgmf_hg32_jurisdiction import quantum_process_tensor_current_carrier, OUT
from hgmf_hg32_hmm_noise_floor import hmm_noise_floor_loglik_upper, saturated_state_count_nogo
from hgmf_hg32_power import required_log_e, required_average_log_advantage
from hgmf_hg32_kernel_capfree import cap_free_profile_upper, _profile_ll, _q

assert quantum_process_tensor_current_carrier(False,False)==OUT
assert abs(required_log_e()-math.log(140))<1e-15
assert abs(required_average_log_advantage(24)-math.log(140)/24)<1e-15

R=np.eye(2)
hb=hmm_noise_floor_loglik_upper([R,R])
assert abs(hb["log_likelihood_upper_bound"]+2*math.log(2*math.pi))<1e-12
assert saturated_state_count_nogo(24,24)["saturated_possible"]
assert not saturated_state_count_nogo(24,3)["saturated_possible"]

y=np.array([0.2,-0.1,0.3])
S=np.eye(3)
lam=np.array([1.0,2.0,4.0])
src=np.array([1.0,0.5,-0.4])

for kind in ("screened","fractional","heat"):
    b=cap_free_profile_upper(kind,y,S,lam,src,finite_log_slack=1e-2,tail_log_slack=1e-2,max_grid_points=300000)
    M=b["tail_start"]
    if kind=="screened":
        grid=np.concatenate([np.linspace(0,M,4000),np.geomspace(max(M,1e-6),1e6,4000)])
    else:
        grid=np.concatenate([np.linspace(0,M,4000),np.linspace(M,M+40,4000)])
    sampled=max(_profile_ll(y,S,_q(kind,lam,src,float(x)))[0] for x in grid)
    assert b["log_likelihood_upper_bound"]+1e-10>=sampled

print("PASS_HGMF_HG32_EXACT")
print("observable_jurisdiction=PASS")
print("quantum_process_tensor_current_carriers=OUT_OF_JURISDICTION_AS_DISTINCT_NULL")
print("kernel_cap_free_projective_bounds=PASS")
print("hmm_noise_floor_bound=PASS")
print("saturated_hmm_power_nogo=PASS")
print(f"log_e_threshold={math.log(140)}")
print(f"zero_slack_nats_per_cell={math.log(140)/24}")
print("carrier_specific_registry_complete=false")
print("empirical_adjudication=false")
