#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from core import memory as memory_store
from core.evidence import REPORT_ROOT, ensure_project, record_event, write_json
from core.report import write_report
from core.scope import assert_in_scope, load_scope, make_scope, save_scope, scope_targets
from core.tool_registry import install_profile, tool_status
from modules.exploitation_gate import prepare_exploitation
from modules.information_gathering import scan_target
from modules.vulnerability_analysis import nikto_scan
from modules.web_applications import web_baseline


def slug(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "assessment"


def project_dir_arg(value: str | None) -> Path:
    if not value:
        raise SystemExit("--project is required")
    return ensure_project(value)


def record_scan_memory(project_dir: Path, result: dict) -> None:
    target = result.get("target", "unknown-target")
    evidence = [result["output"]] if result.get("output") else []
    if result.get("tool") == "python-socket":
        open_ports = [str(item.get("port")) for item in result.get("results", []) if item.get("open")]
        summary = f"Python socket scan observed open ports: {', '.join(open_ports) or 'none'}."
        memory_store.add_surface_path(
            project_dir,
            source="scan",
            title=f"TCP scan: {target}",
            summary=summary,
            evidence_refs=evidence,
            lane_id="assessment",
            dedupe_key=f"scan:{target}:{result.get('tool')}",
        )
        if not open_ports:
            memory_store.record_verification(
                project_dir,
                outcome="negative",
                summary=f"No open TCP ports observed for {target} in the requested scan set.",
                evidence_refs=evidence,
                failure_reason="no open ports in requested scan set",
                next_constraints=["Do not assume exposed TCP services without new evidence or a broader authorized scan."],
            )
    elif result.get("returncode") == 0:
        memory_store.add_surface_path(
            project_dir,
            source="scan",
            title=f"Nmap scan: {target}",
            summary=f"Nmap completed for {target}; review XML/service output before selecting an active route.",
            evidence_refs=[item for item in [result.get("xml"), result.get("output")] if item],
            lane_id="assessment",
            dedupe_key=f"scan:{target}:nmap",
        )
    else:
        memory_store.record_verification(
            project_dir,
            outcome="inconclusive",
            summary=f"Nmap did not complete cleanly for {target}.",
            evidence_refs=[item for item in [result.get("xml"), result.get("output")] if item],
            failure_reason=f"nmap returncode {result.get('returncode')}",
            next_constraints=["Review scan output before trusting service discovery results."],
        )


def record_web_memory(project_dir: Path, target: str, result: dict) -> None:
    evidence = [result["evidence"]] if result.get("evidence") else []
    missing_headers = result.get("missing_security_headers") or []
    status = result.get("status")
    memory_store.add_surface_path(
        project_dir,
        source="web",
        title=f"HTTP baseline: {target}",
        summary=f"HTTP baseline status={status}; missing_headers={', '.join(missing_headers) or 'none'}.",
        evidence_refs=evidence,
        lane_id="assessment",
        dedupe_key=f"web:{target}",
    )
    if not missing_headers:
        memory_store.record_verification(
            project_dir,
            outcome="negative",
            summary=f"Safe HTTP baseline found no missing common security headers for {target}.",
            evidence_refs=evidence,
            failure_reason="no low-risk web baseline finding",
            next_constraints=["Do not report header issues for this target without new HTTP evidence."],
        )


def record_vuln_memory(project_dir: Path, target: str, result: dict) -> None:
    status = result.get("status")
    evidence = [result["output"]] if result.get("output") else []
    if status == "pending-human-confirmation":
        memory_store.record_verification(
            project_dir,
            outcome="gated",
            summary=f"Nikto/heavy scan for {target} is pending human confirmation.",
            evidence_refs=evidence,
            next_constraints=["Obtain explicit high-risk gate confirmation before running heavy scan automation."],
        )
    elif status == "missing-tool":
        memory_store.record_verification(
            project_dir,
            outcome="blocked",
            summary=f"Nikto scan for {target} is blocked because the tool is missing.",
            failure_reason="missing nikto tool",
            next_constraints=["Install or choose an approved alternative before relying on Nikto coverage."],
        )
    elif status == "completed":
        memory_store.add_surface_path(
            project_dir,
            source="vulnerability_analysis",
            title=f"Nikto scan: {target}",
            summary="Nikto completed; review scanner output as evidence, not as proof by itself.",
            evidence_refs=evidence,
            lane_id="assessment",
            dedupe_key=f"nikto:{target}",
        )
    else:
        memory_store.record_verification(
            project_dir,
            outcome="inconclusive",
            summary=f"Nikto scan for {target} ended with status={status}.",
            evidence_refs=evidence,
            failure_reason=f"nikto status {status}",
            next_constraints=["Review scanner output or rerun only within the authorized window."],
        )


def command_init_project(args: argparse.Namespace) -> None:
    project_id = args.project_id or slug(args.name)
    project_dir = ensure_project(project_id)
    scope = make_scope(
        project_id=project_id,
        name=args.name,
        targets=args.target or [],
        excluded=args.exclude or [],
        include_subdomains=args.include_subdomains,
    )
    save_scope(project_dir, scope)
    memory_store.ensure_memory(project_dir)
    memory_store.add_goal(
        project_dir,
        title=f"Assessment: {args.name}",
        summary=f"Scoped Kali-style assessment for targets: {', '.join(args.target or []) or 'none'}",
        evidence_refs=[str(project_dir / "scope.json")],
    )
    record_event(project_dir, "init-project", {"project_id": project_id})
    print(json.dumps({"project": str(project_dir), "scope": str(project_dir / "scope.json")}, indent=2))


def command_check_env(args: argparse.Namespace) -> None:
    project_dir = ensure_project(args.project or "env-check")
    status = tool_status()
    write_json(project_dir / "tool-status.json", status)
    print(json.dumps({"project": str(project_dir), "tools": status}, indent=2))


def command_install_tools(args: argparse.Namespace) -> None:
    project_dir = ensure_project(args.project or "tool-install")
    result = install_profile(args.profile, project_dir, execute=args.execute)
    write_json(project_dir / "install-plan.json", result)
    print(json.dumps(result, indent=2))


def command_validate_scope(args: argparse.Namespace) -> None:
    project_dir = project_dir_arg(args.project)
    scope = load_scope(project_dir)
    targets = args.target or scope_targets(scope)
    for target in targets:
        assert_in_scope(target, scope)
    print(json.dumps({"status": "ok", "targets": targets}, indent=2))


def command_scan(args: argparse.Namespace) -> None:
    project_dir = project_dir_arg(args.project)
    scope = load_scope(project_dir)
    targets = args.target or scope_targets(scope)
    results = [scan_target(project_dir, scope, target, args.ports, args.use_nmap) for target in targets]
    for result in results:
        record_scan_memory(project_dir, result)
    print(json.dumps({"status": "completed", "results": results}, indent=2))


def command_web(args: argparse.Namespace) -> None:
    project_dir = project_dir_arg(args.project)
    scope = load_scope(project_dir)
    targets = args.target or scope_targets(scope)
    results = [web_baseline(project_dir, scope, target, use_whatweb=args.whatweb) for target in targets]
    for target, result in zip(targets, results):
        record_web_memory(project_dir, target, result)
    print(json.dumps({"status": "completed", "results": results}, indent=2))


def command_vuln(args: argparse.Namespace) -> None:
    project_dir = project_dir_arg(args.project)
    scope = load_scope(project_dir)
    target = args.target
    result = nikto_scan(project_dir, scope, target, confirmed=args.confirm_risk)
    record_vuln_memory(project_dir, target, result)
    print(json.dumps(result, indent=2))


def command_exploit_gate(args: argparse.Namespace) -> None:
    project_dir = project_dir_arg(args.project)
    result = prepare_exploitation(project_dir, target=args.target, confirmed=args.confirm_risk)
    memory_store.record_verification(
        project_dir,
        outcome="success" if result.get("status") == "confirmed" else "gated",
        summary=f"Exploit gate status for {args.target or 'project'}: {result.get('status')}",
        next_constraints=None
        if result.get("status") == "confirmed"
        else ["Obtain explicit exploitation approval before attempting exploit-like actions."],
    )
    print(json.dumps(result, indent=2))


def command_report(args: argparse.Namespace) -> None:
    project_dir = project_dir_arg(args.project)
    result = write_report(project_dir)
    print(json.dumps(result, indent=2))


def command_memory(args: argparse.Namespace) -> None:
    project_dir = project_dir_arg(args.project)
    if args.next:
        result = memory_store.generate_next_constraints(project_dir)
    else:
        result = memory_store.summarize_memory(project_dir)
    print(json.dumps({"status": "ok", "memory": result}, indent=2))


def command_candidate(args: argparse.Namespace) -> None:
    project_dir = project_dir_arg(args.project)
    try:
        candidate = memory_store.add_candidate(
            project_dir,
            title=args.title,
            hypothesis=args.hypothesis,
            lane_id=args.lane,
            constraints=args.constraint,
            evidence_refs=args.evidence,
            status=args.status,
            dedupe_key=args.dedupe_key,
        )
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    record_event(project_dir, "candidate", {"id": candidate["id"], "lane_id": candidate.get("lane_id")})
    print(json.dumps({"status": "ok", "candidate": candidate}, indent=2))


def command_attempt(args: argparse.Namespace) -> None:
    project_dir = project_dir_arg(args.project)
    try:
        attempt = memory_store.record_attempt(
            project_dir,
            candidate_id=args.candidate_id,
            outcome=args.outcome,
            summary=args.summary,
            evidence_refs=args.evidence,
            failure_reason=args.failure_reason,
            next_constraints=args.next_constraint,
        )
    except ValueError as exc:
        raise SystemExit(str(exc)) from exc
    record_event(project_dir, "attempt", {"id": attempt["id"], "candidate_id": args.candidate_id, "outcome": args.outcome})
    print(json.dumps({"status": "ok", "attempt": attempt}, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Kali-style authorized assessment workflow")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init-project", help="create a scoped assessment project")
    init.add_argument("--name", required=True)
    init.add_argument("--project-id")
    init.add_argument("--target", action="append", default=[])
    init.add_argument("--exclude", action="append", default=[])
    init.add_argument("--include-subdomains", action="store_true")
    init.set_defaults(func=command_init_project)

    env = sub.add_parser("check-env", help="check installed tool status")
    env.add_argument("--project")
    env.set_defaults(func=command_check_env)

    install = sub.add_parser("install-tools", help="plan or execute apt tool installation")
    install.add_argument("--profile", default="safe-core")
    install.add_argument("--project")
    install.add_argument("--execute", action="store_true", help="actually run sudo apt-get install")
    install.set_defaults(func=command_install_tools)

    validate = sub.add_parser("validate-scope", help="confirm targets are in scope")
    validate.add_argument("--project", required=True)
    validate.add_argument("--target", action="append")
    validate.set_defaults(func=command_validate_scope)

    scan = sub.add_parser("scan", help="run bounded TCP scan or nmap when available")
    scan.add_argument("--project", required=True)
    scan.add_argument("--target", action="append")
    scan.add_argument("--ports")
    scan.add_argument("--use-nmap", action="store_true")
    scan.set_defaults(func=command_scan)

    web = sub.add_parser("web", help="run safe HTTP baseline checks")
    web.add_argument("--project", required=True)
    web.add_argument("--target", action="append")
    web.add_argument("--whatweb", action="store_true")
    web.set_defaults(func=command_web)

    vuln = sub.add_parser("vuln-nikto", help="run Nikto behind a high-risk gate")
    vuln.add_argument("--project", required=True)
    vuln.add_argument("--target", required=True)
    vuln.add_argument("--confirm-risk", action="store_true")
    vuln.set_defaults(func=command_vuln)

    gate = sub.add_parser("exploit-gate", help="record or confirm exploitation gate")
    gate.add_argument("--project", required=True)
    gate.add_argument("--target")
    gate.add_argument("--confirm-risk", action="store_true")
    gate.set_defaults(func=command_exploit_gate)

    report = sub.add_parser("report", help="generate Markdown and JSON report")
    report.add_argument("--project", required=True)
    report.set_defaults(func=command_report)

    mem = sub.add_parser("memory", help="show structured route memory or generate next constraints")
    mem.add_argument("--project", required=True)
    mem_group = mem.add_mutually_exclusive_group(required=True)
    mem_group.add_argument("--summary", action="store_true")
    mem_group.add_argument("--next", action="store_true")
    mem.set_defaults(func=command_memory)

    candidate = sub.add_parser("candidate", help="record a structured candidate route")
    candidate.add_argument("--project", required=True)
    candidate.add_argument("--title", required=True)
    candidate.add_argument("--hypothesis", required=True)
    candidate.add_argument("--lane", default="main")
    candidate.add_argument("--constraint", action="append")
    candidate.add_argument("--evidence", action="append")
    candidate.add_argument("--status", choices=memory_store.VALID_CANDIDATE_STATUSES, default="proposed")
    candidate.add_argument("--dedupe-key")
    candidate.set_defaults(func=command_candidate)

    attempt = sub.add_parser("attempt", help="record a candidate attempt and its evidence outcome")
    attempt.add_argument("--project", required=True)
    attempt.add_argument("--candidate-id", required=True)
    attempt.add_argument("--outcome", choices=memory_store.VALID_OUTCOMES, required=True)
    attempt.add_argument("--summary", required=True)
    attempt.add_argument("--evidence", action="append")
    attempt.add_argument("--failure-reason")
    attempt.add_argument("--next-constraint", action="append")
    attempt.set_defaults(func=command_attempt)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
