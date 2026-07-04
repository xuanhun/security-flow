from __future__ import annotations

from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parent
REPO_ROOT = PACKAGE_ROOT.parents[1]
FRAMEWORK_DIR = REPO_ROOT / "framework"
ENGAGEMENTS_DIR = REPO_ROOT / "engagements"
KNOWLEDGE_DIR = REPO_ROOT / "knowledge"
CASES_DIR = REPO_ROOT / "cases"


def engagement_dir(engagement_id: str) -> Path:
    return ENGAGEMENTS_DIR / engagement_id


def ensure_base_dirs() -> None:
    for path in (FRAMEWORK_DIR, ENGAGEMENTS_DIR, KNOWLEDGE_DIR, CASES_DIR):
        path.mkdir(parents=True, exist_ok=True)
