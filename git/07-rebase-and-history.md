# 07 — Rebase and Rewriting History

> 🔥 **Golden rule:** only rewrite commits that **only you** have (your own unmerged branch).
> Never rebase `main` or a branch others are working on.

## git rebase

**Purpose:** Move ("replay") your commits so they start from a different base commit.
**Risk level:** 🔥 rewrites history (creates new commits) — safe on your own branch

```text
Before:   main:  A---B---C
                  \
          feat:    D---E

git switch feat && git rebase main

After:    main:  A---B---C
                          \
          feat:            D'---E'      (new SHAs)
```

**Basic — update your feature branch with latest main**

```bash
git switch feat/vlan
git fetch origin
git rebase origin/main
# if it was already pushed:
git push --force-with-lease
```

**Conflicts during rebase** (resolved commit by commit):

```bash
# edit files, remove markers
git add <file>
git rebase --continue
git rebase --skip          # drop the current commit
git rebase --abort         # go back to before the rebase
```

> ⚠️ During a rebase, `--ours` means the branch you are rebasing **onto** (e.g. main)
> and `--theirs` means **your** commit being replayed — the opposite of merge.

**Advanced**

```bash
git rebase --onto main feat/base feat/child   # move feat/child (minus feat/base's commits) onto main
git rebase -i HEAD~4                          # interactive: edit last 4 commits (see below)
git rebase --autostash origin/main            # stash/unstash dirty changes automatically
git rebase --exec "make test" origin/main     # run tests after each replayed commit
git rebase --update-refs main                 # also move stacked branches (Git ≥ 2.38)
```

### Merge vs rebase — when to use which

| | Merge | Rebase |
|---|-------|--------|
| History | True, with merge commits | Linear, clean |
| Rewrites commits | No | Yes |
| Safe on shared branches | ✅ | ❌ |
| Typical use | Integrating PRs into `main` | Updating *your* branch before a PR / before merging |

## Interactive rebase (`rebase -i`)

**Purpose:** Clean up your commits before opening/merging a PR — reorder, combine, reword, drop.

```bash
git rebase -i origin/main      # all commits on my branch
git rebase -i HEAD~3           # last 3 commits
```

Your editor opens a todo list (oldest first):

```text
pick 1a2b3c4 feat(vlan): add IoT VLAN
pick 5d6e7f8 wip
pick 9a8b7c6 fix typo
pick 0f1e2d3 feat(vlan): add firewall rules
```

| Command | Effect |
|---------|--------|
| `pick` (p) | Keep commit as is |
| `reword` (r) | Keep changes, edit message |
| `edit` (e) | Stop to amend the commit (split it, change files) |
| `squash` (s) | Merge into previous commit, combine messages |
| `fixup` (f) | Merge into previous commit, discard this message |
| `drop` (d) | Remove commit |
| `exec` (x) | Run a shell command |
| *reorder lines* | Reorder commits |

Example result:

```text
pick   1a2b3c4 feat(vlan): add IoT VLAN
fixup  9a8b7c6 fix typo
fixup  5d6e7f8 wip
pick   0f1e2d3 feat(vlan): add firewall rules
```

### Autosquash (fixup commits)

```bash
git commit --fixup 1a2b3c4             # creates "fixup! feat(vlan): add IoT VLAN"
git rebase -i --autosquash origin/main # automatically places & marks it as fixup
# with rebase.autoSquash=true, plain `git rebase -i` does it
```

### Splitting a commit

```bash
git rebase -i HEAD~3      # mark the commit with `edit`
git reset HEAD~1          # un-commit it, keep changes
git add -p && git commit -m "part 1"
git add -p && git commit -m "part 2"
git rebase --continue
```

## git cherry-pick

**Purpose:** Copy one or more existing commits onto the current branch.
**Risk level:** ✅ safe (adds new commits)

**Basic**

```bash
git switch release/1.x
git cherry-pick 9f8e7d6
```

**Advanced**

```bash
git cherry-pick A..B                 # range (excludes A); use A^..B to include A
git cherry-pick -x <sha>             # append "(cherry picked from commit …)" to message
git cherry-pick -n <sha>             # apply changes without committing
git cherry-pick -m 1 <merge-sha>     # pick a merge commit relative to parent 1
git cherry-pick --continue | --abort | --skip
```

**Example scenario:** a security fix merged to `main` must also go to the `release/1.x` branch:
`git switch release/1.x && git cherry-pick -x <fix-sha> && git push`.

## Why squash-merge on GitHub still matters

With **Squash and merge**, whatever mess your branch contains becomes one clean commit on
`main` — so with this workflow, interactive rebase is mostly for making **reviews** easier, and
the **PR title** must be a good Conventional Commit message.
