# Endpoint Forensics / disk-image

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| http-analysis | 33 | http evidence extraction, timeline reconstruction, registry artifact correlation, credential discovery, dns pivot |
| timeline-analysis | 29 | http evidence extraction, timeline reconstruction, registry artifact correlation, memory artifact analysis, event-log correlation |
| browser-forensics | 27 | http evidence extraction, timeline reconstruction, credential discovery, registry artifact correlation, dns pivot |
| dns-analysis | 20 | http evidence extraction, dns pivot, timeline reconstruction, registry artifact correlation, credential discovery |
| registry-forensics | 20 | timeline reconstruction, http evidence extraction, registry artifact correlation, dns pivot, credential discovery |
| windows-event-analysis | 20 | http evidence extraction, timeline reconstruction, event-log correlation, dns pivot, registry artifact correlation |
| cti-enrichment | 19 | http evidence extraction, timeline reconstruction, event-log correlation, registry artifact correlation, indicator enrichment |
| malware-static | 12 | http evidence extraction, timeline reconstruction, credential discovery, memory artifact analysis, registry artifact correlation |
| stego-extraction | 12 | http evidence extraction, timeline reconstruction, credential discovery, registry artifact correlation, ftk-imager-driven evidence lookup |
| malware-dynamic | 10 | event-log correlation, http evidence extraction, timeline reconstruction, memory artifact analysis, dns pivot |
| memory-forensics | 9 | http evidence extraction, memory artifact analysis, registry artifact correlation, timeline reconstruction, indicator enrichment |
| service-enumeration | 9 | timeline reconstruction, indicator enrichment, credential discovery, http evidence extraction, memory artifact analysis |
| privilege-escalation | 7 | http evidence extraction, timeline reconstruction, credential discovery, file metadata extraction, indicator enrichment |
| maldoc-analysis | 4 | maldoc analysis, dns pivot, http evidence extraction, db-browser-sqlite-driven evidence lookup, event-log correlation |
| password-cracking | 3 | http evidence extraction, timeline reconstruction, autopsy-driven evidence lookup, credential discovery, file metadata extraction |
| reverse-engineering | 3 | file metadata extraction, reverse engineering, timeline reconstruction, dns pivot, event-log correlation |
| mobile-forensics | 1 | autopsy-driven evidence lookup, http evidence extraction, timeline reconstruction |
| network-forensics | 1 | dns pivot, http evidence extraction, memory artifact analysis, registry artifact correlation, timeline reconstruction |
| siem-query | 1 | reverse engineering |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 30 |
| timeline reconstruction | 26 |
| registry artifact correlation | 16 |
| credential discovery | 13 |
| dns pivot | 12 |
| memory artifact analysis | 12 |
| event-log correlation | 11 |
| file metadata extraction | 10 |
| indicator enrichment | 10 |
| db-browser-sqlite-driven evidence lookup | 7 |
| ftk-imager-driven evidence lookup | 7 |
| autopsy-driven evidence lookup | 6 |
| maldoc analysis | 4 |
| cyberchef-driven evidence lookup | 2 |
| mftecmd-driven evidence lookup | 2 |
| reverse engineering | 2 |
| strings-driven evidence lookup | 2 |
| layer-2 endpoint identification | 1 |
| olevba-driven evidence lookup | 1 |
| service-to-access path | 1 |
| tls handshake inspection | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [AfricanFalls Lab](../../../cards/cyber-defenders-africanfalls-lab.md) | CyberDefenders | Medium | browser-forensics, password-cracking, service-enumeration, timeline-analysis |
| [Beta Gamer Lab](../../../cards/cyber-defenders-beta-gamer-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, privilege-escalation, timeline-analysis |
| [Browser Forensics - Cryptominer](../../../cards/btlo-browser-forensics-cryptominer.md) | BTLO | Easy | browser-forensics |
| [Chollima Lab](../../../cards/cyber-defenders-chollima-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, privilege-escalation |
| [CorporateSecrets Lab](../../../cards/cyber-defenders-corporatesecrets-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [Critical](../../../cards/critical.md) | TryHackMe | Easy | dns-analysis, http-analysis, malware-static, memory-forensics |
| [CrownJewel1](../../../cards/crownjewel1.md) | HackTheBox | Easy | dns-analysis, http-analysis, malware-dynamic, reverse-engineering |
| [Dead End?](../../../cards/dead-end.md) | TryHackMe | Hard | cti-enrichment, memory-forensics |
| [DetectLog4j Lab](../../../cards/cyber-defenders-detectlog4j-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, malware-dynamic |
| [DiskFiltration](../../../cards/diskfiltration.md) | TryHackMe | Hard | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [DumpMe Lab](../../../cards/cyber-defenders-dumpme-lab.md) | CyberDefenders | Medium | cti-enrichment, malware-dynamic, memory-forensics, registry-forensics |
| [ELPACO-team Lab](../../../cards/cyber-defenders-elpaco-team-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Fog Ransomware Lab](../../../cards/cyber-defenders-fog-ransomware-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, privilege-escalation |
| [HireMe Lab](../../../cards/cyber-defenders-hireme-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [Hunter Lab](../../../cards/cyber-defenders-hunter-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [Injector Lab](../../../cards/cyber-defenders-injector-lab.md) | CyberDefenders | Medium | http-analysis, malware-static, memory-forensics, registry-forensics |
| [Insider Lab](../../../cards/cyber-defenders-insider-lab.md) | CyberDefenders | Easy | browser-forensics, http-analysis, stego-extraction |
| [Job Trap Lab](../../../cards/cyber-defenders-job-trap-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, maldoc-analysis, malware-dynamic |
| [KioskExpo7 Lab](../../../cards/cyber-defenders-kioskexpo7-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, malware-dynamic, malware-static |
| [Malicious PyPi Lab](../../../cards/cyber-defenders-malicious-pypi-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, malware-dynamic |
| [Maranhao Lab](../../../cards/cyber-defenders-maranhao-lab.md) | CyberDefenders | Easy | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [MeteorHit Lab](../../../cards/cyber-defenders-meteorhit-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, malware-dynamic |
| [MrRobot Lab](../../../cards/cyber-defenders-mrrobot-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [NetX-Support Lab](../../../cards/cyber-defenders-netx-support-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, malware-static |
| [NintendoHunt Lab](../../../cards/cyber-defenders-nintendohunt-lab.md) | CyberDefenders | Hard | http-analysis, malware-static, memory-forensics, service-enumeration |
| [Phishy Lab](../../../cards/cyber-defenders-phishy-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [PwnedDC Lab](../../../cards/cyber-defenders-pwneddc-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [RepoReaper Lab](../../../cards/cyber-defenders-reporeaper-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Silent Breach](../../../cards/cyber-defenders-silent-breach-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, malware-static, stego-extraction |
| [SpottedInTheWild Lab](../../../cards/cyber-defenders-spottedinthewild-lab.md) | CyberDefenders | Hard | cti-enrichment, http-analysis, malware-static, registry-forensics |
| [Sysinternals](../../../cards/cyber-defenders-sysinternals-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, registry-forensics |
| [Szechuan Sauce Lab](../../../cards/cyber-defenders-szechuan-suace-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, memory-forensics |
| [TheTruth Lab](../../../cards/cyber-defenders-thetruth-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, malware-static |
| [Trigona Ransomware Lab](../../../cards/cyber-defenders-trigona-ransomware-lab.md) | CyberDefenders | Medium | cti-enrichment, http-analysis, memory-forensics, registry-forensics |
| [Unattended](../../../cards/unattended.md) | TryHackMe | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [VaultBreak Lab](../../../cards/cyber-defenders-vaultbreak-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, maldoc-analysis |
| [XMRig Lab](../../../cards/cyber-defenders-xmrig-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, malware-static |
| [Zerologon Lab](../../../cards/cyber-defenders-zerologon-lab.md) | CyberDefenders | Hard | browser-forensics, dns-analysis, http-analysis, malware-dynamic |
