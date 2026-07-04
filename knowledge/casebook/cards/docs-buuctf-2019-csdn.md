# BUUCTF__[强网杯 2019]高明的黑客_题解_风过江南乱的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF__[强网杯-2019]高明的黑客_题解_风过江南乱的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF__%5B%E5%BC%BA%E7%BD%91%E6%9D%AF-2019%5D%E9%AB%98%E6%98%8E%E7%9A%84%E9%BB%91%E5%AE%A2_%E9%A2%98%E8%A7%A3_%E9%A3%8E%E8%BF%87%E6%B1%9F%E5%8D%97%E4%B9%B1%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF__[强网杯-2019]高明的黑客_题解_风过江南乱的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat
- Techniques: http-analysis, misc-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `3`
- `docs/img/26ff65538a9693b89140387c19fb6ed6.png`
- `docs/img/da5db2aaa286934c7fc723270d2c93a8.png`
- `docs/img/10ee30527622fec7185641d77ea1e0f8.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BUUCTF__[强网杯 2019]高明的黑客_题解_风过江南乱的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/TM_1024/article/details/106455979](https://blog.csdn.net/TM_1024/article/details/106455979)`

### Step 3: 前言

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 还有一点是python2 和python3。有点差别，比如说 print 函数等等，python3 有些东西与 python2 不兼容。`

### Step 4: 研究

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `26ff65538a9693b89140387c19fb6ed6`

### Step 5: 解决

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

### Step 6: 最后

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 最后欢迎来访[个人博客](http://ctf-web.zm996.cloud/)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
