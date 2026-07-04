# [网鼎杯 2018]Fakebook

## Case Metadata

- Category: `Web`
- Platform: `网鼎杯 2018`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/[网鼎杯 2018]Fakebook.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%5B%E7%BD%91%E9%BC%8E%E6%9D%AF%202018%5DFakebook.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/[网鼎杯 2018]Fakebook.md`
- Challenge URL: `https://www.nssctf.cn/problem/20`

## Why This Case Matters

Use this case as a Web reference for web-app, web-service challenges.

## Input Signals

- Artifacts: web-app, web-service
- Tools: burp, netcat
- Techniques: binary-exploitation, deserialization, http-analysis, php-tricks, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `5`
- `web/images/[网鼎杯 2018]Fakebook-用户页面.png`
- `web/images/[网鼎杯 2018]Fakebook-报错页面.png`
- `web/images/[网鼎杯 2018]Fakebook-WAF.png`
- `web/images/[网鼎杯 2018]Fakebook-flag.php.png`
- `web/images/[网鼎杯 2018]Fakebook-flag.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**题目关键信息列表**：`

### Step 2: 想到什么解题思路

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `view.php`

### Step 3: 尝试过程和结果记录

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use burp, netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use burp, netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `view.php`

### Step 4: 结果1testba3253876aed6bc22d4a6ff53d8406c6ad864195ed144ab5c87621b6c233b548baeae6956df346ec8c17f5ea10f35ee3cbc514797ed7ddd3145464e2a0bab413O:8:"UserInfo":3:{s:4:"name";s:4:"test";s:3:"age";i:18;s:4:"blog";s:13:"www.baidu.com

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `?no=0%20union/**/select%201,group_concat(data),3,4 from users`

### Step 5: 结果

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `view.php`

### Step 6: O:8:"UserInfo":3:{s:4:"name";s:0:"";s:3:"age";i:0;s:4:"blog";s:29:"file:///var/www/html/view.php";}

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `flag.php`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
