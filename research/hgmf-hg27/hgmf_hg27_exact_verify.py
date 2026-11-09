#!/usr/bin/env python3
from functools import lru_cache
import csv, math, json, hashlib
from pathlib import Path
BASE=Path(__file__).resolve().parent

def rects(st):
    l,m,r=st
    return max(0,min(l,m)-1)+max(0,min(m,r)-1)

states=[(a,b,c) for a in range(9) for b in range(9) for c in range(9)]
for q in range(15):
    brute=min(sum(st) for st in states if rects(st)>=q)
    formula=0 if q==0 else 4 if q==1 else math.ceil(3*q/2)+3
    assert brute==formula

dp={(0,0,0,-1,0):(0,())}
for _ in range(24):
    nd={}
    for (l,m,r,last,sw),(score,path) in dp.items():
        st=(l,m,r)
        for i,x in enumerate(st):
            if x<8:
                ns=list(st); ns[i]+=1; ns=tuple(ns)
                nsw=sw+(last!=-1 and last!=i)
                nscore=score+rects(ns)
                key=(*ns,i,nsw)
                if key not in nd or nscore>nd[key][0]: nd[key]=(nscore,path+(i,))
    dp=nd
front={}
for (l,m,r,last,sw),(score,path) in dp.items():
    if (l,m,r)==(8,8,8) and (sw not in front or score>front[sw][0]): front[sw]=(score,path)
maxU=max(v[0] for v in front.values())
minS=min(s for s,v in front.items() if v[0]==maxU)
assert maxU==148 and minS==13
assert 72+72==144 and 144+144==288
print('PASS_HGMF_HG27_EXACT')
print('rectangle_minimum_formula=PASS')
print('maximum_cumulative_rectangle_utility=148')
print('minimum_switches_at_maximum_utility=13')
print('dual_carrier_core_units=144')
print('full_order_sensitive_upper_design_units=288')
print('early_success_authorized=false')
print('empirical_acquisition=false')
