# Crypto / ciphertext

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| crypto-analysis | 106 | cipher decoding, http evidence extraction, netcat-driven evidence lookup, evidence lookup, reverse engineering |
| encoding-analysis | 82 | cipher decoding, http evidence extraction, netcat-driven evidence lookup, evidence lookup, reverse engineering |
| classical-crypto | 66 | cipher decoding, netcat-driven evidence lookup, http evidence extraction, evidence lookup, reverse engineering |
| web-exploitation | 43 | cipher decoding, http evidence extraction, netcat-driven evidence lookup, evidence lookup, reverse engineering |
| http-analysis | 42 | cipher decoding, netcat-driven evidence lookup, http evidence extraction, reverse engineering, evidence lookup |
| php-tricks | 36 | cipher decoding, http evidence extraction, netcat-driven evidence lookup, evidence lookup, reverse engineering |
| qr-analysis | 26 | cipher decoding, http evidence extraction, netcat-driven evidence lookup, reverse engineering, command execution path |
| binary-exploitation | 22 | cipher decoding, http evidence extraction, netcat-driven evidence lookup, reverse engineering, command execution path |
| misc-analysis | 16 | cipher decoding, netcat-driven evidence lookup, http evidence extraction, command execution path, evidence lookup |
| reverse-engineering | 15 | reverse engineering, cipher decoding, http evidence extraction, command execution path, constraint solving |
| command-injection | 14 | cipher decoding, netcat-driven evidence lookup, command execution path, reverse engineering, http evidence extraction |
| symbolic-execution | 13 | cipher decoding, constraint solving, http evidence extraction, netcat-driven evidence lookup, reverse engineering |
| image-analysis | 11 | cipher decoding, http evidence extraction, netcat-driven evidence lookup, constraint solving, stego extraction |
| file-inclusion | 8 | cipher decoding, file inclusion exploitation, reverse engineering, http evidence extraction, netcat-driven evidence lookup |
| dns-analysis | 4 | cipher decoding, constraint solving, http evidence extraction, netcat-driven evidence lookup, reverse engineering |
| waf-bypass | 4 | reverse engineering, waf bypass, cipher decoding, command execution path, detect-it-easy-driven evidence lookup |
| mobile-forensics | 3 | reverse engineering, cipher decoding, command execution path, constraint solving, file inclusion exploitation |
| network-forensics | 3 | cipher decoding, reverse engineering, command execution path, http evidence extraction, netcat-driven evidence lookup |
| service-enumeration | 3 | cipher decoding, http evidence extraction, reverse engineering, constraint solving, indicator enrichment |
| stego-extraction | 3 | cipher decoding, http evidence extraction, angr-driven evidence lookup, command execution path, constraint solving |
| stream-cipher | 3 | cipher decoding, http evidence extraction, angr-driven evidence lookup, constraint solving, dns pivot |
| traffic-analysis | 3 | cipher decoding, reverse engineering, command execution path, http evidence extraction, netcat-driven evidence lookup |
| xss | 3 | cipher decoding, http evidence extraction, netcat-driven evidence lookup, constraint solving, indicator enrichment |
| malware-static | 2 | cipher decoding, http evidence extraction, angr-driven evidence lookup, constraint solving, credential discovery |
| memory-forensics | 2 | cipher decoding, http evidence extraction, angr-driven evidence lookup, constraint solving, credential discovery |
| siem-query | 2 | reverse engineering, cipher decoding, command execution path, constraint solving, file inclusion exploitation |
| sql-injection | 2 | cipher decoding, http evidence extraction, detect-it-easy-driven evidence lookup, evidence lookup, stego extraction |
| browser-forensics | 1 | cipher decoding, evidence lookup |
| deserialization | 1 | cipher decoding, http evidence extraction, reverse engineering, stego extraction |
| integer-overflow | 1 | command execution path, file inclusion exploitation, reverse engineering |
| osint | 1 | cipher decoding, constraint solving, http evidence extraction, reverse engineering |
| password-cracking | 1 | cipher decoding, credential discovery, http evidence extraction, john-driven evidence lookup, netcat-driven evidence lookup |
| privilege-escalation | 1 | credential discovery, evidence lookup |
| ret2libc | 1 | command execution path, file inclusion exploitation, reverse engineering |
| ssti | 1 | angr-driven evidence lookup, cipher decoding, constraint solving, http evidence extraction |

