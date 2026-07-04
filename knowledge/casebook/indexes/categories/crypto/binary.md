# Crypto / binary

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| crypto-analysis | 36 | cipher decoding, http evidence extraction, netcat-driven evidence lookup, reverse engineering, constraint solving |
| encoding-analysis | 33 | cipher decoding, http evidence extraction, netcat-driven evidence lookup, reverse engineering, constraint solving |
| classical-crypto | 22 | cipher decoding, http evidence extraction, reverse engineering, netcat-driven evidence lookup, constraint solving |
| binary-exploitation | 20 | cipher decoding, http evidence extraction, reverse engineering, netcat-driven evidence lookup, command execution path |
| http-analysis | 16 | cipher decoding, reverse engineering, http evidence extraction, netcat-driven evidence lookup, command execution path |
| reverse-engineering | 16 | reverse engineering, cipher decoding, http evidence extraction, command execution path, constraint solving |
| php-tricks | 15 | cipher decoding, http evidence extraction, reverse engineering, netcat-driven evidence lookup, constraint solving |
| web-exploitation | 15 | cipher decoding, http evidence extraction, reverse engineering, netcat-driven evidence lookup, constraint solving |
| qr-analysis | 12 | cipher decoding, http evidence extraction, reverse engineering, command execution path, constraint solving |
| symbolic-execution | 9 | cipher decoding, constraint solving, http evidence extraction, reverse engineering, angr-driven evidence lookup |
| command-injection | 8 | reverse engineering, cipher decoding, command execution path, file inclusion exploitation, http evidence extraction |
| file-inclusion | 6 | reverse engineering, file inclusion exploitation, cipher decoding, http evidence extraction, constraint solving |
| image-analysis | 5 | cipher decoding, http evidence extraction, constraint solving, reverse engineering, angr-driven evidence lookup |
| misc-analysis | 3 | cipher decoding, http evidence extraction, reverse engineering, angr-driven evidence lookup, command execution path |
| service-enumeration | 3 | cipher decoding, http evidence extraction, reverse engineering, constraint solving, file inclusion exploitation |
| stego-extraction | 3 | cipher decoding, http evidence extraction, angr-driven evidence lookup, command execution path, constraint solving |
| waf-bypass | 3 | reverse engineering, waf bypass, cipher decoding, command execution path |
| dns-analysis | 2 | constraint solving, reverse engineering, angr-driven evidence lookup, cipher decoding, dns pivot |
| malware-static | 2 | cipher decoding, http evidence extraction, angr-driven evidence lookup, constraint solving, credential discovery |
| memory-forensics | 2 | cipher decoding, http evidence extraction, angr-driven evidence lookup, constraint solving, credential discovery |
| mobile-forensics | 2 | reverse engineering, command execution path, constraint solving, file inclusion exploitation, ida-driven evidence lookup |
| network-forensics | 2 | reverse engineering, cipher decoding, command execution path, http evidence extraction, stego extraction |
| ret2libc | 2 | file inclusion exploitation, command execution path, gdb-driven evidence lookup, reverse engineering |
| siem-query | 2 | reverse engineering, cipher decoding, command execution path, constraint solving, file inclusion exploitation |
| stream-cipher | 2 | angr-driven evidence lookup, cipher decoding, constraint solving, http evidence extraction, dns pivot |
| traffic-analysis | 2 | reverse engineering, cipher decoding, command execution path, http evidence extraction, stego extraction |
| browser-forensics | 1 | file inclusion exploitation, gdb-driven evidence lookup |
| deserialization | 1 | cipher decoding, http evidence extraction, reverse engineering, stego extraction |
| integer-overflow | 1 | command execution path, file inclusion exploitation, reverse engineering |
| osint | 1 | cipher decoding, constraint solving, http evidence extraction, reverse engineering |
| password-cracking | 1 | cipher decoding, credential discovery, http evidence extraction, john-driven evidence lookup, netcat-driven evidence lookup |
| privilege-escalation | 1 | file inclusion exploitation, gdb-driven evidence lookup |
| sql-injection | 1 | cipher decoding, evidence lookup, http evidence extraction |
| ssti | 1 | angr-driven evidence lookup, cipher decoding, constraint solving, http evidence extraction |
| xss | 1 | cipher decoding, constraint solving, http evidence extraction, reverse engineering |

## Route Types

