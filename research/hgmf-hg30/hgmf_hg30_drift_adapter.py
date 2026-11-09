#!/usr/bin/env python3
from __future__ import annotations
import numpy as np
from hgmf_hg30_predictive import exact_linear_predictive_f_p

def fit_linear_gaussian(X_train,y_train):
    X=np.asarray(X_train,dtype=float); y=np.asarray(y_train,dtype=float)
    if X.ndim!=2 or y.ndim!=1 or X.shape[0]!=y.size: raise ValueError("shape")
    n,p=X.shape
    if n<=p: raise ValueError("training df <= 0")
    XtX=X.T@X
    if np.linalg.matrix_rank(XtX)<p: raise ValueError("rank deficient training design")
    XtX_inv=np.linalg.inv(XtX)
    beta=XtX_inv@X.T@y
    resid=y-X@beta
    df=n-p
    s2=float(resid@resid/df)
    if s2<=0: raise ValueError("zero training variance")
    return {"beta":beta,"XtX_inv":XtX_inv,"s2":s2,"df":df,"n":n,"p":p}

def predictive_check(fit,X_holdout,y_holdout):
    Xh=np.asarray(X_holdout,dtype=float); yh=np.asarray(y_holdout,dtype=float)
    if Xh.ndim!=2 or yh.ndim!=1 or Xh.shape[0]!=yh.size: raise ValueError("shape")
    if Xh.shape[1]!=fit["p"]: raise ValueError("design columns")
    mean=Xh@fit["beta"]
    V=np.eye(yh.size)+Xh@fit["XtX_inv"]@Xh.T
    ans=exact_linear_predictive_f_p(yh-mean,V,fit["s2"],fit["df"])
    ans.update({"predictive_mean":mean,"relative_covariance":V,"calibration_authority":"EXACT_FINITE_SAMPLE"})
    return ans
