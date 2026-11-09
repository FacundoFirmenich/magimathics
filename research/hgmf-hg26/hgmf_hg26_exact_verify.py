#!/usr/bin/env python3
from pathlib import Path
import csv, json, hashlib
base=Path(__file__).resolve().parent

def sh(p): return hashlib.sha256(p.read_bytes()).hexdigest()

with (base/'HGMF_HG26_TARGET_GRID_MAGNETIC.csv').open(encoding='utf-8') as f:
    mag=list(csv.DictReader(f))
with (base/'HGMF_HG26_TARGET_GRID_ADSORPTION.csv').open(encoding='utf-8') as f:
    ads=list(csv.DictReader(f))
assert len(mag)==72
assert len(ads)==72
assert sum(r['split']=='TRAIN' for r in mag)==48
assert sum(r['split']=='HOLDOUT' for r in mag)==24
assert sum(r['split']=='TRAIN' for r in ads)==48
assert sum(r['split']=='HOLDOUT' for r in ads)==24
seal=json.loads((base/'HGMF_HG26_ANALYSIS_SEAL.json').read_text(encoding='utf-8'))
x=dict(seal); declared=x.pop('self_hash')
payload=json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'),allow_nan=False).encode()
assert hashlib.sha256(payload).hexdigest()==declared
report=json.loads((base/'HGMF_HG26_CURRENT_ADMISSION_REPORT.json').read_text(encoding='utf-8'))
assert report['receipt_files']==0
assert report['admitted_receipts']==0
assert report['magnetic_grid']=={'admitted':0,'required':72}
assert report['adsorption_grid']=={'admitted':0,'required':72}
assert report['magnetic_adjacent_rectangles']=={'admitted':0,'required':42}
assert report['empirical_verdict']=='ABSTAIN_INCOMPLETE_RECEIPTS'
print('PASS_HGMF_HG26_EXACT')
print(f'analysis_seal_sha256={declared}')
print('magnetic_target_cells=72')
print('adsorption_target_cells=72')
print('receipt_files=0')
print('admitted_receipts=0')
print('empirical_verdict=ABSTAIN_INCOMPLETE_RECEIPTS')
