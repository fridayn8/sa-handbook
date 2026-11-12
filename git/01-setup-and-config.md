# 01 — Setup and Configuration

## git config

**Purpose:** Read and write Git settings.
**Risk level:** ✅ safe

Settings live at three levels; the more specific one wins:

| Level | Flag | File | Scope |
|-------|------|------|-------|
| System | `--system` | `/etc/gitconfig` | All users on the machine |
| Global | `--global` | `~/.gitconfig` | Your user |
| Local | `--local` (default) | `.git/config` | This repository only |

**Basic**

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"     # VS Code as editor (or: nano, vim)

git config --list --show-origin                   # all settings + which file they come from
git config user.email                             # read one value
```

**Recommended defaults**

```bash
git config --global pull.rebase true          # git pull rebases instead of creating merge commits
git config --global fetch.prune true          # remove remote-tracking branches deleted on remote
git config --global push.autoSetupRemote true # first `git push` sets upstream automatically
git config --global rebase.autoStash true     # stash/unstash automatically around a rebase
git config --global rebase.autoSquash true    # honour fixup!/squash! commits in rebase -i
git config --global rerere.enabled true       # remember how you resolved conflicts
git config --global diff.colorMoved zebra     # highlight moved lines in diffs
git config --global core.autocrlf input       # Linux/macOS; on Windows use: true
git config --global help.autocorrect prompt   # suggest fixes for typos like `git stauts`
```

**Advanced — per-directory identity (e.g. work vs personal)**

```ini
# ~/.gitconfig
[includeIf "gitdir:~/work/"]
    path = ~/.gitconfig-work
```

```ini
# ~/.gitconfig-work
[user]
    email = you@company.example
```

**Example scenario**
> You committed with the wrong email in this repo only:

```bash
git config user.email "personal@example.com"     # fix for this repo
git commit --amend --reset-author --no-edit      # fix the last commit (if not pushed)
```

## Aliases

**Purpose:** Short names for long commands.

```bash
git config --global alias.st  "status -sb"
git config --global alias.co  "checkout"
git config --global alias.sw  "switch"
git config --global alias.lg  "log --oneline --graph --decorate --all"
git config --global alias.last "log -1 HEAD --stat"
git config --global alias.unstage "restore --staged"
git config --global alias.amend "commit --amend --no-edit"
git config --global alias.undo "reset --soft HEAD~1"
git config --global alias.branches "branch -vv --sort=-committerdate"
```

Usage: `git lg`, `git undo`. Aliases starting with `!` run shell commands:

```bash
git config --global alias.cleanup '!git branch --merged main | grep -v "^\*\|main" | xargs -r git branch -d'
```

## SSH keys for GitHub

**Purpose:** Authenticate to GitHub without typing a password/token.

```bash
ssh-keygen -t ed25519 -C "you@example.com"     # creates ~/.ssh/id_ed25519 (+ .pub)
eval "$(ssh-agent -s)" && ssh-add ~/.ssh/id_ed25519
cat ~/.ssh/id_ed25519.pub                       # copy → GitHub → Settings → SSH and GPG keys
ssh -T git@github.com                           # test: "Hi <user>! You've successfully authenticated"
```

Clone with SSH URLs: `git clone git@github.com:<owner>/<repo>.git`.
Switch an existing repo from HTTPS to SSH:

```bash
git remote set-url origin git@github.com:<owner>/<repo>.git
```

Alternative: HTTPS + the GitHub CLI credential helper — `gh auth login` then `gh auth setup-git`.

## Commit signing (Verified badge)

**Purpose:** Prove commits really come from you. Many companies require it.

**Advanced — sign with your SSH key (simplest)**

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
git config --global tag.gpgsign true
# Add the same public key on GitHub as a **Signing key** (Settings → SSH and GPG keys)

git log --show-signature -1     # verify locally
```

## Useful global ignore

```bash
git config --global core.excludesfile ~/.gitignore_global
printf ".DS_Store\nThumbs.db\n.idea/\n*.swp\n" >> ~/.gitignore_global
```

**See also:** [02 — `.gitignore`](02-basics.md#gitignore), [10 — hooks](10-advanced.md#git-hooks)
