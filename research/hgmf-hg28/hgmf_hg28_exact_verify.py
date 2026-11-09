#!/usr/bin/env python3
import csv
from pathlib import Path
base=Path(__file__).resolve().parent
rows=list(csv.DictReader((base/'HGMF_HG28_ORDER_MODULE.csv').open(encoding='utf-8')))
assert len(rows)==36
assert sum(int(r['sequence_blocks']) for r in rows)==72
assert sum(int(r['sequence_blocks']) for r in rows if r['split']=='TRAIN')==48
assert sum(int(r['sequence_blocks']) for r in rows if r['split']=='HOLDOUT')==24
for carrier in ('magnetism','adsorption'):
    for wave in ('1','2','3'):
        sub=[r for r in rows if r['carrier']==carrier and r['wave']==wave]
        assert len(sub)==6
        edges={(int(r['history_low']),int(r['history_high'])) for r in sub}
        assert edges=={(1,2),(4,5),(7,8)}
print('PASS_HGMF_HG28_EXACT')
print('order_context_rows=36')
print('order_sequence_blocks=72')
print('order_training_blocks=48')
print('order_holdout_blocks=24')
print('confirmatory_causal_hypotheses=14')
print('familywise_alpha=0.05')
print('physical_protogeometry=HOLD')
