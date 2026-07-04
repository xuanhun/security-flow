# Rules Of Engagement

## Required Before Real Testing

- Written authorization reference.
- In-scope targets.
- Explicit exclusions.
- Allowed time window.
- Rate limits and concurrency limits.
- Allowed techniques.
- Emergency contact or stop condition.
- Data handling rule for sensitive evidence.

## Scope Rules

`scripts/kali.py` reads `scope.json` from the project directory. A target must
match `targets` and must not match `excluded`.

Use exact targets unless the authorization explicitly allows broader matching.
Set `include_subdomains` only when subdomains are in scope.

## Default Deny

Do not run these without explicit human approval:

- exploitation;
- online password attacks;
- sniffing or spoofing;
- wireless attacks;
- post-exploitation;
- destructive fuzzing;
- high-rate or heavy scans.

## Evidence Handling

Store generated evidence under `engagements/<project-id>/`. Do not copy
secrets into durable notes. Redact tokens, credentials, personal data, and
private keys before sharing reports.
