# [SWPUCTF 2021 新生赛]ez_caesar

## Case Metadata

- Category: `Crypto`
- Platform: `SWPUCTF 2021 新生赛`
- Difficulty: `简单`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `crypto/[SWPUCTF 2021 新生赛]ez_caesar.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/crypto/%5BSWPUCTF%202021%20%E6%96%B0%E7%94%9F%E8%B5%9B%5Dez_caesar.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/crypto/[SWPUCTF 2021 新生赛]ez_caesar.md`
- Challenge URL: `https://www.nssctf.cn/problem/430`

## Why This Case Matters

Use this case as a Crypto reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: 随波逐流6.6
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `3`
- `crypto/image/ez_caesar_题目代码.png`
- `crypto/image/ez_caesar_decodebase64.png`
- `crypto/image/ez_caesar_decode_caesar.png`

## Solve Thinking

### Step 1: 题目

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use 随波逐流6.6 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: 随波逐流6.6
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use 随波逐流6.6 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 给出的密文可以明显看出是base64加密`

### Step 2: 解题思路

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use 随波逐流6.6 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: 随波逐流6.6
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use 随波逐流6.6 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 先解密密文得到密文2，而后对密文2解密`

### Step 3: 尝试过程和结果记录

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use 随波逐流6.6 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: 随波逐流6.6
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use 随波逐流6.6 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `![alt text](./image/ez_caesar_decode_caesar.png)`

### Step 4: 参考文献

- Route type: `随波逐流6.6-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 随波逐流6.6 to collect the smallest evidence slice that answers the goal.
- Tools: 随波逐流6.6
- Reasoning chain:
  - Recognize the section as 随波逐流6.6-driven evidence lookup.
  - Use 随波逐流6.6 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `无`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
