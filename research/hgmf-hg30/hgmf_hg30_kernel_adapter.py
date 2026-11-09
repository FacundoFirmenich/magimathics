#!/usr/bin/env python3
from __future__ import annotations
import numpy as np
from scipy.optimize import least_squares
from hgmf_hg30_predictive import gaussian_mahalanobis_p
from hgmf_hg30_covariance import pinv_psd

def kappa(kind, lam, theta=None):
    lam=np.asarray(lam,dtype=float)
    if np.any(lam<=0): raise ValueError("positive eigenvalues required")
    theta=[] if theta is None else list(theta)
    if kind=="identity": return np.ones_like(lam)
    if kind=="green": return 1/lam
    if kind=="screened":
        if len(theta)!=1 or theta[0]<0: raise ValueError("screened m2>=0")
        return 1/(lam+theta[0])
    if kind=="fractional":
        if len(theta)!=1 or theta[0]<=0: raise ValueError("fractional alpha>0")
        return lam**(-theta[0])
    if kind=="heat":
        if len(theta)!=1 or theta[0]<0: raise ValueError("heat tau>=0")
        return np.exp(-theta[0]*lam)
    raise ValueError("unknown kernel")

def _bounds(kind):
    if kind in ("identity","green"): return [],([],[])
    if kind=="screened": return [1.0],([0.0],[np.inf])
    if kind=="fractional": return [1.0],([1e-8],[np.inf])
    if kind=="heat": return [0.01],([0.0],[np.inf])
    raise ValueError(kind)

def fit_kernel(kind, lam, source, response, covariance):
    lam=np.asarray(lam,float); s=np.asarray(source,float); y=np.asarray(response,float); S=np.asarray(covariance,float)
    if not (lam.shape==s.shape==y.shape): raise ValueError("shape")
    P,rank,U=pinv_psd(S,1e-12)
    if rank<1: raise ValueError("no covariance support")
    W=(U/np.sqrt(np.maximum(np.linalg.eigvalsh(U.T@S@U),1e-300)))@U.T if rank==len(y) else None
    # use eigen whitening robustly
    vals,vecs=np.linalg.eigh((S+S.T)/2)
    mask=vals>1e-12
    L=(vecs[:,mask]/np.sqrt(vals[mask])).T
    init_shape,bounds_shape=_bounds(kind)
    x0=np.array([1.0]+init_shape,dtype=float)
    lb=np.array([-np.inf]+list(bounds_shape[0]),dtype=float)
    ub=np.array([ np.inf]+list(bounds_shape[1]),dtype=float)
    def pred(x):
        return x[0]*kappa(kind,lam,x[1:])*s
    def resid(x):
        return L@(y-pred(x))
    fit=least_squares(resid,x0,bounds=(lb,ub),jac="2-point")
    p=len(fit.x); df=max(0,rank-p)
    JTJ=fit.jac.T@fit.jac
    cov_theta=np.linalg.pinv(JTJ,rcond=1e-12)
    if df>0:
        cov_theta*=float(np.sum(fit.fun**2)/df)
    return {"kind":kind,"params":fit.x,"param_cov":cov_theta,"df":df,"cost":float(np.sum(fit.fun**2))}

def predict_kernel(fit, lam_hold, source_hold, measurement_cov):
    lam=np.asarray(lam_hold,float); s=np.asarray(source_hold,float); Sm=np.asarray(measurement_cov,float)
    x=np.asarray(fit["params"],float)
    mean=x[0]*kappa(fit["kind"],lam,x[1:])*s
    eps=1e-6
    J=np.zeros((len(lam),len(x)))
    for j in range(len(x)):
        d=eps*(1+abs(x[j])); xp=x.copy(); xm=x.copy(); xp[j]+=d; xm[j]-=d
        if j>0 and xm[j]<0: xm[j]=x[j]
        mp=xp[0]*kappa(fit["kind"],lam,xp[1:])*s
        mm=xm[0]*kappa(fit["kind"],lam,xm[1:])*s
        den=xp[j]-xm[j]
        J[:,j]=(mp-mm)/den if den else 0
    Sp=Sm+J@fit["param_cov"]@J.T
    return {"mean":mean,"covariance":Sp,"calibration_authority":"ASYMPTOTIC_THEOREM_PENDING_REGIME_AUDIT"}

def holdout_check(prediction, observed):
    ans=gaussian_mahalanobis_p(observed,prediction["mean"],prediction["covariance"])
    ans["calibration_authority"]=prediction["calibration_authority"]
    return ans
