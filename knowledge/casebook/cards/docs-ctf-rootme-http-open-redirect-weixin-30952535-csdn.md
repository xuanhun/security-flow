# CTF-rootme 题解之HTTP - Open redirect_weixin_30952535的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF-rootme-题解之HTTP---Open-redirect_weixin_30952535的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF-rootme-%E9%A2%98%E8%A7%A3%E4%B9%8BHTTP---Open-redirect_weixin_30952535%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF-rootme-题解之HTTP---Open-redirect_weixin_30952535的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for web-app, web-service challenges.

## Input Signals

- Artifacts: web-app, web-service
- Tools: burp, netcat
- Techniques: binary-exploitation, command-injection, http-analysis, php-tricks, ssti, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: Document

- Route type: `burp-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use burp, netcat to collect the smallest evidence slice that answers the goal.
- Tools: burp, netcat
- Reasoning chain:
  - Recognize the section as burp-driven evidence lookup.
  - Use burp, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF-rootme 题解之HTTP - Open redirect_weixin_30952535的博客-CSDN博客

- Route type: `ssti exploitation`
- Why: SSTI cases should prove evaluation first, then turn blacklist details into object-traversal or file-read pivots.
- Probe: Use burp, netcat with the extracted filter/query `|__| |__| [__ |__| |__] | | [__ | |___ |__/` and inspect the matching evidence.
- Tools: burp, netcat
- Filters or commands:
  - `|__| |__| [__ |__| |__] | | [__ | |___ |__/`
  - `| | | | ___] | | |__] |__| ___] | |___ | \ v3.0`
  - `[ BlackArch burpsuite ]# echo -n 'https://baidu.com'|md5sum|awk '{print $1}'`
- Reasoning chain:
  - Recognize the section as ssti exploitation.
  - Use burp, netcat with the extracted filter/query `|__| |__| [__ |__| |__] | | [__ | |___ |__/` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a023cfbf5f1c39bdf8407f28b60cd134`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
