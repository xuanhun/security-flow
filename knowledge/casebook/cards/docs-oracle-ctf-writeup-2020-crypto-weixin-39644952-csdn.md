# 最后一位被整除 oracle,【CTF WriteUp】2020第四届强网杯部分Crypto题解_weixin_39644952的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `最后一位被整除`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/最后一位被整除-oracle,【CTF-WriteUp】2020第四届强网杯部分Crypto题解_weixin_39644952的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E6%9C%80%E5%90%8E%E4%B8%80%E4%BD%8D%E8%A2%AB%E6%95%B4%E9%99%A4-oracle%2C%E3%80%90CTF-WriteUp%E3%80%912020%E7%AC%AC%E5%9B%9B%E5%B1%8A%E5%BC%BA%E7%BD%91%E6%9D%AF%E9%83%A8%E5%88%86Crypto%E9%A2%98%E8%A7%A3_weixin_39644952%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/最后一位被整除-oracle,【CTF-WriteUp】2020第四届强网杯部分Crypto题解_weixin_39644952的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext challenges.

## Input Signals

- Artifacts: binary, ciphertext
- Tools: netcat, pwntools
- Techniques: binary-exploitation, crypto-analysis, encoding-analysis

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `4`
- `docs/img/e0e8bd9c3f5665aae68168f23cd655ea.png`
- `docs/img/b7dee84d75bcfe2850fb10a5201713ec.png`
- `docs/img/598d3104956bfe18bb65f6dde523376a.png`
- `docs/img/c03632876c42efd87f7a32f411b4eb8a.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 最后一位被整除 oracle,【CTF WriteUp】2020第四届强网杯部分Crypto题解_weixin_39644952的博客-CSDN博客

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `[+] assert len(secret)==16` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `[+] assert len(secret)==16`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `[+] assert len(secret)==16` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `552ebbeb9276a8cd9f741b7d29f8c9e1eb455757207ac420659e7eab56ddee25`

### Step 3: -*- coding: utf-8 -*-

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, pwntools with the extracted filter/query `print "==========================="` and inspect the matching evidence.
- Tools: netcat, pwntools
- Filters or commands:
  - `print "==========================="`
  - `f.write("=== ")`
  - `print "==============================="`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, pwntools with the extracted filter/query `print "==========================="` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `106.14.66.172`

### Step 4: pass the PoW

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `print p.recvuntil("[-] your choice:")`

### Step 5: Step 1

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print p.recvuntil("[-] your choice:")`

### Step 6: Step 2

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `80808080808080808080808080808080`

### Step 7: Step 3

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print p.recvuntil("[-] your choice:")`

### Step 8: Step 4(finished)

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `98c2ae1ef3ff5aee4999172ec6bd32f3`

### Step 9: Step 5(finished)

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6122db344a73a14e8247fb2856fbbf94`

### Step 10: Step 6(finished)

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0a1c9e1464925d23d4a3068313b407ee`

### Step 11: -*- coding: utf-8 -*-

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `print "p = " + str(p)`

### Step 12: p = 149580444233086025790179573414856711556292635219028492250676309233306926698347672114881938858364663009604584293251087505211665595084567645013671843742930965283973691725982783226085450276850737892819830479107029360437

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use netcat, pwntools to align timestamps and identify the event that satisfies the question.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use netcat, pwntools to align timestamps and identify the event that satisfies the question.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dc69f07434a25cdb6365168e44471560`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
