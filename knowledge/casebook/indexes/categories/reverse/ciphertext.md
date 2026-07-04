# Reverse / ciphertext

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| crypto-analysis | 20 | cipher decoding, reverse engineering, http evidence extraction, file inclusion exploitation, IDA Pro-driven evidence lookup |
| classical-crypto | 16 | cipher decoding, reverse engineering, http evidence extraction, file inclusion exploitation, IDA Pro-driven evidence lookup |
| reverse-engineering | 16 | reverse engineering, cipher decoding, http evidence extraction, file inclusion exploitation, IDA Pro-driven evidence lookup |
| encoding-analysis | 15 | reverse engineering, cipher decoding, http evidence extraction, file inclusion exploitation, IDA Pro-driven evidence lookup |
| http-analysis | 10 | cipher decoding, reverse engineering, http evidence extraction, IDA Pro-driven evidence lookup, file inclusion exploitation |
| web-exploitation | 10 | cipher decoding, reverse engineering, http evidence extraction, IDA Pro-driven evidence lookup, file inclusion exploitation |
| qr-analysis | 7 | cipher decoding, http evidence extraction, reverse engineering, command execution path, stego extraction |
| mobile-forensics | 6 | reverse engineering, http evidence extraction, cipher decoding, command execution path, file inclusion exploitation |
| file-inclusion | 5 | file inclusion exploitation, http evidence extraction, reverse engineering, cipher decoding, command execution path |
| integer-overflow | 5 | reverse engineering, http evidence extraction, cipher decoding, command execution path, integer-overflow bypass |
| php-tricks | 4 | cipher decoding, reverse engineering, http evidence extraction, file inclusion exploitation, command execution path |
| command-injection | 3 | cipher decoding, http evidence extraction, reverse engineering, file inclusion exploitation, command execution path |
| malware-static | 3 | reverse engineering, cipher decoding, file inclusion exploitation, http evidence extraction, integer-overflow bypass |
| stego-extraction | 3 | reverse engineering, cipher decoding, file inclusion exploitation, http evidence extraction, integer-overflow bypass |
| stream-cipher | 3 | cipher decoding, file inclusion exploitation, http evidence extraction, IDA Pro-driven evidence lookup, netcat-driven evidence lookup |
| misc-analysis | 2 | reverse engineering, cipher decoding, file inclusion exploitation, http evidence extraction, integer-overflow bypass |
| symbolic-execution | 2 | angr-driven evidence lookup, cipher decoding, constraint solving, file inclusion exploitation, reverse engineering |
| waf-bypass | 2 | reverse engineering, integer-overflow bypass, waf bypass |
| dns-analysis | 1 | cipher decoding, file inclusion exploitation, http evidence extraction, reverse engineering |
| ret2libc | 1 | cipher decoding, command execution path, http evidence extraction, reverse engineering |
| stack-overflow | 1 | cipher decoding, command execution path, http evidence extraction, reverse engineering |

## Route Types

