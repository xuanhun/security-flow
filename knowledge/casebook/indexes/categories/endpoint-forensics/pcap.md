# Endpoint Forensics / pcap

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| dns-analysis | 3 | dns pivot, http evidence extraction, registry artifact correlation, timeline reconstruction, cyberchef-driven evidence lookup |
| http-analysis | 3 | dns pivot, http evidence extraction, registry artifact correlation, timeline reconstruction, cyberchef-driven evidence lookup |
| network-forensics | 3 | dns pivot, http evidence extraction, registry artifact correlation, timeline reconstruction, cyberchef-driven evidence lookup |
| cti-enrichment | 2 | dns pivot, cyberchef-driven evidence lookup, event-log correlation, http evidence extraction, indicator enrichment |
| registry-forensics | 2 | dns pivot, http evidence extraction, registry artifact correlation, timeline reconstruction, memory artifact analysis |
| timeline-analysis | 2 | dns pivot, cyberchef-driven evidence lookup, event-log correlation, http evidence extraction, indicator enrichment |
| windows-event-analysis | 2 | dns pivot, cyberchef-driven evidence lookup, event-log correlation, http evidence extraction, indicator enrichment |
| email-header-analysis | 1 | cyberchef-driven evidence lookup, dns pivot, event-log correlation, indicator enrichment |
| malware-static | 1 | cyberchef-driven evidence lookup, dns pivot, event-log correlation, indicator enrichment |
| memory-forensics | 1 | dns pivot, http evidence extraction, memory artifact analysis, registry artifact correlation, timeline reconstruction |
| password-cracking | 1 | cyberchef-driven evidence lookup, dns pivot, event-log correlation, indicator enrichment |
| privilege-escalation | 1 | cyberchef-driven evidence lookup, dns pivot, event-log correlation, indicator enrichment |
| stego-extraction | 1 | cyberchef-driven evidence lookup, dns pivot, event-log correlation, indicator enrichment |

## Route Types

| Route type | Cases |
| --- | --- |
| dns pivot | 3 |
| http evidence extraction | 2 |
| registry artifact correlation | 2 |
| timeline reconstruction | 2 |
| cyberchef-driven evidence lookup | 1 |
| event-log correlation | 1 |
| indicator enrichment | 1 |
| memory artifact analysis | 1 |
| registry-explorer-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Secret Recipe](../../../cards/secret-recipe.md) | TryHackMe | Medium | dns-analysis, http-analysis, network-forensics, registry-forensics |
| [Szechuan Sauce Lab](../../../cards/cyber-defenders-szechuan-suace-lab.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, http-analysis, memory-forensics |
| [Tempest](../../../cards/temptest-writeup.md) | TryHackMe | Medium | cti-enrichment, dns-analysis, email-header-analysis, http-analysis |
