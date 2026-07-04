# RSA算法原理及CTF解题_WHOAMIAnony的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `RSA算法原理及CTF解题`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/RSA算法原理及CTF解题_WHOAMIAnony的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/RSA%E7%AE%97%E6%B3%95%E5%8E%9F%E7%90%86%E5%8F%8ACTF%E8%A7%A3%E9%A2%98_WHOAMIAnony%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/RSA算法原理及CTF解题_WHOAMIAnony的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat
- Techniques: binary-exploitation, classical-crypto, command-injection, crypto-analysis, encoding-analysis, file-inclusion, http-analysis, misc-analysis, php-tricks, qr-analysis, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `34`
- `docs/img/334e80910694fc56f17572ff631701a7.png`
- `docs/img/da28097194304ce5221605611d500f23.png`
- `docs/img/f0e540ab5c3770e867a8ea2a03612b3a.png`
- `docs/img/38d565608384a53bcd3b1fb2977a5828.png`
- `docs/img/49eaf6c06cff767d27c682212f4045ab.png`
- `docs/img/62c867b31d31cf641bfe19ca31d10429.png`
- `docs/img/28bb4ebbf7c724f14b4d4bc71ed2a24b.png`
- `docs/img/3f248cd53d2a5384291fd48fd190cd58.png`
- `docs/img/b95672fc37e03a9e5649378a788d6ac5.png`
- `docs/img/e2e4fdf870159621c245e9a488a97853.png`
- `docs/img/ad4cb3379b77b97f7b18022c8e674b2d.png`
- `docs/img/414fff99dba474fe0ab69a71e8811176.png`
- ... and `22` more

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

### Step 2: RSA算法原理及CTF解题_WHOAMIAnony的博客-CSDN博客

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `已知c ，e，n（非常大），和 dp，dq，求解明文m`

### Step 3: 什么是RSA

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 公钥密码：加密和解密使用不同密码的方式，因此公钥密码通常也称为非对称密码。`

### Step 4: RSA加密

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `334e80910694fc56f17572ff631701a7`

### Step 5: RSA解密

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `| | |` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `| | |`
  - `| :-: | :-: |`
  - `| **公钥** | **（E，N）** |`
  - `| **私钥** | **（D，N）** |`
  - `| **密钥对** | **（E，D，N）** |`
  - `| 加密 | 密文＝明文^E mod N |`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `| | |` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f0e540ab5c3770e867a8ea2a03612b3a`

### Step 6: 生成密钥对

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `既然公钥是（E，N），私钥是（D，N）所以密钥对即为（E，D，N）但密钥对是怎样生成的？步骤如下：`

### Step 7: 1\. 求N

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `准备两个质数p，q。这两个数不能太小，太小则会容易破解，将p乘以q就是N`

### Step 8: 2\. 求欧拉函数φ(N)

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `然后计算欧拉函数φ(N)或L：`

### Step 9: 3\. 求E

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `之所以需要E和φ(N)的最大公约数为1是为了保证一定存在解密时需要使用的数D。现在我们已经求出了E和N也就是说我们已经生成了密钥对中的公钥了。`

### Step 10: 4\. 求D

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat with the extracted filter/query `| 求N | N＝ p ＊ q ；p，q为大质数 |` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `| 求N | N＝ p ＊ q ；p，q为大质数 |`
  - `| :-: | :-: |`
  - `| 求φ(N) | φ(N)＝ (p－1，q－1) |`
  - `| 求E | 1 < E < φ(N)，gcd(E，φ(N))=1；E，φ(N)最大公约数为1（E和L互质） |`
  - `| 求D | 1 < D < φ(N)，(E＊D) mod φ(N) ＝ 1 |`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat with the extracted filter/query `| 求N | N＝ p ＊ q ；p，q为大质数 |` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `| 求φ(N) | φ(N)＝ (p－1，q－1) |`

### Step 11: CTF中的常见RSA题型

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `49eaf6c06cff767d27c682212f4045ab`

### Step 12: 已知p、q、e，求d

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `62c867b31d31cf641bfe19ca31d10429`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
