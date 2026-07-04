# CTF-2021中国能源网络WEB题目全解_wulanlin的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF-2021中国能源网络WEB题目全解_wulanlin的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF-2021%E4%B8%AD%E5%9B%BD%E8%83%BD%E6%BA%90%E7%BD%91%E7%BB%9CWEB%E9%A2%98%E7%9B%AE%E5%85%A8%E8%A7%A3_wulanlin%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF-2021中国能源网络WEB题目全解_wulanlin的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, linux-logs challenges.

## Input Signals

- Artifacts: binary, ciphertext, linux-logs, web-app
- Tools: detect-it-easy, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, file-upload, http-analysis, php-tricks, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `39`
- `docs/img/ca01d287fa2ae1cf5cf5f969695b995a.png`
- `docs/img/28750befccf50b99fe9e369ef2620dc5.png`
- `docs/img/444044d8d4d740cbe72746f0bb68a441.png`
- `docs/img/7b299154265bcb4c26645c2c779af36f.png`
- `docs/img/00929bbce41a6ebce04330a2c21cd163.png`
- `docs/img/fa2d7d893e76f0ce3b9000530791c572.png`
- `docs/img/082f2ef46dad608690f228f8db25cd96.png`
- `docs/img/883ae23794930f64fc77e56e63ea2d47.png`
- `docs/img/1cfd5fec5f08ad95ec6434df9299f49f.png`
- `docs/img/a68ca99c6c515bbcfa059f9354ef7dec.png`
- `docs/img/89816972172d4a42b72fef45dd8bf9ce.png`
- `docs/img/bdf27327c742209a98bae88a8536da4f.png`
- ... and `27` more

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF-2021中国能源网络WEB题目全解_wulanlin的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/wulanlin/article/details/122254933](https://blog.csdn.net/wulanlin/article/details/122254933)`

### Step 3: **0x01 前言**

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use detect-it-easy, netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use detect-it-easy, netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ca01d287fa2ae1cf5cf5f969695b995a`

### Step 4: **0x02 ezphp**

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `444044d8d4d740cbe72746f0bb68a441`

### Step 5: **0x03 phar**

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `883ae23794930f64fc77e56e63ea2d47`

### Step 6: **0x04 HardCode**

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `30837528110f8053141d92cca6caf9bc`

### Step 7: **0x05 CODE**

- Route type: `incident timeline reconstruction`
- Why: Incident-response cases become reusable when every claim is anchored to timestamped artifact correlation.
- Probe: Use detect-it-easy to anchor the event in time, user, host, and file/process context before answering.
- Tools: detect-it-easy
- Reasoning chain:
  - Recognize the section as incident timeline reconstruction.
  - Use detect-it-easy to anchor the event in time, user, host, and file/process context before answering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c601bff492b06515be087dcb3b65e3ef`

### Step 8: **0x06 EZpy**

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use netcat with the extracted filter/query `| import base64data=b'c__main__\nb\n}(Vname\nVtest\nVage\nV13\nVsex\nVnan\nub0c__main__\npeople\n)\x81}(Vname\nVtest\nVage\nV13\nVsex\nVnan\nub.'print(base64.b64encode(data)) |` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `| import base64data=b'c__main__\nb\n}(Vname\nVtest\nVage\nV13\nVsex\nVnan\nub0c__main__\npeople\n)\x81}(Vname\nVtest\nVage\nV13\nVsex\nVnan\nub.'print(base64.b64encode(data)) |`
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use netcat with the extracted filter/query `| import base64data=b'c__main__\nb\n}(Vname\nVtest\nVage\nV13\nVsex\nVnan\nub0c__main__\npeople\n)\x81}(Vname\nVtest\nVage\nV13\nVsex\nVnan\nub.'print(base64.b64encode(data)) |` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0.0.0.0`

### Step 9: **0x07 ezp0p**

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use detect-it-easy, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use detect-it-easy, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `264487d152c25970064f8bad1a16cbf7`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
