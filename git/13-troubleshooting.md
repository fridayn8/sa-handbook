# 13 — Troubleshooting: "Oops" Recipes

> **Step 0, always:** `git status` — it usually tells you what is going on and what to type next.
> **Step 1 if something "disappeared":** `git reflog` — almost nothing is truly lost.

## Commits in the wrong place

### I committed to `main` instead of a feature branch (not pushed)

```bash
git branch feat/my-work          # save commits under a new branch name
git reset --hard origin/main     # move main back
git switch feat/my-work
```

### I committed to the wrong feature branch

```bash
git switch correct-branch
git cherry-pick <sha>            # copy the commit
git switch wrong-branch
git reset --hard HEAD~1          # remove it there (only if not pushed/shared)
```

### I started working on `main` but haven't committed yet

```bash
git switch -c feat/my-work       # uncommitted changes come with you
```

## Fixing commits

### Wrong commit message (last commit, not pushed)

```bash
git commit --amend -m "fix(dns): correct message"
```

### Forgot a file in the last commit (not pushed)

```bash
git add forgotten.md
git commit --amend --no-edit
```

### Wrong message on an older commit / already pushed on MY branch

```bash
git rebase -i origin/main        # mark the commit with `reword`
git push --force-with-lease      # only on your own branch
```

### I need to undo a commit that is already on `main`

```bash
git switch -c revert/bad-change origin/main
git revert <sha>
git push -u origin revert/bad-change     # then open a PR
```

## Push / pull problems

### `! [rejected] main -> main (fetch first)` or `non-fast-forward`

Someone (or GitHub, e.g. a merged PR) added commits you don't have.

```bash
git pull --rebase
git push
```

### `fatal: The current branch has no upstream branch`

```bash
git push -u origin HEAD
# prevent forever: git config --global push.autoSetupRemote true
```

### `Your branch and 'origin/x' have diverged` after I rebased

Expected after a rebase on an already pushed branch:

```bash
git push --force-with-lease      # your own branch only
```

### `fatal: refusing to merge unrelated histories`

Two repos with independent histories (e.g. GitHub created a README and you `git init`-ed locally).

```bash
git pull origin main --allow-unrelated-histories
```

### `Permission denied (publickey)`

```bash
ssh -T git@github.com            # test SSH auth
ssh-add -l                       # is your key loaded?
git remote -v                    # SSH or HTTPS URL?
```

See [01 — SSH keys](01-setup-and-config.md#ssh-keys-for-github).

### Push blocked by a ruleset / protected branch

You tried to push to `main`. Push to a branch and open a PR instead — that is the point. 🙂

## Merge & rebase problems

### Merge conflict — help

```bash
git status                      # which files conflict
# edit files: keep the right content, delete <<<<<<< ======= >>>>>>> lines
git add <file>
git merge --continue            # or: git rebase --continue
# bail out:
git merge --abort               # or: git rebase --abort
```

### I finished a merge/rebase and the result is wrong

```bash
git reset --hard ORIG_HEAD      # state before the last merge/rebase/reset (if not pushed)
# or find the right point:
git reflog
git reset --hard HEAD@{5}
```

### Stuck in "rebase in progress" / "detached HEAD" after a rebase

```bash
git status                      # shows the current step
git rebase --continue | --skip | --abort
```

## Lost work

### I ran `git reset --hard` and lost commits

```bash
git reflog
git reset --hard <sha-before-reset>
```

### I deleted a branch that wasn't merged

```bash
git reflog | grep "feat/my-branch"     # or look for its last commit message
git switch -c feat/my-branch <sha>
```

### I lost a stash

```bash
git fsck --no-reflogs | grep "dangling commit"
git show <sha>                          # find the right one
git stash apply <sha>
```

### I ran `git restore .` / `git clean -fd` on uncommitted work

Those changes were never in Git — Git cannot recover them. Check your editor's local
history (VS Code: *Timeline* view; JetBrains: *Local History*). **Lesson:** commit early
(WIP commits on your branch are fine) and always `git clean -n` first.

## Detached HEAD

`You are in 'detached HEAD' state` — you checked out a commit/tag, not a branch.

```bash
git switch -                     # go back to where you were
git switch -c feat/from-here     # or keep any commits you made here in a new branch
```

## Secrets

### 🔥 I committed a secret (token, password, private key)

1. **Revoke / rotate the secret immediately** in the issuing system (Cloudflare, Tailscale…).
   Assume it is compromised the moment it was pushed — bots scan GitHub within minutes.
2. If **not pushed**: `git reset --soft HEAD~1`, remove the secret, recommit.
3. If **pushed**: remove it from all history with `git filter-repo`
   (see [10](10-advanced.md#git-filter-repo-rewriting-whole-history)), force-push, and ask
   collaborators to re-clone. For GitHub-cached views, contact GitHub Support if needed.
4. Prevent it next time: `.gitignore`, SOPS encryption, `gitleaks` pre-commit hook.

### I committed a file that should be ignored (e.g. `.terraform/`, `.env`)

```bash
echo ".env" >> .gitignore
git rm --cached .env                  # stop tracking, keep file locally
git commit -m "chore: stop tracking .env"
# if it contained secrets → see the section above
```

## Line endings / file mode noise

### Every line shows as changed (CRLF vs LF)

```bash
git config --global core.autocrlf input   # Linux/macOS (Windows: true)
# repo-wide fix: add `* text=auto eol=lf` to .gitattributes, then
git add --renormalize .
git commit -m "chore: normalise line endings"
```

### Files show as modified with no content change (permission bits)

```bash
git diff                                   # "old mode 100644 / new mode 100755"
git config core.fileMode false             # ignore mode changes (e.g. on Windows/WSL mounts)
```

## Large files

### `remote: error: File X is 120 MB; this exceeds GitHub's file size limit of 100 MB`

```bash
git reset --soft origin/main     # if the big file is only in unpushed commits
git restore --staged big.iso
echo "*.iso" >> .gitignore
git commit -m "…"
# if it is in older history: git filter-repo --path big.iso --invert-paths
```

## Still stuck?

```bash
git <command> --help             # full manual page
git help -g                      # list concept guides (e.g. git help revisions)
```

Pro Git book: <https://git-scm.com/book/en/v2> · Oh Shit, Git!?!: <https://ohshitgit.com/>
