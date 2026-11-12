# 02 — Basics

## git init

**Purpose:** Create a new, empty repository in the current folder.
**Risk level:** ✅ safe

```bash
git init                     # in current folder
git init my-project          # creates folder my-project/
git init -b main             # explicit initial branch name
```

## git clone

**Purpose:** Copy an existing repository (all history) to your machine.
**Risk level:** ✅ safe

**Basic**

```bash
git clone git@github.com:<owner>/<repo>.git
git clone https://github.com/<owner>/<repo>.git my-folder
```

**Advanced**

```bash
git clone --depth 1 <url>                 # shallow: only latest commit (fast, for CI)
git clone --branch v1.0.0 --depth 1 <url> # one tag/branch only
git clone --filter=blob:none <url>        # partial clone: download file contents on demand
git clone --recurse-submodules <url>      # also clone submodules
```

## git status

**Purpose:** Show which files are modified, staged or untracked, and the branch state.
**Risk level:** ✅ safe — run it constantly.

```bash
git status
git status -sb          # short format + branch info
```

Short format codes: `M` modified, `A` added, `D` deleted, `R` renamed, `??` untracked.
Left column = staged, right column = unstaged (e.g. `MM` = staged *and* further modified).

## git add

**Purpose:** Put changes into the staging area (prepare the next commit).
**Risk level:** ✅ safe

**Basic**

```bash
git add README.md            # one file
git add docs/                # a folder
git add .                    # everything in current folder (check `git status` first!)
```

**Advanced**

```bash
git add -p                   # interactive: choose hunks (y/n/s=split/e=edit/q)
git add -u                   # only already-tracked files (no new files)
git add -N new-file.md       # "intent to add": makes new file visible to `git diff`
git add --dry-run .          # show what would be added
```

**Example scenario**
> You fixed a firewall rule *and* a typo in the same file, but want two commits:

```bash
git add -p ansible/roles/opnsense/tasks/rules.yml   # pick only the rule hunk
git commit -m "fix(opnsense): allow NTP from server VLAN"
git add ansible/roles/opnsense/tasks/rules.yml      # the rest (typo)
git commit -m "docs(opnsense): fix typo in task name"
```

## git commit

**Purpose:** Save the staged snapshot permanently in history.
**Risk level:** ✅ safe

**Basic**

```bash
git commit -m "feat(proxmox): add VM template module"
git commit                   # opens editor for a longer message
```

**Good commit message structure**

```text
fix(opnsense): allow DNS from IoT VLAN to Unbound          ← subject ≤ 72 chars, imperative

IoT devices failed to resolve names because the default     ← body: WHY, not how
deny rule blocked UDP/53 to the firewall interface.

Closes #42                                                  ← footer: issue links, BREAKING CHANGE
```

**Advanced**

```bash
git commit -a -m "…"                  # stage all tracked modified files + commit (skips new files)
git commit --amend                    # replace last commit (see 05)
git commit --fixup <sha>              # mark as fix for an older commit (see 07 autosquash)
git commit --allow-empty -m "…"       # commit with no changes (rarely needed)
git commit -S -m "…"                  # sign this commit
git commit --no-verify -m "…"         # ⚠️ skip pre-commit hooks — avoid
git commit -m "subject" -m "body paragraph"   # multiple -m = multiple paragraphs
```

## git diff

**Purpose:** Show line-by-line changes.
**Risk level:** ✅ safe

| Command | Compares |
|---------|----------|
| `git diff` | Working tree ↔ staging area (unstaged changes) |
| `git diff --staged` (= `--cached`) | Staging area ↔ last commit (what you will commit) |
| `git diff HEAD` | Working tree ↔ last commit (all changes) |
| `git diff main..feat/x` | Tip of `main` ↔ tip of `feat/x` |
| `git diff main...feat/x` | Changes on `feat/x` since it branched from `main` (what a PR shows) |
| `git diff <sha1> <sha2> -- <path>` | Two commits, limited to a path |

**Advanced**

```bash
git diff --stat                 # summary: files and number of lines changed
git diff --name-only main...    # just file names changed on this branch
git diff --word-diff            # changes within lines (great for prose / Markdown)
git diff -w                     # ignore whitespace
```

## git log (basics)

**Purpose:** Show commit history. More in [08](08-inspecting-history.md).

```bash
git log
git log --oneline
git log --oneline --graph --all --decorate
git log -5                      # last 5 commits
git log -- docs/                # only commits touching a path
```

## git rm / git mv

**Purpose:** Delete or rename files *and* stage that change.

```bash
git rm old-file.md                  # delete from disk and stage deletion
git rm --cached secrets.env         # stop tracking but keep on disk (then add to .gitignore!)
git rm -r --cached .terraform/      # stop tracking a folder
git mv draft.md docs/hld.md         # rename/move
```

## .gitignore

**Purpose:** Tell Git which untracked files to ignore.

| Pattern | Matches |
|---------|---------|
| `*.log` | Any `.log` file, anywhere |
| `/build` | `build` only at repo root |
| `build/` | Any directory named `build` |
| `**/.terraform/*` | Contents of any `.terraform` dir at any depth |
| `!keep.log` | Exception — do **not** ignore this |
| `#` | Comment |

```bash
git check-ignore -v path/to/file    # which rule ignores this file?
git status --ignored                # list ignored files
```

⚠️ `.gitignore` does not affect files that are **already tracked**. Use `git rm --cached` first.

Templates: <https://github.com/github/gitignore>. Example: this handbook's own [`.gitignore`](../.gitignore).
