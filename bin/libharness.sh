#!/usr/bin/env bash

set -euo pipefail

readonly HARNESS_DEFAULT_REPO_URL="${HARNESS_DEFAULT_REPO_URL:-https://github.com/Simon-Initiative/harness.git}"
readonly HARNESS_DEFAULT_REPO_PATH="${HARNESS_DEFAULT_REPO_PATH:-$HOME/.local/share/harness}"
readonly HARNESS_CONFIG_PATH="${HARNESS_CONFIG_PATH:-$HOME/.local/share/harness/.install-config}"
readonly HARNESS_VERSION_FILE="version.json"

harness_log() {
  printf '%s\n' "$*"
}

harness_err() {
  printf 'error: %s\n' "$*" >&2
}

harness_warn() {
  printf 'warning: %s\n' "$*" >&2
}

harness_script_dir() {
  cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd
}

harness_repo_root_from_script() {
  cd "$(harness_script_dir)/.." >/dev/null 2>&1 && pwd
}

harness_current_origin_url() {
  local repo_root
  repo_root="$(harness_repo_root_from_script)"

  if git -C "$repo_root" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    git -C "$repo_root" remote get-url origin 2>/dev/null || true
  fi
}

harness_repo_url() {
  if [[ -n "${HARNESS_REPO_URL:-}" ]]; then
    printf '%s\n' "$HARNESS_REPO_URL"
    return
  fi

  local origin_url
  origin_url="$(harness_current_origin_url)"
  if [[ -n "$origin_url" ]]; then
    printf '%s\n' "$origin_url"
    return
  fi

  printf '%s\n' "$HARNESS_DEFAULT_REPO_URL"
}

harness_config_dir() {
  dirname "$HARNESS_CONFIG_PATH"
}

harness_load_config() {
  if [[ -f "$HARNESS_CONFIG_PATH" ]]; then
    # shellcheck disable=SC1090
    source "$HARNESS_CONFIG_PATH"
  fi
}

harness_save_config() {
  mkdir -p "$(harness_config_dir)"
  cat >"$HARNESS_CONFIG_PATH" <<EOF
CHANNEL=${CHANNEL}
REPO_PATH=${REPO_PATH}
REPO_URL=${REPO_URL}
INSTALLED_VERSION=${INSTALLED_VERSION:-}
CODEX_TARGET_ROOT=${CODEX_TARGET_ROOT:-}
CODEX_NAMESPACE=${CODEX_NAMESPACE:-}
CLAUDE_TARGET_ROOT=${CLAUDE_TARGET_ROOT:-}
CLAUDE_NAMESPACE=${CLAUDE_NAMESPACE:-}
EOF
}

harness_require_git() {
  if ! command -v git >/dev/null 2>&1; then
    harness_err "git is required"
    exit 1
  fi
}

harness_normalize_channel() {
  local requested="${1:-stable}"
  case "$requested" in
    stable|latest)
      printf '%s\n' "$requested"
      ;;
    *)
      harness_err "unknown channel '$requested' (expected 'stable' or 'latest')"
      exit 1
      ;;
  esac
}

harness_detect_default_branch() {
  local repo_path="$1"
  local ref

  ref="$(git -C "$repo_path" symbolic-ref refs/remotes/origin/HEAD 2>/dev/null || true)"
  if [[ -n "$ref" ]]; then
    printf '%s\n' "${ref##refs/remotes/origin/}"
    return
  fi

  ref="$(git -C "$repo_path" remote show origin 2>/dev/null | sed -n 's/.*HEAD branch: //p' | head -n 1)"
  if [[ -n "$ref" ]]; then
    printf '%s\n' "$ref"
    return
  fi

  printf 'master\n'
}

harness_clone_or_fetch_repo() {
  local repo_path="$1"
  local repo_url="$2"

  mkdir -p "$(dirname "$repo_path")"
  if [[ ! -d "$repo_path/.git" ]]; then
    harness_log "Cloning harness repo into $repo_path"
    git clone "$repo_url" "$repo_path"
  else
    harness_log "Fetching updates in $repo_path"
    git -C "$repo_path" fetch --tags origin
  fi
}

harness_latest_release_tag() {
  local repo_path="$1"
  git -C "$repo_path" tag --sort=-version:refname | head -n 1
}

harness_checkout_channel() {
  local repo_path="$1"
  local channel="$2"
  local default_branch
  local tag

  if [[ "$channel" == "stable" ]]; then
    tag="$(harness_latest_release_tag "$repo_path")"
    if [[ -n "$tag" ]]; then
      git -C "$repo_path" checkout --detach "$tag" >/dev/null
      printf '%s\n' "$tag"
      return
    fi

    harness_warn "no release tags found; falling back to default branch for stable"
  fi

  default_branch="$(harness_detect_default_branch "$repo_path")"
  git -C "$repo_path" checkout "$default_branch" >/dev/null 2>&1 || git -C "$repo_path" checkout -B "$default_branch" "origin/$default_branch" >/dev/null
  git -C "$repo_path" reset --hard "origin/$default_branch" >/dev/null
  printf '%s\n' "origin/$default_branch"
}

harness_version_file_path() {
  local repo_path="$1"
  printf '%s\n' "$repo_path/$HARNESS_VERSION_FILE"
}

harness_repo_version() {
  local repo_path="$1"
  local version_file
  local version

  version_file="$(harness_version_file_path "$repo_path")"
  if [[ ! -f "$version_file" ]]; then
    harness_err "missing $HARNESS_VERSION_FILE in $repo_path"
    exit 1
  fi

  version="$(sed -n 's/^[[:space:]]*"version"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' "$version_file" | head -n 1)"
  if [[ -z "$version" ]]; then
    harness_err "unable to read version from $version_file"
    exit 1
  fi

  printf '%s\n' "$version"
}

