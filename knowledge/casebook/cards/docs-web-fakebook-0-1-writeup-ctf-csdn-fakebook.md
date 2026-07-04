# 攻防世界-web-fakebook-从0到1的解题历程writeup_CTF小白的博客-CSDN博客_攻防世界fakebook

## Case Metadata

- Category: `Web`
- Platform: `攻防世界`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/攻防世界-web-fakebook-从0到1的解题历程writeup_CTF小白的博客-CSDN博客_攻防世界fakebook.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C-web-fakebook-%E4%BB%8E0%E5%88%B01%E7%9A%84%E8%A7%A3%E9%A2%98%E5%8E%86%E7%A8%8Bwriteup_CTF%E5%B0%8F%E7%99%BD%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8Cfakebook.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/攻防世界-web-fakebook-从0到1的解题历程writeup_CTF小白的博客-CSDN博客_攻防世界fakebook.md`

## Why This Case Matters

Use this case as a Web reference for web-app, web-service challenges.

## Input Signals

- Artifacts: web-app, web-service
- Tools: netcat, nikto, sqlmap
- Techniques: deserialization, http-analysis, php-tricks, sql-injection, waf-bypass, web-enumeration, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `7`
- `docs/img/7bcc9a1479e36cefd40e60647078cc3d.png`
- `docs/img/7c8917bab4405897ad9b8cef71d2a1c2.png`
- `docs/img/dbb791027ff8b0daa9294636b98c0ac4.png`
- `docs/img/23f096d91195af69272bb5625c2b08d7.png`
- `docs/img/2d8e3ace9a5052f394f66fce66f69c6e.png`
- `docs/img/d0d309c85dc0bb77f4de4697db843f15.png`
- `docs/img/547c73fd31bd68a43377a6129d6c2bf2.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, nikto, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: netcat, nikto, sqlmap
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, nikto, sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 攻防世界-web-fakebook-从0到1的解题历程writeup_CTF小白的博客-CSDN博客_攻防世界fakebook

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, nikto, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, nikto, sqlmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, nikto, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_41429081/article/details/105495932](https://blog.csdn.net/qq_41429081/article/details/105495932)`

### Step 3: 题目分析

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: sqlmap
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `159.138.137.79:55692`

### Step 4: 解题思路

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat, nikto with the extracted filter/query `if($httpCode == 404) {` and inspect the matching evidence.
- Tools: netcat, nikto
- Filters or commands:
  - `if($httpCode == 404) {`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat, nikto with the extracted filter/query `if($httpCode == 404) {` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `159.138.137.79:55692`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
