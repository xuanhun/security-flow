# CTF-z3简要介绍_Thunder_J的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `CTF`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/CTF-z3简要介绍_Thunder_J的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/CTF-z3%E7%AE%80%E8%A6%81%E4%BB%8B%E7%BB%8D_Thunder_J%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/CTF-z3简要介绍_Thunder_J的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: angr, z3
- Techniques: symbolic-execution

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Solve Thinking

### Step 1: Document

- Route type: `angr-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use angr, z3 to collect the smallest evidence slice that answers the goal.
- Tools: angr, z3
- Reasoning chain:
  - Recognize the section as angr-driven evidence lookup.
  - Use angr, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: CTF-z3简要介绍_Thunder_J的博客-CSDN博客

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use angr, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: angr, z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use angr, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/charlesgodx/article/details/89931468](https://blog.csdn.net/charlesgodx/article/details/89931468)`

### Step 3: 介绍

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Z3是微软研究院的一个定理验证器。它是由麻省理工学院授权的，常用来解一些方程组，在做一些CTF逆向题目的时候很有用，下面就简单介绍一下这个工具。`

### Step 4: 下载

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `sudo pip install z3-solver`

### Step 5: 例子

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use angr, z3 with the extracted filter/query `Python 3.6.7 (default, Oct 22 2018, 11:32:17)` and inspect the matching evidence.
- Tools: angr, z3
- Filters or commands:
  - `Python 3.6.7 (default, Oct 22 2018, 11:32:17)`
  - `>>> s.add(x^y&z==12)`
  - `>>> s.add(y&x>>3==3)`
  - `>>> s.add(z^y==4)`
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use angr, z3 with the extracted filter/query `Python 3.6.7 (default, Oct 22 2018, 11:32:17)` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `[https://github.com/UnnameBao/My_ctf_path/tree/master/blog/I_Hate_Math](https://github.com/UnnameBao/My_ctf_path/tree/master/blog/I_Hate_Math)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
