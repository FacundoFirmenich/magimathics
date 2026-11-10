#!/usr/bin/env python3
from __future__ import annotations
import argparse, copy, hashlib, json
from pathlib import Path

PROTOCOL_HASH = "2406dafddfbec2f98b2a3d83c1f48381a3d7cd16130eb8ef48dc2f9a93d471aa"
EXPECTED = {
    "magnetic": ("hgmf-magnetic-calibration-receipt/1.0", "REAL_CALIBRATION"),
    "adsorption_reference": ("hgmf-adsorption-reference-receipt/1.0", "REAL_REFERENCE_MEASUREMENT"),
    "topology": ("hgmf-topology-receipt/1.0", "REAL_INDEPENDENT_CHARACTERIZATION"),
}


def canonical_hash(doc: dict) -> str:
    x = copy.deepcopy(doc)
    x.pop("self_hash", None)
    payload = json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(payload).hexdigest()


def validate(doc: dict) -> dict:
    errors = []
    blockers = []

    if doc.get("profile") != "hgmf-hg39-commissioning-dossier/1.0":
        errors.append("PROFILE_MISMATCH")
    if doc.get("protocol_seal_hash") != PROTOCOL_HASH:
        errors.append("PROTOCOL_SEAL_HASH_MISMATCH")
    if doc.get("self_hash") != canonical_hash(doc):
        errors.append("DOSSIER_SELF_HASH_MISMATCH")

    future = doc.get("future_only", {})
    if future.get("holdout_accessed") is not False:
        errors.append("HOLDOUT_ACCESS_VIOLATION")
    if future.get("prospective_outcomes_present") is not False:
        errors.append("PROSPECTIVE_OUTCOME_VIOLATION")

    packages = doc.get("work_packages", {})
    for key, (profile, status) in EXPECTED.items():
        pkg = packages.get(key)
        if not isinstance(pkg, dict):
            errors.append(f"MISSING_WORK_PACKAGE:{key}")
            continue
        if not pkg.get("candidate_routes"):
            errors.append(f"NO_CANDIDATE_ROUTE:{key}")
        if pkg.get("signed_service_confirmation") is None:
            blockers.append(f"MISSING_SIGNED_SERVICE_CONFIRMATION:{key}")
        receipt = pkg.get("actual_result_receipt")
        if receipt is None:
            blockers.append(f"MISSING_ACTUAL_RESULT_RECEIPT:{key}")
        else:
            if receipt.get("profile") != profile:
                errors.append(f"RECEIPT_PROFILE_MISMATCH:{key}")
            if receipt.get("status") != status:
                errors.append(f"RECEIPT_STATUS_MISMATCH:{key}")
            if not receipt.get("self_hash"):
                errors.append(f"RECEIPT_SELF_HASH_MISSING:{key}")

    fitness = doc.get("fitness", {})
    if fitness.get("numeric_limits_frozen") is not True:
        blockers.append("NUMERIC_FITNESS_LIMITS_NOT_FROZEN")
    if fitness.get("fitness_input_artifact") is None:
        blockers.append("FITNESS_INPUT_ARTIFACT_MISSING")
    if fitness.get("fitness_output_artifact") is None:
        blockers.append("FITNESS_OUTPUT_ARTIFACT_MISSING")

    if doc.get("state") != "COMMISSIONED_READY_FOR_ARMING":
        blockers.append("DOSSIER_STATE_NOT_COMMISSIONED")
    if doc.get("authority") != "NO_ARMING_AUTHORITY":
        errors.append("HG39_DOSSIER_MAY_NOT_GRANT_ARMING_AUTHORITY")

    authorized = not errors and not blockers
    if errors:
        status = "FAIL_INVALID_COMMISSIONING_DOSSIER"
    elif blockers:
        status = "ABSTAIN_REAL_COMMISSIONING_NOT_COMPLETE"
    else:
        status = "PASS_COMMISSIONED_READY_FOR_HG38_ARMING_REVIEW"

    return {
        "profile": "hgmf-hg39-adjudication/1.0",
        "status": status,
        "authorized_for_hg38_arming_review": bool(authorized),
        "acquisition_authorized": False,
        "errors": errors,
        "blockers": blockers,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("dossier", type=Path)
    p.add_argument("--output", type=Path)
    args = p.parse_args()
    doc = json.loads(args.dossier.read_text(encoding="utf-8"))
    result = validate(doc)
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
