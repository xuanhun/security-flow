# 如何在ctf解题实战中绕过disable_function_YnG_t0的博客-CSDN博客_disablefunctions 绕过

## Case Metadata

- Category: `Web`
- Platform: `如何在ctf解题实战中绕过disable`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/如何在ctf解题实战中绕过disable_function_YnG_t0的博客-CSDN博客_disablefunctions-绕过.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E5%A6%82%E4%BD%95%E5%9C%A8ctf%E8%A7%A3%E9%A2%98%E5%AE%9E%E6%88%98%E4%B8%AD%E7%BB%95%E8%BF%87disable_function_YnG_t0%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_disablefunctions-%E7%BB%95%E8%BF%87.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/如何在ctf解题实战中绕过disable_function_YnG_t0的博客-CSDN博客_disablefunctions-绕过.md`

## Why This Case Matters

Use this case as a Web reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: detect-it-easy, netcat
- Techniques: binary-exploitation, classical-crypto, command-injection, crypto-analysis, encoding-analysis, file-inclusion, http-analysis, privilege-escalation, ret2libc, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `18`
- `docs/img/b886b6bbc469ec7c3c6815dfb5a9f59f.png`
- `docs/img/0b80fd77e395c47e33eef656b82402ee.png`
- `docs/img/bdd44bbc1515ae2dc50fafb483a92a6f.png`
- `docs/img/cdad703f4fb8e3cbaa7229ef3d0409ad.png`
- `docs/img/5a9c886bd3760d75579ef63c1d00fccb.png`
- `docs/img/85f85d3a351e61b1c3e1e557288c14ca.png`
- `docs/img/1e53c10001d19a774292968ca3e924fc.png`
- `docs/img/b200ac1e669ae56ed8c22d2a20574a4f.png`
- `docs/img/9a6355ce8c991b84655d30362332447e.png`
- `docs/img/909dfebb0c5333ba50eabac7526aa727.png`
- `docs/img/22f1608ffcde23405ade037e21bfe2a1.png`
- `docs/img/5cab03b7a8e2af07f70202fa83e07ec1.png`
- ... and `6` more

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

### Step 2: 如何在ctf解题实战中绕过disable_function_YnG_t0的博客-CSDN博客_disablefunctions 绕过

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use detect-it-easy, netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use detect-it-easy, netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_47168481/article/details/122638886](https://blog.csdn.net/qq_47168481/article/details/122638886)`

### Step 3: 文章介绍

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.

### Step 4: 利用pcntl_exec函数

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `CVE-2017-9841`

### Step 5: 利用LD_PRELOAD 环境变量

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `b200ac1e669ae56ed8c22d2a20574a4f`

### Step 6: 题目分析过程

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `9a6355ce8c991b84655d30362332447e`

### Step 7: 利用蚁剑插件

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use antsword, detect-it-easy, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: antsword, detect-it-easy, netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use antsword, detect-it-easy, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `dac481c96a293d46357095dd86e66638`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
