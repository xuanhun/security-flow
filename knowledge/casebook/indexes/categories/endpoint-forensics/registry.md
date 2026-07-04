# Endpoint Forensics / registry

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| http-analysis | 38 | http evidence extraction, timeline reconstruction, dns pivot, registry artifact correlation, event-log correlation |
| timeline-analysis | 32 | http evidence extraction, timeline reconstruction, dns pivot, registry artifact correlation, event-log correlation |
| dns-analysis | 26 | dns pivot, http evidence extraction, timeline reconstruction, registry artifact correlation, event-log correlation |
| windows-event-analysis | 26 | http evidence extraction, event-log correlation, timeline reconstruction, dns pivot, registry artifact correlation |
| browser-forensics | 25 | http evidence extraction, timeline reconstruction, dns pivot, registry artifact correlation, credential discovery |
| cti-enrichment | 24 | http evidence extraction, dns pivot, event-log correlation, registry artifact correlation, indicator enrichment |
| registry-forensics | 20 | http evidence extraction, timeline reconstruction, registry artifact correlation, dns pivot, credential discovery |
| memory-forensics | 14 | http evidence extraction, registry artifact correlation, memory artifact analysis, indicator enrichment, credential discovery |
| malware-static | 13 | http evidence extraction, credential discovery, registry artifact correlation, timeline reconstruction, memory artifact analysis |
| stego-extraction | 13 | http evidence extraction, registry artifact correlation, timeline reconstruction, credential discovery, dns pivot |
| malware-dynamic | 10 | dns pivot, event-log correlation, http evidence extraction, timeline reconstruction, file metadata extraction |
| privilege-escalation | 9 | http evidence extraction, timeline reconstruction, event-log correlation, indicator enrichment, credential discovery |
| service-enumeration | 7 | timeline reconstruction, http evidence extraction, credential discovery, indicator enrichment, db-browser-sqlite-driven evidence lookup |
| maldoc-analysis | 4 | maldoc analysis, dns pivot, http evidence extraction, db-browser-sqlite-driven evidence lookup, event-log correlation |
| reverse-engineering | 4 | reverse engineering, dns pivot, file metadata extraction, timeline reconstruction, event-log correlation |
| network-forensics | 3 | dns pivot, http evidence extraction, registry artifact correlation, timeline reconstruction, cyberchef-driven evidence lookup |
| password-cracking | 2 | cyberchef-driven evidence lookup, dns pivot, event-log correlation, indicator enrichment, reverse engineering |
| email-header-analysis | 1 | cyberchef-driven evidence lookup, dns pivot, event-log correlation, indicator enrichment |
| siem-query | 1 | reverse engineering |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 31 |
| timeline reconstruction | 22 |
| registry artifact correlation | 21 |
| dns pivot | 20 |
| event-log correlation | 15 |
| memory artifact analysis | 13 |
| credential discovery | 12 |
| indicator enrichment | 10 |
| file metadata extraction | 9 |
| db-browser-sqlite-driven evidence lookup | 7 |
| autopsy-driven evidence lookup | 5 |
| ftk-imager-driven evidence lookup | 4 |
| maldoc analysis | 4 |
| cyberchef-driven evidence lookup | 3 |
| layer-2 endpoint identification | 3 |
| reverse engineering | 3 |
| evtxecmd-driven evidence lookup | 2 |
| service-to-access path | 2 |
| strings-driven evidence lookup | 2 |
| tls handshake inspection | 2 |
| memprocfs-driven evidence lookup | 1 |
| mftecmd-driven evidence lookup | 1 |
| olevba-driven evidence lookup | 1 |
| registry-explorer-driven evidence lookup | 1 |
| virustotal-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Akira Lab](../../../cards/cyber-defenders-akira-lab.md) | CyberDefedners | Medium | dns-analysis, http-analysis, malware-static, memory-forensics |
| [Andromeda Bot Lab](../../../cards/cyber-defenders-andromeda-bot-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, memory-forensics |
| [BankingTroubles Lab](../../../cards/cyber-defenders-bankingtroubles-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Beta Gamer Lab](../../../cards/cyber-defenders-beta-gamer-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, privilege-escalation, timeline-analysis |
| [Chollima Lab](../../../cards/cyber-defenders-chollima-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, privilege-escalation |
| [Chollima Lab](../../../cards/cyber-defenders-weblogic-lab.md) | CyberDefenders | Medium | http-analysis, malware-static, memory-forensics, stego-extraction |
| [CorporateSecrets Lab](../../../cards/cyber-defenders-corporatesecrets-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [CrownJewel1](../../../cards/crownjewel1.md) | HackTheBox | Easy | dns-analysis, http-analysis, malware-dynamic, reverse-engineering |
| [Dead End?](../../../cards/dead-end.md) | TryHackMe | Hard | cti-enrichment, memory-forensics |
| [DetectLog4j Lab](../../../cards/cyber-defenders-detectlog4j-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, malware-dynamic |
| [DiskFiltration](../../../cards/diskfiltration.md) | TryHackMe | Hard | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [Fog Ransomware Lab](../../../cards/cyber-defenders-fog-ransomware-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, privilege-escalation |
| [Forensics](../../../cards/forensics.md) | TryHackMe | Hard | browser-forensics, cti-enrichment, malware-static, memory-forensics |
| [HireMe Lab](../../../cards/cyber-defenders-hireme-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [Hunter Lab](../../../cards/cyber-defenders-hunter-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [IcedID 2 Lab](../../../cards/cyber-defenders-icedid-2-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, memory-forensics |
| [Injector Lab](../../../cards/cyber-defenders-injector-lab.md) | CyberDefenders | Medium | http-analysis, malware-static, memory-forensics, registry-forensics |
| [Job Trap Lab](../../../cards/cyber-defenders-job-trap-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, maldoc-analysis, malware-dynamic |
| [KioskExpo7 Lab](../../../cards/cyber-defenders-kioskexpo7-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, malware-dynamic, malware-static |
| [Lockbit](../../../cards/lockbit.md) | LetsDefend | Easy | cti-enrichment, http-analysis, memory-forensics, privilege-escalation |
| [LummaStealer Lab](../../../cards/cyber-defenders-lummastealer-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Malicious PyPi Lab](../../../cards/cyber-defenders-malicious-pypi-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, malware-dynamic |
| [Maranhao Lab](../../../cards/cyber-defenders-maranhao-lab.md) | CyberDefenders | Easy | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [MeteorHit Lab](../../../cards/cyber-defenders-meteorhit-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, malware-dynamic |
| [MinerHunt Lab](../../../cards/cyber-defenders-minerhunt-lab.md) | CyberDefenders | Medium | cti-enrichment, http-analysis, malware-static, privilege-escalation |
| [MrRobot Lab](../../../cards/cyber-defenders-mrrobot-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [NetX-Support Lab](../../../cards/cyber-defenders-netx-support-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, malware-static |
| [NintendoHunt Lab](../../../cards/cyber-defenders-nintendohunt-lab.md) | CyberDefenders | Hard | http-analysis, malware-static, memory-forensics, service-enumeration |
| [Operationa Blackout 2025: Phantom Check](../../../cards/operation-blackout-2025-phantom-check.md) | HackTheBox | Easy | dns-analysis, timeline-analysis, windows-event-analysis |
| [Phishy Lab](../../../cards/cyber-defenders-phishy-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [PwnedDC Lab](../../../cards/cyber-defenders-pwneddc-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [RepoReaper Lab](../../../cards/cyber-defenders-reporeaper-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [RevengeHotels APT Lab](../../../cards/cyber-defenders-revengehotels-apt-lab.md) | CyberDefenders | Easy | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Secret Recipe](../../../cards/secret-recipe.md) | TryHackMe | Medium | dns-analysis, http-analysis, network-forensics, registry-forensics |
| [SpottedInTheWild Lab](../../../cards/cyber-defenders-spottedinthewild-lab.md) | CyberDefenders | Hard | cti-enrichment, http-analysis, malware-static, registry-forensics |
| [Sysinternals](../../../cards/cyber-defenders-sysinternals-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, registry-forensics |
| [Szechuan Sauce Lab](../../../cards/cyber-defenders-szechuan-suace-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, memory-forensics |
| [Tempest](../../../cards/temptest-writeup.md) | TryHackMe | Medium | cti-enrichment, dns-analysis, email-header-analysis, http-analysis |
| [Trigona Ransomware Lab](../../../cards/cyber-defenders-trigona-ransomware-lab.md) | CyberDefenders | Medium | cti-enrichment, http-analysis, memory-forensics, registry-forensics |
| [Unattended](../../../cards/unattended.md) | TryHackMe | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [VaultBreak Lab](../../../cards/cyber-defenders-vaultbreak-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, maldoc-analysis |
| [Zerologon Lab](../../../cards/cyber-defenders-zerologon-lab.md) | CyberDefenders | Hard | browser-forensics, dns-analysis, http-analysis, malware-dynamic |
