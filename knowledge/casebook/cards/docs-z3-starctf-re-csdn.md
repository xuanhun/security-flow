# 初遇z3并与starCTF碰面_黑羽re的博客-CSDN博客

## Case Metadata

- Category: `Web`
- Platform: `初遇z3并与starCTF碰面`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/初遇z3并与starCTF碰面_黑羽re的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E5%88%9D%E9%81%87z3%E5%B9%B6%E4%B8%8EstarCTF%E7%A2%B0%E9%9D%A2_%E9%BB%91%E7%BE%BDre%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/初遇z3并与starCTF碰面_黑羽re的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Web reference for ciphertext, web-app challenges.

## Input Signals

- Artifacts: ciphertext, web-app
- Tools: netcat, radare2, z3
- Techniques: crypto-analysis, sql-injection, symbolic-execution, web-exploitation

## First-Principles Route

- Identify the exposed entry point, reflected behavior, trust boundary, and any explicit hints or blacklists.
- Validate the suspected primitive with the smallest payload that proves code/data/control influence.
- Chain the primitive into file read, code execution, auth bypass, or state manipulation only after recording the bypass condition.

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 初遇z3并与starCTF碰面_黑羽re的博客-CSDN博客

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use netcat, radare2, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use netcat, radare2, z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `> 来源：[http://blog.csdn.net/m0_38094687/article/details/80113019](http://blog.csdn.net/m0_38094687/article/details/80113019)`

### Step 3: 介绍

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 with the extracted filter/query `Z3 是一个微软出品的开源约束求解器，能够解决很多种情况下的给定部分约束条件寻求一组满足条件的解的问题.在CTF中的应用主要在CRYPTO上.` and inspect the matching evidence.
- Tools: z3
- Filters or commands:
  - `Z3 是一个微软出品的开源约束求解器，能够解决很多种情况下的给定部分约束条件寻求一组满足条件的解的问题.在CTF中的应用主要在CRYPTO上.`
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 with the extracted filter/query `Z3 是一个微软出品的开源约束求解器，能够解决很多种情况下的给定部分约束条件寻求一组满足条件的解的问题.在CTF中的应用主要在CRYPTO上.` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Z3 是一个微软出品的开源约束求解器，能够解决很多种情况下的给定部分约束条件寻求一组满足条件的解的问题.在CTF中的应用主要在CRYPTO上.`

### Step 4: 安装

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `如果发现安装了用不了,可以使用`pip install z3-solver``

### Step 5: 使用

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 with the extracted filter/query `solve(x > 2, y < 10, x + 2*y == 7)` and inspect the matching evidence.
- Tools: z3
- Filters or commands:
  - `solve(x > 2, y < 10, x + 2*y == 7)`
  - `s.add(x > 2, y < 10, x<3,y>9,x + 2 * y == 8.5)`
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 with the extracted filter/query `solve(x > 2, y < 10, x + 2*y == 7)` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `同时z3包含Or,Not,And,if等逻辑运算符,详见[官方API](http://www.cs.tau.ac.il/~msagiv/courses/asv/z3py/guide-examples.htm)`

### Step 6: 举例

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use netcat with the extracted filter/query `diag_c = [ And(Q[i] - Q[j] != i - j, Q[i] - Q[j] != j - i))` and inspect the matching evidence.
- Tools: netcat
- Filters or commands:
  - `diag_c = [ And(Q[i] - Q[j] != i - j, Q[i] - Q[j] != j - i))`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use netcat with the extracted filter/query `diag_c = [ And(Q[i] - Q[j] != i - j, Q[i] - Q[j] != j - i))` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `solve(val_c + col_c + diag_c)`

### Step 7: *CTF SimpleWeb

- Route type: `sql injection exploitation`
- Why: SQLi cases are cheapest when the injection style is classified early and every response difference is recorded.
- Probe: Use netcat, radare2, z3 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
- Tools: netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as sql injection exploitation.
  - Use netcat, radare2, z3 to confirm injection context, then narrow to the cheapest boolean, union, error, or stacked route that leaks proof.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `因此我一开始想到了js的数组`sort()`问题,纯数字会按照字典序排还是数字大小排,但是没有测试,然后就gg了,浪费了一次宝贵的晋升大佬的机会 :P`

### Step 8: 题目

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 with the extracted filter/query `if (arr.length != 5)` and inspect the matching evidence.
- Tools: netcat, radare2
- Filters or commands:
  - `if (arr.length != 5)`
  - `if (arr1[i+1] == arr1[i] || arr[i] < 0 || arr1[i+1] > 127)`
  - `if (val != 0x23332333)`
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 with the extracted filter/query `if (arr.length != 5)` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `});`

### Step 9: 分析

- Route type: `http evidence extraction`
- Why: HTTP questions usually reduce to request metadata, response body, host/URI correlation, or object extraction.
- Probe: Use radare2 with the extracted filter/query `> 正常思路由题目`val != 0x23332333`可知最后计算要得到`0x23332333`,向上分析看来是迭代累加`x*0x100+y`,所以用`0x23332333`逐次`%0x100`,得到数组`arr2=[35,51,35,51]`.` and inspect the matching evidence.
- Tools: radare2
- Filters or commands:
  - `> 正常思路由题目`val != 0x23332333`可知最后计算要得到`0x23332333`,向上分析看来是迭代累加`x*0x100+y`,所以用`0x23332333`逐次`%0x100`,得到数组`arr2=[35,51,35,51]`.`
- Reasoning chain:
  - Recognize the section as http evidence extraction.
  - Use radare2 with the extracted filter/query `> 正常思路由题目`val != 0x23332333`可知最后计算要得到`0x23332333`,向上分析看来是迭代累加`x*0x100+y`,所以用`0x23332333`逐次`%0x100`,得到数组`arr2=[35,51,35,51]`.` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `2.javascript的`sort()`方法采用的是字典序,举例`[9,18,32,33]`的结果为`[18,32,33,9]``

### Step 10: 非预期

- Route type: `netcat-driven evidence lookup`
- Why: For Web, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2, z3
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2, z3 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: ``answer:1 33.75 80.75 81.75 97.25``

### Step 11: 预期

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 with the extracted filter/query `(value[2] + value[3])) * 0x100 + (value[3] + value[4])) == 0x23332333)` and inspect the matching evidence.
- Tools: z3
- Filters or commands:
  - `(value[2] + value[3])) * 0x100 + (value[3] + value[4])) == 0x23332333)`
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 with the extracted filter/query `(value[2] + value[3])) * 0x100 + (value[3] + value[4])) == 0x23332333)` and inspect the matching evidence.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `print s.model()`

### Step 12: 相关链接

- Route type: `constraint solving`
- Why: Constraint-solving cases become manageable after the exact branch conditions are isolated from the rest of the binary.
- Probe: Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
- Tools: z3
- Reasoning chain:
  - Recognize the section as constraint solving.
  - Use z3 to recover the exact checks or symbolic constraints and solve only the minimal branch needed for success.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `simpleweb非预期解: [https://ctftime.org/writeup/9835](https://ctftime.org/writeup/9835)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
