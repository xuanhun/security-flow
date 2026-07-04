# z3 巧解CTF逆向题_weixin_30613343的博客-CSDN博客

## Case Metadata

- Category: `Reverse`
- Platform: `z3 巧解CTF逆向题`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/z3-巧解CTF逆向题_weixin_30613343的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/z3-%E5%B7%A7%E8%A7%A3CTF%E9%80%86%E5%90%91%E9%A2%98_weixin_30613343%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/z3-巧解CTF逆向题_weixin_30613343的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Reverse reference for binary challenges.

## Input Signals

- Artifacts: binary
- Tools: z3
- Techniques: crypto-analysis, symbolic-execution

## First-Principles Route

- Inventory strings, imports, validation points, encoded constants, and packer/runtime clues before solving logic.
- Translate one observed input/output behavior into the exact compare, decode, or constraint branch that controls success.
- Prefer the smallest static or dynamic proof that explains the flag or accepted input.

## Solve Thinking

### Step 1: Document

- Route type: `z3-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use z3 to collect the smallest evidence slice that answers the goal.
- Tools: z3
- Reasoning chain:
  - Recognize the section as z3-driven evidence lookup.
  - Use z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: z3 巧解CTF逆向题_weixin_30613343的博客-CSDN博客

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[https://blog.csdn.net/weixin_30613343/article/details/97154205](https://blog.csdn.net/weixin_30613343/article/details/97154205)`

### Step 3: z3 巧解逆向题

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `download.php`

### Step 4: z3 求解器是什么？

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 with the extracted filter/query `x-y == 3` and inspect the matching evidence.
- Tools: z3
- Filters or commands:
  - `x-y == 3`
  - `3x-8y == 4`
  - `In [134]: solver.add(x-y == 3)`
  - `In [135]: solver.add(3*x-8*y == 4)`
  - `z3 难道就只能用来解小学方程吗？当然不是！来看题。`
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 with the extracted filter/query `x-y == 3` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `z3 难道就只能用来解小学方程吗？当然不是！来看题。`

### Step 5: 0x0 定位

- Route type: `z3-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use z3 with the extracted filter/query `if ( *(username - 12) == 4 )` and inspect the matching evidence.
- Tools: z3
- Filters or commands:
  - `if ( *(username - 12) == 4 )`
  - `if ( v1 != v4 )`
  - `if ( ATL::CSimpleStringT<wchar_t,1>::GetAt(&username, v1) == v5 )`
  - `if ( *(serial - 12) == 11 && ATL::CSimpleStringT<wchar_t,1>::GetAt(&serial, 5) == '-' )`
  - `if ( ATL::CSimpleStringT<wchar_t,1>::GetAt(&serial, 0) == v11 )`
  - `if ( v13 == ATL::CSimpleStringT<wchar_t,1>::GetAt(&v52, 0) )`
- Reasoning chain:
  - Recognize the section as z3-driven evidence lookup.
  - Use z3 with the extracted filter/query `if ( *(username - 12) == 4 )` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `}`

### Step 6: 0x1 初步分析，输入有效性分析

- Route type: `z3-driven evidence lookup`
- Why: For Reverse, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use z3 with the extracted filter/query `serial 只有11字节，且第serial[5]=='-'。` and inspect the matching evidence.
- Tools: z3
- Filters or commands:
  - `serial 只有11字节，且第serial[5]=='-'。`
- Reasoning chain:
  - Recognize the section as z3-driven evidence lookup.
  - Use z3 with the extracted filter/query `serial 只有11字节，且第serial[5]=='-'。` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `serial 只有11字节，且第serial[5]=='-'。`

### Step 7: 0x2 进一步分析，约束条件

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 with the extracted filter/query `2、username[3] == 'p' //这个是题目给出的条件，非逆向所得。` and inspect the matching evidence.
- Tools: z3
- Filters or commands:
  - `2、username[3] == 'p' //这个是题目给出的条件，非逆向所得。`
  - `((username[0]&1)+5+(((username[1]>>2) & 1 )+1))==ord('7')-0x30`
  - `((((username[0]>>3) & 1)+5)+(((username[1]>>3)&1)+1))==ord('6')-0x30`
  - `(((username[0]>>1) & 1)+5+(((username[1]>>4) & 1 )+1))==ord('8')-0x30`
  - `(((username[0]>>2) & 1)+5+(((username[1]) & 1 )+1))==ord('7')-0x30`
  - `(((username[0]>>4) & 1)+5+(((username[1]>>1) & 1 )+1))==ord('6')-0x30`
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 with the extracted filter/query `2、username[3] == 'p' //这个是题目给出的条件，非逆向所得。` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `ord是python中的函数，功能是将字符转成对应int。为什么我要这么做呢？从逆向出的代码片段可知，原程序用itow_s将运算值转为文本，然后取文本的最高位和输入的ASCII进行比较，但是运算结果只有一位数，我就直接用加减0x30，其次z3条件里面好像不能有str()这样的函数出现。`

### Step 8: 0x3 编写程序，取得flag！

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 with the extracted filter/query `solver.add(((username[0]&1)+5+(((username[1]>>2) & 1 )+1))==ord('7')-0x30)` and inspect the matching evidence.
- Tools: z3
- Filters or commands:
  - `solver.add(((username[0]&1)+5+(((username[1]>>2) & 1 )+1))==ord('7')-0x30)`
  - `solver.add(((((username[0]>>3) & 1)+5)+(((username[1]>>3)&1)+1))==ord('6')-0x30)`
  - `solver.add((((username[0]>>1) & 1)+5+(((username[1]>>4) & 1 )+1))==ord('8')-0x30)`
  - `solver.add((((username[0]>>2) & 1)+5+(((username[1]) & 1 )+1))==ord('7')-0x30)`
  - `solver.add((((username[0]>>4) & 1)+5+(((username[1]>>1) & 1 )+1))==ord('6')-0x30)`
  - `solver.add((((username[2]) & 1)+5+(((username[3]>>2) & 1 )+1))==ord('7')-0x30)`
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 with the extracted filter/query `solver.add(((username[0]&1)+5+(((username[1]>>2) & 1 )+1))==ord('7')-0x30)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `[https://github.com/Z3Prover/z3](https://github.com/Z3Prover/z3)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
