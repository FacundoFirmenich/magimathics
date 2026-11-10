#!/usr/bin/env python3
import copy, json
from pathlib import Path
from hgmf_hg38_validator import adjudicate, object_hash

ROOT=Path(__file__).resolve().parent
seal=json.loads((ROOT/'HGMF_HG38_PROSPECTIVE_SEAL.json').read_text(encoding='utf-8'))

assert object_hash(seal)==seal['self_hash']

# Current state must be a clean, explicit abstention: no real calibration receipts exist.
a=adjudicate(seal,None)
assert a['authorized'] is False
assert a['status']=='ABSTAIN_NOT_ARMED_MISSING_REAL_RECEIPTS'
assert a['errors']==[]

# Any tamper to the frozen protocol must fail its self-hash.
t=copy.deepcopy(seal)
t['split']['holdout_units_per_carrier']=23
b=adjudicate(t,None)
assert b['authorized'] is False
assert any('self hash mismatch' in x for x in b['errors'])

# A fake arming object without real receipts must fail closed.
fake={
 'profile':'hgmf-hg38-arming-seal/1.0','state':'ARMED',
 'protocol_seal_hash':seal['self_hash'],'armed_at':'2026-11-10T00:00:00+01:00',
 'first_holdout_not_before':'2026-11-10T00:01:00+01:00',
 'holdout_access_log':[], 'frozen_design_artifacts':[],
 'analysis_environment':{}, 'magnetic_calibration_receipt':{},
 'adsorption_reference_receipt':{}, 'topology_receipt':{}, 'self_hash':'0'*64
}
c=adjudicate(seal,fake)
assert c['authorized'] is False
assert c['status']=='FAIL_CLOSED_NOT_ARMED'

assert seal['magnetic_cartridge']['planning_ceiling_not_confirmatory_mT']==0.80
assert seal['magnetic_cartridge']['max_permissible_expanded_field_uncertainty_mT'] is None
assert seal['adsorption_cartridge']['max_permissible_temperature_uncertainty_K'] is None
assert seal['future_only']['prospective_outcomes_admitted'] is False
assert seal['future_only']['early_efficacy'] is False

print('PASS_HGMF_HG38_EXACT')
print('protocol_self_hash=PASS')
print('current_state=PROTOCOL_FROZEN_UNARMED')
print('missing_real_receipts=ABSTAIN')
print('tamper_detection=PASS')
print('fake_arming_fail_closed=PASS')
print('prospective_outcomes_admitted=false')
print('acquisition_authorized=false')
print('empirical_hgmf_claim=false')
print('physical_protogeometry=HOLD')
