# Pwn / binary

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| binary-exploitation | 117 | http evidence extraction, reverse engineering, stack control exploitation, command execution path, memory artifact analysis |
| web-exploitation | 94 | stack control exploitation, http evidence extraction, reverse engineering, memory artifact analysis, command execution path |
| ret2libc | 73 | http evidence extraction, reverse engineering, stack control exploitation, command execution path, memory artifact analysis |
| stack-overflow | 63 | stack control exploitation, reverse engineering, http evidence extraction, command execution path, memory artifact analysis |
| reverse-engineering | 62 | reverse engineering, http evidence extraction, stack control exploitation, command execution path, memory artifact analysis |
| command-injection | 42 | command execution path, http evidence extraction, reverse engineering, stack control exploitation, memory artifact analysis |
| encoding-analysis | 41 | http evidence extraction, reverse engineering, stack control exploitation, waf bypass, command execution path |
| http-analysis | 38 | stack control exploitation, gdb-driven evidence lookup, http evidence extraction, pwntools-driven evidence lookup, reverse engineering |
| waf-bypass | 27 | http evidence extraction, reverse engineering, waf bypass, command execution path, memory artifact analysis |
| integer-overflow | 24 | command execution path, reverse engineering, http evidence extraction, stack control exploitation, memory artifact analysis |
| ret2text | 21 | stack control exploitation, gdb-driven evidence lookup, pwntools-driven evidence lookup, command execution path, http evidence extraction |
| crypto-analysis | 20 | http evidence extraction, reverse engineering, waf bypass, netcat-driven evidence lookup, checksec-driven evidence lookup |
| classical-crypto | 17 | http evidence extraction, reverse engineering, stack control exploitation, checksec-driven evidence lookup, cipher decoding |
| file-inclusion | 15 | file inclusion exploitation, http evidence extraction, reverse engineering, gdb-driven evidence lookup, memory artifact analysis |
| format-string | 14 | http evidence extraction, reverse engineering, command execution path, format-string control path, stack control exploitation |
| service-enumeration | 11 | file inclusion exploitation, http evidence extraction, command execution path, gdb-driven evidence lookup, credential discovery |
| browser-forensics | 6 | file inclusion exploitation, http evidence extraction, command execution path, credential discovery, gdb-driven evidence lookup |
| image-analysis | 6 | http evidence extraction, reverse engineering, memory artifact analysis, command execution path, file inclusion exploitation |
| symbolic-execution | 6 | reverse engineering, http evidence extraction, stack control exploitation, waf bypass, checksec-driven evidence lookup |
| misc-analysis | 5 | http evidence extraction, reverse engineering, checksec-driven evidence lookup, stack control exploitation, cipher decoding |
| malware-static | 3 | command execution path, capa-driven evidence lookup, file inclusion exploitation, gdb-driven evidence lookup, http evidence extraction |
| php-tricks | 3 | cipher decoding, http evidence extraction, reverse engineering, waf bypass, command execution path |
| privilege-escalation | 3 | file inclusion exploitation, command execution path, credential discovery, gdb-driven evidence lookup, http evidence extraction |
| qr-analysis | 3 | http evidence extraction, checksec-driven evidence lookup, reverse engineering, stack control exploitation, cipher decoding |
| osint | 2 | reverse engineering, checksec-driven evidence lookup, http evidence extraction, stack control exploitation, waf bypass |
| stego-extraction | 2 | command execution path, file inclusion exploitation, gdb-driven evidence lookup, http evidence extraction, pwntools-driven evidence lookup |
| dns-analysis | 1 | checksec-driven evidence lookup, http evidence extraction, reverse engineering, waf bypass |
| mobile-forensics | 1 | http evidence extraction, jadx-driven evidence lookup |
| sql-injection | 1 | cipher decoding, constraint solving, http evidence extraction, memory artifact analysis, reverse engineering |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 63 |
| reverse engineering | 54 |
| stack control exploitation | 52 |
| command execution path | 31 |
| memory artifact analysis | 29 |
| gdb-driven evidence lookup | 28 |
| netcat-driven evidence lookup | 23 |
| checksec-driven evidence lookup | 16 |
| pwntools-driven evidence lookup | 16 |
| waf bypass | 16 |
| file inclusion exploitation | 15 |
| timeline reconstruction | 8 |
| credential discovery | 7 |
| cipher decoding | 6 |
| format-string control path | 6 |
| ida-driven evidence lookup | 6 |
| integer-overflow bypass | 6 |
| evidence lookup | 3 |
| 无-driven evidence lookup | 3 |
| one-gadget-driven evidence lookup | 2 |
| radare2-driven evidence lookup | 2 |
| capa-driven evidence lookup | 1 |
| constraint solving | 1 |
| cyberchef-driven evidence lookup | 1 |
| ghidra-driven evidence lookup | 1 |
| IDA Pro 非必须-driven evidence lookup | 1 |
| IDA pro-driven evidence lookup | 1 |
| IDA-driven evidence lookup | 1 |
| incident timeline reconstruction | 1 |
| jadx-driven evidence lookup | 1 |
| ropgadget-driven evidence lookup | 1 |
| sql injection exploitation | 1 |
| stego extraction | 1 |
| tls handshake inspection | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [*CTF-2022 examination 题解_L3H_CoLin的博客-CSDN博客](../../../cards/docs-ctf-2022-examination-l3h-colin-csdn.md) | *CTF |  | binary-exploitation, ret2libc, waf-bypass, web-exploitation |
| [*CTF2021部分题目解题思路及exp_liucc09的博客-CSDN博客](../../../cards/docs-ctf2021-exp-liucc09-csdn.md) | *CTF2021部分题目解题思路及exp |  | binary-exploitation, crypto-analysis, encoding-analysis, ret2libc |
| [0ctf-2017-pwn-char 题解___lifanxin的博客-CSDN博客](../../../cards/docs-0ctf-2017-pwn-char-lifanxin-csdn.md) | 0ctf |  | binary-exploitation, ret2libc, stack-overflow, web-exploitation |
| [2016 ZCTF note2 题解_coco##的博客-CSDN博客](../../../cards/docs-2016-zctf-note2-coco-csdn.md) | 2016 ZCTF note2 题解 |  | binary-exploitation, encoding-analysis, integer-overflow, ret2libc |
| [2019 D^3CTF new_heap详细题解_ha1vk的博客-CSDN博客](../../../cards/docs-2019-d-3ctf-new-heap-ha1vk-csdn.md) | 2019 D^3CTF new |  | binary-exploitation, encoding-analysis, ret2libc, reverse-engineering |
| [2019 D^3CTF unprintableV详细题解_ha1vk的博客-CSDN博客](../../../cards/docs-2019-d-3ctf-unprintablev-ha1vk-csdn.md) | 2019 D^3CTF unprintableV详细题解 |  | binary-exploitation, encoding-analysis, file-inclusion, format-string |
| [2021dasctf七月赛 pwn题解复现（strdup,md5,protect,setcontext)_N1ch0l4s的博客-CSDN博客](../../../cards/docs-2021dasctf-pwn-strdup-md5-protect-setcontext-n1ch0l4s-csdn.md) | 2021dasctf |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [2021DNUICTF（东软杯CTF）的几个签到题writeup_Q1X1的博客-CSDN博客](../../../cards/docs-2021dnuictf-ctf-writeup-q1x1-csdn.md) | 2021DNUICTF（东软杯CTF）的几个签到题writeup |  | binary-exploitation, crypto-analysis, encoding-analysis, misc-analysis |
| [[BJDCTF 2020]babystack2.0](../../../cards/pwn-bjdctf-2020-babystack2-0.md) | BJDCTF 2020 |  | binary-exploitation, command-injection, http-analysis, integer-overflow |
| [[BUUCTF]PWN——铁人三项(第五赛区)_2018_rop_Angel~Yan的博客-CSDN博客_铁人三项(第五赛区)_2018_rop](../../../cards/docs-buuctf-pwn-2018-rop-angel-yan-csdn-2018-rop.md) | BUUCTF |  | binary-exploitation, ret2libc, reverse-engineering, web-exploitation |
| [[CISCN 2019华北]PWN1](../../../cards/pwn-ciscn-2019-pwn1.md) | CISCN 2019华北 |  | binary-exploitation, command-injection, http-analysis, ret2libc |
| [[FSCTF 2023]rdi](../../../cards/pwn-rdi.md) | FSCTF 2023 |  | binary-exploitation, http-analysis, ret2libc, ret2text |
| [[GFCTF 2021]where_is_shell](../../../cards/pwn-gfctf-2021-where-is-shell.md) | GFCTF 2021 |  | binary-exploitation, http-analysis, ret2libc, ret2text |
| [[GHCTF 2025]Hello_world](../../../cards/pwn-ghctf-2025-hello-world.md) | GHCTF 2025 |  | binary-exploitation, http-analysis, ret2text, reverse-engineering |
| [[GHCTF 2025]Hello_world](../../../cards/pwn-hello-world.md) | GHCTF 2025 |  | binary-exploitation, http-analysis, ret2libc, ret2text |
| [[HGAME 2023 week1]test_nc](../../../cards/pwn-test-nc.md) | HGAME 2023 week1 |  | binary-exploitation, encoding-analysis, http-analysis, reverse-engineering |
| [[HNCTF 2022 Week1]easyoverflow](../../../cards/pwn-hnctf-2022-week1-easyoverflow.md) | HNCTF 2022 Week1 |  | binary-exploitation, command-injection, file-inclusion, http-analysis |
| [[HNCTF 2022 WEEK4]checker](../../../cards/pwn-checker.md) | HNCTF 2022 WEEK4 |  | binary-exploitation, crypto-analysis, http-analysis, web-exploitation |
| [[LitCTF 2023]口算题卡](../../../cards/pwn-025e9586.md) | LitCTF 2023 |  | binary-exploitation, http-analysis, web-exploitation |
| [[MoeCTF 2021]ret2text_ez](../../../cards/pwn-ret2text-ez.md) | MoeCTF 2021 |  | binary-exploitation, http-analysis, ret2text, stack-overflow |
| [[NISACTF 2022]ezpie](../../../cards/pwn-ezpie.md) | NISACTF 2022 |  | binary-exploitation, http-analysis, ret2libc, ret2text |
| [[NISACTF 2022]ezpie](../../../cards/pwn-nisactf-2022-ezpie.md) | NISACTF 2022 |  | binary-exploitation, http-analysis, ret2text, reverse-engineering |
| [[NSSCTF 2022 Spring Recruit]R3m4ke?](../../../cards/pwn-r3m4ke.md) | NSSCTF 2022 Spring Recruit |  | binary-exploitation, http-analysis, ret2text, stack-overflow |
| [[SDCTF 2022]Horoscope](../../../cards/pwn-horoscope.md) | SDCTF 2022 |  | binary-exploitation, http-analysis, ret2text, stack-overflow |
| [[SUCTF 2018 招新赛]stack](../../../cards/pwn-stack.md) | SUCTF 2018 招新赛 |  | binary-exploitation, http-analysis, ret2text, stack-overflow |
| [[SWPUCTF 2021 新生赛]gift_pwn](../../../cards/pwn-swpuctf-2021-gift-pwn.md) | SWPUCTF 2021 新生赛 |  | binary-exploitation, command-injection, http-analysis, ret2libc |
| [[SWPUCTF 2022 新生赛]FindanotherWay](../../../cards/pwn-findanotherway.md) | SWPUCTF 2022 新生赛 |  | binary-exploitation, http-analysis, reverse-engineering, stack-overflow |
| [[SWPUCTF 2022 新生赛]Integer Overflow](../../../cards/pwn-integeroverflow.md) | SWPUCTF 2022 新生赛 |  | binary-exploitation, http-analysis, integer-overflow, ret2libc |
| [[SWPUCTF 2023 秋季新生赛]ezlibc](../../../cards/pwn-ezlibc.md) | SWPUCTF 2023 秋季新生赛 |  | binary-exploitation, encoding-analysis, http-analysis, ret2libc |
| [[SWPUCTF 2024 秋季新生赛]又是签到！？](../../../cards/pwn-63e2f2f1.md) | SWPUCTF 2024 秋季新生赛 |  | binary-exploitation, http-analysis, mobile-forensics, web-exploitation |
| [[WUSTCTF 2020]getshell2](../../../cards/pwn-wustctf-2020-getshell2.md) | WUSTCTF 2020 |  | binary-exploitation, command-injection, http-analysis, ret2libc |
| [[WUSTCTF 2020]level1](../../../cards/pwn-level1.md) | WUSTCTF 2020 |  | binary-exploitation, http-analysis, reverse-engineering, web-exploitation |
| [Asis CTF 2016 b00ks理解_weixin_30666753的博客-CSDN博客](../../../cards/docs-asis-ctf-2016-b00ks-weixin-30666753-csdn.md) | Asis CTF 2016 b00ks理解 |  | binary-exploitation, web-exploitation |
| [babyfengshui [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列23_3riC5r的博客-CSDN博客](../../../cards/docs-babyfengshui-xctf-pwn-ctf-writeup-23-3ric5r-csdn.md) | babyfengshui [XCTF |  | binary-exploitation, command-injection, integer-overflow, malware-static |
| [boston-key-party-2016-pwn-simple_calc 题解___lifanxin的博客-CSDN博客](../../../cards/docs-boston-key-party-2016-pwn-simple-calc-lifanxin-csdn.md) | boston |  | binary-exploitation, crypto-analysis, ret2libc, reverse-engineering |
| [BSides Delhi CTF 2018部分pwn题题解_Peanuts_CTF的博客-CSDN博客](../../../cards/docs-bsides-delhi-ctf-2018-pwn-peanuts-ctf-csdn.md) | BSides Delhi CTF 2018部分pwn题题解 |  | binary-exploitation, ret2libc, reverse-engineering, waf-bypass |
| [BugkuCTF-PWN题pwn2-overflow超详细讲解_彬彬有礼am_03的博客-CSDN博客_bugkupwn2](../../../cards/docs-bugkuctf-pwn-pwn2-overflow-am-03-csdn-bugkupwn2.md) | BugkuCTF |  | binary-exploitation, reverse-engineering, stack-overflow, web-exploitation |
| [BugkuCTF-PWN题pwn7-repeater详细讲解多解法_彬彬有礼am_03的博客-CSDN博客](../../../cards/docs-bugkuctf-pwn-pwn7-repeater-am-03-csdn.md) | BugkuCTF |  | binary-exploitation, command-injection, encoding-analysis, format-string |
| [BUUCTF (PWN) RIP详细分析_qy201706的博客-CSDN博客_buuctf rip](../../../cards/docs-buuctf-pwn-rip-qy201706-csdn-buuctf-rip.md) | BUUCTF (PWN) RIP详细分析 |  | binary-exploitation, reverse-engineering, stack-overflow, web-exploitation |
| [BUUCTF ciscn_2019_c_1__N1rvana_的博客-CSDN博客](../../../cards/docs-buuctf-ciscn-2019-c-1-n1rvana-csdn.md) | BUUCTF ciscn |  | binary-exploitation, crypto-analysis, encoding-analysis, http-analysis |
| [buuctf pwn刷题（1）_qingmu-z的博客-CSDN博客_buuctf pwn1](../../../cards/docs-buuctf-pwn-1-qingmu-z-csdn-buuctf-pwn1.md) | buuctf pwn刷题（1） |  | binary-exploitation, command-injection, ret2libc, reverse-engineering |
| [buuctf:ciscn_s_3题解_xi@0ji233的博客-CSDN博客](../../../cards/docs-buuctf-ciscn-s-3-xi-0ji233-csdn.md) | buuctf:ciscn |  | binary-exploitation, classical-crypto, file-inclusion, http-analysis |
| [buuctf[cmcc_pwnme1]题解_N1ch0l4s的博客-CSDN博客](../../../cards/docs-buuctf-cmcc-pwnme1-n1ch0l4s-csdn.md) | buuctf[cmcc |  | binary-exploitation, encoding-analysis, ret2libc, stack-overflow |
| [buuctf解题记录_song-10的博客-CSDN博客_buuctf解题](../../../cards/docs-buuctf-song-10-csdn-buuctf.md) | buuctf解题记录 |  | binary-exploitation, command-injection, encoding-analysis, file-inclusion |
| [CG-ctf中RE Hello,RE和ReadAsm2超详细题解_jovy-rtt的博客-CSDN博客](../../../cards/docs-cg-ctf-re-hello-re-readasm2-jovy-rtt-csdn.md) | CG |  | http-analysis, reverse-engineering, web-exploitation |
| [CSAWCTF-2018-pwn-shellcode 题解___lifanxin的博客-CSDN博客](../../../cards/docs-csawctf-2018-pwn-shellcode-lifanxin-csdn.md) | CSAWCTF |  | binary-exploitation, command-injection, encoding-analysis, ret2libc |
| [CTF pwn -- ARM架构的pwn题详解___lifanxin的博客-CSDN博客](../../../cards/docs-ctf-pwn-arm-pwn-lifanxin-csdn.md) | CTF pwn |  | binary-exploitation, command-injection, ret2libc, reverse-engineering |
| [CTF pwn 方向部分题解_普通网友的博客-CSDN博客_ctfpwn方向比赛题目及解析](../../../cards/docs-ctf-pwn-csdn-ctfpwn.md) | CTF pwn 方向部分题解 |  | binary-exploitation, classical-crypto, command-injection, encoding-analysis |
| [CTF pwn题之虚拟机题型详解___lifanxin的博客-CSDN博客_pwn题型](../../../cards/docs-ctf-pwn-lifanxin-csdn-pwn.md) | CTF pwn题之虚拟机题型详解 |  | binary-exploitation |
| [ctf xor题_2020 KCTF秋季赛 | 第九题设计及解题思路_当下的幸福的博客-CSDN博客](../../../cards/docs-ctf-xor-2020-kctf-csdn.md) | ctf xor题 |  | binary-exploitation, file-inclusion, http-analysis, ret2libc |
| [ctf-wiki ARM ROP Codegate2018_Melong题解_flypwn的博客-CSDN博客](../../../cards/docs-ctf-wiki-arm-rop-codegate2018-melong-flypwn-csdn.md) | ctf |  | binary-exploitation, classical-crypto, command-injection, encoding-analysis |
| [ctf.bugku ctf题目详解——pwn2_yeshen4328的博客-CSDN博客](../../../cards/docs-ctf-bugku-ctf-pwn2-yeshen4328-csdn.md) | ctf.bugku ctf题目详解——pwn2 |  | binary-exploitation, reverse-engineering, stack-overflow |
| [CTF|pwn栈溢出入门题level3解题思路及个人总结_一个不融化的雪人的博客-CSDN博客_ctf pwn 栈溢出](../../../cards/docs-ctf-pwn-level3-csdn-ctf-pwn.md) | CTF|pwn栈溢出入门题level3解题思路及个人总结 |  | binary-exploitation, misc-analysis, ret2libc, reverse-engineering |
| [CTF|pwn栈溢出题目int_overflow解题思路及个人总结_一个不融化的雪人的博客-CSDN博客_ctfpwn栈溢出](../../../cards/docs-ctf-pwn-int-overflow-csdn-ctfpwn.md) | CTF|pwn栈溢出题目int |  | binary-exploitation, integer-overflow, reverse-engineering, stack-overflow |
| [CTF|入门题目when_did_you_born解题思路以个人总结_一个不融化的雪人的博客-CSDN博客](../../../cards/docs-ctf-when-did-you-born-csdn.md) | CTF|入门题目when |  | binary-exploitation, image-analysis, reverse-engineering, stack-overflow |
| [CTF|栈溢出入门题hellopwn解题思路_一个不融化的雪人的博客-CSDN博客_pwn解题思路](../../../cards/docs-ctf-hellopwn-csdn-pwn.md) | CTF|栈溢出入门题hellopwn解题思路 |  | binary-exploitation, ret2libc, reverse-engineering, stack-overflow |
| [CTF|栈溢出入门题level0解题思路及个人总结_一个不融化的雪人的博客-CSDN博客_栈溢出ctf](../../../cards/docs-ctf-level0-csdn-ctf.md) | CTF|栈溢出入门题level0解题思路及个人总结 |  | binary-exploitation, command-injection, ret2libc, reverse-engineering |
| [dice_game [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列12_3riC5r的博客-CSDN博客_dice game](../../../cards/docs-dice-game-xctf-pwn-ctf-writeup-12-3ric5r-csdn-dice-game.md) | dice |  | binary-exploitation, integer-overflow, stack-overflow, web-exploitation |
| [EASYHOOK XCTF 4TH-WHCTF-2017 攻防世界 通过此题理解hook钩子_hincon的博客-CSDN博客](../../../cards/docs-easyhook-xctf-4th-whctf-2017-hook-hincon-csdn.md) | EASYHOOK XCTF 4TH |  | binary-exploitation |
| [forgot [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列13_3riC5r的博客-CSDN博客](../../../cards/docs-forgot-xctf-pwn-ctf-writeup-13-3ric5r-csdn.md) | forgot [XCTF |  | binary-exploitation, command-injection, ret2libc, reverse-engineering |
| [get_started_3dsctf_2016 1_一路开花●-●的博客-CSDN博客](../../../cards/docs-get-started-3dsctf-2016-1-csdn.md) | get |  | binary-exploitation, classical-crypto, file-inclusion, reverse-engineering |
| [get_started_3dsctf_2016 题解___lifanxin的博客-CSDN博客_get_started_3dsctf_2016](../../../cards/docs-get-started-3dsctf-2016-lifanxin-csdn-get-started-3dsctf-2016.md) | get |  | binary-exploitation, classical-crypto, reverse-engineering, stack-overflow |
| [glibc2.31下的新double free手法/字节跳动pwn题gun题解_一只狗20000402的博客-CSDN博客](../../../cards/docs-glibc2-31-double-free-pwn-gun-20000402-csdn.md) | glibc2.31下的新double free手法/字节跳动pwn题gun题解 |  | binary-exploitation, command-injection, crypto-analysis, encoding-analysis |
| [GXYCTF部分详细题解_合天网安实验室的博客-CSDN博客](../../../cards/docs-gxyctf-csdn.md) | GXYCTF部分详细题解 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [HgameCTF(week1)-RE,PWN题解析_合天网安实验室的博客-CSDN博客](../../../cards/docs-hgamectf-week1-re-pwn-csdn.md) | HgameCTF(week1) |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [linux sort 0x7f,【真题解析】浅析CTF中PWN题型的解题思路_余曉波的博客-CSDN博客](../../../cards/docs-linux-sort-0x7f-ctf-pwn-csdn.md) | linux sort 0x7f,【真题解析】浅析CTF中PWN题型的解题思路 |  | binary-exploitation, encoding-analysis, format-string, http-analysis |
| [Mary_Morton [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列17_3riC5r的博客-CSDN博客](../../../cards/docs-mary-morton-xctf-pwn-ctf-writeup-17-3ric5r-csdn.md) | Mary |  | binary-exploitation, command-injection, format-string, ret2libc |
| [monkey [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列18_3riC5r的博客-CSDN博客](../../../cards/docs-monkey-xctf-pwn-ctf-writeup-18-3ric5r-csdn.md) | monkey [XCTF |  | binary-exploitation, command-injection, crypto-analysis, ret2libc |
| [NepCTF2021个人赛_Sakura给爷pwn全场的博客-CSDN博客](../../../cards/docs-nepctf2021-sakura-pwn-csdn.md) | NepCTF2021个人赛 |  | binary-exploitation |
| [off by one --- Asis CTF 2016 b00ks题解_coco##的博客-CSDN博客](../../../cards/docs-off-by-one-asis-ctf-2016-b00ks-coco-csdn.md) | off by one |  | binary-exploitation, encoding-analysis, ret2libc, reverse-engineering |
| [Openctf-2016-pwn-apprentice_www 题解___lifanxin的博客-CSDN博客](../../../cards/docs-openctf-2016-pwn-apprentice-www-lifanxin-csdn.md) | Openctf |  | binary-exploitation, classical-crypto |
| [play [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列26（超详细分析）_3riC5r的博客-CSDN博客](../../../cards/docs-play-xctf-pwn-ctf-writeup-26-3ric5r-csdn.md) | play [XCTF |  | binary-exploitation, integer-overflow, service-enumeration, stack-overflow |
| [PWN bof [pwnable.kr]CTF writeup题解系列3_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-bof-pwnable-kr-ctf-writeup-3-3ric5r-csdn.md) | PWN bof [pwnable.kr]CTF writeup题解系列3 |  | binary-exploitation, command-injection, crypto-analysis, file-inclusion |
| [PWN dragon echo1 echo2 [pwnable.kr]CTF writeup题解系列16_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-dragon-echo1-echo2-pwnable-kr-ctf-writeup-16-3ric5r-csdn.md) | PWN dragon echo1 echo2 |  | binary-exploitation, format-string, integer-overflow, reverse-engineering |
| [PWN horcruxes [pwnable.kr]CTF writeup题解系列15_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-horcruxes-pwnable-kr-ctf-writeup-15-3ric5r-csdn.md) | PWN horcruxes |  | binary-exploitation, command-injection, service-enumeration, stack-overflow |
| [PWN input [pwnable.kr]CTF writeup题解系列7_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-input-pwnable-kr-ctf-writeup-7-3ric5r-csdn.md) | PWN input [pwnable.kr]CTF writeup题解系列7 |  | binary-exploitation, browser-forensics, command-injection, file-inclusion |
| [PWN mistake [pwnable.kr]CTF writeup题解系列8_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-mistake-pwnable-kr-ctf-writeup-8-3ric5r-csdn.md) | PWN mistake [pwnable.kr]CTF writeup题解系列8 |  | binary-exploitation, browser-forensics, command-injection, crypto-analysis |
| [PWN passcode [pwnable.kr]CTF writeup题解系列5_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-passcode-pwnable-kr-ctf-writeup-5-3ric5r-csdn.md) | PWN passcode |  | binary-exploitation, browser-forensics, command-injection, file-inclusion |
| [PWN random [pwnable.kr]CTF writeup题解系列6_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-random-pwnable-kr-ctf-writeup-6-3ric5r-csdn.md) | PWN random [pwnable.kr]CTF writeup题解系列6 |  | binary-exploitation, browser-forensics, command-injection, crypto-analysis |
| [PWN shellshock [pwnable.kr]CTF writeup题解系列9_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-shellshock-pwnable-kr-ctf-writeup-9-3ric5r-csdn.md) | PWN shellshock |  | binary-exploitation, browser-forensics, command-injection, file-inclusion |
| [PWN uaf [pwnable.kr]CTF writeup题解系列13_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-uaf-pwnable-kr-ctf-writeup-13-3ric5r-csdn.md) | PWN uaf [pwnable.kr]CTF writeup题解系列13 |  | binary-exploitation, browser-forensics, classical-crypto, command-injection |
| [PWN unlink [pwnable.kr]CTF writeup题解系列14（包含本地解决方法）_3riC5r的博客-CSDN博客](../../../cards/docs-pwn-unlink-pwnable-kr-ctf-writeup-14-3ric5r-csdn.md) | PWN unlink |  | binary-exploitation, service-enumeration, web-exploitation |
| [pwn1 babystack [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列19_3riC5r的博客-CSDN博客_pwn题babystack](../../../cards/docs-pwn1-babystack-xctf-pwn-ctf-writeup-19-3ric5r-csdn-pwn-babystack.md) | pwn1 babystack [XCTF |  | binary-exploitation, command-injection, ret2libc, reverse-engineering |
| [pwn100 [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列16_3riC5r的博客-CSDN博客](../../../cards/docs-pwn100-xctf-pwn-ctf-writeup-16-3ric5r-csdn.md) | pwn100 [XCTF |  | binary-exploitation, command-injection, integer-overflow, ret2libc |
| [pwn200 [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列21_3riC5r的博客-CSDN博客](../../../cards/docs-pwn200-xctf-pwn-ctf-writeup-21-3ric5r-csdn.md) | pwn200 [XCTF |  | binary-exploitation, ret2libc, stack-overflow, web-exploitation |
| [PWNctf的pwn题解析_Peanuts_CTF的博客-CSDN博客_ctfpwn题](../../../cards/docs-pwnctf-pwn-peanuts-ctf-csdn-ctfpwn.md) | PWNctf的pwn题解析 |  | binary-exploitation, encoding-analysis, ret2libc, reverse-engineering |
| [ReeHY-main-100 [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列22_3riC5r的博客-CSDN博客](../../../cards/docs-4-reehy-main-100-xctf-pwn-ctf-writeup-22-3ric5r-csdn.md) | ReeHY |  | binary-exploitation, integer-overflow, stack-overflow, web-exploitation |
| [Seccon-ctf-2016-pwn-cheer_msg 题解___lifanxin的博客-CSDN博客](../../../cards/docs-seccon-ctf-2016-pwn-cheer-msg-lifanxin-csdn.md) | Seccon |  | binary-exploitation, command-injection, encoding-analysis, ret2libc |
| [shell [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列25_3riC5r的博客-CSDN博客](../../../cards/docs-shell-xctf-pwn-ctf-writeup-25-3ric5r-csdn.md) | shell [XCTF |  | binary-exploitation, file-inclusion, integer-overflow, reverse-engineering |
| [stack2 [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列15_3riC5r的博客-CSDN博客](../../../cards/docs-stack2-xctf-pwn-ctf-writeup-15-3ric5r-csdn.md) | stack2 [XCTF |  | binary-exploitation, command-injection, integer-overflow, ret2libc |
| [swpuctf2019 Login pwn详细题解_ha1vk的博客-CSDN博客](../../../cards/docs-swpuctf2019-login-pwn-ha1vk-csdn.md) | swpuctf2019 Login pwn详细题解 |  | binary-exploitation, encoding-analysis, format-string, ret2libc |
| [swpuctf2019 p1KkHeap 详细题解_ha1vk的博客-CSDN博客](../../../cards/docs-swpuctf2019-p1kkheap-ha1vk-csdn.md) | swpuctf2019 p1KkHeap 详细题解 |  | binary-exploitation, classical-crypto, encoding-analysis, file-inclusion |
| [team [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列28（网站配置错误，需自行配置本地环境测试）_3riC5r的博客-CSDN博客_攻防世界创建动态环境失败](../../../cards/docs-team-xctf-pwn-ctf-writeup-28-3ric5r-csdn.md) | team [XCTF |  | binary-exploitation, encoding-analysis, format-string, integer-overflow |
| [time_formatter [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列20_3riC5r的博客-CSDN博客](../../../cards/docs-time-formatter-xctf-pwn-ctf-writeup-20-3ric5r-csdn.md) | time |  | binary-exploitation, command-injection, format-string, integer-overflow |
| [troia_server [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列27(未完待续）_3riC5r的博客-CSDN博客](../../../cards/docs-troia-server-xctf-pwn-ctf-writeup-27-3ric5r-csdn.md) | troia |  | binary-exploitation, crypto-analysis, integer-overflow, reverse-engineering |
| [unctf2019 pwn部分题解_NoOneGroup的博客-CSDN博客](../../../cards/docs-unctf2019-pwn-noonegroup-csdn.md) | unctf2019 pwn部分题解 |  | binary-exploitation, classical-crypto, command-injection, encoding-analysis |
| [warmup [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列14_3riC5r的博客-CSDN博客](../../../cards/docs-warmup-xctf-pwn-ctf-writeup-14-3ric5r-csdn.md) | warmup [XCTF |  | binary-exploitation, web-exploitation |
| [welpwn [XCTF-PWN][高手进阶区]CTF writeup攻防世界题解系列24_3riC5r的博客-CSDN博客_welpwn](../../../cards/docs-welpwn-xctf-pwn-ctf-writeup-24-3ric5r-csdn-welpwn.md) | welpwn [XCTF |  | binary-exploitation, reverse-engineering, web-exploitation |
| [”BUUCTF之pwn题解（一些栈题+程序分析）_swedsn的博客-CSDN博客_buuctf pwn](../../../cards/docs-buuctf-pwn-swedsn-csdn-buuctf-pwn.md) | ”BUUCTF之pwn题解（一些栈题+程序分析） |  | binary-exploitation, command-injection, encoding-analysis, format-string |
| [【CTF题解NO.00001】西安电子科技大学网络与信息安全学院2020年网络空间安全专业实验班选拔考试 - write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00001-2020-write-up-by-arttnba3-arttnba3-csdn.md) | docs |  | binary-exploitation, classical-crypto, dns-analysis, encoding-analysis |
| [【CTF题解NO.00002】minilCTF 2020 - write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00002-minilctf-2020-write-up-by-arttnba3-arttnba3-csdn.md) | 【CTF题解NO.00002】minilCTF 2020 |  | binary-exploitation, command-injection, http-analysis, integer-overflow |
| [【CTF题解NO.00003】moeCTF 2020 - official write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00003-moectf-2020-official-write-up-by-arttnba3-arttnba3-csdn.md) | 【CTF题解NO.00003】moeCTF 2020 |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [【CTF题解NO.00004】BUUCTF/BUUOJ - Pwn write up by arttnb3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00004-buuctf-buuoj-pwn-write-up-by-arttnb3-arttnba3-csdn.md) | 【CTF题解NO.00004】BUUCTF/BUUOJ |  | binary-exploitation, classical-crypto, command-injection, crypto-analysis |
| [【CTF题解NO.00005】ByteCTF2020 - pwn - write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00005-bytectf2020-pwn-write-up-by-arttnba3-arttnba3-csdn.md) | 【CTF题解NO.00005】ByteCTF2020 |  | binary-exploitation, encoding-analysis, ret2libc, reverse-engineering |
| [【CTF题解NO.00006】*CTF2021 - pwn - write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00006-ctf2021-pwn-write-up-by-arttnba3-arttnba3-csdn.md) | 【CTF题解NO.00006】*CTF2021 |  | binary-exploitation, command-injection, encoding-analysis, ret2libc |
| [【CTF题解NO.00007】VNCTF2021 - pwn - write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00007-vnctf2021-pwn-write-up-by-arttnba3-arttnba3-csdn.md) | 【CTF题解NO.00007】VNCTF2021 |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [【CTF题解NO.00008】mini-LCTF 2021 official write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00008-mini-lctf-2021-official-write-up-by-arttnba3-arttnba3-csdn.md) | 【CTF题解NO.00008】mini |  | binary-exploitation, classical-crypto, crypto-analysis, encoding-analysis |
| [【CTF题解NO.00009】CISCN2021-初赛-pwn write up by arttnba3_arttnba3的博客-CSDN博客](../../../cards/docs-ctf-no-00009-ciscn2021-pwn-write-up-by-arttnba3-arttnba3-csdn.md) | 【CTF题解NO.00009】CISCN2021 |  | binary-exploitation, crypto-analysis, encoding-analysis, image-analysis |
| [一道逆向CTF题-read asm详解_sherlly666的博客-CSDN博客](../../../cards/docs-ctf-read-asm-sherlly666-csdn.md) | 一道逆向CTF题 |  | binary-exploitation |
| [信息安全铁人三项赛真题解析_【ctf】2018信息安全铁人三项赛个人赛总决赛赛题分享..._weixin_39573512的博客-CSDN博客](../../../cards/docs-ctf-2018-weixin-39573512-csdn.md) | 信息安全铁人三项赛真题解析 |  | binary-exploitation, encoding-analysis |
| [信息安全铁人三项赛真题解析_对 [CrackMe] 【ctf】2018信息安全铁人三项赛个人赛总决赛赛题分享 的一些补充..._weixin_39587238的博客-CSDN博客](../../../cards/docs-crackme-ctf-2018-weixin-39587238-csdn.md) | 信息安全铁人三项赛真题解析 |  | binary-exploitation, encoding-analysis, http-analysis, ret2libc |
| [南邮CTF逆向题第二道ReadAsm2解题思路_iqiqiya的博客-CSDN博客](../../../cards/docs-ctf-readasm2-iqiqiya-csdn.md) | 南邮CTF逆向题第二道ReadAsm2解题思路 |  | binary-exploitation |
| [厄了吗](../../../cards/pwn-gccctf-2025.md) | GCCCTF 2025 |  | binary-exploitation, command-injection, crypto-analysis, encoding-analysis |
| [昔涟的礼物](../../../cards/pwn-gccctf-2025.md) | GCCCTF 2025 |  | binary-exploitation, command-injection, reverse-engineering, stack-overflow |
| [由一道CTF pwn题深入理解libc2.26中的tcache机制_weixin_30363981的博客-CSDN博客](../../../cards/docs-ctf-pwn-libc2-26-tcache-weixin-30363981-csdn.md) | 由一道CTF pwn题深入理解libc2.26中的tcache机制 |  | binary-exploitation, http-analysis, ret2libc, web-exploitation |
| [砰砰砰！2021美团CTF决赛PWN题详解_代码熬夜敲的博客-CSDN博客](../../../cards/docs-2021-ctf-pwn-csdn.md) | 砰砰砰！2021美团CTF决赛PWN题详解 |  | binary-exploitation, command-injection, encoding-analysis, format-string |
| [绝对详细的babyheap_0ctf_2017题解_eeeeeeeeeeeeeeeea的博客-CSDN博客](../../../cards/docs-babyheap-0ctf-2017-eeeeeeeeeeeeeeeea-csdn.md) | 绝对详细的babyheap |  | binary-exploitation, encoding-analysis, ret2libc, web-exploitation |
| [辣卤客，我为你带来烩面啦！](../../../cards/pwn-gccctf-2025.md) | GCCCTF 2025 |  | binary-exploitation, command-injection, encoding-analysis, http-analysis |
