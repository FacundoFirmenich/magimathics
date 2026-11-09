#!/usr/bin/env python3
"""HGMF-HG26 receipt validator. Standard library only."""
from __future__ import annotations
import argparse, json, hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict, deque

HEX64=set("0123456789abcdef")

def canonical_payload(obj):
    x=dict(obj)
    x.pop("self_hash",None)
    x.pop("signature",None)
    return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode("utf-8")

def sha256_bytes(b): return hashlib.sha256(b).hexdigest()
def self_hash(obj): return sha256_bytes(canonical_payload(obj))
def parse_time(s): return datetime.fromisoformat(s.replace("Z","+00:00"))

def cell_key(r):
    c=r["cell"]
    if r["carrier"]=="magnetism":
        return ("magnetism",c["wave"],c["preset"],c["field_mT"],c["cycle"])
    return ("adsorption",c["wave"],c["control_slot"],c["reversal_depth"])

def expected_magnetic():
    return {("magnetism",w,"-",f,c) for w in (1,2,3) for f in (100,150,200) for c in range(1,9)}
def expected_adsorption():
    return {("adsorption",w,u,d) for w in (1,2,3) for u in (1,2,3) for d in range(1,9)}

def basic_acquisition_errors(r):
    e=[]
    req=["receipt_profile","receipt_type","receipt_id","carrier","cell","acquisition","raw_artifact","intervention","provenance","split","qc","self_hash"]
    for k in req:
        if k not in r: e.append(f"missing:{k}")
    if e: return e
    if r["receipt_profile"]!="hgmf-acquisition-receipt/1.0": e.append("profile")
    if r["receipt_type"]!="raw_acquisition": e.append("receipt_type")
    if r["carrier"] not in ("magnetism","adsorption"): e.append("carrier")
    if r["self_hash"]!=self_hash(r): e.append("self_hash")
    a=r["acquisition"]
    try:
        if parse_time(a["ended_at"]) < parse_time(a["started_at"]): e.append("time_order")
    except Exception: e.append("timestamp")
    raw=r["raw_artifact"]
    if len(raw.get("sha256",""))!=64 or any(ch not in HEX64 for ch in raw.get("sha256","")): e.append("raw_sha256")
    if raw.get("bytes",0)<1: e.append("raw_bytes")
    c=r["cell"]
    role="TRAIN" if c.get("wave") in (1,2) else "HOLDOUT"
    if r["split"].get("role")!=role: e.append("split_wave_mismatch")
    if role=="HOLDOUT" and r["split"].get("seen_during_training") is not False: e.append("holdout_seen")
    if r["qc"].get("status")!="PASS": e.append("qc_not_pass")
    for k in ("calibration_pass","reset_pass","raw_trace_pass"):
        if r["qc"].get(k) is not True: e.append(k)
    if r["intervention"].get("prefix_closed") is not True: e.append("prefix_closed")
    return e

def file_integrity_errors(r, root):
    if root is None: return []
    p=root/r["raw_artifact"]["relative_path"]
    if not p.exists(): return ["raw_missing"]
    b=p.read_bytes(); e=[]
    if len(b)!=r["raw_artifact"]["bytes"]: e.append("raw_size_mismatch")
    if sha256_bytes(b)!=r["raw_artifact"]["sha256"]: e.append("raw_hash_mismatch")
    return e

def graph_cycle(parents):
    indeg={k:0 for k in parents}; children=defaultdict(list)
    for child,ps in parents.items():
        for p in ps:
            if p in indeg:
                children[p].append(child); indeg[child]+=1
    q=deque([k for k,v in indeg.items() if v==0]); seen=0
    while q:
        n=q.popleft(); seen+=1
        for ch in children[n]:
            indeg[ch]-=1
            if indeg[ch]==0:q.append(ch)
    return seen!=len(indeg)

