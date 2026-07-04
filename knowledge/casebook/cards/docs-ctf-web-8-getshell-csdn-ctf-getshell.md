# CTF_Web：8位以内可控字符getshell_星辰照耀你我的博客-CSDN博客_ctf getshell

## Case Metadata

- Category: `Web`
- Platform: `CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF_Web：8位以内可控字符getshell_星辰照耀你我的博客-CSDN博客_ctf-getshell.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF_Web%EF%BC%9A8%E4%BD%8D%E4%BB%A5%E5%86%85%E5%8F%AF%E6%8E%A7%E5%AD%97%E7%AC%A6getshell_%E6%98%9F%E8%BE%B0%E7%85%A7%E8%80%80%E4%BD%A0%E6%88%91%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctf-getshell.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF_Web：8位以内可控字符getshell_星辰照耀你我的博客-CSDN博客_ctf-getshell.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: not detected
- Techniques: classical-crypto, command-injection, encoding-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `6`
- `docs/img/35dabc349b4f74ea79814dc2c37fab5e.png`
- `docs/img/0dfbe269012efdf11e48e1e72717d1fa.png`
- `docs/img/88864b176e78f3268f7c04f6b6a139e0.png`
- `docs/img/d1906730a340293268c6ccbdc1807925.png`
- `docs/img/5f5dc64863a74b1be33e7868e0fb1fbe.png`
- `docs/img/eb6451efda78701c2f893baf6988367f.png`

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

### Step 2: CTF_Web：8位以内可控字符getshell_星辰照耀你我的博客-CSDN博客_ctf getshell

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/qq_35493457/article/details/119385240](https://blog.csdn.net/qq_35493457/article/details/119385240)`

### Step 3: 题目来源

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use the artifact-specific tool to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use the artifact-specific tool to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `35dabc349b4f74ea79814dc2c37fab5e`

### Step 4: 解题利用知识点

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use the artifact-specific tool with the extracted filter/query `echo PD9waHAgZWNobyBzaGVsbF9leGVjKCRfR0VUWzFdKTs=|base64 -d>1.php "使用base64的方式避免$等特殊字符输入失败"` and inspect the matching evidence.
- Filters or commands:
  - `echo PD9waHAgZWNobyBzaGVsbF9leGVjKCRfR0VUWzFdKTs=|base64 -d>1.php "使用base64的方式避免$等特殊字符输入失败"`
  - `>\=\|\\`
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use the artifact-specific tool with the extracted filter/query `echo PD9waHAgZWNobyBzaGVsbF9leGVjKCRfR0VUWzFdKTs=|base64 -d>1.php "使用base64的方式避免$等特殊字符输入失败"` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `88864b176e78f3268f7c04f6b6a139e0`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
