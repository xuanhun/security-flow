# JIS-CTF : VulnUpload 题解_weixin_33676492的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `JIS`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/JIS-CTF-：-VulnUpload-题解_weixin_33676492的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/JIS-CTF-%EF%BC%9A-VulnUpload-%E9%A2%98%E8%A7%A3_weixin_33676492%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/JIS-CTF-：-VulnUpload-题解_weixin_33676492的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app, web-service challenges.

## Input Signals

- Artifacts: web-app, web-service
- Tools: nmap
- Techniques: file-upload, http-analysis, service-enumeration, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: Document

- Route type: `nmap-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use nmap to collect the smallest evidence slice that answers the goal.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as nmap-driven evidence lookup.
  - Use nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: JIS-CTF : VulnUpload 题解_weixin_33676492的博客-CSDN博客

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use nmap to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use nmap to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_33676492/article/details/91709905](https://blog.csdn.net/weixin_33676492/article/details/91709905)`

### Step 3: 思路

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `3\. 留意文件中隐藏的内容`

### Step 4: Flag 1

- Route type: `nmap-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use nmap to collect the smallest evidence slice that answers the goal.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as nmap-driven evidence lookup.
  - Use nmap to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `The 1st flag is : {8734509128730458630012095}`

### Step 5: Flag 2

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `The 2nd flag is : {7412574125871236547895214}`

### Step 6: Flag 3

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a hidden file ;)`

### Step 7: Flag 4

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use nmap to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `username : technawi`

### Step 8: Flag 5

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use nmap to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use nmap to confirm extension, content-type, parser, and reachable upload path controls before escalating to code execution.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `转载于:https://blog.51cto.com/executer/2091159`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
