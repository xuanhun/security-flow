# Operationa Blackout 2025: Phantom Check

## Case Metadata

- Category: `Endpoint Forensics`
- Platform: `HackTheBox`
- Difficulty: `Easy`
- Source PDF: `https://github.com/tim-barc/ctf_writeups/blob/main/writeups/operation_blackout_2025_phantom_check.pdf`

## Why This Case Matters

Use this case as a Endpoint Forensics reference for registry, windows-events challenges.

## Input Signals

- Artifacts: registry, windows-events
- Tools: evtxecmd
- Techniques: dns-analysis, timeline-analysis, windows-event-analysis

## First-Principles Route

- Start from artifact inventory: event logs, registry hives, browser data, file system timelines, memory, and application databases.
- Build a timeline around the suspicious user, process, file path, login, persistence item, or network connection.
- Correlate logs with file and registry evidence before trusting one artifact alone.
- Extract concrete indicators such as process names, command lines, hashes, timestamps, users, and persistence locations.

## Solve Thinking

### Step 1: Which WMI class did the attacker use to retrieve model and manufacturer information for virtualization detection?

- Route type: `layer-2 endpoint identification`
- Why: MAC/OUI questions should start from the relevant endpoint conversation, then verify the address in Ethernet fields.
- Probe: Use evtxecmd to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as layer-2 endpoint identification.
  - Use evtxecmd to inspect Ethernet fields, endpoint conversations, and OUI/manufacturer context.
  - Trust the result only when the extracted evidence line or field directly supports it.
- Evidence rule: Trust the result only when the extracted evidence line or field directly supports it.
- Result: `Win32_ComputerSystem`

### Step 2: Which WMI query did the attacker execute to retrieve the current temperature value of the machine?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use evtxecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use evtxecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `SELECT * FROM MSAcpi_ThermalZoneTemperature`

### Step 3: of the script?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Check-VM`

### Step 4: Which registry key did the above script query to retrieve service details for virtualization detection?

- Route type: `dns pivot`
- Why: DNS questions usually reduce to source host, resolver, queried name, response, or packet number pivots.
- Probe: Use evtxecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as dns pivot.
  - Use evtxecmd to filter DNS traffic and pivot from source host to queried domain or resolver.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `HKLM:\SYSTEM\ControlSet001\Services`

### Step 5: determine if the system is running VirtualBox?

- Route type: `memory artifact analysis`
- Why: Memory routes start broad with process/socket inventory, then narrow to suspicious process evidence.
- Probe: Use evtxecmd to enumerate processes, network sockets, injected regions, and command lines.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as memory artifact analysis.
  - Use evtxecmd to enumerate processes, network sockets, injected regions, and command lines.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `vboxservice.exe, vboxtray.exe`

### Step 6: virtualization platforms did the script detect?

- Route type: `event-log correlation`
- Why: Event-log cases should be solved by field correlation, not by reading logs chronologically.
- Probe: Use evtxecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
- Tools: evtxecmd
- Reasoning chain:
  - Recognize the goal as event-log correlation.
  - Use evtxecmd to search the relevant event IDs and correlate user, process, host, and timestamp fields.
  - Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Evidence rule: Treat the extracted answer as proven only after locating the source artifact field that produced it.
- Result: `Hyper-V , Vmware`

## Reuse Checklist

- Match the new challenge's artifact and question shape against this case before copying any tool sequence.
- Start from the same evidence class, then adapt filters, fields, and timestamps to the new artifact.
- Promote any repeated manual action into a skill command before relying on it for the final solve.
