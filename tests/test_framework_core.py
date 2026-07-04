from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from security_framework.scope import assert_in_scope
from security_framework.utils import LOG_FIELDS, standard_log_record


def test_standard_log_record_has_required_fields() -> None:
    record = standard_log_record(engagement_id="demo", phase="recon", action="probe")
    assert set(LOG_FIELDS).issubset(record)
    assert record["engagement_id"] == "demo"
    assert record["phase"] == "recon"
    assert record["evidence_refs"] == []


def test_scope_accepts_exact_target_and_rejects_other_target() -> None:
    scope = {"targets": [{"value": "127.0.0.1", "include_subdomains": False}], "excluded": []}
    assert_in_scope("http://127.0.0.1:8000", scope)
    try:
        assert_in_scope("192.0.2.10", scope)
    except SystemExit as exc:
        assert "out of scope" in str(exc)
    else:
        raise AssertionError("out-of-scope target was accepted")
