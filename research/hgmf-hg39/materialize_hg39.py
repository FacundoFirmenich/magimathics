#!/usr/bin/env python3
"""Expand the embedded canonical HG39 payload into this directory."""
from pathlib import Path
import base64
import hashlib
import io
import zipfile

EXPECTED_ZIP_SHA256 = "5e38e6629162ec56b81846ab3dae90af8675e780b9b094c17adfd79b039ac8a8"
PART_COUNT = 19


def main() -> None:
    root = Path(__file__).resolve().parent
    payload = "".join(
        (root / f"payload_{i:02d}.txt").read_text(encoding="utf-8").strip()
        for i in range(PART_COUNT)
    )
    payload = "".join(payload.split())
    raw = base64.b64decode(payload, validate=True)
    actual = hashlib.sha256(raw).hexdigest()
    if actual != EXPECTED_ZIP_SHA256:
        raise RuntimeError(f"payload SHA-256 mismatch: {actual}")
    with zipfile.ZipFile(io.BytesIO(raw), "r") as archive:
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"corrupt payload member: {bad}")
        archive.extractall(root)
        print(f"payload_sha256={actual}")
        print(f"materialized={len(archive.namelist())}")


if __name__ == "__main__":
    main()
