# team [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列28（网站配置错误，需自行配置本地环境测试）_3riC5r的博客-CSDN博客_攻防世界创建动态环境失败

## Case Metadata

- Category: `Pwn`
- Platform: `team [XCTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/team-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列28（网站配置错误，需自行配置本地环境测试）_3riC5r的博客-CSDN博客_攻防世界创建动态环境失败.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/team-%5BXCTF-PWN%5D%5B%E9%AB%98%E6%89%8B%E8%BF%9B%E9%98%B6%E5%8C%BA%5DCTF-writeup%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%E9%A2%98%E8%A7%A3%E7%B3%BB%E5%88%9728%EF%BC%88%E7%BD%91%E7%AB%99%E9%85%8D%E7%BD%AE%E9%94%99%E8%AF%AF%EF%BC%8C%E9%9C%80%E8%87%AA%E8%A1%8C%E9%85%8D%E7%BD%AE%E6%9C%AC%E5%9C%B0%E7%8E%AF%E5%A2%83%E6%B5%8B%E8%AF%95%EF%BC%89_3riC5r%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_%E6%94%BB%E9%98%B2%E4%B8%96%E7%95%8C%E5%88%9B%E5%BB%BA%E5%8A%A8%E6%80%81%E7%8E%AF%E5%A2%83%E5%A4%B1%E8%B4%A5.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/team-[XCTF-PWN][高手进阶区]CTF-writeup攻防世界题解系列28（网站配置错误，需自行配置本地环境测试）_3riC5r的博客-CSDN博客_攻防世界创建动态环境失败.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: netcat, pwntools
- Techniques: binary-exploitation, encoding-analysis, format-string, integer-overflow, ret2libc, stack-overflow, web-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Linked Assets

- Referenced assets: `2`
- `docs/img/20e97091453d54e1c948b6779b69141e.png`
- `docs/img/f06ec722399742d98791fccaa2b87567.png`

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: team [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列28（网站配置错误，需自行配置本地环境测试）_3riC5r的博客-CSDN博客_攻防世界创建动态环境失败

- Route type: `integer-overflow bypass`
- Why: Numeric edge cases matter when they alter a length, signedness, allocation, or control-flow boundary.
- Probe: Use netcat, pwntools to verify the numeric edge case and how it changes the downstream size or bounds check.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as integer-overflow bypass.
  - Use netcat, pwntools to verify the numeric edge case and how it changes the downstream size or bounds check.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `20e97091453d54e1c948b6779b69141e`

### Step 3: param_num = 10 + (0x70-0xc)/4

- Route type: `netcat-driven evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
- Tools: netcat, pwntools
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, pwntools to collect the smallest evidence slice that answers the goal.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print(flag)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
