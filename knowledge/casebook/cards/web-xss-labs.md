# 当堂XSS-labs 挑战

## Case Metadata

- Category: `Web`
- Platform: `当堂XSS`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/xss-labs.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/xss-labs.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/xss-labs.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat, radare2
- Techniques: classical-crypto, crypto-analysis, encoding-analysis, http-analysis, service-enumeration, waf-bypass, web-exploitation, xss

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `13`
- `web/images/xss-labs_闭合.png`
- `web/images/xss-labs_输入被转义.png`
- `web/images/xss-labs_onclick执行结果.png`
- `web/images/xss-labs_href被过滤.png`
- `web/images/xss-labs_友情链接.png`
- `web/images/xss-labs_引号和script被过滤.png`
- `web/images/xss-labs_被替换.png`
- `web/images/xss-labs_网页源代码.png`
- `web/images/xss-labs_修改前端页面隐藏域.png`
- `web/images/xss-labs_前端修改.png`
- `web/images/xss-labs_referer注入.png`
- `web/images/xss-labs_ua头注入.png`
- ... and `1` more

## Solve Thinking

### Step 1: 分享人：tonglinggejimo

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

### Step 2: Level 1：最基础的XSS注入

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use netcat, radare2 to verify the sink, context, and trigger condition before choosing the smallest executable payload.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as xss route.
  - Use netcat, radare2 to verify the sink, context, and trigger condition before choosing the smallest executable payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

### Step 3: Level 1 - 直接注入

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

### Step 4: Level 2：HTML属性闭合技巧

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

### Step 5: Level 2 - 分析

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use netcat, radare2 to verify the sink, context, and trigger condition before choosing the smallest executable payload.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as xss route.
  - Use netcat, radare2 to verify the sink, context, and trigger condition before choosing the smallest executable payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

### Step 6: Level 2 - 解决方案

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

### Step 7: Level 3：HTML特殊字符转义绕过

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat, radare2 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat, radare2 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

### Step 8: Level 3 - 问题分析

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as xss route.
  - Use netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

### Step 9: Level 3 - 绕过方法

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as xss route.
  - Use netcat to verify the sink, context, and trigger condition before choosing the smallest executable payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

### Step 10: 其他可用的事件处理程序

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

### Step 11: Level 3 - 源码分析

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

### Step 12: htmlspecialchars 函数转换表

- Route type: `xss route`
- Why: XSS cases should classify the rendering context before payload design.
- Probe: Use netcat, radare2 with the extracted filter/query `| 字符 | 替换后 |` and inspect the matching evidence.
- Tools: netcat, radare2
- Filters or commands:
  - `| 字符 | 替换后 |`
  - `| :----: | :----: |`
  - `| `&` (& 符号) | `&amp;` |`
  - `| `"` (双引号) | `&quot;` |`
  - `| `'` (单引号) | `&#039;` |`
  - `| `<` (小于) | `&lt;` |`
- Reasoning chain:
  - Recognize the section as xss route.
  - Use netcat, radare2 with the extracted filter/query `| 字符 | 替换后 |` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `---`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
