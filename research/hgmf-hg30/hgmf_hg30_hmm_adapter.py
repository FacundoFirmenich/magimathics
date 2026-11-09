#!/usr/bin/env python3
from __future__ import annotations
import numpy as np
from scipy.special import logsumexp
from hgmf_hg30_predictive import monte_carlo_rank_p

def _elog(X,means,vars_):
    X=np.asarray(X,float)
    if X.ndim==1: X=X[:,None]
    return -0.5*np.sum(np.log(2*np.pi*vars_[None,:,:])+(X[:,None,:]-means[None,:,:])**2/vars_[None,:,:],axis=2)

def _fb(X,pi,A,means,vars_):
    logB=_elog(X,means,vars_); T,K=logB.shape
    la=np.empty((T,K)); la[0]=np.log(pi+1e-300)+logB[0]
    for t in range(1,T):
        la[t]=logB[t]+logsumexp(la[t-1][:,None]+np.log(A+1e-300),axis=0)
    ll=float(logsumexp(la[-1]))
    lb=np.zeros((T,K))
    for t in range(T-2,-1,-1):
        lb[t]=logsumexp(np.log(A+1e-300)+logB[t+1][None,:]+lb[t+1][None,:],axis=1)
    lg=la+lb-ll; gamma=np.exp(lg)
    xi=np.empty((max(0,T-1),K,K))
    for t in range(T-1):
        z=la[t][:,None]+np.log(A+1e-300)+logB[t+1][None,:]+lb[t+1][None,:]-ll
        xi[t]=np.exp(z)
    filt=np.exp(la[-1]-logsumexp(la[-1]))
    return ll,gamma,xi,filt

def fit_gaussian_hmm(X,K,max_iter=200,tol=1e-7,var_floor=1e-6,seed=0):
    X=np.asarray(X,float)
    if X.ndim==1:X=X[:,None]
    T,d=X.shape
    if not (1<=K<T): raise ValueError("K must be bounded and < training length")
    rng=np.random.default_rng(seed)
    idx=np.linspace(0,T-1,K,dtype=int)
    means=X[idx].copy()
    base=np.var(X,axis=0)+var_floor
    vars_=np.tile(base,(K,1))
    A=np.full((K,K),1/K); pi=np.full(K,1/K)
    old=-np.inf
    for it in range(max_iter):
        ll,gamma,xi,_=_fb(X,pi,A,means,vars_)
        w=gamma.sum(axis=0)+1e-12
        pi=gamma[0]+1e-12; pi/=pi.sum()
        if T>1:
            A=xi.sum(axis=0)+1e-12
            A/=A.sum(axis=1,keepdims=True)
        means=(gamma.T@X)/w[:,None]
        for k in range(K):
            diff=X-means[k]
            vars_[k]=(gamma[:,k,None]*(diff**2)).sum(axis=0)/w[k]
        vars_=np.maximum(vars_,var_floor)
        if ll-old < tol*(1+abs(ll)) and ll>=old: break
        old=ll
    ll,gamma,xi,filt=_fb(X,pi,A,means,vars_)
    return {"K":K,"pi":pi,"A":A,"means":means,"vars":vars_,"train_loglik":ll,"last_filter":filt,"iterations":it+1,"calibration_authority":"UNPROVEN_FAMILY_LEVEL"}

def predictive_loglik(model,Xh):
    Xh=np.asarray(Xh,float)
    if Xh.ndim==1:Xh=Xh[:,None]
    prior=model["last_filter"]@model["A"]
    logB=_elog(Xh,model["means"],model["vars"])
    la=np.log(prior+1e-300)+logB[0]
    for t in range(1,len(Xh)):
        la=logB[t]+logsumexp(la[:,None]+np.log(model["A"]+1e-300),axis=0)
    return float(logsumexp(la))

def sample_predictive(model,T,B,seed=0):
    rng=np.random.default_rng(seed); K=model["K"]; d=model["means"].shape[1]
    out=np.empty((B,T,d))
    start=model["last_filter"]@model["A"]
    for b in range(B):
        z=rng.choice(K,p=start)
        for t in range(T):
            out[b,t]=rng.normal(model["means"][z],np.sqrt(model["vars"][z]))
            if t<T-1:z=rng.choice(K,p=model["A"][z])
    return out

def frozen_predictive_check(model,Xh,B=999,seed=0):
    obs=-predictive_loglik(model,Xh)
    sims=sample_predictive(model,len(Xh),B,seed)
    Tsim=np.array([-predictive_loglik(model,s) for s in sims])
    ans=monte_carlo_rank_p(obs,Tsim)
    ans.update({"T_obs":obs,"calibration_authority":"FROZEN_PREDICTIVE_ONLY_NOT_FAMILY_CONFIRMATORY"})
    return ans
