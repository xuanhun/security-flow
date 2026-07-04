# BUUCTF__[BUUCTF 2018]Online Tool_题解_风过江南乱的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BUUCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BUUCTF__[BUUCTF-2018]Online-Tool_题解_风过江南乱的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BUUCTF__%5BBUUCTF-2018%5DOnline-Tool_%E9%A2%98%E8%A7%A3_%E9%A3%8E%E8%BF%87%E6%B1%9F%E5%8D%97%E4%B9%B1%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BUUCTF__[BUUCTF-2018]Online-Tool_题解_风过江南乱的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app, web-service challenges.

## Input Signals

- Artifacts: web-app, web-service
- Tools: nmap
- Techniques: command-injection, http-analysis, php-tricks, ret2libc, service-enumeration, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `4`
- `docs/img/14e0b5ab86ea875ae1215937337a5e98.png`
- `docs/img/2208186f9fa3f876ee27a98ffb979956.png`
- `docs/img/a2a927717a01d85c18fa5f673fc2da7c.png`
- `docs/img/cf19b846849652bce1b684401394baec.png`

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

### Step 2: BUUCTF__[BUUCTF 2018]Online Tool_题解_风过江南乱的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/tm_1024/article/details/107393796](https://blog.csdn.net/tm_1024/article/details/107393796)`

### Step 3: 前言

- Route type: `nmap-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use nmap to collect the smallest evidence slice that answers the goal.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as nmap-driven evidence lookup.
  - Use nmap to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 太真实了。。。有点迷。`

### Step 4: 研究

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use nmap to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use nmap to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `14e0b5ab86ea875ae1215937337a5e98`

### Step 5: 最后

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: nmap
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use nmap to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* 最后欢迎来访[个人博客](http://ctf-web.zm996.cloud/)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
