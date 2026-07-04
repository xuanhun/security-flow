# BUUCTF Reverse解题记录（三）_sxhthreo的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `BUUCTF Reverse解题记录（三）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF-Reverse解题记录（三）_sxhthreo的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF-Reverse%E8%A7%A3%E9%A2%98%E8%AE%B0%E5%BD%95%EF%BC%88%E4%B8%89%EF%BC%89_sxhthreo%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF-Reverse解题记录（三）_sxhthreo的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary, ciphertext challenges.

## Input Signals

- Artifacts: binary, ciphertext
- Tools: radare2
- Techniques: crypto-analysis, qr-analysis

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `1`
- `docs/img/b8e18de8a839f28bccc2c63a0c7e9afa.png`

## Solve Thinking

### Step 1: Document

- Route type: `radare2-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use radare2 to collect the smallest evidence slice that answers the goal.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as radare2-driven evidence lookup.
  - Use radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF Reverse解题记录（三）_sxhthreo的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/sxH3O/article/details/123262906](https://blog.csdn.net/sxH3O/article/details/123262906)`

### Step 3: 第九题：不一样的flag

- Route type: `radare2-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use radare2 with the extracted filter/query `if ( v7[5 * *(_DWORD *)&v3[25] - 41 + v4] == 49 )` and inspect the matching evidence.
- Tools: radare2
- Filters or commands:
  - `if ( v7[5 * *(_DWORD *)&v3[25] - 41 + v4] == 49 )`
  - `if ( v7[5 * *(_DWORD *)&v3[25] - 41 + v4] == 35 )`
- Reasoning chain:
  - Recognize the section as radare2-driven evidence lookup.
  - Use radare2 with the extracted filter/query `if ( v7[5 * *(_DWORD *)&v3[25] - 41 + v4] == 49 )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `b8e18de8a839f28bccc2c63a0c7e9afa`

### Step 4: 第十题：SimpleRev

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use radare2 with the extracted filter/query `if ( v1 == 10 )` and inspect the matching evidence.
- Tools: radare2
- Filters or commands:
  - `if ( v1 == 10 )`
  - `if ( v1 == 32 )`
  - `if ( v1 <= 96 || v1 > 122 )`
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use radare2 with the extracted filter/query `if ( v1 == 10 )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `最后解得flag为KLDQCUDFZO。`

### Step 5: 第十一题：Java逆向解密

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2022.3.3 22：52`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
