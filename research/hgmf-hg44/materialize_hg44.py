#!/usr/bin/env python3
"""Expand the verified multipart HG44 canonical payload into this directory."""
from pathlib import Path
import base64
import hashlib
import io
import zipfile

EXPECTED_ZIP_SHA256 = "067aaa1db6a8ad27f7d616d6adb58bd65e0da4ae5003f9d8d2c869b6248f5fe6"
PART_COUNT = 6


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
