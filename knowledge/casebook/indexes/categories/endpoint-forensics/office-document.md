# Endpoint Forensics / office-document

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| http-analysis | 7 | maldoc analysis, dns pivot, http evidence extraction, memory artifact analysis, db-browser-sqlite-driven evidence lookup |
| maldoc-analysis | 7 | maldoc analysis, dns pivot, http evidence extraction, memory artifact analysis, db-browser-sqlite-driven evidence lookup |
| browser-forensics | 5 | maldoc analysis, dns pivot, http evidence extraction, db-browser-sqlite-driven evidence lookup, event-log correlation |
| cti-enrichment | 4 | maldoc analysis, dns pivot, http evidence extraction, autopsy-driven evidence lookup, credential discovery |
| dns-analysis | 4 | maldoc analysis, dns pivot, http evidence extraction, autopsy-driven evidence lookup, credential discovery |
| malware-static | 3 | maldoc analysis, memory artifact analysis, olevba-driven evidence lookup, dns pivot, event-log correlation |
| memory-forensics | 3 | maldoc analysis, memory artifact analysis, olevba-driven evidence lookup, dns pivot, event-log correlation |
| stego-extraction | 3 | maldoc analysis, memory artifact analysis, olevba-driven evidence lookup, dns pivot, event-log correlation |
| timeline-analysis | 3 | maldoc analysis, db-browser-sqlite-driven evidence lookup, memory artifact analysis, dns pivot, event-log correlation |
| windows-event-analysis | 3 | maldoc analysis, db-browser-sqlite-driven evidence lookup, dns pivot, event-log correlation, http evidence extraction |
| email-header-analysis | 1 | maldoc analysis, oledump-driven evidence lookup |
| malware-dynamic | 1 | db-browser-sqlite-driven evidence lookup, event-log correlation, maldoc analysis |
| registry-forensics | 1 | autopsy-driven evidence lookup, credential discovery, dns pivot, http evidence extraction, maldoc analysis |

## Route Types

| Route type | Cases |
| --- | --- |
| maldoc analysis | 7 |
| dns pivot | 3 |
| http evidence extraction | 3 |
| memory artifact analysis | 3 |
| db-browser-sqlite-driven evidence lookup | 2 |
| event-log correlation | 2 |
| olevba-driven evidence lookup | 2 |
| autopsy-driven evidence lookup | 1 |
| credential discovery | 1 |
| indicator enrichment | 1 |
| oledump-driven evidence lookup | 1 |
| timeline reconstruction | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Boogeyman 2](../../../cards/boogeyman2-writeup.md) | TryHackMe | Medium | http-analysis, maldoc-analysis, malware-static, memory-forensics |
| [Job Trap Lab](../../../cards/cyber-defenders-job-trap-lab.md) | CyberDefenders | Medium | browser-forensics, http-analysis, maldoc-analysis, malware-dynamic |
| [Phishy Lab](../../../cards/cyber-defenders-phishy-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [PwnedDC Lab](../../../cards/cyber-defenders-pwneddc-lab.md) | CyberDefenders | Hard | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [QBot Lab](../../../cards/cyber-defenders-qbot-lab.md) | CyberDefenders | Medium | browser-forensics, cti-enrichment, http-analysis, maldoc-analysis |
| [T1598.002 Lab](../../../cards/cyber-defenders-t1598-002-lab.md) | CyberDefenders | Easy | cti-enrichment, dns-analysis, email-header-analysis, http-analysis |
| [VaultBreak Lab](../../../cards/cyber-defenders-vaultbreak-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, maldoc-analysis |
