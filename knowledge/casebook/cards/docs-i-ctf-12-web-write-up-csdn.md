# i春秋网络内生安全试验场CTF夺旗赛（第四季）12月赛web write up题解_努力的学渣'#的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `i春秋网络内生安全试验场CTF夺旗赛（第四季）12月赛web`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/i春秋网络内生安全试验场CTF夺旗赛（第四季）12月赛web-write-up题解_努力的学渣'#的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/i%E6%98%A5%E7%A7%8B%E7%BD%91%E7%BB%9C%E5%86%85%E7%94%9F%E5%AE%89%E5%85%A8%E8%AF%95%E9%AA%8C%E5%9C%BACTF%E5%A4%BA%E6%97%97%E8%B5%9B%EF%BC%88%E7%AC%AC%E5%9B%9B%E5%AD%A3%EF%BC%8912%E6%9C%88%E8%B5%9Bweb-write-up%E9%A2%98%E8%A7%A3_%E5%8A%AA%E5%8A%9B%E7%9A%84%E5%AD%A6%E6%B8%A3%27%23%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/i春秋网络内生安全试验场CTF夺旗赛（第四季）12月赛web-write-up题解_努力的学渣'#的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: detect-it-easy, netcat
- Techniques: classical-crypto, command-injection, crypto-analysis, deserialization, encoding-analysis, file-inclusion, http-analysis, php-tricks, ret2libc, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `17`
- `docs/img/8df53c19708c26464630e9ad4da79213.png`
- `docs/img/fcacab3b4649a8da82fca2e67d177e4a.png`
- `docs/img/46d5a81f57bc0fdaa6878c0e0b0caf70.png`
- `docs/img/a256ed7b3486d8e179e99c4202e985b7.png`
- `docs/img/8fcb89d87cc7d46d50532eae8a1436dd.png`
- `docs/img/c619d6d135da66d9e1cbef6763b4ba4c.png`
- `docs/img/a8a5987ac5b8f9ef7fc0a0cc60379eb9.png`
- `docs/img/190f646c03088d1071bfd45164f20b3a.png`
- `docs/img/5c5b1bb6814f3d0e8285018338cfc1db.png`
- `docs/img/020a7520369290e79e5da37bb50e114d.png`
- `docs/img/c85a8d7f3133b2db4acb954ab38238f9.png`
- `docs/img/e4a4150b7ffe1f3e54204281aa076097.png`
- ... and `5` more

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

### Step 2: i春秋网络内生安全试验场CTF夺旗赛（第四季）12月赛web write up题解_努力的学渣'#的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* * *`

### Step 3: <mark>题目：nani</mark>

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8df53c19708c26464630e9ad4da79213`

### Step 4: <mark>题目：admin</mark>

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat with the extracted filter/query `if(isset($user)&&(file_get_contents($user,'r')==="admin")){` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if(isset($user)&&(file_get_contents($user,'r')==="admin")){`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat with the extracted filter/query `if(isset($user)&&(file_get_contents($user,'r')==="admin")){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `120.55.43.255:28119`

### Step 5: <mark>题目：Ping</mark>

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `'|' => '',` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `'|' => '',`
  - `'||' => '',`
  - `linux中：%0a 、%0d 、; 、& 、| 、&&、||`
  - `windows中：%0a、&、|、%1a（一个神奇的角色，作为.bat文件中的命令分隔符）`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy, netcat with the extracted filter/query `'|' => '',` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `190f646c03088d1071bfd45164f20b3a`

### Step 6: <mark>题目random</mark>

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if ($key == $true_key){` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if ($key == $true_key){`
  - `seed在mt_srand（）这个函数下出来的值要和post传入的key值相等才会执行下一步eval( "var_dump( a ) ; " ) 如 果 a);") 如果 a);")如果key == $true_key值不等，就会执行else这个进程die（）结束掉。**`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat with the extracted filter/query `if ($key == $true_key){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag.php`

### Step 7: ![在这里插入图片描述](img/c85a8d7f3133b2db4acb954ab38238f9.png)

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use detect-it-easy, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use detect-it-easy, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `e4a4150b7ffe1f3e54204281aa076097`

### Step 8: cut查看语句

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `120.55.43.255:22712`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
