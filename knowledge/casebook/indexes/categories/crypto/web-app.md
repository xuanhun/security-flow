# Crypto / web-app

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| crypto-analysis | 48 | cipher decoding, netcat-driven evidence lookup, http evidence extraction, reverse engineering, evidence lookup |
| web-exploitation | 43 | cipher decoding, http evidence extraction, netcat-driven evidence lookup, evidence lookup, command execution path |
| http-analysis | 39 | cipher decoding, netcat-driven evidence lookup, http evidence extraction, reverse engineering, command execution path |
| classical-crypto | 36 | cipher decoding, netcat-driven evidence lookup, http evidence extraction, reverse engineering, command execution path |
| encoding-analysis | 36 | cipher decoding, netcat-driven evidence lookup, http evidence extraction, reverse engineering, command execution path |
| php-tricks | 24 | cipher decoding, netcat-driven evidence lookup, http evidence extraction, command execution path, evidence lookup |
| qr-analysis | 15 | cipher decoding, http evidence extraction, reverse engineering, netcat-driven evidence lookup, command execution path |
| binary-exploitation | 14 | cipher decoding, reverse engineering, http evidence extraction, command execution path, netcat-driven evidence lookup |
| command-injection | 14 | cipher decoding, command execution path, netcat-driven evidence lookup, reverse engineering, file inclusion exploitation |
| file-inclusion | 12 | file inclusion exploitation, netcat-driven evidence lookup, cipher decoding, http evidence extraction, reverse engineering |
| misc-analysis | 12 | cipher decoding, netcat-driven evidence lookup, http evidence extraction, command execution path, stego extraction |
| image-analysis | 9 | cipher decoding, http evidence extraction, constraint solving, netcat-driven evidence lookup, stego extraction |
| reverse-engineering | 9 | reverse engineering, cipher decoding, http evidence extraction, command execution path, file inclusion exploitation |
| symbolic-execution | 9 | cipher decoding, constraint solving, reverse engineering, command execution path, file inclusion exploitation |
| service-enumeration | 4 | cipher decoding, http evidence extraction, reverse engineering, constraint solving, file inclusion exploitation |
| dns-analysis | 3 | cipher decoding, netcat-driven evidence lookup, constraint solving, file inclusion exploitation, http evidence extraction |
| waf-bypass | 3 | cipher decoding, reverse engineering, waf bypass, command execution path, detect-it-easy-driven evidence lookup |
| mobile-forensics | 2 | reverse engineering, command execution path, constraint solving, file inclusion exploitation, ida-driven evidence lookup |
| network-forensics | 2 | reverse engineering, cipher decoding, command execution path, http evidence extraction, stego extraction |
| osint | 2 | http evidence extraction, cipher decoding, constraint solving, file inclusion exploitation, netcat-driven evidence lookup |
| ret2libc | 2 | file inclusion exploitation, command execution path, gdb-driven evidence lookup, reverse engineering |
| siem-query | 2 | reverse engineering, cipher decoding, command execution path, constraint solving, file inclusion exploitation |
| sql-injection | 2 | cipher decoding, http evidence extraction, detect-it-easy-driven evidence lookup, evidence lookup, stego extraction |
| stego-extraction | 2 | angr-driven evidence lookup, cipher decoding, command execution path, constraint solving, http evidence extraction |
| traffic-analysis | 2 | reverse engineering, cipher decoding, command execution path, http evidence extraction, stego extraction |
| xss | 2 | cipher decoding, http evidence extraction, constraint solving, netcat-driven evidence lookup, reverse engineering |
| browser-forensics | 1 | file inclusion exploitation, gdb-driven evidence lookup |
| deserialization | 1 | cipher decoding, http evidence extraction, reverse engineering, stego extraction |
| integer-overflow | 1 | command execution path, file inclusion exploitation, reverse engineering |
| malware-static | 1 | angr-driven evidence lookup, cipher decoding, constraint solving, http evidence extraction |
| memory-forensics | 1 | angr-driven evidence lookup, cipher decoding, constraint solving, http evidence extraction |
| privilege-escalation | 1 | file inclusion exploitation, gdb-driven evidence lookup |
| ssti | 1 | angr-driven evidence lookup, cipher decoding, constraint solving, http evidence extraction |
| stream-cipher | 1 | angr-driven evidence lookup, cipher decoding, constraint solving, http evidence extraction |

## Route Types

