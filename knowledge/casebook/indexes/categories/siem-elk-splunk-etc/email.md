# SIEM (ELK, Splunk, etc.) / email

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| dns-analysis | 3 | credential discovery, dns pivot, elk-driven evidence lookup, event-log correlation, http evidence extraction |
| http-analysis | 3 | credential discovery, dns pivot, elk-driven evidence lookup, event-log correlation, http evidence extraction |
| siem-query | 3 | credential discovery, dns pivot, elk-driven evidence lookup, event-log correlation, http evidence extraction |
| windows-event-analysis | 3 | credential discovery, dns pivot, elk-driven evidence lookup, event-log correlation, http evidence extraction |
| cti-enrichment | 1 | dns pivot, elk-driven evidence lookup |
| service-enumeration | 1 | credential discovery, dns pivot, event-log correlation, http evidence extraction |

## Route Types

| Route type | Cases |
| --- | --- |
| credential discovery | 2 |
| dns pivot | 2 |
| elk-driven evidence lookup | 2 |
| event-log correlation | 2 |
| http evidence extraction | 2 |
| memory artifact analysis | 1 |
| timeline reconstruction | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Boogeyman 3](../../../cards/boogeyman3-writeup.md) | TryHackMe | Medium | dns-analysis, http-analysis, siem-query, windows-event-analysis |
| [PS Eclipse](../../../cards/pseclipse.md) | TryHackMe | Medium | cti-enrichment, dns-analysis, http-analysis, siem-query |
| [T1110-003 Lab](../../../cards/cyber-defenders-t1110-003-lab.md) | CyberDefenders | Easy | dns-analysis, http-analysis, service-enumeration, siem-query |
