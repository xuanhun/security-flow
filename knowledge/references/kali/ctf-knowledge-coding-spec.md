# CTF Coding Specification

## First Pass

- Read the statement as a contract puzzle: input format, output format,
  forbidden behavior, edge cases, complexity, and hidden validator assumptions.
- Build tiny local cases before optimizing.
- Separate parsing bugs from algorithmic mistakes.

## Routes

### Parser And Format

- Check whitespace, encoding, line endings, integer size, empty input, repeated
  keys, ordering, and invalid-but-accepted cases.

### Algorithm

- Identify constraints before choosing brute force, dynamic programming, graph,
  number theory, string matching, or simulation.
- Generate random small cases and compare a slow oracle with the optimized
  solution.

### Security-Flavored Spec

- Look for unsafe eval, path handling, regex denial, serialization, sandbox
  boundary, and canonicalization traps.

### Validator Games

- Check precision, floating point tolerance, deterministic output, timeout,
  memory, and hidden judge language quirks.
- When the validator is interactive or oracle-like, log each query/result and
  build a replayable local simulator before optimizing.

### Differential Privacy Output Grid Leakage

- Signal: repeated noisy answers are not useful by their average, but every
  value falls on a fixed arithmetic grid.
- First probes: sample a target aggregate many times, then sample aggregates
  with known true maxima to calibrate the grid formula.
- Common route: scale floats to integers, take the GCD of nonzero observed
  values, convert the step back to a real value, and invert the bucket formula
  with the known base and bucket count.
- False leads: averaging DP noise, searching for SQL injection bypasses only,
  or trusting rounded medians as the protected value.
- Useful tools: `ctf_web.py dp-sample` with `--store-values`,
  `--grid-scale`, `--grid-base`, and `--grid-buckets`.
- Evidence to keep: raw sample responses, inferred grid step, calibration
  columns with known maxima, and final verification response.
- Example cases: [NO.7 SQL Differential Privacy Salary](ctf-case-no7-sql-dp-salary.md).

### Platform Navigation

- For CTFd-like platforms, prefer API-driven listing, file download, and flag
  submission when the user provides a token; keep platform credentials out of
  challenge notes.

## Useful Tools

Python, pytest, hypothesis when available, z3 for constraints, small fuzzers,
profilers, and diff-based oracle tests.
