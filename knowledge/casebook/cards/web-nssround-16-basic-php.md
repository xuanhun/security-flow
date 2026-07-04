# [NSSRound_16 Basic]了解过PHP特性吗

## Case Metadata

- Category: `Web`
- Platform: `NSSRound_16 Basic`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/[NSSRound#16 Basic]了解过PHP特性吗.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%5BNSSRound%2316%20Basic%5D%E4%BA%86%E8%A7%A3%E8%BF%87PHP%E7%89%B9%E6%80%A7%E5%90%97.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/[NSSRound#16 Basic]了解过PHP特性吗.md`
- Challenge URL: `https://www.nssctf.cn/problem/5059`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: PHP环境, detect-it-easy, netcat
- Techniques: command-injection, file-inclusion, http-analysis, php-tricks, ret2libc, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: 解题思路

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if (ctype_alpha($ctype) && is_numeric($is_num) && md5($ctype) == md5($is_num)) {` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if (ctype_alpha($ctype) && is_numeric($is_num) && md5($ctype) == md5($is_num)) {`
  - `if ($arr4y[$i] === "NSS") {`
  - `if (array_search("NSS", $arr4y) === 0) {`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat with the extracted filter/query `if (ctype_alpha($ctype) && is_numeric($is_num) && md5($ctype) == md5($is_num)) {` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `rce.php`

### Step 2: 解题过程

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `这里检查`ctype_alpha($ctype)`和`is_numeric($is_num)`，并且要求`md5($ctype) == md5($is_num)`。` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `这里检查`ctype_alpha($ctype)`和`is_numeric($is_num)`，并且要求`md5($ctype) == md5($is_num)`。`
  - `这里检查`$arr4y`是否为数组，并且要求数组中元素不强等于`"NSS"`，同时将数组元素转换为整数，最后检查`array_search("NSS", $arr4y) === 0`。`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use detect-it-easy, netcat with the extracted filter/query `这里检查`ctype_alpha($ctype)`和`is_numeric($is_num)`，并且要求`md5($ctype) == md5($is_num)`。` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `0e830400451993494058024219903391`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
