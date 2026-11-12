# Postmortem — {Incident title}

<!-- Blameless: describe what the system and process allowed, not who made a mistake.
     Write it within a few days, while memory is fresh. Replace {placeholders}, delete comments
     and the example. -->

| | |
|---|---|
| **Date** | {YYYY-MM-DD} |
| **Severity** | SEV{1-4} |
| **Duration** | {start → end, total time} |
| **Authors** | {names or roles} |
| **Status** | Draft / Reviewed |

## Summary

{Three sentences: what broke, who was affected, how it was fixed.}

## Impact

- Users or services affected: {…}
- Data lost: {none / description}
- Business impact: {…}

## Timeline

<!-- Use one time zone. Include detection, escalation, workarounds and recovery. -->

| Time | Event |
|------|-------|
| {hh:mm} | {what happened or was done} |

## Root cause

{Why it happened. Ask "why" until you reach something you can change (five whys).}

## What went well

- {…}

## What went badly

- {…}

## Where we got lucky

- {…}

## Action items

| # | Action | Type (prevent / detect / mitigate) | Owner | Due |
|---|--------|-----------------------------------|-------|-----|
| 1 | {action} | {type} | {who} | {date} |

## Lessons for runbooks and design

- {runbook to update, ADR to revisit}

## Example (delete before use)

| Time | Event |
|------|-------|
| 09:12 | Monitoring alerts: wiki returns HTTP 502 |
| 09:20 | On-call finds the tunnel connector stopped after an update |
