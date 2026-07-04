# CTF解题小记--心得记录1_Air_cat的博客-CSDN博客

## Case Metadata

- Category: `Crypto`
- Platform: `CTF解题小记`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF解题小记--心得记录1_Air_cat的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF%E8%A7%A3%E9%A2%98%E5%B0%8F%E8%AE%B0--%E5%BF%83%E5%BE%97%E8%AE%B0%E5%BD%951_Air_cat%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF解题小记--心得记录1_Air_cat的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Crypto reference for binary, ciphertext, pe-malware challenges.

## Input Signals

- Artifacts: binary, ciphertext, pe-malware
- Tools: angr, dnspy, netcat
- Techniques: crypto-analysis, dns-analysis, php-tricks, reverse-engineering, stream-cipher, symbolic-execution

## First-Principles Route

- Classify the cipher family, encoding layer, and available known-plaintext or structural clues before writing code.
- Separate transport/encoding cleanup from the actual cryptographic break so each assumption can be verified.
- Keep one reproducible decode or solve path that explains why the recovered plaintext is trustworthy.

## Solve Thinking

### Step 1: Document

- Route type: `reverse engineering`
- Why: Reverse routes pivot from strings/imports into the exact validation or decoding logic.
- Probe: Use angr, dnspy, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
- Tools: angr, dnspy, netcat
- Reasoning chain:
  - Recognize the section as reverse engineering.
  - Use angr, dnspy, netcat to locate strings, comparisons, and control-flow decisions relevant to the input.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF解题小记--心得记录1_Air_cat的博客-CSDN博客

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use angr, dnspy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Tools: angr, dnspy, netcat
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use angr, dnspy, netcat to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `CTF解题笔记 (Aircat)`

### Step 3: RSA题

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `304008741604601924494328155975272418463`

### Step 4: Unity

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use angr, dnspy to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: angr, dnspy
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use angr, dnspy to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - The proof is the recovered input satisfying the exact validation branch or symbolic condition.
- Evidence rule: The proof is the recovered input satisfying the exact validation branch or symbolic condition.

### Step 5: HE-CTF2019

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use dnspy to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: dnspy
- Reasoning chain:
  - Recognize the section as dns pivot.
  - Use dnspy to filter DNS traffic and pivot from source host to queried domain or resolver.
  - The proof is the DNS packet, resolver, queried domain, or response record.
- Evidence rule: The proof is the DNS packet, resolver, queried domain, or response record.

### Step 6: 巅峰极客2019

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use angr, dnspy, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
- Tools: angr, dnspy, netcat
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use angr, dnspy, netcat to separate encoding cleanup from the actual cipher break and verify the plaintext structure after each step.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `本次比赛死在了不懂rc4（我自己觉得），好好做题，好好搜集加密算法，看完爆破不就完事了吗。`

### Step 7: V&N2020公开赛 – strangecpp

- Route type: `angr-driven evidence lookup`
- Why: For Crypto, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use angr, dnspy, netcat to collect the smallest evidence slice that answers the goal.
- Tools: angr, dnspy, netcat
- Reasoning chain:
  - Recognize the section as angr-driven evidence lookup.
  - Use angr, dnspy, netcat to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `这题主函数就是个five，我是摸到通过主函数调用的全局数组摸到数据段才发现关键数组的，查看调用之后发现了加密函数，证实是加密数组。不过我自己做卡在了md5上，悲。对于md5这种东西是对字符串处理的东西一定要注意数据的表达形式啊。`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