## Route Types

| Route type | Cases |
| --- | --- |
| cipher decoding | 98 |
| http evidence extraction | 50 |
| netcat-driven evidence lookup | 49 |
| evidence lookup | 37 |
| reverse engineering | 14 |
| constraint solving | 8 |
| command execution path | 7 |
| indicator enrichment | 6 |
| stego extraction | 6 |
| file inclusion exploitation | 5 |
| burp-driven evidence lookup | 4 |
| detect-it-easy-driven evidence lookup | 3 |
| pwntools-driven evidence lookup | 3 |
| waf bypass | 3 |
| angr-driven evidence lookup | 2 |
| credential discovery | 2 |
| ida-driven evidence lookup | 2 |
| dns pivot | 1 |
| john-driven evidence lookup | 1 |
| memory artifact analysis | 1 |
| xss route | 1 |
| z3-driven evidence lookup | 1 |
| 无-driven evidence lookup | 1 |
| 随波逐流6.6 [社会主义核心价值观密码解码工具] https:-driven evidence lookup | 1 |
| 随波逐流6.6-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [[buuctf]crypto刷题学习记录（1-22）_hyxyan的博客-CSDN博客](../../../cards/docs-buuctf-crypto-1-22-hyxyan-csdn.md) | buuctf |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [[DASCTF 2020 四月春季赛] not_RSA 题解_随缘懂点密码学的博客-CSDN博客](../../../cards/docs-dasctf-2020-not-rsa-csdn.md) | DASCTF 2020 四月春季赛 |  | crypto-analysis |
| [[DASCTF八月挑战赛]easymath题解_mortal15的博客-CSDN博客](../../../cards/docs-dasctf-easymath-mortal15-csdn.md) | DASCTF八月挑战赛 |  | crypto-analysis |
| [[De1CTF2019]babyrsa的wp_fevergun的博客-CSDN博客](../../../cards/docs-de1ctf2019-babyrsa-wp-fevergun-csdn.md) | De1CTF2019 |  | crypto-analysis |
| [[GCCCTF 2025]伊莫鸡](../../../cards/crypto-gccctf-2025.md) | GCCCTF 2025 |  | classical-crypto, crypto-analysis, encoding-analysis, qr-analysis |
| [[GCCCTF 2025]密钥危机](../../../cards/crypto-gccctf-2025.md) | GCCCTF 2025 |  | crypto-analysis, encoding-analysis, reverse-engineering |
| [[GUET-CTF2019]BabyRSA 题解_偷一个月亮的博客-CSDN博客_ctf rsa](../../../cards/docs-guet-ctf2019-babyrsa-csdn-ctf-rsa.md) | GUET-CTF2019 |  | encoding-analysis |
| [[SDCTF 2022]Case64AR](../../../cards/crypto-sdctf-2022-case64ar.md) | SDCTF 2022 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [[SWPUCTF 2021 新生赛]ez_caesar](../../../cards/crypto-swpuctf-2021-ez-caesar.md) | SWPUCTF 2021 新生赛 | 简单 | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [[SWPUCTF 2022 新生赛]什锦](../../../cards/crypto-swpuctf-2022.md) | SWPUCTF 2022 新生赛 | 中等 | crypto-analysis, encoding-analysis, http-analysis, php-tricks |
| [[watevrCTF 2019]ECC-RSA 题解_mortal15的博客-CSDN博客](../../../cards/docs-watevrctf-2019-ecc-rsa-mortal15-csdn.md) | watevrCTF 2019 |  | crypto-analysis, encoding-analysis |
| [[WP/BUU/CTF]Cookie Store 题解_車鈊的博客-CSDN博客](../../../cards/docs-wp-buu-ctf-cookie-store-csdn.md) | WP/BUU/CTF |  | browser-forensics, classical-crypto, encoding-analysis |
| [[鹤城杯 2021]A_CRYPTO](../../../cards/crypto-2021-a-crypto.md) | 鹤城杯 2021 | 中等 | classical-crypto, crypto-analysis, http-analysis, web-exploitation |
| [AGCTF WP_weixin_52631365的博客-CSDN博客](../../../cards/docs-agctf-wp-weixin-52631365-csdn.md) | AGCTF WP |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [asc量子计算机,[推荐][原创]CTF-RSA常见题型、思路及解法_何壁咚的博客-CSDN博客](../../../cards/docs-asc-ctf-rsa-csdn.md) | asc量子计算机,[推荐][原创]CTF |  | classical-crypto, crypto-analysis, encoding-analysis, file-inclusion |
| [BugKu-CTF(解密篇Crypto)---道友不来算一算凶吉？_Nailaoyyds的博客-CSDN博客](../../../cards/docs-bugku-ctf-crypto-nailaoyyds-csdn.md) | BugKu |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [bugkuCTF平台逆向题第五道love题解_iqiqiya的博客-CSDN博客_bugku love](../../../cards/docs-bugkuctf-love-iqiqiya-csdn-bugku-love.md) | bugkuCTF平台逆向题第五道love题解 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [buuctf misc 一些其他题目_Lig_HossssT的博客-CSDN博客](../../../cards/docs-buuctf-misc-lig-hosssst-csdn.md) | buuctf misc 一些其他题目 |  | classical-crypto, encoding-analysis, misc-analysis |
| [Buuctf RSA 详细题解_偷一个月亮的博客-CSDN博客_buuctf rsa](../../../cards/docs-buuctf-rsa-csdn-buuctf-rsa.md) | Buuctf RSA 详细题解 |  | crypto-analysis |
| [BUUCTF RSA1 解题代码以及详细公式推导_拔草能手晓寒的博客-CSDN博客](../../../cards/docs-buuctf-rsa1-csdn.md) | BUUCTF RSA1 解题代码以及详细公式推导 |  | crypto-analysis, encoding-analysis |
| [BUUCTF RSA2&RSA3 解题思路及公式推导_拔草能手晓寒的博客-CSDN博客_buuctf rsa](../../../cards/docs-buuctf-rsa2-rsa3-csdn-buuctf-rsa.md) | BUUCTF RSA2&RSA3 解题思路及公式推导 |  | crypto-analysis, encoding-analysis |
| [BUUCTF RSA题目全解1_宁嘉的博客-CSDN博客_buuctf rsa1](../../../cards/docs-buuctf-rsa-1-csdn-buuctf-rsa1.md) | BUUCTF RSA题目全解1 |  | crypto-analysis, encoding-analysis, http-analysis, php-tricks |
| [BUUCTF RSA题目全解2_宁嘉的博客-CSDN博客](../../../cards/docs-buuctf-rsa-2-csdn.md) | BUUCTF RSA题目全解2 |  | crypto-analysis |
| [BUUCTF RSA题目全解3_宁嘉的博客-CSDN博客_buuctf rsa3](../../../cards/docs-buuctf-rsa-3-csdn-buuctf-rsa3.md) | BUUCTF RSA题目全解3 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [BUUCTF RSA题目全解4_宁嘉的博客-CSDN博客](../../../cards/docs-buuctf-rsa-4-csdn.md) | BUUCTF RSA题目全解4 |  | classical-crypto, crypto-analysis, encoding-analysis, symbolic-execution |
| [BUUCTF 基础破解_Charles_Andrew的博客-CSDN博客](../../../cards/docs-buuctf-charles-andrew-csdn.md) | BUUCTF 基础破解 |  | classical-crypto, crypto-analysis, encoding-analysis, misc-analysis |
| [BUUCTF-Crypto-MD5题解_ASSOINT的博客-CSDN博客](../../../cards/docs-buuctf-crypto-md5-assoint-csdn.md) | BUUCTF |  | crypto-analysis, http-analysis, php-tricks, web-exploitation |
| [BUUCTF-Crypto-password+变异凯撒题解_ASSOINT的博客-CSDN博客_变异凯撒密码解密](../../../cards/docs-buuctf-crypto-password-assoint-csdn.md) | BUUCTF |  | classical-crypto, crypto-analysis, file-inclusion |
| [BUUCTF-Crypto-rabbit+篱笆墙上的影子（栅栏密码）+RSA题解_ASSOINT的博客-CSDN博客](../../../cards/docs-buuctf-crypto-rabbit-rsa-assoint-csdn.md) | BUUCTF |  | classical-crypto, crypto-analysis, http-analysis, web-exploitation |
| [BUUCTF-Crypto-一眼就解密题解_ASSOINT的博客-CSDN博客_buuctf 一眼就解密](../../../cards/docs-buuctf-crypto-assoint-csdn-buuctf.md) | BUUCTF |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [BUUCTF-Crypto-变异凯撒解题思路_Georgeiweb的博客-CSDN博客_buuctf 变异凯撒](../../../cards/docs-buuctf-crypto-georgeiweb-csdn-buuctf.md) | BUUCTF |  | classical-crypto, crypto-analysis, web-exploitation |
| [BUUCTF-Crypto-大帝的密码武器题解（凯撒密码）_ASSOINT的博客-CSDN博客](../../../cards/docs-buuctf-crypto-assoint-csdn.md) | BUUCTF |  | classical-crypto, crypto-analysis |
| [BUUCTF-Crypto-摩丝题解_ASSOINT的博客-CSDN博客_buuctf 摩丝](../../../cards/docs-buuctf-crypto-assoint-csdn-buuctf.md) | BUUCTF |  | crypto-analysis, http-analysis, web-exploitation |
| [BUUCTF-Crypto-看我回旋踢题解_ASSOINT的博客-CSDN博客_看我回旋踢](../../../cards/docs-buuctf-crypto-assoint-csdn.md) | BUUCTF |  | classical-crypto, crypto-analysis, http-analysis, qr-analysis |
| [BUUCTF-Crypto-签到题解（base64）_ASSOINT的博客-CSDN博客](../../../cards/docs-buuctf-crypto-base64-assoint-csdn.md) | BUUCTF |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [BUUCTF-Crypto-老文盲了+Alice与Bob题解_ASSOINT的博客-CSDN博客](../../../cards/docs-buuctf-crypto-alice-bob-assoint-csdn.md) | BUUCTF |  | crypto-analysis |
| [BUUCTF-Crypto-（无语的）丢失的MD5题解_ASSOINT的博客-CSDN博客_输入让你无语的md5](../../../cards/docs-buuctf-crypto-md5-assoint-csdn-md5.md) | BUUCTF |  | crypto-analysis, encoding-analysis, php-tricks |
| [buuctf——rot_m0_46607055的博客-CSDN博客](../../../cards/docs-buuctf-rot-m0-46607055-csdn.md) | buuctf——rot |  | classical-crypto, crypto-analysis, encoding-analysis, php-tricks |
| [BUUCTF中CrackRTF题详细解法_F10W3RDANC3的博客-CSDN博客](../../../cards/docs-buuctf-crackrtf-f10w3rdanc3-csdn.md) | BUUCTF中CrackRTF题详细解法 |  | command-injection, crypto-analysis, encoding-analysis, http-analysis |
| [CG CTF CRYPTO easy!_Starzkg的博客-CSDN博客](../../../cards/docs-cg-ctf-crypto-easy-starzkg-csdn.md) | CG CTF CRYPTO easy! |  | classical-crypto, crypto-analysis, encoding-analysis |
| [CTF - Base64换表_建瓯最坏的博客-CSDN博客_base64换表](../../../cards/docs-ctf-base64-csdn-base64.md) | CTF |  | classical-crypto, encoding-analysis, qr-analysis, reverse-engineering |
| [CTF [网络安全实验室] [解密关第6题]_沙之夏的博客-CSDN博客](../../../cards/docs-ctf-6-csdn.md) | CTF [网络安全实验室] [解密关第6题] |  | classical-crypto, crypto-analysis, encoding-analysis, image-analysis |
| [CTF show 萌新区解题报告 （一）_Vayn3的博客-CSDN博客_ctf解题报告](../../../cards/docs-ctf-show-vayn3-csdn-ctf.md) | CTF show 萌新区解题报告 （一） |  | classical-crypto, crypto-analysis, encoding-analysis, image-analysis |
| [CTF show 萌新区解题报告 （三）_Vayn3的博客-CSDN博客](../../../cards/docs-ctf-show-vayn3-csdn.md) | CTF show 萌新区解题报告 （三） |  | classical-crypto, crypto-analysis, encoding-analysis, image-analysis |
| [CTF 中RSA的常见解析_LOL哦糯米藕的博客-CSDN博客_ctf rsa](../../../cards/docs-ctf-rsa-lol-csdn-ctf-rsa.md) | CTF 中RSA的常见解析 |  | crypto-analysis, network-forensics, qr-analysis, traffic-analysis |
| [CTF-bacon(培根密码)_咕唔～的博客-CSDN博客_培根密码](../../../cards/docs-ctf-bacon-csdn.md) | CTF |  | crypto-analysis |
| [CTF-rootme 题解之sudo - weak configuration_weixin_30663391的博客-CSDN博客](../../../cards/docs-ctf-rootme-sudo-weak-configuration-weixin-30663391-csdn.md) | CTF |  | privilege-escalation |
| [CTF-加密与解密（七）_红烧兔纸的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | CTF |  | classical-crypto, crypto-analysis, qr-analysis |
| [CTF-加密与解密（三）_红烧兔纸的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | CTF |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [CTF-加密与解密（九）_红烧兔纸的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | CTF |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [CTF-加密与解密（二）_红烧兔纸的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | CTF |  | crypto-analysis, encoding-analysis, php-tricks |
| [CTF-加密与解密（六）_红烧兔纸的博客-CSDN博客_加密与解密 附件](../../../cards/docs-ctf-csdn.md) | CTF |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [CTF-加密与解密（十八）_红烧兔纸的博客-CSDN博客_曼联加密](../../../cards/docs-ctf-csdn.md) | CTF |  | classical-crypto, crypto-analysis, encoding-analysis |
| [CTF-加密与解密（十四）_红烧兔纸的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | CTF |  | crypto-analysis, php-tricks |
| [ctf.show RSA入门题目题解若干_Rabbit_Gray的博客-CSDN博客_ctf中rsa实验题解析](../../../cards/docs-ctf-show-rsa-rabbit-gray-csdn-ctf-rsa.md) | ctf.show RSA入门题目题解若干 |  | crypto-analysis, dns-analysis, http-analysis, qr-analysis |
| [CTF中常见密码题解密网站总结_greedy-hat的博客-CSDN博客_当铺密码在线解密](../../../cards/docs-ctf-greedy-hat-csdn.md) | CTF中常见密码题解密网站总结 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [CTF习题解答--查找正确的密码 [JS题型]_乌恩大侠的博客-CSDN博客](../../../cards/docs-ctf-js-csdn.md) | CTF习题解答 |  | crypto-analysis, qr-analysis |
| [ctf刷题日记_AndrewMe8211的博客-CSDN博客](../../../cards/docs-ctf-andrewme8211-csdn.md) | ctf刷题日记 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [CTF加密题型解析：RSA算法的CTF解法之一_heshaai6843的博客-CSDN博客_rsa已知nec求pq](../../../cards/docs-ctf-rsa-ctf-heshaai6843-csdn-rsa-nec-pq.md) | CTF加密题型解析：RSA算法的CTF解法之一 |  | crypto-analysis, encoding-analysis |
| [CTF加密题型解析：RSA算法的CTF解法之一_weixin_30666943的博客-CSDN博客](../../../cards/docs-ctf-rsa-ctf-weixin-30666943-csdn.md) | CTF加密题型解析：RSA算法的CTF解法之一 |  | crypto-analysis, encoding-analysis |
| [CTF基础解题_destin_love的博客-CSDN博客_ctf解题](../../../cards/docs-ctf-destin-love-csdn-ctf.md) | CTF基础解题 |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [CTF学习-密码学解题思路_菜鸟-传奇的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | CTF学习 |  | classical-crypto, crypto-analysis, encoding-analysis, php-tricks |
| [ctf学习经历——极客部分题解_RoleMee的博客-CSDN博客](../../../cards/docs-ctf-rolemee-csdn.md) | ctf学习经历——极客部分题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [CTF密码学(crypto)题目easychallenge解题过程总结_hippotomons的博客-CSDN博客_easychallenge](../../../cards/docs-ctf-crypto-easychallenge-hippotomons-csdn-easychallenge.md) | CTF密码学(crypto)题目easychallenge解题过程总结 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [CTF密码学密文脚本解密及WP（凯撒解密）_weixin_33849942的博客-CSDN博客](../../../cards/docs-ctf-wp-weixin-33849942-csdn.md) | CTF密码学密文脚本解密及WP（凯撒解密） |  | classical-crypto, crypto-analysis, http-analysis, web-exploitation |
| [ctf密码学特殊的编码和解密_落雪wink的博客-CSDN博客_编码](../../../cards/docs-ctf-wink-csdn.md) | ctf密码学特殊的编码和解密 |  | classical-crypto, command-injection, crypto-analysis, http-analysis |
| [CTF解题小记--心得记录1_Air_cat的博客-CSDN博客](../../../cards/docs-ctf-1-air-cat-csdn.md) | CTF解题小记 |  | crypto-analysis, dns-analysis, php-tricks, reverse-engineering |
| [CTF解题记录-Misc-Base_今天解题了吗?的博客-CSDN博客_ctf misc 这才是base](../../../cards/docs-ctf-misc-base-csdn-ctf-misc-base.md) | CTF解题记录 |  | classical-crypto, crypto-analysis, encoding-analysis, misc-analysis |
| [ctf论剑场题解(1)_m0_51080245的博客-CSDN博客](../../../cards/docs-ctf-1-m0-51080245-csdn.md) | ctf论剑场题解(1) |  | encoding-analysis, php-tricks |
| [CTF部分题目解析_阿峰啊啊啊的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | CTF部分题目解析 |  | crypto-analysis, encoding-analysis, php-tricks |
| [CTF部分题目解析_阿峰啊啊啊的博客-CSDN博客_ctf竞赛试题及答案](../../../cards/docs-ctf-csdn-ctf.md) | CTF部分题目解析 |  | classical-crypto, crypto-analysis, encoding-analysis, symbolic-execution |
| [decrypt-WEB-BugKuCTF_Alasding的博客-CSDN博客](../../../cards/docs-decrypt-web-bugkuctf-alasding-csdn.md) | decrypt |  | classical-crypto, crypto-analysis, encoding-analysis, php-tricks |
| [HDCTF RSA 详细题解_偷一个月亮的博客-CSDN博客](../../../cards/docs-hdctf-rsa-csdn.md) | HDCTF RSA 详细题解 |  | crypto-analysis |
| [IceCTF Round Rabins!_前方是否可导？的博客-CSDN博客](../../../cards/docs-icectf-round-rabins-csdn.md) | IceCTF Round Rabins! |  | crypto-analysis |
| [Jarvis OJ 刷题题解 RE_pipixia233333的博客-CSDN博客](../../../cards/docs-jarvis-oj-re-pipixia233333-csdn.md) | Jarvis OJ 刷题题解 RE |  | binary-exploitation, classical-crypto, crypto-analysis, dns-analysis |
| [KCTF2019 Q3 签到题WP_飞鸿踏雪（蓝屏选手）的博客-CSDN博客](../../../cards/docs-kctf2019-q3-wp-csdn.md) | KCTF2019 Q3 签到题WP |  | crypto-analysis, encoding-analysis, php-tricks |
| [python md5解密_CTF-敲错键盘的md5解密，python通解_weixin_39616416的博客-CSDN博客](../../../cards/docs-python-md5-ctf-md5-python-weixin-39616416-csdn.md) | python md5解密 |  | crypto-analysis, encoding-analysis, http-analysis, php-tricks |
| [python求解二元二次方程组_【CTF WriteUp】2020祥云杯Crypto题解_张仁鹏的博客-CSDN博客](../../../cards/docs-python-ctf-writeup-2020-crypto-csdn.md) | python求解二元二次方程组 |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [rgss加密文件解包器_OGeek线上CTF挑战赛逆向及加密类赛题详细Write Up_weixin_39751871的博客-CSDN博客](../../../cards/docs-rgss-ogeek-ctf-write-up-weixin-39751871-csdn.md) | rgss加密文件解包器 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [RSA密码的学习以及几种常见CTF题型的总结(收集RSA解题脚本)_m0re的博客-CSDN博客_rsa脚本](../../../cards/docs-rsa-ctf-rsa-m0re-csdn-rsa.md) | RSA密码的学习以及几种常见CTF题型的总结(收集RSA解题脚本) |  | crypto-analysis, encoding-analysis, misc-analysis |
| [RSA算法原理及CTF解题_WHOAMIAnony的博客-CSDN博客](../../../cards/docs-rsa-ctf-whoamianony-csdn.md) | RSA算法原理及CTF解题 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [SCTF 2019 re部分题解(持续更新中)_pipixia233333的博客-CSDN博客](../../../cards/docs-sctf-2019-re-pipixia233333-csdn.md) | SCTF 2019 re部分题解(持续更新中) |  | classical-crypto, crypto-analysis, encoding-analysis, mobile-forensics |
| [writeup: 实验吧 CTF模拟试题 解密关-RSARSA_sinat_33769106的博客-CSDN博客](../../../cards/docs-writeup-ctf-rsarsa-sinat-33769106-csdn.md) | writeup: 实验吧 CTF模拟试题 解密关 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [“百度杯”CTF比赛 十一月场(Misc)_andiao1218的博客-CSDN博客](../../../cards/docs-ctf-misc-andiao1218-csdn.md) | “百度杯”CTF比赛 十一月场(Misc) |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [【CTF WriteUp】201909广东强网杯部分题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-201909-csdn.md) | 【CTF WriteUp】201909广东强网杯部分题解 |  | binary-exploitation, crypto-analysis, encoding-analysis, http-analysis |
| [【CTF WriteUp】2020中央企业”新基建“网络安全技术大赛决赛部分Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [【CTF WriteUp】2020中央企业”新基建“网络安全技术大赛初赛Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF |  | classical-crypto, crypto-analysis, encoding-analysis, qr-analysis |
| [【CTF WriteUp】2020全国工业互联网安全技术技能大赛（原护网杯）Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF |  | binary-exploitation, crypto-analysis, encoding-analysis, web-exploitation |
| [【CTF WriteUp】2020天翼杯Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF WriteUp】2020天翼杯Crypto题解 |  | crypto-analysis, http-analysis, php-tricks, qr-analysis |
| [【CTF WriteUp】2020数字中国创新大赛部分题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-csdn.md) | 【CTF WriteUp】2020数字中国创新大赛部分题解 |  | binary-exploitation, crypto-analysis, encoding-analysis |
| [【CTF WriteUp】2020电信和互联网行业赛个人赛部分Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF WriteUp】2020电信和互联网行业赛个人赛部分Crypto题解 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [【CTF WriteUp】2020祥云杯Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF WriteUp】2020祥云杯Crypto题解 |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [【CTF WriteUp】2020第四届强网杯部分Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF WriteUp】2020第四届强网杯部分Crypto题解 |  | binary-exploitation, crypto-analysis, encoding-analysis |
| [【CTF WriteUp】2020网鼎杯第一场Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF WriteUp】2020网鼎杯第一场Crypto题解 |  | crypto-analysis, encoding-analysis, php-tricks |
| [【CTF WriteUp】2020网鼎杯第三场Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF WriteUp】2020网鼎杯第三场Crypto题解 |  | crypto-analysis |
| [【CTF WriteUp】2020网鼎杯第二场Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2020-crypto-csdn.md) | 【CTF WriteUp】2020网鼎杯第二场Crypto题解 |  | classical-crypto, crypto-analysis, encoding-analysis, qr-analysis |
| [【CTF WriteUp】2021 starCTF部分Crypto题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-2021-starctf-crypto-csdn.md) | 【CTF WriteUp】2021 starCTF部分Crypto题解 |  | binary-exploitation, crypto-analysis, encoding-analysis, http-analysis |
| [【CTF WriteUp】UTCTF 2020部分题解_零食商人的博客-CSDN博客](../../../cards/docs-ctf-writeup-utctf-2020-csdn.md) | 【CTF WriteUp】UTCTF 2020部分题解 |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [【CTF大赛】陇剑杯-机密内存-解题过程分析_IT老涵的博客-CSDN博客_ctf内存分析](../../../cards/docs-ctf-it-csdn-ctf.md) | 【CTF大赛】陇剑杯 |  | crypto-analysis, encoding-analysis, malware-static, memory-forensics |
| [【moeCTF题解-0x04】Crypto_框架主义者的博客-CSDN博客](../../../cards/docs-moectf-0x04-crypto-csdn.md) | 【moeCTF题解 |  | classical-crypto, crypto-analysis, encoding-analysis, file-inclusion |
| [东南大学CTF之签到题_以夕阳落款的博客-CSDN博客_签到题解题思路ctf](../../../cards/docs-ctf-csdn-ctf.md) | 东南大学CTF之签到题 |  | classical-crypto, encoding-analysis |
| [再不学点现代密码，CTF就Hold不住啦！_合天网安实验室的博客-CSDN博客](../../../cards/docs-ctf-hold-csdn.md) | 再不学点现代密码，CTF就Hold不住啦！ |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [功防世界CTF-crypto-Morse_萌萌哒的baola的博客-CSDN博客](../../../cards/docs-ctf-crypto-morse-baola-csdn.md) | 功防世界CTF |  | crypto-analysis |
| [南邮CTF逆向题第三道Py交易解题思路_iqiqiya的博客-CSDN博客](../../../cards/docs-ctf-py-iqiqiya-csdn.md) | 南邮CTF逆向题第三道Py交易解题思路 |  | classical-crypto, crypto-analysis, encoding-analysis |
| [大连海事大学第一届“启航杯”DLMU CTF部分题解_ℳ๓₯㎕₯㎕ζั的博客-CSDN博客](../../../cards/docs-dlmu-ctf-csdn.md) | 大连海事大学第一届“启航杯”DLMU CTF部分题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [实验吧 部分逆向题解_pipixia233333的博客-CSDN博客](../../../cards/docs-pipixia233333-csdn.md) | 实验吧 部分逆向题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [最后一位被整除 oracle,【CTF WriteUp】2020第四届强网杯部分Crypto题解_weixin_39644952的博客-CSDN博客](../../../cards/docs-oracle-ctf-writeup-2020-crypto-weixin-39644952-csdn.md) | 最后一位被整除 |  | binary-exploitation, crypto-analysis, encoding-analysis |
| [百度杯”CTF比赛（十一月场)_Root__Liu的博客-CSDN博客](../../../cards/docs-ctf-root-liu-csdn.md) | 百度杯”CTF比赛（十一月场) |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [看雪CTF 2017 第六题设计思路和解题思路_Ericky_的博客-CSDN博客](../../../cards/docs-ctf-2017-ericky-csdn.md) | 看雪CTF 2017 第六题设计思路和解题思路 |  | classical-crypto, encoding-analysis, stream-cipher |
| [看雪ctf部分题解_合天网安实验室的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | 看雪ctf部分题解 |  | binary-exploitation, crypto-analysis, encoding-analysis, reverse-engineering |
| [第6篇：基础入门~加密编码算法_廖一语山的博客-CSDN博客](../../../cards/docs-6-csdn.md) | 第6篇：基础入门~加密编码算法 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [美团杯MEITUAN网络安全大赛CTF2021-humburgerRSA题解_rickliuxiao的博客-CSDN博客](../../../cards/docs-meituan-ctf2021-humburgerrsa-rickliuxiao-csdn.md) | 美团杯MEITUAN网络安全大赛CTF2021 |  | crypto-analysis |
| [西普实验吧CTF-杯酒人生_以夕阳落款的博客-CSDN博客](../../../cards/docs-ctf-csdn.md) | 西普实验吧CTF |  | classical-crypto, crypto-analysis |
| [邑网杯 CTF 2021 ,cipher2 ADFGVX 解题_euzen的博客-CSDN博客](../../../cards/docs-ctf-2021-cipher2-adfgvx-euzen-csdn.md) | 邑网杯 CTF 2021 ,cipher2 ADFGVX 解题 |  | crypto-analysis, qr-analysis |
