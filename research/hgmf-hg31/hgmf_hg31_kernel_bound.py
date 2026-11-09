#!/usr/bin/env python3
from __future__ import annotations
import math
import numpy as np

def _q(kind,lam,source,eta=None):
    lam=np.asarray(lam,dtype=float); s=np.asarray(source,dtype=float)
    if np.any(lam<=0): raise ValueError("positive eigenvalues required")
    if kind=="identity": return s
    if kind=="green": return s/lam
    if kind=="screened": return s/(lam+float(eta))
    if kind=="fractional": return s*lam**(-float(eta))
    if kind=="heat": return s*np.exp(-float(eta)*lam)
    raise ValueError("unknown kernel")

def _profile_loglik(y,S,q):
    y=np.asarray(y,float); S=np.asarray(S,float); q=np.asarray(q,float)
    if S.shape!=(y.size,y.size) or q.shape!=y.shape: raise ValueError("shape")
    S=(S+S.T)/2
    sign,logdet=np.linalg.slogdet(S)
    if sign<=0: raise ValueError("kernel likelihood covariance must be positive definite")
    P=np.linalg.inv(S)
    b=float(q@P@q)
    if b<=0: raise ValueError("zero source direction")
    gamma=float(q@P@y/b)
    r=y-gamma*q
    ll=float(-0.5*(y.size*math.log(2*math.pi)+logdet+r@P@r))
    return ll,gamma

def exact_fixed_kernel_loglik_upper(kind,y,S,lam,source):
    if kind not in ("identity","green"): raise ValueError("fixed kernel only")
    ll,gamma=_profile_loglik(y,S,_q(kind,lam,source))
    return {"log_likelihood_upper_bound":ll,"profile_gamma":gamma,"method":"EXACT_PROFILE"}

def _lipschitz_bound(kind,y,S,lam,source,a,b):
    y=np.asarray(y,float); S=np.asarray(S,float); lam=np.asarray(lam,float); s=np.asarray(source,float)
    P=np.linalg.inv((S+S.T)/2)
    ev=np.linalg.eigvalsh(P)
    if ev[0]<=0: raise ValueError("positive definite covariance required")
    yn2=float(y@P@y)
    if kind=="screened":
        if a<0: raise ValueError("screened m2 lower bound must be >=0")
        minq=np.linalg.norm(s/(lam+b))
        maxdq=np.linalg.norm(s/(lam+a)**2)
    elif kind=="heat":
        if a<0: raise ValueError("heat tau lower bound must be >=0")
        minq=np.linalg.norm(s*np.exp(-b*lam))
        maxdq=np.linalg.norm(s*lam*np.exp(-a*lam))
    elif kind=="fractional":
        q2a=(s*lam**(-a))**2; q2b=(s*lam**(-b))**2
        minq=math.sqrt(float(np.sum(np.minimum(q2a,q2b))))
        d2a=(s*np.log(lam)*lam**(-a))**2
        d2b=(s*np.log(lam)*lam**(-b))**2
        maxdq=math.sqrt(float(np.sum(np.maximum(d2a,d2b))))
    else:
        raise ValueError("continuous kernel expected")
    if minq<=0: raise ValueError("source gives no uniform kernel direction")
    return yn2*math.sqrt(float(ev[-1]/ev[0]))*maxdq/minq

def certified_continuous_kernel_upper(kind,y,S,lam,source,eta_lo,eta_hi,log_slack=1e-3,max_grid_points=1000000,numeric_roundoff_slack=1e-10):
    """Mathematical upper bound using a global Lipschitz constant for profile log-likelihood.

    The theorem is exact; floating-point evaluation is conservative only to the declared
    numeric_roundoff_slack and is not interval-arithmetic certification.
    """
    a=float(eta_lo); b=float(eta_hi)
    if not (b>a): raise ValueError("nonempty compact parameter interval required")
    if log_slack<=0: raise ValueError("positive upper slack required")
    L=_lipschitz_bound(kind,y,S,lam,source,a,b)
    if L==0:
        n=2
    else:
        n=math.ceil(L*(b-a)/(2*log_slack))+1
    if n>max_grid_points:
        raise RuntimeError(f"required certified grid {n} exceeds cap {max_grid_points}")
    grid=np.linspace(a,b,n)
    best=-math.inf; best_eta=None; best_gamma=None
    for eta in grid:
        ll,gamma=_profile_loglik(y,S,_q(kind,lam,source,eta))
        if ll>best:
            best=ll; best_eta=float(eta); best_gamma=float(gamma)
    h=(b-a)/(n-1)
    upper=best+L*h/2+float(numeric_roundoff_slack)
    return {
      "log_likelihood_upper_bound":float(upper),
      "grid_max_loglik":float(best),
      "grid_best_eta":best_eta,
      "grid_profile_gamma":best_gamma,
      "lipschitz_constant":float(L),
      "grid_points":int(n),
      "mathematical_slack":float(L*h/2),
      "numeric_roundoff_slack":float(numeric_roundoff_slack),
      "method":"CERTIFIED_GRID_LIPSCHITZ_THEOREM_FLOATING_IMPLEMENTATION",
      "authority":"MATH_BOUND_MACHINE_INTERVAL_CERTIFICATION_PENDING"
    }
