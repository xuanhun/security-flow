# DASCTF-两道web题复现_cr4ke3的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `DASCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/DASCTF-两道web题复现_cr4ke3的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/DASCTF-%E4%B8%A4%E9%81%93web%E9%A2%98%E5%A4%8D%E7%8E%B0_cr4ke3%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/DASCTF-两道web题复现_cr4ke3的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ids, web-app challenges.

## Input Signals

- Artifacts: ids, web-app
- Tools: detect-it-easy, netcat, radare2
- Techniques: command-injection, crypto-analysis, deserialization, format-string, http-analysis, php-tricks, waf-bypass, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `1`
- `docs/img/5bc820a9480f63dd7af93e52bca9e847.png`

## Solve Thinking

### Step 1: Document

- Route type: `detect-it-easy-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: detect-it-easy, netcat, radare2
- Reasoning chain:
  - Recognize the section as detect-it-easy-driven evidence lookup.
  - Use detect-it-easy, netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: DASCTF-两道web题复现_cr4ke3的博客-CSDN博客

- Route type: `deserialization chain`
- Why: Deserialization cases usually reduce to identifying a controllable object graph and one executable magic-method sink.
- Probe: Use detect-it-easy, netcat, radare2 with the extracted filter/query `if($_SESSION['login']!=1){` and inspect the matching evidence.
- Tools: detect-it-easy, netcat, radare2
- Filters or commands:
  - `if($_SESSION['login']!=1){`
- Reasoning chain:
  - Recognize the section as deserialization chain.
  - Use detect-it-easy, netcat, radare2 with the extracted filter/query `if($_SESSION['login']!=1){` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `183.129.189.60:10010`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
