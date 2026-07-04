# 题目：[GCCCTF 2025]计小鸡的秘密

## Case Metadata

- Category: `Misc`
- Platform: `GCCCTF2025`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `misc/GCCCTF2025_计小鸡的秘密.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/misc/GCCCTF2025_%E8%AE%A1%E5%B0%8F%E9%B8%A1%E7%9A%84%E7%A7%98%E5%AF%86.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/misc/GCCCTF2025_计小鸡的秘密.md`

## Why This Case Matters

Use this case as a Misc reference for pcap, stego-media, web-app challenges.

## Input Signals

- Artifacts: pcap, stego-media, web-app
- Tools: binwalk, foremost
- Techniques: http-analysis, image-analysis, misc-analysis, network-forensics, stego-extraction, traffic-analysis, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `8`
- `misc/images/计小鸡的秘密/协议分布.png`
- `misc/images/计小鸡的秘密/secret-png.png`
- `misc/images/计小鸡的秘密/upload-png.png`
- `misc/images/计小鸡的秘密/exact-png.png`
- `misc/images/计小鸡的秘密/error.png`
- `misc/images/计小鸡的秘密/ihdr-error.png`
- `misc/images/计小鸡的秘密/unhex.png`
- `misc/images/计小鸡的秘密/flag.png`

## Solve Thinking

### Step 1: 考点：

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use binwalk, foremost to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: binwalk, foremost
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use binwalk, foremost to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `#流量分析 #图片隐写 #宽高隐写`

### Step 2: 思路

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use binwalk, foremost to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: binwalk, foremost
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use binwalk, foremost to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `直接得到了flag`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