| Route type | Cases |
| --- | --- |
| cipher decoding | 39 |
| netcat-driven evidence lookup | 24 |
| http evidence extraction | 21 |
| evidence lookup | 9 |
| file inclusion exploitation | 9 |
| reverse engineering | 9 |
| command execution path | 8 |
| constraint solving | 5 |
| stego extraction | 4 |
| indicator enrichment | 3 |
| burp-driven evidence lookup | 2 |
| pwntools-driven evidence lookup | 2 |
| waf bypass | 2 |
| angr-driven evidence lookup | 1 |
| detect-it-easy-driven evidence lookup | 1 |
| gdb-driven evidence lookup | 1 |
| ida-driven evidence lookup | 1 |
| xss route | 1 |
| 无-driven evidence lookup | 1 |
| 随波逐流6.6 [社会主义核心价值观密码解码工具] https:-driven evidence lookup | 1 |
| 随波逐流6.6-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [*ctf box题解_Cosmop01itan的博客-CSDN博客](../../../cards/docs-ctf-box-cosmop01itan-csdn.md) | *ctf box题解 |  | crypto-analysis, encoding-analysis, file-inclusion |
| [[buuctf]crypto刷题学习记录（1-22）_hyxyan的博客-CSDN博客](../../../cards/docs-buuctf-crypto-1-22-hyxyan-csdn.md) | buuctf |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [[SDCTF 2022]Case64AR](../../../cards/crypto-sdctf-2022-case64ar.md) | SDCTF 2022 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [[SWPUCTF 2021 新生赛]ez_caesar](../../../cards/crypto-swpuctf-2021-ez-caesar.md) | SWPUCTF 2021 新生赛 | 简单 | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [[SWPUCTF 2022 新生赛]什锦](../../../cards/crypto-swpuctf-2022.md) | SWPUCTF 2022 新生赛 | 中等 | crypto-analysis, encoding-analysis, http-analysis, php-tricks |
| [[鹤城杯 2021]A_CRYPTO](../../../cards/crypto-2021-a-crypto.md) | 鹤城杯 2021 | 中等 | classical-crypto, crypto-analysis, http-analysis, web-exploitation |
| [AGCTF WP_weixin_52631365的博客-CSDN博客](../../../cards/docs-agctf-wp-weixin-52631365-csdn.md) | AGCTF WP |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [asc量子计算机,[推荐][原创]CTF-RSA常见题型、思路及解法_何壁咚的博客-CSDN博客](../../../cards/docs-asc-ctf-rsa-csdn.md) | asc量子计算机,[推荐][原创]CTF |  | classical-crypto, crypto-analysis, encoding-analysis, file-inclusion |
| [BUUCTF RSA题目全解1_宁嘉的博客-CSDN博客_buuctf rsa1](../../../cards/docs-buuctf-rsa-1-csdn-buuctf-rsa1.md) | BUUCTF RSA题目全解1 |  | crypto-analysis, encoding-analysis, http-analysis, php-tricks |
| [BUUCTF RSA题目全解3_宁嘉的博客-CSDN博客_buuctf rsa3](../../../cards/docs-buuctf-rsa-3-csdn-buuctf-rsa3.md) | BUUCTF RSA题目全解3 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [BUUCTF-Crypto-MD5题解_ASSOINT的博客-CSDN博客](../../../cards/docs-buuctf-crypto-md5-assoint-csdn.md) | BUUCTF |  | crypto-analysis, http-analysis, php-tricks, web-exploitation |
| [BUUCTF-Crypto-password+变异凯撒题解_ASSOINT的博客-CSDN博客_变异凯撒密码解密](../../../cards/docs-buuctf-crypto-password-assoint-csdn.md) | BUUCTF |  | classical-crypto, crypto-analysis, file-inclusion |
| [BUUCTF-Crypto-rabbit+篱笆墙上的影子（栅栏密码）+RSA题解_ASSOINT的博客-CSDN博客](../../../cards/docs-buuctf-crypto-rabbit-rsa-assoint-csdn.md) | BUUCTF |  | classical-crypto, crypto-analysis, http-analysis, web-exploitation |
| [BUUCTF-Crypto-一眼就解密题解_ASSOINT的博客-CSDN博客_buuctf 一眼就解密](../../../cards/docs-buuctf-crypto-assoint-csdn-buuctf.md) | BUUCTF |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [BUUCTF-Crypto-变异凯撒解题思路_Georgeiweb的博客-CSDN博客_buuctf 变异凯撒](../../../cards/docs-buuctf-crypto-georgeiweb-csdn-buuctf.md) | BUUCTF |  | classical-crypto, crypto-analysis, web-exploitation |
| [BUUCTF-Crypto-摩丝题解_ASSOINT的博客-CSDN博客_buuctf 摩丝](../../../cards/docs-buuctf-crypto-assoint-csdn-buuctf.md) | BUUCTF |  | crypto-analysis, http-analysis, web-exploitation |
| [BUUCTF-Crypto-看我回旋踢题解_ASSOINT的博客-CSDN博客_看我回旋踢](../../../cards/docs-buuctf-crypto-assoint-csdn.md) | BUUCTF |  | classical-crypto, crypto-analysis, http-analysis, qr-analysis |
| [BUUCTF-Crypto-签到题解（base64）_ASSOINT的博客-CSDN博客](../../../cards/docs-buuctf-crypto-base64-assoint-csdn.md) | BUUCTF |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [BUUCTF中CrackRTF题详细解法_F10W3RDANC3的博客-CSDN博客](../../../cards/docs-buuctf-crackrtf-f10w3rdanc3-csdn.md) | BUUCTF中CrackRTF题详细解法 |  | command-injection, crypto-analysis, encoding-analysis, http-analysis |
| [CTF show 萌新区解题报告 （一）_Vayn3的博客-CSDN博客_ctf解题报告](../../../cards/docs-ctf-show-vayn3-csdn-ctf.md) | CTF show 萌新区解题报告 （一） |  | classical-crypto, crypto-analysis, encoding-analysis, image-analysis |
| [CTF show 萌新区解题报告 （三）_Vayn3的博客-CSDN博客](../../../cards/docs-ctf-show-vayn3-csdn.md) | CTF show 萌新区解题报告 （三） |  | classical-crypto, crypto-analysis, encoding-analysis, image-analysis |
| [CTF-加密与解密（三）_红烧兔纸的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | CTF |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [CTF-加密与解密（十八）_红烧兔纸的博客-CSDN博客_曼联加密](../../../cards/docs-ctf-csdn.md) | CTF |  | classical-crypto, crypto-analysis, encoding-analysis |
| [ctf.show RSA入门题目题解若干_Rabbit_Gray的博客-CSDN博客_ctf中rsa实验题解析](../../../cards/docs-ctf-show-rsa-rabbit-gray-csdn-ctf-rsa.md) | ctf.show RSA入门题目题解若干 |  | crypto-analysis, dns-analysis, http-analysis, qr-analysis |
| [CTF中常见密码题解密网站总结_greedy-hat的博客-CSDN博客_当铺密码在线解密](../../../cards/docs-ctf-greedy-hat-csdn.md) | CTF中常见密码题解密网站总结 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [ctf刷题日记_AndrewMe8211的博客-CSDN博客](../../../cards/docs-ctf-andrewme8211-csdn.md) | ctf刷题日记 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [CTF基础解题_destin_love的博客-CSDN博客_ctf解题](../../../cards/docs-ctf-destin-love-csdn-ctf.md) | CTF基础解题 |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [ctf学习经历——极客部分题解_RoleMee的博客-CSDN博客](../../../cards/docs-ctf-rolemee-csdn.md) | ctf学习经历——极客部分题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [CTF密码学(crypto)题目easychallenge解题过程总结_hippotomons的博客-CSDN博客_easychallenge](../../../cards/docs-ctf-crypto-easychallenge-hippotomons-csdn-easychallenge.md) | CTF密码学(crypto)题目easychallenge解题过程总结 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [CTF密码学密文脚本解密及WP（凯撒解密）_weixin_33849942的博客-CSDN博客](../../../cards/docs-ctf-wp-weixin-33849942-csdn.md) | CTF密码学密文脚本解密及WP（凯撒解密） |  | classical-crypto, crypto-analysis, http-analysis, web-exploitation |
| [ctf密码学特殊的编码和解密_落雪wink的博客-CSDN博客_编码](../../../cards/docs-ctf-wink-csdn.md) | ctf密码学特殊的编码和解密 |  | classical-crypto, command-injection, crypto-analysis, http-analysis |
| [decrypt-WEB-BugKuCTF_Alasding的博客-CSDN博客](../../../cards/docs-decrypt-web-bugkuctf-alasding-csdn.md) | decrypt |  | classical-crypto, crypto-analysis, encoding-analysis, php-tricks |
| [Jarvis OJ 刷题题解 RE_pipixia233333的博客-CSDN博客](../../../cards/docs-jarvis-oj-re-pipixia233333-csdn.md) | Jarvis OJ 刷题题解 RE |  | binary-exploitation, classical-crypto, crypto-analysis, dns-analysis |
| [PWN fd [pwnable.kr]CTF writeup题解系列1_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-fd-pwnable-kr-ctf-writeup-1-3ric5r-csdn.md) | PWN fd [pwnable.kr]CTF writeup题解系列1 |  | binary-exploitation, browser-forensics, command-injection, crypto-analysis |
| [python md5解密_CTF-敲错键盘的md5解密，python通解_weixin_39616416的博客-CSDN博客](../../../cards/docs-python-md5-ctf-md5-python-weixin-39616416-csdn.md) | python md5解密 |  | crypto-analysis, encoding-analysis, http-analysis, php-tricks |
| [rgss加密文件解包器_OGeek线上CTF挑战赛逆向及加密类赛题详细Write Up_weixin_39751871的博客-CSDN博客](../../../cards/docs-rgss-ogeek-ctf-write-up-weixin-39751871-csdn.md) | rgss加密文件解包器 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [RSA算法原理及CTF解题_WHOAMIAnony的博客-CSDN博客](../../../cards/docs-rsa-ctf-whoamianony-csdn.md) | RSA算法原理及CTF解题 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [“百度杯”CTF比赛 十一月场(Misc)_andiao1218的博客-CSDN博客](../../../cards/docs-ctf-misc-andiao1218-csdn.md) | “百度杯”CTF比赛 十一月场(Misc) |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [【CTF WriteUp】201909广东强网杯部分题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-201909-csdn.md) | 【CTF WriteUp】201909广东强网杯部分题解 |  | binary-exploitation, crypto-analysis, encoding-analysis, http-analysis |
| [【CTF WriteUp】2020天翼杯Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF WriteUp】2020天翼杯Crypto题解 |  | crypto-analysis, http-analysis, php-tricks, qr-analysis |
| [【CTF WriteUp】2021 starCTF部分Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2021-starctf-crypto-csdn.md) | 【CTF WriteUp】2021 starCTF部分Crypto题解 |  | binary-exploitation, crypto-analysis, encoding-analysis, http-analysis |
| [【CTF WriteUp】UTCTF 2020部分题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-utctf-2020-csdn.md) | 【CTF WriteUp】UTCTF 2020部分题解 |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [【moeCTF题解-0x04】Crypto_框架主义者的博客-CSDN博客](../../../cards/docs-moectf-0x04-crypto-csdn.md) | 【moeCTF题解 |  | classical-crypto, crypto-analysis, encoding-analysis, file-inclusion |
| [再不学点现代密码，CTF就Hold不住啦！_合天网安实验室的博客-CSDN博客](../../../cards/docs-ctf-hold-csdn.md) | 再不学点现代密码，CTF就Hold不住啦！ |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [大连海事大学第一届“启航杯”DLMU CTF部分题解_ℳ๓₯㎕₯㎕ζั的博客-CSDN博客](../../../cards/docs-dlmu-ctf-csdn.md) | 大连海事大学第一届“启航杯”DLMU CTF部分题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [实验吧 部分逆向题解_pipixia233333的博客-CSDN博客](../../../cards/docs-pipixia233333-csdn.md) | 实验吧 部分逆向题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [实验吧CTF练习题---WEB---FALSE解析_dingbai2663的博客-CSDN博客](../../../cards/docs-ctf-web-false-dingbai2663-csdn.md) | 实验吧CTF练习题 |  | command-injection, php-tricks, web-exploitation |
| [百度杯”CTF比赛（十一月场)_Root__Liu的博客-CSDN博客](../../../cards/docs-ctf-root-liu-csdn.md) | 百度杯”CTF比赛（十一月场) |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [看雪.京东 2018CTF 第十二题 破解之道_大灬白的博客-CSDN博客](../../../cards/docs-2018ctf-csdn.md) | 看雪.京东 2018CTF 第十二题 破解之道 |  | file-inclusion |
| [第6篇：基础入门~加密编码算法_廖一语山的博客-CSDN博客](../../../cards/docs-6-csdn.md) | 第6篇：基础入门~加密编码算法 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [题解 贪吃蛇_weixin_30566063的博客-CSDN博客](../../../cards/docs-weixin-30566063-csdn.md) | 题解 贪吃蛇 |  | file-inclusion, osint |
