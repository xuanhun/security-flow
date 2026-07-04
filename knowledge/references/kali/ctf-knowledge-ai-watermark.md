# CTF AI And Digital Watermark

## First Pass

- Identify artifact type: image, audio, video, model, prompt transcript,
  generated text, embedding, or watermark detector.
- Preserve originals and compare derived outputs with hashes and dimensions.
- Determine whether the task is extraction, evasion, classification, prompt
  injection, model behavior, or signal processing.

## Routes

### Digital Watermark

- Inspect metadata, pixel/channel residuals, frequency domain, compression
  artifacts, repeated patterns, and known watermark libraries.
- Compare original-like variants when available.

### Dark Watermark From Channel Residuals

This pattern was distilled from the user-provided dark-watermark screenshot
used during NO.10. Treat it as a first-class route whenever a PNG/JPEG looks
visually normal but the prompt hints at a hidden identity, watermark, or image
secret.

- Intake:
  - Preserve the original image; do not resave through a lossy editor before
    analysis.
  - Record dimensions, hash, PNG chunks, printable strings, and basic bitplane
    outputs.
  - If ordinary metadata, strings, and direct LSB scans are empty, move to
    visual residual analysis instead of staying on string extraction.
- Residual exploration:
  - Render channel differences for `B-R`, `R-B`, `R-G`, `G-R`, `B-G`, and
    `G-B`.
  - View centered, positive, negative, absolute, and stretched maps. Faint
    repeated text or a tiled pattern means the signal is spatial rather than a
    linear byte stream.
  - Check whether one residual has an unusual distribution, such as a strong
    even/odd imbalance or many pixels concentrated around a small set of
    difference values.
- Mask extraction:
  - Try exact difference bands first when a residual map shows clear levels:
    `diff == c` or a small band around `c`.
  - Try residue classes next: `(channel_a - channel_b) mod 2`, then `mod 4`
    and `mod 8` if parity is noisy.
  - Render both the selected class and its inverse; one may be much easier to
    read.
  - Crop a readable patch and optionally scale with nearest-neighbor before
    transcription.
- Interpretation:
  - Repeated watermark text is often the answer, even when it looks like a
    prompt or sentence.
  - Submit the exact extracted `flag{...}` string before expanding acronyms,
    translating words, or answering the apparent question.
- Replay skeleton:

```bash
for pair in B:R R:B R:G G:R B:G G:B; do
  left=${pair%:*}
  right=${pair#*:}
  python scripts/sec.py probe image channel-diff \
    --case-dir <case-dir> --input <image> \
    --label "diff-${left}-${right}" \
    --left "$left" --right "$right" --all-maps
done

for m in 2 4 8; do
  for r in $(seq 0 $((m - 1))); do
    python scripts/sec.py probe image channel-mod \
      --case-dir <case-dir> --input <image> \
      --label "mod-${m}-${r}" \
      --left B --right R --modulus "$m" --remainder "$r"
  done
done
```

### Channel Difference Modulo Watermarks

- Signal:
  - Direct metadata, strings, and ordinary per-channel LSB scans are empty.
  - A hint, histogram imbalance, or residual image suggests comparing two color
    channels such as `B - R`.
  - Residual stretch or positive/negative maps may show faint repeated text but
    not enough contrast.
- First probes:
  - Run `ctf_image.py channel-diff` across likely channel pairs.
  - Render small residue classes with `ctf_image.py channel-mod`, especially
    `(B - R) mod 2 == 0` and `== 1`.
  - Crop a readable patch before relying on manual transcription.
- Screenshot-derived route:
  - The practical move is to turn the residual condition into a black/white
    image: `white` for pixels matching the selected difference residue and
    `black` for the rest.
  - If the mask repeats text across the image, crop any high-contrast area and
    read the watermark directly.
- Common route:
  - Use the residue mask as the final extracted layer.
  - If the extracted text is already in `flag{...}` format, submit the exact
    text first even when it reads like a question or clue.
- False leads:
  - Treating a question-looking `flag{...}` as a prompt to answer.
  - Spending time on AI verification, OCR, or semantic expansion before
    validating the extracted string.
- Useful tools:
  - `python scripts/sec.py probe image channel-mod --left B --right R --modulus 2 --remainder 0`
- Evidence to keep:
  - The generated residue mask, a cropped readable sample, and the command JSON
    summary with matched pixel ratio.
- Example cases:
  - [NO.10 Multimodal Identity](ctf-case-no10-multimodal-identity.md)

### Local Barcode Or Micro-Structure Check

- Signal:
  - A visually small square, border, high-contrast patch, or bottom/edge mark
    appears in an otherwise natural image.
  - Metadata, append checks, and ordinary LSB scans do not produce text.
- First probes:
  - Crop the suspicious patch and a wider context.
  - Run `ctf_image.py barcode-scan` on the full image, the edge band, and the
    tight crop. The command tries zxingcpp and OpenCV QR after common
    nearest-neighbor scale, padding, inversion, threshold, and rotation
    variants.
- Interpretation:
  - Accept the route only when a decoder returns stable text, a URL, a flag, or
    a clear 32-character body.
  - A code-like visual shape without decoder output is only a clue candidate,
    not proof of the algorithm or password.
