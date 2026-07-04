# [BUUCTF 2018]Online Tool_Sk1y的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF 2018`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/[BUUCTF-2018]Online-Tool_Sk1y的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%5BBUUCTF-2018%5DOnline-Tool_Sk1y%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/[BUUCTF-2018]Online-Tool_Sk1y的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app, web-service challenges.

## Input Signals

- Artifacts: web-app, web-service
- Tools: nmap
- Techniques: command-injection, http-analysis, php-tricks, ret2libc, service-enumeration, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `2`
- `docs/img/c204d45cfcd6cd01c09e8ae7c2d4df1e.png`
- `docs/img/b0590f401245b1c9c6ead2a17edd0f40.png`

## Solve Thinking

### Step 1: Document

- Route type: `nmap-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use nmap to collect the smallest evidence slice that answers the goal.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as nmap-driven evidence lookup.
  - Use nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: [BUUCTF 2018]Online Tool_Sk1y的博客-CSDN博客

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use nmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use nmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `考点：本题考查的一个点是escapeshellarg()和escapeshellcmd()函数，他们一起用的时候导致的一个漏洞，我把这个理解成一个类似于**sql注入闭合单引号**的一个漏洞。`

### Step 3: 解题过程

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat, nmap to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat, nmap
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat, nmap to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `172.17.0.2`

### Step 4: 参考文章：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3.[大佬博文](https://blog.csdn.net/qq_26406447/article/details/100711933)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
