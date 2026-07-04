# 【web】BUUCTF-web刷题记录_weixin_30684743的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `【web】BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【web】BUUCTF-web刷题记录_weixin_30684743的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90web%E3%80%91BUUCTF-web%E5%88%B7%E9%A2%98%E8%AE%B0%E5%BD%95_weixin_30684743%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【web】BUUCTF-web刷题记录_weixin_30684743的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app, web-service challenges.

## Input Signals

- Artifacts: web-app, web-service
- Tools: burp, netcat
- Techniques: binary-exploitation, encoding-analysis, http-analysis, php-tricks, ret2text, sql-injection, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `22`
- `docs/img/970f79b1eff051aec8d6b769ebe7843d.png`
- `docs/img/1ba17dde9f3e44f6be0ab9d56bff1126.png`
- `docs/img/9853aa89ee2b5247629622ce9034e208.png`
- `docs/img/385085ba1a87b1b4e72419b8b7e24bff.png`
- `docs/img/0a0a31bc288c6b191458a145d4dd9fe8.png`
- `docs/img/5d557f1baf02cf6e801f39ec2cf094d7.png`
- `docs/img/6a8698ae71a07f42062cb101d314abfc.png`
- `docs/img/fb97ae9ec12e701615fccafb0e5213c8.png`
- `docs/img/513aa2c8d94059b555809da1d2dbf095.png`
- `docs/img/287b34c56b523361dafdf8f0b2c3c90f.png`
- `docs/img/b503bc128e439e89aaf224f2c9803f84.png`
- `docs/img/99c5575e6f2b72c8d6a62ad38fdbc12b.png`
- ... and `10` more

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【web】BUUCTF-web刷题记录_weixin_30684743的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `本来一题一篇文章，结果发现太浪费了，所以整合起来了，这篇博文就记录 BUUCTF 的 web 题目的题解吧！`

### Step 3: 随便注

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat with the extracted filter/query `"/select|update|delete|drop|insert|where|\./i"` and inspect the matching evidence.
- Tools: burp, netcat
- Filters or commands:
  - `"/select|update|delete|drop|insert|where|\./i"`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat with the extracted filter/query `"/select|update|delete|drop|insert|where|\./i"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `970f79b1eff051aec8d6b769ebe7843d`

### Step 4: easy_tornado

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `513aa2c8d94059b555809da1d2dbf095`

### Step 5: 高明的黑客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
