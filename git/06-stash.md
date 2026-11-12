# 06 — Stash

## git stash

**Purpose:** Temporarily park uncommitted changes so you get a clean working tree,
then bring them back later.
**Risk level:** ✅ safe (but stashes are easy to forget — prefer a WIP commit for long breaks)

Typical use: you are halfway through something and must urgently switch branches.

**Basic**

```bash
git stash                         # stash tracked changes (staged + unstaged)
git stash push -m "wip: vlan rules"   # with a description (recommended)
git stash list                    # stash@{0}: On feat/vlan: wip: vlan rules
git stash pop                     # re-apply latest stash and remove it
git stash apply                   # re-apply latest stash, keep it in the list
git stash drop stash@{1}          # delete one stash
```

**Advanced**

```bash
git stash -u                      # include untracked files
git stash -a                      # include untracked + ignored files
git stash push -p                 # interactively choose hunks
git stash push -- path/file.tf    # stash only specific paths
git stash --staged                # stash only what is staged (Git ≥ 2.35)
git stash show -p stash@{0}       # see the diff inside a stash
git stash branch feat/new stash@{0}   # create branch from where stash was made + apply it
git stash clear                   # ⚠️ delete ALL stashes
```

**Example scenario — urgent fix while mid-feature**

```bash
git stash push -u -m "wip: tailscale ACL draft"
git switch main && git pull
git switch -c fix/cloudflare-dns
# ...fix, commit, push, PR...
git switch feat/tailscale-acl
git stash pop
```

**Conflict on pop:** resolve like a merge conflict, `git add` the files, then
`git stash drop` (pop does not drop the stash when it conflicts).

**Recover a dropped stash:**

```bash
git fsck --no-reflogs | grep "dangling commit"   # candidates
git show <sha>                                   # inspect
git stash apply <sha>
```

**Alternative to stash — WIP commit:**

```bash
git commit -am "wip"          # on your feature branch
# later
git reset --soft HEAD~1       # turn it back into uncommitted changes
```
