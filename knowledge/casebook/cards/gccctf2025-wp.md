# GCCCTF 2025 官方 Writeup

## Case Metadata

- Category: `Training and Meta`
- Platform: `GCCCTF 2025`
- Difficulty: `unknown`
- Source repository: `https://github.com/CUCCS/ctf-wps`
- Source commit: `50d7ff1080f746e3d0f23a80e22d86c0f8a67d70`
- Source file: `GCCCTF2025_官方WP.md`
- Source URL: `https://github.com/CUCCS/ctf-wps/blob/50d7ff1080f746e3d0f23a80e22d86c0f8a67d70/GCCCTF2025_%E5%AE%98%E6%96%B9WP.md`
- Local source mirror: `sources/cuccs-ctf-wps/repo/GCCCTF2025_官方WP.md`

## Why This Case Matters

Use this case as a Training and Meta reference for binary, ciphertext, web-app challenges.

## Input Signals

- Artifacts: binary, ciphertext, web-app
- Tools: not detected
- Techniques: binary-exploitation, crypto-analysis, dns-analysis, http-analysis, misc-analysis, symbolic-execution, web-exploitation

## First-Principles Route

- Treat the document as study guidance: extract challenge taxonomy, workflow rules, tool references, and reusable habits.
- Record platform names, topic tags, and tool examples so later queries can reach the right note quickly.
- Prefer compact summaries that preserve lookup value over full-text duplication.

## Solve Thinking

### Step 1: 真题复现

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use the artifact-specific tool to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use the artifact-specific tool to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- [守法公民](https://www.nssctf.cn/problem/7214)`

### Step 2: PWN

- Route type: `evidence lookup`
- Why: For Training and Meta, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- [昔涟的礼物](pwn/%5BGCCCTF%202025%5D昔涟的礼物.md)`

### Step 3: Reverse

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use the artifact-specific tool to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use the artifact-specific tool to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- [constraint](reverse/%5BGCCCTF%202025%5D%20constraint.md)`

### Step 4: Crypto

- Route type: `evidence lookup`
- Why: For Training and Meta, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
- Reasoning chain:
  - Recognize the section as evidence lookup.
  - Use the artifact-specific tool to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- [密钥危机](crypto/%5BGCCCTF%202025%5D密钥危机.md)`

### Step 5: MISC

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use the artifact-specific tool to filter DNS traffic and pivot from source host to queried domain or resolver.
- Reasoning chain:
  - Recognize the section as dns pivot.
  - Use the artifact-specific tool to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- [eztalk](misc/GCCCTF2025_eztalk.md)`

### Step 6: WEB

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use the artifact-specific tool to inspect HTTP requests, hosts, URIs, headers, and response bodies.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `- [守法公民](web/%5BGCCCTF%202025%5D守法公民.md)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
