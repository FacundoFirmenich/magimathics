#!/usr/bin/env python3
from __future__ import annotations
import numpy as np

def validate_covariance(S, symmetry_tol=1e-10, psd_tol=1e-10):
    S=np.asarray(S,dtype=float)
    if S.ndim!=2 or S.shape[0]!=S.shape[1]:
        raise ValueError("covariance must be square")
    asym=float(np.max(np.abs(S-S.T))) if S.size else 0.0
    if asym>symmetry_tol:
        raise ValueError(f"covariance asymmetry {asym}")
    S=(S+S.T)/2
    vals=np.linalg.eigvalsh(S)
    if vals[0] < -psd_tol:
        raise ValueError(f"covariance not PSD: lambda_min={vals[0]}")
    rank=int(np.sum(vals>psd_tol))
    return {"matrix":S,"rank":rank,"lambda_min":float(vals[0]),"lambda_max":float(vals[-1]),"asymmetry":asym}

def propagate_linear(A,S):
    A=np.asarray(A,dtype=float); S=np.asarray(S,dtype=float)
    return A@S@A.T

def pinv_psd(S, tol=1e-10):
    info=validate_covariance(S,psd_tol=tol)
    vals,vecs=np.linalg.eigh(info["matrix"])
    inv=np.zeros_like(vals)
    mask=vals>tol
    inv[mask]=1/vals[mask]
    return (vecs*inv)@vecs.T, int(mask.sum()), vecs[:,mask]

def vector_in_support(v,S,tol=1e-10):
    v=np.asarray(v,dtype=float)
    P,rank,U=pinv_psd(S,tol)
    if rank==0:
        return bool(np.linalg.norm(v)<=tol)
    proj=U@(U.T@v)
    return bool(np.linalg.norm(v-proj)<=tol*(1+np.linalg.norm(v)))
