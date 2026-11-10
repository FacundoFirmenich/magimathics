#!/usr/bin/env python3
"""Expand the embedded canonical HG39 payload into this directory."""
from pathlib import Path
import base64
import io
import zipfile


def main() -> None:
    root = Path(__file__).resolve().parent
    payload = (root / "payload_00.txt").read_text(encoding="utf-8")
    payload = "".join(payload.split())
    raw = base64.b64decode(payload, validate=True)
    with zipfile.ZipFile(io.BytesIO(raw), "r") as archive:
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"corrupt payload member: {bad}")
        archive.extractall(root)
        print(f"materialized={len(archive.namelist())}")


if __name__ == "__main__":
    main()
