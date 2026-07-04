# ctfshow 萌新22 （类似级客巅峰web4）_Firebasky的博客-CSDN博客_ctf p神

## Case Metadata

- Category: `Web`
- Platform: `ctfshow 萌新22 （类似级客巅峰web4）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/ctfshow-萌新22-（类似级客巅峰web4）_Firebasky的博客-CSDN博客_ctf-p神.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/ctfshow-%E8%90%8C%E6%96%B022-%EF%BC%88%E7%B1%BB%E4%BC%BC%E7%BA%A7%E5%AE%A2%E5%B7%85%E5%B3%B0web4%EF%BC%89_Firebasky%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf-p%E7%A5%9E.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/ctfshow-萌新22-（类似级客巅峰web4）_Firebasky的博客-CSDN博客_ctf-p神.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat
- Techniques: command-injection, file-inclusion, http-analysis, ret2libc, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `10`
- `docs/img/0044589c7115a39976baf63340ea5bcb.png`
- `docs/img/661ec6937262a222d02b337b2f74a795.png`
- `docs/img/7da1d5d725f6f3c68416af4c8b16a777.png`
- `docs/img/6a3ab5481308b742eefd256b790bd20f.png`
- `docs/img/7832e117c61c7ad9ade3ba1064fcbe74.png`
- `docs/img/1d1650dee61be955969dd600aad02c05.png`
- `docs/img/e455bc50cf1387386744060849b27109.png`
- `docs/img/e9508b74a5de4b50ece51c0d7d645541.png`
- `docs/img/82f62ea019ca018f8bd6f89a2211f4b9.png`
- `docs/img/90105f1400a5c625866dcd373b28953d.png`

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

### Step 2: ctfshow 萌新22 （类似级客巅峰web4）_Firebasky的博客-CSDN博客_ctf p神

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0044589c7115a39976baf63340ea5bcb`

### Step 3: 源代码

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `if(!preg_match("/\:|\/|\\\/i",$c)){` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if(!preg_match("/\:|\/|\\\/i",$c)){`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `if(!preg_match("/\:|\/|\\\/i",$c)){` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `?>`

### Step 4: register_argc_argv的介绍

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `661ec6937262a222d02b337b2f74a795`

### Step 5: PEAR的介绍

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `在linux下面安装直接输入命令`apt install php-pear``

### Step 6: 解题

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6a3ab5481308b742eefd256b790bd20f`

### Step 7: 方法一

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7832e117c61c7ad9ade3ba1064fcbe74`

### Step 8: 方法二

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat with the extracted filter/query `然后通过python3开一个http服务 `python3 -m http.server 81`` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `然后通过python3开一个http服务 `python3 -m http.server 81``
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat with the extracted filter/query `然后通过python3开一个http服务 `python3 -m http.server 81`` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `e455bc50cf1387386744060849b27109`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
