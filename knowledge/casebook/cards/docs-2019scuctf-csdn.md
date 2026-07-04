# 2019SCUCTF部分题解_东坡何罪发文章总是审核不通过，去博客园了的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `2019SCUCTF部分题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2019SCUCTF部分题解_东坡何罪发文章总是审核不通过，去博客园了的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2019SCUCTF%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_%E4%B8%9C%E5%9D%A1%E4%BD%95%E7%BD%AA%E5%8F%91%E6%96%87%E7%AB%A0%E6%80%BB%E6%98%AF%E5%AE%A1%E6%A0%B8%E4%B8%8D%E9%80%9A%E8%BF%87%EF%BC%8C%E5%8E%BB%E5%8D%9A%E5%AE%A2%E5%9B%AD%E4%BA%86%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2019SCUCTF部分题解_东坡何罪发文章总是审核不通过，去博客园了的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, memory challenges.

## Input Signals

- Artifacts: binary, ciphertext, memory, pcap, stego-media, web-app, web-service
- Tools: burp, netcat, pwntools, tshark, volatility
- Techniques: binary-exploitation, classical-crypto, crypto-analysis, deserialization, dns-analysis, encoding-analysis, file-inclusion, http-analysis, image-analysis, memory-forensics, misc-analysis, network-forensics, php-tricks, qr-analysis, stack-overflow, traffic-analysis, waf-bypass, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `16`
- `docs/img/9a972de4a4af10a0a18c860d8dfc0dcb.png`
- `docs/img/c51209ab68b02a03a57ade8876ef1af1.png`
- `docs/img/144b287234bad9b925173699208b2b2b.png`
- `docs/img/ce705a8ae8e7433005eeea9da39dfd7b.png`
- `docs/img/50751194a78a098be3d513b05748ccd0.png`
- `docs/img/d28e75d9b56bfb9481f7c2ea74d30893.png`
- `docs/img/2d6f584d20d1ef457eafdd5419540430.png`
- `docs/img/170a2132cbb2b66dfbbf1ffa22a115cf.png`
- `docs/img/f6194102526cd96362e44b6aafdb6505.png`
- `docs/img/f88d5dd0f23e336e9288902fcfad084b.png`
- `docs/img/f0e0dfd6c8b3a24a20162e923a211bf1.png`
- `docs/img/62b49f50d76b2afe36c22b998cfd7dd9.png`
- ... and `4` more

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat, pwntools, tshark to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat, pwntools, tshark, volatility
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat, pwntools, tshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 2019SCUCTF部分题解_东坡何罪发文章总是审核不通过，去博客园了的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat, pwntools, tshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat, pwntools, tshark, volatility
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat, pwntools, tshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/perfect0066/article/details/90381016](https://blog.csdn.net/perfect0066/article/details/90381016)`

### Step 3: 2019SCUCTF部分题解

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat, pwntools, tshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat, pwntools, tshark, volatility
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat, pwntools, tshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `时间有限，writeup写的简单了点，有时间再补充`

### Step 4: 解题思路

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat, pwntools, tshark to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat, pwntools, tshark, volatility
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat, pwntools, tshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `9a972de4a4af10a0a18c860d8dfc0dcb`

### Step 5: flag

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat, pwntools, tshark to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat, pwntools, tshark, volatility
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat, pwntools, tshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `scuctf{signup}`

### Step 6: 解题思路

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: burp
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c51209ab68b02a03a57ade8876ef1af1`

### Step 7: flag

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat, pwntools, tshark to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat, pwntools, tshark, volatility
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat, pwntools, tshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `SCUCTF{y0U_jUs7_neEd_car3ful}`

### Step 8: 解题思路

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use burp, netcat, pwntools, tshark to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: burp, netcat, pwntools, tshark, volatility
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use burp, netcat, pwntools, tshark to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `144b287234bad9b925173699208b2b2b`

### Step 9: 参考链接：

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use burp, netcat, pwntools, tshark to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: burp, netcat, pwntools, tshark, volatility
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use burp, netcat, pwntools, tshark to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `CVE-2017-5941`

### Step 10: flag

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat, pwntools, tshark to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat, pwntools, tshark, volatility
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat, pwntools, tshark to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2602547F25B5C13D62F010230D917481`

### Step 11: 解题思路

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat, pwntools, tshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat, pwntools, tshark, volatility
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat, pwntools, tshark to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `120.78.185.175:5000`

### Step 12: 参考链接

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use burp, netcat, pwntools, tshark with the extracted filter/query `Bypassing path restriction on whitelisted CDNs to circumvent CSP protections - SECT CTF Web 400 writeup | Blog - 0daylabs` and inspect the matching evidence.
- Tools: burp, netcat, pwntools, tshark, volatility
- Filters or commands:
  - `Bypassing path restriction on whitelisted CDNs to circumvent CSP protections - SECT CTF Web 400 writeup | Blog - 0daylabs`
- Reasoning chain:
  - Recognize the section as xss route.
  - Use burp, netcat, pwntools, tshark with the extracted filter/query `Bypassing path restriction on whitelisted CDNs to circumvent CSP protections - SECT CTF Web 400 writeup | Blog - 0daylabs` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[https://paper.seebug.org/574/#h4x0rsspace](https://paper.seebug.org/574/#h4x0rsspace)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
