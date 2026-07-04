# buuoj部分web题解_Lionel_kai的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `buuoj部分web题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/buuoj部分web题解_Lionel_kai的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/buuoj%E9%83%A8%E5%88%86web%E9%A2%98%E8%A7%A3_Lionel_kai%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/buuoj部分web题解_Lionel_kai的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat, radare2
- Techniques: classical-crypto, command-injection, dns-analysis, encoding-analysis, file-inclusion, http-analysis, image-analysis, sql-injection, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `34`
- `docs/img/c662ab7d897e2a8b21fcc0ec4015d70e.png`
- `docs/img/faad0ff405664ef65bf9b9c560775042.png`
- `docs/img/ba1c3ab3696dcb3587ac61ab81766ad2.png`
- `docs/img/43713449828d9bcb39076f41d45ca1c2.png`
- `docs/img/cec82fbed9b53e952c3a9f2e82c6a8ce.png`
- `docs/img/05a6968aac6efb71f221efc3a7312afe.png`
- `docs/img/664e56ff391ce8e01e3df24b5f72eacb.png`
- `docs/img/561abe75672468024eb484da0931aaf0.png`
- `docs/img/3a9d4abf336e3204dbe0929a39b7dbd6.png`
- `docs/img/452e85a6a5847860d0a8fea2cae35fb6.png`
- `docs/img/6711175fc666ca54fccf10cde29e04f6.png`
- `docs/img/334287623c3fd5ed2e1fd3ed102673f5.png`
- ... and `22` more

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

### Step 2: buuoj部分web题解_Lionel_kai的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/Lionel_kai/article/details/119724091](https://blog.csdn.net/Lionel_kai/article/details/119724091)`

### Step 3: [HCTF 2018]WarmUp

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use radare2 to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use radare2 to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c662ab7d897e2a8b21fcc0ec4015d70e`

### Step 4: [极客大挑战 2019]EasySQL

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `664e56ff391ce8e01e3df24b5f72eacb`

### Step 5: ![](img/3a9d4abf336e3204dbe0929a39b7dbd6.png)

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `452e85a6a5847860d0a8fea2cae35fb6`

### Step 6: [强网杯 2019]随便注

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `334287623c3fd5ed2e1fd3ed102673f5`

### Step 7: [ACTF2020 新生赛]Include

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8665063083e657ed8366b84ef34031cc`

### Step 8: [SUCTF 2019]EasySQL

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use netcat, radare2 to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use netcat, radare2 to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - The proof is the returned command output or filesystem effect from the injected command.
- Evidence rule: The proof is the returned command output or filesystem effect from the injected command.

### Step 9: [极客大挑战 2019]Secret File

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use netcat to verify controllable include/read paths and then test the shortest local or wrapper-based read primitive.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7afc6ff5bdb5eedd7bff66ff74072e04`

### Step 10: [GYCTF2020]Blacklist

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use netcat, radare2 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use netcat, radare2 to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `69417cd477bec2a5e9d18ab555678d69`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
