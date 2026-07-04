# Web / email

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| http-analysis | 12 | http evidence extraction, evidence lookup, burp-driven evidence lookup, file inclusion exploitation, netcat-driven evidence lookup |
| web-exploitation | 12 | http evidence extraction, evidence lookup, burp-driven evidence lookup, file inclusion exploitation, netcat-driven evidence lookup |
| command-injection | 8 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, netcat-driven evidence lookup, detect-it-easy-driven evidence lookup |
| file-upload | 8 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, deserialization chain, detect-it-easy-driven evidence lookup |
| php-tricks | 8 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, deserialization chain, detect-it-easy-driven evidence lookup |
| sql-injection | 8 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, sql injection exploitation, detect-it-easy-driven evidence lookup |
| waf-bypass | 8 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, deserialization chain, detect-it-easy-driven evidence lookup |
| classical-crypto | 7 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, detect-it-easy-driven evidence lookup, netcat-driven evidence lookup |
| crypto-analysis | 7 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, detect-it-easy-driven evidence lookup, netcat-driven evidence lookup |
| encoding-analysis | 7 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, detect-it-easy-driven evidence lookup, sql injection exploitation |
| file-inclusion | 7 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, detect-it-easy-driven evidence lookup, sql injection exploitation |
| deserialization | 6 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, deserialization chain, detect-it-easy-driven evidence lookup |
| ret2libc | 5 | http evidence extraction, file inclusion exploitation, burp-driven evidence lookup, detect-it-easy-driven evidence lookup, command execution path |
| browser-forensics | 4 | http evidence extraction, burp-driven evidence lookup, file inclusion exploitation, detect-it-easy-driven evidence lookup, dns pivot |
| ssti | 4 | http evidence extraction, file inclusion exploitation, detect-it-easy-driven evidence lookup, ssti exploitation, burp-driven evidence lookup |
| dns-analysis | 3 | detect-it-easy-driven evidence lookup, file inclusion exploitation, http evidence extraction, deserialization chain, dns pivot |
| binary-exploitation | 2 | file inclusion exploitation, http evidence extraction, burp-driven evidence lookup, detect-it-easy-driven evidence lookup, dns pivot |
| email-header-analysis | 2 | burp-driven evidence lookup, http evidence extraction, waf bypass |
| qr-analysis | 2 | detect-it-easy-driven evidence lookup, dns pivot, evidence lookup, file inclusion exploitation, http evidence extraction |
| symbolic-execution | 2 | file inclusion exploitation, http evidence extraction, burp-driven evidence lookup, detect-it-easy-driven evidence lookup, dns pivot |
| jwt-analysis | 1 | detect-it-easy-driven evidence lookup, dns pivot, file inclusion exploitation, http evidence extraction, sql injection exploitation |
| mobile-forensics | 1 | evidence lookup |
| service-enumeration | 1 | detect-it-easy-driven evidence lookup, dns pivot, file inclusion exploitation, http evidence extraction, sql injection exploitation |
| timeline-analysis | 1 | detect-it-easy-driven evidence lookup, dns pivot, file inclusion exploitation, http evidence extraction, sql injection exploitation |
| web-enumeration | 1 | deserialization chain, detect-it-easy-driven evidence lookup, file inclusion exploitation, http evidence extraction, ssti exploitation |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 10 |
| evidence lookup | 4 |
| burp-driven evidence lookup | 3 |
| file inclusion exploitation | 3 |
| netcat-driven evidence lookup | 3 |
| sql injection exploitation | 3 |
| ssti exploitation | 3 |
| command execution path | 2 |
| deserialization chain | 2 |
| detect-it-easy-driven evidence lookup | 2 |
| waf bypass | 2 |
| cipher decoding | 1 |
| credential discovery | 1 |
| dns pivot | 1 |
| file upload bypass | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [[0CTF 2016] piapiapia 题解_lonmar~的博客-CSDN博客](../../../cards/docs-0ctf-2016-piapiapia-lonmar-csdn.md) | 0CTF 2016 |  | deserialization, file-upload, http-analysis, php-tricks |
| [ApacheCN CTF 知识库](../../../cards/readme.md) | ApacheCN CTF |  | http-analysis, web-exploitation |
| [BugKu题解备注（1）_s11show_163的博客-CSDN博客](../../../cards/docs-bugku-1-s11show-163-csdn.md) | BugKu题解备注（1） |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [buuctf web小结_绿冰壶的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | buuctf web小结 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [BUUCTF寒假刷题-Web_深海神奇舰舰长的博客-CSDN博客](../../../cards/docs-buuctf-web-csdn.md) | BUUCTF寒假刷题 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [BUUCTF解题十一道(04)_Sprint#51264的博客-CSDN博客](../../../cards/docs-buuctf-04-sprint-51264-csdn.md) | BUUCTF解题十一道(04) |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF-rootme 题解之Hash - SHA-2_weixin_30237719的博客-CSDN博客](../../../cards/docs-ctf-rootme-hash-sha-2-weixin-30237719-csdn.md) | CTF |  | command-injection, crypto-analysis, http-analysis, php-tricks |
| [CTF中文件上传题目整理总结_xiaosec的博客-CSDN博客_文件上传ctf题目](../../../cards/docs-ctf-xiaosec-csdn-ctf.md) | CTF中文件上传题目整理总结 |  | dns-analysis, encoding-analysis, file-inclusion, file-upload |
| [CTF解题-Bugku_Web_WriteUp (上）_Tr0e的博客-CSDN博客_bugku web writeup](../../../cards/docs-ctf-bugku-web-writeup-tr0e-csdn-bugku-web-writeup.md) | CTF解题 |  | classical-crypto, command-injection, crypto-analysis, deserialization |
| [CTF论剑场web解题_梳刘海的杰瑞的博客-CSDN博客](../../../cards/docs-ctf-web-csdn.md) | CTF论剑场web解题 |  | classical-crypto, command-injection, encoding-analysis, file-inclusion |
| [D3CTF 8-bit解题详解_N0Tai1学习又咕了的博客-CSDN博客](../../../cards/docs-d3ctf-8-bit-n0tai1-csdn.md) | D3CTF 8 |  | browser-forensics, classical-crypto, command-injection, crypto-analysis |
| [攻防世界-web-unfinish-从0到1的解题历程writeup_CTF小白的博客-CSDN博客](../../../cards/docs-web-unfinish-0-1-writeup-ctf-csdn.md) | 攻防世界 |  | http-analysis, sql-injection, web-exploitation |
