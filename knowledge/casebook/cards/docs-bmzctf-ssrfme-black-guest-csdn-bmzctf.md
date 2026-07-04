# BMZCTF SSRFME 详解_black guest丶的博客-CSDN博客_bmzctf

## Case Metadata

- Category: `Web`
- Platform: `BMZCTF SSRFME 详解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BMZCTF-SSRFME-详解_black-guest丶的博客-CSDN博客_bmzctf.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BMZCTF-SSRFME-%E8%AF%A6%E8%A7%A3_black-guest%E4%B8%B6%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_bmzctf.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BMZCTF-SSRFME-详解_black-guest丶的博客-CSDN博客_bmzctf.md`

## Why This Case Matters

Use this case as a Web reference for web-app challenges.

## Input Signals

- Artifacts: web-app
- Tools: netcat
- Techniques: command-injection, crypto-analysis, encoding-analysis, file-inclusion, file-upload, http-analysis, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `6`
- `docs/img/d11aa61fdcc9de52cee32af3b354dfff.png`
- `docs/img/7861e81df07b24e883fd2c66ff55bc7f.png`
- `docs/img/8f51c70ba31871c3662c1c7869df3c02.png`
- `docs/img/77165b7b41d628ce10d53a0470f56360.png`
- `docs/img/368bfed4ed9495a2eb135919e875fd18.png`
- `docs/img/d82a9296c043606e69158ad1d9320782.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BMZCTF SSRFME 详解_black guest丶的博客-CSDN博客_bmzctf

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/u013797594/article/details/118463622](https://blog.csdn.net/u013797594/article/details/118463622)`

### Step 3: 题目：

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `127.0.0.1`

### Step 4: 文件包含漏洞

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `127.0.0.1`

### Step 5: 通过http方式包含的文件可传入参数

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use netcat to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `127.0.0.1`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
