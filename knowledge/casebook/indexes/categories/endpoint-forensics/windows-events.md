# Endpoint Forensics / windows-events

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| windows-event-analysis | 33 | http evidence extraction, event-log correlation, timeline reconstruction, dns pivot, memory artifact analysis |
| http-analysis | 30 | http evidence extraction, event-log correlation, timeline reconstruction, dns pivot, registry artifact correlation |
| timeline-analysis | 30 | http evidence extraction, event-log correlation, timeline reconstruction, dns pivot, memory artifact analysis |
| dns-analysis | 20 | dns pivot, http evidence extraction, event-log correlation, timeline reconstruction, memory artifact analysis |
| cti-enrichment | 18 | http evidence extraction, event-log correlation, dns pivot, timeline reconstruction, registry artifact correlation |
| browser-forensics | 16 | http evidence extraction, timeline reconstruction, event-log correlation, db-browser-sqlite-driven evidence lookup, dns pivot |
| registry-forensics | 12 | http evidence extraction, timeline reconstruction, registry artifact correlation, event-log correlation, file metadata extraction |
| malware-dynamic | 10 | event-log correlation, dns pivot, http evidence extraction, timeline reconstruction, file metadata extraction |
| malware-static | 8 | http evidence extraction, event-log correlation, timeline reconstruction, credential discovery, dns pivot |
| privilege-escalation | 7 | http evidence extraction, timeline reconstruction, event-log correlation, file metadata extraction, indicator enrichment |
| stego-extraction | 7 | http evidence extraction, timeline reconstruction, event-log correlation, dns pivot, registry artifact correlation |
| memory-forensics | 6 | http evidence extraction, dns pivot, event-log correlation, memory artifact analysis, registry artifact correlation |
| reverse-engineering | 5 | dns pivot, reverse engineering, timeline reconstruction, event-log correlation, file metadata extraction |
| service-enumeration | 5 | timeline reconstruction, http evidence extraction, db-browser-sqlite-driven evidence lookup, dns pivot, credential discovery |
| maldoc-analysis | 3 | maldoc analysis, db-browser-sqlite-driven evidence lookup, dns pivot, event-log correlation, http evidence extraction |
| network-forensics | 2 | dns pivot, cyberchef-driven evidence lookup, event-log correlation, http evidence extraction, indicator enrichment |
| password-cracking | 2 | cyberchef-driven evidence lookup, dns pivot, event-log correlation, indicator enrichment, reverse engineering |
| email-header-analysis | 1 | cyberchef-driven evidence lookup, dns pivot, event-log correlation, indicator enrichment |
| siem-query | 1 | reverse engineering |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 23 |
| event-log correlation | 22 |
| timeline reconstruction | 17 |
| dns pivot | 15 |
| memory artifact analysis | 10 |
| registry artifact correlation | 10 |
| credential discovery | 9 |
| db-browser-sqlite-driven evidence lookup | 7 |
| file metadata extraction | 7 |
| evtxecmd-driven evidence lookup | 4 |
| cyberchef-driven evidence lookup | 3 |
| indicator enrichment | 3 |
| maldoc analysis | 3 |
| reverse engineering | 3 |
| evidence lookup | 2 |
| ftk-imager-driven evidence lookup | 2 |
| mftecmd-driven evidence lookup | 2 |
| layer-2 endpoint identification | 1 |
| olevba-driven evidence lookup | 1 |
| service-to-access path | 1 |
| virustotal-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Akira Lab](../../../cards/cyber-defenders-akira-lab.md) | CyberDefedners | Medium | dns-analysis, http-analysis, malware-static, memory-forensics |
| [Andromeda Bot Lab](../../../cards/cyber-defenders-andromeda-bot-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, memory-forensics |
| [Beta Gamer Lab](../../../cards/cyber-defenders-beta-gamer-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, privilege-escalation, timeline-analysis |
| [Bruteforce](../../../cards/btlo-bruteforce.md) | BTLO | Medium | http-analysis, timeline-analysis, windows-event-analysis |
| [Chollima Lab](../../../cards/cyber-defenders-chollima-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, privilege-escalation |
| [CorporateSecrets Lab](../../../cards/cyber-defenders-corporatesecrets-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [Crownjewel-2](../../../cards/crownjewewl2.md) | HackTheBox | Easy | dns-analysis, http-analysis, reverse-engineering, timeline-analysis |
| [CrownJewel1](../../../cards/crownjewel1.md) | HackTheBox | Easy | dns-analysis, http-analysis, malware-dynamic, reverse-engineering |
| [DarkCrystal Lab](../../../cards/cyber-defenders-darkcrystal-lab.md) | CyberDefenders | Medium | http-analysis, malware-static, memory-forensics, stego-extraction |
| [Deep Blue](../../../cards/btlo-deep-blue.md) | BTLO | Easy | http-analysis, windows-event-analysis |
| [DetectLog4j Lab](../../../cards/cyber-defenders-detectlog4j-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, malware-dynamic |
| [ELPACO-team Lab](../../../cards/cyber-defenders-elpaco-team-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Fog Ransomware Lab](../../../cards/cyber-defenders-fog-ransomware-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, privilege-escalation |
| [Hunter Lab](../../../cards/cyber-defenders-hunter-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [Job Trap Lab](../../../cards/cyber-defenders-job-trap-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, maldoc-analysis, malware-dynamic |
| [Lockbit Lab](../../../cards/cyber-defenders-lockbit-lab.md) | CyberDefenders | Medium | cti-enrichment, timeline-analysis, windows-event-analysis |
| [LummaStealer Lab](../../../cards/cyber-defenders-lummastealer-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Malicious PyPi Lab](../../../cards/cyber-defenders-malicious-pypi-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, malware-dynamic |
| [Maranhao Lab](../../../cards/cyber-defenders-maranhao-lab.md) | CyberDefenders | Easy | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [MeteorHit Lab](../../../cards/cyber-defenders-meteorhit-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, malware-dynamic |
| [MinerHunt Lab](../../../cards/cyber-defenders-minerhunt-lab.md) | CyberDefenders | Medium | cti-enrichment, http-analysis, malware-static, privilege-escalation |
| [NetX-Support Lab](../../../cards/cyber-defenders-netx-support-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, malware-static |
| [Operationa Blackout 2025: Phantom Check](../../../cards/operation-blackout-2025-phantom-check.md) | HackTheBox | Easy | dns-analysis, timeline-analysis, windows-event-analysis |
| [PwnedDC Lab](../../../cards/cyber-defenders-pwneddc-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [RepoReaper Lab](../../../cards/cyber-defenders-reporeaper-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Retracted](../../../cards/retracted.md) | TryHackMe | Easy | windows-event-analysis |
| [RevengeHotels APT Lab](../../../cards/cyber-defenders-revengehotels-apt-lab.md) | CyberDefenders | Easy | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [SpottedInTheWild Lab](../../../cards/cyber-defenders-spottedinthewild-lab.md) | CyberDefenders | Hard | cti-enrichment, http-analysis, malware-static, registry-forensics |
| [Szechuan Sauce Lab](../../../cards/cyber-defenders-szechuan-suace-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, memory-forensics |
| [Tempest](../../../cards/temptest-writeup.md) | TryHackMe | Medium | cti-enrichment, dns-analysis, email-header-analysis, http-analysis |
| [Trigona Ransomware Lab](../../../cards/cyber-defenders-trigona-ransomware-lab.md) | CyberDefenders | Medium | cti-enrichment, http-analysis, memory-forensics, registry-forensics |
| [VaultBreak Lab](../../../cards/cyber-defenders-vaultbreak-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, maldoc-analysis |
| [Zerologon Lab](../../../cards/cyber-defenders-zerologon-lab.md) | CyberDefenders | Hard | browser-forensics, dns-analysis, http-analysis, malware-dynamic |
