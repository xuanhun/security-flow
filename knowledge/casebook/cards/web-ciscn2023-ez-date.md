# [CISCN 2023 华北]ez_date

## Case Metadata

- Category: `Web`
- Platform: `CISCN 2023 华北`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/CISCN2023华北-ez_date.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/CISCN2023%E5%8D%8E%E5%8C%97-ez_date.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/CISCN2023华北-ez_date.md`
- Challenge URL: `https://www.nssctf.cn/problem/4096`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: PHP环境, netcat
- Techniques: classical-crypto, deserialization, encoding-analysis, http-analysis, php-tricks, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: 看到什么

- Route type: `PHP环境-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use PHP环境, netcat to collect the smallest evidence slice that answers the goal.
- Tools: PHP环境, netcat
- Reasoning chain:
  - Recognize the section as PHP环境-driven evidence lookup.
  - Use PHP环境, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**题目关键信息列表**：`

### Step 2: 想到什么解题思路

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use PHP环境, netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: PHP环境, netcat
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use PHP环境, netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `可能是考察 PHP 的反序列化；`

### Step 3: 尝试过程和结果记录

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use PHP环境, netcat with the extracted filter/query ``if(is_array($this->a)||is_array($this->b))`说明`$a`和`$b`不能为数组，不能使用数组绕过；` and inspect the matching evidence.
- Tools: PHP环境, netcat
- Filters or commands:
  - ``if(is_array($this->a)||is_array($this->b))`说明`$a`和`$b`不能为数组，不能使用数组绕过；`
  - ``if( ($this->a !== $this->b) && (md5($this->a) === md5($this->b)) && (sha1($this->a)=== sha1($this->b)) )``
  - `if( ($a !== $b) && (md5($a) === md5($b)) && (sha1($a)=== sha1($b)) ){`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use PHP环境, netcat with the extracted filter/query ``if(is_array($this->a)||is_array($this->b))`说明`$a`和`$b`不能为数组，不能使用数组绕过；` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c4ca4238a0b923820dcc509a6f75849b`

### Step 4: 可以通过转义符'\'避免被转义

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use netcat to confirm object injection and map the gadget or magic-method path before building the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `echo base64_encode(serialize($a));`

### Step 5: Tzo0OiJkYXRlIjozOntzOjE6ImEiO2k6MTtzOjE6ImIiO3M6MToiMSI7czo0OiJmaWxlIjtzOjg6Ii9mXGxcYVxnIjt9

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use PHP环境, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: PHP环境, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use PHP环境, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