- Replay skeleton:

```bash
python scripts/sec.py probe image barcode-scan \
  --case-dir <case-dir> --input <image> --label full

python scripts/sec.py probe image barcode-scan \
  --case-dir <case-dir> --input <image> --label suspicious-crop \
  --x <x> --y <y> --width <w> --height <h> \
  --scales 2 4 8 16 --pads 0 16 64 128
```

### ML Model Or Inference

- Inspect preprocessing, normalization, labels, thresholds, seed behavior, and
  output confidence.
- Probe with minimal input changes and record deltas.
- For model files, inventory architecture, weights, tokenizer/preprocessor,
  label map, quantization, adapters, and embedded metadata before attacks.

### Prompt Or Agent Tasks

- Separate system/developer/user-visible text from hidden target behavior.
- Look for instruction hierarchy, tool boundary, retrieval leakage, and output
  parser assumptions.
- Check prompt injection, context-window smuggling, retrieval source poisoning,
  and output parser confusion as separate hypotheses.

### Multimodal Image Prompt Injection To Prompt Leakage

- Signal:
  - A challenge asks a multimodal model to analyze a user-supplied image, or
    the user can modify the image before submitting it.
  - The image contains visible text that looks like an instruction rather than
    scene content, such as a request to reveal what the model is saying or what
    instructions it follows.
  - The model response includes copied policy/system text, an encoded blob, or
    content that should have stayed in a hidden prompt.
- First probes:
  - Preserve the original image and run a benign baseline analysis.
  - Add a small, readable text overlay to a natural part of the image and submit
    the modified image through the intended multimodal workflow.
  - Ask for ordinary content analysis; do not rely on metadata or pixel
    steganography until the visual-instruction path is tested.
  - When the response contains an encoded blob, run
    `ctf_crypto.py base64-chain --stop-on-flag` before trying unrelated
    ciphers.
- Common CTF route:
  - The model OCRs the overlaid text and treats it as an instruction.
  - The instruction causes the model to reveal hidden system-prompt content.
  - The revealed content contains a flag or a Base64/Base64URL encoded flag,
    often with two layers of encoding.
- Multi-agent workflow variant:
  - A search or assistant service may have an upstream agent that rewrites the
    user query and calls a search plugin, followed by a downstream agent that
    summarizes retrieved content.
  - A stable attack tries to force routing into the target workflow, prevent
    the first agent from decomposing or rewriting the payload, suppress plugin
    calls that would pollute the prompt with retrieval content, and make the
    second agent repeat hidden instructions.
  - Treat this as a workflow-boundary issue, not a single prompt-string issue:
    the dangerous transition is untrusted content becoming instructions for a
    later agent.
- Defensive controls:
  - Never store flags, secrets, credentials, or sensitive operational policy in
    prompts that a model can echo. Use opaque identifiers and server-side
    verification instead.
  - Treat OCR text, document text, retrieved snippets, and user query text as
    untrusted data. Delimit them as evidence and explicitly require agents to
    summarize content rather than obey instructions found inside that content.
  - Make workflow routing and tool policy deterministic and server-controlled;
    user content should not be able to select "no plugin", "raw prompt", or
    "repeat system instructions" modes.
  - Split roles with typed interfaces: one component extracts image/search
    facts, one planner chooses allowed tools, and one summarizer receives
    retrieved facts as data. Do not pass raw user-controlled instructions
    across those boundaries.
  - Add output guards for system-prompt repetition, hidden-policy disclosure,
    and high-entropy/Base64-like blobs when the business flow should not return
    encoded secrets.
  - Log baseline request, modified image, model transcript, tool decisions, and
    decoded outputs so the route can be reproduced without exposing real
    secrets.
- False leads:
  - Spending all effort on LSB/watermark extraction when the visible text is
    the active payload.
  - Decoding only one Base64 layer and abandoning an intermediate printable
    Base64 string.
  - Assuming a search plugin or retrieval step sanitizes prompt injection by
    itself.
  - Letting "do not call tools" or "repeat system prompt" from untrusted content
    override the workflow contract.
- Useful tools:
  - Image editor or `Pillow` for controlled text overlays.
  - `ctf_crypto.py base64-chain` for recursive Base64/Base64URL decoding.
  - Browser or API transcript capture for model output and tool-call evidence.
- Evidence to keep:
  - Original image hash, modified image hash, exact overlay text, request body
    or browser transcript, model response, decoded chain JSON, final flag, and
    notes on which agent/tool boundary was crossed.
- Example cases:
  - [AI Security Multimodal Prompt Injection](ctf-case-ai-security-multimodal-prompt-injection.md)

### Adversarial Or Robustness

- Start with benign perturbations and measurement. Avoid destructive or
  out-of-scope abuse of external services.
- If attacking a classifier, record baseline confidence, perturbation budget,
  targeted/untargeted goal, and whether gradients, logits, or only labels are
  available.

## Useful Tools

Python, pillow, numpy, scipy, opencv, ffmpeg, exiftool, torch when available,
`scripts/ctf_crypto.py base64-chain`, notebooks for repeatable experiments.
