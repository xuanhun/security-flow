# 由一道CTF pwn题深入理解libc2.26中的tcache机制_weixin_30363981的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `由一道CTF pwn题深入理解libc2.26中的tcache机制`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/由一道CTF-pwn题深入理解libc2.26中的tcache机制_weixin_30363981的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E7%94%B1%E4%B8%80%E9%81%93CTF-pwn%E9%A2%98%E6%B7%B1%E5%85%A5%E7%90%86%E8%A7%A3libc2.26%E4%B8%AD%E7%9A%84tcache%E6%9C%BA%E5%88%B6_weixin_30363981%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/由一道CTF-pwn题深入理解libc2.26中的tcache机制_weixin_30363981的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, web-app challenges.

## Input Signals

- Artifacts: binary, web-app
- Tools: netcat
- Techniques: binary-exploitation, http-analysis, ret2libc, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 由一道CTF pwn题深入理解libc2.26中的tcache机制_weixin_30363981的博客-CSDN博客

- Route type: `credential discovery`
- Why: When a capture or logs mention a cleartext protocol, check credentials and followed streams before expensive analysis.
- Probe: Use netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as credential discovery.
  - Use netcat to inspect credentials, authentication fields, or followed streams before deeper analysis.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `在刚结束的HITB-XCTF有一道pwn题gundam使用了2.26版本的libc.因为2.26版本中加入了一些新的机制，自己一开始没有找到利用方式，后来经大佬提醒，才明白2.26版本中新加了一种名叫tcache(thread local caching)的缓存机制。`

### Step 3: Tcache介绍

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `#if USE_TCACHE`

### Step 4: define MAX_TCACHE_SIZE    tidx2usize (TCACHE_MAX_BINS-1)

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `/* Only used to pre-fill the tunables. */`

### Step 5: define tidx2usize(idx)    (((size_t) idx) * MALLOC_ALIGNMENT + MINSIZE - SIZE_SZ)

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `/* When "x" is from chunksize(). */`

### Step 6: define csize2tidx(x) (((x) - MINSIZE + MALLOC_ALIGNMENT - 1) / MALLOC_ALIGNMENT)

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `/* When "x" is a user-provided size. */`

### Step 7: define usize2tidx(x) csize2tidx (request2size (x))

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat to collect the smallest evidence slice that answers the goal.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `etc. */`

### Step 8: define TCACHE_FILL_COUNT 7

- Route type: `timeline reconstruction`
- Why: Timeline questions should be answered from normalized artifact timestamps with timezone assumptions recorded.
- Probe: Use netcat to align timestamps and identify the event that satisfies the question.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as timeline reconstruction.
  - Use netcat to align timestamps and identify the event that satisfies the question.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `static __thread tcache_perthread_struct *tcache = NULL;`

### Step 9: chunk进入tcache的情形

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use netcat with the extracted filter/query `if (victim != 0)` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `if (victim != 0)`
  - `if (__builtin_expect (fastbin_index (chunksize (victim)) != idx, 0))`
  - `&& (pp = *fb) != NULL)`
  - `if (tc_victim != 0)`
  - `if (size == nb)`
  - `if (av != &main_arena)`
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use netcat with the extracted filter/query `if (victim != 0)` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `}`

### Step 10: 从tcache获取chunk的情形

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use netcat with the extracted filter/query `&& tcache->entries[tc_idx] != NULL)` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `&& tcache->entries[tc_idx] != NULL)`
  - `while ((victim = unsorted_chunks (av)->bk) != unsorted_chunks (av))`
- Reasoning chain:
  - Recognize the section as memory artifact analysis.
  - Use netcat with the extracted filter/query `&& tcache->entries[tc_idx] != NULL)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `}`

### Step 11: 对旧的利用技术的影响

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat with the extracted filter/query `在unsorted bin的unlink中，它回到了最原始的unlink，未进行其他检查(如bck->fd != victim)，这样又可以进行DWORD SHOOT啦：` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `在unsorted bin的unlink中，它回到了最原始的unlink，未进行其他检查(如bck->fd != victim)，这样又可以进行DWORD SHOOT啦：`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat with the extracted filter/query `在unsorted bin的unlink中，它回到了最原始的unlink，未进行其他检查(如bck->fd != victim)，这样又可以进行DWORD SHOOT啦：` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `tcache原理及利用凡是介绍完毕，下面我们就gundam一题进行实用tcache漏洞利用`

### Step 12: gundam题解

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `完整脚本[在此](https://github.com/moonAgirl/CTF/tree/master/2018/Hitbxctf/gundam)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
