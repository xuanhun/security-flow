# Network Forensics / email

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| dns-analysis | 9 | dns pivot, http evidence extraction, conversation statistics, credential discovery, layer-2 endpoint identification |
| http-analysis | 9 | dns pivot, http evidence extraction, conversation statistics, credential discovery, layer-2 endpoint identification |
| network-forensics | 9 | dns pivot, http evidence extraction, conversation statistics, credential discovery, layer-2 endpoint identification |
| cti-enrichment | 7 | dns pivot, conversation statistics, http evidence extraction, virustotal-driven evidence lookup, credential discovery |
| malware-static | 2 | conversation statistics, dns pivot, credential discovery, http evidence extraction, maldoc analysis |
| service-enumeration | 2 | dns pivot, http evidence extraction, cyberchef-driven evidence lookup, layer-2 endpoint identification, service-to-access path |
| stego-extraction | 2 | conversation statistics, dns pivot, credential discovery, http evidence extraction, maldoc analysis |
| browser-forensics | 1 | dns pivot |
| email-header-analysis | 1 | credential discovery, dns pivot, wireshark-driven evidence lookup |
| maldoc-analysis | 1 | conversation statistics, credential discovery, dns pivot, http evidence extraction, maldoc analysis |
| password-cracking | 1 | dns pivot |
| reverse-engineering | 1 | conversation statistics, dns pivot, reverse engineering |
| windows-event-analysis | 1 | credential discovery, dns pivot, wireshark-driven evidence lookup |

## Route Types

| Route type | Cases |
| --- | --- |
| dns pivot | 8 |
| http evidence extraction | 4 |
| conversation statistics | 3 |
| credential discovery | 2 |
| layer-2 endpoint identification | 2 |
| virustotal-driven evidence lookup | 2 |
| wireshark-driven evidence lookup | 2 |
| cyberchef-driven evidence lookup | 1 |
| maldoc analysis | 1 |
| reverse engineering | 1 |
| service-to-access path | 1 |
| timeline reconstruction | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Boogeyman 1](../../../cards/boogeyman1-writeup.md) | TryHackMe | Medium | dns-analysis, email-header-analysis, http-analysis, network-forensics |
| [Carnage](../../../cards/carnage-writeup.md) | TryHackMe | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [HawkEye Lab](../../../cards/cyber-defenders-hawkeye-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [Malware Traffic Analysis 5 Lab](../../../cards/cyber-defenders-malware-traffic-analysis-5.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, maldoc-analysis |
| [Masterminds](../../../cards/masterminds.md) | TryHackMe | Medium | browser-forensics, cti-enrichment, dns-analysis, http-analysis |
| [Trident Lab](../../../cards/cyber-defenders-trident-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, malware-static |
| [TShark Challenge 1: Teamwork](../../../cards/tshark-challenge-1-teamwork.md) | TryHackMe | Easy | cti-enrichment, dns-analysis, http-analysis, network-forensics |
| [WireDive Lab](../../../cards/cyber-defenders-wiredive-lab.md) | CyberDefenders | Medium | dns-analysis, http-analysis, network-forensics, service-enumeration |
| [Zeek Exercises](../../../cards/zeek-exercises.md) | TryHackMe | Medium | cti-enrichment, dns-analysis, http-analysis, network-forensics |
