# [羊城杯 2020] easyre

## Case Metadata

- Category: `Reverse`
- Platform: `羊城杯 2020`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `reverse/[羊城杯 2020] easyre.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/reverse/%5B%E7%BE%8A%E5%9F%8E%E6%9D%AF%202020%5D%20easyre.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/reverse/[羊城杯 2020] easyre.md`
- Challenge URL: `https://www.nssctf.cn/problem/1416`

## Why This Case Matters

Use this case as a Reverse reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: IDA Pro, die, detect-it-easy, ida, netcat, radare2
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, reverse-engineering, web-exploitation

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `5`
- `reverse/images/[羊城杯 2020] easyre_1.png`
- `reverse/images/[羊城杯 2020] easyre_2.png`
- `reverse/images/[羊城杯 2020] easyre_3.png`
- `reverse/images/[羊城杯 2020] easyre_4.png`
- `reverse/images/[羊城杯 2020] easyre_5.png`

## Solve Thinking

### Step 1: 1 看到什么

- Route type: `IDA Pro-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use IDA Pro, die, detect-it-easy, ida to collect the smallest evidence slice that answers the goal.
- Tools: IDA Pro, die, detect-it-easy, ida, netcat
- Reasoning chain:
  - Recognize the section as IDA Pro-driven evidence lookup.
  - Use IDA Pro, die, detect-it-easy, ida to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `下载附件后发现是一个名为easyre的exe运行文件`

### Step 2: 2 解题思路

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `既然是exe文件，那么思路仍是查壳，有壳脱，无壳直接丢进IDA分析，再写脚本得出flag`

### Step 3: 3 ✅ 尝试过程和结果记录

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat, radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `encrypted_str = "EmBmP5Pmn7QcPU4gLYKv5QcMmB3PWHcP5YkPq3=cT6QckkPckoRG"`

### Step 4: 逆向三步处理

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `672cc4778a38e80cb362987341133ea2`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
