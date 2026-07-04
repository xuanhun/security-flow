# 看雪.京东 2018CTF 第十二题 破解之道_大灬白的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `看雪.京东 2018CTF 第十二题 破解之道`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/看雪.京东-2018CTF-第十二题-破解之道_大灬白的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E7%9C%8B%E9%9B%AA.%E4%BA%AC%E4%B8%9C-2018CTF-%E7%AC%AC%E5%8D%81%E4%BA%8C%E9%A2%98-%E7%A0%B4%E8%A7%A3%E4%B9%8B%E9%81%93_%E5%A4%A7%E7%81%AC%E7%99%BD%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/看雪.京东-2018CTF-第十二题-破解之道_大灬白的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat
- Techniques: file-inclusion

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Linked Assets

- Referenced assets: `21`
- `docs/img/9df579223e5c9801aa0721e5d319f030.png`
- `docs/img/ab8448b6c87cbb6f5dfc5e925894664b.png`
- `docs/img/0de6e2206c2d601873180730b34c4ea5.png`
- `docs/img/47111fe5934d04cae9fb7aa10dff10ff.png`
- `docs/img/40c9322a904b4c127f4c1ae4d49e4563.png`
- `docs/img/60b47b3535d09b98ee239719bd28a8a2.png`
- `docs/img/44f6309b1afa0a6d7931691b351af418.png`
- `docs/img/20a20a885e4747c2261916c54a420262.png`
- `docs/img/d856a7662807ca8f83ee3a0167c3c237.png`
- `docs/img/043385b51eb901387d44d12374c44ebf.png`
- `docs/img/48b78fc683fe95086a5b3cb1cbb27dbc.png`
- `docs/img/bf7c1cf814f63e721d7993320611d40a.png`
- ... and `9` more

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 看雪.京东 2018CTF 第十二题 破解之道_大灬白的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/Onlyone_1314/article/details/113813918](https://blog.csdn.net/Onlyone_1314/article/details/113813918)`

### Step 3: CTF（看雪.京东 2018CTF 第十二题 破解之道）

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `9df579223e5c9801aa0721e5d319f030`

### Step 4: 第一步：

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ab8448b6c87cbb6f5dfc5e925894664b`

### Step 5: 第二步：

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0de6e2206c2d601873180730b34c4ea5`

### Step 6: 第三步：

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `if(temp==a[i])` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if(temp==a[i])`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `if(temp==a[i])` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `60b47b3535d09b98ee239719bd28a8a2`

### Step 7: 第四步：

- Route type: `netcat-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `20a20a885e4747c2261916c54a420262`

### Step 8: 第五步：

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `d856a7662807ca8f83ee3a0167c3c237`

### Step 9: 第六步：

- Route type: `indicator enrichment`
- Why: Threat-intel enrichment is only useful after local extraction of stable indicators.
- Probe: Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as indicator enrichment.
  - Extract local indicators first, then enrich hashes, domains, IPs, or malware names.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `96b96f6943b761c3429777425452533e`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
