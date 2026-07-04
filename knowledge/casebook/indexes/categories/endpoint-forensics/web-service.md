# Endpoint Forensics / web-service

Navigation: root -> category -> artifact -> technique/route -> card.

## Techniques

| Technique | Cases | Common routes |
| --- | --- | --- |
| service-enumeration | 3 | credential discovery, http evidence extraction, timeline reconstruction, db-browser-sqlite-driven evidence lookup, dns pivot |
| browser-forensics | 2 | credential discovery, timeline reconstruction, db-browser-sqlite-driven evidence lookup, dns pivot, file metadata extraction |
| dns-analysis | 2 | credential discovery, db-browser-sqlite-driven evidence lookup, dns pivot, exiftool-driven evidence lookup, http evidence extraction |
| http-analysis | 2 | credential discovery, db-browser-sqlite-driven evidence lookup, dns pivot, exiftool-driven evidence lookup, http evidence extraction |
| timeline-analysis | 2 | credential discovery, timeline reconstruction, db-browser-sqlite-driven evidence lookup, dns pivot, file metadata extraction |
| malware-static | 1 | credential discovery, exiftool-driven evidence lookup, http evidence extraction, memory artifact analysis |
| password-cracking | 1 | credential discovery, file metadata extraction, ftk-imager-driven evidence lookup, http evidence extraction, indicator enrichment |
| registry-forensics | 1 | credential discovery, db-browser-sqlite-driven evidence lookup, dns pivot, registry artifact correlation, timeline reconstruction |
| stego-extraction | 1 | credential discovery, exiftool-driven evidence lookup, http evidence extraction, memory artifact analysis |
| windows-event-analysis | 1 | credential discovery, db-browser-sqlite-driven evidence lookup, dns pivot, registry artifact correlation, timeline reconstruction |

## Route Types

| Route type | Cases |
| --- | --- |
| credential discovery | 3 |
| http evidence extraction | 2 |
| timeline reconstruction | 2 |
| db-browser-sqlite-driven evidence lookup | 1 |
| dns pivot | 1 |
| exiftool-driven evidence lookup | 1 |
| file metadata extraction | 1 |
| ftk-imager-driven evidence lookup | 1 |
| indicator enrichment | 1 |
| memory artifact analysis | 1 |
| registry artifact correlation | 1 |

## Cards

| Case | Platform | Difficulty | Techniques |
| --- | --- | --- | --- |
| [AfricanFalls Lab](../../../cards/cyber-defenders-africanfalls-lab.md) | CyberDefenders | Medium | browser-forensics, password-cracking, service-enumeration, timeline-analysis |
| [Hammered Lab](../../../cards/cyber-defenders-hammered-lab.md) | CyberDefenders | Medium | dns-analysis, http-analysis, malware-static, service-enumeration |
| [Hunter Lab](../../../cards/cyber-defenders-hunter-lab.md) | CyberDefenders | Medium | browser-forensics, dns-analysis, http-analysis, registry-forensics |
