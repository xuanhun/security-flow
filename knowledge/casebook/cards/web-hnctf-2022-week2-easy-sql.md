# [HNCTF 2022 WEEK2]easy_sql

## Case Metadata

- Category: `Web`
- Platform: `HNCTF 2022 WEEK2`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `web/[HNCTF 2022 WEEK2]easy_sql.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/web/%5BHNCTF%202022%20WEEK2%5Deasy_sql.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/web/[HNCTF 2022 WEEK2]easy_sql.md`
- Challenge URL: `https://www.nssctf.cn/problem/2952`

## Why This Case Matters

Use this case as a Web reference for web-app, web-service challenges.

## Input Signals

- Artifacts: web-app, web-service
- Tools: burp, sqlmap, netcat
- Techniques: http-analysis, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `3`
- `web/images/[HNCTF 2022 WEEK2]easy_sql-waf.png`
- `web/images/[HNCTF 2022 WEEK2]easy_sql-table.png`
- `web/images/[HNCTF 2022 WEEK2]easy_sql-database.png`

## Solve Thinking

### Step 1: 看到什么

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, sqlmap, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, sqlmap, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, sqlmap, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `**题目关键信息列表**：`

### Step 2: 想到什么解题思路

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp, sqlmap to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: burp, sqlmap
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp, sqlmap to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - The proof is the blocked primitive working through the filter path, not just a payload variation that reflects.
- Evidence rule: The proof is the blocked primitive working through the filter path, not just a payload variation that reflects.

### Step 3: 尝试过程和结果记录

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp, netcat, sqlmap to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: burp, netcat, sqlmap
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp, netcat, sqlmap to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- `id`设置为`information`时，提示`error`，都是字符串，但是结果不同，说明存在WAF。图中响应长度为`530`的都是被过滤的。空格和`order`，`and` 等等这些都被过滤了。`

### Step 4: 正常

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, sqlmap, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, sqlmap, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, sqlmap, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `1'/**/group/**/by/**/3,'1`

### Step 5: error

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, sqlmap, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, sqlmap, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, sqlmap, netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1'/**/union/**/select/**/1,2,database()/**/'1`

### Step 6: 正常语句爆表名的时候，出现error,是因为information被过滤了。

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `1'/**/union/**/select/**/1,2,group_concat(table_name)/**/from/**/information_schema.tables/**/where/**/table_schema=database()/**/'1`

### Step 7: 换成mysql.innodb_table_stats,但是这个时候就是查询所有数据库里的所有表，没有表和数据库的关系。

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `- `1`作用是查询 子查询（虚拟表）的第一列。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
