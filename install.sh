#!/usr/bin/env bash

set -euo pipefail

CHANNEL="${1:-stable}"
REPO_URL="${HARNESS_REPO_URL:-https://github.com/Simon-Initiative/harness.git}"
REPO_PATH="${HARNESS_REPO_PATH:-$HOME/.local/share/harness}"

mkdir -p "$(dirname "$REPO_PATH")"
if [[ ! -d "$REPO_PATH/.git" ]]; then
  git clone "$REPO_URL" "$REPO_PATH"
else
  git -C "$REPO_PATH" fetch --tags origin
fi

exec "$REPO_PATH/bin/harness-install" "$CHANNEL"
