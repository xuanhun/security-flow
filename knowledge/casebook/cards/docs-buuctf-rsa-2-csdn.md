# BUUCTF RSA题目全解2_宁嘉的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `BUUCTF RSA题目全解2`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF-RSA题目全解2_宁嘉的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF-RSA%E9%A2%98%E7%9B%AE%E5%85%A8%E8%A7%A32_%E5%AE%81%E5%98%89%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF-RSA题目全解2_宁嘉的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for ciphertext challenges.

## Input Signals

- Artifacts: ciphertext
- Tools: netcat, radare2
- Techniques: crypto-analysis

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `21`
- `docs/img/8aa94ff74a319035d2a838355f57c8cf.png`
- `docs/img/1ef8ddc2b7aff7abe32e27fa0a4e8c4b.png`
- `docs/img/d1a7a575b3a9f006d67796f8d3d91a39.png`
- `docs/img/c85581d9fee0a278a9052599e4a8e0a7.png`
- `docs/img/f627df17a321477716618b0fb495939e.png`
- `docs/img/b6c66806e6424ef65fa5e67b39718ee6.png`
- `docs/img/df4a7ab52217fc9576607cbc64b02748.png`
- `docs/img/2b1ae60b917d35847cd61fb56373d711.png`
- `docs/img/4abc80f41feb0ead92e5e0051bbb1bcd.png`
- `docs/img/7de20b50b0ec8deff2c37f346dff4dfb.png`
- `docs/img/ffde27596f9ec36b513e7783619f1fdb.png`
- `docs/img/3c8149aabeda74baa7a4943d1ac24d66.png`
- ... and `9` more

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

### Step 2: BUUCTF RSA题目全解2_宁嘉的博客-CSDN博客

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/MikeCoke/article/details/107206707](https://blog.csdn.net/MikeCoke/article/details/107206707)`

### Step 3: [NCTF2019]childRSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8aa94ff74a319035d2a838355f57c8cf`

### Step 4: [HDCTF2019]bbbbbbrsa

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `d1a7a575b3a9f006d67796f8d3d91a39`

### Step 5: SameMod

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f627df17a321477716618b0fb495939e`

### Step 6: [BJDCTF2020]RSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `b6c66806e6424ef65fa5e67b39718ee6`

### Step 7: [GKCTF2020]babycrypto

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 8: p>>128<<128:0xe4e4b390c1d201dae2c00a4669c0865cc5767bc444f5d310f3cfc75872d96feb89e556972c99ae20753e3314240a52df5dccd076a47c6b5d11b531b92d901b2b512aeb0b263bbfd624fe3d52e5e238beeb581ebe012b2f176a4ffd1e0d2aa8c4d3a2656573b727

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `df4a7ab52217fc9576607cbc64b02748`

### Step 9: [GWCTF 2019]BabyRSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2 with the extracted filter/query `0assert(len(flag) == 38)` and inspect the matching evidence.
- Tools: netcat, radare2
- Filters or commands:
  - `0assert(len(flag) == 38)`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2 with the extracted filter/query `0assert(len(flag) == 38)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4abc80f41feb0ead92e5e0051bbb1bcd`

### Step 10: [BJDCTF2020]rsa_output

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{r3a_C0mmoN_moD@_4ttack}`

### Step 11: [ACTF新生赛2020]crypto-rsa0

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `51fe58112c537a570956345fbca7749e`

### Step 12: [BJDCTF2020]easyrsa

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2d12fff353de2a21e425721384955d67`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
