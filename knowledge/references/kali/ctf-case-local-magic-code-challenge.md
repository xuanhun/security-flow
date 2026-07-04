# Local Magic Code Challenge

## Metadata

- Category: mobile, iOS, local CTF artifact.
- Pattern: broad iOS input format gate reveals a visual algorithm clue; final
  answer is not yet judge-verified.
- Knowledge: [ctf-knowledge-mobile.md#ios-format-gate-with-visual-algorithm-hint](ctf-knowledge-mobile.md#ios-format-gate-with-visual-algorithm-hint).
- Evidence: [local-demo-magic-code-challenge](../../../engagements/local-demo-magic-code-challenge).

## Signal Inventory

- Prompt: Liu forgot the password for a box; extra hint was `what algorithm`.
- IPA static triage found `Payload/ctf02.app/ctf02` and `Assets.car`.
- `-[ViewController checkButtonClicked:]` gets the text field value, removes
  spaces, and accepts any value matching `flag{[a-z0-9]{32}}`.
- The accepted input only unhides an image view. It does not compare against a
  unique hardcoded digest.
- macOS CoreUI extraction of `Assets.car` yielded `image.png`, a 914x600 image
  of hikers shown from the back while walking on a trail/track.
- The important local clue is a structured white box/square at the bottom of
  the exported image: near-white fill at `x=402..416, y=594..599` with
  black/gray border. The PNG has exactly 600 scanlines and no appended bytes,
  so the square is an in-image clue rather than hidden extra rows.

## Current Route

The app is a resource gate, not the final checker. After the resource is
exported, solve from the visual resource and CoreUI metadata rather than
continuing to search for a hardcoded password in the binary. Because the app
requires a 32-character lowercase alphanumeric body, `flag{md5(answer)}` is a
reasonable candidate format, but each candidate must be verified externally or
against additional evidence before this case is marked solved.

Rejected candidate:

```text
flag{dba645ebd83eae56a0f1cf788d0ebbbb}
```

This is `md5("knapsack")`. The user reported it was wrong, so the
backpack/knapsack interpretation is only a failed hypothesis, not the answer.

Current hypotheses to verify:

- `whitebox`, because the prompt mentions a box, the hidden image exposes a
  white box, and the hint asks `what algorithm`.
- `white-box` / `white box`, if the challenge expects separator-preserving
  spelling before hashing.
- `backtracking`, a weaker whole-image pun from people seen from the back on a
  track/trail.
- `deepmap2`, the explicit CoreUI compression/algorithm-like value in
  `Assets.car.extracted/Assets.car.info`, although it is likely toolchain
  metadata.
- Image-file or metadata digests, if the final password is tied to the exported
  resource instead of the visible scene.

## Replay Commands

```bash
python scripts/sec.py probe mobile ipa-summary \
  --case-dir local-demo-magic-code-challenge \
  --input test-reports/ctf-2026_magic-code-challenge.ipa \
  --label magic-code \
  --extract \
  --include-entries
```

On macOS:

```bash
mkdir -p out
xcrun assetutil --extract out Assets.car
md5 -s whitebox
```

On Linux:

```bash
python scripts/sec.py probe image inspect \
  --case-dir local-demo-magic-code-challenge \
  --input local-demo-magic-code-challenge/files/magic-code-ipa/Payload/ctf02.app/Assets.car.extracted/image.png \
  --label extracted-image
```

## False Leads

- Treating the app's broad regex acceptance as proof of the final flag.
- Searching for a hardcoded password after the method already proves no unique
  comparison exists.
- Trying to solve from raw `.car` LZFSE/BGRA render artifacts when a macOS
  CoreUI export is available.
- Promoting a visual clue guess into durable knowledge before the user or judge
  verifies it.
