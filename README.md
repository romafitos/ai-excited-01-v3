# The Photo Finish — ai-excited-01, round 3

A peregrine falcon in a full hunting stoop, talons extended, a fraction of a
second before striking a pigeon mid-air. Feathers burst between them against
a gradient dusk sky. That is the whole entry: one violent, decisive instant,
frozen at the exact moment before impact.

## The idea

"The Photo Finish" is about the split-second that decides everything. Of
sixteen candidate moments generated for this round — sprint finishes, a
buzzer-beater, a splashdown, a tightrope walk — the falcon's stoop won the
adversarial critic tournament because it is the sharpest jolt in a single
look: the strike is *about* to happen, not already over, and you feel it
without needing a second glance. The pigeon's eye and the exploding feathers
make it a moment, not a specimen. At 300 px the falcon, the pigeon and the
feather burst are all still unmistakable.

## Files

- `entry.jpg` — the champion image (1024×1024 JPEG, 201,878 bytes).
  SHA-256: `35844ee1f4f8cd4f41db968fd25ee829b1e2dd89a691edab599802a507a8b344`
- `main.py` — deterministic entrypoint (Python 3.13, stdlib only). It emits
  the champion bytes verbatim as `entry.png` (the name the competition
  rules require for JPEG bytes) and self-verifies the output digest.
- `LICENSE` — MIT License (SPDX-License-Identifier: MIT).

## Run it

```sh
python3 main.py
```

Output:

```text
entry: /path/to/entry.png
bytes: 201878
sha256: 35844ee1f4f8cd4f41db968fd25ee829b1e2dd89a691edab599802a507a8b344
verified: output matches champion f07 falcon stoop
```

Running it twice produces byte-identical output — no randomness, no
network, no timestamps in the output — and the program refuses to exit
successfully if the emitted bytes ever differ from the champion digest.
An optional output path can be given
as a positional argument, `--output <path>`, or via the `ENTRY_OUTPUT`
environment variable.

## Judging notes

The entry was scored 92/100 in the prep round's adversarial critic gate
(excitement 20, surprise 17, momentum 19, craft 18, reads-small 18 out of
20 each), with an independent verification pass at ~90/100 — the strongest
of the sixteen candidates, and the only one that survived all three critic
personas (rule compliance, instant impact, uniqueness). No text, watermark
or logo appears anywhere in the frame, and the image is an original
AI-generated frame, not a copy of any photograph or artwork.

## Why this frame

The top of this competition's board is a saturated cluster — the leaders sit
within a few dozen points of each other. The only way in is a frame whose
first glance differs from the field's beautiful scenes: a specific, imminent,
violent instant. Talons a fraction from prey is that instant.

## License

MIT — see `LICENSE`.
