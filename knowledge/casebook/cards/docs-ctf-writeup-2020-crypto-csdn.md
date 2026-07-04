# 【CTF WriteUp】2020网鼎杯第二场Crypto题解_零食商人的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `【CTF WriteUp】2020网鼎杯第二场Crypto题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF-WriteUp】2020网鼎杯第二场Crypto题解_零食商人的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF-WriteUp%E3%80%912020%E7%BD%91%E9%BC%8E%E6%9D%AF%E7%AC%AC%E4%BA%8C%E5%9C%BACrypto%E9%A2%98%E8%A7%A3_%E9%9B%B6%E9%A3%9F%E5%95%86%E4%BA%BA%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF-WriteUp】2020网鼎杯第二场Crypto题解_零食商人的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for ciphertext challenges.

## Input Signals

- Artifacts: ciphertext
- Tools: netcat, z3
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, qr-analysis, symbolic-execution

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `1`
- `docs/img/1977e2a72663bbd1a3075dcd79266312.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, z3 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【CTF WriteUp】2020网鼎杯第二场Crypto题解_零食商人的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/cccchhhh6819/article/details/106134649](https://blog.csdn.net/cccchhhh6819/article/details/106134649)`

### Step 3: b64

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1977e2a72663bbd1a3075dcd79266312`

### Step 4: -*- coding: utf-8 -*-

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use netcat, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use netcat, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `依次提交，其中某一个为正确答案`

### Step 5: rand

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `#!/usr/bin/env python`

### Step 6: -*- coding: utf-8 -*-

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `print BinToStr(plaintext)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
