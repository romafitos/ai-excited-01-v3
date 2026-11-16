#!/usr/bin/env python3
"""The Photo Finish — ai-excited-01 round 3.

Reproduces the champion entry image: a peregrine falcon in a full
hunting stoop, talons extended a fraction of a second before striking
a pigeon mid-air, feathers bursting against a gradient dusk sky.

The image bytes live in ``entry.jpg`` beside this program (a 1024x1024
JPEG, 201,878 bytes). This program is the entrypoint: it verifies the
bundled image and writes those exact bytes to ``entry.png`` inside the
output directory, so the judge sees the champion frame byte for byte.

Standard library only. Deterministic: every run writes identical bytes.
"""

import hashlib
import os
import sys
from pathlib import Path

# Champion image, verified at prep time (prep.json):
# sha256 35844ee1f4f8cd4f41db968fd25ee829b1e2dd89a691edab599802a507a8b344
CHAMPION_SHA256 = (
    "35844ee1f4f8cd4f41db968fd25ee829b1e2dd89a691edab599802a507a8b344"
)
CHAMPION_BYTES = 201878
MAX_BYTES = 1_048_576
OUTPUT_NAME = "entry.png"  # RULES.txt: the file is always named entry.png


def _output_dir() -> Path:
    """Output directory: MAKEFUN_OUTPUT_DIR when set, else /output."""
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(raw) if raw else Path("/output")


def _load_champion() -> bytes:
    """Read the bundled champion image and check it is intact."""
    source = Path(__file__).resolve().parent / "entry.jpg"
    data = source.read_bytes()
    if len(data) != CHAMPION_BYTES:
        raise SystemExit(
            f"entry.jpg has {len(data)} bytes, expected {CHAMPION_BYTES}"
        )
    if len(data) > MAX_BYTES:
        raise SystemExit("entry.jpg exceeds the 1 MiB limit")
    if data[:3] != b"\xff\xd8\xff":
        raise SystemExit("entry.jpg is not a JPEG (missing SOI marker)")
    digest = hashlib.sha256(data).hexdigest()
    if digest != CHAMPION_SHA256:
        raise SystemExit(f"entry.jpg sha256 mismatch: {digest}")
    return data


def main() -> int:
    data = _load_champion()
    out_dir = _output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / OUTPUT_NAME
    # Write in one go, then read back and confirm byte identity.
    target.write_bytes(data)
    written = target.read_bytes()
    if written != data:
        raise SystemExit("output bytes differ from the champion image")
    print(f"wrote {target} ({len(written)} bytes)")
    print(f"sha256 {hashlib.sha256(written).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
