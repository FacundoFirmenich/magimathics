#!/usr/bin/env python3
from __future__ import annotations
import math
import numpy as np

def threshold_representatives(x):
    x=np.asarray(x,dtype=float)
    if x.ndim!=1 or x.size<1 or not np.all(np.isfinite(x)):
        raise ValueError("finite 1D input required")
    u=np.unique(x)
    if u.size==1:
        delta=max(1.0,abs(float(u[0]))+1.0)
        return np.array([u[0]-delta,u[0],u[0]+delta],dtype=float)
    mids=(u[:-1]+u[1:])/2
    span=float(u[-1]-u[0])
    delta=max(1.0,span)
    reps=np.concatenate([[u[0]-delta],u,mids,[u[-1]+delta]])
    return np.unique(reps)

def relay_pattern(x,alpha,beta,initial_state):
    if alpha < beta:
        raise ValueError("require alpha>=beta")
    if initial_state not in (-1.0,1.0,-1,1):
        raise ValueError("initial_state must be +/-1")
    x=np.asarray(x,dtype=float)
    state=float(initial_state)
    out=np.empty(x.size,dtype=float)
    for t,xt in enumerate(x):
        if xt>=alpha:
            state=1.0
        elif xt<=beta:
            state=-1.0
        out[t]=state
    return out

def enumerate_unique_relay_patterns(x, include_zero_width=True):
    x=np.asarray(x,dtype=float)
    reps=threshold_representatives(x)
    seen={}
    for a in reps:
        for b in reps:
            if include_zero_width:
                ok=a>=b
            else:
                ok=a>b
            if not ok:
                continue
            for init in (-1.0,1.0):
                p=relay_pattern(x,float(a),float(b),init)
                key=np.ascontiguousarray(p,dtype=np.int8).tobytes()
                if key not in seen:
                    seen[key]=p
    pats=np.column_stack(list(seen.values())) if seen else np.empty((x.size,0))
    return {
      "representatives":reps,
      "patterns":pats,
      "n_representatives":int(reps.size),
      "n_patterns":int(pats.shape[1])
    }

def preisach_outer_design(x,reversible_degree=1,include_zero_width=True):
    x=np.asarray(x,dtype=float)
    enum=enumerate_unique_relay_patterns(x,include_zero_width=include_zero_width)
    cols=[np.ones_like(x)]
    if reversible_degree<0:
        raise ValueError("reversible_degree must be >=0")
    if reversible_degree:
        xc=(x-np.mean(x))
        scale=np.std(xc)
        if scale<=0:
            scale=1.0
        z=xc/scale
        for d in range(1,reversible_degree+1):
            cols.append(z**d)
    if enum["patterns"].shape[1]:
        cols.extend([enum["patterns"][:,j] for j in range(enum["patterns"].shape[1])])
    X=np.column_stack(cols)
    return {
      "X":X,
      "rank":int(np.linalg.matrix_rank(X)),
      "n_obs":int(x.size),
      "n_columns":int(X.shape[1]),
      "n_relay_patterns":enum["n_patterns"],
      "n_threshold_representatives":enum["n_representatives"],
      "saturated":bool(np.linalg.matrix_rank(X)>=x.size),
      "reversible_degree":int(reversible_degree)
    }

def gaussian_outer_loglik_upper(y,covariance,X):
    y=np.asarray(y,dtype=float)
    S=np.asarray(covariance,dtype=float)
    X=np.asarray(X,dtype=float)
    n=y.size
    if S.shape!=(n,n) or X.shape[0]!=n:
        raise ValueError("shape mismatch")
    S=(S+S.T)/2
    sign,logdet=np.linalg.slogdet(S)
    if sign<=0:
        raise ValueError("positive definite covariance required for density")
    P=np.linalg.inv(S)
    G=X.T@P@X
    beta=np.linalg.pinv(G,rcond=1e-12)@(X.T@P@y)
    resid=y-X@beta
    q=float(resid@P@resid)
    ll=float(-0.5*(n*math.log(2*math.pi)+logdet+q))
    rank=int(np.linalg.matrix_rank(X))
    return {
      "log_likelihood_upper_bound":ll,
      "gls_beta":beta,
      "residual_q":q,
      "design_rank":rank,
      "n_obs":n,
      "saturated":bool(rank>=n),
      "authority":"EXACT_OUTER_SPAN_PROFILE"
    }

def finite_path_preisach_upper(x,y,covariance,reversible_degree=1):
    d=preisach_outer_design(x,reversible_degree=reversible_degree)
    ans=gaussian_outer_loglik_upper(y,covariance,d["X"])
    ans.update({
      "n_relay_patterns":d["n_relay_patterns"],
      "n_threshold_representatives":d["n_threshold_representatives"],
      "n_columns":d["n_columns"],
      "reversible_degree":reversible_degree,
      "status":"ABSTAIN_PREISACH_OUTER_BOUND_SATURATED" if ans["saturated"] else "CERTIFIED_PREISACH_OUTER_BOUND"
    })
    return ans
