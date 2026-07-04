# 2018年浙江省网络安全技能竞赛ctf部分解题思路writeup_xuchen16的博客-CSDN博客_网络安全ctf

## Case Metadata

- Category: `Misc`
- Platform: `2018年浙江省网络安全技能竞赛ctf部分解题思路writeup`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2018年浙江省网络安全技能竞赛ctf部分解题思路writeup_xuchen16的博客-CSDN博客_网络安全ctf.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2018%E5%B9%B4%E6%B5%99%E6%B1%9F%E7%9C%81%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E6%8A%80%E8%83%BD%E7%AB%9E%E8%B5%9Bctf%E9%83%A8%E5%88%86%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AFwriteup_xuchen16%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8ctf.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2018年浙江省网络安全技能竞赛ctf部分解题思路writeup_xuchen16的博客-CSDN博客_网络安全ctf.md`

## Why This Case Matters

Use this case as a Misc reference for ciphertext, disk-image, pcap challenges.

## Input Signals

- Artifacts: ciphertext, disk-image, pcap, siem, stego-media, web-app
- Tools: binwalk, elk, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, encoding-analysis, http-analysis, image-analysis, misc-analysis, network-forensics, qr-analysis, ret2libc, siem-query, stack-overflow, stego-extraction, timeline-analysis, traffic-analysis, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Linked Assets

- Referenced assets: `18`
- `docs/img/6a9e855c6da4612c01605b34d2ebd107.png`
- `docs/img/3fda8121ee2bdb2d7296d1d80f89e3ca.png`
- `docs/img/c2d3c9f1d63ad055802e5f8ed4437a22.png`
- `docs/img/1fb203717fa253d4859b5701ea1b66e1.png`
- `docs/img/907d3dae48c69d566bb8fadcd14b7f31.png`
- `docs/img/27e7ff0d8f9f48e0ebbda22b6f01e806.png`
- `docs/img/92e821fab2c42c03f5c1a38d2f6b0574.png`
- `docs/img/c321621a5ff7a9e30ac626d5af8e249a.png`
- `docs/img/a3330dce3aa2b7d5831ba69c64352e1e.png`
- `docs/img/407b10835b04de5a29b53c2d1c004cfe.png`
- `docs/img/39307a2ae12180773d943f469048ce9c.png`
- `docs/img/d7d31edc1da3ff287125e5516150a6a5.png`
- ... and `6` more

## Solve Thinking

### Step 1: Document

- Route type: `binwalk-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use binwalk, elk, netcat to collect the smallest evidence slice that answers the goal.
- Tools: binwalk, elk, netcat
- Reasoning chain:
  - Recognize the section as binwalk-driven evidence lookup.
  - Use binwalk, elk, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 2018年浙江省网络安全技能竞赛ctf部分解题思路writeup_xuchen16的博客-CSDN博客_网络安全ctf

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use binwalk, elk, netcat with the extracted filter/query `用wireshare打开wire.pcapng数据包，执行http.request.method==”POST”过滤http post` and inspect the matching evidence.
- Tools: binwalk, elk, netcat
- Filters or commands:
  - `用wireshare打开wire.pcapng数据包，执行http.request.method==”POST”过滤http post`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use binwalk, elk, netcat with the extracted filter/query `用wireshare打开wire.pcapng数据包，执行http.request.method==”POST”过滤http post` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `101.101.101.110`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
