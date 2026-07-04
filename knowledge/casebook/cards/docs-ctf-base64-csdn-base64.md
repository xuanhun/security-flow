# CTF - Base64换表_建瓯最坏的博客-CSDN博客_base64换表

## Case Metadata

- Category: `Crypto`
- Platform: `CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF---Base64换表_建瓯最坏的博客-CSDN博客_base64换表.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF---Base64%E6%8D%A2%E8%A1%A8_%E5%BB%BA%E7%93%AF%E6%9C%80%E5%9D%8F%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_base64%E6%8D%A2%E8%A1%A8.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF---Base64换表_建瓯最坏的博客-CSDN博客_base64换表.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext challenges.

## Input Signals

- Artifacts: binary, ciphertext
- Tools: ida, netcat
- Techniques: classical-crypto, encoding-analysis, qr-analysis, reverse-engineering

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `8`
- `docs/img/4687557b0453e4dc8fa6f6ecb3b58e92.png`
- `docs/img/602abf9f30d89ec84cd58824d69aef6f.png`
- `docs/img/def3d130c05aa4d85f80ffa30a29d570.png`
- `docs/img/7d65ea7260b08dd76f08f82d4339ac0c.png`
- `docs/img/b91f658f66f240bec3f60f89ba3b28cf.png`
- `docs/img/db79ed1af21c047e2f327ea0eaf9a60b.png`
- `docs/img/b5cbb351965128531082ba2d6c73690e.png`
- `docs/img/7d8761eeb7a0761bfbc89e973c18e4ba.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF - Base64换表_建瓯最坏的博客-CSDN博客_base64换表

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/JiangBuLiu/article/details/117661772](https://blog.csdn.net/JiangBuLiu/article/details/117661772)`

### Step 3: 复制保存为16进制即可得文件

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `4687557b0453e4dc8fa6f6ecb3b58e92`

### Step 4: IDA显示

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `602abf9f30d89ec84cd58824d69aef6f`

### Step 5: 题目解读

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `def3d130c05aa4d85f80ffa30a29d570`

### Step 6: 提示：base64程序逆向

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `7d65ea7260b08dd76f08f82d4339ac0c`

### Step 7: 题目特点

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - The proof is the code path, comparison, constant, or decoded data that explains the answer.
- Evidence rule: The proof is the code path, comparison, constant, or decoded data that explains the answer.

### Step 8: Base64表格

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `b91f658f66f240bec3f60f89ba3b28cf`

### Step 9: 位移

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ``>> 0/6/12/18 & 0x3F``

### Step 10: 等号补位

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `上面提到了，这里就不赘述了`

### Step 11: Base64变体 - 换表

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `db79ed1af21c047e2f327ea0eaf9a60b`

### Step 12: Base64变体 - 题外话

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `b5cbb351965128531082ba2d6c73690e`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
