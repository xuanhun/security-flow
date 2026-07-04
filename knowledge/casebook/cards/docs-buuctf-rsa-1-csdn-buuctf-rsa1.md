# BUUCTF RSA题目全解1_宁嘉的博客-CSDN博客_buuctf rsa1

## Case Metadata

- Category: `Crypto`
- Platform: `BUUCTF RSA题目全解1`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF-RSA题目全解1_宁嘉的博客-CSDN博客_buuctf-rsa1.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF-RSA%E9%A2%98%E7%9B%AE%E5%85%A8%E8%A7%A31_%E5%AE%81%E5%98%89%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_buuctf-rsa1.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF-RSA题目全解1_宁嘉的博客-CSDN博客_buuctf-rsa1.md`

## Why This Case Matters

Use this case as a Crypto reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: not detected
- Techniques: crypto-analysis, encoding-analysis, http-analysis, php-tricks, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `10`
- `docs/img/5862abed27f69d3ec91ec5d66779e681.png`
- `docs/img/ca62f3d133dd2e0769c01f958fc442ce.png`
- `docs/img/1449859a9473a645bedf8924eb44234d.png`
- `docs/img/2484fb37f020c8c11a123983f5b64c73.png`
- `docs/img/044dc3224fa2f6e55acec8d6404abf58.png`
- `docs/img/758c209a87c770f7dc9181320a1a29d1.png`
- `docs/img/f06515daad512e78b528580f89f57b43.png`
- `docs/img/05dd5c6066c683f8f9b63e62c504be41.png`
- `docs/img/80be0ca6086f7f4675bccd44be90bae8.png`
- `docs/img/25b0785546df73d6d5ee4565633a597d.png`

## Solve Thinking

### Step 1: Document

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF RSA题目全解1_宁嘉的博客-CSDN博客_buuctf rsa1

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/mikecoke/article/details/105967809](https://blog.csdn.net/mikecoke/article/details/105967809)`

### Step 3: RSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5862abed27f69d3ec91ec5d66779e681`

### Step 4: rsarsa

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1449859a9473a645bedf8924eb44234d`

### Step 5: RSA1

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `至于flag是16进制转文本还是10进制数，我忘记了，自己试一下吧。`

### Step 6: RSA2

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `print(bytes.fromhex(hex(m)[2:]))`

### Step 7: RSA3

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `运行得到flag`

### Step 8: RSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `044dc3224fa2f6e55acec8d6404abf58`

### Step 9: RSAROLL

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[BUUCTF RSAROLL](https://blog.csdn.net/MikeCoke/article/details/106146568)`

### Step 10: [BJDCTF 2nd]rsa0

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[[BJDCTF 2nd] RSA0](https://blog.csdn.net/MikeCoke/article/details/106144002)`

### Step 11: Dangerous RSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool with the extracted filter/query `if(gmpy2.iroot(c+i*n,3)[1]==1): #开根号` and inspect the matching evidence.
- Filters or commands:
  - `if(gmpy2.iroot(c+i*n,3)[1]==1): #开根号`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool with the extracted filter/query `if(gmpy2.iroot(c+i*n,3)[1]==1): #开根号` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `758c209a87c770f7dc9181320a1a29d1`

### Step 12: rsa2

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f06515daad512e78b528580f89f57b43`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
