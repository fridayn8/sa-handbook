# 04 — Remotes and Collaboration

## git remote

**Purpose:** Manage connections to other copies of the repository.
**Risk level:** ✅ safe

**Basic**

```bash
git remote -v                                   # list remotes with URLs
git remote add origin git@github.com:<owner>/<repo>.git
```

**Advanced**

```bash
git remote set-url origin git@github.com:<owner>/<new-repo>.git   # change URL
git remote rename origin github
git remote remove old-remote
git remote show origin           # details: branches, tracking, stale refs
git remote prune origin          # delete local refs to branches gone from remote
```

## git fetch

**Purpose:** Download new commits/branches/tags from a remote **without changing your branches**.
**Risk level:** ✅ always safe

```bash
git fetch                    # from origin
git fetch --all --prune      # all remotes, remove deleted branches
git fetch origin main        # one branch
git fetch --tags
```

After fetching, inspect before integrating:

```bash
git log --oneline HEAD..origin/main     # commits on remote I don't have
git log --oneline origin/main..HEAD     # my commits not on remote
git diff HEAD...origin/main             # what changed upstream
```

## git pull

**Purpose:** `fetch` + integrate the upstream branch into the current branch.
**Risk level:** ✅ mostly safe (may produce conflicts)

**Basic**

```bash
git pull                     # uses config pull.rebase (recommended: true)
```

**Advanced**

```bash
git pull --rebase            # replay my local commits on top of upstream (linear history)
git pull --ff-only           # only update if it is a fast-forward; fail otherwise (safest)
git pull --no-rebase         # merge instead (creates "Merge branch 'main' of …" commits)
git pull origin main         # pull a specific branch into the current one
```

**Merge vs rebase on pull**

| `pull --no-rebase` (merge) | `pull --rebase` |
|----------------------------|-----------------|
| Creates merge commits like *"Merge branch 'main' of github.com:…"* | Linear history |
| Never rewrites your commits | Rewrites your **local, unpushed** commits (fine) |

## git push

**Purpose:** Upload your local commits to a remote branch.
**Risk level:** ✅ normal push · 🔥 force push

**Basic**

```bash
git push -u origin feat/vlan     # first push: create remote branch + set upstream
git push                         # afterwards
```

**Advanced**

```bash
git push --force-with-lease      # 🔥 overwrite remote branch, but only if nobody else pushed
                                 #    since your last fetch. Use after rebasing YOUR OWN branch.
git push --force                 # 🔥🔥 overwrite unconditionally — avoid
git push origin --delete feat/vlan        # delete remote branch
git push origin v1.0.0                    # push one tag
git push --follow-tags                    # push commits + their annotated tags
git push origin HEAD                      # push current branch to same name
git push --dry-run
```

**Why `--force-with-lease` instead of `--force`?** `--force` silently destroys commits a
teammate pushed in the meantime. `--force-with-lease` refuses if the remote moved.

**Rejected push** (`! [rejected] … (fetch first)` / `non-fast-forward`): the remote has
commits you don't have. Fix with `git pull --rebase` then `git push`. See [13](13-troubleshooting.md).

## Upstream tracking

```bash
git push -u origin feat/x            # set upstream while pushing
git branch -u origin/feat/x          # set upstream later
git branch -vv                       # show upstream + [ahead 2, behind 1]
git status -sb                       # "## feat/x...origin/feat/x [ahead 2]"
```

## Forks (contributing to someone else's project)

```text
upstream (original repo)  ──fork──▶  origin (your copy on GitHub)  ──clone──▶  local
```

```bash
git clone git@github.com:<you>/<project>.git
cd <project>
git remote add upstream https://github.com/<original-owner>/<project>.git

# keep your fork up to date
git fetch upstream
git switch main
git merge --ff-only upstream/main
git push origin main

# contribute
git switch -c fix/typo
# ...commit...
git push -u origin fix/typo
gh pr create --repo <original-owner>/<project>
```

Shortcut: `gh repo fork <owner>/<repo> --clone` sets up both remotes for you.
