# BUUCTF misc 解题记录 二（超级详细）_Vayn3的博客-CSDN博客

## Case Metadata

- Category: `Misc`
- Platform: `BUUCTF misc 解题记录 二（超级详细）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF-misc-解题记录-二（超级详细）_Vayn3的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF-misc-%E8%A7%A3%E9%A2%98%E8%AE%B0%E5%BD%95-%E4%BA%8C%EF%BC%88%E8%B6%85%E7%BA%A7%E8%AF%A6%E7%BB%86%EF%BC%89_Vayn3%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF-misc-解题记录-二（超级详细）_Vayn3的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, ids challenges.

## Input Signals

- Artifacts: binary, ciphertext, ids, pcap, stego-media, web-app
- Tools: binwalk, foremost, hashcat, ida, netcat, tshark, wireshark
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, image-analysis, misc-analysis, network-forensics, password-cracking, php-tricks, reverse-engineering, stego-extraction, traffic-analysis, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `64`
- `docs/img/252fd65df63bf5e5d3ed019ff8164f05.png`
- `docs/img/02e48e7431e67962414507ec81d3cd4d.png`
- `docs/img/fb207896c0ec424b8f0157466eb24e80.png`
- `docs/img/210a61d796db5f79706909cd9d0cc92d.png`
- `docs/img/304e32a8aaf2b432dff1a7b24d53d05e.png`
- `docs/img/374aa1e4f2206c053311328ebb2e8546.png`
- `docs/img/79100da966f5ee2509aaa35cc4ed744e.png`
- `docs/img/2cb4fe94b64343b1a20712cdfedd9029.png`
- `docs/img/f0b327534958a4c43ca66009e54b45da.png`
- `docs/img/3f99e0ef55f1ed7a270e857bb1fc065f.png`
- `docs/img/a8ee9e25c9254599aff990a031b36257.png`
- `docs/img/d866a01d4eb64eb38e3c8e3bee3f8123.png`
- ... and `52` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use binwalk, foremost, hashcat, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: binwalk, foremost, hashcat, ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use binwalk, foremost, hashcat, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF misc 解题记录 二（超级详细）_Vayn3的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, foremost, hashcat, ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, foremost, hashcat, ida, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, foremost, hashcat, ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_51090016/article/details/115712647](https://blog.csdn.net/qq_51090016/article/details/115712647)`

### Step 3: [SUCTF2018]followme（kali下搜索整个文件夹）

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, foremost, hashcat, ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, foremost, hashcat, ida, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, foremost, hashcat, ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `252fd65df63bf5e5d3ed019ff8164f05`

### Step 4: 蜘蛛侠呀（tshark提取数据）

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, tshark with the extracted filter/query `tshark -r out.pcap -T fields -e data > data.txt` and inspect the matching evidence.
- Tools: netcat, tshark
- Filters or commands:
  - `tshark -r out.pcap -T fields -e data > data.txt`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, tshark with the extracted filter/query `tshark -r out.pcap -T fields -e data > data.txt` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `02e48e7431e67962414507ec81d3cd4d`

### Step 5: [RCTF2019]draw（logo解释器）

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, foremost, hashcat, ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, foremost, hashcat, ida, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, foremost, hashcat, ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `79100da966f5ee2509aaa35cc4ed744e`

### Step 6: **[MRCTF2020]不眠之夜**（montage和gaps）

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use binwalk, foremost, hashcat, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: binwalk, foremost, hashcat, ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use binwalk, foremost, hashcat, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2cb4fe94b64343b1a20712cdfedd9029`

### Step 7: [安洵杯 2019]easy misc（盲水印）

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, foremost with the extracted filter/query `QW8obWdIWT9pMkFSQWtRQjVfXiE/WSFTajBtcw==` and inspect the matching evidence.
- Tools: binwalk, foremost
- Filters or commands:
  - `QW8obWdIWT9pMkFSQWtRQjVfXiE/WSFTajBtcw==`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, foremost with the extracted filter/query `QW8obWdIWT9pMkFSQWtRQjVfXiE/WSFTajBtcw==` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f0b327534958a4c43ca66009e54b45da`

### Step 8: [MRCTF2020]Hello_ misc

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, foremost, hashcat, ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, foremost, hashcat, ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, foremost, hashcat, ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4786ef9cfc180afcb8e29e3a250b1692`

### Step 9: [BSidesSF2019]zippy（密码解压）

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, foremost, hashcat, ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, foremost, hashcat, ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, foremost, hashcat, ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2a3b94e13aa79bfee0cb3d2a4b9f7782`

### Step 10: [ACTF新生赛2020]明文攻击(隐藏文件内容在010)

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, hashcat, ida to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, hashcat, ida, netcat
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, hashcat, ida to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5a28b0f9a99385495011267fc1a788c8`

### Step 11: 粽子的来历（脑洞太大 ff修复 行间距问题）

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, foremost, hashcat, ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk, foremost, hashcat, ida, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, foremost, hashcat, ida to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3e2db7e44f706e011dea3e17b1d1457d`

### Step 12: 派大星的烦恼（倒过来的二进制）

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use binwalk, foremost, hashcat, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: binwalk, foremost, hashcat, ida, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use binwalk, foremost, hashcat, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `a5951c2c544c3281354ecbdbf1b8836f`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
