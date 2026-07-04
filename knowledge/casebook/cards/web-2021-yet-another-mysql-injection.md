# [第五空间 2021]yet_another_mysql_injection

## Case Metadata

- Category: `Web`
- Platform: `第五空间 2021`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/第五空间2021-yet_another_mysql_injection.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%E7%AC%AC%E4%BA%94%E7%A9%BA%E9%97%B42021-yet_another_mysql_injection.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/第五空间2021-yet_another_mysql_injection.md`
- Challenge URL: `https://www.nssctf.cn/problem/334`

## Why This Case Matters

Use this case as a Web reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: Yakit, sqlmap, mysql, adminer, detect-it-easy, netcat
- Techniques: command-injection, dns-analysis, file-inclusion, http-analysis, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `1`
- `web/images/2021-yet_another_mysql_injection-yakit-phpmyadmin.png`

## Solve Thinking

### Step 1: 第一轮

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use Yakit, sqlmap, mysql, adminer to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: Yakit, sqlmap, mysql, adminer, detect-it-easy
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use Yakit, sqlmap, mysql, adminer to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**题目关键信息列表**：`

### Step 2: 第一轮

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use Yakit, sqlmap, mysql, adminer to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: Yakit, sqlmap, mysql, adminer, detect-it-easy
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use Yakit, sqlmap, mysql, adminer to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - The proof is the returned command output or filesystem effect from the injected command.
- Evidence rule: The proof is the returned command output or filesystem effect from the injected command.

### Step 3: 第一轮

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat, yakit with the extracted filter/query `if(preg_match("/regexp|between|in|flag|=|>|<|and|\||right|left|reverse|update|extractvalue|floor|substr|&|;|\\\$|0x|sleep|\ /i",$s)){ // sql 注入黑名单关键词，需要绕过` and inspect the matching evidence.
- Tools: detect-it-easy, netcat, yakit
- Filters or commands:
  - `if(preg_match("/regexp|between|in|flag|=|>|<|and|\||right|left|reverse|update|extractvalue|floor|substr|&|;|\\\$|0x|sleep|\ /i",$s)){ // sql 注入黑名单关键词，需要绕过`
  - `if (isset($_POST['username']) && $_POST['username'] != '' && isset($_POST['password']) && $_POST['password'] != '') {`
  - `if ($username !== 'admin') {`
  - `if ($row['password'] === $password) {`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat, yakit with the extracted filter/query `if(preg_match("/regexp|between|in|flag|=|>|<|and|\||right|left|reverse|update|extractvalue|floor|substr|&|;|\\\$|0x|sleep|\ /i",$s)){ // sql 注入黑名单关键词，需要绕过` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `lib.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
