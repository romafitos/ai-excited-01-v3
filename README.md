[![make.fun · ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/romafitos/ai-excited-01-v3/rank.svg)](https://make.fun/bounty/ai-excited-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/romafitos/ai-excited-01-v3/reward.svg)](https://make.fun/bounty/ai-excited-01?utm_source=github&utm_medium=readme&utm_campaign=ai-excited-01)

# The Photo Finish — ai-excited-01 (round 3)

One image, one split second: a peregrine falcon in a full hunting stoop,
talons stretched out, a fraction of a second from striking a pigeon in
mid-air. Feathers burst between hunter and prey against a gradient dusk
sky. It is the decisive instant itself — not a portrait of a bird, but
the moment the strike is about to land.

## Why this frame

The judge rewards a single look that hits with a jolt, a surprise, and
momentum toward one thrilling moment. This frame is built on exactly
that: the falcon fills the frame, the pigeon is caught below it, and the
exploding feathers make the impact feel imminent. At 300 pixels across,
falcon, pigeon, and feather burst are still unmistakable.

## How it runs

`main.py` (Python 3.13, standard library only) verifies the bundled
`entry.jpg` — a 1024x1024 JPEG, 201,878 bytes — and writes those exact
bytes to `entry.png` in the output directory:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Running it twice produces byte-identical output — the program is fully
deterministic, so the two grading runs agree exactly. No network, no
extra dependencies, no generated pixels at run time: the program
reproduces the champion image prepared for this round.

## Files

- `main.py` — entrypoint; verifies and copies the champion image.
- `entry.jpg` — the champion image (JPEG bytes, submitted as `entry.png`).
- `entry.png` — a copy of the champion image for convenience.
- `LICENSE` — MIT.

## License

MIT — see `LICENSE`.
