# NO.9 Tonight Party

## Metadata

- Event: ByteCTF 143
- Category: Crypto / Oracle
- Pattern: Fixed shuffle oracle with equal-weight anagram queries
- Knowledge link:
  [ctf-knowledge-crypto.md#prng-and-oracles](ctf-knowledge-crypto.md#prng-and-oracles)
- Local solution:
  [solution.md](../../../ctf/bytectf-143/challenges/no9-tonight-party/notes/solution.md)

## Prompt Summary

The challenge provides a fixed IPv6 service and a Python source attachment. The
service prints a shuffled binary string derived from `base64(flag)`, then
allows 150 equal-weight binary anagram queries and returns the same shuffle
applied to each query.

## Signals

- WSL has no global IPv6 route, so Windows `netsh interface portproxy` was used
  to expose the IPv6 service to WSL over IPv4.
- The attachment encodes `base64(FLAG)` as bits, seeds one random permutation
  with `os.urandom(8)`, and reuses that permutation for every `shuffle(...)`.
- Query validation checks only length and counts of `0` and `1`, not that the
  submitted string is related to the real flag.
- The observed target length is 320 bits with 160 ones and 160 zeros.

## Route

1. Inventory the attachment and read `ctf-2026_main.py`.
2. Use Windows host forwarding to reach the IPv6-only service from WSL:
   `172.19.64.1:30561 -> [2605:340:cd50:2002:137b:e85:d50a:6468]:30561`.
3. Generate unique balanced binary codes for all original positions. Each code
   column contains exactly 160 ones, so every query passes the anagram check.
4. Send each code column to the service. The response reveals whether each
   output position came from an original position whose code bit was set.
5. Reconstruct the inverse permutation from the output-side codes.
6. Apply the inverse permutation to the target shuffled bits, convert bits to
   bytes, then base64-decode the recovered string.

## Replay Commands

```bash
python scripts/sec.py probe network shuffle-oracle-solve \
  --case-dir ctf/bytectf-143/challenges/no9-tonight-party \
  --host 172.19.64.1 \
  --port 30561 \
  --label shuffle_oracle_solve_forwarded \
  --store-map
```

## Evidence

- Forwarding notes:
  [windows-forwarding.md](../../../ctf/bytectf-143/challenges/no9-tonight-party/notes/windows-forwarding.md)
- Solver output:
  [shuffle-oracle-solve-forwarded-shuffle-oracle.json](../../../ctf/bytectf-143/challenges/no9-tonight-party/artifacts/shuffle-oracle-solve-forwarded-shuffle-oracle.json)
- Transcript:
  [shuffle-oracle-solve-forwarded-transcript.json](../../../ctf/bytectf-143/challenges/no9-tonight-party/artifacts/shuffle-oracle-solve-forwarded-transcript.json)

## Final

`flag{3v32y_d4y_1'm_5huffl1ng~}`
