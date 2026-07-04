# Cyber Threat Intelligence (CTI) / registry

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| cti-enrichment | 2 | dns pivot, credential discovery, http evidence extraction, memory artifact analysis, timeline reconstruction |
| dns-analysis | 2 | dns pivot, credential discovery, http evidence extraction, memory artifact analysis, timeline reconstruction |
| http-analysis | 2 | dns pivot, credential discovery, http evidence extraction, memory artifact analysis, timeline reconstruction |
| email-header-analysis | 1 | dns pivot, http evidence extraction, timeline reconstruction |
| malware-dynamic | 1 | credential discovery, dns pivot, memory artifact analysis, virustotal-driven evidence lookup |

## Route Types

| Route type | Cases |
| --- | --- |
| dns pivot | 2 |
| credential discovery | 1 |
| http evidence extraction | 1 |
| memory artifact analysis | 1 |
| timeline reconstruction | 1 |
| virustotal-driven evidence lookup | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [Oski Lab](../../../cards/cyber-defenders-oski-lab.md) | CyberDefenders | Easy | cti-enrichment, dns-analysis, http-analysis, malware-dynamic |
| [PhishStrike Lab](../../../cards/cyber-defenders-phishstrike.md) | CyberDefenders | Medium | cti-enrichment, dns-analysis, email-header-analysis, http-analysis |