| Route type | Cases |
| --- | --- |
| cipher decoding | 15 |
| reverse engineering | 14 |
| http evidence extraction | 9 |
| file inclusion exploitation | 4 |
| IDA Pro-driven evidence lookup | 3 |
| command execution path | 2 |
| integer-overflow bypass | 2 |
| netcat-driven evidence lookup | 2 |
| stego extraction | 2 |
| angr-driven evidence lookup | 1 |
| constraint solving | 1 |
| ida-driven evidence lookup | 1 |
| radare2-driven evidence lookup | 1 |
| waf bypass | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [**[长城杯 2021 政企组]魔鬼凯撒的RC4茶室**](../../../cards/reverse-2021-rc4.md) | 长城杯 2021 政企组 |  | classical-crypto, crypto-analysis, stream-cipher |
| [2021虎符ctf-逆向题解_20000s的博客-CSDN博客](../../../cards/docs-2021-ctf-20000s-csdn.md) | 2021虎符ctf |  | crypto-analysis, encoding-analysis, file-inclusion, integer-overflow |
| [[BUUCTF 刷题] Reverse解题方法总结（一）_Y1seco的博客-CSDN博客_buuctf reverse](../../../cards/docs-buuctf-reverse-y1seco-csdn-buuctf-reverse.md) | BUUCTF 刷题 |  | classical-crypto, command-injection, crypto-analysis, dns-analysis |
| [[MoeCTF 2022] Base](../../../cards/reverse-moectf-2022-base.md) | MoeCTF 2022 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [[SWPUCTF 2022 新生赛] upx](../../../cards/reverse-swpuctf-2022-upx.md) | SWPUCTF 2022 新生赛 |  | crypto-analysis, http-analysis, reverse-engineering, web-exploitation |
| [[SWPUCTF 2024 秋季新生赛] 动态调试](../../../cards/reverse-swpuctf-2024.md) | SWPUCTF 2024 秋季新生赛 |  | classical-crypto, crypto-analysis, http-analysis, reverse-engineering |
| [[羊城杯 2020] easyre](../../../cards/reverse-2020-easyre.md) | 羊城杯 2020 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [android ctf 分析,Android逆向笔记 - ZCTF2016题解_weixin_39590635的博客-CSDN博客](../../../cards/docs-android-ctf-android-zctf2016-weixin-39590635-csdn.md) | android ctf 分析,Android逆向笔记 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [BugkuCTF RE部分题解_z.volcano的博客-CSDN博客_bugku 杰瑞的影分身](../../../cards/docs-bugkuctf-re-z-volcano-csdn-bugku.md) | BugkuCTF RE部分题解 |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [BUUCTF Reverse解题记录（三）_sxhthreo的博客-CSDN博客](../../../cards/docs-buuctf-reverse-sxhthreo-csdn.md) | BUUCTF Reverse解题记录（三） |  | crypto-analysis, qr-analysis |
| [BUUCTF reverse：[GXYCTF2019]luck_guy,findit,简单注册器题解_June_gjy的博客-CSDN博客](../../../cards/docs-buuctf-reverse-gxyctf2019-luck-guy-findit-june-gjy-csdn.md) | BUUCTF reverse：[GXYCTF2019]luck |  | classical-crypto, crypto-analysis, http-analysis, integer-overflow |
| [buuctf-crackMe题解及感悟_夏男人的博客-CSDN博客](../../../cards/docs-buuctf-crackme-csdn.md) | buuctf |  | crypto-analysis, php-tricks, reverse-engineering |
| [BUUCTF逆向题练习记录（wp） --（3）WUSTCTF2020&&level1-4已完成_Air_cat的博客-CSDN博客](../../../cards/docs-buuctf-wp-3-wustctf2020-level1-4-air-cat-csdn.md) | BUUCTF逆向题练习记录（wp） |  | classical-crypto, crypto-analysis, encoding-analysis, qr-analysis |
| [buu逆向刷题（二）_北风~的博客-CSDN博客](../../../cards/docs-buu-csdn.md) | buu逆向刷题（二） |  | classical-crypto, command-injection, crypto-analysis, encoding-analysis |
| [ctf xor题_详解两道CTF逆向题_weixin_34324618的博客-CSDN博客](../../../cards/docs-ctf-xor-ctf-weixin-34324618-csdn.md) | ctf xor题 |  | classical-crypto, encoding-analysis, integer-overflow, misc-analysis |
| [CTF-安卓逆向入门题目_Thunder_J的博客-CSDN博客_ctf 安卓逆向](../../../cards/docs-ctf-thunder-j-csdn-ctf.md) | CTF |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [CTF题解四 逆向 顺藤摸瓜（ISCC2017）_目标是技术宅的博客-CSDN博客](../../../cards/docs-ctf-iscc2017-csdn.md) | CTF题解四 逆向 顺藤摸瓜（ISCC2017） |  | crypto-analysis, encoding-analysis, qr-analysis, reverse-engineering |
| [《BUUCTF逆向题解》——reverse3_IpartmentXHC的博客-CSDN博客](../../../cards/docs-buuctf-reverse3-ipartmentxhc-csdn.md) | 《BUUCTF逆向题解》——reverse3 |  | classical-crypto, crypto-analysis, encoding-analysis, reverse-engineering |
| [【CTF reverse】逆向入门题解集合+逆向相关软件安装_hans774882968的博客-CSDN博客](../../../cards/docs-ctf-reverse-hans774882968-csdn.md) | 【CTF reverse】逆向入门题解集合+逆向相关软件安装 |  | classical-crypto, crypto-analysis, encoding-analysis, http-analysis |
| [【二进制】【WP】MOCTF逆向题解_weixin_30684743的博客-CSDN博客](../../../cards/docs-wp-moctf-weixin-30684743-csdn.md) | 【二进制】【WP】MOCTF逆向题解 |  | classical-crypto, crypto-analysis, encoding-analysis, reverse-engineering |
| [深信服杯 CTF 线上 逆向题解_pipixia233333的博客-CSDN博客](../../../cards/docs-ctf-pipixia233333-csdn.md) | 深信服杯 CTF 线上 逆向题解 |  | classical-crypto, crypto-analysis, encoding-analysis, file-inclusion |
