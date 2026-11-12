# 08 — Inspecting History

## git log (advanced)

**Purpose:** Explore and filter commit history.
**Risk level:** ✅ safe

**Formatting**

```bash
git log --oneline --graph --decorate --all
git log --stat                     # files changed per commit
git log -p                         # full diff per commit
git log --format="%h %an %ar %s"   # custom: hash, author, relative date, subject
git log --pretty=fuller            # author AND committer
```

Useful `--format` placeholders: `%h` short hash, `%H` full hash, `%an` author name,
`%ae` author email, `%ad` author date, `%ar` relative date, `%s` subject, `%d` refs.

**Filtering**

```bash
git log --author="Alice"
git log --since="2 weeks ago" --until="yesterday"
git log --grep="opnsense" -i          # commit message contains (case-insensitive)
git log -S "allowed_vlans"            # "pickaxe": commits that added/removed this string
git log -G "vlan_id\s*=\s*30"         # commits whose diff matches a regex
git log -- terraform/modules/vm/      # commits touching a path
git log --follow -- docs/hld.md          # follow a file across renames
git log --no-merges                   # hide merge commits
git log --first-parent main           # only the main-line history (one entry per merged PR)
```

**Comparing branches**

```bash
git log main..feat/vlan          # commits in feat/vlan not in main (what the PR adds)
git log feat/vlan..main          # commits in main that feat/vlan lacks (need rebase?)
git log --left-right --oneline main...feat/vlan   # < = only main, > = only feat
git log -L 10,30:ansible/site.yml     # history of lines 10–30 of a file
git log -L :resource_name:main.tf     # history of a function/block (language support varies)
```

## git show

**Purpose:** Show one object — usually a commit with its diff.

```bash
git show                         # last commit
git show 9f8e7d6                 # specific commit
git show 9f8e7d6 --stat          # only file summary
git show v1.0.0                  # tag + commit it points to
git show main:docs/hld.md        # file content at a given ref (without checking out)
git show HEAD~2:README.md > /tmp/old-readme.md
```

## git blame

**Purpose:** For each line of a file, show which commit and author last changed it.

```bash
git blame docs/lld-network.md
git blame -L 40,60 terraform/main.tf     # only lines 40–60
git blame -w -C -C -C file               # ignore whitespace, detect moved/copied lines
git blame <sha>^ -- file                 # blame as of before a commit (dig further back)
```

**Ignore formatting-only commits** (e.g. a mass reformat):

```bash
echo "<sha-of-reformat-commit>" >> .git-blame-ignore-revs
git config blame.ignoreRevsFile .git-blame-ignore-revs   # GitHub also honours this file
```

Blame is for understanding *why* code exists (then read the commit/PR), not for blaming people.

## git bisect

**Purpose:** Binary-search the history to find the commit that introduced a bug.
**Risk level:** ✅ safe (checks out commits temporarily)

With 1 000 commits, bisect needs only ~10 tests.

**Manual**

```bash
git bisect start
git bisect bad                    # current commit is broken
git bisect good v1.2.0            # this old version worked
# Git checks out a middle commit → test it, then:
git bisect good                   # or: git bisect bad
# ...repeat until Git prints "<sha> is the first bad commit"
git bisect reset                  # return to where you started
```

**Automated** — a script returning exit code 0 = good, 1–127 (except 125) = bad, 125 = skip:

```bash
git bisect start HEAD v1.2.0
git bisect run terraform validate
git bisect reset
```

## git shortlog

**Purpose:** Summarise commits by author — handy for release notes and contribution stats.

```bash
git shortlog -sn                  # commit count per author
git shortlog -sn --since="1 month ago"
git shortlog v1.0.0..v1.1.0       # who did what between releases
```

## git grep

**Purpose:** Fast search through tracked files (and any revision).

```bash
git grep "cloudflare_record"
git grep -n -i "todo"                       # with line numbers, case-insensitive
git grep "vlan_id" v1.0.0                   # search in a tag
git grep -e "api_token" -- '*.tf' '*.yml'   # only certain file types
```

## Other useful inspection commands

```bash
git describe --tags               # nearest tag, e.g. v1.2.0-5-g9f8e7d6 (5 commits after v1.2.0)
git rev-parse HEAD                # full SHA of HEAD
git rev-parse --abbrev-ref HEAD   # current branch name (great in scripts)
git rev-list --count HEAD         # number of commits
git merge-base main feat/vlan     # common ancestor commit
git ls-files                      # all tracked files
git cat-file -p HEAD              # raw commit object (tree, parents, author…)
git count-objects -vH             # repository size
```
