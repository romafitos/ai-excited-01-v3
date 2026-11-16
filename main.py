#!/usr/bin/env python3
"""The Photo Finish — ai-excited-01 round 3 (r3 revision, edit pass 2).

Revision notes (r3 vs the previous round's generator): the emitter now
writes atomically (temp file + os.replace + fsync) so an interrupted run
cannot leave a truncated entry.png behind, and the output path honours an
explicit --output flag / positional argument / $ENTRY_OUTPUT before falling
back to entry.png in the cwd. The champion bytes and digest are unchanged.

Champion: f07 "falcon stoop" — a peregrine falcon in a full hunting stoop,
talons extended, a fraction of a second before striking a pigeon mid-air,
feathers bursting against a gradient dusk sky.

This program is the deterministic entrypoint. It emits the champion image
byte-for-byte into the output file the rules require (JPEG bytes named
``entry.png``) and then self-verifies the emitted bytes against the known
champion digest, so a run either reproduces the exact entry or fails loudly.

Stdlib only. No network, no randomness, no timestamps in the output:
running it twice produces identical bytes.
"""

import hashlib
import os
import sys
from pathlib import Path

CHAMPION_SHA256 = "35844ee1f4f8cd4f41db968fd25ee829b1e2dd89a691edab599802a507a8b344"
CHAMPION_BYTES = 201878
SOURCE_NAME = "entry.jpg"   # champion image shipped in this repo
OUTPUT_NAME = "entry.png"   # name the competition rules require


def script_dir() -> Path:
    """Directory containing this file (the repo root when run in place)."""
    return Path(__file__).resolve().parent


def locate_source() -> Path:
    """Find the champion image next to this script, or in the cwd."""
    here = script_dir() / SOURCE_NAME
    if here.is_file():
        return here
    cwd = Path.cwd() / SOURCE_NAME
    if cwd.is_file():
        return cwd
    raise FileNotFoundError(
        f"champion source {SOURCE_NAME!r} not found next to main.py or in cwd"
    )


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def emit(data: bytes, out_path: Path) -> Path:
    """Write the bytes verbatim (atomic: temp file + rename, so a failed run
    can never leave a half-written entry behind), then read back and verify."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = out_path.with_suffix(out_path.suffix + ".tmp")
    with open(tmp_path, "wb") as fh:
        fh.write(data)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp_path, out_path)
    written = out_path.read_bytes()
    if digest(written) != CHAMPION_SHA256:
        raise SystemExit(
            f"verification failed: {out_path} sha256 "
            f"{digest(written)} != expected {CHAMPION_SHA256}"
        )
    if len(written) != CHAMPION_BYTES:
        raise SystemExit(
            f"verification failed: {out_path} is {len(written)} bytes, "
            f"expected {CHAMPION_BYTES}"
        )
    return out_path


def resolve_output(argv: list[str]) -> Path:
    """Output path: --output/argv[1] wins, else $ENTRY_OUTPUT, else entry.png
    in the current working directory."""
    for i, arg in enumerate(argv):
        if arg == "--output" and i + 1 < len(argv):
            return Path(argv[i + 1])
        if arg.startswith("--output="):
            return Path(arg.split("=", 1)[1])
    positional = [a for a in argv if not a.startswith("-")]
    if positional:
        return Path(positional[0])
    env_out = os.environ.get("ENTRY_OUTPUT")
    if env_out:
        return Path(env_out)
    return Path.cwd() / OUTPUT_NAME


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    source = locate_source()
    data = source.read_bytes()
    if digest(data) != CHAMPION_SHA256:
        print(
            f"error: source {source} sha256 {digest(data)} "
            f"!= champion {CHAMPION_SHA256}",
            file=sys.stderr,
        )
        return 1
    out_path = emit(data, resolve_output(args))
    print(f"entry: {out_path}")
    print(f"bytes: {len(data)}")
    print(f"sha256: {digest(data)}")
    print("verified: output matches champion f07 falcon stoop")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
