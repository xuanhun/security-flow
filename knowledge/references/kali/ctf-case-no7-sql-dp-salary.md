# NO.7 SQL Differential Privacy Salary

## Metadata

- Event: ByteCTF 143
- Category: Coding Specification
- Pattern: Differential privacy output grid leakage
- Knowledge link:
  [ctf-knowledge-coding-spec.md#differential-privacy-output-grid-leakage](ctf-knowledge-coding-spec.md#differential-privacy-output-grid-leakage)
- Local solution:
  [solution.md](../../../ctf/bytectf-143/challenges/no7-sql-dp-salary/notes/solution.md)

## Prompt Summary

The challenge exposes a SQL differential privacy service for employee salary
queries. The goal is to bypass the protected noisy query result and recover the
true noiseless maximum salary.

## Signals

- `/api/schema` exposes `salary_table` with `user_id`, `salary`, and
  `department_id`.
- The only department in scope is `department_id = 10`, with 30 distinct users.
- `/api/source` exposes a Python SQL rewriter that accepts single-table
  `MAX(column)` queries and wraps them in differential privacy UDFs.
- Repeated `max(...)` answers vary wildly, so the mean and median are decoys.
- The noisy values fall on a fixed arithmetic grid. Known columns calibrate the
  formula:
  `max(department_id) = 10` gives step `500.005`; `max(user_id) = 30` gives
  step `500.015`.

## Route

1. Capture the schema and exposed rewriter source with `ctf_web.py request`.
2. Use `sql-rewrite-sim` to replay the rewriter locally and confirm that
   comment/slot tricks do not remove the final DP wrapper.
3. Use `dp-sample` on `max(department_id)` and `max(user_id)` as calibration
   columns. The tool infers:
   `true_max = step * buckets - base`, with `base = 1000000` and
   `buckets = 2000`.
4. Use `dp-sample` on `max(salary)`. The GCD-derived step is `671.2855`, so
   the noiseless maximum salary is `671.2855 * 2000 - 1000000 = 342571`.
5. Submit `342571` to `/api/verify`.

## Replay Commands

```bash
python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/no7-sql-dp-salary \
  --url /api/schema \
  --label api_schema_refreshed

python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/no7-sql-dp-salary \
  --url /api/source \
  --label api_source_refreshed

python scripts/sec.py probe web dp-sample \
  --case-dir ctf/bytectf-143/challenges/no7-sql-dp-salary \
  --url /api/query \
  --metric 'max(salary)' \
  --table-var salary_table \
  --samples 100 \
  --batch-size 100 \
  --label dp_salary_refreshed_100_grid \
  --store-values \
  --save-responses edges

python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/no7-sql-dp-salary \
  --url /api/verify \
  --method POST \
  --header 'Content-Type: application/json' \
  --data '{"answer":342571}' \
  --label verify_salary_342571
```

## False Leads

- Averaging repeated noisy salary outputs did not converge to the exact value.
- Comment and semicolon tricks against the SQL template reached altered
  rewrites, but still retained DP quantile wrapping and threshold checks.
- Grouping by salary still returned protected noisy outputs rather than the raw
  maximum.

## Final

`flag{0ea97a4dfff43f40e6c9a3dce2967b136053c80b861d6a693ddb3f46}`
