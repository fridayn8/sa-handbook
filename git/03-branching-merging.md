# 03 — Branching and Merging

## git branch

**Purpose:** List, create, rename and delete branches.
**Risk level:** ✅ safe (`-D` ⚠️)

**Basic**

```bash
git branch                       # list local branches (* = current)
git branch -a                    # local + remote-tracking
git branch -vv                   # with last commit, upstream and ahead/behind
git branch feat/vlan             # create (does not switch)
git branch -d feat/vlan          # delete — only if merged
```

**Advanced**

```bash
git branch -D feat/abandoned            # ⚠️ force delete, even if unmerged
git branch -m old-name new-name         # rename
git branch -m new-name                  # rename current branch
git branch --merged main                # branches already merged into main (safe to delete)
git branch --no-merged main             # branches with unmerged work
git branch --sort=-committerdate        # most recently used first
git branch -u origin/feat/vlan          # set upstream for current branch
git branch feat/hotfix <sha>            # create a branch at a specific commit
```

## git switch (modern) / git checkout (classic)

**Purpose:** Change the current branch. `switch` (Git ≥ 2.23) does only this, clearly.
`checkout` is older and does many things (switch branches *and* restore files).
**Risk level:** ✅ safe — Git refuses to switch if it would overwrite uncommitted changes.

| Task | Modern | Classic |
|------|--------|---------|
| Go to branch | `git switch main` | `git checkout main` |
| Create + go | `git switch -c feat/x` | `git checkout -b feat/x` |
| Previous branch | `git switch -` | `git checkout -` |
| Track remote branch | `git switch feat/x` (auto if `origin/feat/x` exists) | `git checkout --track origin/feat/x` |
| Detached at tag | `git switch --detach v1.0.0` | `git checkout v1.0.0` |

**Advanced**

```bash
git switch -c fix/dns origin/main     # new branch starting from remote main
git switch -C feat/x                  # ⚠️ create or reset existing branch to HEAD
git switch --discard-changes main     # ⚠️ switch and throw away local changes
```

### Branch naming convention (recommended)

```text
<type>/<short-kebab-description>

feat/proxmox-vm-module
fix/opnsense-dns-rule
docs/remote-access-decision
chore/update-pre-commit
```

## git merge

**Purpose:** Integrate another branch's commits into the current branch.
**Risk level:** ✅ safe (can be undone before push)

**Merge types**

```text
Fast-forward (no divergence — label just moves):
  main: A---B            feat: A---B---C---D      →   main: A---B---C---D

Three-way merge (both sides have new commits — creates merge commit M):
  main: A---B---E                                 →   A---B---E---M
              \                                             \     /
  feat:        C---D                                         C---D

Squash (all feature changes become ONE new commit S, no link to feat):
                                                  →   A---B---E---S
```

**Basic**

```bash
git switch main
git merge feat/vlan
```

**Advanced**

```bash
git merge --ff-only origin/main    # only fast-forward, fail otherwise (safe update)
git merge --no-ff feat/vlan        # always create a merge commit (preserves branch shape)
git merge --squash feat/vlan       # stage all changes as one; you then `git commit`
git merge --abort                  # cancel a merge with conflicts
git merge -X theirs feat/x         # on conflicts prefer their side (use carefully)
```

On GitHub you choose the type in the PR: **Create a merge commit**, **Squash and merge**,
or **Rebase and merge**. The handbook recommends **Squash and merge** (and `sa-handbook` itself uses it).

## Merge conflicts

**What happens:** both branches changed the same lines; Git cannot choose automatically.

```text
<<<<<<< HEAD
allowed_vlans = [10, 20]
=======
allowed_vlans = [10, 30]
>>>>>>> feat/iot-vlan
```

- Between `<<<<<<<` and `=======`: your current branch (HEAD).
- Between `=======` and `>>>>>>>`: the branch being merged.

**Resolution steps**

```bash
git status                       # lists "both modified" files
# 1. edit each file: keep the correct content, delete ALL marker lines
#    e.g. allowed_vlans = [10, 20, 30]
git add <file>                   # 2. mark resolved
git merge --continue             # 3. finish (or: git commit)
# or give up:
git merge --abort
```

**Helpful extras**

```bash
git diff                                 # during conflict: shows combined diff
git checkout --ours   <file>             # take current branch version entirely
git checkout --theirs <file>             # take incoming branch version entirely
git mergetool                            # open configured visual merge tool
git config --global merge.conflictstyle zdiff3   # also show the common ancestor (clearer)
```

**Tips to avoid conflicts:** keep branches short-lived, pull/rebase on `main` often, keep
PRs small, and don't reformat whole files in feature PRs.
