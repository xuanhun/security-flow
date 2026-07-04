# [buuctf]crypto刷题学习记录（1-22）_hyxyan的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `buuctf`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/[buuctf]crypto刷题学习记录（1-22）_hyxyan的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%5Bbuuctf%5Dcrypto%E5%88%B7%E9%A2%98%E5%AD%A6%E4%B9%A0%E8%AE%B0%E5%BD%95%EF%BC%881-22%EF%BC%89_hyxyan%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/[buuctf]crypto刷题学习记录（1-22）_hyxyan的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: netcat, z3
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, http-analysis, php-tricks, symbolic-execution, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `12`
- `docs/img/a6f9df6bd7dd786b538673db9be1b568.png`
- `docs/img/0503ab67a919478986b9ea7faa9f9aa5.png`
- `docs/img/c602a04972d095a77210001fde7aa820.png`
- `docs/img/93a26f9520ff8474351055f2b22b6450.png`
- `docs/img/e2a60d2f58488659a1e06ac04ef01be6.png`
- `docs/img/1e363bcbe2620e3e2427253234980d60.png`
- `docs/img/71ffb8e75540b29445a5f6948ff75799.png`
- `docs/img/2dc7891df3a2d48d05e2e4f428e7a367.png`
- `docs/img/fd2a9e0d4b40ec41ddb28ea91be51426.png`
- `docs/img/1698e0e9f79e84d0b0db7fb9644f0469.png`
- `docs/img/2f4a0082797dcef15701678b43d1bffb.png`
- `docs/img/6c0dfe893f7f3fd1a1c705417c038fab.png`

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

### Step 2: [buuctf]crypto刷题学习记录（1-22）_hyxyan的博客-CSDN博客

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* * *`

### Step 3: 直接https://www.cmd5.com/解密可得flag{admin1}

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 4: 直接解码得flag{and 1=1}

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, z3 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `a6f9df6bd7dd786b538673db9be1b568`

### Step 5: 像凯撒密码形式，直接解密得flag{5cd1004d-86a5-46d8-b720-beb5ba0417e1}

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0503ab67a919478986b9ea7faa9f9aa5`

### Step 6: 直接base64解密得flag{THE_FLAG_OF_THIS_STRING}

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c602a04972d095a77210001fde7aa820`

### Step 7: 直接莫尔斯解密得flag{ILOVEYOU}

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `93a26f9520ff8474351055f2b22b6450`

### Step 8: 直接base64解密得BJD{W3lc0me_T0_BJDCTF}

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e2a60d2f58488659a1e06ac04ef01be6`

### Step 9: 试着将姓名头字母加数字得flag{zs19900315}

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, z3 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 10: 得出规律，写python脚本解得flag{Caesar_variation}

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print new_str`

### Step 11: 直接解码得flag{那你也很棒哦}

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, z3 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `1e363bcbe2620e3e2427253234980d60`

### Step 12: 直接http://www.jsons.cn/rabbitencrypt/解密可得flag{Cute_Rabbit}

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, z3 to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