| Route type | Cases |
| --- | --- |
| cipher decoding | 28 |
| http evidence extraction | 21 |
| reverse engineering | 15 |
| netcat-driven evidence lookup | 14 |
| constraint solving | 5 |
| file inclusion exploitation | 4 |
| command execution path | 3 |
| pwntools-driven evidence lookup | 3 |
| angr-driven evidence lookup | 2 |
| detect-it-easy-driven evidence lookup | 2 |
| evidence lookup | 2 |
| ida-driven evidence lookup | 2 |
| waf bypass | 2 |
| burp-driven evidence lookup | 1 |
| credential discovery | 1 |
| dns pivot | 1 |
| gdb-driven evidence lookup | 1 |
| indicator enrichment | 1 |
| john-driven evidence lookup | 1 |
| memory artifact analysis | 1 |
| stego extraction | 1 |
| z3-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [[buuctf]crypto刷题学习记录（1-22）_hyxyan的博客-CSDN博客](../../../cards/docs-buuctf-crypto-1-22-hyxyan-csdn.md) | buuctf |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [[GCCCTF 2025]密钥危机](../../../cards/crypto-gccctf-2025.md) | GCCCTF 2025 |  | crypto-analysis, encoding-analysis, reverse-engineering |
| [AGCTF WP_weixin_52631365的博客-CSDN博客](../../../cards/docs-agctf-wp-weixin-52631365-csdn.md) | AGCTF WP |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [bugkuCTF平台逆向题第五道love题解_iqiqiya的博客-CSDN博客_bugku love](../../../cards/docs-bugkuctf-love-iqiqiya-csdn-bugku-love.md) | bugkuCTF平台逆向题第五道love题解 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [BUUCTF[SCTF2019]Who is he题解_mortal15的博客-CSDN博客](../../../cards/docs-buuctf-sctf2019-who-is-he-mortal15-csdn.md) | BUUCTF[SCTF2019]Who is he题解 |  | crypto-analysis |
| [CTF - Base64换表_建瓯最坏的博客-CSDN博客_base64换表](../../../cards/docs-ctf-base64-csdn-base64.md) | CTF |  | classical-crypto, encoding-analysis, qr-analysis, reverse-engineering |
| [CTF-加密与解密（十八）_红烧兔纸的博客-CSDN博客_曼联加密](../../../cards/docs-ctf-csdn.md) | CTF |  | classical-crypto, crypto-analysis, encoding-analysis |
| [CTF基础解题_destin_love的博客-CSDN博客_ctf解题](../../../cards/docs-ctf-destin-love-csdn-ctf.md) | CTF基础解题 |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [ctf学习经历——极客部分题解_RoleMee的博客-CSDN博客](../../../cards/docs-ctf-rolemee-csdn.md) | ctf学习经历——极客部分题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [CTF解题小记--心得记录1_Air_cat的博客-CSDN博客](../../../cards/docs-ctf-1-air-cat-csdn.md) | CTF解题小记 |  | crypto-analysis, dns-analysis, php-tricks, reverse-engineering |
| [CTF部分题目解析_阿峰啊啊啊的博客-CSDN博客_ctf竞赛试题及答案](../../../cards/docs-ctf-csdn-ctf.md) | CTF部分题目解析 |  | classical-crypto, crypto-analysis, encoding-analysis, symbolic-execution |
| [Jarvis OJ 刷题题解 RE_pipixia233333的博客-CSDN博客](../../../cards/docs-jarvis-oj-re-pipixia233333-csdn.md) | Jarvis OJ 刷题题解 RE |  | binary-exploitation, classical-crypto, crypto-analysis, dns-analysis |
| [PWN fd [pwnable.kr]CTF writeup题解系列1_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-fd-pwnable-kr-ctf-writeup-1-3ric5r-csdn.md) | PWN fd [pwnable.kr]CTF writeup题解系列1 |  | binary-exploitation, browser-forensics, command-injection, crypto-analysis |
| [python md5解密_CTF-敲错键盘的md5解密，python通解_weixin_39616416的博客-CSDN博客](../../../cards/docs-python-md5-ctf-md5-python-weixin-39616416-csdn.md) | python md5解密 |  | crypto-analysis, encoding-analysis, http-analysis, php-tricks |
| [python求解二元二次方程组_【CTF WriteUp】2020祥云杯Crypto题解_张仁鹏的博客-CSDN博客](../../../cards/docs-python-ctf-writeup-2020-crypto-csdn.md) | python求解二元二次方程组 |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [rgss加密文件解包器_OGeek线上CTF挑战赛逆向及加密类赛题详细Write Up_weixin_39751871的博客-CSDN博客](../../../cards/docs-rgss-ogeek-ctf-write-up-weixin-39751871-csdn.md) | rgss加密文件解包器 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [【CTF WriteUp】201909广东强网杯部分题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-201909-csdn.md) | 【CTF WriteUp】201909广东强网杯部分题解 |  | binary-exploitation, crypto-analysis, encoding-analysis, http-analysis |
| [【CTF WriteUp】2020中央企业”新基建“网络安全技术大赛决赛部分Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [【CTF WriteUp】2020全国工业互联网安全技术技能大赛（原护网杯）Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF |  | binary-exploitation, crypto-analysis, encoding-analysis, web-exploitation |
| [【CTF WriteUp】2020数字中国创新大赛部分题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-csdn.md) | 【CTF WriteUp】2020数字中国创新大赛部分题解 |  | binary-exploitation, crypto-analysis, encoding-analysis |
| [【CTF WriteUp】2020电信和互联网行业赛个人赛部分Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF WriteUp】2020电信和互联网行业赛个人赛部分Crypto题解 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [【CTF WriteUp】2020祥云杯Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF WriteUp】2020祥云杯Crypto题解 |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [【CTF WriteUp】2020第四届强网杯部分Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF WriteUp】2020第四届强网杯部分Crypto题解 |  | binary-exploitation, crypto-analysis, encoding-analysis |
| [【CTF WriteUp】2020网鼎杯第一场Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF WriteUp】2020网鼎杯第一场Crypto题解 |  | crypto-analysis, encoding-analysis, php-tricks |
| [【CTF WriteUp】2021 starCTF部分Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2021-starctf-crypto-csdn.md) | 【CTF WriteUp】2021 starCTF部分Crypto题解 |  | binary-exploitation, crypto-analysis, encoding-analysis, http-analysis |
| [【CTF WriteUp】UTCTF 2020部分题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-utctf-2020-csdn.md) | 【CTF WriteUp】UTCTF 2020部分题解 |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [【CTF大赛】陇剑杯-机密内存-解题过程分析_IT老涵的博客-CSDN博客_ctf内存分析](../../../cards/docs-ctf-it-csdn-ctf.md) | 【CTF大赛】陇剑杯 |  | crypto-analysis, encoding-analysis, malware-static, memory-forensics |
| [【moeCTF题解-0x04】Crypto_框架主义者的博客-CSDN博客](../../../cards/docs-moectf-0x04-crypto-csdn.md) | 【moeCTF题解 |  | classical-crypto, crypto-analysis, encoding-analysis, file-inclusion |
| [再不学点现代密码，CTF就Hold不住啦！_合天网安实验室的博客-CSDN博客](../../../cards/docs-ctf-hold-csdn.md) | 再不学点现代密码，CTF就Hold不住啦！ |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [南邮CTF逆向题第三道Py交易解题思路_iqiqiya的博客-CSDN博客](../../../cards/docs-ctf-py-iqiqiya-csdn.md) | 南邮CTF逆向题第三道Py交易解题思路 |  | classical-crypto, crypto-analysis, encoding-analysis |
| [大连海事大学第一届“启航杯”DLMU CTF部分题解_ℳ๓₯㎕₯㎕ζั的博客-CSDN博客](../../../cards/docs-dlmu-ctf-csdn.md) | 大连海事大学第一届“启航杯”DLMU CTF部分题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [实验吧 部分逆向题解_pipixia233333的博客-CSDN博客](../../../cards/docs-pipixia233333-csdn.md) | 实验吧 部分逆向题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [最后一位被整除 oracle,【CTF WriteUp】2020第四届强网杯部分Crypto题解_weixin_39644952的博客-CSDN博客](../../../cards/docs-oracle-ctf-writeup-2020-crypto-weixin-39644952-csdn.md) | 最后一位被整除 |  | binary-exploitation, crypto-analysis, encoding-analysis |
| [百度杯”CTF比赛（十一月场)_Root__Liu的博客-CSDN博客](../../../cards/docs-ctf-root-liu-csdn.md) | 百度杯”CTF比赛（十一月场) |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [看雪ctf部分题解_合天网安实验室的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | 看雪ctf部分题解 |  | binary-exploitation, crypto-analysis, encoding-analysis, reverse-engineering |
| [第6篇：基础入门~加密编码算法_廖一语山的博客-CSDN博客](../../../cards/docs-6-csdn.md) | 第6篇：基础入门~加密编码算法 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [记ctf解题思路_weixin_49757373的博客-CSDN博客_ctf夺旗赛解题思路](../../../cards/docs-ctf-weixin-49757373-csdn-ctf.md) | 记ctf解题思路 |  | php-tricks, reverse-engineering |
| [邑网杯 CTF 2021 ,cipher2 ADFGVX 解题_euzen的博客-CSDN博客](../../../cards/docs-ctf-2021-cipher2-adfgvx-euzen-csdn.md) | 邑网杯 CTF 2021 ,cipher2 ADFGVX 解题 |  | crypto-analysis, qr-analysis |
