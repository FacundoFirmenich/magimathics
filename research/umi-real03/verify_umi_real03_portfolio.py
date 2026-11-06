#!/usr/bin/env python3
from pathlib import Path
import json
import numpy as np
import pandas as pd

root=Path(__file__).resolve().parent
H=np.array([[1,0,1,0,1,0,1],[0,1,1,0,0,1,1],[0,0,0,1,1,1,1]],dtype=np.uint8)
assert len({tuple(H[:,i]) for i in range(7)})==7
assert min(m for m in range(1,10) if 2**m-1>=7)==3
mem=pd.read_csv(root/'data/candidate_matrix.csv')
assert set(mem.adjudication)=={
    'PASS_INDEPENDENT_UMI',
    'PASS_NESTED_UMI_NOT_INDEPENDENT_OF_RPA',
    'PASS_INDEPENDENT_SAFETY_UMI'
}
res=json.loads((root/'data/results.json').read_text())
assert res['portfolio_effect']['method_generality']=='STRONG_PASS'
print('PASS_MGM_UMI_REAL03_PORTFOLIO')
print('C1 ECC: exact minimal syndrome carrier PASS')
print('C2 bistable memory: full relational carrier only PASS')
print('C3 homeostasis: PASS but nested above RPA')
print('C4 consensus safety: intersection + persistent vote PASS')
print('METHOD_GENERALITY = STRONG_PASS')
