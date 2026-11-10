#!/usr/bin/env python3
"""Expand the embedded canonical HG38 payload into this directory."""
from pathlib import Path
import base64
import io
import zipfile


def main() -> None:
    root = Path(__file__).resolve().parent
    payload = "".join(
        (root / f"payload_{i:02d}.txt").read_text(encoding="utf-8").strip()
        for i in range(7)
    )
    raw = base64.b64decode(payload, validate=True)
    with zipfile.ZipFile(io.BytesIO(raw), "r") as archive:
        bad = archive.testzip()
        if bad is not None:
            raise RuntimeError(f"corrupt payload member: {bad}")
        archive.extractall(root)
        print(f"materialized={len(archive.namelist())}")


if __name__ == "__main__":
    main()
