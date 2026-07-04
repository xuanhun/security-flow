#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC = REPO_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from security_framework import env, engagement, knowledge, memory, report, summary
from security_framework.paths import engagement_dir
from security_framework.probes import agent_ws, artifact, browser, local, scan, web
from security_framework.scope import assert_in_scope, load_scope, target_values
from security_framework.utils import read_json, slug, write_json


def engagement_path(value: str) -> Path:
    path = engagement_dir(slug(value))
    if not path.exists():
        raise SystemExit(f"unknown engagement: {value}")
    return path


def print_json(data: object) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))


def cmd_init(args: argparse.Namespace) -> None:
    print_json(
        engagement.init_engagement(
            engagement_id=args.id,
            name=args.name,
            engagement_type=args.type,
            targets=args.target or [],
            excluded=args.exclude or [],
        )
    )


def cmd_phase(args: argparse.Namespace) -> None:
    path = engagement_path(args.engagement)
    if args.phase_command == "enter":
        state = engagement.phase_enter(path, args.phase)
    elif args.phase_command == "exit":
        state = engagement.phase_exit(path, args.phase)
    else:
        state = engagement.phase_next(path)
    print_json({"status": "ok", "state": state})


def cmd_scope_validate(args: argparse.Namespace) -> None:
    path = engagement_path(args.engagement)
    scope = load_scope(path)
    targets = args.target or target_values(scope)
    for target in targets:
        assert_in_scope(target, scope)
    engagement.log_event(path, "scope-validate", tool="scope", target=", ".join(targets), outcome="success")
    print_json({"status": "ok", "targets": targets})


def cmd_knowledge_ingest(args: argparse.Namespace) -> None:
    print_json(knowledge.ingest(Path(args.path), args.type, domain=args.domain, phase=args.phase))


def cmd_knowledge_reindex(args: argparse.Namespace) -> None:
    print_json(knowledge.reindex())


def cmd_knowledge_search(args: argparse.Namespace) -> None:
    print_json(knowledge.search(args.query, phase=args.phase, domain=args.domain, limit=args.limit))


def cmd_knowledge_browse(args: argparse.Namespace) -> None:
    print_json(knowledge.browse(domain=args.domain, phase=args.phase, resource_type=args.type, limit=args.limit))


def cmd_knowledge_recall(args: argparse.Namespace) -> None:
    path = engagement_path(args.engagement)
    print_json(knowledge.recall(path, args.phase, limit=args.limit))


def cmd_knowledge_show(args: argparse.Namespace) -> None:
    print_json(knowledge.show(args.id))


def cmd_probe(args: argparse.Namespace) -> None:
    path = engagement_path(args.engagement)
    if args.probe_command == "web":
        result = web.baseline(path, args.target, timeout=args.timeout)
    elif args.probe_command == "scan":
        result = scan.tcp_scan(path, args.target, ports=args.ports, timeout=args.timeout)
    elif args.probe_command == "artifact":
        result = artifact.inventory(path, Path(args.path))
    elif args.probe_command == "browser":
        result = browser.check(path)
    elif args.probe_command == "agent-ws":
        result = agent_ws.probe(path, args.url, message=args.message, timeout=args.timeout)
    elif args.probe_command == "crypto":
        result = local.crypto_triage(path, args.value)
    elif args.probe_command in {"mobile", "image", "pdf"}:
        result = local.file_stub(path, args.probe_command, Path(args.path))
    else:
        raise SystemExit(f"unknown probe: {args.probe_command}")
    print_json(result)


def cmd_memory(args: argparse.Namespace) -> None:
    path = engagement_path(args.engagement)
    if args.memory_command == "summary":
        result = memory.summary(path)
    elif args.memory_command == "next":
        result = memory.next_constraints(path)
    elif args.memory_command == "candidate":
        state = read_json(path / "state.json", {})
        refs = (state.get("knowledge_recalls") or {}).get(state.get("phase"), [])
        result = memory.add_candidate(
            path,
            title=args.title,
            hypothesis=args.hypothesis,
            constraints=args.constraint or [],
            evidence_refs=args.evidence or [],
            knowledge_refs=args.knowledge_ref or refs,
            lane_id=args.lane,
            status=args.status,
        )
    else:
        result = memory.record_attempt(
            path,
            candidate_id=args.candidate_id,
            outcome=args.outcome,
            summary=args.summary,
            evidence_refs=args.evidence or [],
            failure_reason=args.failure_reason,
            next_constraints_list=args.next_constraint or [],
        )
    print_json({"status": "ok", "memory": result})


def cmd_context(args: argparse.Namespace) -> None:
    path = engagement_path(args.engagement)
    if args.context_command == "show":
        print((path / "context" / "current.md").read_text(encoding="utf-8"))
        return
    if args.context_command == "snapshot":
        print_json(read_json(path / "context" / "snapshot.json", {}))
        return
    current = (path / "context" / "current.md").read_text(encoding="utf-8") if (path / "context" / "current.md").exists() else ""
    (path / "context" / "current.md").write_text(current.rstrip() + "\n\n" + args.text + "\n", encoding="utf-8")
    engagement.log_event(path, "context-append", tool="context", outcome="success")
    print_json({"status": "ok", "context": str(path / "context" / "current.md")})


