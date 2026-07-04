# ctf show-web入门 SSTI篇部分题解_z.volcano的博客-CSDN博客_ctfshow web入门ssti

## Case Metadata

- Category: `Web`
- Platform: `ctf show`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/ctf-show-web入门-SSTI篇部分题解_z.volcano的博客-CSDN博客_ctfshow-web入门ssti.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/ctf-show-web%E5%85%A5%E9%97%A8-SSTI%E7%AF%87%E9%83%A8%E5%88%86%E9%A2%98%E8%A7%A3_z.volcano%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_ctfshow-web%E5%85%A5%E9%97%A8ssti.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/ctf-show-web入门-SSTI篇部分题解_z.volcano的博客-CSDN博客_ctfshow-web入门ssti.md`

## Why This Case Matters

Use this case as a Web reference for web-app, web-service challenges.

## Input Signals

- Artifacts: web-app, web-service
- Tools: burp
- Techniques: command-injection, ssti, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `5`
- `docs/img/3c307c0cd65b12b9a51bbe1ee691e8c8.png`
- `docs/img/6e28f61514feebfba33930462a7bef35.png`
- `docs/img/41a44907562af26816cb75872c7a3588.png`
- `docs/img/0360b045d3a094463a9663f3affb4790.png`
- `docs/img/936f06a49b3c11844f5ec3f11d752b16.png`

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp to collect the smallest evidence slice that answers the goal.
- Tools: burp
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: ctf show-web入门 SSTI篇部分题解_z.volcano的博客-CSDN博客_ctfshow web入门ssti

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use burp to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: burp
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use burp to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_45696568/article/details/113625650](https://blog.csdn.net/weixin_45696568/article/details/113625650)`

### Step 3: SSTI

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use burp to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: burp
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use burp to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ssti模板注入基本原理推荐看[这篇文章](https://xz.aliyun.com/t/3679)，这个师傅写的很详细，小白也很容易看懂。`

### Step 4: web361

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `3c307c0cd65b12b9a51bbe1ee691e8c8`

### Step 5: web362

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这题说开始过滤了，但是不知道过滤了什么，而且用web361的payload就可以直接过。。。`

### Step 6: web363

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `过滤了`引号``

### Step 7: request.args传参绕过

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: burp
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: ``?name={{ config.__class__.__init__.__globals__[request.args.a].popen(request.args.b).read() }}&a=os&b=cat ../flag``

### Step 8: web364

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: burp
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - The proof is the blocked primitive working through the filter path, not just a payload variation that reflects.
- Evidence rule: The proof is the blocked primitive working through the filter path, not just a payload variation that reflects.

### Step 9: chr()绕过

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: burp
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `41a44907562af26816cb75872c7a3588`

### Step 10: web365

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: burp
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use burp to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `比上题又多过滤了一个`中括号``

### Step 11: 中括号绕过

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use burp to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: burp
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use burp to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `最终payload:`

### Step 12: web366

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use burp to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
- Tools: burp
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use burp to validate template evaluation with the smallest safe expression, then extend toward controlled object traversal or file read.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `多过滤了一个`_`,这里参考的羽师傅的[SSTI模板注入绕过（进阶篇）](https://blog.csdn.net/miuzzx/article/details/110220425)，不得不说，师傅们姿势是真的多。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
