# Knowledge Retrieval

The framework treats local knowledge as part of the testing loop, not a passive
folder.

## Retrieval Points

- Before entering a practical testing step.
- After key evidence is captured.
- Before running a candidate route.
- Before high-risk escalation.
- Before exiting each phase.

## Local Resources

- `knowledge/registry.jsonl`: resource metadata.
- `knowledge/index.sqlite`: SQLite FTS index.
- `knowledge/taxonomy.json`: phase, domain, artifact, and risk mapping.
- `knowledge/links.jsonl`: relationships between engagements and resources.
