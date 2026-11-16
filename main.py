#!/usr/bin/env python3
"""ai-excited-01 round 3 — "The Photo Finish".

Writes the champion image to the output directory as ``entry.png``.

The image is a peregrine falcon in a full hunting stoop, talons extended,
a fraction of a second before striking a pigeon mid-air — feathers
bursting between them against a gradient dusk sky. It is the decisive
split-second, frozen at peak tension: the strike is about to happen, not
already over.

The file is JPEG bytes carried under the name ``entry.png`` (the rules
tell PNG and JPEG apart by their first bytes, and the name stays
``entry.png`` either way). The program ships the image as ``entry.jpg``
next to this file and copies its bytes verbatim, so every run produces
byte-identical output. Standard library only; no network, no randomness.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

# The competition caps an entry at 1 MiB and 1024x1024 pixels.
MAX_BYTES = 1_048_576
JPEG_MAGIC = b"\xff\xd8\xff"

# The champion image, as prepared for this round (1024x1024, 201,878 bytes).
EXPECTED_SHA256 = "35844ee1f4f8cd4f41db968fd25ee829b1e2dd89a691edab599802a507a8b344"


def main() -> int:
    here = Path(__file__).resolve().parent
    source = here / "entry.jpg"

    if not source.is_file():
        print(f"missing source image: {source}", file=sys.stderr)
        return 1

    data = source.read_bytes()

    if len(data) > MAX_BYTES:
        print(f"entry too large: {len(data)} bytes > {MAX_BYTES}", file=sys.stderr)
        return 1
    if not data.startswith(JPEG_MAGIC):
        print("entry is not a JPEG (bad magic bytes)", file=sys.stderr)
        return 1

    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"entry sha256 mismatch: got {digest}", file=sys.stderr)
        return 1

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"

    # Copy the bytes verbatim; a temp file + rename keeps the write atomic
    # so a second run never sees a half-written entry.
    tmp = dest.with_suffix(".tmp")
    with open(tmp, "wb") as fh:
        fh.write(data)
    shutil.move(tmp, dest)

    # Robustness: read the written file back and confirm it is exactly
    # the bytes we meant to ship, so a partial or interrupted write can
    # never pass silently as a valid entry.
    written = dest.read_bytes()
    if hashlib.sha256(written).hexdigest() != digest:
        print("output verification failed: written bytes differ", file=sys.stderr)
        return 1

    print(f"wrote {dest} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
