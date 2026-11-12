# SA Handbook

A timeless **reference** for a Solution Architect: what things are and how to use them.
Open it when you are confused; it answers most questions in under a minute.

| | |
|---|---|
| **Purpose** | Reference: Git and GitHub workflow, SA concepts, glossary, blank templates |
| **Audience** | A beginner Solution Architect building a professional habit and a portfolio |
| **Language** | English |
| **Data** | Fictional only (`example.com`, `10.10.x.x`); no real company, person or credential |

## I want to…

| I want to… | Open |
|------------|------|
| Look up a Git command | [Git cheatsheet](git/cheatsheet.md), then the [Git handbook index](git/README.md) |
| Fix a Git mistake | [05 — Undo and recovery](git/05-undo-and-recovery.md), [13 — Troubleshooting](git/13-troubleshooting.md) |
| Choose a branching strategy | [14 — Branching strategies and environments](git/14-branching-strategies-and-environments.md) |
| Understand a term (RTO, HLD, SLO …) | [Glossary](architecture/glossary.md) — A–Z index at the top |
| See how terms connect over a project | [Lifecycle and term chains](architecture/lifecycle-and-term-chains.md) |
| Know what a Solution Architect produces | [Top 10 SA activities](architecture/solution-architect-top10.md) |
| Pick a tool for a job | [Tools stack](architecture/tools-stack.md) |
| Start an ADR, HLD, LLD, threat model or runbook | [Templates](templates/) |
| Practise the PR flow | [Git workflow practice](practice/git-workflow-practice.md) |

## Contents

```text
git/             Git and GitHub handbook (README, cheatsheet, chapters 00–14)
architecture/    Top 10 SA activities, glossary (141 terms), tools stack, lifecycle and term chains
templates/       Blank, copy-and-fill documents and GitHub issue forms
practice/        Hands-on exercises
scripts/         check-links.py (links and anchors), gen-glossary-index.py (glossary A–Z index)
```

## Companion repositories

The three repositories follow the order of work of a Solution Architect: **know → think → build**.

| Repository | Purpose |
|------------|---------|
| `sa-handbook` (this one) | **Know** — reference |
| [`sa-case-studies`](https://github.com/fridayn8/sa-case-studies) | **Think** — one worked case, from first contact to handover |
| [`sa-projects`](https://github.com/fridayn8/sa-projects) | **Build** — hands-on projects as code |

## Working in this repository

Contributions follow [CONTRIBUTING.md](CONTRIBUTING.md): GitHub Flow, Conventional Commits,
squash merge. Install the checks with `pre-commit install`; run them with
`pre-commit run --all-files`.

Check links and anchors, and regenerate the glossary index after editing it:

```bash
python3 scripts/check-links.py .
python3 scripts/gen-glossary-index.py
```

Planned and parked work is tracked in [BACKLOG.md](BACKLOG.md); history in
[CHANGELOG.md](CHANGELOG.md).

## Licence

[MIT](LICENSE).
