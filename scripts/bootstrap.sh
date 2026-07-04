#!/usr/bin/env bash
set -euo pipefail

PROFILE="python-core"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --profile)
      PROFILE="${2:-}"
      shift 2
      ;;
    *)
      echo "unknown argument: $1" >&2
      exit 2
      ;;
  esac
done

cd "$(dirname "$0")/.."

python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

case "$PROFILE" in
  python-core|safe-core|web|network|mobile|forensics|crypto|ai-agent)
    ;;
  node-browser)
    if ! command -v node >/dev/null 2>&1 || ! command -v npm >/dev/null 2>&1; then
      echo "Node/npm not found. Install Node 20 or use nvm before node-browser profile." >&2
      exit 1
    fi
    npm install
    ;;
  full-lab)
    if ! command -v node >/dev/null 2>&1 || ! command -v npm >/dev/null 2>&1; then
      echo "Node/npm not found. Python core installed; install Node before full-lab browser dependencies." >&2
      exit 1
    fi
    npm install
    ;;
  *)
    echo "unknown profile: $PROFILE" >&2
    exit 2
    ;;
esac

python scripts/sec.py env check --profile "$PROFILE"
