# USB流量分析

## Case Metadata

- Category: `Misc`
- Platform: `ciscn 2022 初赛`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `misc/[ciscn 2022 初赛]ez_usb.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/misc/%5Bciscn%202022%20%E5%88%9D%E8%B5%9B%5Dez_usb.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/misc/[ciscn 2022 初赛]ez_usb.md`

## Why This Case Matters

Use this case as a Misc reference for ciphertext, pcap, stego-media challenges.

## Input Signals

- Artifacts: ciphertext, pcap, stego-media
- Tools: tshark, wireshark
- Techniques: classical-crypto, crypto-analysis, image-analysis, misc-analysis, network-forensics, qr-analysis, traffic-analysis

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `9`
- `misc/images/ez_usb/download.jpg`
- `misc/images/ez_usb/extract.jpg`
- `misc/images/ez_usb/extract2.jpg`
- `misc/images/ez_usb/tshark1.jpg`
- `misc/images/ez_usb/tshark2.jpg`
- `misc/images/ez_usb/tshark3.jpg`
- `misc/images/ez_usb/password1.jpg`
- `misc/images/ez_usb/password2.jpg`
- `misc/images/ez_usb/flag.jpg`

## Solve Thinking

### Step 1: USB流量分析

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use tshark, wireshark with the extracted filter/query `tshark -r "C:\Users\lxy34\Desktop\2-8-1.pcapng" -T fields -e usb.capdata > keystrokes.txt` and inspect the matching evidence.
- Tools: tshark, wireshark
- Filters or commands:
  - `tshark -r "C:\Users\lxy34\Desktop\2-8-1.pcapng" -T fields -e usb.capdata > keystrokes.txt`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use tshark, wireshark with the extracted filter/query `tshark -r "C:\Users\lxy34\Desktop\2-8-1.pcapng" -T fields -e usb.capdata > keystrokes.txt` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `![image](./images/ez_usb/flag.jpg)`

### Step 2: 流量包分析题解题步骤

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use tshark, wireshark with the extracted filter/query `Host，Protocol，contains，特征值` and inspect the matching evidence.
- Tools: tshark, wireshark
- Filters or commands:
  - `Host，Protocol，contains，特征值`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use tshark, wireshark with the extracted filter/query `Host，Protocol，contains，特征值` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- 文件提取`

### Step 3: USB流量题解题步骤：

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use tshark, wireshark to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: tshark, wireshark
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use tshark, wireshark to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- 多个设备数据可能需交叉引用`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
