# i春秋CTF-WEB题解(一)_ 晓德的博客-CSDN博客_ctf题解

## Case Metadata

- Category: `Web`
- Platform: `i春秋CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/i春秋CTF-WEB题解(一)_-晓德的博客-CSDN博客_ctf题解.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/i%E6%98%A5%E7%A7%8BCTF-WEB%E9%A2%98%E8%A7%A3%28%E4%B8%80%29_-%E6%99%93%E5%BE%B7%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf%E9%A2%98%E8%A7%A3.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/i春秋CTF-WEB题解(一)_-晓德的博客-CSDN博客_ctf题解.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: detect-it-easy, netcat
- Techniques: command-injection, crypto-analysis, file-inclusion, file-upload, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `10`
- `docs/img/1aa9738fc1103f723e2cb089a48c236b.png`
- `docs/img/2f6746c0fd1391fa0fc2877c9d6bf10d.png`
- `docs/img/7440da70c315e361166a93dbbe4278a6.png`
- `docs/img/ced05459412e419fc32cc9e7905c7a74.png`
- `docs/img/fa46cb7017c27d2e08a95f90ec4a96b3.png`
- `docs/img/ec2de42af00b3ff596be29a00d8211cc.png`
- `docs/img/24a3e0070fb61c730886ff41e812b3b1.png`
- `docs/img/1ecd6b643d329d7a7dedfc87a3447001.png`
- `docs/img/1c562b4500e1939e8fdcb5e1e6481753.png`
- `docs/img/8aa1f80e50695445874635f8c3d677a7.png`

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: i春秋CTF-WEB题解(一)_ 晓德的博客-CSDN博客_ctf题解

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use detect-it-easy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_42271850/article/details/107139184](https://blog.csdn.net/weixin_42271850/article/details/107139184)`

### Step 3: 简述

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这次转到了i春秋平台上面练习，和之前一样也是每3道题目就写一篇题解来作为记录。`

### Step 4: 爆破-1（百度杯CTF比赛 2017 二月场）

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use detect-it-easy, netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use detect-it-easy, netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `1aa9738fc1103f723e2cb089a48c236b`

### Step 5: 爆破-2（百度杯CTF比赛 2017 二月场）

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7440da70c315e361166a93dbbe4278a6`

### Step 6: Upload（百度杯CTF比赛 九月场）

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use detect-it-easy, netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use detect-it-easy, netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `fa46cb7017c27d2e08a95f90ec4a96b3`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