def validate(receipts_dir, root=None, seal_hash=None):
    files=sorted(Path(receipts_dir).glob("*.json")); receipts=[]; load_errors=[]
    for p in files:
        try: receipts.append(json.loads(p.read_text(encoding="utf-8")))
        except Exception as ex: load_errors.append({"file":str(p),"error":str(ex)})
    by_id={}; duplicate_ids=[]
    for r in receipts:
        rid=r.get("receipt_id")
        if rid in by_id: duplicate_ids.append(rid)
        by_id[rid]=r
    parents={rid:set(r.get("provenance",{}).get("parent_receipt_ids",[])) | set(r.get("parent_receipt_ids",[])) for rid,r in by_id.items()}
    graph_has_cycle=graph_cycle(parents)
    missing_parents=sorted({p for ps in parents.values() for p in ps if p not in by_id})
    cell_map=defaultdict(list); records=[]
    for rid,r in by_id.items():
        if r.get("receipt_type")!="raw_acquisition": continue
        errs=basic_acquisition_errors(r)+file_integrity_errors(r,root)
        if seal_hash and r.get("split",{}).get("analysis_seal_sha256")!=seal_hash: errs.append("analysis_seal_mismatch")
        for p in parents[rid]:
            if p not in by_id: errs.append(f"missing_parent:{p}")
        try: cell_map[cell_key(r)].append(rid)
        except Exception: errs.append("invalid_cell")
        records.append({"receipt_id":rid,"errors":sorted(set(errs)),"status":"ADMITTED" if not errs else "QUARANTINED"})
    duplicate_cells={str(k):v for k,v in cell_map.items() if len(v)>1}
    if duplicate_cells:
        dupids={rid for ids in duplicate_cells.values() for rid in ids}
        for rec in records:
            if rec["receipt_id"] in dupids:
                rec["status"]="QUARANTINED"; rec["errors"].append("duplicate_cell")
    admitted={rec["receipt_id"] for rec in records if rec["status"]=="ADMITTED"}
    admitted_keys={k for k,ids in cell_map.items() if len(ids)==1 and ids[0] in admitted}
    mag=admitted_keys & expected_magnetic(); ads=admitted_keys & expected_adsorption()
    ancestry_errors=[]
    mag_lookup={k:cell_map[k][0] for k in cell_map if len(k)==5 and len(cell_map[k])==1}
    for k,rid in mag_lookup.items():
        _,w,preset,field,cycle=k; r=by_id[rid]
        prev=r["intervention"].get("previous_cycle_receipt_id")
        if cycle==1:
            if prev is not None: ancestry_errors.append([rid,"cycle1_previous_not_null"])
        else:
            pk=("magnetism",w,preset,field,cycle-1); exp=mag_lookup.get(pk)
            if prev!=exp: ancestry_errors.append([rid,"previous_cycle_mismatch"])
    rect=0
    for w in (1,2,3):
        for f0,f1 in ((100,150),(150,200)):
            for c in range(1,8):
                corners={("magnetism",w,"-",f0,c),("magnetism",w,"-",f0,c+1),("magnetism",w,"-",f1,c),("magnetism",w,"-",f1,c+1)}
                if corners<=admitted_keys: rect+=1
    return {
      "receipt_files":len(files),"load_errors":load_errors,"duplicate_receipt_ids":duplicate_ids,
      "missing_parent_receipt_ids":missing_parents,"provenance_graph_cycle":graph_has_cycle,
      "duplicate_cells":duplicate_cells,"ancestry_errors":ancestry_errors,"records":records,
      "admitted_receipts":len(admitted),"magnetic_grid":{"admitted":len(mag),"required":72},
      "adsorption_grid":{"admitted":len(ads),"required":72},
      "magnetic_adjacent_rectangles":{"admitted":rect,"required":42},
      "empirical_verdict":"READY_FOR_ANALYSIS" if len(mag)==72 and len(ads)==72 and rect==42 else "ABSTAIN_INCOMPLETE_RECEIPTS"
    }

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("receipts_dir"); ap.add_argument("--root",type=Path)
    ap.add_argument("--seal-hash"); ap.add_argument("--report",type=Path); args=ap.parse_args()
    report=validate(args.receipts_dir,args.root,args.seal_hash)
    out=json.dumps(report,ensure_ascii=False,indent=2,sort_keys=True)+"\n"
    if args.report: args.report.write_text(out,encoding="utf-8")
    print(out,end="")
    return 0 if report["empirical_verdict"]=="READY_FOR_ANALYSIS" else 2

if __name__=="__main__":
    raise SystemExit(main())
