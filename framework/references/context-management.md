# Context Management

Each engagement owns a compact context layer:

```text
context/
  current.md
  snapshot.json
  history.jsonl
```

`current.md` is for human handoff: current target, confirmed facts, active
candidates, routes not to repeat, and next constraints.

`snapshot.json` is machine-readable recovery state.

`history.jsonl` records phase transitions, candidate changes, key evidence,
blocking conditions, and closure summaries.
