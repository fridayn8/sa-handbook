# Contributing

This repository follows a professional team workflow, even when you work alone.
Background: [Git 11 — Professional workflow on GitHub](git/11-github-workflow.md).

## Workflow (GitHub Flow)

1. **Create an issue** with a template (Task or Bug). Add a type label and an `area:` label.
2. **Create a branch** from an up-to-date `main`:

   ```bash
   git switch main && git pull
   git switch -c <type>/<short-description>
   ```

3. **Commit** small, focused changes with [Conventional Commits](#commit-messages).
4. **Push and open a pull request**; fill in the template and write `Closes #<issue>`.

   ```bash
   git push -u origin <branch>
   gh pr create
   ```

5. **Self-review the diff**, make sure checks pass, resolve all conversations.
6. **Squash and merge.** The PR title becomes the commit on `main`.
7. **Clean up:** `git switch main && git pull && git branch -d <branch>`.

## Branch names

`<type>/<short-kebab-description>`, using the same types as commits:

```text
docs/git-rebase-drill
fix/glossary-broken-anchor
chore/update-pre-commit
```

## Commit messages

[Conventional Commits](https://www.conventionalcommits.org/):

```text
<type>(<scope>): <imperative description, lower-case, no period, ≤ 72 chars>

<optional body: why the change is needed>

<optional footer: Closes #12, BREAKING CHANGE: …>
```

| Type | Use |
|------|-----|
| `feat` | New content or capability |
| `fix` | Correction of an error |
| `docs` | Wording, structure or links only |
| `style` | Formatting |
| `refactor` | Restructure without changing meaning |
| `perf` | Performance |
| `test` | Tests |
| `build` | Build system, dependency pins |
| `ci` | CI configuration |
| `chore` | Maintenance and tooling |
| `revert` | Revert an earlier commit |

**Scopes:** `git`, `architecture`, `glossary`, `templates`, `practice`, `scripts`, `github`, `ci`.

The `commit-msg` pre-commit hook enforces the format.

## Local checks

```bash
pip install pre-commit
pre-commit install
pre-commit install --hook-type commit-msg
pre-commit run --all-files
```

Before opening a PR also run:

```bash
python3 scripts/check-links.py .        # relative links and anchors resolve
python3 scripts/gen-glossary-index.py   # only after editing the glossary; a second run changes nothing
```

Every Mermaid diagram must render on GitHub.

## Scope

This repository is **reference only**: no project-specific content, no code that needs
infrastructure. Worked cases belong in
[`sa-case-studies`](https://github.com/fridayn8/sa-case-studies) and code in
[`sa-projects`](https://github.com/fridayn8/sa-projects). Park new ideas in
[BACKLOG.md](BACKLOG.md) instead of building them.

## Data hygiene — never commit

- Secrets: tokens, passwords, private keys (SSH, age, WireGuard), `.env` files
- Real IP addresses, domains, hostnames or anything from a real employer

Use placeholders (`example.com`, `10.10.x.x`). If a secret is committed by mistake, follow
[the secret recipe](git/13-troubleshooting.md#-i-committed-a-secret-token-password-private-key) — **rotate it first**.
