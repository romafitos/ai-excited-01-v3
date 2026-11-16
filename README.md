# The Photo Finish — ai-excited-01, round 3

A peregrine falcon in a full hunting stoop, talons extended, a fraction of
a second before striking a pigeon mid-air. Feathers burst between hunter
and prey against a gradient dusk sky. The strike has not landed yet — it
is about to, and that is the whole picture: the decisive split-second,
frozen at peak tension.

## The entry

- `entry.jpg` — the champion image, 1024x1024 JPEG, 201,878 bytes.
- `main.py` — the program. It copies `entry.jpg` verbatim to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`), checking first
  that the bytes are a JPEG under the 1 MiB cap and match the expected
  sha256, then reading the written file back to confirm it. Standard
  library only; no network, no randomness. Every run writes identical
  bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png — sha256 must be
# 35844ee1f4f8cd4f41db968fd25ee829b1e2dd89a691edab599802a507a8b344
```

## Reproducibility

Run the program twice and compare: both runs must produce the same
201,878 bytes. The output is a verbatim copy of the shipped image, so
there is nothing in the pipeline that can drift between runs.

## Why this frame

Most exciting-photo entries show a beautiful scene or a finished
triumph. This one shows the instant *before* the outcome: the falcon's
eye locked, the pigeon's eye wide, the feather burst already starting.
One look is a jolt, the motion is about to burst, and at 300 pixels
across the falcon, the pigeon and the burst are still unmistakable.

## License

MIT — see `LICENSE`.
