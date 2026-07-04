# CTF Reverse And Pwn

## Reverse First Pass

- Identify architecture, format, symbols, packing, strings, imports, and
  runtime dependencies.
- Run the binary only in a controlled local environment.
- Find input parsing, comparison functions, crypto loops, anti-debug checks,
  and hidden command paths.

## Reverse Routes

- Static strings first, then decompile, then trace.
- Patch or emulate only after understanding the check.
- For VM/obfuscation, identify instruction format and build a small tracer.
- For license/keygen tasks, separate transformation, comparison, and constants.
- Check anti-debug, anti-VM, timing, self-hash, signal handlers, forked child
  logic, and packed sections before trusting a single static view.
- For bytecode/custom VM challenges, log instruction pointer, opcode, operands,
  register/state deltas, and memory accesses; solve the VM semantics before
  writing a final solver.

## Pwn First Pass

- Confirm architecture, mitigations, input path, crash primitive, and local
  service behavior.
- Record `checksec`, crash offset, registers, stack/heap state, and libc if
  provided.

## Pwn Routes

- Stack overflow: offset, canary, PIE, NX, ret2win, ROP, ret2libc.
- Format string: leak, arbitrary write, GOT/return overwrite when mitigations
  allow.
- Heap: allocator version, UAF/double free/overflow, tcache/fastbin route.
- Sandbox: syscalls, seccomp, file descriptor assumptions.
- Integer bugs: signed/unsigned mismatch, truncation, negative indexing,
  length-field wrap, and allocator size class confusion.
- Constrained exploitation: bad characters, short writes, partial overwrites,
  one-byte pivots, seccomp syscall alternatives, and inherited file
  descriptors.

### SUID Menu Object Function Pointer Via Signed Length

- Signal: an agent or shell foothold reveals a small custom SUID menu binary
  with actions such as add/view/rename/remove, fixed slot counts, and strings
  for a hidden flag routine.
- First probes: copy the binary locally if allowed by the CTF, run `file`,
  `readelf -sW`, `strings -tx`, and focused `objdump -d -M intel` on menu
  handlers before fuzzing. Confirm the object layout and callback offsets.
- Common route: add creates a fixed-size object whose first bytes are a name
  and later bytes hold a function pointer used by view. Rename asks for a
  signed length, checks only `len > max`, then passes the value to `read`.
  Supplying `-1` bypasses the signed upper-bound check and becomes a huge
  unsigned read size, allowing an overwrite of the callback with a hidden
  win/flag function address.
- Replay shape: use a staged pipe so the oversized `read` consumes only the
  overflow payload, then send the menu action that triggers the overwritten
  callback:
  `(printf '...-1\n'; perl -e 'print "A"x64 . pack("Q", WIN)'; sleep 0.2; printf '2\n5\n') | ./menu`.
- False leads: assuming a 0x40 maximum prevents overwrites, forgetting that
  writing to a 32-bit register zero-extends a negative length before the
  syscall, or appending follow-up menu commands without a delay so the large
  read consumes them.
- Evidence to keep: SUID listing, extracted binary, symbols/strings showing
  the hidden routine, disassembly of add/view/rename, local control-flow proof,
  target exploit output, and final flag.
- Example cases: [Bytedance Lobster Hole](ctf-case-bytedance-lobster-hole.md).

## Useful Tools

file, readelf, objdump, strings, gdb, pwndbg/gef, checksec, ltrace, strace,
radare2/rizin, Ghidra, angr, pwntools, qemu-user/system, ropper, ROPgadget,
Unicorn, Capstone, Frida for authorized dynamic instrumentation.
