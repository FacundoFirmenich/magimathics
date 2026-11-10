#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

HEX=set('0123456789abcdef')

class ValidationError(Exception):
    pass

def canonical_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')

def object_hash(obj: dict) -> str:
    x=dict(obj); x.pop('self_hash',None)
    return hashlib.sha256(canonical_bytes(x)).hexdigest()

def require(cond: bool, msg: str) -> None:
    if not cond: raise ValidationError(msg)

def require_hash(x: str, name: str) -> None:
    require(isinstance(x,str) and len(x)==64 and all(c in HEX for c in x), f'{name}: invalid sha256')

def parse_time(s: str) -> datetime:
    if s.endswith('Z'): s=s[:-1]+'+00:00'
    d=datetime.fromisoformat(s)
    require(d.tzinfo is not None, 'timestamp must be timezone-aware')
    return d.astimezone(timezone.utc)

def validate_self_hash(obj: dict, label: str) -> None:
    require_hash(obj.get('self_hash',''), f'{label}.self_hash')
    require(object_hash(obj)==obj['self_hash'], f'{label}: self hash mismatch')

def validate_protocol(seal: dict) -> list[str]:
    errors=[]
    try:
        require(seal.get('profile')=='hgmf-hg38-prospective-protocol-seal/1.0','profile')
        require(seal.get('gate')=='HGMF-HG38','gate')
        require(seal.get('future_only',{}).get('prospective_outcomes_admitted') is False,'prospective outcomes already admitted')
        require(seal.get('future_only',{}).get('early_efficacy') is False,'early efficacy must be false')
        validate_self_hash(seal,'protocol')
    except ValidationError as e: errors.append(str(e))
    return errors

def validate_magnetic(r: dict, armed_at: datetime, first_holdout: datetime) -> list[str]:
    e=[]
    try:
        require(r.get('profile')=='hgmf-magnetic-calibration-receipt/1.0','mag profile')
        require(r.get('status')=='REAL_CALIBRATION','mag status')
        validate_self_hash(r,'magnetic')
        u=r['uncertainty_budget']
        require(u['fitness_pass'] is True,'mag fitness failed')
        require(float(u['expanded_uncertainty_mT']) <= float(u['fitness_limit_mT']),'mag uncertainty exceeds fitness limit')
        c=r['coverage']
        require(c['all_experimental_points_bracketed'] is True,'field points not bracketed')
        require(c['drift_pass'] is True and float(c['pre_post_drift_mT'])<=float(c['drift_limit_mT']),'mag drift failed')
        w=r['calibration_window']
        pre_end=parse_time(w['pre_end']); post_start=parse_time(w['post_start']); acq_start=parse_time(w['acquisition_start']); acq_end=parse_time(w['acquisition_end'])
        require(pre_end<=acq_start,'pre calibration after acquisition start')
        require(post_start>=acq_end,'post calibration before acquisition end')
        require(acq_start>=first_holdout,'acquisition starts before authorized holdout')
        valid_until=parse_time(r['instrument']['valid_until'])
        require(valid_until>=acq_end,'reference calibration expires before acquisition end')
    except (ValidationError,KeyError,TypeError,ValueError) as x: e.append(str(x))
    return e

def validate_adsorption(r: dict) -> list[str]:
    e=[]
    try:
        require(r.get('profile')=='hgmf-adsorption-reference-receipt/1.0','ads profile')
        require(r.get('status')=='REAL_REFERENCE_MEASUREMENT','ads status')
        validate_self_hash(r,'adsorption')
        require(r['adsorbate']['same_lot_as_sample'] is True,'adsorbate lot mismatch')
        require(r['curves']['full_pressure_domain_covered'] is True,'reference curves do not cover domain')
        require(r['uncertainty']['temperature_limit_pass'] is True,'temperature fitness failed')
        require(r['uncertainty']['pressure_limit_pass'] is True,'pressure fitness failed')
        require(r['uncertainty']['surface_area_uncertainty_included'] is True,'surface area uncertainty missing')
        require(r['uncertainty']['curve_covariance_included'] is True,'curve covariance missing')
        require(r['interleaving']['reference_sample_interleaved'] is True,'reference/sample not interleaved')
    except (ValidationError,KeyError,TypeError,ValueError) as x: e.append(str(x))
    return e

def validate_topology(r: dict) -> list[str]:
    e=[]
    try:
        require(r.get('profile')=='hgmf-topology-receipt/1.0','topology profile')
        require(r.get('status')=='REAL_INDEPENDENT_CHARACTERIZATION','topology status')
        validate_self_hash(r,'topology')
        require(r['independence']['holdout_outcomes_used'] is False,'topology used holdout')
        require(r['independence']['characterization_completed_before_holdout'] is True,'topology after holdout')
    except (ValidationError,KeyError,TypeError,ValueError) as x: e.append(str(x))
    return e

def adjudicate(protocol: dict, arming: dict|None) -> dict:
    errors=validate_protocol(protocol)
    if arming is None:
        return {'profile':'hgmf-hg38-adjudication/1.0','status':'ABSTAIN_NOT_ARMED_MISSING_REAL_RECEIPTS','authorized':False,'errors':errors}
    try:
        require(arming.get('profile')=='hgmf-hg38-arming-seal/1.0','arming profile')
        require(arming.get('state')=='ARMED','arming state')
        validate_self_hash(arming,'arming')
        require(arming.get('protocol_seal_hash')==protocol.get('self_hash'),'protocol hash mismatch')
        require(arming.get('holdout_access_log')==[],'holdout accessed before arming')
        armed_at=parse_time(arming['armed_at']); first=parse_time(arming['first_holdout_not_before'])
        require(first>armed_at,'holdout must start after arming')
        errors += validate_magnetic(arming['magnetic_calibration_receipt'],armed_at,first)
        errors += validate_adsorption(arming['adsorption_reference_receipt'])
        errors += validate_topology(arming['topology_receipt'])
        require(len(arming.get('frozen_design_artifacts',[]))>0,'no frozen design artifacts')
    except (ValidationError,KeyError,TypeError,ValueError) as x:
        errors.append(str(x))
    return {
      'profile':'hgmf-hg38-adjudication/1.0',
      'status':'PASS_ARMED_FUTURE_ONLY' if not errors else 'FAIL_CLOSED_NOT_ARMED',
      'authorized':not errors,
      'errors':errors
    }

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument('protocol',type=Path)
    ap.add_argument('--arming',type=Path)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    protocol=json.loads(a.protocol.read_text(encoding='utf-8'))
    arming=json.loads(a.arming.read_text(encoding='utf-8')) if a.arming else None
    out=adjudicate(protocol,arming)
    txt=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if a.output: a.output.write_text(txt,encoding='utf-8')
    print(txt,end='')

if __name__=='__main__': main()
