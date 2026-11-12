# Requirements — {System or project name}

<!-- Copy this file, replace every {placeholder}, delete the guidance comments and the example.
     Rule: every requirement gets an ID, a priority and (later) a test or acceptance criterion. -->

| | |
|---|---|
| **Document** | Requirements specification |
| **Version** | 0.1 (draft) |
| **Status** | Proposed |
| **Owner** | {name or role} |

## 1. Business context

{Who is the customer, what do they do, what is the situation today? 3–6 sentences.}

| # | Problem | Raised by |
|---|---------|-----------|
| P1 | {problem in the stakeholder's words} | {who} |

## 2. Business goals

<!-- A goal without a measure cannot be verified. Give every goal a KPI. -->

| ID | Goal | Measure (KPI) |
|----|------|---------------|
| BG-1 | {goal} | {how you will know it is met} |

## 3. Stakeholders

| Stakeholder | Interest |
|-------------|----------|
| {role} | {what they care about} |

## 4. Functional requirements

<!-- What the system must DO. One sentence, testable, no solution words. -->

| ID | Requirement | Priority (MoSCoW) |
|----|-------------|-------------------|
| FR-01 | {requirement} | Must |

## 5. Non-functional requirements

<!-- How well it must do it. Cover each quality below, or write "n/a" with a reason. -->

| ID | Quality | Requirement (with a number) |
|----|---------|-----------------------------|
| NFR-01 | Availability / recovery | {e.g. RTO 4 h, RPO 24 h} |
| NFR-02 | Security | {e.g. MFA for all staff} |
| NFR-03 | Performance / capacity | {e.g. 50 concurrent users} |
| NFR-04 | Operability | {e.g. every change via PR} |
| NFR-05 | Cost | {e.g. below USD 100 per month} |

## 6. Constraints

<!-- Fixed from outside: budget, tools mandated, regulation, deadlines. -->

- {constraint}

## 7. Assumptions

<!-- Things you believe but have not verified. Each one is a risk until confirmed. -->

- {assumption}

## 8. Out of scope

- {item explicitly not included}

## 9. Traceability

<!-- Link each requirement to the decision and design element that satisfies it. -->

| Requirement | Decision (ADR) | Design element | Test / acceptance |
|-------------|----------------|----------------|-------------------|
| FR-01 | ADR-NNNN | {HLD section} | {test id} |

## Example (delete before use)

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-01 | Staff can open the wiki from home with single sign-on and MFA | Must |
| NFR-01 | The wiki is restorable within 4 hours of a failure (RTO) with at most 24 hours of lost data (RPO) | Must |
