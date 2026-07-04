# Network Forensics / windows-events

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| http-analysis | 3 | conversation statistics, credential discovery, dns pivot, event-log correlation, http evidence extraction |
| network-forensics | 3 | conversation statistics, credential discovery, dns pivot, event-log correlation, http evidence extraction |
| windows-event-analysis | 3 | conversation statistics, credential discovery, dns pivot, event-log correlation, http evidence extraction |
| dns-analysis | 2 | credential discovery, dns pivot, conversation statistics, event-log correlation, http evidence extraction |
| service-enumeration | 2 | conversation statistics, event-log correlation, http evidence extraction, credential discovery, dns pivot |
| timeline-analysis | 2 | conversation statistics, event-log correlation, http evidence extraction, credential discovery, dns pivot |
| cti-enrichment | 1 | conversation statistics, credential discovery, dns pivot, event-log correlation, http evidence extraction |
| email-header-analysis | 1 | credential discovery, dns pivot, wireshark-driven evidence lookup |
| privilege-escalation | 1 | conversation statistics, credential discovery, dns pivot, event-log correlation, http evidence extraction |

## Route Types

| Route type | Cases |
| --- | --- |
| conversation statistics | 2 |
| credential discovery | 2 |
| dns pivot | 2 |
| event-log correlation | 2 |
| http evidence extraction | 2 |
| registry artifact correlation | 1 |
| service-to-access path | 1 |
| wireshark-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [BlueSky Ransomware Lab](../../../cards/cyber-defenders-bluesky-ransomware-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [Boogeyman 1](../../../cards/boogeyman1-writeup.md) | TryHackMe | Medium | dns-analysis, email-header-analysis, http-analysis, network-forensics |
| [PacketDetective](../../../cards/cyber-defenders-pakcet-defective-lab.md) | CyberDefenders | Easy | http-analysis, network-forensics, service-enumeration, timeline-analysis |
