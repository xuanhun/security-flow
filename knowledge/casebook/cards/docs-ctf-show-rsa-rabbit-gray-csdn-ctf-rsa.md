# ctf.show RSA入门题目题解若干_Rabbit_Gray的博客-CSDN博客_ctf中rsa实验题解析

## Case Metadata

- Category: `Crypto`
- Platform: `ctf.show RSA入门题目题解若干`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/ctf.show-RSA入门题目题解若干_Rabbit_Gray的博客-CSDN博客_ctf中rsa实验题解析.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/ctf.show-RSA%E5%85%A5%E9%97%A8%E9%A2%98%E7%9B%AE%E9%A2%98%E8%A7%A3%E8%8B%A5%E5%B9%B2_Rabbit_Gray%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf%E4%B8%ADrsa%E5%AE%9E%E9%AA%8C%E9%A2%98%E8%A7%A3%E6%9E%90.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/ctf.show-RSA入门题目题解若干_Rabbit_Gray的博客-CSDN博客_ctf中rsa实验题解析.md`

## Why This Case Matters

Use this case as a Crypto reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat
- Techniques: crypto-analysis, dns-analysis, http-analysis, qr-analysis, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: ctf.show RSA入门题目题解若干_Rabbit_Gray的博客-CSDN博客_ctf中rsa实验题解析

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 3: babyrsa 普通rsa解密

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* * *`

### Step 4: easyrsa1 n太小可以直接分解

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1455925529734358105461406532259911790807347616464991065301847`

### Step 5: easyrsa2 两个n有公因数

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* * *`

### Step 6: easyrsa3 相同的n，共模攻击

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `assert libnum.gcd(e1, e2)==1` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `assert libnum.gcd(e1, e2)==1`
  - `assert s1*s2<0 and q==1`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `assert libnum.gcd(e1, e2)==1` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* * *`

### Step 7: easyrsa4 e很小，n和c比较大

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* * *`

### Step 8: easyrsa5 e很大，n和c比较大

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* * *`

### Step 9: easyrsa6 p和q很接近

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `yafu-x64.exe`

### Step 10: easyrsa7 已知p的部分高位

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* * *`

### Step 11: easyrsa8 p很小导致n可被分解

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `assert p*q==n` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `assert p*q==n`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `assert p*q==n` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `得到明文：flag{p_1s_5mall_num6er}`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
