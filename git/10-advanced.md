# 10 — Advanced Features

## git worktree

**Purpose:** Check out **several branches at the same time** in different folders, sharing one `.git`.
**Risk level:** ✅ safe

Great for: reviewing a PR while keeping your own work open, or running a long `terraform plan`
on one branch while editing another — no stashing needed.

```bash
git worktree add ../repo-review feat/teammate-pr     # existing branch
git worktree add -b fix/urgent ../repo-hotfix main   # new branch from main
git worktree list
git worktree remove ../repo-review
git worktree prune                                   # clean up stale entries
```

A branch can be checked out in only one worktree at a time.

## git submodule

**Purpose:** Embed another Git repository inside yours at a **pinned commit**.
**Risk level:** ⚠️ easy to get wrong — consider alternatives first

```bash
git submodule add https://github.com/<owner>/terraform-modules.git vendor/modules
git clone --recurse-submodules <url>        # clone including submodules
git submodule update --init --recursive     # after a normal clone
git submodule update --remote               # move submodules to latest upstream commit
git submodule status
```

**Alternatives:** Terraform module sources with a version (`source = "git::https://…?ref=v1.2.0"`),
Ansible Galaxy requirements, or package managers. They are usually simpler than submodules.

## git sparse-checkout

**Purpose:** Check out only part of a big repository (monorepos).

```bash
git clone --filter=blob:none --no-checkout <url> repo && cd repo
git sparse-checkout set --cone terraform/ docs/
git checkout main
git sparse-checkout list
git sparse-checkout disable          # back to full checkout
```

## Git hooks

**Purpose:** Scripts that Git runs automatically on events.
**Location:** `.git/hooks/` (not versioned) — so teams use a **hook manager** like `pre-commit`
whose config *is* versioned ([`.pre-commit-config.yaml`](../.pre-commit-config.yaml)).

| Hook | Runs | Typical use |
|------|------|-------------|
| `pre-commit` | Before a commit is created | Lint, format, secret scan |
| `commit-msg` | After message is written | Enforce Conventional Commits |
| `pre-push` | Before push | Run tests |
| `post-merge` / `post-checkout` | After merge / checkout | Reinstall dependencies |

A hook exiting non-zero aborts the action. Bypass (⚠️ only when you know why): `--no-verify`.

**Minimal hand-written hook example:**

```bash
cat > .git/hooks/pre-push <<'EOF'
#!/usr/bin/env bash
branch=$(git rev-parse --abbrev-ref HEAD)
if [ "$branch" = "main" ]; then
  echo "❌ Direct push to main is not allowed. Open a PR."; exit 1
fi
EOF
chmod +x .git/hooks/pre-push
```

**Using pre-commit (example: this handbook's config):**

```bash
pre-commit install                          # pre-commit hook
pre-commit install --hook-type commit-msg   # commit message hook
pre-commit run --all-files
pre-commit run gitleaks --all-files         # one hook only
SKIP=markdownlint git commit -m "…"     # skip a specific hook once
```

Server-side enforcement on GitHub is done with **rulesets** and **required status checks** —
local hooks can be bypassed, so CI must repeat the important checks.

## .gitattributes

**Purpose:** Per-path settings: line endings, diff behaviour, merge strategy, LFS.

```gitattributes
# Normalise line endings in the repo
* text=auto eol=lf
*.sh  text eol=lf
*.ps1 text eol=crlf
*.png binary
*.pdf binary
# Custom diff driver for encrypted files (e.g. SOPS)
*.sops.yaml diff=sopsdiffer
docs/**/*.md linguist-documentation
```

> Comments in `.gitattributes` must be on their own line — a trailing `# …` would be
> parsed as attribute names.

## Git LFS (Large File Storage)

**Purpose:** Store large binaries (ISOs, images, videos) outside normal Git history; the repo
keeps small pointer files.

```bash
git lfs install
git lfs track "*.iso" "*.qcow2"     # writes rules to .gitattributes
git add .gitattributes
git lfs ls-files
```

Rule of thumb: **don't commit VM images or ISOs at all** — build or download them with code (for example, OpenTofu can download an official cloud image).

## git filter-repo (rewriting whole history)

**Purpose:** Remove files or text from **all** history (e.g. a leaked secret, a huge file).
**Risk level:** 🔥🔥 rewrites every commit; every clone must be re-cloned

Install: `pip install git-filter-repo` (replacement for the deprecated `git filter-branch`).

```bash
# Work on a fresh mirror clone
git clone --mirror git@github.com:<owner>/<repo>.git && cd <repo>.git

git filter-repo --path secrets.env --invert-paths        # delete a file from all history
git filter-repo --replace-text ../replacements.txt       # replace strings, e.g.:
#   replacements.txt:  my-real-token==>REMOVED

git push --force --mirror
```

⚠️ **A leaked secret must be considered compromised: rotate/revoke it FIRST.** Rewriting history
doesn't remove copies in forks, clones, caches or CI logs. See [13](13-troubleshooting.md).

## Other power tools

```bash
git rerere                      # "reuse recorded resolution" — enable with rerere.enabled=true
git notes add -m "Deployed to lab on 2026-11-11" <sha>   # attach notes without changing the commit
git archive --format=zip -o release.zip v1.0.0            # export a snapshot without .git
git bundle create repo.bundle --all                       # whole repo in one file (offline transfer)
git maintenance start           # background optimisation for large repos
git gc                          # garbage-collect unreachable objects
```
