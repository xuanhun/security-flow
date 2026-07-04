# CTF解题-网安实验室(注入关)_Tr0e的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `CTF解题`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF解题-网安实验室(注入关)_Tr0e的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E8%A7%A3%E9%A2%98-%E7%BD%91%E5%AE%89%E5%AE%9E%E9%AA%8C%E5%AE%A4%28%E6%B3%A8%E5%85%A5%E5%85%B3%29_Tr0e%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF解题-网安实验室(注入关)_Tr0e的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ids, web-app, web-service challenges.

## Input Signals

- Artifacts: ids, web-app, web-service
- Tools: burp, netcat, sqlmap
- Techniques: dns-analysis, file-inclusion, http-analysis, php-tricks, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `85`
- `docs/img/01ea14c5ba4928f18020d8f8d741f29f.png`
- `docs/img/6fa7383e76009e774be38228bb9d65df.png`
- `docs/img/b394eb4c2d82dfe406f95b149a49ce0a.png`
- `docs/img/89b5b528cd5c613367934bd0f9e1fe20.png`
- `docs/img/0ff8616c32f27ffd548d1b3205902d78.png`
- `docs/img/0baf2e77c86557e9cb20950ef346bb44.png`
- `docs/img/a824e752a5cc5f970733d40aebfbdbf1.png`
- `docs/img/2c27585da6dc0aca1006b63adea3021b.png`
- `docs/img/929ff36cbd37e779105510ae35a53308.png`
- `docs/img/62ab758cc9bc78b3c2aff0832933f132.png`
- `docs/img/75ef75864e627c33c812cc884991b371.png`
- `docs/img/7712465d0d689d853011cbc91b7e1bfa.png`
- ... and `73` more

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF解题-网安实验室(注入关)_Tr0e的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_39190897/article/details/100526788](https://blog.csdn.net/weixin_39190897/article/details/100526788)`

### Step 3: 万能密码

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use burp, netcat, sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: burp, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use burp, netcat, sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `01ea14c5ba4928f18020d8f8d741f29f`

### Step 4: 联合查询

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `89b5b528cd5c613367934bd0f9e1fe20`

### Step 5: 宽字节注入

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2447fcffa977aba22d2ba445fa697200`

### Step 6: 基础理论

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat with the extracted filter/query `[ALL | DISTINCT | DISTINCTROW ]` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `[ALL | DISTINCT | DISTINCTROW ]`
  - `[SQL_CACHE | SQL_NO_CACHE] [SQL_CALC_FOUND_ROWS]`
  - `[GROUP BY {col_name | expr | position}`
  - `[ASC | DESC], ... [WITH ROLLUP]]`
  - `[ORDER BY {col_name | expr | position}`
  - `[ASC | DESC], ...]`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat with the extracted filter/query `[ALL | DISTINCT | DISTINCTROW ]` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4c2e326a3de3daf5c5138d58bf303ab0`

### Step 7: 结合报错注入

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2f3ca25b458717ee0c3f182f5b13c4e1`

### Step 8: 图片链接注入

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use burp, netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use burp, netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a96944e74e47c8b9589753c428572e69`

### Step 9: 报错型盲注

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat, sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat, sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2393f381846a581ce1de98811bd3faf8`

### Step 10: 时间型盲注

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: sqlmap
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `d9496584e6c07f3a9da973d98ff71ab1`

### Step 11: Cookie 注入

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6a0d475721ae58bb080bc6756b3b13e6`

### Step 12: MD5绕过注入

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `if($row!=null){` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if($row!=null){`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `if($row!=null){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `cadb714acf74c823c82018c6c5f6c6ee`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
