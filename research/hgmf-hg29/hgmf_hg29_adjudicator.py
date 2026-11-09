#!/usr/bin/env python3
"""HGMF-HG29 machine adjudicator.

Consumes only already-computed holdout p-values/counts. It does not fit models,
impute missing values, select carriers, or alter the confirmatory graph.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path

COMPONENTS=("A","B","C","K","E","Q","Z")
ALPHA=0.05/7
REQUIRED_NUISANCE=(
    "drift_control",
    "finite_hidden_state",
    "bounded_process_tensor",
    "alternative_standard_kernels",
    "hidden_ancilla_control_geometry",
)
CLAIMS={
    0:"NO_CONFIRMATORY_COMPONENT_CLAIM",
    1:"DUAL_CARRIER_CAUSAL_COMPONENT",
    2:"DUAL_CARRIER_MODAL_TRANSFER",
    3:"DUAL_CARRIER_NODAL_TRANSFER",
    4:"CANDIDATE_OUTSIDE_FROZEN_STANDARD_NUISANCE_ENVELOPE",
    5:"ORDER_SENSITIVE_CANDIDATE_OUTSIDE_FROZEN_NUISANCE_ENVELOPE",
}

def valid_p(x):
    if x is None: return None
    x=float(x)
    if not 0<=x<=1: raise ValueError("invalid p")
    return x

def replicated_node(node):
    vals=[]
    for carrier in ("magnetism","adsorption"):
        z=node.get(carrier)
        if not z or not z.get("holdout_only",False): return None,"ABSTAIN_NOT_HOLDOUT"
        p=valid_p(z.get("p_value"))
        if p is None: return None,"ABSTAIN_MISSING_P"
        if not z.get("direction_concordant",False): p=1.0
        vals.append(p)
    return max(vals),"OK"

def nuisance_carrier(z):
    if not z or not z.get("holdout_only",False): return None,"ABSTAIN_NOT_HOLDOUT"
    fp=z.get("family_pvalues",{})
    missing=[k for k in REQUIRED_NUISANCE if fp.get(k) is None]
    if missing: return None,"ABSTAIN_NUISANCE_ENVELOPE_INCOMPLETE"
    ps=[valid_p(fp[k]) for k in REQUIRED_NUISANCE]
    return max(ps),"OK"

def nuisance_rep(node):
    ps=[]
    for carrier in ("magnetism","adsorption"):
        p,status=nuisance_carrier(node.get(carrier))
        if status!="OK": return None,status
        ps.append(p)
    return max(ps),"OK"

def sign_p(z):
    if not z or not z.get("holdout_only",False): return None,"ABSTAIN_NOT_HOLDOUT"
    pos=int(z.get("positive",0)); neg=int(z.get("negative",0)); ties=int(z.get("ties",0))
    n=pos+neg
    if n==0:return None,"ABSTAIN_NO_ORDER_PAIRS"
    p=sum(math.comb(n,k) for k in range(pos,n+1))/(2**n)
    return p,"OK"

def order_rep(node):
    if node is None: return None,"OPTIONAL_NOT_RUN"
    ps=[]
    for carrier in ("magnetism","adsorption"):
        p,status=sign_p(node.get(carrier))
        if status!="OK": return None,status
        ps.append(p)
    return max(ps),"OK"

def adjudicate_component(c):
    out={"nodes":{},"highest_level":0,"claim":CLAIMS[0]}
    chain=(("C","causal",replicated_node),("M","modal",replicated_node),("N","nodal",replicated_node),("X","nuisance",nuisance_rep))
    for level,(label,key,fn) in enumerate(chain,1):
        p,status=fn(c.get(key,{}))
        passed=(status=="OK" and p<=ALPHA)
        out["nodes"][label]={"p_rep":p,"status":status,"pass":passed}
        if not passed:
            out["stop_node"]=label
            return out
        out["highest_level"]=level; out["claim"]=CLAIMS[level]
    p,status=order_rep(c.get("order"))
    passed=(status=="OK" and p<=ALPHA)
    out["nodes"]["O"]={"p_rep":p,"status":status,"pass":passed}
    if passed:
        out["highest_level"]=5; out["claim"]=CLAIMS[5]
    return out

def adjudicate(doc):
    if doc.get("profile")!="hgmf-hg29-confirmatory-input/1.0": raise ValueError("profile")
    comps=doc.get("components",{})
    missing=[x for x in COMPONENTS if x not in comps]
    if missing: raise ValueError("missing components: "+",".join(missing))
    results={k:adjudicate_component(comps[k]) for k in COMPONENTS}
    levels={k:v["highest_level"] for k,v in results.items()}
    multi={}
    for level in range(1,6):
        names=[k for k,v in levels.items() if v>=level]
        multi[str(level)]=names
    return {
      "profile":"hgmf-hg29-adjudication/1.0",
      "alpha_global":0.05,
      "alpha_component":ALPHA,
      "components":results,
      "multicomponent_levels":multi,
      "physical_protogeometry_confirmed":False
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("input",type=Path)
    ap.add_argument("--output",type=Path)
    a=ap.parse_args()
    doc=json.loads(a.input.read_text(encoding="utf-8"))
    ans=adjudicate(doc)
    txt=json.dumps(ans,indent=2,sort_keys=True)+"\n"
    if a.output:a.output.write_text(txt,encoding="utf-8")
    print(txt,end="")

if __name__=="__main__":
    main()
