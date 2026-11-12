# 12 — GitHub CLI (`gh`)

**Purpose:** Do GitHub work (issues, PRs, Actions, releases) from the terminal.
Install: <https://cli.github.com/>

## Setup

```bash
gh auth login              # interactive: GitHub.com → SSH or HTTPS → browser login
gh auth status
gh auth setup-git          # use gh as Git credential helper for HTTPS
gh repo set-default        # choose default repo when several remotes exist
```

## Repositories

```bash
gh repo view --web                         # open repo in browser
gh repo clone <owner>/<repo>
gh repo create my-lab --private --clone
gh repo fork <owner>/<repo> --clone        # fork + clone + set upstream remote
```

## Issues

```bash
gh issue list                              # open issues
gh issue list --label area:git --assignee @me
gh issue create --title "docs: add VLAN plan" --label docs,area:git --milestone "v1.0"
gh issue view 12 --comments
gh issue comment 12 --body "Started on branch docs/vlan-plan"
gh issue close 12 --reason completed
gh issue develop 12 --checkout             # create a branch linked to issue #12 and switch to it
```

## Pull requests

```bash
gh pr create --fill                        # title/body from commits
gh pr create --draft --title "feat(proxmox): add VM module" --body "Closes #15"
gh pr list
gh pr status                               # your PRs + review requests
gh pr view 15 --web
gh pr checkout 15                          # check out someone's PR locally
gh pr diff 15
gh pr checks 15 --watch                    # wait for CI
gh pr review 15 --approve | --request-changes -b "…" | --comment -b "…"
gh pr ready 15                             # mark draft as ready for review
gh pr merge 15 --squash --delete-branch
gh pr merge 15 --squash --auto             # merge automatically when checks pass
```

## GitHub Actions

```bash
gh run list                                # recent workflow runs
gh run watch                               # follow a running workflow
gh run view <run-id> --log-failed          # only logs of failed steps
gh run rerun <run-id> --failed             # re-run failed jobs
gh workflow list
gh workflow run terraform-plan.yml -f env=lab   # trigger a workflow_dispatch workflow
gh secret set CLOUDFLARE_API_TOKEN         # prompts for value; stored encrypted in repo secrets
gh variable set TF_VERSION --body "1.9.8"
```

## Releases

```bash
gh release create v1.0.0 --generate-notes
gh release list
gh release download v1.0.0
```

## Power features

```bash
gh api repos/{owner}/{repo}/branches       # raw REST API call
gh api graphql -f query='query { viewer { login } }'
gh search issues "vlan" --repo <owner>/<repo>
gh alias set prs 'pr list --author @me'
gh browse docs/hld.md                      # open a file on GitHub
```
