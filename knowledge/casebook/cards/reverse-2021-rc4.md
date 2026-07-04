# **[长城杯 2021 政企组]魔鬼凯撒的RC4茶室**

## Case Metadata

- Category: `Reverse`
- Platform: `长城杯 2021 政企组`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `reverse/[长城杯 2021 政企组]魔鬼凯撒的RC4茶室.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/reverse/%5B%E9%95%BF%E5%9F%8E%E6%9D%AF%202021%20%E6%94%BF%E4%BC%81%E7%BB%84%5D%E9%AD%94%E9%AC%BC%E5%87%AF%E6%92%92%E7%9A%84RC4%E8%8C%B6%E5%AE%A4.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/reverse/[长城杯 2021 政企组]魔鬼凯撒的RC4茶室.md`

## Why This Case Matters

Use this case as a Reverse reference for ciphertext challenges.

## Input Signals

- Artifacts: ciphertext
- Tools: not detected
- Techniques: classical-crypto, crypto-analysis, stream-cipher

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Solve Thinking

### Step 1: **[长城杯 2021 政企组]魔鬼凯撒的RC4茶室**

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

### Step 2: 考点

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `----`

### Step 3: 思路

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `然后再根据附件得到的加密后的flag文件，反推得到前半段flag的值flag{x1aom1ng_1s_3o_easy_`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
