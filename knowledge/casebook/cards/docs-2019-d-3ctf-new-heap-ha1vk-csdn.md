# 2019 D^3CTF new_heap详细题解_ha1vk的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `2019 D^3CTF new`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/2019-D^3CTF-new_heap详细题解_ha1vk的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/2019-D%5E3CTF-new_heap%E8%AF%A6%E7%BB%86%E9%A2%98%E8%A7%A3_ha1vk%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/2019-D^3CTF-new_heap详细题解_ha1vk的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: gdb, ida
- Techniques: binary-exploitation, encoding-analysis, ret2libc, reverse-engineering, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `19`
- `docs/img/18b62b68c4f9bd710cd858b6a1222255.png`
- `docs/img/74fcdd9ab9f4931473a861e49e073891.png`
- `docs/img/a9e308fb1518953a2a3f78bd4fddf3c3.png`
- `docs/img/1e5aeaae1d1586db8c6be59bd46c7c7b.png`
- `docs/img/826e8b60b90a3b51c7ee830185800e1b.png`
- `docs/img/4948ec84c563bc28544882ffcbf25443.png`
- `docs/img/34a1399aef2f347576c82576a2143912.png`
- `docs/img/5cfda784620c9b1193d1fc5469535730.png`
- `docs/img/4ed4fd44d9d51588c411877e91167da8.png`
- `docs/img/1c8bd396271ef8b269f7045a4f66fcff.png`
- `docs/img/c675dc2e5d96efd3aa8aa6cfd8b71276.png`
- `docs/img/37518532a5e0c97f1c55cbea6b5cd8b4.png`
- ... and `7` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: gdb, ida
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 2019 D^3CTF new_heap详细题解_ha1vk的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use gdb, ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: gdb, ida
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use gdb, ida to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/seaaseesa/article/details/103302721](https://blog.csdn.net/seaaseesa/article/details/103302721)`

### Step 3: new_heap(高质量题)

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use gdb, ida with the extracted filter/query `7. **if** ((_IO_vtable_offset (_IO_stdout) != 0` and inspect the matching evidence.
- Tools: gdb, ida
- Filters or commands:
  - `7. **if** ((_IO_vtable_offset (_IO_stdout) != 0`
  - `8. || _IO_fwide (_IO_stdout, -1) == -1)`
  - `9. && _IO_sputn (_IO_stdout, str, len) == len`
  - `10. && _IO_putc_unlocked ('\n', _IO_stdout) != EOF)`
  - `6. f->_flags |= _IO_ERR_SEEN;`
  - `11. **if** ((f->_flags & _IO_CURRENTLY_PUTTING) == 0 || f->_IO_write_base == NULL)`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use gdb, ida with the extracted filter/query `7. **if** ((_IO_vtable_offset (_IO_stdout) != 0` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `18b62b68c4f9bd710cd858b6a1222255`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
