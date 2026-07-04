# Reverse / web-app

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| reverse-engineering | 16 | reverse engineering, cipher decoding, file inclusion exploitation, http evidence extraction, command execution path |
| http-analysis | 14 | reverse engineering, cipher decoding, http evidence extraction, IDA Pro-driven evidence lookup, command execution path |
| web-exploitation | 14 | reverse engineering, cipher decoding, http evidence extraction, IDA Pro-driven evidence lookup, command execution path |
| crypto-analysis | 13 | reverse engineering, cipher decoding, http evidence extraction, file inclusion exploitation, IDA Pro-driven evidence lookup |
| classical-crypto | 11 | reverse engineering, cipher decoding, http evidence extraction, file inclusion exploitation, IDA Pro-driven evidence lookup |
| encoding-analysis | 10 | reverse engineering, cipher decoding, http evidence extraction, file inclusion exploitation, IDA Pro-driven evidence lookup |
| file-inclusion | 7 | file inclusion exploitation, reverse engineering, http evidence extraction, cipher decoding, netcat-driven evidence lookup |
| mobile-forensics | 6 | reverse engineering, http evidence extraction, cipher decoding, command execution path, file inclusion exploitation |
| command-injection | 4 | reverse engineering, cipher decoding, http evidence extraction, command execution path, file inclusion exploitation |
| integer-overflow | 4 | http evidence extraction, reverse engineering, cipher decoding, command execution path, file inclusion exploitation |
| malware-static | 4 | reverse engineering, file inclusion exploitation, cipher decoding, http evidence extraction, integer-overflow bypass |
| qr-analysis | 4 | cipher decoding, http evidence extraction, reverse engineering, command execution path, file inclusion exploitation |
| stego-extraction | 4 | reverse engineering, file inclusion exploitation, cipher decoding, http evidence extraction, integer-overflow bypass |
| php-tricks | 3 | cipher decoding, http evidence extraction, reverse engineering, file inclusion exploitation, command execution path |
| osint | 2 | reverse engineering |
| stream-cipher | 2 | cipher decoding, file inclusion exploitation, http evidence extraction, IDA Pro-driven evidence lookup, netcat-driven evidence lookup |
| symbolic-execution | 2 | reverse engineering, constraint solving, file inclusion exploitation |
| waf-bypass | 2 | reverse engineering, integer-overflow bypass, waf bypass |
| binary-exploitation | 1 | command execution path, reverse engineering |
| dns-analysis | 1 | cipher decoding, file inclusion exploitation, http evidence extraction, reverse engineering |
| misc-analysis | 1 | cipher decoding, file inclusion exploitation, http evidence extraction, reverse engineering |
| password-cracking | 1 | command execution path, reverse engineering |
| ret2libc | 1 | cipher decoding, command execution path, http evidence extraction, reverse engineering |
| stack-overflow | 1 | cipher decoding, command execution path, http evidence extraction, reverse engineering |

## Route Types

