# [MoeCTF 2022] Base

## Case Metadata

- Category: `Reverse`
- Platform: `MoeCTF 2022`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `reverse/[MoeCTF 2022] Base.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/reverse/%5BMoeCTF%202022%5D%20Base.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/reverse/[MoeCTF 2022] Base.md`
- Challenge URL: `https://www.nssctf.cn/problem/3319`

## Why This Case Matters

Use this case as a Reverse reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: IDA Pro, DIE, detect-it-easy, ida, radare2
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, qr-analysis, reverse-engineering, web-exploitation

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `6`
- `reverse/images/[MoeCTF 2022] Base_1.png`
- `reverse/images/[MoeCTF 2022] Base_2.png`
- `reverse/images/[MoeCTF 2022] Base_3.png`
- `reverse/images/[MoeCTF 2022] Base_4.png`
- `reverse/images/[MoeCTF 2022] Base_5.png`
- `reverse/images/[MoeCTF 2022] Base_6.png`

## Solve Thinking

### Step 1: 1 看到什么

- Route type: `IDA Pro-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use IDA Pro, DIE, detect-it-easy, ida to collect the smallest evidence slice that answers the goal.
- Tools: IDA Pro, DIE, detect-it-easy, ida, radare2
- Reasoning chain:
  - Recognize the section as IDA Pro-driven evidence lookup.
  - Use IDA Pro, DIE, detect-it-easy, ida to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `下载附件后发现是一个名为base的exe运行文件`

### Step 2: 2 解题思路

- Route type: `IDA Pro-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use IDA Pro, DIE, detect-it-easy, ida to collect the smallest evidence slice that answers the goal.
- Tools: IDA Pro, DIE, detect-it-easy, ida, radare2
- Reasoning chain:
  - Recognize the section as IDA Pro-driven evidence lookup.
  - Use IDA Pro, DIE, detect-it-easy, ida to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `显然，我们需要对这个文件进行反汇编逆向分析，猜测需要分析反汇编后的代码，然后编写脚本得出flag，同时，结合题目名字和文件名，猜测会用到base系列的编码。`

### Step 3: 3 ✅ 尝试过程和结果记录

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, radare2 with the extracted filter/query `此时，聪明的人已经想到直接将字符串进行base64解码就可以得到flag。==但是==，这里有个**坑**，初学者很容易犯，就是函数`base64_decode`，我们并没有查看里面的代码具体是什么，就直接判断了，出题人是可以随意更改里面的内容的。` and inspect the matching evidence.
- Tools: ida, radare2
- Filters or commands:
  - `此时，聪明的人已经想到直接将字符串进行base64解码就可以得到flag。==但是==，这里有个**坑**，初学者很容易犯，就是函数`base64_decode`，我们并没有查看里面的代码具体是什么，就直接判断了，出题人是可以随意更改里面的内容的。`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, radare2 with the extracted filter/query `此时，聪明的人已经想到直接将字符串进行base64解码就可以得到flag。==但是==，这里有个**坑**，初学者很容易犯，就是函数`base64_decode`，我们并没有查看里面的代码具体是什么，就直接判断了，出题人是可以随意更改里面的内容的。` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `s1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'`

### Step 4: 换表

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use radare2 to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use radare2 to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `en_text = '1wX/yRrA4RfR2wj72Qv52x3L5qa='`

### Step 5: 将换表字符映射回标准表

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use IDA Pro, DIE, detect-it-easy, ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: IDA Pro, DIE, detect-it-easy, ida, radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use IDA Pro, DIE, detect-it-easy, ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `所以flag是`moectf{qwqbase_qwq}``

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
