# Pwn / ciphertext

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| binary-exploitation | 12 | http evidence extraction, reverse engineering, checksec-driven evidence lookup, stack control exploitation, netcat-driven evidence lookup |
| web-exploitation | 12 | http evidence extraction, reverse engineering, checksec-driven evidence lookup, stack control exploitation, netcat-driven evidence lookup |
| crypto-analysis | 10 | http evidence extraction, reverse engineering, stack control exploitation, checksec-driven evidence lookup, memory artifact analysis |
| encoding-analysis | 10 | http evidence extraction, reverse engineering, stack control exploitation, checksec-driven evidence lookup, waf bypass |
| ret2libc | 8 | http evidence extraction, reverse engineering, stack control exploitation, checksec-driven evidence lookup, netcat-driven evidence lookup |
| classical-crypto | 7 | http evidence extraction, reverse engineering, stack control exploitation, checksec-driven evidence lookup, cipher decoding |
| reverse-engineering | 7 | reverse engineering, http evidence extraction, stack control exploitation, checksec-driven evidence lookup, cipher decoding |
| waf-bypass | 7 | http evidence extraction, reverse engineering, waf bypass, checksec-driven evidence lookup, stack control exploitation |
| command-injection | 6 | http evidence extraction, checksec-driven evidence lookup, reverse engineering, stack control exploitation, command execution path |
| stack-overflow | 5 | http evidence extraction, stack control exploitation, checksec-driven evidence lookup, reverse engineering, cipher decoding |
| http-analysis | 4 | http evidence extraction, reverse engineering, stack control exploitation, checksec-driven evidence lookup, cipher decoding |
| misc-analysis | 4 | http evidence extraction, reverse engineering, checksec-driven evidence lookup, cipher decoding, constraint solving |
| format-string | 3 | http evidence extraction, command execution path, reverse engineering, waf bypass, checksec-driven evidence lookup |
| integer-overflow | 3 | http evidence extraction, memory artifact analysis, reverse engineering, checksec-driven evidence lookup, command execution path |
| qr-analysis | 3 | http evidence extraction, checksec-driven evidence lookup, reverse engineering, stack control exploitation, cipher decoding |
| ret2text | 3 | http evidence extraction, stack control exploitation, checksec-driven evidence lookup, reverse engineering, command execution path |
| symbolic-execution | 3 | reverse engineering, http evidence extraction, checksec-driven evidence lookup, cipher decoding, constraint solving |
| image-analysis | 2 | http evidence extraction, memory artifact analysis, checksec-driven evidence lookup, cipher decoding, constraint solving |
| osint | 2 | reverse engineering, checksec-driven evidence lookup, http evidence extraction, stack control exploitation, waf bypass |
| php-tricks | 2 | http evidence extraction, cipher decoding, command execution path, constraint solving, cyberchef-driven evidence lookup |
| service-enumeration | 2 | http evidence extraction, checksec-driven evidence lookup, command execution path, file inclusion exploitation, memory artifact analysis |
| browser-forensics | 1 | checksec-driven evidence lookup, file inclusion exploitation, http evidence extraction, memory artifact analysis |
| dns-analysis | 1 | checksec-driven evidence lookup, http evidence extraction, reverse engineering, waf bypass |
| file-inclusion | 1 | checksec-driven evidence lookup, file inclusion exploitation, http evidence extraction, memory artifact analysis |
| sql-injection | 1 | cipher decoding, constraint solving, http evidence extraction, memory artifact analysis, reverse engineering |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 10 |
| reverse engineering | 7 |
| checksec-driven evidence lookup | 5 |
| stack control exploitation | 5 |
| netcat-driven evidence lookup | 4 |
| waf bypass | 4 |
| memory artifact analysis | 3 |
| cipher decoding | 2 |
| command execution path | 2 |
| constraint solving | 1 |
| cyberchef-driven evidence lookup | 1 |
| evidence lookup | 1 |
| file inclusion exploitation | 1 |
| format-string control path | 1 |
| gdb-driven evidence lookup | 1 |
| incident timeline reconstruction | 1 |
| integer-overflow bypass | 1 |
| ropgadget-driven evidence lookup | 1 |
| sql injection exploitation | 1 |
| timeline reconstruction | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [2021DNUICTF（东软杯CTF）的几个签到题writeup_Q1X1的博客-CSDN博客](../../../cards/docs-2021dnuictf-ctf-writeup-q1x1-csdn.md) | 2021DNUICTF（东软杯CTF）的几个签到题writeup |  | binary-exploitation, crypto-analysis, encoding-analysis, misc-analysis |
| [BUUCTF ciscn_2019_c_1__N1rvana_的博客-CSDN博客](../../../cards/docs-buuctf-ciscn-2019-c-1-n1rvana-csdn.md) | BUUCTF ciscn |  | binary-exploitation, crypto-analysis, encoding-analysis, http-analysis |
| [CTF pwn 方向部分题解_普通网友的博客-CSDN博客_ctfpwn方向比赛题目及解析](../../../cards/docs-ctf-pwn-csdn-ctfpwn.md) | CTF pwn 方向部分题解 |  | binary-exploitation, classical-crypto, command-injection, encoding-analysis |
| [GXYCTF部分详细题解_合天网安实验室的博客-CSDN博客](../../../cards/docs-gxyctf-csdn.md) | GXYCTF部分详细题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [HgameCTF(week1)-RE,PWN题解析_合天网安实验室的博客-CSDN博客](../../../cards/docs-hgamectf-week1-re-pwn-csdn.md) | HgameCTF(week1) |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [PWN random [pwnable.kr]CTF writeup题解系列6_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-random-pwnable-kr-ctf-writeup-6-3ric5r-csdn.md) | PWN random [pwnable.kr]CTF writeup题解系列6 |  | binary-exploitation, browser-forensics, command-injection, crypto-analysis |
| [troia_server [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列27(未完待续）_3riC5r的博客-CSDN博客](../../../cards/docs-troia-server-xctf-pwn-ctf-writeup-27-3ric5r-csdn.md) | troia |  | binary-exploitation, crypto-analysis, integer-overflow, reverse-engineering |
| [【CTF题解NO.00001】西安电子科技大学网络与信息安全学院2020年网络空间安全专业实验班选拔考试 - write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00001-2020-write-up-by-arttnba3-arttnba3-csdn.md) | docs |  | binary-exploitation, classical-crypto, dns-analysis, encoding-analysis |
| [【CTF题解NO.00003】moeCTF 2020 - official write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00003-moectf-2020-official-write-up-by-arttnba3-arttnba3-csdn.md) | 【CTF题解NO.00003】moeCTF 2020 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [【CTF题解NO.00004】BUUCTF/BUUOJ - Pwn write up by arttnb3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00004-buuctf-buuoj-pwn-write-up-by-arttnb3-arttnba3-csdn.md) | 【CTF题解NO.00004】BUUCTF/BUUOJ |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [【CTF题解NO.00007】VNCTF2021 - pwn - write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00007-vnctf2021-pwn-write-up-by-arttnba3-arttnba3-csdn.md) | 【CTF题解NO.00007】VNCTF2021 |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [厄了吗](../../../cards/pwn-gccctf-2025.md) | GCCCTF 2025 |  | binary-exploitation, command-injection, crypto-analysis, encoding-analysis |
