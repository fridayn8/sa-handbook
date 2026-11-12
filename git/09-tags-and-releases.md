# 09 — Tags and Releases

## git tag

**Purpose:** Give a permanent, human-friendly name to a specific commit — typically a release.
**Risk level:** ✅ safe (moving/deleting pushed tags 🔥 confuses everyone)

| Type | Command | Stores | Use for |
|------|---------|--------|---------|
| Lightweight | `git tag v1.0.0` | Just a pointer | Private/temporary marks |
| Annotated | `git tag -a v1.0.0 -m "…"` | Tagger, date, message (+ signature) | **Releases** |

**Basic**

```bash
git tag -a v1.0.0 -m "Release 1.0.0: first stable design"
git tag                          # list
git tag -l "v1.*"                # filter
git show v1.0.0                  # details
git push origin v1.0.0           # tags are NOT pushed by default
```

**Advanced**

```bash
git tag -a v0.9.0 9f8e7d6 -m "…"     # tag an older commit
git tag -s v1.0.0 -m "…"             # signed tag
git push --follow-tags               # push commits + annotated tags reachable from them
git push origin --tags               # push all tags (careful: includes local experiments)
git tag -d v1.0.0                    # delete local tag
git push origin --delete v1.0.0      # 🔥 delete remote tag
git tag --sort=-v:refname            # sort by version, newest first
git tag --contains 9f8e7d6           # which releases include this commit?
git switch --detach v1.0.0           # look at the code of a release
```

## Semantic Versioning (SemVer)

Format: **`MAJOR.MINOR.PATCH`** (e.g. `v2.4.1`), optionally with pre-release `-rc.1` or build `+build.5`.

| Increase | When | Example |
|----------|------|---------|
| **MAJOR** | Incompatible / breaking change | `1.4.2 → 2.0.0` |
| **MINOR** | New functionality, backward compatible | `1.4.2 → 1.5.0` |
| **PATCH** | Backward-compatible bug fix | `1.4.2 → 1.4.3` |

- `0.y.z` = initial development; anything may change.
- Pre-releases sort before the release: `1.0.0-alpha < 1.0.0-rc.1 < 1.0.0`.

**Mapping from Conventional Commits:** `fix:` → PATCH, `feat:` → MINOR,
`feat!:` or `BREAKING CHANGE:` footer → MAJOR.

**For an infrastructure/docs repo like this one**, a practical interpretation:

| Version bump | Example |
|--------------|---------|
| MAJOR | Network re-design (new IP plan), module interface change |
| MINOR | New feature, new module, new ADR accepted |
| PATCH | Fixes and doc corrections |

## GitHub Releases

A **Release** = a tag + release notes + optional files (binaries, PDFs).

```bash
gh release create v1.0.0 --title "v1.0.0 — Design baseline" --notes-file notes.md
gh release create v1.0.0 --generate-notes         # notes from merged PRs
gh release list
gh release view v1.0.0
```

## Automating releases with release-please

`release-please` (GitHub Action by Google) reads Conventional Commits on `main` and keeps a
**release PR** open containing the next version number and the updated `CHANGELOG.md`.
Merging that PR creates the tag and the GitHub Release.

```text
feat/fix commits merged to main
        ↓
release-please opens/updates "chore(main): release 1.1.0" PR (CHANGELOG + version)
        ↓
you merge it when ready
        ↓
tag v1.1.0 + GitHub Release created automatically
```

Minimal workflow:

```yaml
# .github/workflows/release-please.yml
on:
  push:
    branches: [main]
permissions:
  contents: write
  pull-requests: write
jobs:
  release-please:
    runs-on: ubuntu-latest
    steps:
      - uses: googleapis/release-please-action@v4
        with:
          release-type: simple
```
