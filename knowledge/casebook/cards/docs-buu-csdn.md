# buu逆向刷题（二）_北风~的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `buu逆向刷题（二）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/buu逆向刷题（二）_北风~的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/buu%E9%80%86%E5%90%91%E5%88%B7%E9%A2%98%EF%BC%88%E4%BA%8C%EF%BC%89_%E5%8C%97%E9%A3%8E~%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/buu逆向刷题（二）_北风~的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: ida, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, file-inclusion, http-analysis, misc-analysis, php-tricks, reverse-engineering, web-exploitation

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Linked Assets

- Referenced assets: `10`
- `docs/img/d6fa34112ced4a14c46693ccfc96ff7c.png`
- `docs/img/62b9773327ab0a90fc0d1a5a678da0ff.png`
- `docs/img/269692bfdfc36d80b153641c0ef430b9.png`
- `docs/img/edf8b1107d1693d0a67942ec6212879a.png`
- `docs/img/8a2b40015d5d1e0d6d3e4f2cf2ba0dc6.png`
- `docs/img/5958de983b04b86efeb3efb6eb70fe47.png`
- `docs/img/a91485cac7a062654363d7b93fbf9dbb.png`
- `docs/img/40d7643328dbf104af1277dced889150.png`
- `docs/img/fcc7f6655023dbd3d3e34e6693c066a8.png`
- `docs/img/8f84189394f4993ca0f513fe69c0a7e0.png`

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

### Step 2: buu逆向刷题（二）_北风~的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_45055269/article/details/108748458](https://blog.csdn.net/weixin_45055269/article/details/108748458)`

### Step 3: Java逆向解密

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `print(chr((i^0x20)-ord('@')),end='')`

### Step 4: 刮开有奖

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use ida, netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use ida, netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8个字符拼接在一起。`

### Step 5: findit

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - The proof is the plaintext structure or key schedule step that explains why the decoded output is correct.
- Evidence rule: The proof is the plaintext structure or key schedule step that explains why the decoded output is correct.

### Step 6: parallel-comparator-200

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `d6fa34112ced4a14c46693ccfc96ff7c`

### Step 7: 8086

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `16位汇编，DOSBox跑一下，好吧，啥也没有，IDA打开，字符串与0x1F的异或。`

### Step 8: [GKCTF2020]Check_1n

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `师傅牛逼，控制台里的虚拟电脑，搜索中文字符串拿到开机密码HelloWorld，打砖块游戏，死亡得flag。`

### Step 9: luck_guy

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `62b9773327ab0a90fc0d1a5a678da0ff`

### Step 10: 简单注册器

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dd2940c04462b4dd7c450528835cca15`

### Step 11: rsa

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `算法题，真不错，公钥求私钥，解密密文`

### Step 12: 公钥解析（提取e，n）

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use ida, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `edf8b1107d1693d0a67942ec6212879a`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
