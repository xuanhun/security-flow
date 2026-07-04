# CTF题解四 逆向 顺藤摸瓜（ISCC2017）_目标是技术宅的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `CTF题解四 逆向 顺藤摸瓜（ISCC2017）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF题解四-逆向-顺藤摸瓜（ISCC2017）_目标是技术宅的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E9%A2%98%E8%A7%A3%E5%9B%9B-%E9%80%86%E5%90%91-%E9%A1%BA%E8%97%A4%E6%91%B8%E7%93%9C%EF%BC%88ISCC2017%EF%BC%89_%E7%9B%AE%E6%A0%87%E6%98%AF%E6%8A%80%E6%9C%AF%E5%AE%85%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF题解四-逆向-顺藤摸瓜（ISCC2017）_目标是技术宅的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary, ciphertext challenges.

## Input Signals

- Artifacts: binary, ciphertext
- Tools: ida
- Techniques: crypto-analysis, encoding-analysis, qr-analysis, reverse-engineering

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `4`
- `docs/img/30f686c6a22a50f0f2094678d6a1567b.png`
- `docs/img/9a1ca76b8841e35f352b7abd55360e26.png`
- `docs/img/3e6799a50079c4b26e6ce0fa2e042b8b.png`
- `docs/img/c43d416231de1d4b6021dc3b05be1aa9.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF题解四 逆向 顺藤摸瓜（ISCC2017）_目标是技术宅的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/ljfyyj/article/details/81017322](https://blog.csdn.net/ljfyyj/article/details/81017322)`

### Step 3: 首先在IDA中找到main函数：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `30f686c6a22a50f0f2094678d6a1567b`

### Step 4: 观察sub_400796函数：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `9a1ca76b8841e35f352b7abd55360e26`

### Step 5: 观察sub_400937函数：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c43d416231de1d4b6021dc3b05be1aa9`

### Step 6: 猜测随机数的种子：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: ``0x67616C66`。`

### Step 7: sub_400937解密：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ``vhex{bykfnpl_lgtn_tr_xzsl_lavp_ghbsgekwntn}``

### Step 8: sub_400796解密：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida with the extracted filter/query `if (c[k] == b[26 * ((i - 97) % 26) + (a[k % 26] - 97) % 26]) {` and inspect the matching evidence.
- Tools: ida
- Filters or commands:
  - `if (c[k] == b[26 * ((i - 97) % 26) + (a[k % 26] - 97) % 26]) {`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida with the extracted filter/query `if (c[k] == b[26 * ((i - 97) % 26) + (a[k % 26] - 97) % 26]) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag{decrypt_game_is_very_very_interesting}`

### Step 9: 反思：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2.猜测&0x200的意义。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
