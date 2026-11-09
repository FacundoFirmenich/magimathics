#!/usr/bin/env python3
from __future__ import annotations
import math
import numpy as np
from scipy.stats import chi2, f as f_dist
from hgmf_hg30_covariance import pinv_psd, vector_in_support

def gaussian_mahalanobis_p(observed, mean, covariance, tol=1e-10):
    y=np.asarray(observed,dtype=float); mu=np.asarray(mean,dtype=float); S=np.asarray(covariance,dtype=float)
    if y.shape!=mu.shape: raise ValueError("shape mismatch")
    resid=y-mu
    P,rank,_=pinv_psd(S,tol)
    if rank==0: raise ValueError("zero-rank predictive covariance")
    if not vector_in_support(resid,S,tol): raise ValueError("residual outside covariance support")
    q=float(resid@P@resid)
    return {"q":q,"df":rank,"p_value":float(chi2.sf(q,rank))}

def exact_linear_predictive_f_p(residual, V, s2, df_train):
    e=np.asarray(residual,dtype=float); V=np.asarray(V,dtype=float)
    if s2<=0 or df_train<=0: raise ValueError("invalid training variance/df")
    P,rank,_=pinv_psd(V,1e-12)
    if rank!=e.size: raise ValueError("predictive V must be full rank")
    q=float(e@P@e)
    F=q/(e.size*s2)
    return {"F":F,"df1":e.size,"df2":int(df_train),"p_value":float(f_dist.sf(F,e.size,df_train))}

def monte_carlo_rank_p(T_obs, T_sim):
    sims=np.asarray(T_sim,dtype=float)
    if sims.ndim!=1 or sims.size<1: raise ValueError("need simulations")
    ge=int(np.sum(sims>=float(T_obs)))
    return {"B":int(sims.size),"exceedances":ge,"p_value":(1+ge)/(1+sims.size),"resolution":1/(1+sims.size)}

def minimum_mc_draws(alpha):
    if not 0<alpha<1: raise ValueError("alpha")
    return max(1,math.ceil(1/alpha)-1)
