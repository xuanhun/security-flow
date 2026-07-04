# buuctf pwn刷题（1）_qingmu-z的博客-CSDN博客_buuctf pwn1

## Case Metadata

- Category: `Pwn`
- Platform: `buuctf pwn刷题（1）`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/buuctf-pwn刷题（1）_qingmu-z的博客-CSDN博客_buuctf-pwn1.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/buuctf-pwn%E5%88%B7%E9%A2%98%EF%BC%881%EF%BC%89_qingmu-z%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_buuctf-pwn1.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/buuctf-pwn刷题（1）_qingmu-z的博客-CSDN博客_buuctf-pwn1.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: checksec, ida, netcat, pwntools
- Techniques: binary-exploitation, command-injection, ret2libc, reverse-engineering, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `26`
- `docs/img/4907286b1798c169e99bec0f9279bc07.png`
- `docs/img/7669aca6c9aa65870079c26680837bce.png`
- `docs/img/ee150a2bbf1c3887999af7f4683d0a9f.png`
- `docs/img/5dad186efaa07c121fc41212d67e682d.png`
- `docs/img/880c73bb3064dbb7d6355ea0d41832ce.png`
- `docs/img/0aac7b1b4f41866c0a598e5a3b1e941d.png`
- `docs/img/24e7ed2b078c9cd82283cf7e6ed58a31.png`
- `docs/img/c9b19a53fd54baa9a5c776dd42f8eaab.png`
- `docs/img/628cdb3818d39edf8b92c8430b9d091d.png`
- `docs/img/dce8560b55fff28295aa73ad2442dd88.png`
- `docs/img/1db781aeaaa74b78a60018b552dbeba1.png`
- `docs/img/f89ba3be88238813221859e7cbdcea1a.png`
- ... and `14` more

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use checksec, ida, netcat, pwntools to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: buuctf pwn刷题（1）_qingmu-z的博客-CSDN博客_buuctf pwn1

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use checksec, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use checksec, ida, netcat, pwntools to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_42689613/article/details/113432007](https://blog.csdn.net/weixin_42689613/article/details/113432007)`

### Step 3: test_your_nc

- Route type: `command execution path`
- Why: Command execution routes should separate syntax proof, filter bypass, and final file-read or shell step.
- Probe: Use ida, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
- Tools: ida, netcat
- Reasoning chain:
  - Recognize the section as command execution path.
  - Use ida, netcat to verify command execution or shell expansion with a tiny proof command before reading the target file.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `4907286b1798c169e99bec0f9279bc07`

### Step 4: pwn1

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: ida, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0aac7b1b4f41866c0a598e5a3b1e941d`

### Step 5: warmup_csaw_2016

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, ida, pwntools with the extracted filter/query `checksec` and inspect the matching evidence.
- Tools: checksec, ida, pwntools
- Filters or commands:
  - `checksec`
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, ida, pwntools with the extracted filter/query `checksec` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `f89ba3be88238813221859e7cbdcea1a`

### Step 6: pwn1_sctf_2016

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, ida, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `c6f5f61b56d017e7ad796eb4d7d85543`

### Step 7: ciscn_2019_n_1

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, ida, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, ida, netcat, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, ida, netcat, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `7447a265885746be382e075e71a3bb7c`

### Step 8: level0

- Route type: `stack control exploitation`
- Why: Binary exploitation cases should lock offsets, mitigations, and the shortest win path before gadget collecting spirals.
- Probe: Use checksec, ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
- Tools: checksec, ida, pwntools
- Reasoning chain:
  - Recognize the section as stack control exploitation.
  - Use checksec, ida, pwntools to confirm the overwrite boundary, control target, and calling path before sending the final payload.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `0817ef0ec1ffcfea5f032c27f945db7a`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
