# Git Workflow Practice

> **Goal:** set up your tools and run the professional workflow once, end to end:
> **issue → branch → commit → pull request → squash merge → cleanup**.

Do this in a **scratch repository of your own** (create an empty one on GitHub, for example
`git-practice`), not in a repository you care about. Everything you need is explained in the
[Git handbook](../git/README.md).

## 1. Concepts you will use

| Concept | Why it matters for a Solution Architect | Read |
|---------|------------------------------------------|------|
| **Pre-commit hooks** | Automated quality gates *before* work leaves your laptop ("shift left") | [10](../git/10-advanced.md) |
| **GitHub Flow** | Simple, widely used branching model; `main` is always in a good state | [11](../git/11-github-workflow.md) |
| **Conventional Commits** | Machine-readable history, so changelogs and versions can be generated | [11](../git/11-github-workflow.md) |
| **Pull requests** | Where design and code are reviewed; architects spend a lot of time here | [11](../git/11-github-workflow.md) |
| **Squash merge** | One clean commit per PR, so the PR title matters | [03](../git/03-branching-merging.md) |

## 2. Hands-on steps

### 2.1 Install the tools

```bash
# Git (version 2.40 or newer is recommended)
git --version

# pre-commit (Python)
pip install pre-commit

# gitleaks (secret scanner): https://github.com/gitleaks/gitleaks#installing
# GitHub CLI: https://cli.github.com/
gh --version
```

### 2.2 Configure your Git identity and defaults

Details in [01 — Setup and config](../git/01-setup-and-config.md).

```bash
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global pull.rebase true
```

### 2.3 Clone your scratch repository and enable hooks

Copy this handbook's [`.pre-commit-config.yaml`](../.pre-commit-config.yaml) into the scratch
repository (drop the `check-links` hook if you do not copy `scripts/check-links.py`).

```bash
git clone git@github.com:<you>/git-practice.git
cd git-practice
pre-commit install
pre-commit install --hook-type commit-msg
pre-commit run --all-files
```

### 2.4 Configure the repository on GitHub

1. **Settings → General → Pull Requests**: allow *squash merging* only and enable
   *Automatically delete head branches*.
2. **Settings → Rules → Rulesets → New branch ruleset** for `main`: require a pull request and
   block force pushes. On GitHub Free, rulesets are **enforced only on public repositories**; on
   a private repository rely on the local `no-commit-to-branch` hook and discipline.
3. **Issues → Labels**: create `docs`, `feat`, `fix`, `chore`.

### 2.5 Run the full workflow once

```bash
# 1. Create an issue, e.g. #1 "Add a README"
gh issue create --title "docs: add README" --label docs

# 2. Branch from an up-to-date main
git switch main && git pull
git switch -c docs/add-readme

# 3. Edit, stage, commit (Conventional Commit message)
echo "# Git practice" > README.md
git add README.md
git commit -m "docs: add README"

# 4. Push and open a PR that closes the issue
git push -u origin docs/add-readme
gh pr create --fill --body "Closes #1"

# 5. Review your own diff on GitHub, then squash-merge and delete the branch
gh pr merge --squash --delete-branch

# 6. Update local main and confirm the cleanup
git switch main && git pull
git branch --list
```

## 3. Definition of Done

- `pre-commit run --all-files` passes locally.
- A direct commit to `main` is rejected by the `no-commit-to-branch` hook.
- At least one issue was closed by a merged PR whose title is a Conventional Commit.
- The feature branch is deleted locally and on GitHub.

## 4. Reflection questions

1. Why is it dangerous to commit a secret even if you delete it in the next commit?
   (See [13 — Troubleshooting](../git/13-troubleshooting.md).)
2. What is the difference between `git merge --squash` and a normal merge? When would a team
   prefer each?
3. Which decision in your practice deserves an ADR, and which does not? Why?
   (Start from the [ADR template](../templates/adr-template.md).)
4. What would you put in CODEOWNERS for a team of 1 architect, 3 developers and 1 security
   engineer?

## 5. Further reading

- Pro Git book (free): <https://git-scm.com/book/en/v2>
- GitHub Flow: <https://docs.github.com/en/get-started/using-github/github-flow>
- Conventional Commits: <https://www.conventionalcommits.org/>
- ADRs: <https://adr.github.io/> and MADR: <https://adr.github.io/madr/>
- pre-commit: <https://pre-commit.com/>
