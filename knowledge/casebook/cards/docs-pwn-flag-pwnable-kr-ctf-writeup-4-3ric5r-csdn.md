# PWN flag [pwnable.kr]CTF writeup题解系列4_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `PWN flag [pwnable.kr]CTF writeup题解系列4`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/PWN-flag-[pwnable.kr]CTF-writeup题解系列4_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/PWN-flag-%5Bpwnable.kr%5DCTF-writeup%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%974_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/PWN-flag-[pwnable.kr]CTF-writeup题解系列4_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: ida, john, netcat
- Techniques: binary-exploitation, command-injection, http-analysis, password-cracking, reverse-engineering, web-exploitation

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `5`
- `docs/img/ec24061263cc33a7949c69d660adddc4.png`
- `docs/img/73657e4b2fcbb43c02935a1e97d8f912.png`
- `docs/img/438532b84a44e3d67b63d84dfd46a99c.png`
- `docs/img/7fc5990dae66c3b5332e8b2e4da55769.png`
- `docs/img/8450da7fb0884dc11a4aa59752470631.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, john, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, john, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, john, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: PWN flag [pwnable.kr]CTF writeup题解系列4_3riC5r的博客-CSDN博客

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use ida, john, netcat with the extracted filter/query `Connecting to pwnable.kr (pwnable.kr)|128.61.240.205|:80... connected.` and inspect the matching evidence.
- Tools: ida, john, netcat
- Filters or commands:
  - `Connecting to pwnable.kr (pwnable.kr)|128.61.240.205|:80... connected.`
  - `flag 100%[=================================================>] 327.43K 162KB/s in 2.0s`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use ida, john, netcat with the extracted filter/query `Connecting to pwnable.kr (pwnable.kr)|128.61.240.205|:80... connected.` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `128.61.240.205`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
