# CTF pwn题之虚拟机题型详解___lifanxin的博客-CSDN博客_pwn题型

## Case Metadata

- Category: `Pwn`
- Platform: `CTF pwn题之虚拟机题型详解`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF-pwn题之虚拟机题型详解___lifanxin的博客-CSDN博客_pwn题型.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF-pwn%E9%A2%98%E4%B9%8B%E8%99%9A%E6%8B%9F%E6%9C%BA%E9%A2%98%E5%9E%8B%E8%AF%A6%E8%A7%A3___lifanxin%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2_pwn%E9%A2%98%E5%9E%8B.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF-pwn题之虚拟机题型详解___lifanxin的博客-CSDN博客_pwn题型.md`

## Why This Case Matters

Use this case as a Pwn reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: not detected
- Techniques: binary-exploitation

## First-Principles Route

- Start from binary properties, architecture, mitigations, and obvious control-flow or memory-corruption primitives.
- Prove the crash or control point first, then derive the shortest control-flow path such as ret2text, ret2libc, or stack pivot.
- Keep offsets, gadgets, and calling assumptions tied to concrete disassembly or debugger evidence.

## Solve Thinking

### Step 1: Document

- Route type: `evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF pwn题之虚拟机题型详解___lifanxin的博客-CSDN博客_pwn题型

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/A951860555/article/details/117202160](https://blog.csdn.net/A951860555/article/details/117202160)`

### Step 3: 概述

- Route type: `evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `其实这种题做法和普通pwn类似，也是寻找漏洞，复杂的地方在于需要我们去分析出虚拟机实现的指令，然后用这些指令操作进行漏洞利用。`

### Step 4: 如何分析

- Route type: `evidence lookup`
- Why: For Pwn, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `VM类型的pwn究其本质还是用程序实现了一个虚拟机，这个虚拟机可以解析自定义的指令。这里我们可以类比真实的机器，程序在运行时需要操作寄存器、内存空间，内存空间细分的话还有栈、堆以及代码段等。pwn题的虚拟机就是用程序虚拟了这些物理器件，并通过代码逻辑来对指令进行解析，使得各个虚拟部件合理配合，完成工作。`

### Step 5: 一个例子

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[OGeek_2019_Final OVM题解](https://blog.csdn.net/A951860555/article/details/117214601)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
