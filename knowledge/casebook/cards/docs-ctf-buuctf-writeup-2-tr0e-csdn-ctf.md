# CTF杂项-BUUCTF竞赛真题WriteUp(2）_Tr0e的博客-CSDN博客_ctf竞赛试题及答案

## Case Metadata

- Category: `Misc`
- Platform: `CTF杂项`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF杂项-BUUCTF竞赛真题WriteUp(2）_Tr0e的博客-CSDN博客_ctf竞赛试题及答案.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E6%9D%82%E9%A1%B9-BUUCTF%E7%AB%9E%E8%B5%9B%E7%9C%9F%E9%A2%98WriteUp%282%EF%BC%89_Tr0e%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf%E7%AB%9E%E8%B5%9B%E8%AF%95%E9%A2%98%E5%8F%8A%E7%AD%94%E6%A1%88.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF杂项-BUUCTF竞赛真题WriteUp(2）_Tr0e的博客-CSDN博客_ctf竞赛试题及答案.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, pcap challenges.

## Input Signals

- Artifacts: binary, ciphertext, pcap, stego-media, web-app
- Tools: binwalk, ida, steghide, stegsolve, wireshark
- Techniques: classical-crypto, crypto-analysis, dns-analysis, encoding-analysis, http-analysis, image-analysis, misc-analysis, network-forensics, qr-analysis, reverse-engineering, service-enumeration, stego-extraction, traffic-analysis, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `152`
- `docs/img/4dabddf2c6f3734a69b7fc7830efd77a.png`
- `docs/img/964919cec24b103a61450a34bdafa4ef.png`
- `docs/img/eadf5376f4c8bc4ee1ccde7c91a66e68.png`
- `docs/img/fc5d6d3d5928d9fe32b9b2063aefabcb.png`
- `docs/img/eb14da58f81ec9583fe6a61d4dea8a9c.png`
- `docs/img/91a4660fc0967ef7f6c561452637d1f6.png`
- `docs/img/1abafe6b0d6b9f1344807362dbc000fc.png`
- `docs/img/ccaaee7e00c53c42ae983018b8c35b05.png`
- `docs/img/0aafa894a8beb2a05259b5846fb8c7d7.png`
- `docs/img/65afe20d3101b719f882e3d4f7b2580c.png`
- `docs/img/6daf4f4b39a6e3808d519a7e3cdecb65.png`
- `docs/img/48fd5d24589d29c3a792b2856be36fe6.png`
- ... and `140` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use binwalk, ida, steghide, stegsolve to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: binwalk, ida, steghide, stegsolve, wireshark
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use binwalk, ida, steghide, stegsolve to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF杂项-BUUCTF竞赛真题WriteUp(2）_Tr0e的博客-CSDN博客_ctf竞赛试题及答案

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, ida, steghide, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, ida, steghide, stegsolve, wireshark
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, ida, steghide, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_39190897/article/details/116430110](https://blog.csdn.net/weixin_39190897/article/details/116430110)`

### Step 3: 前言

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use binwalk, ida, steghide, stegsolve to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: binwalk, ida, steghide, stegsolve, wireshark
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use binwalk, ida, steghide, stegsolve to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `为了划水过几天的“ 红帽杯 ” 网络安全大赛，学习并记录下 BUUCTF 平台的杂项部分题目，因为去年参加“ 强网杯 ”网络安全大赛发现杂项类型的题目还是可以争取得分的，也希望过几天运气好点吧…`

### Step 4: No.1 Git动图分解提取信息

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use stegsolve with the extracted filter/query `| 功能键 | 作用 |` and inspect the matching evidence.
- Tools: stegsolve
- Filters or commands:
  - `| 功能键 | 作用 |`
  - `| --- | --- |`
  - `| File Format | 文件格式，这个主要是查看图片的具体信息 |`
  - `| Data Extract | 数据抽取，图片中隐藏数据的抽取 |`
  - `| Frame Browser | 帧浏览器，主要是对GIF之类的动图进行分解，动图变成一张张图片，便于查看 |`
  - `| Image Combiner | 拼图，图片拼接 |`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use stegsolve with the extracted filter/query `| 功能键 | 作用 |` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4dabddf2c6f3734a69b7fc7830efd77a`

### Step 5: No.2 隐藏文件提取与爆破

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `91a4660fc0967ef7f6c561452637d1f6`

### Step 6: N0.3 Base64编码还原图片

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, ida, steghide, stegsolve to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, ida, steghide, stegsolve, wireshark
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, ida, steghide, stegsolve to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `94e07b2b9076c716cd36a57a8ff8b68e`

### Step 7: No.4 winhex修改图片大小

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, ida, steghide, stegsolve to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, ida, steghide, stegsolve, wireshark
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, ida, steghide, stegsolve to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `47842e1cf4a296c7d58f4aab4a816c4b`

### Step 8: No.5 编辑器查看图片隐写

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use binwalk, ida, steghide, stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: binwalk, ida, steghide, stegsolve, wireshark
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use binwalk, ida, steghide, stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dbe2091193d56fffa39475ad6e8c0e60`

### Step 9: No.6 LSB隐写的信息导出

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: stegsolve
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6569944d154956518884fa5c16319e20`

### Step 10: No.7 图片属性中隐藏信息

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use binwalk, ida, steghide, stegsolve to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: binwalk, ida, steghide, stegsolve, wireshark
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use binwalk, ida, steghide, stegsolve to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9f365b89e8a155620bb4b4215c081630`

### Step 11: No.8 LSB隐写的数据抽取

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use binwalk, stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: binwalk, stegsolve
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use binwalk, stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2e6ef8961232932d07058914c9376a84`

### Step 12: No.9 RAR文件加密的爆破

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, stegsolve to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, stegsolve
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, stegsolve to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4d3541a1a8bffc07b50df5f8ffe606d6`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
