# [SWPU 2019]神奇的二维码

## Case Metadata

- Category: `Misc`
- Platform: `SWPU 2019`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `misc/[SWPU 2019]神奇的二维码.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/misc/%5BSWPU%202019%5D%E7%A5%9E%E5%A5%87%E7%9A%84%E4%BA%8C%E7%BB%B4%E7%A0%81.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/misc/[SWPU 2019]神奇的二维码.md`

## Why This Case Matters

Use this case as a Misc reference for ciphertext, stego-media challenges.

## Input Signals

- Artifacts: ciphertext, stego-media
- Tools: binwalk, netcat
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, image-analysis, misc-analysis, qr-analysis, stego-extraction

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `6`
- `misc/<images/[SWPU 2019]神奇的二维码-010editor.png>`
- `misc/<images/[SWPU 2019]神奇的二维码-binwalk.png>`
- `misc/<images/[SWPU 2019]神奇的二维码-base64.png>`
- `misc/<images/[SWPU 2019]神奇的二维码-base64解码.png>`
- `misc/<images/[SWPU 2019]神奇的二维码-Audacity.png>`
- `misc/images/[SWPU 2019]神奇的二维码-莫斯密码解码.png`

## Solve Thinking

### Step 1: [SWPU 2019]神奇的二维码

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `NSSCTF{morseisveryveryeasy}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
