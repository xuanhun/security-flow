# NO.10 Multimodal Identity

## Metadata

- Platform: ByteCTF challenge 143 series.
- Category: AI and digital watermark.
- Targets:
  - `https://a78b6b58783a18fcaa0d8959452ffb7d.ctf.bytedance.net`
  - `https://a62da3c8680dcbe7b85862c6ab993454.ctf.bytedance.net`
- Attachment:
  `/home/xuanhun/security/ctf/bytectf-143/reports/ctf-2023_embed_11.png`
- Final flag: `flag{What_is_the_full_name_of_CTF}`

## Prompt Summary

The challenge has two independent subtasks: an attachment image dark watermark
task and a click-scene AI task. Solving either gives an accepted flag. The
watermark path asks for information hidden in the administrator image.

## Pattern

Channel-difference modulo watermark.

The hidden message is not in normal PNG metadata or a single-channel LSB text
stream. It becomes visible when rendering residue classes of the blue-minus-red
pixel residual.

The user-provided screenshot contributed the reusable tactic: when residual
text is too faint, do not only stretch the residual. Turn the residual into
binary class masks, especially parity masks, and read the tiled watermark from
the clearest class.

## Signal Inventory

- Original artifact is a large PNG.
- Direct strings and ordinary LSB scanning are negative.
- Blue-minus-red residual layers contain a strong repeated spatial pattern.
- `(B - R) mod 2 == 0` produces readable repeated text.

## Probes And Evidence

Replay:

```bash
python scripts/sec.py probe image channel-mod \
  --case-dir ctf/bytectf-143/challenges/no10-multimodal-identity \
  --input ctf/bytectf-143/reports/ctf-2023_embed_11.png \
  --label br-mod2-r0 \
  --left B --right R --modulus 2 --remainder 0
```

Evidence:

- Summary:
  `../../../ctf/bytectf-143/challenges/no10-multimodal-identity/artifacts/br-mod2-r0-channel-mod.json`
- Mask:
  `../../../ctf/bytectf-143/challenges/no10-multimodal-identity/files/br-mod2-r0-b-minus-r-mod2-eq0.png`
- Readable crop:
  `../../../ctf/bytectf-143/challenges/no10-multimodal-identity/files/br-mod2-text-sample-crop-x0-y0-w1100-h180.png`

## Route Decision

Read the `flag{...}` text exactly as extracted. The phrase looks like a
question, but in this challenge it is the final answer. Submit the exact hidden
string before attempting semantic expansion such as `Capture_The_Flag`.

## Reusable Lesson

For image watermark CTFs with visible channel-difference clues or odd/even
histogram imbalance, render `(channel_a - channel_b) mod n` masks for small
`n`, especially `2`, before moving to OCR, model behavior, or unrelated web
routes.

Keep the extracted flag literal. A hidden watermark may be phrased like a
question, but if it is already wrapped in `flag{...}`, treat it as an answer
candidate first.
