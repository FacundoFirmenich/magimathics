#!/usr/bin/env python3
from __future__ import annotations
import math
import numpy as np

def scalar_gaussian_logsup(x, mu_lo, mu_hi, var_lo, var_hi):
    x=float(x); mu_lo=float(mu_lo); mu_hi=float(mu_hi)
    var_lo=float(var_lo); var_hi=float(var_hi)
    if mu_hi<mu_lo or var_lo<=0 or var_hi<var_lo:
        raise ValueError("invalid emission cap")
    if x<mu_lo: d=mu_lo-x
    elif x>mu_hi: d=x-mu_hi
    else: d=0.0
    vstar=min(max(d*d,var_lo),var_hi)
    return -0.5*(math.log(2*math.pi*vstar)+(d*d)/vstar)

def state_emission_logsup(x, state_box):
    x=np.asarray(x,dtype=float)
    lo=np.asarray(state_box["mean_lo"],dtype=float)
    hi=np.asarray(state_box["mean_hi"],dtype=float)
    vlo=np.asarray(state_box["var_lo"],dtype=float)
    vhi=np.asarray(state_box["var_hi"],dtype=float)
    if not (x.shape==lo.shape==hi.shape==vlo.shape==vhi.shape):
        raise ValueError("state box dimension mismatch")
    return float(sum(scalar_gaussian_logsup(xi,a,b,c,d) for xi,a,b,c,d in zip(x,lo,hi,vlo,vhi)))

def bounded_hmm_loglik_upper(X_holdout, state_boxes):
    """Pointwise likelihood upper bound for any HMM whose states respect state_boxes.

    Transition and initial probabilities may be arbitrary stochastic matrices/vectors.
    The bound follows because every path emission product is bounded by the product
    of per-time maximum emission densities, while path probabilities sum to one.
    """
    X=np.asarray(X_holdout,dtype=float)
    if X.ndim==1: X=X[:,None]
    if not state_boxes:
        raise ValueError("at least one bounded state box required")
    total=0.0
    for x in X:
        total += max(state_emission_logsup(x,b) for b in state_boxes)
    return {
      "log_likelihood_upper_bound":float(total),
      "method":"ANALYTIC_EMISSION_ENVELOPE",
      "authority":"CERTIFIED_MATHEMATICAL_BOUND",
      "power_note":"bound ignores transition consistency and may be conservative"
    }
