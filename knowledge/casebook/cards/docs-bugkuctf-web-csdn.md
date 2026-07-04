# BugkuCTF平台-Web题目笔记_手可摘星辰丶的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BugkuCTF平台`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BugkuCTF平台-Web题目笔记_手可摘星辰丶的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BugkuCTF%E5%B9%B3%E5%8F%B0-Web%E9%A2%98%E7%9B%AE%E7%AC%94%E8%AE%B0_%E6%89%8B%E5%8F%AF%E6%91%98%E6%98%9F%E8%BE%B0%E4%B8%B6%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BugkuCTF平台-Web题目笔记_手可摘星辰丶的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app, web-service challenges.

## Input Signals

- Artifacts: web-app, web-service
- Tools: burp, detect-it-easy, netcat
- Techniques: command-injection, crypto-analysis, encoding-analysis, file-inclusion, http-analysis, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `6`
- `docs/img/285a3a71f8a70b1e34d13e00613653f1.png`
- `docs/img/205d04716962883092b3ba7cb5ba5a0e.png`
- `docs/img/94f3a078211c663ee54e79817132a34e.png`
- `docs/img/6451b7d3547940892bbbc46737a38cde.png`
- `docs/img/c48bb9245d8503fcb4dc179a8b474c00.png`
- `docs/img/f5fc2bef99ecc479e382fd93bd2dae15.png`

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BugkuCTF平台-Web题目笔记_手可摘星辰丶的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `先从简单的下手，慢慢学习，不断更新~`

### Step 3: Web2

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `查看页面源码，就找到了，嗯，真的好简单。`

### Step 4: 计算器

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `然后发现直接在页面上改一下maxlength的限制，输入正确的计算结果，得到flag。`

### Step 5: Web基础$_GET

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `在URL那一栏直接加上?what=flag，回车，ok~`

### Step 6: Web基础$_POST

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `285a3a71f8a70b1e34d13e00613653f1`

### Step 7: 矛盾

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat with the extracted filter/query `if($num==1)` and inspect the matching evidence.
- Tools: burp, detect-it-easy, netcat
- Filters or commands:
  - `if($num==1)`
  - `> 1. php中有两种比较的符号 == 和 === 。=== 在进行比较的时候，会先判断两种字符串的类型是否相等，再比较；== 在进行比较的时候，会先将字符串类型转化成相同，再比较。`
  - `> 如果比较一个数字和字符串或者比较涉及到数字内容的字符串，则字符串会被转换成数值，并且比较按照数值来进行。判断admin == 0？成功。`
  - `> 2. 当一个字符串作一个数值来取值，其结果和类型如下：如果该字符串没有包含’.’,‘e’,'E’并且其数值在整形的范围之内，该字符串被当作int来取值，其他所有情况下都被作为float来取值，该字符串的开始部分决定了它的值，如果该字符串以合法的数值开始，则使用该数值，否则其值为0。即判断1admin == 1 ？成功，而判断admin1 == 1？不成功。`
  - `以及，活到老学到老，以后有关于这种==判断的，都可以考虑一下是不是有这个漏洞。`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat with the extracted filter/query `if($num==1)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:8002`

### Step 8: Web3

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `205d04716962883092b3ba7cb5ba5a0e`

### Step 9: web5

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use burp, detect-it-easy, netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
- Tools: burp, detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as xss route.
  - Use burp, detect-it-easy, netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `94f3a078211c663ee54e79817132a34e`

### Step 10: 域名解析

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240`

### Step 11: 你必须让他停下

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6451b7d3547940892bbbc46737a38cde`

### Step 12: 变量1

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240:8004`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
