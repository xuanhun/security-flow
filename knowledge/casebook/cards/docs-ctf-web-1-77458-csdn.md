# CTF实验吧-WEB专题-1_77458的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `CTF实验吧`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF实验吧-WEB专题-1_77458的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E5%AE%9E%E9%AA%8C%E5%90%A7-WEB%E4%B8%93%E9%A2%98-1_77458%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF实验吧-WEB专题-1_77458的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: not detected
- Techniques: command-injection, crypto-analysis, encoding-analysis, http-analysis, qr-analysis, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `9`
- `docs/img/20e3f75a7b5a4d0dd02c183a0ee89092.png`
- `docs/img/d6a245fd60a7c8ad2173105c1ac29e06.png`
- `docs/img/fe0e2774ce002c273bc5f3d5088d0923.png`
- `docs/img/1fd88ba74ea13268f03a7cb2891eb30b.png`
- `docs/img/0b1020d0b9a688c5825aad896c25e6d6.png`
- `docs/img/d3363456d08648d94a49f3494cbb7ca0.png`
- `docs/img/797ad33fb94116aa5a8533baeed51f14.png`
- `docs/img/074eddf99b6842011ac0ba72628ed83f.png`
- `docs/img/afd636eabbe65cff29ce86e9f4533337.png`

## Solve Thinking

### Step 1: Document

- Route type: `evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF实验吧-WEB专题-1_77458的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_18661257/article/details/53739543](https://blog.csdn.net/qq_18661257/article/details/53739543)`

### Step 3: **1.登陆一下好吗??**

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use the artifact-specific tool to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use the artifact-specific tool to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `20e3f75a7b5a4d0dd02c183a0ee89092`

### Step 4: **2.who are you?**

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use the artifact-specific tool to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use the artifact-specific tool to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `d6a245fd60a7c8ad2173105c1ac29e06`

### Step 5: **3.因缺思汀的绕过**

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use the artifact-specific tool with the extracted filter/query `这里只提一下rollup的作用，他会根据某一个列进行组合，然后会产生null值，就是让最终的表中有多个null值，然而我们要利用的就是null==null，嘿` and inspect the matching evidence.
- Filters or commands:
  - `这里只提一下rollup的作用，他会根据某一个列进行组合，然后会产生null值，就是让最终的表中有多个null值，然而我们要利用的就是null==null，嘿`
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use the artifact-specific tool with the extracted filter/query `这里只提一下rollup的作用，他会根据某一个列进行组合，然后会产生null值，就是让最终的表中有多个null值，然而我们要利用的就是null==null，嘿` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `797ad33fb94116aa5a8533baeed51f14`

### Step 6: **4.简单的sql注入之3**

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use the artifact-specific tool to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use the artifact-specific tool to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `afd636eabbe65cff29ce86e9f4533337`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
