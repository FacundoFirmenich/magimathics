#!/usr/bin/env python3
from __future__ import annotations
import math
import numpy as np

def gaussian_noise_floor_logsup(R):
    R=np.asarray(R,dtype=float)
    if R.ndim!=2 or R.shape[0]!=R.shape[1]:
        raise ValueError("R must be square")
    R=(R+R.T)/2
    sign,logdet=np.linalg.slogdet(R)
    if sign<=0:
        raise ValueError("noise floor must be positive definite")
    d=R.shape[0]
    return float(-0.5*(d*math.log(2*math.pi)+logdet))

def hmm_noise_floor_loglik_upper(noise_floor_covariances):
    vals=[gaussian_noise_floor_logsup(R) for R in noise_floor_covariances]
    if not vals:
        raise ValueError("need at least one observation")
    return {
      "log_likelihood_upper_bound":float(sum(vals)),
      "per_time_log_upper_bounds":vals,
      "method":"MEASUREMENT_NOISE_FLOOR_ENVELOPE",
      "valid_for":"arbitrary means, arbitrary stochastic transitions, arbitrary K"
    }

def saturated_state_count_nogo(T:int,Kmax:int|None):
    if T<1: raise ValueError("T")
    if Kmax is None:
        return {"saturated_possible":True,"reason":"unbounded K permits one state per holdout observation"}
    if Kmax<1: raise ValueError("Kmax")
    return {"saturated_possible":bool(Kmax>=T),"reason":"K>=T can allocate one deterministic state per holdout time"}
