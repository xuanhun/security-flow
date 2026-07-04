# 南邮CTF平台-Vigenere题解（穷举法）_无意中流逝的博客-CSDN博客

## Case Metadata

- Category: `Training and Meta`
- Platform: `南邮CTF平台`
- Difficulty: `unknown`
- Source repository: `https://github.com/apachecn/apachecn-ctf-wiki`
- Source commit: `762ca130572c95196cf120e5f4ad5fbdd88b1b93`
- Source file: `docs/南邮CTF平台-Vigenere题解（穷举法）_无意中流逝的博客-CSDN博客.md`
- Source URL: `https://github.com/apachecn/apachecn-ctf-wiki/blob/762ca130572c95196cf120e5f4ad5fbdd88b1b93/docs/%E5%8D%97%E9%82%AECTF%E5%B9%B3%E5%8F%B0-Vigenere%E9%A2%98%E8%A7%A3%EF%BC%88%E7%A9%B7%E4%B8%BE%E6%B3%95%EF%BC%89_%E6%97%A0%E6%84%8F%E4%B8%AD%E6%B5%81%E9%80%9D%E7%9A%84%E5%8D%9A%E5%AE%A2-CSDN%E5%8D%9A%E5%AE%A2.md`
- Local source mirror: `sources/apachecn-apachecn-ctf-wiki/repo/docs/南邮CTF平台-Vigenere题解（穷举法）_无意中流逝的博客-CSDN博客.md`

## Why This Case Matters

Use this case as a Training and Meta reference for ciphertext challenges.

## Input Signals

- Artifacts: ciphertext
- Tools: netcat, radare2
- Techniques: crypto-analysis, siem-query

## First-Principles Route

- Treat the document as study guidance: extract challenge taxonomy, workflow rules, tool references, and reusable habits.
- Record platform names, topic tags, and tool examples so later queries can reach the right note quickly.
- Prefer compact summaries that preserve lookup value over full-text duplication.

## Solve Thinking

### Step 1: Document

- Route type: `netcat-driven evidence lookup`
- Why: For Training and Meta, keep every answer tied to one artifact, one probe, and one proof field.
- Probe: Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
- Tools: netcat, radare2
- Reasoning chain:
  - Recognize the section as netcat-driven evidence lookup.
  - Use netcat, radare2 to collect the smallest evidence slice that answers the goal.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `-->`

### Step 2: 南邮CTF平台-Vigenere题解（穷举法）_无意中流逝的博客-CSDN博客

- Route type: `cipher decoding`
- Why: Crypto cases should peel encodings first and keep every transformation individually checkable.
- Probe: Use netcat, radare2 with the extracted filter/query `| a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p |` and inspect the matching evidence.
- Tools: netcat, radare2
- Filters or commands:
  - `| a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p |`
  - `| W | X | Y | Z | W | X | Y | Z | W | X | Y | Z | W | X | Y | Z |`
  - `print('keylen=',keylen,'index=',index,'keys=',ans_keys)`
  - `keylen= 1 index= 0 keys= []`
  - `keylen= 2 index= 0 keys= []`
  - `keylen= 2 index= 1 keys= []`
- Reasoning chain:
  - Recognize the section as cipher decoding.
  - Use netcat, radare2 with the extracted filter/query `| a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p |` and inspect the matching evidence.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `print(ming)`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
