# Low-Level Design — {Area, e.g. Network}

<!-- The LLD is precise enough for someone else to build from, without asking you.
     One LLD per area (network, compute, access ...). Use only placeholder data in public repos:
     example.com, 10.10.x.x. Replace every {placeholder}, delete comments and the example. -->

| | |
|---|---|
| **Document** | Low-Level Design — {area} |
| **Version** | 0.1 (draft) |
| **Status** | Proposed |
| **Implements** | HLD section {n} |

## 1. Design principles

- {rule that guides every detail below, e.g. default-deny between zones}

## 2. Inventory and naming

<!-- Naming convention first; it makes everything else readable. -->

| Item | Convention | Example |
|------|------------|---------|
| Host | `<role><nn>` | `app01` |

## 3. Parameters and sizing

| Item | Value | Reason |
|------|-------|--------|
| {setting, size or address} | {value} | {why} |

## 4. Configuration details

{Tables, snippets or diagrams: addressing plan, rule matrix, resource sizes, schedules.}

```text
{configuration excerpt}
```

## 5. Dependencies

- {what must exist first}

## 6. Verification

<!-- How the builder proves the design was implemented as written. -->

- {check, e.g. `ping` between zones is blocked}

## 7. Open points

- {question not yet decided, with owner}

## Example (delete before use)

| Zone | VLAN | Subnet | Purpose |
|------|------|--------|---------|
| MGMT | 10 | 10.10.10.0/24 | Administration only |
| SERVERS | 20 | 10.10.20.0/24 | Internal services |
