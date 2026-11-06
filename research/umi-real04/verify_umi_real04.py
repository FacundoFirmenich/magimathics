#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

root=Path(__file__).resolve().parent
m=pd.read_csv(root/'data/METRICS_BY_SIGNATURE.csv').set_index('profile')
assert m.loc['strict','tp']==5
assert m.loc['strict','tn']==5
assert m.loc['strict','fp']==0
assert m.loc['strict','fn']==0
assert abs(m.loc['moderate','false_discovery_rate']-1/6)<1e-12
assert abs(m.loc['weak','false_discovery_rate']-.5)<1e-12
r=pd.read_csv(root/'data/MISSING_EVIDENCE_ROBUSTNESS.csv')
assert (r.accuracy_on_adjudicated==1).all()
assert (r.false_positive_rate_on_adjudicated==0).all()
print('PASS_MGM_UMI_REAL04')
print('strict: TP=5 FP=0 TN=5 FN=0')
print('moderate: one deceptive false positive')
print('weak: all five deceptive systems pass')
print('missing evidence: no false positives under conservative abstention')
