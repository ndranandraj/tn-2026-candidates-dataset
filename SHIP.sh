#!/usr/bin/env bash
#
# SHIP.sh — one-shot publish of tn-2026-candidates-dataset to GitHub.
#
# What it does (in order):
#   1. Verifies prerequisites (git, gh, gh auth)
#   2. Creates a clean local repo directory
#   3. Copies all dataset files out of your blog repo
#   4. Makes the first commit on `main`
#   5. Creates a PUBLIC GitHub repo under your account
#   6. Pushes `main`
#   7. Tags v1.0 and creates a GitHub Release
#   8. (Optional) uploads candidates_2026.csv as a release asset
#
# Run this script AFTER you have:
#   • Installed the GitHub CLI:  brew install gh
#   • Logged in:                 gh auth login
#   • Produced candidates_2026.csv from your real dataset
#     (or re-run with SKIP_DATA_UPLOAD=1 and upload the CSV later via the UI)
#
# Usage:
#   chmod +x SHIP.sh
#   BLOG_REPO=/Users/anandrajr/path/to/anand-blog \
#   CSV_PATH=/path/to/candidates_2026.csv \
#     ./SHIP.sh
#
# To preview without pushing:
#   DRY_RUN=1 BLOG_REPO=/Users/anandrajr/path/to/anand-blog ./SHIP.sh

set -euo pipefail

# ------------------------- Config ---------------------------------------
REPO_NAME="tn-2026-candidates-dataset"
REPO_OWNER="ndranandraj"
TARGET_DIR="${TARGET_DIR:-$HOME/code/${REPO_NAME}}"
BLOG_REPO="${BLOG_REPO:-}"
CSV_PATH="${CSV_PATH:-}"
DRY_RUN="${DRY_RUN:-0}"
SKIP_DATA_UPLOAD="${SKIP_DATA_UPLOAD:-0}"

RELEASE_NOTES=$(cat <<'EOF'
# v1.0 — Initial public release

Candidate-level data for the TN 2026 Legislative Assembly, with namesake
groupings identified per `METHODOLOGY.md`.

## Contents

- `candidates_2026.csv` — full candidate list (see `DATA_DICTIONARY.md` for schema)

## Citation

Raj, Anand. *TN 2026 Candidates — Open Dataset* (v1.0). 2026. CC-BY-4.0.
https://github.com/ndranandraj/tn-2026-candidates-dataset

## Known limitations

See `METHODOLOGY.md` §6. Corrections welcome via Issues.
EOF
)

# ------------------------- Helpers --------------------------------------
step() { printf "\n\033[1;34m==>\033[0m %s\n" "$*"; }
run()  { if [[ "$DRY_RUN" == "1" ]]; then echo "  [dry-run] $*"; else eval "$*"; fi; }
bail() { printf "\n\033[1;31m✗\033[0m %s\n" "$*" >&2; exit 1; }

# ------------------------- Preflight ------------------------------------
step "Preflight checks"

command -v git >/dev/null || bail "git not found. Install Xcode CLT: xcode-select --install"
command -v gh  >/dev/null || bail "gh not found. Install: brew install gh"
gh auth status >/dev/null 2>&1 || bail "gh not authenticated. Run: gh auth login"

[[ -n "$BLOG_REPO"   ]] || bail "Set BLOG_REPO to your local anand-blog path."
[[ -d "$BLOG_REPO"   ]] || bail "BLOG_REPO '$BLOG_REPO' does not exist."

SRC="$BLOG_REPO/docs/outreach/dataset-repo"
[[ -d "$SRC" ]] || bail "Expected dataset files at $SRC — are you on the right branch?"

if [[ -e "$TARGET_DIR" ]]; then
  bail "Target '$TARGET_DIR' already exists. Move it or set TARGET_DIR=/some/other/path."
fi

if [[ "$SKIP_DATA_UPLOAD" != "1" ]]; then
  [[ -n "$CSV_PATH" ]] || bail "Set CSV_PATH to your candidates_2026.csv, or SKIP_DATA_UPLOAD=1"
  [[ -f "$CSV_PATH" ]] || bail "CSV_PATH '$CSV_PATH' not found."
