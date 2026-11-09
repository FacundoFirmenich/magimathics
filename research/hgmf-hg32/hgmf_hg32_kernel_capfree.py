#!/usr/bin/env python3
from __future__ import annotations
import math
import numpy as np

def _q(kind,lam,s,eta):
    lam=np.asarray(lam,float); s=np.asarray(s,float)
    if kind=="screened": return s/(lam+eta)
    if kind=="fractional": return s*lam**(-eta)
    if kind=="heat": return s*np.exp(-eta*lam)
    raise ValueError(kind)

def _profile_ll(y,S,q):
    y=np.asarray(y,float); S=np.asarray(S,float); q=np.asarray(q,float)
    P=np.linalg.inv((S+S.T)/2)
    sign,logdet=np.linalg.slogdet(S)
    if sign<=0: raise ValueError("positive definite covariance required")
    b=float(q@P@q)
    if b<=0: raise ValueError("zero direction")
    gamma=float(q@P@y/b)
    r=y-gamma*q
    ll=float(-0.5*(y.size*math.log(2*math.pi)+logdet+r@P@r))
    return ll,gamma

def _finite_lipschitz(kind,y,S,lam,s,a,b):
    y=np.asarray(y,float); S=np.asarray(S,float); lam=np.asarray(lam,float); s=np.asarray(s,float)
    P=np.linalg.inv((S+S.T)/2)
    ev=np.linalg.eigvalsh(P)
    if ev[0]<=0: raise ValueError("positive definite precision required")
    yn2=float(y@P@y)
    if kind=="screened":
        minq=np.linalg.norm(s/(lam+b))
        maxdq=np.linalg.norm(s/(lam+a)**2)
    elif kind=="heat":
        minq=np.linalg.norm(s*np.exp(-b*lam))
        maxdq=np.linalg.norm(s*lam*np.exp(-a*lam))
    elif kind=="fractional":
        q2a=(s*lam**(-a))**2; q2b=(s*lam**(-b))**2
        minq=math.sqrt(float(np.sum(np.minimum(q2a,q2b))))
        d2a=(s*np.log(lam)*lam**(-a))**2
        d2b=(s*np.log(lam)*lam**(-b))**2
        maxdq=math.sqrt(float(np.sum(np.maximum(d2a,d2b))))
    else: raise ValueError(kind)
    if minq<=0: raise ValueError("no source support")
    return yn2*math.sqrt(float(ev[-1]/ev[0]))*maxdq/minq

def finite_interval_upper(kind,y,S,lam,s,a,b,log_slack=1e-3,max_grid_points=1000000,roundoff_slack=1e-10):
    L=_finite_lipschitz(kind,y,S,lam,s,a,b)
    n=2 if L==0 else math.ceil(L*(b-a)/(2*log_slack))+1
    if n>max_grid_points: raise RuntimeError(f"grid cap exceeded: {n}")
    grid=np.linspace(a,b,n)
    best=-math.inf
    for eta in grid:
        ll,_=_profile_ll(y,S,_q(kind,lam,s,float(eta)))
        if ll>best: best=ll
    h=(b-a)/(n-1)
    return {"upper":float(best+L*h/2+roundoff_slack),"grid_max":float(best),"L":float(L),"n":int(n),"slack":float(L*h/2+roundoff_slack)}

def _tail_limit(kind,lam,s):
    lam=np.asarray(lam,float); s=np.asarray(s,float)
    if kind=="screened":
        return s.copy(), None, None
    mask=np.abs(s)>0
    if not np.any(mask): raise ValueError("zero source")
    l0=float(np.min(lam[mask]))
    minmask=mask & np.isclose(lam,l0,rtol=1e-12,atol=1e-15)
    qlim=np.where(minmask,s,0.0)
    rest=mask & ~minmask
    if not np.any(rest):
        return qlim,l0,None
    if kind=="heat":
        gap=float(np.min(lam[rest]-l0))
        return qlim,l0,gap
    if kind=="fractional":
        rho=float(np.max(l0/lam[rest]))
        return qlim,l0,rho
    raise ValueError(kind)

def tail_profile_upper(kind,y,S,lam,s,M):
    y=np.asarray(y,float); S=np.asarray(S,float); lam=np.asarray(lam,float); s=np.asarray(s,float)
    P=np.linalg.inv((S+S.T)/2)
    ev=np.linalg.eigvalsh(P)
    pmin,pmax=float(ev[0]),float(ev[-1])
    if pmin<=0: raise ValueError("precision not PD")
    qlim,l0,param=_tail_limit(kind,lam,s)
    nlim=math.sqrt(float(qlim@P@qlim))
    if nlim<=0: raise ValueError("zero limit direction")
    if kind=="screened":
        d=math.sqrt(pmax)*float(np.linalg.norm(s*lam))/M
    elif kind=="heat":
        if param is None: d=0.0
        else:
            rest=~np.isclose(lam,l0,rtol=1e-12,atol=1e-15)
            d=math.sqrt(pmax)*float(np.linalg.norm(s[rest]))*math.exp(-M*param)
    elif kind=="fractional":
        if param is None: d=0.0
        else:
            rest=~np.isclose(lam,l0,rtol=1e-12,atol=1e-15)
            d=math.sqrt(pmax)*float(np.linalg.norm(s[rest]))*(param**M)
    else: raise ValueError(kind)
    if d>=nlim:
        return {"usable":False,"direction_bound":math.inf,"profile_slack":math.inf}
    dirb=2*d/(nlim-d)
    yn2=float(y@P@y)
    ll0,_=_profile_ll(y,S,qlim)
    return {"usable":True,"direction_bound":float(dirb),"profile_slack":float(yn2*dirb),"limit_loglik":float(ll0),"upper":float(ll0+yn2*dirb)}

def cap_free_profile_upper(kind,y,S,lam,s,finite_log_slack=1e-3,tail_log_slack=1e-3,max_M=1e12,max_grid_points=1000000):
    M=1.0
    while True:
        t=tail_profile_upper(kind,y,S,lam,s,M)
        if t["usable"] and t["profile_slack"]<=tail_log_slack:
            break
        M*=2
        if M>max_M: raise RuntimeError("tail compactification failed")
    f=finite_interval_upper(kind,y,S,lam,s,0.0,M,log_slack=finite_log_slack,max_grid_points=max_grid_points)
    return {
      "log_likelihood_upper_bound":float(max(f["upper"],t["upper"])),
      "finite_upper":f,
      "tail_upper":t,
      "tail_start":M,
      "parameter_domain":"[0,infinity] with projective endpoint",
      "authority":"MATHEMATICAL_CAP_FREE_BOUND_FLOATING_INTERVAL_CERT_PENDING"
    }
