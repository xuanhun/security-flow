# ctf中文转unicode_CTF实战题解笔记 - Web篇_weixin_39707597的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `ctf中文转unicode`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/ctf中文转unicode_CTF实战题解笔记---Web篇_weixin_39707597的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/ctf%E4%B8%AD%E6%96%87%E8%BD%ACunicode_CTF%E5%AE%9E%E6%88%98%E9%A2%98%E8%A7%A3%E7%AC%94%E8%AE%B0---Web%E7%AF%87_weixin_39707597%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/ctf中文转unicode_CTF实战题解笔记---Web篇_weixin_39707597的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: netcat, sqlmap
- Techniques: binary-exploitation, encoding-analysis, file-upload, http-analysis, sql-injection, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: ctf中文转unicode_CTF实战题解笔记 - Web篇_weixin_39707597的博客-CSDN博客

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat, sqlmap to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat, sqlmap to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `web部分是CTF的重要组成部分之一，素有WEB大魔王之称，题目种类繁多，关键是如何发。现漏洞的类型和怎样构造特殊的负载绕过过滤。`

### Step 3: **简单的招聘系统**

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat, sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat, sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.57.212.112:7891`

### Step 4: CTF实战题解 – 代码审计篇

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use netcat, sqlmap with the extracted filter/query `{% if c.__name__=='catch_warnings' %}` and inspect the matching evidence.
- Tools: netcat, sqlmap
- Filters or commands:
  - `{% if c.__name__=='catch_warnings' %}`
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use netcat, sqlmap with the extracted filter/query `{% if c.__name__=='catch_warnings' %}` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
