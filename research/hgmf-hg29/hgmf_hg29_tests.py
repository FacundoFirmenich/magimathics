#!/usr/bin/env python3
"""HGMF-HG29 confirmatory test primitives.

No empirical data are embedded. All functions operate on externally supplied,
holdout-only summaries and training-frozen templates.
"""
from __future__ import annotations
import math
from typing import Iterable, Mapping
import numpy as np

def normal_sf(z: float) -> float:
    return 0.5 * math.erfc(float(z) / math.sqrt(2.0))

def _validate_p(p: float) -> float:
    p=float(p)
    if not (0.0 <= p <= 1.0):
        raise ValueError("p-value outside [0,1]")
    return p

def causal_projection_p(cell_estimates, cell_cov, rectangle_matrix, template):
    y=np.asarray(cell_estimates,dtype=float)
    S=np.asarray(cell_cov,dtype=float)
    D=np.asarray(rectangle_matrix,dtype=float)
    w=np.asarray(template,dtype=float)
    if S.shape!=(y.size,y.size): raise ValueError("cell covariance shape")
    if D.shape[1]!=y.size: raise ValueError("rectangle matrix shape")
    if w.shape!=(D.shape[0],): raise ValueError("template shape")
    if not np.allclose(S,S.T,atol=1e-10): raise ValueError("covariance not symmetric")
    I=D@y
    SI=D@S@D.T
    var=float(w@SI@w)
    if not math.isfinite(var) or var<=0: raise ValueError("nonpositive projection variance")
    z=float(w@I)/math.sqrt(var)
    return {"z":z,"p_value":normal_sf(z),"variance":var}

def modal_alignment_p(modal_estimates, modal_cov, prediction):
    m=np.asarray(modal_estimates,dtype=float)
    S=np.asarray(modal_cov,dtype=float)
    r=np.asarray(prediction,dtype=float)
    if m.shape!=r.shape: raise ValueError("modal/prediction shape")
    if S.shape!=(m.size,m.size): raise ValueError("modal covariance shape")
    if m.size<2: raise ValueError("at least two holdout modal blocks required")
    if not np.allclose(S,S.T,atol=1e-10): raise ValueError("covariance not symmetric")
    P=np.linalg.pinv(S,rcond=1e-12)
    if np.linalg.norm(S@P@r-r) > 1e-8*(1+np.linalg.norm(r)):
        raise ValueError("prediction outside covariance support")
    denom=float(r@P@r)
    if denom<=0: raise ValueError("nonpositive modal information")
    z=float(r@P@m)/math.sqrt(denom)
    gamma=float(r@P@m)/denom
    resid=m-gamma*r
    q=float(resid@P@resid)
    return {"z":z,"p_value":normal_sf(z),"gamma_diagnostic":gamma,"residual_q_diagnostic":q}

def nodal_bracket_iut(estimates, standard_errors, expected_signs):
    x=np.asarray(estimates,dtype=float)
    se=np.asarray(standard_errors,dtype=float)
    s=np.asarray(expected_signs,dtype=float)
    if not (x.shape==se.shape==s.shape): raise ValueError("nodal arrays shape")
    if x.size<2 or x.size%2: raise ValueError("nodal flanks must come in pairs")
    if np.any(se<=0): raise ValueError("nonpositive nodal SE")
    if not np.all(np.isin(s,[-1.0,1.0])): raise ValueError("expected signs must be +/-1")
    ps=[normal_sf(float(si*xi/sei)) for xi,sei,si in zip(x,se,s)]
    return {"flank_pvalues":ps,"p_value":max(ps)}

def nuisance_union_iut(family_pvalues: Mapping[str,float], required_ids: Iterable[str]):
    required=list(required_ids)
    missing=[k for k in required if k not in family_pvalues or family_pvalues[k] is None]
    if missing:
        raise ValueError("missing nuisance families: "+",".join(missing))
    ps={k:_validate_p(family_pvalues[k]) for k in required}
    return {"family_pvalues":ps,"p_value":max(ps.values())}

def order_sign_test(positive: int, negative: int, ties: int=0):
    if min(positive,negative,ties)<0: raise ValueError("negative count")
    n=positive+negative
    if n==0: raise ValueError("no non-tied pairs")
    tail=sum(math.comb(n,k) for k in range(positive,n+1))/(2**n)
    return {"n_non_tied":n,"positive":positive,"negative":negative,"ties":ties,"p_value":tail}

def replication_p(p_magnetism: float, p_adsorption: float):
    return max(_validate_p(p_magnetism),_validate_p(p_adsorption))
