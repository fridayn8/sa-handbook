# Runbook — {Task, e.g. Restore the wiki from backup}

<!-- A runbook lets a tired person do one task correctly at 3 a.m.
     Short imperative steps, exact commands, an expected result after each step, a way back.
     Test it on a fresh machine before you trust it. Replace {placeholders}, delete comments
     and the example. -->

| | |
|---|---|
| **Owner** | {name or role} |
| **Last tested** | {YYYY-MM-DD} |
| **Risk** | Low / Medium / High |
| **Estimated time** | {minutes} |

## When to use this

{Trigger, e.g. alert name or symptom. When NOT to use it.}

## Before you start

- Access needed: {accounts, VPN, break-glass}
- Tools: {commands, links}
- Notify: {who, if users are affected}

## Steps

1. {Action.}

   ```bash
   {exact command}
   ```

   Expected: {what you should see}.
2. {Action.}

## Verify

- {check that proves the task worked}

## Roll back

{How to return to the previous state if a step fails.}

## Escalate

{Who to call, after how long, with what information.}

## Example (delete before use)

1. Stop the service.

   ```bash
   sudo systemctl stop wiki
   ```

   Expected: `systemctl status wiki` shows `inactive (dead)`.
