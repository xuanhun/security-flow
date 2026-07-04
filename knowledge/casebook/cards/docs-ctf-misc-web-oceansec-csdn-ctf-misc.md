# CTF解题基本思路步骤（misc和web）_OceanSec的博客-CSDN博客_ctf misc解题思路

## Case Metadata

- Category: `Misc`
- Platform: `CTF解题基本思路步骤（misc和web）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF解题基本思路步骤（misc和web）_OceanSec的博客-CSDN博客_ctf-misc解题思路.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E8%A7%A3%E9%A2%98%E5%9F%BA%E6%9C%AC%E6%80%9D%E8%B7%AF%E6%AD%A5%E9%AA%A4%EF%BC%88misc%E5%92%8Cweb%EF%BC%89_OceanSec%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf-misc%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF解题基本思路步骤（misc和web）_OceanSec的博客-CSDN博客_ctf-misc解题思路.md`

## Why This Case Matters

Use this case as a Misc reference for binary, ciphertext, pcap challenges.

## Input Signals

- Artifacts: binary, ciphertext, pcap, stego-media, web-app, web-service
- Tools: angr, binwalk, burp, exiftool, ida, netcat, radare2, steghide, strings
- Techniques: command-injection, crypto-analysis, encoding-analysis, file-inclusion, http-analysis, image-analysis, malware-static, misc-analysis, network-forensics, reverse-engineering, stego-extraction, symbolic-execution, traffic-analysis, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `3`
- `docs/img/8035b53f380f563bc27ff484c7898d0e.png`
- `docs/img/be0c166922a8631e8644bb2d36667731.png`
- `docs/img/d717a424deb896a4ca97a7f1f83da1f8.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use angr, binwalk, burp, exiftool to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: angr, binwalk, burp, exiftool, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use angr, binwalk, burp, exiftool to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF解题基本思路步骤（misc和web）_OceanSec的博客-CSDN博客_ctf misc解题思路

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use angr, binwalk, burp, exiftool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: angr, binwalk, burp, exiftool, ida
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use angr, binwalk, burp, exiftool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `8035b53f380f563bc27ff484c7898d0e`

### Step 3: CTF-web基础解题步骤

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3.burp抓包分析http头`

### Step 4: 图片：

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use angr, binwalk, burp, exiftool to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: angr, binwalk, burp, exiftool, ida
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use angr, binwalk, burp, exiftool to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `​ 图片内容、图片分析、图片拼接、图片修复、EXIF、LSB`

### Step 5: 主要步骤：

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use binwalk, strings with the extracted filter/query `strings test | grep -i flag` and inspect the matching evidence.
- Tools: binwalk, strings
- Filters or commands:
  - `strings test | grep -i flag`
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use binwalk, strings with the extracted filter/query `strings test | grep -i flag` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `file 1.txt`

### Step 6: JPG：

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use angr, ida, radare2, steghide with the extracted filter/query `steghide(win)**` and inspect the matching evidence.
- Tools: angr, ida, radare2, steghide
- Filters or commands:
  - `steghide(win)**`
  - `steghide info out.jpg`
  - `steghide extract -sf out.jpg -p 123456`
  - `steghide extract -sf out.jpg`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use angr, ida, radare2, steghide with the extracted filter/query `steghide(win)**` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `pngcheck.exe`

### Step 7: PNG：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use binwalk, exiftool, ida with the extracted filter/query `python pinyubwm.py --original 1.png --image 2.png --result out.png` and inspect the matching evidence.
- Tools: binwalk, exiftool, ida
- Filters or commands:
  - `python pinyubwm.py --original 1.png --image 2.png --result out.png`
  - `python lsb.py extract [stego_file] [out_file] [password]`
  - `exiftool（查看图片exif信息）**`
  - `exiftool 1.jpg`
  - `exiftool 1.jpg | grep flag`
  - `exiftool *`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use binwalk, exiftool, ida with the extracted filter/query `python pinyubwm.py --original 1.png --image 2.png --result out.png` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `pngcheck.exe`

### Step 8: GIF：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use angr, binwalk, burp, exiftool to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: angr, binwalk, burp, exiftool, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use angr, binwalk, burp, exiftool to locate strings, comparisons, and control-flow decisions relevant to the input.
  - The proof is the code path, comparison, constant, or decoded data that explains the answer.
- Evidence rule: The proof is the code path, comparison, constant, or decoded data that explains the answer.

### Step 9: - bgp：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `be0c166922a8631e8644bb2d36667731`

### Step 10: 音频：

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Decode.exe`

### Step 11: 视频：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use angr, binwalk, burp, exiftool to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: angr, binwalk, burp, exiftool, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use angr, binwalk, burp, exiftool to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `​ 视频中的音频、视频放到010中查看`

### Step 12: 压缩包：

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use angr, binwalk, burp, exiftool to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: angr, binwalk, burp, exiftool, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use angr, binwalk, burp, exiftool to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `7.多个压缩文件合并 cat 文件名(按需) > 保存文件名`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