def cmd_report(args: argparse.Namespace) -> None:
    print_json(report.generate(engagement_path(args.engagement)))


def cmd_summary(args: argparse.Namespace) -> None:
    path = engagement_path(args.engagement)
    if args.summary_command == "generate":
        print_json(
            summary.generate(
                path,
                result_status=args.result_status,
                outcome_summary=args.outcome_summary,
                proof=args.proof or [],
                next_steps=args.next_step or [],
                distillation=args.distillation or [],
                flag=args.flag,
                notes=args.note or [],
            )
        )
    else:
        result = summary.validate(path)
        print_json(result)
        if result["status"] != "ok":
            raise SystemExit(1)


def cmd_env_check(args: argparse.Namespace) -> None:
    root = engagement_path(args.engagement) if args.engagement else None
    print_json(env.check(root, profile=args.profile))


def cmd_tools_plan(args: argparse.Namespace) -> None:
    print_json(env.plan(args.profile))


def cmd_validate(args: argparse.Namespace) -> None:
    errors: list[str] = []
    if (REPO_ROOT / "ai").exists():
        errors.append("ai directory still exists")
    old_workflow_marker = "ai" + "/workflows"
    for path in (REPO_ROOT / "AGENTS.md", REPO_ROOT / "README.md"):
        if path.exists() and old_workflow_marker in path.read_text(encoding="utf-8", errors="ignore"):
            errors.append(f"old workflow reference in {path}")
    if not (REPO_ROOT / "knowledge" / "registry.jsonl").exists():
        errors.append("knowledge registry missing")
    status = "ok" if not errors else "failed"
    print_json({"status": status, "tier": args.tier, "errors": errors})
    if errors:
        raise SystemExit(1)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Unified local security assessment framework")
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init", help="initialize an engagement")
    init.add_argument("--id", required=True)
    init.add_argument("--name", required=True)
    init.add_argument("--type", choices=engagement.ENGAGEMENT_TYPES, required=True)
    init.add_argument("--target", action="append", default=[])
    init.add_argument("--exclude", action="append", default=[])
    init.set_defaults(func=cmd_init)

    phase = sub.add_parser("phase", help="manage engagement phases")
    phase_sub = phase.add_subparsers(dest="phase_command", required=True)
    for name in ("enter", "exit"):
        item = phase_sub.add_parser(name)
        item.add_argument("--engagement", required=True)
        item.add_argument("--phase", required=True, choices=engagement.PHASES)
        item.set_defaults(func=cmd_phase)
    nxt = phase_sub.add_parser("next")
    nxt.add_argument("--engagement", required=True)
    nxt.set_defaults(func=cmd_phase)

    scope = sub.add_parser("scope", help="scope commands")
    scope_sub = scope.add_subparsers(dest="scope_command", required=True)
    validate_scope = scope_sub.add_parser("validate")
    validate_scope.add_argument("--engagement", required=True)
    validate_scope.add_argument("--target", action="append")
    validate_scope.set_defaults(func=cmd_scope_validate)

    know = sub.add_parser("knowledge", help="local knowledge base commands")
    know_sub = know.add_subparsers(dest="knowledge_command", required=True)
    ingest = know_sub.add_parser("ingest")
    ingest.add_argument("--path", required=True)
    ingest.add_argument("--type", choices=["case", "playbook", "tool", "report", "asset", "reference"], required=True)
    ingest.add_argument("--domain")
    ingest.add_argument("--phase")
    ingest.set_defaults(func=cmd_knowledge_ingest)
    reindex = know_sub.add_parser("reindex")
    reindex.set_defaults(func=cmd_knowledge_reindex)
    search = know_sub.add_parser("search")
    search.add_argument("--query", required=True)
    search.add_argument("--phase")
    search.add_argument("--domain")
    search.add_argument("--limit", type=int, default=10)
    search.set_defaults(func=cmd_knowledge_search)
    browse = know_sub.add_parser("browse")
    browse.add_argument("--domain")
    browse.add_argument("--phase")
    browse.add_argument("--type", choices=["case", "playbook", "tool", "report", "asset", "reference"])
    browse.add_argument("--limit", type=int, default=50)
    browse.set_defaults(func=cmd_knowledge_browse)
    recall = know_sub.add_parser("recall")
    recall.add_argument("--engagement", required=True)
    recall.add_argument("--phase", required=True, choices=engagement.PHASES)
    recall.add_argument("--limit", type=int, default=10)
    recall.set_defaults(func=cmd_knowledge_recall)
    show = know_sub.add_parser("show")
    show.add_argument("--id", required=True)
    show.set_defaults(func=cmd_knowledge_show)

    probe = sub.add_parser("probe", help="run safe probes")
    probe_sub = probe.add_subparsers(dest="probe_command", required=True)
    pweb = probe_sub.add_parser("web")
    pweb.add_argument("--engagement", required=True)
    pweb.add_argument("--target", required=True)
    pweb.add_argument("--timeout", type=int, default=15)
    pweb.set_defaults(func=cmd_probe)
    pscan = probe_sub.add_parser("scan")
    pscan.add_argument("--engagement", required=True)
    pscan.add_argument("--target", required=True)
    pscan.add_argument("--ports")
    pscan.add_argument("--timeout", type=float, default=1.0)
    pscan.set_defaults(func=cmd_probe)
    part = probe_sub.add_parser("artifact")
    part.add_argument("--engagement", required=True)
    part.add_argument("--path", required=True)
    part.set_defaults(func=cmd_probe)
    pbrowser = probe_sub.add_parser("browser")
    pbrowser.add_argument("--engagement", required=True)
    pbrowser.set_defaults(func=cmd_probe)
    pagent = probe_sub.add_parser("agent-ws")
    pagent.add_argument("--engagement", required=True)
    pagent.add_argument("--url", required=True)
    pagent.add_argument("--message")
    pagent.add_argument("--timeout", type=float, default=30.0)
    pagent.set_defaults(func=cmd_probe)
    pcrypto = probe_sub.add_parser("crypto")
    pcrypto.add_argument("--engagement", required=True)
    pcrypto.add_argument("--value", required=True)
    pcrypto.set_defaults(func=cmd_probe)
    for name in ("mobile", "image", "pdf"):
        item = probe_sub.add_parser(name)
        item.add_argument("--engagement", required=True)
        item.add_argument("--path", required=True)
        item.set_defaults(func=cmd_probe)

    mem = sub.add_parser("memory", help="structured memory commands")
    mem_sub = mem.add_subparsers(dest="memory_command", required=True)
    msum = mem_sub.add_parser("summary")
    msum.add_argument("--engagement", required=True)
    msum.set_defaults(func=cmd_memory)
    mnxt = mem_sub.add_parser("next")
    mnxt.add_argument("--engagement", required=True)
    mnxt.set_defaults(func=cmd_memory)
    mcand = mem_sub.add_parser("candidate")
    mcand.add_argument("--engagement", required=True)
    mcand.add_argument("--title", required=True)
    mcand.add_argument("--hypothesis", required=True)
    mcand.add_argument("--constraint", action="append")
    mcand.add_argument("--evidence", action="append")
    mcand.add_argument("--knowledge-ref", action="append")
    mcand.add_argument("--lane", default="main")
    mcand.add_argument("--status", choices=memory.VALID_STATUSES, default="proposed")
    mcand.set_defaults(func=cmd_memory)
    matt = mem_sub.add_parser("attempt")
    matt.add_argument("--engagement", required=True)
    matt.add_argument("--candidate-id", required=True)
    matt.add_argument("--outcome", choices=memory.VALID_OUTCOMES, required=True)
    matt.add_argument("--summary", required=True)
    matt.add_argument("--evidence", action="append")
    matt.add_argument("--failure-reason")
    matt.add_argument("--next-constraint", action="append")
    matt.set_defaults(func=cmd_memory)

    ctx = sub.add_parser("context", help="context commands")
    ctx_sub = ctx.add_subparsers(dest="context_command", required=True)
    for name in ("show", "snapshot"):
        item = ctx_sub.add_parser(name)
        item.add_argument("--engagement", required=True)
        item.set_defaults(func=cmd_context)
    capp = ctx_sub.add_parser("append")
    capp.add_argument("--engagement", required=True)
    capp.add_argument("--text", required=True)
    capp.set_defaults(func=cmd_context)

    rep = sub.add_parser("report")
    rep.add_argument("--engagement", required=True)
    rep.set_defaults(func=cmd_report)

    summ = sub.add_parser("summary", help="generate or validate post-test summaries")
    summ_sub = summ.add_subparsers(dest="summary_command", required=True)
    sgen = summ_sub.add_parser("generate")
    sgen.add_argument("--engagement", required=True)
    sgen.add_argument("--result-status", choices=summary.RESULT_STATUSES, required=True)
    sgen.add_argument("--outcome-summary", required=True)
    sgen.add_argument("--proof", action="append")
    sgen.add_argument("--next-step", action="append")
    sgen.add_argument("--distillation", action="append")
    sgen.add_argument("--flag")
    sgen.add_argument("--note", action="append")
    sgen.set_defaults(func=cmd_summary)
    sval = summ_sub.add_parser("validate")
    sval.add_argument("--engagement", required=True)
    sval.set_defaults(func=cmd_summary)

    env_parser = sub.add_parser("env")
    env_sub = env_parser.add_subparsers(dest="env_command", required=True)
    env_check = env_sub.add_parser("check")
    env_check.add_argument("--profile", default="python-core")
    env_check.add_argument("--engagement")
    env_check.set_defaults(func=cmd_env_check)

    tools = sub.add_parser("tools")
    tools_sub = tools.add_subparsers(dest="tools_command", required=True)
    tplan = tools_sub.add_parser("plan")
    tplan.add_argument("--profile", required=True)
    tplan.set_defaults(func=cmd_tools_plan)

    validate = sub.add_parser("validate")
    validate.add_argument("--tier", default="smoke")
    validate.set_defaults(func=cmd_validate)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
