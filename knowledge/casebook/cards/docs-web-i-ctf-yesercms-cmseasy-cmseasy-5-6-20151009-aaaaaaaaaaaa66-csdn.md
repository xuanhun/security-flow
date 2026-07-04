# [WEB攻防] i春秋- “百度杯”CTF比赛 十二月场-YeserCMS cmseasy CmsEasy_5.6_20151009 无限制报错注入 复现过程_AAAAAAAAAAAA66的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `WEB攻防`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/[WEB攻防]-i春秋--“百度杯”CTF比赛-十二月场-YeserCMS-cmseasy-CmsEasy_5.6_20151009-无限制报错注入-复现过程_AAAAAAAAAAAA66的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%5BWEB%E6%94%BB%E9%98%B2%5D-i%E6%98%A5%E7%A7%8B--%E2%80%9C%E7%99%BE%E5%BA%A6%E6%9D%AF%E2%80%9DCTF%E6%AF%94%E8%B5%9B-%E5%8D%81%E4%BA%8C%E6%9C%88%E5%9C%BA-YeserCMS-cmseasy-CmsEasy_5.6_20151009-%E6%97%A0%E9%99%90%E5%88%B6%E6%8A%A5%E9%94%99%E6%B3%A8%E5%85%A5-%E5%A4%8D%E7%8E%B0%E8%BF%87%E7%A8%8B_AAAAAAAAAAAA66%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/[WEB攻防]-i春秋--“百度杯”CTF比赛-十二月场-YeserCMS-cmseasy-CmsEasy_5.6_20151009-无限制报错注入-复现过程_AAAAAAAAAAAA66的博客-CSDN博客.md`

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

- Referenced assets: `17`
- `docs/img/92593b0ba33e5d893ad1691ccbcbfd8e.png`
- `docs/img/08d4bfe002c6a15dce22fe03e6775806.png`
- `docs/img/40b5ce30e4a03f05dd483892a2b3687d.png`
- `docs/img/2accc5bc489ffccc37d7f7e302efd490.png`
- `docs/img/5628895f82995641fd4a1a34b1f01bf4.png`
- `docs/img/42f16896d6f1a8c3ee1c75d85bc77c71.png`
- `docs/img/1e2b26f491fe0381ca0a8ba58b54af2d.png`
- `docs/img/f6377571a2c5296f59e492fa20dd30b0.png`
- `docs/img/837f8e406718c7d7a312b601a5e8b10a.png`
- `docs/img/c9919d43e72a38271dd52c44533425a1.png`
- `docs/img/4111771a4611c794669741909bd79889.png`
- `docs/img/2c5ef8e027a814b855c7e5574f0e3dac.png`
- ... and `5` more

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

### Step 2: [WEB攻防] i春秋- “百度杯”CTF比赛 十二月场-YeserCMS cmseasy CmsEasy_5.6_20151009 无限制报错注入 复现过程_AAAAAAAAAAAA66的博客-CSDN博客

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat, radare2 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `20.php`

### Step 3: 题目

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `92593b0ba33e5d893ad1691ccbcbfd8e`

### Step 4: 寻找方向

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 但是要按照题目意思来，毕竟这是比赛，时间还是比较紧张的，不可能让你在没漏洞的地方浪费时间，而是给了你一点提示`

### Step 5: flag .php

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `40b5ce30e4a03f05dd483892a2b3687d`

### Step 6: YearsCMS

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `5628895f82995641fd4a1a34b1f01bf4`

### Step 7: 报错注入

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat, radare2, sqlmap with the extracted filter/query `(UpdateXML(1,CONCAT(0x5b,mid((SELECT/**/GROUP_CONCAT(concat(username,'|',password)) from cmseasy_user),1,32),0x5d),1)),NULL,NULL,NULL,NULL,NULL,NULL)-- </q></xjxquery>` and inspect the matching evidence.
- Tools: netcat, radare2, sqlmap
- Filters or commands:
  - `(UpdateXML(1,CONCAT(0x5b,mid((SELECT/**/GROUP_CONCAT(concat(username,'|',password)) from cmseasy_user),1,32),0x5d),1)),NULL,NULL,NULL,NULL,NULL,NULL)-- </q></xjxquery>`
  - `[admin|ff512d4240cbbdeafada404677ccbe61]`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat, radare2, sqlmap with the extracted filter/query `(UpdateXML(1,CONCAT(0x5b,mid((SELECT/**/GROUP_CONCAT(concat(username,'|',password)) from cmseasy_user),1,32),0x5d),1)),NULL,NULL,NULL,NULL,NULL,NULL)-- </q></xjxquery>` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `42f16896d6f1a8c3ee1c75d85bc77c71`

### Step 8: 后台读取flag

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat, radare2 to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat, radare2 to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `16461effce01fa2682149df51ed6a373`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
