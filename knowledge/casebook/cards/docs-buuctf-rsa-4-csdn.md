# BUUCTF RSA题目全解4_宁嘉的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `BUUCTF RSA题目全解4`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF-RSA题目全解4_宁嘉的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF-RSA%E9%A2%98%E7%9B%AE%E5%85%A8%E8%A7%A34_%E5%AE%81%E5%98%89%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF-RSA题目全解4_宁嘉的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for ciphertext challenges.

## Input Signals

- Artifacts: ciphertext
- Tools: netcat, radare2, z3
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, symbolic-execution

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `6`
- `docs/img/e385d5ea50ea500c243320add0061ee9.png`
- `docs/img/e0fe68c86041605cff832149437492f0.png`
- `docs/img/7e1e2bff1313034f34c2dde36df3e385.png`
- `docs/img/9935355d90fc8b5cd5015734fcad124a.png`
- `docs/img/6e7cd6759ad4cebabf6ae60a5c22249d.png`
- `docs/img/b7c3af47c5e70577bb9590fc851b915e.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF RSA题目全解4_宁嘉的博客-CSDN博客

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/MikeCoke/article/details/108540699](https://blog.csdn.net/MikeCoke/article/details/108540699)`

### Step 3: [MRCTF2020]babyRSA

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 with the extracted filter/query `assert (gcd(_E, (_P - 1) * (_Q - 1)) == 1)` and inspect the matching evidence.
- Tools: z3
- Filters or commands:
  - `assert (gcd(_E, (_P - 1) * (_Q - 1)) == 1)`
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 with the extracted filter/query `assert (gcd(_E, (_P - 1) * (_Q - 1)) == 1)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `206027926847308612719677572554991143421`

### Step 4: [WUSTCTF2020]dp_leaking_1s_very_d@angerous

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `print(n2s(m))`

### Step 5: [De1CTF2019]babyrsa

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6e7cd6759ad4cebabf6ae60a5c22249d`

### Step 6: 4\. [V&N2020 公开赛]CRT

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Use netcat, radare2 with the extracted filter/query `r2, m2 = Q` and inspect the matching evidence.
- Tools: netcat, radare2
- Filters or commands:
  - `r2, m2 = Q`
  - `assert (r2-r1) % d == 0`
- Reasoning chain:
  - Recognize the section as indicator enrichment.
  - Use netcat, radare2 with the extracted filter/query `r2, m2 = Q` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `284461942441737992421992210219060544764`

### Step 7: [V&N2020 公开赛]easy_RSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print(long_to_bytes(m))`

### Step 8: [V&N2020 公开赛]Fast

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `b7c3af47c5e70577bb9590fc851b915e`

### Step 9: [MRCTF2020]Easy_RSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use radare2 with the extracted filter/query `assert (gcd(_E, (_P - 1) * (_Q - 1)) == 1)` and inspect the matching evidence.
- Tools: radare2
- Filters or commands:
  - `assert (gcd(_E, (_P - 1) * (_Q - 1)) == 1)`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use radare2 with the extracted filter/query `assert (gcd(_E, (_P - 1) * (_Q - 1)) == 1)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print(n2s(_M))`

### Step 10: [NPUCTF2020]EzRSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `phi = gift*8`

### Step 11: 因为 (p-1)  * (q-1) < n ，所以gcd(p-1,q-1)有阈值,为8

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**NPUCTF{diff1cult_rsa_1s_e@sy}**`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
