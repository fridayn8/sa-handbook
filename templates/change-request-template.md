# Change Request (RFC) — {Short title}

<!-- An RFC asks for approval to change production. It must let the approver judge risk without
     asking questions. Replace {placeholders}, delete comments and the example. -->

| | |
|---|---|
| **ID** | RFC-{NNNN} |
| **Type** | Standard / Normal / Emergency |
| **Requested by** | {name or role} |
| **Planned window** | {YYYY-MM-DD hh:mm–hh:mm, time zone} |
| **Status** | Draft / Submitted / Approved / Implemented / Closed |

## Reason

{Why the change is needed. Link the issue, requirement or ADR.}

## Scope

- Systems affected: {…}
- Users affected and downtime expected: {…}

## Implementation plan

1. {step}

## Test plan

- {smoke tests after the change}

## Risk assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| {risk} | {H/M/L} | {H/M/L} | {action} |

## Rollback plan

<!-- Decide the rollback trigger BEFORE the change: "if X is not true by hh:mm, we roll back". -->

- Trigger: {condition and time}
- Steps: {how to return to the previous state}
- Backup verified: {yes / no, when}

## Communication

- Before: {who is told, when}
- After: {who is told}

## Approval

| Role | Name | Decision | Date |
|------|------|----------|------|
| Change approver | {name} | | |

## Example (delete before use)

- Trigger: if the VPN does not reconnect within 15 minutes of the upgrade, restore the VM snapshot.
