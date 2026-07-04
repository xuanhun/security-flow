# PWN cmd2 [pwnable.kr]CTF writeup题解系列12_3riC5r的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `PWN cmd2 [pwnable.kr]CTF writeup题解系列12`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/PWN-cmd2-[pwnable.kr]CTF-writeup题解系列12_3riC5r的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/PWN-cmd2-%5Bpwnable.kr%5DCTF-writeup%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9712_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/PWN-cmd2-[pwnable.kr]CTF-writeup题解系列12_3riC5r的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: gdb, netcat
- Techniques: binary-exploitation, command-injection, file-inclusion, ret2libc, service-enumeration, waf-bypass

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Linked Assets

- Referenced assets: `2`
- `docs/img/b692abf2cd5804b530616923fc2e8069.png`
- `docs/img/5666397b70d8969f3be7ada8ac83b779.png`

## Solve Thinking

### Step 1: Document

- Route type: `gdb-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, netcat to collect the smallest evidence slice that answers the goal.
- Tools: gdb, netcat
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: PWN cmd2 [pwnable.kr]CTF writeup题解系列12_3riC5r的博客-CSDN博客

- Route type: `file inclusion exploitation`
- Why: Inclusion cases usually start with path control and end with wrapper, traversal, or source disclosure pivots.
- Probe: Use gdb, netcat with the extracted filter/query `r += strstr(cmd, "=")!=0;` and inspect the matching evidence.
- Tools: gdb, netcat
- Filters or commands:
  - `r += strstr(cmd, "=")!=0;`
  - `r += strstr(cmd, "PATH")!=0;`
  - `r += strstr(cmd, "export")!=0;`
  - `r += strstr(cmd, "/")!=0;`
  - `r += strstr(cmd, "`")!=0;`
  - `r += strstr(cmd, "flag")!=0;`
- Reasoning chain:
  - Recognize the section as file inclusion exploitation.
  - Use gdb, netcat with the extracted filter/query `r += strstr(cmd, "=")!=0;` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `120.84.12.64`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
