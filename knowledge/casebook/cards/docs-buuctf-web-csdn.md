# buuctf web小结_绿冰壶的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `buuctf web小结`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/buuctf-web小结_绿冰壶的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/buuctf-web%E5%B0%8F%E7%BB%93_%E7%BB%BF%E5%86%B0%E5%A3%B6%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/buuctf-web小结_绿冰壶的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, email challenges.

## Input Signals

- Artifacts: binary, ciphertext, email, ids, web-app, web-service
- Tools: burp, detect-it-easy, netcat, z3
- Techniques: binary-exploitation, browser-forensics, classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, file-upload, http-analysis, php-tricks, ret2libc, sql-injection, ssti, symbolic-execution, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `19`
- `docs/img/c6b2b6b1cd7ad60737d861253edccbad.png`
- `docs/img/e9f384002dcb40c3b33a74b18df109be.png`
- `docs/img/07816fb18418bb43671a21fe84599cb6.png`
- `docs/img/b8fa56ac475e95affb30eb5157da7d2e.png`
- `docs/img/2ab14cead5c555039b1137360f2f8126.png`
- `docs/img/dfc89347b9368d7a6497814f207e3fde.png`
- `docs/img/27dbdab1586eeaae0621550f78338cc9.png`
- `docs/img/6bc1f4d34c585f4dc59c9380148e4f93.png`
- `docs/img/d95ceb0c2de5dba534799e240cf1fdaa.png`
- `docs/img/72973b03e737b882008029f2636feeb1.png`
- `docs/img/7ad05d5d1b6136a65d8b4b4b4ef3d40d.png`
- `docs/img/6c367bc19d2cde072b7ea23d8ebeb80b.png`
- ... and `7` more

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, z3 to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, z3
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: buuctf web小结_绿冰壶的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_42551635/article/details/116137579](https://blog.csdn.net/qq_42551635/article/details/116137579)`

### Step 3: .htaccess文件

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `本句话的作用是使该.htaccess文件所在目录及其子目录中的后缀为.xxx的文件被Apache当做php文件`

### Step 4: 一个傻逼错误

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, detect-it-easy, netcat, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, detect-it-easy, netcat, z3
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, detect-it-easy, netcat, z3 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `所以蚁剑里链接时不能重复输入`

### Step 5: 题解

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp, detect-it-easy, netcat, z3 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: burp, detect-it-easy, netcat, z3
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp, detect-it-easy, netcat, z3 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - The proof is the blocked primitive working through the filter path, not just a payload variation that reflects.
- Evidence rule: The proof is the blocked primitive working through the filter path, not just a payload variation that reflects.

### Step 6: 首先查看源码 发现链接

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, z3 to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, z3
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `点进去`

### Step 7: 发现一个button 点击 提示时间太短看不清

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `然后提示flag在flag.php里`

### Step 8: 通过url访问

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use burp, detect-it-easy, netcat, z3 to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: burp, detect-it-easy, netcat, z3
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use burp, detect-it-easy, netcat, z3 to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `失败，说明file可能被过滤了，通过源码发现有file传参，猜测有文件包含，使用文件包含访问源码`

### Step 9: [GXYCTF2019]Ping Ping Ping

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use burp, detect-it-easy, netcat, z3 to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: burp, detect-it-easy, netcat, z3
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use burp, detect-it-easy, netcat, z3 to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

### Step 10: 于是使用一些方法代替空格

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use burp, detect-it-easy, netcat, z3 with the extracted filter/query `?ip=127.0.0.1;echo$IFS$1Y2F0IGZsYWcucGhw|base64$IFS$1-d|sh` and inspect the matching evidence.
- Tools: burp, detect-it-easy, netcat, z3
- Filters or commands:
  - `?ip=127.0.0.1;echo$IFS$1Y2F0IGZsYWcucGhw|base64$IFS$1-d|sh`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use burp, detect-it-easy, netcat, z3 with the extracted filter/query `?ip=127.0.0.1;echo$IFS$1Y2F0IGZsYWcucGhw|base64$IFS$1-d|sh` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

### Step 11: exec

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use burp, detect-it-easy, netcat, z3 to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: burp, detect-it-easy, netcat, z3
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use burp, detect-it-easy, netcat, z3 to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `直接;cat /flag; 得到flag`

### Step 12: [极客大挑战 2019]Knife

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, netcat, z3 to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, netcat, z3
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, netcat, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `白给的shell 没啥好总结的 有手就行`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
