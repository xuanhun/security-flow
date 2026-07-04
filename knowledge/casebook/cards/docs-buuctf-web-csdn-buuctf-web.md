# BUUCTF__web题解合集（一）_风过江南乱的博客-CSDN博客_buuctf web

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF__web题解合集（一）_风过江南乱的博客-CSDN博客_buuctf-web.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF__web%E9%A2%98%E8%A7%A3%E5%90%88%E9%9B%86%EF%BC%88%E4%B8%80%EF%BC%89_%E9%A3%8E%E8%BF%87%E6%B1%9F%E5%8D%97%E4%B9%B1%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_buuctf-web.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF__web题解合集（一）_风过江南乱的博客-CSDN博客_buuctf-web.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: netcat, sqlmap
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, php-tricks, qr-analysis, sql-injection, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `9`
- `docs/img/4633c0460454bc784570c0ea62866e65.png`
- `docs/img/cac301cd0000d5d140216f3a7edbff1d.png`
- `docs/img/40dca115bb348ec672b83a0fc456a82e.png`
- `docs/img/651ee725de935158c85a072254f0ac21.png`
- `docs/img/4167e76f28d77854fa41bcce5051b06b.png`
- `docs/img/77d354cde21b5f6a7d13895ee02ea000.png`
- `docs/img/d56de83b26aa20d2a9227a762f1ac903.png`
- `docs/img/7cc45f4d29760d96cc5275190f67ca85.png`
- `docs/img/da99fe8066a1ab617e2d2e858017baa3.png`

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

### Step 2: BUUCTF__web题解合集（一）_风过江南乱的博客-CSDN博客_buuctf web

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/TM_1024/article/details/107482984](https://blog.csdn.net/TM_1024/article/details/107482984)`

### Step 3: 前言

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 至少得过一遍知道相关知识点。`

### Step 4: [极客大挑战 2019]HardSQL

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `check.php`

### Step 5: [GXYCTF2019]BabySQli

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: sqlmap
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4633c0460454bc784570c0ea62866e65`

### Step 6: [RoarCTF 2019]Easy Java

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat, sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat, sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `40dca115bb348ec672b83a0fc456a82e`

### Step 7: [De1CTF 2019]SSRF Me

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat with the extracted filter/query `getSign(self.action, self.param) == self.sign` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `getSign(self.action, self.param) == self.sign`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat with the extracted filter/query `getSign(self.action, self.param) == self.sign` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0.0.0.0`

### Step 8: [网鼎杯 2020 青龙组]AreUSerialz

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat with the extracted filter/query `先注意到`===` 强比较，不仅比较值还不仅数据类型。`op==="2"` 满足后才能继续往下，满足后分别为 op、content 赋值为1、空。并调用`process()` 函数。` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `先注意到`===` 强比较，不仅比较值还不仅数据类型。`op==="2"` 满足后才能继续往下，满足后分别为 op、content 赋值为1、空。并调用`process()` 函数。`
  - `再看 `process()` 函数。继续验证了op，为 1 则调用`write()`函数，为 2 则调用 `read()`函数。很明显得为2，因为2才有输出返回值。但注意到此时验证用的是 `==` 而且前面用的是`"2"` 属于字符型，那就会就来了，让`op=2`，整数型，在 `op==="2"` 时不成立，但在`op=="2"`时成立。`
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat with the extracted filter/query `先注意到`===` 强比较，不仅比较值还不仅数据类型。`op==="2"` 满足后才能继续往下，满足后分别为 op、content 赋值为1、空。并调用`process()` 函数。` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `da99fe8066a1ab617e2d2e858017baa3`

### Step 9: 最后

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 最后欢迎来访[个人博客](http://ctf-web.zm996.cloud/)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
