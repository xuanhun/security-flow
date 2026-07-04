#!/usr/bin/env bash
set -euo pipefail

SKILL_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"

if [[ -s "$NVM_DIR/nvm.sh" ]]; then
  # shellcheck disable=SC1090
  . "$NVM_DIR/nvm.sh"
  nvm use "$(tr -d '[:space:]' < "$SKILL_ROOT/.nvmrc")" >/dev/null
fi

if ! command -v node >/dev/null 2>&1; then
  echo "node is required for ctf_browser.js" >&2
  exit 2
fi

if ! command -v npm >/dev/null 2>&1; then
  echo "npm is required for the Playwright runtime. Install npm in the nvm node version from $SKILL_ROOT/.nvmrc." >&2
  exit 2
fi

exec node "$SKILL_ROOT/scripts/ctf_browser.js" "$@"
