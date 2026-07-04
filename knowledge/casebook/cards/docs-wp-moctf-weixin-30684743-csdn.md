# 【二进制】【WP】MOCTF逆向题解_weixin_30684743的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `【二进制】【WP】MOCTF逆向题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【二进制】【WP】MOCTF逆向题解_weixin_30684743的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90%E4%BA%8C%E8%BF%9B%E5%88%B6%E3%80%91%E3%80%90WP%E3%80%91MOCTF%E9%80%86%E5%90%91%E9%A2%98%E8%A7%A3_weixin_30684743%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【二进制】【WP】MOCTF逆向题解_weixin_30684743的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary, ciphertext challenges.

## Input Signals

- Artifacts: binary, ciphertext
- Tools: ida
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, reverse-engineering

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `31`
- `docs/img/efc9453076042693f171b6916d8f9b7c.png`
- `docs/img/d657a1bbb5dc7488800f1f90f7c8da51.png`
- `docs/img/b4f0344670a1dec23b7bca6b59aae80b.png`
- `docs/img/9c18bac17b90d9ee2425f9403b3972be.png`
- `docs/img/4c8aa0d82924694f71c23713b03de42b.png`
- `docs/img/ee61c49bc6343e66f2d2eae6a65b7e38.png`
- `docs/img/dcd99f050a4668e5f55b78701c5d5b4a.png`
- `docs/img/d68ccfc2435247a61baf9a8dddc8ffd4.png`
- `docs/img/ab4681a2599e0c685a60c443effd3535.png`
- `docs/img/db592b60e6197dae5bf13b0491eb103c.png`
- `docs/img/2db2b128fe56cc85beb377edad681098.png`
- `docs/img/93c167424913e48e28af6d330071991d.png`
- ... and `19` more

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

### Step 2: 【二进制】【WP】MOCTF逆向题解_weixin_30684743的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_30684743/article/details/101336980](https://blog.csdn.net/weixin_30684743/article/details/101336980)`

### Step 3: moctf 逆向第一题：SOEASY

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这个是个 64 位的软件，OD 打不开，只能用 IDA64 打开，直接搜字符串（shift+F12）就可以看到`

### Step 4: moctf 逆向第二题：跳跳跳

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `efc9453076042693f171b6916d8f9b7c`

### Step 5: moctf 逆向第三题：暗恋的苦恼

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dcd99f050a4668e5f55b78701c5d5b4a`

### Step 6: moctf 逆向第四题：crackme1

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `b88964d98430d01546f15dbf75e947be`

### Step 7: moctf 逆向第五题：crackme2

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `23ea8fef150f1bf67ae0fcdbd04cd694`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
