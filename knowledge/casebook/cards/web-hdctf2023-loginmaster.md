# [HDCTF 2023]LoginMaster

## Case Metadata

- Category: `Web`
- Platform: `HDCTF 2023`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/hdctf2023-loginmaster.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/hdctf2023-loginmaster.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/hdctf2023-loginmaster.md`
- Challenge URL: `https://www.nssctf.cn/problem/3782`

## Why This Case Matters

Use this case as a Web reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: Yakit, sqlmap, mysql, adminer, detect-it-easy, netcat
- Techniques: http-analysis, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `4`
- `web/images/2023-loginmaster-yakit-dirscan.png`
- `web/images/2023-loginmaster-yakit-dirscan-filter.png`
- `web/images/2023-loginmaster-sqldebug.png`
- `web/images/2023-loginmaster-yakit-payload.png`

## Solve Thinking

### Step 1: 第一轮

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use Yakit, sqlmap, mysql, adminer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: Yakit, sqlmap, mysql, adminer, detect-it-easy
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use Yakit, sqlmap, mysql, adminer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**题目关键信息列表**：`

### Step 2: 第一轮

- Route type: `Yakit-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use Yakit, sqlmap, mysql, adminer to collect the smallest evidence slice that answers the goal.
- Tools: Yakit, sqlmap, mysql, adminer, detect-it-easy
- Reasoning chain:
  - Recognize the section as Yakit-driven evidence lookup.
  - Use Yakit, sqlmap, mysql, adminer to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 3: 第一轮

- Route type: `Yakit-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use Yakit, sqlmap, mysql, adminer to collect the smallest evidence slice that answers the goal.
- Tools: Yakit, sqlmap, mysql, adminer, detect-it-easy
- Reasoning chain:
  - Recognize the section as Yakit-driven evidence lookup.
  - Use Yakit, sqlmap, mysql, adminer to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ````bash`

### Step 4: `--tamper` 该参数用于指定 `sqlmap` 的篡改脚本，这些脚本的作用是对发送给目标网站的 payload（攻击载荷、测试数据等）进行一定的变形或者处理，以绕过目标网站可能存在的一些简单的防护机制，比如对特定字符过滤、对常见 SQL 注入语句格式的检测等情况，增加 SQL 注入成功的几率。

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy, netcat, sqlmap, yakit with the extracted filter/query `sqlmap -u http://node4.anna.nssctf.cn:28077/index.php --data="username=admin&password=testpassword" -p password --proxy socks5://127.0.0.1:8083 --tamper "space2comment.py"` and inspect the matching evidence.
- Tools: detect-it-easy, netcat, sqlmap, yakit
- Filters or commands:
  - `sqlmap -u http://node4.anna.nssctf.cn:28077/index.php --data="username=admin&password=testpassword" -p password --proxy socks5://127.0.0.1:8083 --tamper "space2comment.py"`
  - `if(preg_match("/regexp|between|in|flag|=|>|<|and|\||right|left|reverse|update|extractvalue|floor|substr|&|;|\\\$|0x|sleep|\ /i",$s)){ // SQL 注入黑名单关键词，需要绕过`
  - `if ($row['password'] === $password) { // 要求输入的密码与数据库中实际取出的密码完全相等，这就意味着不能使用常规的 SQL 注入造成真值逻辑漏洞利用方式`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy, netcat, sqlmap, yakit with the extracted filter/query `sqlmap -u http://node4.anna.nssctf.cn:28077/index.php --data="username=admin&password=testpassword" -p password --proxy socks5://127.0.0.1:8083 --tamper "space2comment.py"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1:8083`

### Step 5: 本地 `SQL Debug 环境配置`

- Route type: `Yakit-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use Yakit, sqlmap, mysql, adminer to collect the smallest evidence slice that answers the goal.
- Tools: Yakit, sqlmap, mysql, adminer, detect-it-easy
- Reasoning chain:
  - Recognize the section as Yakit-driven evidence lookup.
  - Use Yakit, sqlmap, mysql, adminer to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ````bash`

### Step 6: 配置 mysql debug 环境

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use Yakit, sqlmap, mysql, adminer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: Yakit, sqlmap, mysql, adminer, detect-it-easy
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use Yakit, sqlmap, mysql, adminer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `cat README.md`

### Step 7: 提供内置 [adminer.php](https://www.adminer.org/) ，方便查看和管理 dvwa 的数据库。

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use Yakit, sqlmap, mysql, adminer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: Yakit, sqlmap, mysql, adminer, detect-it-easy
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use Yakit, sqlmap, mysql, adminer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `#`

### Step 8: 访问 http://<target_ip>:8086/adminer.php ，用户名 app ，密码 vulnerables

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use Yakit, sqlmap, mysql, adminer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: Yakit, sqlmap, mysql, adminer, detect-it-easy
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use Yakit, sqlmap, mysql, adminer to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - The proof is the request or response field such as Host, URI, header, body, or status.
- Evidence rule: The proof is the request or response field such as Host, URI, header, body, or status.

### Step 9: Yakit 爆破工具使用

- Route type: `yakit-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use yakit to collect the smallest evidence slice that answers the goal.
- Tools: yakit
- Reasoning chain:
  - Recognize the section as yakit-driven evidence lookup.
  - Use yakit to collect the smallest evidence slice that answers the goal.
  - The proof is the smallest artifact field that directly answers the goal.
- Evidence rule: The proof is the smallest artifact field that directly answers the goal.

### Step 10: Yakit 字典配置

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use yakit to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: yakit
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use yakit to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `日常做题过程中，多积累各种 **规模适中** 和 **用途专一** 的字典，方便在爆破过程中使用。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
