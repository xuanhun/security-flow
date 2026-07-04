# CTF平台题库writeup（三）--BugKuCTF-杂项（1-20题详解）_Hacking黑白红的博客-CSDN博客_ctf题库及详解

## Case Metadata

- Category: `Misc`
- Platform: `CTF平台题库writeup（三）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF平台题库writeup（三）--BugKuCTF-杂项（1-20题详解）_Hacking黑白红的博客-CSDN博客_ctf题库及详解.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E5%B9%B3%E5%8F%B0%E9%A2%98%E5%BA%93writeup%EF%BC%88%E4%B8%89%EF%BC%89--BugKuCTF-%E6%9D%82%E9%A1%B9%EF%BC%881-20%E9%A2%98%E8%AF%A6%E8%A7%A3%EF%BC%89_Hacking%E9%BB%91%E7%99%BD%E7%BA%A2%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf%E9%A2%98%E5%BA%93%E5%8F%8A%E8%AF%A6%E8%A7%A3.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF平台题库writeup（三）--BugKuCTF-杂项（1-20题详解）_Hacking黑白红的博客-CSDN博客_ctf题库及详解.md`

## Why This Case Matters

Use this case as a Misc reference for ciphertext, ids, pcap challenges.

## Input Signals

- Artifacts: ciphertext, ids, pcap, stego-media, web-app
- Tools: binwalk, foremost, netcat, stegsolve, wireshark
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, image-analysis, misc-analysis, network-forensics, qr-analysis, stego-extraction, traffic-analysis, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `84`
- `docs/img/c9932af5f404e3f7fda86816e5e82fff.png`
- `docs/img/f1612a1459c910e463296ef5e6ca6ef9.png`
- `docs/img/c0dea3afc08810e641ddf0caad724f8e.png`
- `docs/img/6e36611dd5348f4d31dbde5c980ba31b.png`
- `docs/img/0af49380fd9201945de393bf02dfb37f.png`
- `docs/img/59dfcd6cc92a8e1c7521b3a060b59e23.png`
- `docs/img/06bb9732738572b448b469eaf4bc5a5f.png`
- `docs/img/4da2042249fd49881dd72df4df9d8725.png`
- `docs/img/3de969da9b2c5034fb86b5896ec04b72.png`
- `docs/img/5263380e25dac55d4de606cdcb664434.png`
- `docs/img/77d0e274463a0c709efbb3fb99d79f7b.png`
- `docs/img/f3b2844354901f2ca52b5c2d54e31d3e.png`
- ... and `72` more

## Solve Thinking

### Step 1: Document

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, netcat, stegsolve, wireshark
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF平台题库writeup（三）--BugKuCTF-杂项（1-20题详解）_Hacking黑白红的博客-CSDN博客_ctf题库及详解

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use binwalk, foremost, netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: binwalk, foremost, netcat, stegsolve, wireshark
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use binwalk, foremost, netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/zsw15841822890/article/details/107013549](https://blog.csdn.net/zsw15841822890/article/details/107013549)`

### Step 3: **1****、签到题**

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use binwalk, foremost, netcat, stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: binwalk, foremost, netcat, stegsolve, wireshark
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use binwalk, foremost, netcat, stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `扫描二维码直接获取flag`

### Step 4: 这是一张单纯的图片

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use binwalk, foremost, netcat, stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: binwalk, foremost, netcat, stegsolve, wireshark
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use binwalk, foremost, netcat, stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `120.24.86.145:8002`

### Step 5: 隐写(文件头)

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use binwalk, foremost, netcat, stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: binwalk, foremost, netcat, stegsolve, wireshark
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use binwalk, foremost, netcat, stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6e36611dd5348f4d31dbde5c980ba31b`

### Step 6: telnet

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use wireshark to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: wireshark
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use wireshark to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `5263380e25dac55d4de606cdcb664434`

### Step 7: 眼见非实(ISCCCTF)

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `f3b2844354901f2ca52b5c2d54e31d3e`

### Step 8: **啊哒**

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: binwalk
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7713bf42cac22844f1fbc1174d3faa44`

### Step 9: dd if=carter.jpg of=carter-1.jpg skip=140147 bs=1

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use foremost to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: foremost
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use foremost to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `foremost是一个基于文件文件头和尾部信息以及文件的内建数据结构恢复文件的命令行工具，直接将文件拆解`

### Step 10: 7\. 又一张图片，还单纯吗

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use binwalk, foremost to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: binwalk, foremost
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use binwalk, foremost to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cf026ccffdfa2026556186f3c64ffecd`

### Step 11: **猜**

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, foremost, netcat, stegsolve, wireshark
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, foremost, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `31281685b6d7b1c90cbe0e36fbcc401b`

### Step 12: 宽带信息泄露

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use binwalk, foremost, netcat, stegsolve to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: binwalk, foremost, netcat, stegsolve, wireshark
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use binwalk, foremost, netcat, stegsolve to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `df392702f27b51ed7acd72a1d127e132`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
