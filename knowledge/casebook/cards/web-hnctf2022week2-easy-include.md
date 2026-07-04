# [HNCTF 2022 WEEK2]easy_include

## Case Metadata

- Category: `Web`
- Platform: `HNCTF 2022 WEEK2`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/HNCTF2022WEEK2-easy_include.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/HNCTF2022WEEK2-easy_include.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/HNCTF2022WEEK2-easy_include.md`
- Challenge URL: `https://www.nssctf.cn/problem/2948`

## Why This Case Matters

Use this case as a Web reference for linux-logs, web-app challenges.

## Input Signals

- Artifacts: linux-logs, web-app
- Tools: Yakit, 蚁剑, detect-it-easy, netcat
- Techniques: command-injection, file-inclusion, http-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `6`
- `web/<images/[HNCTF 2022 WEEK2]easy_include-passwd.jpg>`
- `web/<images/[HNCTF 2022 WEEK2]easy_include-access_log.jpg>`
- `web/<images/[HNCTF 2022 WEEK2]easy_include-phpinfo.jpg>`
- `web/<images/[HNCTF 2022 WEEK2]easy_include-eval.jpg>`
- `web/<images/[HNCTF 2022 WEEK2]easy_include-antsword.jpg>`
- `web/<images/[HNCTF 2022 WEEK2]easy_include-flag.jpg>`

## Solve Thinking

### Step 1: 看到什么

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat with the extracted filter/query `if(preg_match("/php|flag|data|\~|\!|\@|\#|\\$|\%|\^|\&|\*|\(|\)|\-|\_|\+|\=/i", $file)){` and inspect the matching evidence.
- Tools: detect-it-easy, netcat
- Filters or commands:
  - `if(preg_match("/php|flag|data|\~|\!|\@|\#|\\$|\%|\^|\&|\*|\(|\)|\-|\_|\+|\=/i", $file)){`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat with the extracted filter/query `if(preg_match("/php|flag|data|\~|\!|\@|\#|\\$|\%|\^|\&|\*|\(|\)|\-|\_|\+|\=/i", $file)){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- 过滤特殊符号（如~、!、@、$等）`

### Step 2: 想到什么解题思路

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - The proof is the included file content or wrapper output returned by the controlled path.
- Evidence rule: The proof is the included file content or wrapper output returned by the controlled path.

### Step 3: 尝试过程和结果记录

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use antsword, netcat, yakit to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: antsword, netcat, yakit
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use antsword, netcat, yakit to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `![alt text](<images/[HNCTF 2022 WEEK2]easy_include-flag.jpg>)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
