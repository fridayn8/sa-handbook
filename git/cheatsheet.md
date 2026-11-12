# Git Cheatsheet

One page, the commands you use 95 % of the time. Details in the numbered chapters.

## Setup (once)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
git config --global fetch.prune true
```

## Daily workflow (GitHub Flow)

```bash
git switch main && git pull                 # 1. start from fresh main
git switch -c feat/short-description        # 2. new branch
# ...edit files...
git status                                  # 3. what changed?
git diff                                    #    see unstaged changes
git add <file>        # or: git add -p      # 4. stage (interactively with -p)
git commit -m "feat(scope): do something"   # 5. commit (Conventional Commits)
git push -u origin feat/short-description   # 6. push & set upstream
gh pr create --fill                         # 7. open a pull request
# after merge on GitHub:
git switch main && git pull                 # 8. update main
git branch -d feat/short-description        # 9. delete local branch
```

## Look around

| Command | What it shows |
|---------|---------------|
| `git status -sb` | Short status + branch / ahead-behind |
| `git diff` | Unstaged changes |
| `git diff --staged` | Staged changes (what will be committed) |
| `git log --oneline --graph --all` | History as a graph |
| `git log -p <file>` | History of a file with diffs |
| `git show <sha>` | One commit in detail |
| `git blame <file>` | Who last changed each line |
| `git branch -vv` | Local branches + upstream + ahead/behind |
| `git remote -v` | Configured remotes |

## Branches

| Command | Action |
|---------|--------|
| `git switch <branch>` | Go to a branch |
| `git switch -c <new>` | Create and go to a new branch |
| `git branch -d <branch>` | Delete a merged branch |
| `git branch -D <branch>` | ⚠️ Force-delete a branch |
| `git merge <branch>` | Merge `<branch>` into current branch |
| `git rebase origin/main` | Replay my commits on top of latest main |
| `git push origin --delete <branch>` | Delete a remote branch |

## Undo (from safest to most dangerous)

| Situation | Command |
|-----------|---------|
| Discard unstaged changes in a file | `git restore <file>` |
| Unstage a file (keep changes) | `git restore --staged <file>` |
| Change last commit (message or content) — **not pushed yet** | `git commit --amend` |
| Undo last commit, keep changes staged | `git reset --soft HEAD~1` |
| Undo last commit, keep changes unstaged | `git reset HEAD~1` |
| Undo a commit that is **already pushed** | `git revert <sha>` |
| ⚠️ Throw away all local changes & commits | `git reset --hard origin/main` |
| ⚠️ Delete untracked files | `git clean -fd` (preview with `-n`) |
| Find anything you "lost" | `git reflog` |

## Stash

```bash
git stash push -m "wip: half-done firewall rules"   # park changes
git stash list                                      # see stashes
git stash pop                                       # re-apply & drop latest
git stash apply stash@{1}                           # re-apply a specific one, keep it
```

## Sync with remote

```bash
git fetch                    # download, don't change my branches
git pull                     # fetch + rebase (with pull.rebase=true)
git push                     # upload current branch
git push --force-with-lease  # ⚠️ safe-ish force push after a rebase (own branch only!)
```

## Tags

```bash
git tag -a v1.2.0 -m "Release 1.2.0"
git push origin v1.2.0
git tag -l "v1.*"
```

## Conventional Commit types

| Type | Use for | SemVer effect |
|------|---------|---------------|
| `feat` | New feature | MINOR |
| `fix` | Bug fix | PATCH |
| `docs` | Documentation only | — |
| `refactor` | Code change, no behaviour change | — |
| `test` | Tests | — |
| `ci` / `build` | Pipelines / build system | — |
| `chore` | Maintenance | — |
| `feat!` or `BREAKING CHANGE:` footer | Breaking change | MAJOR |

Format: `type(optional-scope): short imperative description` — e.g. `fix(opnsense): allow DNS from IoT VLAN`.

## Golden rules

1. **Never rewrite history that others have pulled** (`reset`, `rebase`, `--amend`, force push) — only on your own unmerged branch.
2. **Pull before you branch; branch before you edit.**
3. **Small commits, one logical change each.**
4. **Never commit secrets.** If you do: rotate the secret first, then clean history.
5. **When in doubt: `git status`. When lost: `git reflog`.**
