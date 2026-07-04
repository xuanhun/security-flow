# [SWPUCTF 2024 秋季新生赛] 动态调试

## Case Metadata

- Category: `Reverse`
- Platform: `SWPUCTF 2024 秋季新生赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `reverse/[SWPUCTF 2024 秋季新生赛] 动态调试 .md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/reverse/%5BSWPUCTF%202024%20%E7%A7%8B%E5%AD%A3%E6%96%B0%E7%94%9F%E8%B5%9B%5D%20%E5%8A%A8%E6%80%81%E8%B0%83%E8%AF%95%20.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/reverse/[SWPUCTF 2024 秋季新生赛] 动态调试 .md`
- Challenge URL: `https://www.nssctf.cn/problem/5985`

## Why This Case Matters

Use this case as a Reverse reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: IDA Pro, Die, dbg, detect-it-easy, gdb, ida
- Techniques: classical-crypto, crypto-analysis, http-analysis, reverse-engineering, stream-cipher, web-exploitation

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `13`
- `reverse/images/[SWPUCTF 2024 秋季新生赛] 动态调试_1.png`
- `reverse/images/[SWPUCTF 2024 秋季新生赛] 动态调试_2.png`
- `reverse/images/[SWPUCTF 2024 秋季新生赛] 动态调试_3.png`
- `reverse/images/[SWPUCTF 2024 秋季新生赛] 动态调试_4.png`
- `reverse/images/[SWPUCTF 2024 秋季新生赛] 动态调试_5.png`
- `reverse/images/[SWPUCTF 2024 秋季新生赛] 动态调试_6.png`
- `reverse/images/[SWPUCTF 2024 秋季新生赛] 动态调试_7.png`
- `reverse/images/[SWPUCTF 2024 秋季新生赛] 动态调试_8.png`
- `reverse/images/[SWPUCTF 2024 秋季新生赛] 动态调试_9.png`
- `reverse/images/[SWPUCTF 2024 秋季新生赛] 动态调试_10.png`
- `reverse/images/[SWPUCTF 2024 秋季新生赛] 动态调试_11.png`
- `reverse/images/[SWPUCTF 2024 秋季新生赛] 动态调试_12.png`
- ... and `1` more

## Solve Thinking

### Step 1: 1 看到什么

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use IDA Pro, Die, dbg, detect-it-easy to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: IDA Pro, Die, dbg, detect-it-easy, gdb
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use IDA Pro, Die, dbg, detect-it-easy to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `下载附件后发现是rc4.exe文件`

### Step 2: 2 解题思路

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `这个题其实只用静态调试就能做出来，我第一遍就是这样，但是多少有些不尊重题目名字，于是用动态又做了一遍，发现动态简单许多，别有一番风味。`

### Step 3: 3 ✅ 尝试过程和结果记录

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: ``rc4_crypt(s, v2, len)`便是加密函数，最后将处理后的V2和V1进行比较，全都相同就是正确的flag，那么思路就是V1反方向进行RC4解密即可，于是有两种做法。`

### Step 4: 静态：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use IDA Pro, Die, dbg, detect-it-easy to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: IDA Pro, Die, dbg, detect-it-easy, gdb
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use IDA Pro, Die, dbg, detect-it-easy to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `def rc4_init(key: bytes):`

### Step 5: 初始化状态 S 和辅助数组 K

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use IDA Pro, Die, dbg, detect-it-easy to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: IDA Pro, Die, dbg, detect-it-easy, gdb
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use IDA Pro, Die, dbg, detect-it-easy to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `S = rc4_init(key)`

### Step 6: 用 bytearray 可原地修改

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use IDA Pro, Die, dbg, detect-it-easy to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: IDA Pro, Die, dbg, detect-it-easy, gdb
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use IDA Pro, Die, dbg, detect-it-easy to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `rc4_crote(S, buf, key)`

### Step 7: 以 0x00 为结束符，打印前面的所有字符

- Route type: `IDA Pro-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use IDA Pro, Die, dbg, detect-it-easy to collect the smallest evidence slice that answers the goal.
- Tools: IDA Pro, Die, dbg, detect-it-easy, gdb
- Reasoning chain:
  - Recognize the section as IDA Pro-driven evidence lookup.
  - Use IDA Pro, Die, dbg, detect-it-easy to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `运行即可得到flag：`NSSCTF{0d6f90ac-4b5e-4efb-8502-6349cf798f2e}``

### Step 8: 动态：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use gdb, ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: gdb, ida
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use gdb, ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `它的值已经被修改成flag，转成字符即可。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
