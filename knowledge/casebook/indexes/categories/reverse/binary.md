# Reverse / binary

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| reverse-engineering | 44 | reverse engineering, http evidence extraction, cipher decoding, file inclusion exploitation, command execution path |
| crypto-analysis | 25 | reverse engineering, cipher decoding, http evidence extraction, file inclusion exploitation, command execution path |
| encoding-analysis | 21 | reverse engineering, http evidence extraction, cipher decoding, file inclusion exploitation, netcat-driven evidence lookup |
| classical-crypto | 15 | reverse engineering, cipher decoding, http evidence extraction, file inclusion exploitation, IDA Pro-driven evidence lookup |
| web-exploitation | 15 | reverse engineering, cipher decoding, http evidence extraction, command execution path, IDA Pro-driven evidence lookup |
| http-analysis | 14 | reverse engineering, cipher decoding, http evidence extraction, IDA Pro-driven evidence lookup, command execution path |
| qr-analysis | 9 | cipher decoding, http evidence extraction, reverse engineering, command execution path, file inclusion exploitation |
| file-inclusion | 8 | file inclusion exploitation, reverse engineering, http evidence extraction, cipher decoding, netcat-driven evidence lookup |
| mobile-forensics | 7 | http evidence extraction, reverse engineering, cipher decoding, command execution path, file inclusion exploitation |
| command-injection | 6 | reverse engineering, command execution path, http evidence extraction, cipher decoding, file inclusion exploitation |
| integer-overflow | 6 | reverse engineering, http evidence extraction, integer-overflow bypass, cipher decoding, command execution path |
| symbolic-execution | 6 | constraint solving, reverse engineering, angr-driven evidence lookup, cipher decoding, file inclusion exploitation |
| malware-static | 5 | reverse engineering, file inclusion exploitation, http evidence extraction, cipher decoding, integer-overflow bypass |
| php-tricks | 5 | reverse engineering, cipher decoding, http evidence extraction, file inclusion exploitation, command execution path |
| stego-extraction | 5 | reverse engineering, file inclusion exploitation, http evidence extraction, cipher decoding, integer-overflow bypass |
| osint | 4 | reverse engineering, http evidence extraction, evidence lookup, gdb-driven evidence lookup |
| misc-analysis | 3 | reverse engineering, http evidence extraction, integer-overflow bypass, cipher decoding, file inclusion exploitation |
| binary-exploitation | 2 | command execution path, reverse engineering, indicator enrichment |
| ret2libc | 2 | command execution path, reverse engineering, cipher decoding, http evidence extraction, indicator enrichment |
| stack-overflow | 2 | reverse engineering, cipher decoding, command execution path, constraint solving, http evidence extraction |
| stream-cipher | 2 | cipher decoding, file inclusion exploitation, http evidence extraction, IDA Pro-driven evidence lookup, netcat-driven evidence lookup |
| waf-bypass | 2 | reverse engineering, integer-overflow bypass, waf bypass |
| browser-forensics | 1 | command execution path, indicator enrichment, reverse engineering |
| dns-analysis | 1 | cipher decoding, file inclusion exploitation, http evidence extraction, reverse engineering |
| password-cracking | 1 | command execution path, reverse engineering |
| service-enumeration | 1 | command execution path, indicator enrichment, reverse engineering |

## Route Types

