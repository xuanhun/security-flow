# 第6篇：基础入门~加密编码算法_廖一语山的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `第6篇：基础入门~加密编码算法`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/第6篇：基础入门~加密编码算法_廖一语山的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E7%AC%AC6%E7%AF%87%EF%BC%9A%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8~%E5%8A%A0%E5%AF%86%E7%BC%96%E7%A0%81%E7%AE%97%E6%B3%95_%E5%BB%96%E4%B8%80%E8%AF%AD%E5%B1%B1%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/第6篇：基础入门~加密编码算法_廖一语山的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: not detected
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, php-tricks, sql-injection, web-exploitation

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `9`
- `docs/img/b572d16e37ee932d01f7d0ac2f9c308b.png`
- `docs/img/7825f7f9981b2ce4844425c46c84cbd8.png`
- `docs/img/847ab633c6e86fda5bce9fbbd8640c36.png`
- `docs/img/50399e1f3ffba84bbb771d74b46080b4.png`
- `docs/img/a69028e1d9dcb5f59cbcfc3ca46fe0d7.png`
- `docs/img/2264bf3acc3ff194544749d665d18bf2.png`
- `docs/img/da06983c437cabdec4e733f2c1459d5e.png`
- `docs/img/78607088e2adec2e0e5f80091d3a8e1b.png`
- `docs/img/e8be069d1f1705986d8b9c4d44b3ed37.png`

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

### Step 2: 第6篇：基础入门~加密编码算法_廖一语山的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 3: 前言

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 4: 常见加密编码等算法解析

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool with the extracted filter/query `BASE64：密文相应于明文长度变长。大小写数字混编（区分大小写）。密文字符串末经常出现“==”（也会一个、也会没有）。便于代码的加密，对参数进行加密等。网站常见` and inspect the matching evidence.
- Filters or commands:
  - `BASE64：密文相应于明文长度变长。大小写数字混编（区分大小写）。密文字符串末经常出现“==”（也会一个、也会没有）。便于代码的加密，对参数进行加密等。网站常见`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool with the extracted filter/query `BASE64：密文相应于明文长度变长。大小写数字混编（区分大小写）。密文字符串末经常出现“==”（也会一个、也会没有）。便于代码的加密，对参数进行加密等。网站常见` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `b572d16e37ee932d01f7d0ac2f9c308b`

### Step 5: 常见加密形式算法解析

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**自定义组合**：利用常见的加密方式加上自定的一些规则`

### Step 6: 常见解密方式（针对）

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `枚举，自定义逆向算法，可逆向`

### Step 7: 了解常规加密算法的特性

- Route type: `evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 8: 某 CTF 比赛题目解析：脚本自定义算法组合逆向

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `847ab633c6e86fda5bce9fbbd8640c36`

### Step 9: 某 CMS 密码加密解密

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `a69028e1d9dcb5f59cbcfc3ca46fe0d7`

### Step 10: 某 URL 加密地址的漏洞测试

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use the artifact-specific tool with the extracted filter/query `> eII8c3JeL0t0dxM7wb3Nzg==` and inspect the matching evidence.
- Filters or commands:
  - `> eII8c3JeL0t0dxM7wb3Nzg==`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use the artifact-specific tool with the extracted filter/query `> eII8c3JeL0t0dxM7wb3Nzg==` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e8be069d1f1705986d8b9c4d44b3ed37`

### Step 11: 某实际应用 URL 地址参数加密

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool with the extracted filter/query `搜索网址结尾为“id=MQ==”（加密过的数字1）的网址：“inurl:id=MQ==”` and inspect the matching evidence.
- Filters or commands:
  - `搜索网址结尾为“id=MQ==”（加密过的数字1）的网址：“inurl:id=MQ==”`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool with the extracted filter/query `搜索网址结尾为“id=MQ==”（加密过的数字1）的网址：“inurl:id=MQ==”` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 12: 涉及资源：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use the artifact-specific tool to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://ctf.bugku.com/challenges`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
