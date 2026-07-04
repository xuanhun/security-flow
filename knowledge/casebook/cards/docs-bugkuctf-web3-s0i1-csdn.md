# BugkuCTF: web3 ； 域名解析_s0i1的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `BugkuCTF: web3 ； 域名解析`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/BugkuCTF：-web3-；-域名解析_s0i1的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/BugkuCTF%EF%BC%9A-web3-%EF%BC%9B-%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90_s0i1%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/BugkuCTF：-web3-；-域名解析_s0i1的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app, web-service challenges.

## Input Signals

- Artifacts: web-app, web-service
- Tools: burp, radare2
- Techniques: crypto-analysis, dns-analysis, file-upload, http-analysis, service-enumeration, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `2`
- `docs/img/921a4214fcd1f8fb6975a0b217731fbc.png`
- `docs/img/a3fa146f77e816b15d3c1566f7bfad89.png`

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: burp, radare2
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: BugkuCTF: web3 ； 域名解析_s0i1的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp, radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp, radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/changer_WE/article/details/85090023](https://blog.csdn.net/changer_WE/article/details/85090023)`

### Step 3: web3

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: radare2
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use radare2 to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `921a4214fcd1f8fb6975a0b217731fbc`

### Step 4: 域名解析

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use burp to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: burp
- Reasoning chain:
  - Recognize the section as dns pivot.
  - Use burp to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.206.87.240`

### Step 5: 补充

- Route type: `file upload bypass`
- Why: Upload cases are about parser differences, path reachability, and filter mismatches more than the upload itself.
- Probe: Use burp, radare2 with the extracted filter/query `curl [option] [url]` and inspect the matching evidence.
- Tools: burp, radare2
- Filters or commands:
  - `curl [option] [url]`
  - `curl -I "XXX" -H "host: 域名" -v`
- Reasoning chain:
  - Recognize the section as file upload bypass.
  - Use burp, radare2 with the extracted filter/query `curl [option] [url]` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `它与不指定host有时访问的并不是同一个ip，同一个url根据不同的Host将同一个请求定向到不同主机（host），从而达到负载均衡的效果。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
