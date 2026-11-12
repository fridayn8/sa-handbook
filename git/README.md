# Git Reference

Your personal Git handbook: **what each command does, basic and advanced usage, examples,
and recipes for when things go wrong.**

> 🆘 **Something broke?** Go straight to [13 — Troubleshooting](13-troubleshooting.md).
> ⚡ **Just need a command?** Open the [Cheatsheet](cheatsheet.md).

## How to read this guide

Every command is documented in the same format:

| Section | Content |
|---------|---------|
| **Purpose** | What the command is for, in one sentence |
| **Risk level** | ✅ safe · ⚠️ can lose local work · 🔥 rewrites shared history |
| **Basic** | The forms you will use every day |
| **Advanced** | Useful flags and less common forms |
| **Example scenario** | A realistic situation and the exact commands |
| **See also** | Related commands |

In examples, `<placeholder>` means "replace with your value", and `#` starts a comment.

## Contents

| # | File | Topics |
|---|------|--------|
| — | [cheatsheet.md](cheatsheet.md) | One-page summary of the most used commands |
| 00 | [00-concepts.md](00-concepts.md) | Mental model: working tree, staging area, commits, branches, HEAD, remotes |
| 01 | [01-setup-and-config.md](01-setup-and-config.md) | `git config`, identity, aliases, SSH keys, commit signing |
| 02 | [02-basics.md](02-basics.md) | `init`, `clone`, `status`, `add`, `commit`, `diff`, `log`, `rm`, `mv`, `.gitignore` |
| 03 | [03-branching-merging.md](03-branching-merging.md) | `branch`, `switch`, `checkout`, `merge`, merge conflicts |
| 04 | [04-remote-collaboration.md](04-remote-collaboration.md) | `remote`, `fetch`, `pull`, `push`, upstream, forks |
| 05 | [05-undo-and-recovery.md](05-undo-and-recovery.md) | `restore`, `reset`, `revert`, `commit --amend`, `reflog`, `clean` |
| 06 | [06-stash.md](06-stash.md) | `stash` push / pop / apply / list / branch |
| 07 | [07-rebase-and-history.md](07-rebase-and-history.md) | `rebase`, interactive rebase, `cherry-pick`, autosquash |
| 08 | [08-inspecting-history.md](08-inspecting-history.md) | Advanced `log`, `show`, `blame`, `bisect`, `shortlog`, `grep` |
| 09 | [09-tags-and-releases.md](09-tags-and-releases.md) | `tag`, SemVer, GitHub releases, release-please |
| 10 | [10-advanced.md](10-advanced.md) | `worktree`, `submodule`, `sparse-checkout`, hooks, LFS, `.gitattributes`, `filter-repo` |
| 11 | [11-github-workflow.md](11-github-workflow.md) | GitHub Flow, Conventional Commits, PRs, reviews, rulesets, CODEOWNERS |
| 12 | [12-github-cli.md](12-github-cli.md) | `gh` for issues, PRs, Actions, releases |
| 13 | [13-troubleshooting.md](13-troubleshooting.md) | "Oops" recipes: problem → solution |
| 14 | [14-branching-strategies-and-environments.md](14-branching-strategies-and-environments.md) | `main` vs `master`, branch types, GitHub Flow / GitFlow / GitLab Flow / trunk-based, environments (DEV → PROD), deployment strategies, release & change management, scenarios |

## "I want to…" lookup

| I want to… | Command | Details |
|------------|---------|---------|
| See what changed | `git status`, `git diff` | [02](02-basics.md) |
| Save my work | `git add <file>` → `git commit -m "…"` | [02](02-basics.md) |
| Start new work | `git switch -c feat/<name>` | [03](03-branching-merging.md) |
| Get latest changes | `git pull` | [04](04-remote-collaboration.md) |
| Share my branch | `git push -u origin <branch>` | [04](04-remote-collaboration.md) |
| Discard changes in a file | `git restore <file>` | [05](05-undo-and-recovery.md) |
| Unstage a file | `git restore --staged <file>` | [05](05-undo-and-recovery.md) |
| Fix my last commit message | `git commit --amend` | [05](05-undo-and-recovery.md) |
| Undo a commit that is already pushed | `git revert <sha>` | [05](05-undo-and-recovery.md) |
| Undo a local commit, keep changes | `git reset --soft HEAD~1` | [05](05-undo-and-recovery.md) |
| Recover "lost" commits | `git reflog` | [05](05-undo-and-recovery.md) |
| Park unfinished work | `git stash` | [06](06-stash.md) |
| Clean up commits before a PR | `git rebase -i origin/main` | [07](07-rebase-and-history.md) |
| Copy one commit to another branch | `git cherry-pick <sha>` | [07](07-rebase-and-history.md) |
| Find who changed a line | `git blame <file>` | [08](08-inspecting-history.md) |
| Find which commit introduced a bug | `git bisect` | [08](08-inspecting-history.md) |
| Mark a release | `git tag -a v1.0.0 -m "…"` | [09](09-tags-and-releases.md) |
| Work on two branches at once | `git worktree add` | [10](10-advanced.md) |
| Choose a branching strategy / understand DEV, UAT, PROD | GitHub Flow, GitFlow, environments | [14](14-branching-strategies-and-environments.md) |
| Ship an urgent production fix | `hotfix/*` branch + emergency change | [14](14-branching-strategies-and-environments.md#c-production-hotfix-incident) |
| Remove a leaked secret from history | `git filter-repo` + **rotate the secret** | [13](13-troubleshooting.md) |
