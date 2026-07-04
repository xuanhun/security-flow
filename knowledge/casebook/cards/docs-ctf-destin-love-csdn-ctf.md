# CTF基础解题_destin_love的博客-CSDN博客_ctf解题

## Case Metadata

- Category: `Crypto`
- Platform: `CTF基础解题`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF基础解题_destin_love的博客-CSDN博客_ctf解题.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E5%9F%BA%E7%A1%80%E8%A7%A3%E9%A2%98_destin_love%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf%E8%A7%A3%E9%A2%98.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF基础解题_destin_love的博客-CSDN博客_ctf解题.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext, ids challenges.

## Input Signals

- Artifacts: binary, ciphertext, ids, memory, stego-media, web-app
- Tools: angr, binwalk, foremost, netcat, pwntools, stegsolve, strings, volatility, z3
- Techniques: binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis, http-analysis, image-analysis, malware-static, memory-forensics, misc-analysis, php-tricks, qr-analysis, ssti, stego-extraction, stream-cipher, symbolic-execution, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `32`
- `docs/img/93a7792d760173b33c948699d681d89f.png`
- `docs/img/c90e855ecfed3ded64f80af36167bdbb.png`
- `docs/img/4fed6ff9580d5a18f80901fe98d14953.png`
- `docs/img/1586aeb54aabb83d65757ffaa2343483.png`
- `docs/img/2d99137e84d5d0692b81f49675d3bd56.png`
- `docs/img/5d82b239814c3033b060edd9f652e3df.png`
- `docs/img/ae181112b490273d82915e10b9b5f818.png`
- `docs/img/c7af985d264e0d595970cc17b7e17ac2.png`
- `docs/img/5e9a370ccc19931592090f3a87874a73.png`
- `docs/img/5189f720938046efa6bb84ccff38fa43.png`
- `docs/img/dabcae992ea0cd0046ad7bb02f94a0ac.png`
- `docs/img/391eadb66de636d1a18f0d5129c33efa.png`
- ... and `20` more

## Solve Thinking

### Step 1: Document

- Route type: `angr-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use angr, binwalk, foremost, netcat to collect the smallest evidence slice that answers the goal.
- Tools: angr, binwalk, foremost, netcat, pwntools
- Reasoning chain:
  - Recognize the section as angr-driven evidence lookup.
  - Use angr, binwalk, foremost, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF基础解题_destin_love的博客-CSDN博客_ctf解题

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use angr, binwalk, foremost, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: angr, binwalk, foremost, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use angr, binwalk, foremost, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_52084568/article/details/120530419](https://blog.csdn.net/weixin_52084568/article/details/120530419)`

### Step 3: 密码学

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use angr, binwalk, foremost, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: angr, binwalk, foremost, netcat, pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use angr, binwalk, foremost, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `密码是通信双方按约定的法则进行信息特殊变换的一种重要保密手段。依照这些法则，变明文为密文，称为加密变换；变密文为明文，称为脱密变换。密码在早期仅对文字或数码进行加、脱密变换，随着通信技术的发展，对语音、图像、数据等都可实施加、脱密变换。`

### Step 4: 专业术语

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Onion Routing`

### Step 5: 常见码制

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use netcat, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use netcat, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `B979FC0C210EBFF2CFFF20FAD9914D1E`

### Step 6: 换位密码

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use angr, binwalk, foremost, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: angr, binwalk, foremost, netcat, pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use angr, binwalk, foremost, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `列移位密码变化密码有Amsco密码 (Amsco Cipher)和 Cadenus密码 (Cadenus Cipher)。`

### Step 7: 替换加密

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use angr, binwalk, foremost, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: angr, binwalk, foremost, netcat, pwntools
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use angr, binwalk, foremost, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `93a7792d760173b33c948699d681d89f`

### Step 8: 其他有趣的机械密码

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5900760b96dd90c0bd0e561150c248e8`

### Step 9: brainfuck

- Route type: `angr-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use angr, binwalk, foremost, netcat to collect the smallest evidence slice that answers the goal.
- Tools: angr, binwalk, foremost, netcat, pwntools
- Reasoning chain:
  - Recognize the section as angr-driven evidence lookup.
  - Use angr, binwalk, foremost, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `(、>、<、+、-、.、,、[、]、)`

### Step 10: JOTHER

- Route type: `angr-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use angr, binwalk, foremost, netcat to collect the smallest evidence slice that answers the goal.
- Tools: angr, binwalk, foremost, netcat, pwntools
- Reasoning chain:
  - Recognize the section as angr-driven evidence lookup.
  - Use angr, binwalk, foremost, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `可在浏览器的console直接还原`

### Step 11: JSFUCK

- Route type: `angr-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use angr, binwalk, foremost, netcat to collect the smallest evidence slice that answers the goal.
- Tools: angr, binwalk, foremost, netcat, pwntools
- Reasoning chain:
  - Recognize the section as angr-driven evidence lookup.
  - Use angr, binwalk, foremost, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `使用6个字符[、]、(、)、!、+来编写JavaScript程序`

### Step 12: 区分Html编码与Unicode编码

- Route type: `angr-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use angr, binwalk, foremost, netcat to collect the smallest evidence slice that answers the goal.
- Tools: angr, binwalk, foremost, netcat, pwntools
- Reasoning chain:
  - Recognize the section as angr-driven evidence lookup.
  - Use angr, binwalk, foremost, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Unicode都以&#10结尾`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
