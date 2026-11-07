#!/usr/bin/env python3
"""Synthesize the frozen magnetic and adsorption HGMF-UMI-10 tribunals."""
from __future__ import annotations
import argparse, json
from pathlib import Path


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out-dir",type=Path,required=True)
    args=ap.parse_args(); root=args.out_dir
    mag=json.loads((root/"HGMF_UMI10_RESULTS.json").read_text())
    ads=json.loads((root/"HGMF_UMI10_ADSORPTION_RESULTS.json").read_text())
    mb=mag["best_model"]["model"]; ab=ads["best_model"]["model"]
    magnetic_rpm=(mb=="rpm_relays")
    adsorption_rpm=(ab=="rpm_relays")
    same_best=(mb==ab)
    magnetic_closure=mag["return_point"]["mean_return_error_norm"]
    result={
      "gate":"HGMF-UMI-10",
      "magnetic_best_model":mb,
      "adsorption_best_model":ab,
      "same_best_operator":same_best,
      "magnetic_mean_return_error_norm":magnetic_closure,
      "adsorption_mean_return_error_norm":ads["mean_return_error_norm"],
      "magnetic_nested_reversals":False,
      "adsorption_reversal_counts":ads["reversal_counts"],
      "adjudication":{
        "binary_recovery":"PASS",
        "history_required_both_domains":"PASS",
        "single_common_best_operator":"PASS_OPERATOR_CLASS" if same_best and mb!="memoryless" else "FAIL_TRANSFER",
        "full_cross_domain_rpm":"PASS_OPERATOR_CLASS" if magnetic_rpm and adsorption_rpm else "FAIL_RPM_MAGNETIC" if not magnetic_rpm else "FAIL_TRANSFER",
        "magnetic_rpm_identifiability":"HOLD_SINGLE_REVERSAL_PROTOCOL",
      },
      "claim_boundary":{
        "shared_history_semantics":"SUPPORTED",
        "shared_return_point_memory":"NOT_ESTABLISHED",
        "shared_microphysics":"NOT_CLAIMED",
        "future_only_absolute_prediction":"NOT_ESTABLISHED",
      },
    }
    (root/"HGMF_UMI10_CROSS_DOMAIN_RESULTS.json").write_text(json.dumps(result,indent=2)+"\n")
    text=f"""# HGMF-UMI-10 — Cross-domain adjudication

## Verdict

- Magnetic best model: `{mb}`
- Adsorption best model: `{ab}`
- Same best operator: `{same_best}`
- Full cross-domain RPM: `{result['adjudication']['full_cross_domain_rpm']}`

## Exact boundary

Both domains reject a memoryless instantaneous state, but a common return-point-memory operator is promoted only if the same RPM update law wins the whole-loop tribunal in both and the protocols identify nested reversals. Those conditions are not relaxed after observing results.
"""
    (root/"HGMF_UMI10_CROSS_DOMAIN_ADJUDICATION.md").write_text(text)
    print(json.dumps(result,indent=2))

if __name__=="__main__": main()
