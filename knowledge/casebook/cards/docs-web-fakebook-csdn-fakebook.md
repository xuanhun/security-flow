# 解网鼎杯一道web题（fakebook）_诸神之眼的博客-CSDN博客_fakebook

## Case Metadata

- Category: `Web`
- Platform: `解网鼎杯一道web题（fakebook）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/解网鼎杯一道web题（fakebook）_诸神之眼的博客-CSDN博客_fakebook.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E8%A7%A3%E7%BD%91%E9%BC%8E%E6%9D%AF%E4%B8%80%E9%81%93web%E9%A2%98%EF%BC%88fakebook%EF%BC%89_%E8%AF%B8%E7%A5%9E%E4%B9%8B%E7%9C%BC%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_fakebook.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/解网鼎杯一道web题（fakebook）_诸神之眼的博客-CSDN博客_fakebook.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, ids, web-app challenges.

## Input Signals

- Artifacts: ciphertext, ids, web-app, web-service
- Tools: burp, netcat, nikto, sqlmap, z3
- Techniques: browser-forensics, classical-crypto, deserialization, encoding-analysis, http-analysis, php-tricks, sql-injection, symbolic-execution, waf-bypass, web-enumeration, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `8`
- `docs/img/2d7d77f2f7b71c4e5300fcbca28b90a3.png`
- `docs/img/4980633314e03327b8ca635a5807f501.png`
- `docs/img/b05e302bdd04a9e243329d66d7c6dc89.png`
- `docs/img/8a7c22511b8e963b087aaace0099c2ec.png`
- `docs/img/7b962c29f32596a822d5e28c4e6cc644.png`
- `docs/img/7db54932de5301b24fb1590ed6ed09cd.png`
- `docs/img/0ce6b58976b7469279ab133daed02472.png`
- `docs/img/36fb1a51f9ee84c4d37239603d5b0c93.png`

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat, nikto, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat, nikto, sqlmap, z3
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat, nikto, sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 解网鼎杯一道web题（fakebook）_诸神之眼的博客-CSDN博客_fakebook

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat, nikto, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat, nikto, sqlmap, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat, nikto, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2d7d77f2f7b71c4e5300fcbca28b90a3`

### Step 3: 扫描：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, nikto with the extracted filter/query `> if($httpCode == 404) {` and inspect the matching evidence.
- Tools: netcat, nikto
- Filters or commands:
  - `> if($httpCode == 404) {`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, nikto with the extracted filter/query `> if($httpCode == 404) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4980633314e03327b8ca635a5807f501`

### Step 4: 注入：

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use burp, netcat, sqlmap to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: burp, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use burp, netcat, sqlmap to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f60c34e18065457cab2a8f72a615f74aeed1bc0d1cd84c6d`

### Step 5: **fuzz测试：**

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat, z3 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat, z3
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat, z3 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7b962c29f32596a822d5e28c4e6cc644`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
