# 第三届上海市大学生网络安全大赛 i春秋CTF Web解题思路_曹振国cc的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `第三届上海市大学生网络安全大赛 i春秋CTF Web解题思路`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/第三届上海市大学生网络安全大赛-i春秋CTF-Web解题思路_曹振国cc的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E7%AC%AC%E4%B8%89%E5%B1%8A%E4%B8%8A%E6%B5%B7%E5%B8%82%E5%A4%A7%E5%AD%A6%E7%94%9F%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8%E5%A4%A7%E8%B5%9B-i%E6%98%A5%E7%A7%8BCTF-Web%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF_%E6%9B%B9%E6%8C%AF%E5%9B%BDcc%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/第三届上海市大学生网络安全大赛-i春秋CTF-Web解题思路_曹振国cc的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: netcat, sqlmap
- Techniques: sql-injection, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `12`
- `docs/img/d7c0aeae43d51c55a7ff0a5c5eccb6d7.png`
- `docs/img/c35ab1af7a2b576935558f9b033464c3.png`
- `docs/img/1a72d8d73f7d44b38a111f97096344b9.png`
- `docs/img/da51a26ba3e207f8a5d7c3858b51ef11.png`
- `docs/img/494cb3d53c2058b292dfa28a04d38ff0.png`
- `docs/img/6eb43be18c3fd7edc3c1af6db3e9e029.png`
- `docs/img/1e0e88dc3242bca3f8b0363b3e72d6fd.png`
- `docs/img/fb241eb6eff4afccdeeaaeee426b6883.png`
- `docs/img/294d5a61a5aa64ad51da125faf632cd9.png`
- `docs/img/f2cde005f507946cfdd5660e91c78e82.png`
- `docs/img/1f7b00860462cc2ee5f46d1a795829d3.png`
- `docs/img/bdf0337a35971e8cca90467e2e8493f1.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 第三届上海市大学生网络安全大赛 i春秋CTF Web解题思路_曹振国cc的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, sqlmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_45736958/article/details/116329558](https://blog.csdn.net/weixin_45736958/article/details/116329558)`

### Step 3: 发现SQL注入

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat, sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat, sqlmap to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `d7c0aeae43d51c55a7ff0a5c5eccb6d7`

### Step 4: 尝试SQLMap

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `c35ab1af7a2b576935558f9b033464c3`

### Step 5: 经实验发现过滤了"=“和"and”

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1a72d8d73f7d44b38a111f97096344b9`

### Step 6: reverse()函数

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `294d5a61a5aa64ad51da125faf632cd9`

### Step 7: flag

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
- Tools: netcat, sqlmap
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, sqlmap to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `* * *`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