| Route type | Cases |
| --- | --- |
| reverse engineering | 42 |
| http evidence extraction | 26 |
| cipher decoding | 14 |
| file inclusion exploitation | 7 |
| command execution path | 5 |
| constraint solving | 5 |
| netcat-driven evidence lookup | 5 |
| IDA Pro-driven evidence lookup | 3 |
| ida-driven evidence lookup | 3 |
| integer-overflow bypass | 3 |
| angr-driven evidence lookup | 2 |
| evidence lookup | 2 |
| gdb-driven evidence lookup | 2 |
| stego extraction | 2 |
| indicator enrichment | 1 |
| jadx-driven evidence lookup | 1 |
| radare2-driven evidence lookup | 1 |
| waf bypass | 1 |
| z3-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [*ctf 逆向math题解_Cosmop01itan的博客-CSDN博客](../../../cards/docs-ctf-math-cosmop01itan-csdn.md) | *ctf 逆向math题解 |  | crypto-analysis, encoding-analysis, file-inclusion, qr-analysis |
| [2021虎符ctf-逆向题解_20000s的博客-CSDN博客](../../../cards/docs-2021-ctf-20000s-csdn.md) | 2021虎符ctf |  | crypto-analysis, encoding-analysis, file-inclusion, integer-overflow |
| [[BUUCTF 刷题] Reverse解题方法总结（一）_Y1seco的博客-CSDN博客_buuctf reverse](../../../cards/docs-buuctf-reverse-y1seco-csdn-buuctf-reverse.md) | BUUCTF 刷题 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [[BUUCTF] [Reverse]不一样的flag_flagorz的博客-CSDN博客_不一样的flag](../../../cards/docs-buuctf-reverse-flag-flagorz-csdn-flag.md) | BUUCTF |  | osint |
| [[CTF]攻防世界Simple-check-100题解（GDB）_拈花倾城的博客-CSDN博客](../../../cards/docs-ctf-simple-check-100-gdb-csdn.md) | CTF |  | crypto-analysis, integer-overflow, misc-analysis, reverse-engineering |
| [[GCCCTF 2025] constraint](../../../cards/reverse-gccctf-2025-constraint.md) | GCCCTF 2025 |  | reverse-engineering, stack-overflow, symbolic-execution |
| [[HZNUCTF 2023 final]虽然他送了我玫瑰花](../../../cards/reverse-hznuctf-2023-final.md) | HZNUCTF 2023 final |  | reverse-engineering |
| [[MoeCTF 2022] Base](../../../cards/reverse-moectf-2022-base.md) | MoeCTF 2022 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [[SWPUCTF 2022 新生赛] upx](../../../cards/reverse-swpuctf-2022-upx.md) | SWPUCTF 2022 新生赛 |  | crypto-analysis, http-analysis, reverse-engineering, web-exploitation |
| [[SWPUCTF 2024 秋季新生赛] 动态调试](../../../cards/reverse-swpuctf-2024.md) | SWPUCTF 2024 秋季新生赛 |  | classical-crypto, crypto-analysis, http-analysis, reverse-engineering |
| [[WUSTCTF 2020] funnyre](../../../cards/reverse-wustctf-2020-funnyre.md) | WUSTCTF 2020 |  | http-analysis, reverse-engineering, symbolic-execution, web-exploitation |
| [[羊城杯 2020] easyre](../../../cards/reverse-2020-easyre.md) | 羊城杯 2020 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [android ctf 分析,Android逆向笔记 - ZCTF2016题解_weixin_39590635的博客-CSDN博客](../../../cards/docs-android-ctf-android-zctf2016-weixin-39590635-csdn.md) | android ctf 分析,Android逆向笔记 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [BugkuCTF RE部分题解_z.volcano的博客-CSDN博客_bugku 杰瑞的影分身](../../../cards/docs-bugkuctf-re-z-volcano-csdn-bugku.md) | BugkuCTF RE部分题解 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [bugkuCTF之逆向入门解题思路_邻家小白的博客-CSDN博客](../../../cards/docs-bugkuctf-csdn.md) | bugkuCTF之逆向入门解题思路 |  | reverse-engineering |
| [bugkuCTF平台逆向题第一道Easy_vb题解_iqiqiya的博客-CSDN博客_bugkueasy_vb](../../../cards/docs-bugkuctf-easy-vb-iqiqiya-csdn-bugkueasy-vb.md) | bugkuCTF平台逆向题第一道Easy |  | http-analysis, osint, reverse-engineering, web-exploitation |
| [bugkuCTF平台逆向题第二道Easy_Re题解_iqiqiya的博客-CSDN博客_easy_re](../../../cards/docs-bugkuctf-easy-re-iqiqiya-csdn-easy-re.md) | bugkuCTF平台逆向题第二道Easy |  | http-analysis, osint, reverse-engineering, web-exploitation |
| [BUUCTF crackMe 题解___lifanxin的博客-CSDN博客_buuctf crackme](../../../cards/docs-buuctf-crackme-lifanxin-csdn-buuctf-crackme.md) | BUUCTF crackMe 题解 |  | encoding-analysis, php-tricks, reverse-engineering |
| [BUUCTF Reverse前五题解题记录_sxhthreo的博客-CSDN博客_buuctf reverse](../../../cards/docs-buuctf-reverse-sxhthreo-csdn-buuctf-reverse.md) | BUUCTF Reverse前五题解题记录 |  | reverse-engineering |
| [BUUCTF Reverse解题记录（三）_sxhthreo的博客-CSDN博客](../../../cards/docs-buuctf-reverse-sxhthreo-csdn.md) | BUUCTF Reverse解题记录（三） |  | crypto-analysis, qr-analysis |
| [BUUCTF reverse：[GXYCTF2019]luck_guy,findit,简单注册器题解_June_gjy的博客-CSDN博客](../../../cards/docs-buuctf-reverse-gxyctf2019-luck-guy-findit-june-gjy-csdn.md) | BUUCTF reverse：[GXYCTF2019]luck |  | classical-crypto, crypto-analysis, http-analysis, integer-overflow |
| [buuctf--SimpleRev_Mr.LangPiao的博客-CSDN博客](../../../cards/docs-buuctf-simplerev-mr-langpiao-csdn.md) | buuctf |  | crypto-analysis, reverse-engineering |
| [buuctf-crackMe题解及感悟_夏男人的博客-CSDN博客](../../../cards/docs-buuctf-crackme-csdn.md) | buuctf |  | crypto-analysis, php-tricks, reverse-engineering |
| [BUUCTF逆向题练习记录（wp） --（3）WUSTCTF2020&&level1-4已完成_Air_cat的博客-CSDN博客](../../../cards/docs-buuctf-wp-3-wustctf2020-level1-4-air-cat-csdn.md) | BUUCTF逆向题练习记录（wp） |  | classical-crypto, crypto-analysis, encoding-analysis, qr-analysis |
| [buu逆向刷题（二）_北风~的博客-CSDN博客](../../../cards/docs-buu-csdn.md) | buu逆向刷题（二） |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [ctf xor题_详解两道CTF逆向题_weixin_34324618的博客-CSDN博客](../../../cards/docs-ctf-xor-ctf-weixin-34324618-csdn.md) | ctf xor题 |  | classical-crypto, encoding-analysis, integer-overflow, misc-analysis |
| [CTF-rootme 题解之PYC - ByteCode_weixin_30437847的博客-CSDN博客](../../../cards/docs-ctf-rootme-pyc-bytecode-weixin-30437847-csdn.md) | CTF |  | command-injection, crypto-analysis, encoding-analysis, qr-analysis |
| [CTF-z3简要介绍_Thunder_J的博客-CSDN博客](../../../cards/docs-ctf-z3-thunder-j-csdn.md) | CTF |  | symbolic-execution |
| [CTF-安卓逆向入门题目_Thunder_J的博客-CSDN博客_ctf 安卓逆向](../../../cards/docs-ctf-thunder-j-csdn-ctf.md) | CTF |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [CTF_REVERSE做题解析_槑~槑的博客-CSDN博客](../../../cards/docs-ctf-reverse-csdn.md) | CTF |  | reverse-engineering |
| [ctf逆向解题——re1_FunkyPants的博客-CSDN博客_ctf逆向题](../../../cards/docs-ctf-re1-funkypants-csdn-ctf.md) | ctf逆向解题——re1 |  | encoding-analysis, malware-static, reverse-engineering, stego-extraction |
| [CTF题目部分解析_阿峰啊啊啊的博客-CSDN博客_ctf题目](../../../cards/docs-ctf-csdn-ctf.md) | CTF题目部分解析 |  | mobile-forensics |
| [CTF题解三 逆向 where is your flag（ISCC2017）_目标是技术宅的博客-CSDN博客](../../../cards/docs-ctf-where-is-your-flag-iscc2017-csdn.md) | CTF题解三 逆向 where is your flag（ISCC2017） |  | reverse-engineering |
| [CTF题解四 逆向 顺藤摸瓜（ISCC2017）_目标是技术宅的博客-CSDN博客](../../../cards/docs-ctf-iscc2017-csdn.md) | CTF题解四 逆向 顺藤摸瓜（ISCC2017） |  | crypto-analysis, encoding-analysis, qr-analysis, reverse-engineering |
| [Flying_Fatty的博客_CSDN博客-ACM题解,CTF之旅,数学领域博主](../../../cards/docs-flying-fatty-csdn-acm-ctf.md) | Flying |  | reverse-engineering |
| [NYIST练习 题解（一）_pipixia233333的博客-CSDN博客](../../../cards/docs-nyist-pipixia233333-csdn.md) | NYIST练习 题解（一） |  | file-inclusion |
| [PWN collision [pwnable.kr]CTF writeup题解系列2_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-collision-pwnable-kr-ctf-writeup-2-3ric5r-csdn.md) | PWN collision |  | binary-exploitation, browser-forensics, command-injection, ret2libc |
| [PWN flag [pwnable.kr]CTF writeup题解系列4_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-flag-pwnable-kr-ctf-writeup-4-3ric5r-csdn.md) | PWN flag [pwnable.kr]CTF writeup题解系列4 |  | binary-exploitation, command-injection, http-analysis, password-cracking |
| [XL----逆向入门新手题解_颜又舞的博客-CSDN博客](../../../cards/docs-xl-csdn.md) | XL |  | file-inclusion, malware-static, reverse-engineering, stego-extraction |
| [z3 巧解CTF逆向题_weixin_30613343的博客-CSDN博客](../../../cards/docs-z3-ctf-weixin-30613343-csdn.md) | z3 巧解CTF逆向题 |  | crypto-analysis, symbolic-execution |
| [《BUUCTF逆向题解》——easyre_IpartmentXHC的博客-CSDN博客](../../../cards/docs-buuctf-easyre-ipartmentxhc-csdn.md) | 《BUUCTF逆向题解》——easyre |  | reverse-engineering |
| [《BUUCTF逆向题解》——helloword_IpartmentXHC的博客-CSDN博客](../../../cards/docs-buuctf-helloword-ipartmentxhc-csdn.md) | 《BUUCTF逆向题解》——helloword |  | reverse-engineering |
| [《BUUCTF逆向题解》——reverse3_IpartmentXHC的博客-CSDN博客](../../../cards/docs-buuctf-reverse3-ipartmentxhc-csdn.md) | 《BUUCTF逆向题解》——reverse3 |  | classical-crypto, crypto-analysis, encoding-analysis, reverse-engineering |
| [《BUUCTF逆向题解》——xor_IpartmentXHC的博客-CSDN博客](../../../cards/docs-buuctf-xor-ipartmentxhc-csdn.md) | 《BUUCTF逆向题解》——xor |  | crypto-analysis, reverse-engineering |
| [《BUUCTF逆向题解》——不一样的flag_IpartmentXHC的博客-CSDN博客](../../../cards/docs-buuctf-flag-ipartmentxhc-csdn.md) | 《BUUCTF逆向题解》——不一样的flag |  | reverse-engineering |
| [【CTF reverse】逆向入门题解集合+逆向相关软件安装_hans774882968的博客-CSDN博客](../../../cards/docs-ctf-reverse-hans774882968-csdn.md) | 【CTF reverse】逆向入门题解集合+逆向相关软件安装 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [【二进制】【WP】MOCTF逆向题解_weixin_30684743的博客-CSDN博客](../../../cards/docs-wp-moctf-weixin-30684743-csdn.md) | 【二进制】【WP】MOCTF逆向题解 |  | classical-crypto, crypto-analysis, encoding-analysis, reverse-engineering |
| [南邮CTF逆向题第一道Hello,RE!解题思路_iqiqiya的博客-CSDN博客](../../../cards/docs-ctf-hello-re-iqiqiya-csdn.md) | 南邮CTF逆向题第一道Hello,RE!解题思路 |  | reverse-engineering |
| [南邮CTF逆向题第四道WxyVM解题思路_iqiqiya的博客-CSDN博客](../../../cards/docs-ctf-wxyvm-iqiqiya-csdn.md) | 南邮CTF逆向题第四道WxyVM解题思路 |  | encoding-analysis, reverse-engineering |
| [南邮ctf非正式题解 -- 逆向maze （方向的判断函数解析）_Air_cat的博客-CSDN博客](../../../cards/docs-ctf-maze-air-cat-csdn.md) | 南邮ctf非正式题解 |  | encoding-analysis |
| [南邮ctf题解--逆向第一道Hello,RE!_Air_cat的博客-CSDN博客](../../../cards/docs-ctf-hello-re-air-cat-csdn.md) | 南邮ctf题解 |  | reverse-engineering |
| [实验吧CTF逆向题目Just Click题解_iqiqiya的博客-CSDN博客](../../../cards/docs-ctf-just-click-iqiqiya-csdn.md) | 实验吧CTF逆向题目Just Click题解 |  | reverse-engineering |
| [攻防世界 Reverse Hello,CTF_thinszx的博客-CSDN博客](../../../cards/docs-reverse-hello-ctf-thinszx-csdn.md) | 攻防世界 Reverse Hello,CTF |  | reverse-engineering |
| [深信服杯 CTF 线上 逆向题解_pipixia233333的博客-CSDN博客](../../../cards/docs-ctf-pipixia233333-csdn.md) | 深信服杯 CTF 线上 逆向题解 |  | classical-crypto, crypto-analysis, encoding-analysis, file-inclusion |
| [软件逆向分析初试reverse；ctf-re 入门题，详解_Cherry_icc的博客-CSDN博客_certreg是什么程序](../../../cards/docs-reverse-ctf-re-cherry-icc-csdn-certreg.md) | 软件逆向分析初试reverse；ctf |  | osint, reverse-engineering |
