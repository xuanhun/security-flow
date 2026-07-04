# [GHCTF 2025]AI Cat Girl (Revenge)题解

## Case Metadata

- Category: `AI and Digital Watermark`
- Platform: `GHCTF 2025`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `ai/[GHCTF 2025]AI Cat Girl (Revenge).md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/ai/%5BGHCTF%202025%5DAI%20Cat%20Girl%20%28Revenge%29.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/ai/[GHCTF 2025]AI Cat Girl (Revenge).md`

## Why This Case Matters

Use this case as a AI and Digital Watermark reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: angr, netcat
- Techniques: classical-crypto, encoding-analysis, http-analysis, php-tricks, symbolic-execution, waf-bypass, web-exploitation

## First-Principles Route

- Inventory channels, metadata, layout, repeated motifs, and model- or watermark-specific residue before editing pixels.
- Test cheap residual views such as channel differences, modulo masks, OCR crops, and simple transforms before deeper reconstruction.
- Keep the final interpretation tied to the exact rendered artifact that exposes the hidden signal.

## Linked Assets

- Referenced assets: `1`
- `ai/images/AI_Cat_Girl(Revenge`

## Solve Thinking

### Step 1: 审题

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use angr, netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: angr, netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use angr, netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `依旧是猫娘，依旧是保守秘密，但是题目给了几点提示：`

### Step 2: 尝试1

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use angr, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: angr, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use angr, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `以下是失败的输出样例：`

### Step 3: 尝试2

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use angr, netcat to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: angr, netcat
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use angr, netcat to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `NSSCTF{1b0b0f26-c838-4508-9927-dbb6bf0e837e}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
