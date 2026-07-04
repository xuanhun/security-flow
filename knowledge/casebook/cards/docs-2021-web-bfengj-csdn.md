# 2021虎符初赛Web部分题解_bfengj的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `2021虎符初赛Web部分题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2021虎符初赛Web部分题解_bfengj的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2021%E8%99%8E%E7%AC%A6%E5%88%9D%E8%B5%9BWeb%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_bfengj%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2021虎符初赛Web部分题解_bfengj的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat
- Techniques: command-injection, crypto-analysis, http-analysis, maldoc-analysis, php-tricks, ret2libc, sql-injection, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: Document

- Route type: `maldoc analysis`
- Why: Maldoc routes start with stream/macro extraction and decoding before behavior claims.
- Probe: Use netcat to extract macros, streams, embedded URLs, and decoded script content.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as maldoc analysis.
  - Use netcat to extract macros, streams, embedded URLs, and decoded script content.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 2021虎符初赛Web部分题解_bfengj的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/rfrder/article/details/115435829](https://blog.csdn.net/rfrder/article/details/115435829)`

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
- Result: `这个WP还是直接复制粘贴的当时随手写的WP。。。太懒了别骂了呜呜呜。。。`

### Step 4: 签到

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `User-Agentt: zerodiumsystem("cat /flag");`

### Step 5: unsetme

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat with the extracted filter/query `'/^@(\w+)((?:\..+|\[(?:(?:[^\[\]]*|(?R))*)\])*)/',` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `'/^@(\w+)((?:\..+|\[(?:(?:[^\[\]]*|(?R))*)\])*)/',`
  - `'/\.([^.\[\]]+)|\[((?:[^\[\]\'"]*|(?R))*)\]/',`
  - `'/^@(\w+)((?:\..+|\[(?:(?:[^\[\]]*|(?R))*)\])*)/'`
  - `/\.([^.\[\]]+)|\[((?:[^\[\]\'"]*|(?R))*)\]/`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat with the extracted filter/query `'/^@(\w+)((?:\..+|\[(?:(?:[^\[\]]*|(?R))*)\])*)/',` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0=system('cat /flag');`

### Step 6: “慢慢做”管理系统

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1:80`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
