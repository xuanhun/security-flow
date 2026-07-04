# python求解二元二次方程组_【CTF WriteUp】2020祥云杯Crypto题解_张仁鹏的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `python求解二元二次方程组`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/python求解二元二次方程组_【CTF-WriteUp】2020祥云杯Crypto题解_张仁鹏的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/python%E6%B1%82%E8%A7%A3%E4%BA%8C%E5%85%83%E4%BA%8C%E6%AC%A1%E6%96%B9%E7%A8%8B%E7%BB%84_%E3%80%90CTF-WriteUp%E3%80%912020%E7%A5%A5%E4%BA%91%E6%9D%AFCrypto%E9%A2%98%E8%A7%A3_%E5%BC%A0%E4%BB%81%E9%B9%8F%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/python求解二元二次方程组_【CTF-WriteUp】2020祥云杯Crypto题解_张仁鹏的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext challenges.

## Input Signals

- Artifacts: binary, ciphertext
- Tools: detect-it-easy, netcat, pwntools
- Techniques: binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis, qr-analysis

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat, pwntools
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: python求解二元二次方程组_【CTF WriteUp】2020祥云杯Crypto题解_张仁鹏的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat, pwntools with the extracted filter/query `assert n == p * q` and inspect the matching evidence.
- Tools: detect-it-easy, netcat, pwntools
- Filters or commands:
  - `assert n == p * q`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat, pwntools with the extracted filter/query `assert n == p * q` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `#!/usr/bin/env python`

### Step 3: -*- coding: utf-8 -*-

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use detect-it-easy, netcat, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: detect-it-easy, netcat, pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use detect-it-easy, netcat, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `#!/usr/bin/env python`

### Step 4: -*- coding: utf-8 -*-

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use detect-it-easy, netcat, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: detect-it-easy, netcat, pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use detect-it-easy, netcat, pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `#!/usr/bin/env python`

### Step 5: -*- coding: utf-8 -*-

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat, pwntools
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cc= vector(ZZ,res)`

### Step 6: Babai's Nearest Plane algorithm

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `#!/usr/bin/env python`

### Step 7: -*- coding: utf-8 -*-

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use pwntools to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `8.131.69.237`

### Step 8: passPoW

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `digest = re.findall(r'== (.*?)\n', rec)[0]` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `digest = re.findall(r'== (.*?)\n', rec)[0]`
  - `io.recvuntil(',_|\n\n')`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `digest = re.findall(r'== (.*?)\n', rec)[0]` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print(flag)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
