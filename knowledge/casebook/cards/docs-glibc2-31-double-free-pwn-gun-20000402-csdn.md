# glibc2.31下的新double free手法/字节跳动pwn题gun题解_一只狗20000402的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `glibc2.31下的新double free手法/字节跳动pwn题gun题解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/glibc2.31下的新double-free手法／字节跳动pwn题gun题解_一只狗20000402的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/glibc2.31%E4%B8%8B%E7%9A%84%E6%96%B0double-free%E6%89%8B%E6%B3%95%EF%BC%8F%E5%AD%97%E8%8A%82%E8%B7%B3%E5%8A%A8pwn%E9%A2%98gun%E9%A2%98%E8%A7%A3_%E4%B8%80%E5%8F%AA%E7%8B%9720000402%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/glibc2.31下的新double-free手法／字节跳动pwn题gun题解_一只狗20000402的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, pwntools
- Techniques: binary-exploitation, command-injection, crypto-analysis, encoding-analysis, waf-bypass

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `11`
- `docs/img/33bca38bdddfa97578a22641d60caa79.png`
- `docs/img/129f582ce35087b9755d2f51d040006b.png`
- `docs/img/81878e5444a3a45c450acbac43b1778b.png`
- `docs/img/de9a5eef57802c0a46f1d98f2415b7b3.png`
- `docs/img/e1ac72bb22debfa54df71f47cc861914.png`
- `docs/img/e0b8eaa4127046721027c06db500725b.png`
- `docs/img/9179b8d9f6024feed6a342fb62de649c.png`
- `docs/img/0384bbd19df03f6d9087361523ac5918.png`
- `docs/img/d3f2b0e9f923544c89156ad545279c39.png`
- `docs/img/fdf0935bfdf38370698f49b91cfe2bf6.png`
- `docs/img/82eb799c3c9c70f573852588d7caae24.png`

## Solve Thinking

### Step 1: Document

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: glibc2.31下的新double free手法/字节跳动pwn题gun题解_一只狗20000402的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/chennbnbnb/article/details/109284780](https://blog.csdn.net/chennbnbnb/article/details/109284780)`

### Step 3: 回顾double free手法

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use gdb, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use gdb, pwntools to isolate the blocked token, then vary encoding, transport, syntax, or indirection until the primitive survives filtering.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `* glibc2.29～glibc2.31，tcache加入了检查机制，如何进行doubel free就是本文的核心`

### Step 4: Tcache的设计目的

- Route type: `tls handshake inspection`
- Why: TLS questions usually require filtering the specific handshake and reading the requested field directly.
- Probe: Use gdb, pwntools to filter the relevant TLS handshake and inspect session, random, key, or certificate fields.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as tls handshake inspection.
  - Use gdb, pwntools to filter the relevant TLS handshake and inspect session, random, key, or certificate fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `因此tcache指针实际上位于TLS区域内，是各个线程独有的`

### Step 5: glibc2.31下的Tcache检查

- Route type: `waf bypass`
- Why: WAF cases are best solved by isolating one blocked token at a time and preserving a working bypass pattern.
- Probe: Use gdb, pwntools with the extracted filter/query `if (tcache != NULL && tc_idx < mp_.tcache_bins)` and inspect the matching evidence.
- Tools: gdb, pwntools
- Filters or commands:
  - `if (tcache != NULL && tc_idx < mp_.tcache_bins)`
  - `if (__glibc_unlikely(e->key == tcache))//剪枝`
  - `if (tmp == e)`
- Reasoning chain:
  - Recognize the section as waf bypass.
  - Use gdb, pwntools with the extracted filter/query `if (tcache != NULL && tc_idx < mp_.tcache_bins)` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这些检查导致我们不能free任何一个已经在tcache中的chunk，绕过的方法有两个：`

### Step 6: Tcache的Stash机制

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, pwntools with the extracted filter/query `if (victim != NULL) //如果有chunk` and inspect the matching evidence.
- Tools: gdb, pwntools
- Filters or commands:
  - `if (victim != NULL) //如果有chunk`
  - `if (__glibc_likely(victim != NULL))`
  - `if (__builtin_expect(victim_idx != idx, 0)) //对fastbin的size检查`
  - `while (tcache->counts[tc_idx] < mp_.tcache_count && (tc_victim = *fb) != NULL) //只要tcache没空，并且fastbin还有chunk`
  - `if (__glibc_unlikely(tc_victim == NULL))`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, pwntools with the extracted filter/query `if (victim != NULL) //如果有chunk` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `}`

### Step 7: 当fastbin double free遇上Tcache Stash

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `33bca38bdddfa97578a22641d60caa79`

### Step 8: 保护

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `81878e5444a3a45c450acbac43b1778b`

### Step 9: 程序分析

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `e1ac72bb22debfa54df71f47cc861914`

### Step 10: 漏洞

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, pwntools with the extracted filter/query `在最后发射时，是否进行free却依赖next!=null这个条件` and inspect the matching evidence.
- Tools: gdb, pwntools
- Filters or commands:
  - `在最后发射时，是否进行free却依赖next!=null这个条件`
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, pwntools with the extracted filter/query `在最后发射时，是否进行free却依赖next!=null这个条件` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0384bbd19df03f6d9087361523ac5918`

### Step 11: 思路

- Route type: `gdb-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: gdb, pwntools
- Reasoning chain:
  - Recognize the section as gdb-driven evidence lookup.
  - Use gdb, pwntools to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `}`

### Step 12: EXP

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use gdb, pwntools with the extracted filter/query `gdb.attach(sh, 'break *'+hex(proc_base + 0x1A84))` and inspect the matching evidence.
- Tools: gdb, pwntools
- Filters or commands:
  - `gdb.attach(sh, 'break *'+hex(proc_base + 0x1A84))`
  - `gdb.attach(sh, 'telescope '+hex(proc_base+0x4050) + ' 44')`
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use gdb, pwntools with the extracted filter/query `gdb.attach(sh, 'break *'+hex(proc_base + 0x1A84))` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `123.56.96.75`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
