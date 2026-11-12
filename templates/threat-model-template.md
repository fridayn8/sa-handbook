# Threat Model — {System name}

<!-- A threat model answers: what are we protecting, from whom, where can it go wrong and what
     do we do about it. Keep it short enough to be re-read at every design change.
     Replace every {placeholder}, delete comments and the example. -->

| | |
|---|---|
| **Document** | Threat model |
| **Version** | 0.1 (draft) |
| **Status** | Proposed |
| **Method** | STRIDE per trust boundary |
| **Related** | HLD · LLDs |

## 1. How to read this

{Scope in two sentences. Likelihood and impact use High / Medium / Low.}

## 2. Assets

| ID | Asset | Why it matters | Confidentiality / Integrity / Availability |
|----|-------|----------------|---------------------------------------------|
| A1 | {data or service} | {impact if lost or exposed} | {C / I / A priority} |

## 3. Trust boundaries

<!-- A trust boundary is where data or control crosses between different levels of trust. -->

| ID | Boundary | Crossed by |
|----|----------|------------|
| TB-1 | {zone or system} → {zone or system} | {protocol or flow} |

## 4. Threat analysis (STRIDE)

<!-- S Spoofing · T Tampering · R Repudiation · I Information disclosure · D Denial of service ·
     E Elevation of privilege. One table per boundary. Write "n/a" where a letter does not apply. -->

### TB-1 — {boundary name}

| STRIDE | Threat | Existing control | Gap / action | Residual risk |
|--------|--------|------------------|--------------|---------------|
| S | {threat} | {control} | {action or none} | {H/M/L} |
| T | | | | |
| R | | | | |
| I | | | | |
| D | | | | |
| E | | | | |

## 5. Top risks and actions

| # | Risk | Residual risk | Action | Owner | Due |
|---|------|---------------|--------|-------|-----|
| 1 | {risk} | {H/M/L} | {action} | {who} | {date} |

## 6. Assumptions and out of scope

- {assumption}

## Example (delete before use)

| STRIDE | Threat | Existing control | Gap / action | Residual risk |
|--------|--------|------------------|--------------|---------------|
| S | Stolen staff password used to reach the wiki | SSO with MFA | Enforce phishing-resistant MFA for admins | Low |
