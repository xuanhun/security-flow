# CTFHub题解-技能树-Web（SQL注入-过滤空格）_唤变的博客-CSDN博客_sqlmap 空格过滤

## Case Metadata

- Category: `Web`
- Platform: `CTFHub题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTFHub题解-技能树-Web（SQL注入-过滤空格）_唤变的博客-CSDN博客_sqlmap-空格过滤.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTFHub%E9%A2%98%E8%A7%A3-%E6%8A%80%E8%83%BD%E6%A0%91-Web%EF%BC%88SQL%E6%B3%A8%E5%85%A5-%E8%BF%87%E6%BB%A4%E7%A9%BA%E6%A0%BC%EF%BC%89_%E5%94%A4%E5%8F%98%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_sqlmap-%E7%A9%BA%E6%A0%BC%E8%BF%87%E6%BB%A4.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTFHub题解-技能树-Web（SQL注入-过滤空格）_唤变的博客-CSDN博客_sqlmap-空格过滤.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: sqlmap
- Techniques: binary-exploitation, http-analysis, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `8`
- `docs/img/392ea30b0854cb4dbbf32391754293ca.png`
- `docs/img/6c91685a7485c16290b26f275a801db8.png`
- `docs/img/e6683a7865e577f5ae6680b8352aabf5.png`
- `docs/img/38c93980017f110501222196acc97db7.png`
- `docs/img/dbc5bc8468449e38e4407d6b979acba9.png`
- `docs/img/4643af5e3fa0805bef30f98f2e9ad2e8.png`
- `docs/img/31260e57d2c57f225f2df611c0b958a8.png`
- `docs/img/1db9312eb4ed703f3319f6b4f8cef018.png`

## Solve Thinking

### Step 1: Document

- Route type: `sqlmap-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: sqlmap
- Reasoning chain:
  - Recognize the section as sqlmap-driven evidence lookup.
  - Use sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTFHub题解-技能树-Web（SQL注入-过滤空格）_唤变的博客-CSDN博客_sqlmap 空格过滤

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: sqlmap
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 3: 前言

- Route type: `sqlmap-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: sqlmap
- Reasoning chain:
  - Recognize the section as sqlmap-driven evidence lookup.
  - Use sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `<mark>在本文中将会采用两种注入手法：SQLmap和手注，当然记录这篇文章主要是对SQLmap的使用进行一下学习</mark>`

### Step 4: 过滤空格

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use sqlmap to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: sqlmap
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use sqlmap to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `392ea30b0854cb4dbbf32391754293ca`

### Step 5: SQLmap

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use sqlmap with the extracted filter/query `python sqlmap.py -u "http://challenge-ba6a5630047ce20b.sandbox.ctfhub.com:10800/?id=1"` and inspect the matching evidence.
- Tools: sqlmap
- Filters or commands:
  - `python sqlmap.py -u "http://challenge-ba6a5630047ce20b.sandbox.ctfhub.com:10800/?id=1"`
  - `python sqlmap.py -u "http://challenge-ba6a5630047ce20b.sandbox.ctfhub.com:10800/?id=1" -D "sqli"`
  - `python sqlmap.py -u "http://challenge-ba6a5630047ce20b.sandbox.ctfhub.com:10800/?id=1" -D "sqli" -T "wnilazwjye"`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use sqlmap with the extracted filter/query `python sqlmap.py -u "http://challenge-ba6a5630047ce20b.sandbox.ctfhub.com:10800/?id=1"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `e6683a7865e577f5ae6680b8352aabf5`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