harness_current_version() {
  local repo_path="$1"
  harness_repo_version "$repo_path"
}

harness_list_skill_dirs() {
  local repo_path="$1"
  find "$repo_path/skills" -mindepth 1 -maxdepth 1 -type d | sort
}

harness_skill_name_for_dir() {
  local skill_dir="$1"
  local metadata_name

  metadata_name="$(sed -n 's/^name:[[:space:]]*//p' "$skill_dir/SKILL.md" | head -n 1)"
  if [[ -n "$metadata_name" ]]; then
    printf '%s\n' "$metadata_name"
    return
  fi

  printf 'harness-%s\n' "$(basename "$skill_dir")"
}

harness_detect_target_roots() {
  local targets=()

  if [[ -d "$HOME/.agents/skills" ]]; then
    targets+=("$HOME/.agents/skills")
  fi
  if [[ -d "$HOME/.claude/skills" ]]; then
    targets+=("$HOME/.claude/skills")
  fi

  if [[ "${#targets[@]}" -eq 0 ]]; then
    mkdir -p "$HOME/.agents/skills" "$HOME/.claude/skills"
    targets+=("$HOME/.agents/skills" "$HOME/.claude/skills")
  fi

  printf '%s\n' "${targets[@]}"
}

harness_namespace_marker_path() {
  local namespace_path="$1"
  printf '%s\n' "$namespace_path/.harness-install-root"
}

harness_namespace_belongs_to_repo() {
  local namespace_path="$1"
  local repo_path="$2"
  local marker

  marker="$(harness_namespace_marker_path "$namespace_path")"
  [[ -f "$marker" ]] || return 1
  grep -Fxq "REPO_PATH=$repo_path" "$marker"
}

harness_write_namespace_marker() {
  local namespace_path="$1"
  local repo_path="$2"
  local channel="$3"

  cat >"$(harness_namespace_marker_path "$namespace_path")" <<EOF
REPO_PATH=$repo_path
CHANNEL=$channel
EOF
}

harness_pick_namespace() {
  local target_root="$1"
  local repo_path="$2"
  local preferred="${3:-harness}"
  local candidate="$preferred"
  local index=0
  local path

  while :; do
    path="$target_root/$candidate"
    if [[ ! -e "$path" && ! -L "$path" ]]; then
      printf '%s\n' "$candidate"
      return
    fi

    if [[ -d "$path" ]] && harness_namespace_belongs_to_repo "$path" "$repo_path"; then
      printf '%s\n' "$candidate"
      return
    fi

    index=$((index + 1))
    candidate="${preferred}_$index"
  done
}

harness_link_skill() {
  local skill_dir="$1"
  local namespace_path="$2"
  local skill_name="$3"
  local link_path="$namespace_path/$skill_name"
  local target_path="$skill_dir"

  if [[ -L "$link_path" ]]; then
    local existing_target
    existing_target="$(readlink "$link_path")"
    if [[ "$existing_target" == "$target_path" ]]; then
      return
    fi
    rm -f "$link_path"
    ln -s "$target_path" "$link_path"
    return
  fi

  if [[ -e "$link_path" ]]; then
    harness_warn "leaving existing non-symlink in place: $link_path"
    return
  fi

  ln -s "$target_path" "$link_path"
}

harness_install_target() {
  local repo_path="$1"
  local channel="$2"
  local target_root="$3"
  local namespace="$4"
  local namespace_path="$target_root/$namespace"
  local linked=()
  local skill_dir
  local skill_name

  mkdir -p "$namespace_path"
  harness_write_namespace_marker "$namespace_path" "$repo_path" "$channel"

  while IFS= read -r skill_dir; do
    skill_name="$(harness_skill_name_for_dir "$skill_dir")"
    harness_link_skill "$skill_dir" "$namespace_path" "$skill_name"
    linked+=("$skill_name")
  done < <(harness_list_skill_dirs "$repo_path")

  printf '%s\n' "${linked[@]}"
}

harness_repair_target_links() {
  local repo_path="$1"
  local channel="$2"
  local target_root="$3"
  local namespace="$4"
  local namespace_path="$target_root/$namespace"
  local skill_dir
  local skill_name

  [[ -d "$namespace_path" ]] || return 0
  harness_write_namespace_marker "$namespace_path" "$repo_path" "$channel"

  while IFS= read -r skill_dir; do
    skill_name="$(harness_skill_name_for_dir "$skill_dir")"
    if [[ ! -e "$namespace_path/$skill_name" || -L "$namespace_path/$skill_name" ]]; then
      harness_link_skill "$skill_dir" "$namespace_path" "$skill_name"
    fi
  done < <(harness_list_skill_dirs "$repo_path")
}

harness_target_label() {
  local target_root="$1"
  if [[ "$target_root" == "$HOME/.agents/skills" ]]; then
    printf 'Codex\n'
  elif [[ "$target_root" == "$HOME/.claude/skills" ]]; then
    printf 'Claude Code\n'
  else
    printf '%s\n' "$target_root"
  fi
}

harness_collect_broken_links() {
  local target_root="$1"
  local namespace="$2"
  local namespace_path="$target_root/$namespace"

  [[ -d "$namespace_path" ]] || return 0
  find "$namespace_path" -mindepth 1 -maxdepth 1 -type l ! -exec test -e {} \; -print | sort
}