fi

echo "  ✓ git, gh, auth OK"
echo "  ✓ BLOG_REPO = $BLOG_REPO"
echo "  ✓ TARGET    = $TARGET_DIR"
[[ "$SKIP_DATA_UPLOAD" == "1" ]] && echo "  • will skip release asset upload" \
                                 || echo "  ✓ CSV_PATH  = $CSV_PATH"

# ------------------------- Copy files -----------------------------------
step "Copying files from $SRC → $TARGET_DIR"

run "mkdir -p '$TARGET_DIR'"
# Copy tracked files only — skip .DS_Store etc. via rsync filters
run "rsync -av --exclude '.DS_Store' --exclude 'docs/' '$SRC/' '$TARGET_DIR/'"

# ------------------------- Local git init -------------------------------
step "Initialising local repo"

run "cd '$TARGET_DIR' && git init -b main"
run "cd '$TARGET_DIR' && git add ."
run "cd '$TARGET_DIR' && git commit -m 'Initial public release — v1.0

Candidate-level data for TN 2026, with namesake groupings documented in
METHODOLOGY.md. See README for usage and limitations.'"

# ------------------------- Create remote --------------------------------
step "Creating public GitHub repo ${REPO_OWNER}/${REPO_NAME}"

run "cd '$TARGET_DIR' && gh repo create '${REPO_OWNER}/${REPO_NAME}' \
  --public \
  --description 'Open dataset of candidate filings for the Tamil Nadu 2026 Legislative Assembly, with namesake/dummy-candidate groupings (CC-BY-4.0).' \
  --source . \
  --remote origin \
  --push"

# ------------------------- Tag & release --------------------------------
step "Tagging v1.0"
run "cd '$TARGET_DIR' && git tag -a v1.0 -m 'Initial public release' && git push origin v1.0"

step "Creating GitHub Release v1.0"
# NOTE: we intentionally bypass the eval-based run() wrapper here because
# the --title and --notes values contain spaces, em-dashes, and newlines
# that don't survive re-quoting on bash 3.2 (macOS default).
if [[ "$DRY_RUN" == "1" ]]; then
  if [[ "$SKIP_DATA_UPLOAD" == "1" ]]; then
    echo "  [dry-run] (cd '$TARGET_DIR' && gh release create v1.0 \\"
    echo "              --title 'v1.0 — Initial public release' \\"
    echo "              --notes '<see RELEASE_NOTES in script>')"
  else
    echo "  [dry-run] (cd '$TARGET_DIR' && gh release create v1.0 \\"
    echo "              --title 'v1.0 — Initial public release' \\"
    echo "              --notes '<see RELEASE_NOTES in script>' \\"
    echo "              '$CSV_PATH')"
  fi
else
  if [[ "$SKIP_DATA_UPLOAD" == "1" ]]; then
    ( cd "$TARGET_DIR" && gh release create v1.0 \
        --title "v1.0 — Initial public release" \
        --notes "$RELEASE_NOTES" )
  else
    ( cd "$TARGET_DIR" && gh release create v1.0 \
        --title "v1.0 — Initial public release" \
        --notes "$RELEASE_NOTES" \
        "$CSV_PATH" )
  fi
fi

# ------------------------- Done -----------------------------------------
step "Done"
echo "  Repo:    https://github.com/${REPO_OWNER}/${REPO_NAME}"
echo "  Release: https://github.com/${REPO_OWNER}/${REPO_NAME}/releases/tag/v1.0"
echo
echo "Next:"
echo "  • Visit the repo, check that README + METHODOLOGY render correctly."
echo "  • Add 'candidates' 'elections' 'tamil-nadu' 'open-data' as topics (repo Settings → Topics)."
echo "  • Wait ~15 minutes before linking from Reddit — new repos occasionally"
echo "    get flagged by GitHub's fresh-account heuristics if traffic spikes too fast."
