#!/usr/bin/env python3
from __future__ import annotations
import math
import numpy as np

def gaussian_log_density(y, mean, covariance):
    y=np.asarray(y,dtype=float); mu=np.asarray(mean,dtype=float); S=np.asarray(covariance,dtype=float)
    if y.shape!=mu.shape or S.shape!=(y.size,y.size):
        raise ValueError("shape mismatch")
    S=(S+S.T)/2
    sign,logdet=np.linalg.slogdet(S)
    if sign<=0:
        raise ValueError("candidate covariance must be positive definite under the declared observation measure")
    P=np.linalg.inv(S)
    r=y-mu
    return float(-0.5*(y.size*math.log(2*math.pi)+logdet+r@P@r))

def universal_union_evalue(log_candidate_density, family_log_upper_bounds):
    if not family_log_upper_bounds:
        raise ValueError("no nuisance upper bounds")
    vals={str(k):float(v) for k,v in family_log_upper_bounds.items()}
    if any(math.isnan(v) for v in vals.values()):
        raise ValueError("NaN likelihood bound")
    log_u=max(vals.values())
    log_e=float(log_candidate_density)-log_u
    threshold_log=math.log(140.0)
    if log_e>=0:
        p_value=math.exp(-log_e) if log_e<745 else 0.0
    else:
        p_value=1.0
    e_value=math.exp(log_e) if -745<log_e<709 else (math.inf if log_e>=709 else 0.0)
    return {
      "log_candidate_density":float(log_candidate_density),
      "family_log_upper_bounds":vals,
      "log_union_upper_bound":log_u,
      "log_e_value":log_e,
      "e_value":e_value,
      "p_value":min(1.0,p_value),
      "passes_alpha_over_7":bool(log_e>=threshold_log),
      "threshold_e_value":140.0,
      "threshold_log_e":threshold_log
    }

def replicate_universal_p(p_magnetism,p_adsorption):
    p1=float(p_magnetism); p2=float(p_adsorption)
    if not (0<=p1<=1 and 0<=p2<=1): raise ValueError("invalid p")
    return max(p1,p2)
