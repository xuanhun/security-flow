# SarCTF Writeup题解 Red King、Confidential_随便吧土豆的博客-CSDN博客

## Case Metadata

- Category: `Misc`
- Platform: `SarCTF Writeup题解 Red King、Confidential`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/SarCTF-Writeup题解-Red-King、Confidential_随便吧土豆的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/SarCTF-Writeup%E9%A2%98%E8%A7%A3-Red-King%E3%80%81Confidential_%E9%9A%8F%E4%BE%BF%E5%90%A7%E5%9C%9F%E8%B1%86%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/SarCTF-Writeup题解-Red-King、Confidential_随便吧土豆的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Misc reference for pcap, web-app challenges.

## Input Signals

- Artifacts: pcap, web-app
- Tools: hashcat, john, netcat, stegsolve
- Techniques: http-analysis, image-analysis, network-forensics, password-cracking, service-enumeration, traffic-analysis, web-exploitation

## First-Principles Route

- Classify the artifact first: encoding, media, archive, QR, traffic, document, or mixed puzzle.
- Use the cheapest extraction or decoding pass that can confirm the intended modality before branching out.
- Treat each recovered clue as a pivot into the next artifact instead of assuming the first visible string is final.

## Solve Thinking

### Step 1: Document

- Route type: `hashcat-driven evidence lookup`
- Why: For Misc, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use hashcat, john, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
- Tools: hashcat, john, netcat, stegsolve
- Reasoning chain:
  - Recognize the section as hashcat-driven evidence lookup.
  - Use hashcat, john, netcat, stegsolve to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: SarCTF Writeup题解 Red King、Confidential_随便吧土豆的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use hashcat, john, netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: hashcat, john, netcat, stegsolve
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use hashcat, john, netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/SBBTD/article/details/104382553](https://blog.csdn.net/SBBTD/article/details/104382553)`

### Step 3: SarCTF

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use hashcat, john, netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: hashcat, john, netcat, stegsolve
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use hashcat, john, netcat, stegsolve to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ctftime链接：https://ctftime.org/event/975/`

### Step 4: 0x01【Stego】Red King

- Route type: `stego extraction`
- Why: Stego cases should test cheap channels before assuming heavy custom hiding logic.
- Probe: Use stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
- Tools: stegsolve
- Reasoning chain:
  - Recognize the section as stego extraction.
  - Use stegsolve to test the cheapest hidden-channel hypothesis first: metadata, QR, appended bytes, channel differences, or simple masks.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `FLAG{who_is_moriarty}`

### Step 5: 0x02【Forensics】Confidential

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use hashcat, john, netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: hashcat, john, netcat
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use hashcat, john, netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `55b1d133aa811878a7573efbfc94107d035be43e56b22194e33a3982a98548b0`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
