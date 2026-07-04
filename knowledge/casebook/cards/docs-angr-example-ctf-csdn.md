# angr-example(解CTF题目)_「已注销」的博客-CSDN博客

## Case Metadata

- Category: `Training and Meta`
- Platform: `angr`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/angr-example(解CTF题目)_「已注销」的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/angr-example%28%E8%A7%A3CTF%E9%A2%98%E7%9B%AE%29_%E3%80%8C%E5%B7%B2%E6%B3%A8%E9%94%80%E3%80%8D%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/angr-example(解CTF题目)_「已注销」的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Training and Meta reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: angr, ida, netcat, z3
- Techniques: command-injection, dns-analysis, encoding-analysis, integer-overflow, qr-analysis, reverse-engineering, stack-overflow, symbolic-execution

## First-Principles Route

- Treat the document as study guidance: extract challenge taxonomy, workflow rules, tool references, and reusable habits.
- Record platform names, topic tags, and tool examples so later queries can reach the right note quickly.
- Prefer compact summaries that preserve lookup value over full-text duplication.

## Linked Assets

- Referenced assets: `2`
- `docs/img/2b2484af6463ae5e7d446e9182008bb6.png`
- `docs/img/0a5514700c8f4cf31e021e37c5b75ea7.png`

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use angr, ida, netcat, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: angr, ida, netcat, z3
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use angr, ida, netcat, z3 to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: angr-example(解CTF题目)_「已注销」的博客-CSDN博客

- Route type: `integer-overflow bypass`
- Why: Numeric edge cases matter when they alter a length, signedness, allocation, or control-flow boundary.
- Probe: Use angr, ida, netcat, z3 with the extracted filter/query `if ( (&v3)[i % 3][2 * (i / 3)] - *(char *)(i + a1) != 1 )` and inspect the matching evidence.
- Tools: angr, ida, netcat, z3
- Filters or commands:
  - `if ( (&v3)[i % 3][2 * (i / 3)] - *(char *)(i + a1) != 1 )`
  - `found.add_constraints(found.memory.load(flag_addr, 5) == int('ASIS{'.encode('hex'), 16))`
  - `#found.solver.add(found.memory.load(flag_addr, 5) == int('ASIS{'.encode('hex'), 16))`
  - `if ( encrypted[i] != ((unsigned __int8)((unsigned __int8)(a1[i] ^ i) << ((i ^ 9) & 3)) | (unsigned __int8)((signed int)(unsigned __int8)(a1[i] ^ i) >> (8 - ((i ^ 9) & 3))))`
  - `return i == 23;`
  - `(unsigned int)"| Welcome Hero |\n",`
- Reasoning chain:
  - Recognize the section as integer-overflow bypass.
  - Use angr, ida, netcat, z3 with the extracted filter/query `if ( (&v3)[i % 3][2 * (i / 3)] - *(char *)(i + a1) != 1 )` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `2b2484af6463ae5e7d446e9182008bb6`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
