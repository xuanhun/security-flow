# ctf web个人总结_recover517的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `ctf web个人总结`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/ctf-web个人总结_recover517的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/ctf-web%E4%B8%AA%E4%BA%BA%E6%80%BB%E7%BB%93_recover517%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/ctf-web个人总结_recover517的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app, web-service
- Tools: burp, detect-it-easy, dirb, netcat, nmap, sqlmap
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, file-upload, http-analysis, jwt-analysis, php-tricks, ret2libc, service-enumeration, sql-injection, waf-bypass, web-enumeration, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `2`
- `docs/img/2231369d65284680520c8ab9a4e239e2.png`
- `docs/img/63b6729be26a123ea174da7939bd5177.png`

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, dirb, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, dirb, netcat, nmap
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, dirb, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 工具

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use antsword, burp, detect-it-easy, dirb to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: antsword, burp, detect-it-easy, dirb, netcat, nmap, sqlmap
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use antsword, burp, detect-it-easy, dirb to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `…想到再补充`

### Step 3: 普通思路

- Route type: `jwt trust-boundary abuse`
- Why: JWT cases hinge on understanding what the server actually trusts: signature, claim, header, or backend lookup.
- Probe: Use dirb to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
- Tools: dirb
- Reasoning chain:
  - Recognize the section as jwt trust-boundary abuse.
  - Use dirb to inspect claims, signing assumptions, and verifier trust boundaries before mutating the token.
  - The proof is the server accepting the mutated claims or signature and exposing the gated action.
- Evidence rule: The proof is the server accepting the mutated claims or signature and exposing the gated action.

### Step 4: 注入思路

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat, sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat, sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `确认可以时间盲注的话，就可以编写脚本进行爆破`

### Step 5: 文件包含漏洞

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `xxxx.php`

### Step 6: 显示源码类型

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use burp, detect-it-easy, dirb, netcat with the extracted filter/query `2. 可利用的php函数的一些特性，比如在做字符串比较的时候，如:`0==$_GET['a']`, 首先带那种过滤了`$_GET`，让你无法提交数字，但是根据php的一些特性，你提交字符串时，在判断时会被强转成数字。` and inspect the matching evidence.
- Tools: burp, detect-it-easy, dirb, netcat, nmap
- Filters or commands:
  - `2. 可利用的php函数的一些特性，比如在做字符串比较的时候，如:`0==$_GET['a']`, 首先带那种过滤了`$_GET`，让你无法提交数字，但是根据php的一些特性，你提交字符串时，在判断时会被强转成数字。`
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use burp, detect-it-easy, dirb, netcat with the extracted filter/query `2. 可利用的php函数的一些特性，比如在做字符串比较的时候，如:`0==$_GET['a']`, 首先带那种过滤了`$_GET`，让你无法提交数字，但是根据php的一些特性，你提交字符串时，在判断时会被强转成数字。` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `fl4g.php`

### Step 7: 绕过类

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `grep` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `grep`
  - `|`
  - `||`
  - `if(!preg_match("/\;|[a-z]|[0-9]|\`|\%|\x09|\x26|\>|\</i", $cmd)){`
  - `$(printf "\154\163") ==>ls`
  - `$(printf "\x63\x61\x74\x20\x2f\x66\x6c\x61\x67") ==>cat /flag`
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use detect-it-easy, netcat with the extracted filter/query `grep` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `101.34.94.44:7001`

### Step 8: 伪协议

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat with the extracted filter/query `php://filter/[read|write]=????/resource=???` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `php://filter/[read|write]=????/resource=???`
  - `mysql ===> 3306`
  - `postgresql ===>`
  - `fastcgi ===> 9000`
  - `redis ===> 6379`
  - `if ($_SERVER["REMOTE_ADDR"] != "127.0.0.1") {`
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat with the extracted filter/query `php://filter/[read|write]=????/resource=???` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1:6379`

### Step 9: 反弹shell

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, dirb, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, dirb, netcat, nmap
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, dirb, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `在近期的夺旗赛中，有一道题目，通过层层挖掘，找到了一个一句话木马的页面，但是系统禁用了很多执行函数，但是开放了一个叫PCNTL 函数，可以利用这个函数进行脚本执行，利用执行到的反弹shell进行服务器shell执行`

### Step 10: xss和csrf

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use burp, detect-it-easy, dirb, netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
- Tools: burp, detect-it-easy, dirb, netcat, nmap
- Reasoning chain:
  - Recognize the section as xss route.
  - Use burp, detect-it-easy, dirb, netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `会有专门的机器人来跑脚本去出发你的payload，不过没遇到过`

### Step 11: 混合型

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, detect-it-easy, dirb, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, detect-it-easy, dirb, netcat, nmap
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, detect-it-easy, dirb, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* * *`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
