# 邑网杯 CTF 2021 ,cipher2 ADFGVX 解题_euzen的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `邑网杯 CTF 2021 ,cipher2 ADFGVX 解题`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/邑网杯-CTF-2021-,cipher2-ADFGVX-解题_euzen的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E9%82%91%E7%BD%91%E6%9D%AF-CTF-2021-%2Ccipher2-ADFGVX-%E8%A7%A3%E9%A2%98_euzen%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/邑网杯-CTF-2021-,cipher2-ADFGVX-解题_euzen的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext challenges.

## Input Signals

- Artifacts: binary, ciphertext
- Tools: netcat, radare2
- Techniques: crypto-analysis, qr-analysis

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `1`
- `docs/img/96ace80db3ddc1159b015b920105376f.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 邑网杯 CTF 2021 ,cipher2 ADFGVX 解题_euzen的博客-CSDN博客

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/euzen/article/details/119085350](https://blog.csdn.net/euzen/article/details/119085350)`

### Step 3: 题目

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print enc.encipher('flag'+flag[5:-1])`

### Step 4: DXVGGVGGVGVFXAFVFXFFXFVFFFVFDVVGADGVAVGDAAVXGDGXGXDFVFDAVADAXAAFFVFXXGVX

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 5: 知识点

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ADFGVX加密的详细解释，可以阅读百度百科： [ADFGVX密码](https://baike.baidu.com/item/ADFGVX%E5%AF%86%E7%A0%81) ，曾经是德国的军用密码，后来被法国人破解。`

### Step 6: 解题思路

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `96ace80db3ddc1159b015b920105376f`

### Step 7: 解题脚本

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `if en_d == key_en : #与题目中的结果对比` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if en_d == key_en : #与题目中的结果对比`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `if en_d == key_en : #与题目中的结果对比` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flagfb0dd5203c02cf7c60dc99330b5bfa66`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
