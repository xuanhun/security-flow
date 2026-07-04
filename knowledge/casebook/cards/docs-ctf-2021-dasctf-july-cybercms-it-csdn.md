# 【CTF大赛】2021 DASCTF July cybercms 一探再探_IT老涵的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `【CTF大赛】2021 DASCTF July cybercms 一探再探`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF大赛】2021-DASCTF-July-cybercms-一探再探_IT老涵的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF%E5%A4%A7%E8%B5%9B%E3%80%912021-DASCTF-July-cybercms-%E4%B8%80%E6%8E%A2%E5%86%8D%E6%8E%A2_IT%E8%80%81%E6%B6%B5%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF大赛】2021-DASCTF-July-cybercms-一探再探_IT老涵的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat
- Techniques: browser-forensics, command-injection, file-upload, http-analysis, ret2libc, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `23`
- `docs/img/78e6b7d6d418ef9d252397dae9210c40.png`
- `docs/img/90cb237cd52aef622814510abc22e5eb.png`
- `docs/img/f09f44f89921ce0279b558eeb12b2f59.png`
- `docs/img/0b404f933e0b31040225c7d0dd7637f4.png`
- `docs/img/6946284d83a3447cd570503df08ef1b7.png`
- `docs/img/83f6fab34995be5056ff5255cbc4477c.png`
- `docs/img/af5c365a54c8f60fe6b2d626a46848e5.png`
- `docs/img/f2a76371c906f860586c14989b8fbac7.png`
- `docs/img/5d04d59fa2520c5070a3f47c5888d39e.png`
- `docs/img/cdb1b20ebcc717319ef52fef3cd47ef9.png`
- `docs/img/358cf441c03c509f971b242987e9996c.png`
- `docs/img/350793f8cfcaf004d3ce75123103e950.png`
- ... and `11` more

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

### Step 2: 【CTF大赛】2021 DASCTF July cybercms 一探再探_IT老涵的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/HBohan/article/details/119968677](https://blog.csdn.net/HBohan/article/details/119968677)`

### Step 3: 引言

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `这篇就来记录一下做这道题时候的心路历程吧……`

### Step 4: 题目初探

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `78e6b7d6d418ef9d252397dae9210c40`

### Step 5: 后台登录绕过 & 上传

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `90cb237cd52aef622814510abc22e5eb`

### Step 6: 源码泄露

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6946284d83a3447cd570503df08ef1b7`

### Step 7: 上传点源码审计

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f2a76371c906f860586c14989b8fbac7`

### Step 8: 另一个上传点审计

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `358cf441c03c509f971b242987e9996c`

### Step 9: SQL 注入写马（预期解）

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat with the extracted filter/query `return preg_replace('/select|insert | update | and | in | on | left | joins | delete |\%|\=|\.\.\/|\.\/| union | from | where | group | into |load_file` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `return preg_replace('/select|insert | update | and | in | on | left | joins | delete |\%|\=|\.\.\/|\.\/| union | from | where | group | into |load_file`
  - `|outfile/i','',$str);`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat with the extracted filter/query `return preg_replace('/select|insert | update | and | in | on | left | joins | delete |\%|\=|\.\.\/|\.\/| union | from | where | group | into |load_file` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `fee46ee0f140e90ad832fa4e80fa64d7`

### Step 10: <?php eval($_REQUEST['m']);?>

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fd4652a61a4b628cd0552c9e73bd61ad`

### Step 11: 上传点再探

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2906568be52062335c1d0da5cd5742df`

### Step 12: 小结

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c228f910793cdb17d32bbff1b85531b6`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
