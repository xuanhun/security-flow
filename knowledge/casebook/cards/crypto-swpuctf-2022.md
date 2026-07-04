# [SWPUCTF 2022 新生赛]什锦

## Case Metadata

- Category: `Crypto`
- Platform: `SWPUCTF 2022 新生赛`
- Difficulty: `中等`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `crypto/[SWPUCTF 2022 新生赛]什锦.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/crypto/%5BSWPUCTF%202022%20%E6%96%B0%E7%94%9F%E8%B5%9B%5D%E4%BB%80%E9%94%A6.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/crypto/[SWPUCTF 2022 新生赛]什锦.md`
- Challenge URL: `https://www.nssctf.cn/problem/2644`

## Why This Case Matters

Use this case as a Crypto reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: 随波逐流6.6 [社会主义核心价值观密码解码工具] https:, ctf.bugku.com, tool, cvecode
- Techniques: crypto-analysis, encoding-analysis, http-analysis, php-tricks, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `6`
- `crypto/image/什锦-codeB.png`
- `crypto/image/什锦-codeC.png`
- `crypto/image/什锦-猪圈密码.png`
- `crypto/image/什锦-brainfuck.png`
- `crypto/image/什锦-brainfuck解码.png`
- `crypto/image/什锦-ascii码转中文.png`

## Solve Thinking

### Step 1: 题目

- Route type: `随波逐流6.6 [社会主义核心价值观密码解码工具] https:-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use 随波逐流6.6 [社会主义核心价值观密码解码工具] https:, ctf.bugku.com, tool, cvecode to collect the smallest evidence slice that answers the goal.
- Tools: 随波逐流6.6 [社会主义核心价值观密码解码工具] https:, ctf.bugku.com, tool, cvecode
- Reasoning chain:
  - Recognize the section as 随波逐流6.6 [社会主义核心价值观密码解码工具] https:-driven evidence lookup.
  - Use 随波逐流6.6 [社会主义核心价值观密码解码工具] https:, ctf.bugku.com, tool, cvecode to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `![alt text](./image/什锦-codeC.png)<br>`

### Step 2: 解题思路

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use 随波逐流6.6 [社会主义核心价值观密码解码工具] https:, ctf.bugku.com, tool, cvecode to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: 随波逐流6.6 [社会主义核心价值观密码解码工具] https:, ctf.bugku.com, tool, cvecode
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use 随波逐流6.6 [社会主义核心价值观密码解码工具] https:, ctf.bugku.com, tool, cvecode to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* 题目中明确说出flag的组成，所以按照顺序解密即可`

### Step 3: 尝试过程和结果记录

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use 随波逐流6.6 [社会主义核心价值观密码解码工具] https:, ctf.bugku.com, tool, cvecode to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: 随波逐流6.6 [社会主义核心价值观密码解码工具] https:, ctf.bugku.com, tool, cvecode
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use 随波逐流6.6 [社会主义核心价值观密码解码工具] https:, ctf.bugku.com, tool, cvecode to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `最终将CodeABC连接起来进行MD5加密即可。`

### Step 4: 参考文献

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use 随波逐流6.6 [社会主义核心价值观密码解码工具] https:, ctf.bugku.com, tool, cvecode to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: 随波逐流6.6 [社会主义核心价值观密码解码工具] https:, ctf.bugku.com, tool, cvecode
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use 随波逐流6.6 [社会主义核心价值观密码解码工具] https:, ctf.bugku.com, tool, cvecode to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-[CTF之密码学（BF与Ook）](https://blog.csdn.net/qq_73792226/article/details/143990891)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
