# [SWPUCTF 2022 新生赛] upx

## Case Metadata

- Category: `Reverse`
- Platform: `SWPUCTF 2022 新生赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `reverse/[SWPUCTF 2022 新生赛] upx.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/reverse/%5BSWPUCTF%202022%20%E6%96%B0%E7%94%9F%E8%B5%9B%5D%20upx.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/reverse/[SWPUCTF 2022 新生赛] upx.md`
- Challenge URL: `https://www.nssctf.cn/problem/2653`

## Why This Case Matters

Use this case as a Reverse reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: UPX, IDA Pro, die, detect-it-easy, ida, netcat, radare2
- Techniques: crypto-analysis, http-analysis, reverse-engineering, web-exploitation

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `4`
- `reverse/images/[SWPUCTF 2022 新生赛] upx_1.png`
- `reverse/images/[SWPUCTF 2022 新生赛] upx_2.png`
- `reverse/images/[SWPUCTF 2022 新生赛] upx_3.png`
- `reverse/images/[SWPUCTF 2022 新生赛] upx_4.png`

## Solve Thinking

### Step 1: 📌 壳介绍：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `加壳之后（以UPX为例），如果别人用工具（如IDA）打开它，只会看到加密/压缩后的内容，而不是原始代码。`

### Step 2: 1 看到什么

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use UPX, IDA Pro, die, detect-it-easy to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: UPX, IDA Pro, die, detect-it-easy, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use UPX, IDA Pro, die, detect-it-easy to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `下载附件后发现是zip文件，解压后发现是p04.exe文件`

### Step 3: 2 解题思路

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `既然还是exe文件，那么思路大致仍然是查壳，有壳脱，无壳直接丢进IDA进行静态调试分析，分析不出就用动态调试，再写脚本得出flag`

### Step 4: 3 ✅ 尝试过程和结果记录

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use detect-it-easy, ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: detect-it-easy, ida, netcat, radare2
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use detect-it-easy, ida, netcat, radare2 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `得到flag：NSSCTF{UPX_1s_xord_way_to_encrypt_flag}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
