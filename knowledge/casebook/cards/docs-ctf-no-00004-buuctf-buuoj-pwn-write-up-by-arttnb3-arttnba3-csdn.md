# 【CTF题解NO.00004】BUUCTF/BUUOJ - Pwn write up by arttnb3_arttnba3的博客-CSDN博客

## Case Metadata

- Category: `Pwn`
- Platform: `【CTF题解NO.00004】BUUCTF/BUUOJ`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/【CTF题解NO.00004】BUUCTF／BUUOJ---Pwn-write-up-by-arttnb3_arttnba3的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E3%80%90CTF%E9%A2%98%E8%A7%A3NO.00004%E3%80%91BUUCTF%EF%BC%8FBUUOJ---Pwn-write-up-by-arttnb3_arttnba3%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/【CTF题解NO.00004】BUUCTF／BUUOJ---Pwn-write-up-by-arttnb3_arttnba3的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Pwn reference for binary, ciphertext challenges.

## Input Signals

- Artifacts: binary, ciphertext
- Tools: checksec, gdb, ida, netcat, one-gadget, pwntools, radare2
- Techniques: binary-exploitation, classical-crypto, command-injection, crypto-analysis, encoding-analysis, format-string, integer-overflow, ret2libc, ret2text, reverse-engineering, service-enumeration, stack-overflow, waf-bypass, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `200`
- `docs/img/d00ecf061574f9f2af5e445e73dec2c1.png`
- `docs/img/ada865eb0c380510cd03ab3096d73182.png`
- `docs/img/80662b783a1e3356c8c8baed98ae7e3e.png`
- `docs/img/d99f8eddf8d60e84de91496e942785a5.png`
- `docs/img/8464a8afea896fa0e56459952742f7ce.png`
- `docs/img/80f8a8a2e876c842b171fe554c1015dd.png`
- `docs/img/ad56fb09e1d3a99203ac00b9f99baabf.png`
- `docs/img/ecd75dfa97f63cf1ac9aa91b6e451a36.png`
- `docs/img/3ec678e37fcbc474cab0d1554e864b3d.png`
- `docs/img/b78d12dc531c52b2dd7d21b066602125.png`
- `docs/img/35ed89b7a787bb8f04db09b2914fc9c0.png`
- `docs/img/02c5b8fee3e62609072559159107317e.png`
- ... and `188` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, gdb, ida, netcat, one-gadget
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, gdb, ida, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 【CTF题解NO.00004】BUUCTF/BUUOJ - Pwn write up by arttnb3_arttnba3的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, ida, netcat, one-gadget
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/arttnba3/article/details/109848247](https://blog.csdn.net/arttnba3/article/details/109848247)`

### Step 3: 0x000.绪论

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, gdb, ida, netcat, one-gadget
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, gdb, ida, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 注2：老生常谈，CSDN阅读体验稀烂，建议来[这里](https://arttnba3.cn/2020/09/08/CTF-0X00-BUUOJ-PWN/)看`

### Step 4: 0x001.test your nc - nc

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use ida, netcat with the extracted filter/query `nc，成功getshell，得flag` and inspect the matching evidence.
- Tools: ida, netcat
- Filters or commands:
  - `nc，成功getshell，得flag`
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use ida, netcat with the extracted filter/query `nc，成功getshell，得flag` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `d00ecf061574f9f2af5e445e73dec2c1`

### Step 5: 0x002.rip - ret2text

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use checksec, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: checksec, pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use checksec, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `80662b783a1e3356c8c8baed98ae7e3e`

### Step 6: 0x003.warmup_csaw_2016 - ret2text

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use checksec, ida, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: checksec, ida, pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use checksec, ida, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `ad56fb09e1d3a99203ac00b9f99baabf`

### Step 7: 0x004.pwn1_sctf_2016 - ret2text

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, ida, pwntools with the extracted filter/query `while ( std::string::find(a2, a3, 0) != -1 ) // 在input中寻找字符串v9（"I"），如果找不到则find方法会返回-1，跳出循环` and inspect the matching evidence.
- Tools: checksec, ida, pwntools
- Filters or commands:
  - `while ( std::string::find(a2, a3, 0) != -1 ) // 在input中寻找字符串v9（"I"），如果找不到则find方法会返回-1，跳出循环`
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, ida, pwntools with the extracted filter/query `while ( std::string::find(a2, a3, 0) != -1 ) // 在input中寻找字符串v9（"I"），如果找不到则find方法会返回-1，跳出循环` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `35ed89b7a787bb8f04db09b2914fc9c0`

### Step 8: 0x005.ciscn_2019_n_1 - overwrite

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `a85d17fd86428d5ba3e3c73d0e725bc6`

### Step 9: 0x006.ciscn_2019_c_1 - ret2csu + ret2libc

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use checksec, ida, netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use checksec, ida, netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `8ff800828c8dd7dd8df8f59bd68c6e2c`

### Step 10: 0x007.[OGeek2019]babyrop - ret2libc

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use checksec, ida, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: checksec, ida, pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use checksec, ida, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `6b73585a1120b035001039583fb42a66`

### Step 11: 0x008.jarvisoj_level0 - ret2text

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use checksec, ida, netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use checksec, ida, netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0a0f31ca0cf4aaac2b01bf845686fa28`

### Step 12: 0x009.ciscn_2019_en_2 - ret2csu + ret2libc

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use checksec, ida, netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use checksec, ida, netcat, pwntools to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `7e4909085a27c33794f97349467dcae2`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