| Route type | Cases |
| --- | --- |
| reverse engineering | 14 |
| cipher decoding | 8 |
| file inclusion exploitation | 6 |
| http evidence extraction | 6 |
| command execution path | 3 |
| IDA Pro-driven evidence lookup | 3 |
| netcat-driven evidence lookup | 3 |
| constraint solving | 1 |
| ida-driven evidence lookup | 1 |
| integer-overflow bypass | 1 |
| stego extraction | 1 |
| waf bypass | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [2021虎符ctf-逆向题解_20000s的博客-CSDN博客](../../../cards/docs-2021-ctf-20000s-csdn.md) | 2021虎符ctf |  | crypto-analysis, encoding-analysis, file-inclusion, integer-overflow |
| [[BUUCTF 刷题] Reverse解题方法总结（一）_Y1seco的博客-CSDN博客_buuctf reverse](../../../cards/docs-buuctf-reverse-y1seco-csdn-buuctf-reverse.md) | BUUCTF 刷题 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [[MoeCTF 2022] Base](../../../cards/reverse-moectf-2022-base.md) | MoeCTF 2022 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [[SWPUCTF 2022 新生赛] upx](../../../cards/reverse-swpuctf-2022-upx.md) | SWPUCTF 2022 新生赛 |  | crypto-analysis, http-analysis, reverse-engineering, web-exploitation |
| [[SWPUCTF 2024 秋季新生赛] 动态调试](../../../cards/reverse-swpuctf-2024.md) | SWPUCTF 2024 秋季新生赛 |  | classical-crypto, crypto-analysis, http-analysis, reverse-engineering |
| [[WUSTCTF 2020] funnyre](../../../cards/reverse-wustctf-2020-funnyre.md) | WUSTCTF 2020 |  | http-analysis, reverse-engineering, symbolic-execution, web-exploitation |
| [[羊城杯 2020] easyre](../../../cards/reverse-2020-easyre.md) | 羊城杯 2020 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [android ctf 分析,Android逆向笔记 - ZCTF2016题解_weixin_39590635的博客-CSDN博客](../../../cards/docs-android-ctf-android-zctf2016-weixin-39590635-csdn.md) | android ctf 分析,Android逆向笔记 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [BugkuCTF RE部分题解_z.volcano的博客-CSDN博客_bugku 杰瑞的影分身](../../../cards/docs-bugkuctf-re-z-volcano-csdn-bugku.md) | BugkuCTF RE部分题解 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [bugkuCTF平台逆向题第一道Easy_vb题解_iqiqiya的博客-CSDN博客_bugkueasy_vb](../../../cards/docs-bugkuctf-easy-vb-iqiqiya-csdn-bugkueasy-vb.md) | bugkuCTF平台逆向题第一道Easy |  | http-analysis, osint, reverse-engineering, web-exploitation |
| [bugkuCTF平台逆向题第二道Easy_Re题解_iqiqiya的博客-CSDN博客_easy_re](../../../cards/docs-bugkuctf-easy-re-iqiqiya-csdn-easy-re.md) | bugkuCTF平台逆向题第二道Easy |  | http-analysis, osint, reverse-engineering, web-exploitation |
| [BUUCTF reverse：[GXYCTF2019]luck_guy,findit,简单注册器题解_June_gjy的博客-CSDN博客](../../../cards/docs-buuctf-reverse-gxyctf2019-luck-guy-findit-june-gjy-csdn.md) | BUUCTF reverse：[GXYCTF2019]luck |  | classical-crypto, crypto-analysis, http-analysis, integer-overflow |
| [buu逆向刷题（二）_北风~的博客-CSDN博客](../../../cards/docs-buu-csdn.md) | buu逆向刷题（二） |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [CTF-安卓逆向入门题目_Thunder_J的博客-CSDN博客_ctf 安卓逆向](../../../cards/docs-ctf-thunder-j-csdn-ctf.md) | CTF |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [NYIST练习 题解（一）_pipixia233333的博客-CSDN博客](../../../cards/docs-nyist-pipixia233333-csdn.md) | NYIST练习 题解（一） |  | file-inclusion |
| [PWN flag [pwnable.kr]CTF writeup题解系列4_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-flag-pwnable-kr-ctf-writeup-4-3ric5r-csdn.md) | PWN flag [pwnable.kr]CTF writeup题解系列4 |  | binary-exploitation, command-injection, http-analysis, password-cracking |
| [XL----逆向入门新手题解_颜又舞的博客-CSDN博客](../../../cards/docs-xl-csdn.md) | XL |  | file-inclusion, malware-static, reverse-engineering, stego-extraction |
| [【CTF reverse】逆向入门题解集合+逆向相关软件安装_hans774882968的博客-CSDN博客](../../../cards/docs-ctf-reverse-hans774882968-csdn.md) | 【CTF reverse】逆向入门题解集合+逆向相关软件安装 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [深信服杯 CTF 线上 逆向题解_pipixia233333的博客-CSDN博客](../../../cards/docs-ctf-pipixia233333-csdn.md) | 深信服杯 CTF 线上 逆向题解 |  | classical-crypto, crypto-analysis, encoding-analysis, file-inclusion |
