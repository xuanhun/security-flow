# De1CTF2020的Web部分题解_合天网安实验室的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `De1CTF2020的Web部分题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/De1CTF2020的Web部分题解_合天网安实验室的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/De1CTF2020%E7%9A%84Web%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_%E5%90%88%E5%A4%A9%E7%BD%91%E5%AE%89%E5%AE%9E%E9%AA%8C%E5%AE%A4%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/De1CTF2020的Web部分题解_合天网安实验室的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: detect-it-easy, netcat
- Techniques: binary-exploitation, browser-forensics, command-injection, crypto-analysis, dns-analysis, file-upload, http-analysis, misc-analysis, php-tricks, ret2libc, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `14`
- `docs/img/6a69c5d9d863e46dff52a7c85674ffaa.png`
- `docs/img/f8ffff9e401780be6391b6725c833a88.png`
- `docs/img/8b78882741074bb38dd70b62df3ce928.png`
- `docs/img/20bd85d99812a5e2d10abd8a768e4927.png`
- `docs/img/e0dbebe29a0483d6e97364fc5962c77f.png`
- `docs/img/f73adc724df2a4056f458228484b10cb.png`
- `docs/img/f500842db24dc421650a9d3771040791.png`
- `docs/img/5816d6d32aad228ae8392e77fdb59f04.png`
- `docs/img/d1792d63dcd7296f4fbe2e3f26194aeb.png`
- `docs/img/d59c568df71eb0604de66c5751873f6f.png`
- `docs/img/7137ed3a96d9d573a49fa55cbbb8a347.png`
- `docs/img/a7ec9414c2992584e2bddd00f02209e3.png`
- ... and `2` more

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: De1CTF2020的Web部分题解_合天网安实验室的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_38154820/article/details/106205544](https://blog.csdn.net/qq_38154820/article/details/106205544)`

### Step 3: 前言

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `题目质量很好，虽然很难但是学到不少东西！`

### Step 4: 打开题目页面如下：

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6a69c5d9d863e46dff52a7c85674ffaa`

### Step 5: 题目是一个文件上传挑战，于是先上传一个`.php`后缀的文件先式式，不出意料失败，那么我们就上传一张`.jpg`的图片试试，结果如下：

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `perl|pyth|ph|auto|curl|base|>|rm|ruby|openssl|war|lua|msf|xter|telnet in contents!` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `perl|pyth|ph|auto|curl|base|>|rm|ruby|openssl|war|lua|msf|xter|telnet in contents!`
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use detect-it-easy, netcat with the extracted filter/query `perl|pyth|ph|auto|curl|base|>|rm|ruby|openssl|war|lua|msf|xter|telnet in contents!` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `perl|pyth|ph|auto|curl|base|>|rm|ruby|openssl|war|lua|msf|xter|telnet in contents!`

### Step 6: 字符，而且我们上传的图片不能解析，因此我们可以上传一个`.htaccess`，添加其他后缀名解析为`.php`文件。如：`AddType application/x-httpd-php shell.ppt`。不过由于`php`字符串的过滤我们上传的文件不能包含`php`，因此我们上传的`.httacess`文件中的`php`可以用换行符绕过，对于上传了的`shell.ppt`文件，如果该php开启了短标签我们可以用短标签`<?=`来代替

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `129.204.21.115`

### Step 7: 结果如下：

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `001149b089f853aad2bda9214b94fb21`

### Step 8: 上传`shell.ppt`:

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `129.204.21.115`

### Step 9: 结果如下：

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `001149b089f853aad2bda9214b94fb21`

### Step 10: 得到flag：

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `De1ctf{cG1_cG1_cg1_857_857_cgll111ll11lll}`

### Step 11: 合天网安实验室相关实验：

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use detect-it-easy, netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use detect-it-easy, netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> ###### 绕过黑名单检查实现文件上传1http://hetianlab.com/expc.do?ec=ECIDc089-d935-4f8d-b0bd-d2342ea4423f（通过本实验了解文件上传漏洞产生的原因，掌握绕过黑名单实现文件上传的利用方法）`

### Step 12: 题目打开是一个计算器，从打开的tab来看是一个使用`spring boot`框架的web项目。

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f8ffff9e401780be6391b6725c833a88`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
