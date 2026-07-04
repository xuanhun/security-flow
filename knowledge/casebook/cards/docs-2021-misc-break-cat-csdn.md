# 2021涅普冬令营Misc笔记与题解_break_cat的博客-CSDN博客

## Case Metadata

- Category: `Misc`
- Platform: `2021涅普冬令营Misc笔记与题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2021涅普冬令营Misc笔记与题解_break_cat的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2021%E6%B6%85%E6%99%AE%E5%86%AC%E4%BB%A4%E8%90%A5Misc%E7%AC%94%E8%AE%B0%E4%B8%8E%E9%A2%98%E8%A7%A3_break_cat%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2021涅普冬令营Misc笔记与题解_break_cat的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, ids challenges.

## Input Signals

- Artifacts: binary, ciphertext, ids, pcap, stego-media, web-app
- Tools: binwalk, exiftool, foremost, ida, john, netcat, steghide, stegsolve, strings, wireshark, z3
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, file-inclusion, http-analysis, image-analysis, malware-static, misc-analysis, network-forensics, password-cracking, qr-analysis, reverse-engineering, stego-extraction, symbolic-execution, traffic-analysis, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `23`
- `docs/img/bd035b6cc62da7048f31f132c6dd820d.png`
- `docs/img/f2e881e90a53cbec1d84aa7072fcfca1.png`
- `docs/img/adbbd047bae9728988bb4f3fbbd7afe9.png`
- `docs/img/ffa8a48734fd519dd7e464a781df2691.png`
- `docs/img/2d1126d04c79e3b76c0741c9f2cac313.png`
- `docs/img/c8f95249cfd84035fb3e23b90dd6fece.png`
- `docs/img/b1629b1351aff5c470aa80c13e1f153f.png`
- `docs/img/02a00f6fc278e552daa36a226ffd915f.png`
- `docs/img/c7cedc2da8eec18809d89ec863828f21.png`
- `docs/img/211a7a954d4878269c148ba057d1399d.png`
- `docs/img/3e73a34e829c5749c7650d11a3e1bc25.png`
- `docs/img/e82cdefabc04c9bc5ca43910f793a29a.png`
- ... and `11` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use binwalk, exiftool, foremost, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: binwalk, exiftool, foremost, ida, john
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use binwalk, exiftool, foremost, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 2021涅普冬令营Misc笔记与题解_break_cat的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, exiftool, foremost, ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, exiftool, foremost, ida, john
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, exiftool, foremost, ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 题目前面有问号的为存在疑问或没能做出来的题，求指点。`

### Step 3: Misc简介

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use binwalk, exiftool, foremost, ida to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: binwalk, exiftool, foremost, ida, john
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use binwalk, exiftool, foremost, ida to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6.游戏隐写`

### Step 4: 属性

- Route type: `file metadata extraction`
- Why: When traffic yields a file, recover the object and inspect metadata before treating visible content as the answer.
- Probe: Use exiftool with the extracted filter/query `exiftool 图片` and inspect the matching evidence.
- Tools: exiftool
- Filters or commands:
  - `exiftool 图片`
- Reasoning chain:
  - Recognize the section as file metadata extraction.
  - Use exiftool with the extracted filter/query `exiftool 图片` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `exiftool 图片`

### Step 5: 文件十六进制藏有字符串

- Route type: `strings-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use strings with the extracted filter/query `strings 文件名` and inspect the matching evidence.
- Tools: strings
- Filters or commands:
  - `strings 文件名`
  - `grep -a 要搜索的关键词 文件名`
- Reasoning chain:
  - Recognize the section as strings-driven evidence lookup.
  - Use strings with the extracted filter/query `strings 文件名` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `file 文件名`

### Step 6: 文件包含

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use binwalk, foremost with the extracted filter/query `binwalk 文件名` and inspect the matching evidence.
- Tools: binwalk, foremost
- Filters or commands:
  - `binwalk 文件名`
  - `binwalk -e 文件名`
  - `| 参数 | 含义 |`
  - `| --- | --- |`
  - `| -t | 需要恢复文件类型后缀(如jpg) |`
  - `| -i | 扫描的分区 |`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use binwalk, foremost with the extracted filter/query `binwalk 文件名` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://www.cnblogs.com/yuanqiangfei/p/9138625.html`

### Step 7: 修改文件头

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use binwalk, exiftool, foremost, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: binwalk, exiftool, foremost, ida, john
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use binwalk, exiftool, foremost, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `破环文件头，一定不能显示，破环文件尾，文件不一定显示不正常`

### Step 8: 常见的文件头

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, exiftool, foremost, ida with the extracted filter/query `| 文件格式 | 文件头 | 文件尾 |` and inspect the matching evidence.
- Tools: binwalk, exiftool, foremost, ida, john
- Filters or commands:
  - `| 文件格式 | 文件头 | 文件尾 |`
  - `| --- | --- | --- |`
  - `| JPEG (jpg) | FF D8 | FF D9 |`
  - `| PNG (png) | 89 50 4E 47 | AE 42 60 82 |`
  - `| GIF (gif) | 47 49 46 38 | 00 3B |`
  - `| ZIP Archive (zip) | 50 4B 03 04 | 50 4B |`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, exiftool, foremost, ida with the extracted filter/query `| 文件格式 | 文件头 | 文件尾 |` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `https://blog.csdn.net/wssmiss/article/details/88071448`

### Step 9: gif

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use binwalk, exiftool, foremost, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: binwalk, exiftool, foremost, ida, john
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use binwalk, exiftool, foremost, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `（2）**帧的时间间隔**`

### Step 10: png & bmp

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use ida, stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: ida, stegsolve
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use ida, stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `（4）**wbs43open（bmp）**`

### Step 11: JPG

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use steghide with the extracted filter/query `steghide extract -sf 图片 -p 密码` and inspect the matching evidence.
- Tools: steghide
- Filters or commands:
  - `steghide extract -sf 图片 -p 密码`
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use steghide with the extracted filter/query `steghide extract -sf 图片 -p 密码` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `stegdetect.exe`

### Step 12: 双图隐写

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use binwalk, exiftool, foremost, ida to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: binwalk, exiftool, foremost, ida, john
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use binwalk, exiftool, foremost, ida to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `XOR`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
