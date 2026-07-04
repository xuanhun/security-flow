# Endpoint Forensics / ids

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| http-analysis | 23 | http evidence extraction, timeline reconstruction, memory artifact analysis, dns pivot, credential discovery |
| dns-analysis | 18 | dns pivot, http evidence extraction, credential discovery, memory artifact analysis, timeline reconstruction |
| timeline-analysis | 17 | timeline reconstruction, http evidence extraction, memory artifact analysis, dns pivot, event-log correlation |
| cti-enrichment | 15 | http evidence extraction, timeline reconstruction, dns pivot, credential discovery, indicator enrichment |
| windows-event-analysis | 15 | http evidence extraction, timeline reconstruction, dns pivot, event-log correlation, db-browser-sqlite-driven evidence lookup |
| browser-forensics | 14 | http evidence extraction, dns pivot, timeline reconstruction, credential discovery, db-browser-sqlite-driven evidence lookup |
| memory-forensics | 10 | memory artifact analysis, http evidence extraction, timeline reconstruction, dns pivot, indicator enrichment |
| malware-static | 9 | memory artifact analysis, http evidence extraction, credential discovery, indicator enrichment, dns pivot |
| stego-extraction | 8 | http evidence extraction, memory artifact analysis, indicator enrichment, timeline reconstruction, credential discovery |
| registry-forensics | 7 | http evidence extraction, timeline reconstruction, credential discovery, dns pivot, registry artifact correlation |
| service-enumeration | 6 | credential discovery, http evidence extraction, timeline reconstruction, db-browser-sqlite-driven evidence lookup, dns pivot |
| malware-dynamic | 5 | dns pivot, event-log correlation, reverse engineering, http evidence extraction, memory artifact analysis |
| reverse-engineering | 5 | dns pivot, reverse engineering, timeline reconstruction, event-log correlation, file metadata extraction |
| maldoc-analysis | 4 | maldoc analysis, dns pivot, http evidence extraction, memory artifact analysis, autopsy-driven evidence lookup |
| privilege-escalation | 4 | timeline reconstruction, http evidence extraction, credential discovery, event-log correlation, file metadata extraction |
| password-cracking | 2 | credential discovery, dns pivot, indicator enrichment, reverse engineering, timeline reconstruction |
| network-forensics | 1 | dns pivot, http evidence extraction, memory artifact analysis, registry artifact correlation, timeline reconstruction |
| siem-query | 1 | reverse engineering |

## Route Types

| Route type | Cases |
| --- | --- |
| http evidence extraction | 15 |
| timeline reconstruction | 14 |
| dns pivot | 12 |
| memory artifact analysis | 12 |
| credential discovery | 9 |
| event-log correlation | 8 |
| indicator enrichment | 6 |
| db-browser-sqlite-driven evidence lookup | 5 |
| registry artifact correlation | 5 |
| maldoc analysis | 4 |
| file metadata extraction | 3 |
| reverse engineering | 3 |
| ftk-imager-driven evidence lookup | 2 |
| autopsy-driven evidence lookup | 1 |
| evidence lookup | 1 |
| evtxecmd-driven evidence lookup | 1 |
| exiftool-driven evidence lookup | 1 |
| mftecmd-driven evidence lookup | 1 |
| olevba-driven evidence lookup | 1 |
| strings-driven evidence lookup | 1 |
| tls handshake inspection | 1 |
| virustotal-driven evidence lookup | 1 |
| volatility-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Amadey Lab](../../../cards/cyber-defenders-amadey-lab.md) | CyberDefenders | Easy | http-analysis, malware-static, memory-forensics, stego-extraction |
| [BankingTroubles Lab](../../../cards/cyber-defenders-bankingtroubles-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Beta Gamer Lab](../../../cards/cyber-defenders-beta-gamer-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, privilege-escalation, timeline-analysis |
| [Chollima Lab](../../../cards/cyber-defenders-chollima-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, privilege-escalation |
| [CorporateSecrets Lab](../../../cards/cyber-defenders-corporatesecrets-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [Crownjewel-2](../../../cards/crownjewewl2.md) | HackTheBox | Easy | dns-analysis, http-analysis, reverse-engineering, timeline-analysis |
| [CrownJewel1](../../../cards/crownjewel1.md) | HackTheBox | Easy | dns-analysis, http-analysis, malware-dynamic, reverse-engineering |
| [DetectLog4j Lab](../../../cards/cyber-defenders-detectlog4j-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, malware-dynamic |
| [ELPACO-team Lab](../../../cards/cyber-defenders-elpaco-team-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Hammered Lab](../../../cards/cyber-defenders-hammered-lab.md) | CyberDefenders | Medium | dns-analysis, http-analysis, malware-static, service-enumeration |
| [Hunter Lab](../../../cards/cyber-defenders-hunter-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
| [LummaStealer Lab](../../../cards/cyber-defenders-lummastealer-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Memory Analysis](../../../cards/lets-defend-memory-analysis.md) | LetsDefend | Medium | cti-enrichment, dns-analysis, memory-forensics, password-cracking |
| [MrRobot Lab](../../../cards/cyber-defenders-mrrobot-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Phishy Lab](../../../cards/cyber-defenders-phishy-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [PwnedDC Lab](../../../cards/cyber-defenders-pwneddc-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [QBot Lab](../../../cards/cyber-defenders-qbot-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, maldoc-analysis |
| [Redline](../../../cards/cyber-defenders-redline-lab.md) | CyberDefenders | Easy | cti-enrichment, http-analysis, malware-static, memory-forensics |
| [RepoReaper Lab](../../../cards/cyber-defenders-reporeaper-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Retracted](../../../cards/retracted.md) | TryHackMe | Easy | windows-event-analysis |
| [Reveal](../../../cards/cyber-defenders-reveal-lab.md) | CyberDefenders | Easy | cti-enrichment, http-analysis, memory-forensics, timeline-analysis |
| [RevengeHotels APT Lab](../../../cards/cyber-defenders-revengehotels-apt-lab.md) | CyberDefenders | Easy | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Szechuan Sauce Lab](../../../cards/cyber-defenders-szechuan-suace-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, memory-forensics |
| [VaultBreak Lab](../../../cards/cyber-defenders-vaultbreak-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, maldoc-analysis |
| [Volatility Traces Lab](../../../cards/cyber-defenders-volatility-traces-lab.md) | CyberDefenders | Easy | dns-analysis, http-analysis, malware-static, memory-forensics |
