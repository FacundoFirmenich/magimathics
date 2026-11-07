#!/usr/bin/env python3
"""Measurement-uncertainty annex for the four public magnetic minor loops."""
from __future__ import annotations
import argparse, json, hashlib
from pathlib import Path
import h5py, numpy as np, pandas as pd

FILES=[
"Minor_loops_PF2500mT_20250325_2005__10K.h5",
"Minor_loops_PF2500mT_20250325_2230__10K.h5",
"Minor_loops_PF2500mT_20250326_0034__10K.h5",
"Minor_loops_PF2500mT_20250326_0219__10K.h5"]


def block_size(field):
    i=0
    while i+1<len(field) and abs(float(field[i]-field[i+1]))<0.01: i+=1
    return i+1


def process(path:Path, loop_id:str):
    with h5py.File(path,'r') as f:
        d=f['Data']; field=np.asarray(d['Magnetic_Field']); vxy=np.asarray(d['Avg_Voltage_Hp34420A_Ch1']); arr=np.asarray(d['Voltage_Array_Hp34420A_Ch1'])
    p2=block_size(field); inv=bool(vxy[0]*vxy[1]<0); p=round(p2/2)
    F=[]; V=[]; E=[]
    for i in range(0,len(field),p2):
        fb=field[i:i+p2]
        if len(fb)<p2: break
        F.append(float(np.mean(fb)))
        if inv:
            a=vxy[i:i+p]; b=vxy[i+p:i+p2]
            if len(a)<p or len(b)<p2-p: break
            V.append(float(np.mean(a-b)))
            e=np.abs(arr[i:i+p])+np.abs(arr[i+p:i+p2])
            E.append(float(np.std(e)))
        else:
            V.append(float(np.mean(vxy[i:i+p2]))); E.append(float(np.std(arr[i:i+p2])))
    F=np.asarray(F)*8000/93.17; V=np.asarray(V)*1e6; E=np.asarray(E)*1e6
    # remove independently identifiable +2500 mT pre-field point
    steps=np.abs(np.diff(F)); ref=float(np.median(steps[1:][steps[1:]>0])) if np.any(steps[1:]>0) else 0
    if ref>0 and steps[0]>10*ref: F,V,E=F[1:],V[1:],E[1:]
    amp=(V.max()-V.min())/2; offset=(V.max()+V.min())/2
    norm=(V-offset)/amp; enorm=E/amp
    rows=pd.DataFrame({'loop_id':loop_id,'field_mT':F,'vxy_uV':V,'vxy_norm':norm,'vxy_err_uV':E,'vxy_err_norm':enorm})
    summary={
      'loop_id':loop_id,'file':path.name,'points':len(F),'amplitude_uV':float(amp),
      'median_point_error_uV':float(np.median(E)),'mean_point_error_uV':float(np.mean(E)),
      'median_normalized_error':float(np.median(enorm)),'mean_normalized_error':float(np.mean(enorm)),
      'amplitude_to_median_error':float(amp/max(np.median(E),1e-30)),
      'max_abs_signal_to_error':float(np.max(np.abs(V-offset)/np.maximum(E,1e-30))),
      'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
    }
    return rows,summary


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source-dir',type=Path,required=True); ap.add_argument('--out-dir',type=Path,required=True); a=ap.parse_args(); a.out_dir.mkdir(parents=True,exist_ok=True)
    frames=[]; summaries=[]
    for i,name in enumerate(FILES,1):
        frame,s=process(a.source_dir/name,f'Loop_{i}'); frames.append(frame); summaries.append(s)
    pd.concat(frames,ignore_index=True).to_csv(a.out_dir/'HGMF_UMI10_MAGNETIC_POINT_UNCERTAINTY.csv',index=False)
    pd.DataFrame(summaries).to_csv(a.out_dir/'HGMF_UMI10_MAGNETIC_SNR_SUMMARY.csv',index=False)
    strong=[s['loop_id'] for s in summaries if s['amplitude_to_median_error']>=10]
    result={'status':'PASS_MAGNETIC_UNCERTAINTY_AUDIT','loops':summaries,'high_snr_loops_threshold10':strong,'claim_boundary':{'normalization_reliable_all_loops':'PASS' if len(strong)==len(summaries) else 'FAIL_LOW_SNR_SUBSET','model_ranking_requires_snr_sensitivity':'YES' if len(strong)<len(summaries) else 'NO'}}
    (a.out_dir/'HGMF_UMI10_MAGNETIC_UNCERTAINTY.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
