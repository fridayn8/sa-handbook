# Solution Architect Glossary

Terms you will meet as a Solution Architect, with **full name**, **what it is**, **when and how
it is used**, how it behaves in **normal operation vs. an incident/special case**, and which
**terms and processes it relates to**.

To see how these terms connect in real projects (new project, normal change, incident,
disaster), read [lifecycle and term chains](lifecycle-and-term-chains.md).

> **Example Corp** is the fictional case used for examples in this glossary. The full worked case
> lives in [`sa-case-studies`](https://github.com/fridayn8/sa-case-studies).

**Entry format**

- **What** — short definition
- **When / how** — the situation where it is used and what you actually do with it
- **Normal vs. incident** — only where the term behaves differently in a crisis
- **Related** — connected terms and processes
- **Example** — a concrete use in the Example Corp scenario

<!-- INDEX:START -->

## Index (A–Z) — 141 entries

| Term | Full name | Category |
|------|-----------|----------|
| [AAA](#aaa--authentication-authorization-accounting) | Authentication, Authorization, Accounting | Security |
| [ADR](#adr--architecture-decision-record) | Architecture Decision Record | Requirements and design |
| [Agile / Scrum / Kanban](#agile--scrum--kanban) | — | Delivery and release |
| [ARB](#arb--architecture-review-board) | Architecture Review Board | Requirements and design |
| [Artifact](#artifact) | — | Delivery and release |
| [As-built documentation](#as-built-documentation) | — | Requirements and design |
| [As-is / To-be](#as-is--to-be--current-state--target-state) | Current state / Target state | Requirements and design |
| [Assumption](#assumption) | — | Requirements and design |
| [Audit trail](#audit-trail) | — | Security |
| [Availability / "Nines"](#availability--nines) | — | Reliability, operations and continuity |
| [Backup / 3-2-1 rule](#backup--3-2-1-rule) | — | Reliability, operations and continuity |
| [BCP](#bcp--business-continuity-plan) | Business Continuity Plan | Reliability, operations and continuity |
| [BIA](#bia--business-impact-analysis) | Business Impact Analysis | Reliability, operations and continuity |
| [Blast radius](#blast-radius) | — | Security |
| [Blue-green / Canary / Rolling deployment](#blue-green--canary--rolling-deployment) | — | Delivery and release |
| [BoM](#bom--bill-of-materials) | Bill of Materials | Business, engagement and pre-sales |
| [BRD](#brd--business-requirements-document) | Business Requirements Document | Business, engagement and pre-sales |
| [Break-glass access](#break-glass-access) | — | Networking |
| [C4 model](#c4-model--context-containers-components-code) | Context, Containers, Components, Code | Requirements and design |
| [CAB / ECAB](#cab--ecab--change-advisory-board--emergency-cab) | Change Advisory Board / Emergency CAB | IT service management and change |
| [Capacity planning / Headroom](#capacity-planning--headroom) | — | Reliability, operations and continuity |
| [CAPEX / OPEX](#capex--opex--capital-expenditure--operating-expenditure) | Capital Expenditure / Operating Expenditure | Business, engagement and pre-sales |
| [Change management / RFC](#change-management--rfc--request-for-change) | Request for Change | IT service management and change |
| [Change types](#change-types--standard--normal--emergency) | Standard / Normal / Emergency | IT service management and change |
| [CI / CD](#ci--cd--continuous-integration--continuous-delivery-or-deployment) | Continuous Integration / Continuous Delivery or Deployment | Delivery and release |
| [CIA triad](#cia-triad--confidentiality-integrity-availability) | Confidentiality, Integrity, Availability | Security |
| [ClickOps](#clickops) | — | Infrastructure and automation |
| [CMDB](#cmdb--configuration-management-database) | Configuration Management Database | Infrastructure and automation |
| [Compliance / Governance](#compliance--governance) | — | Cost and governance |
| [Configuration management](#configuration-management) | — | Infrastructure and automation |
| [Constraint](#constraint) | — | Requirements and design |
| [CVE](#cve--common-vulnerabilities-and-exposures) | Common Vulnerabilities and Exposures | Security |
| [DDoS](#ddos--distributed-denial-of-service) | Distributed Denial of Service | Security |
| [Declarative / Imperative](#declarative--imperative) | — | Infrastructure and automation |
| [Defense in depth](#defense-in-depth) | — | Security |
| [DevOps](#devops) | — | Delivery and release |
| [DHCP](#dhcp--dynamic-host-configuration-protocol) | Dynamic Host Configuration Protocol | Networking |
| [DMZ](#dmz--demilitarized-zone) | Demilitarized Zone | Security |
| [DNS](#dns--domain-name-system) | Domain Name System | Networking |
| [DORA metrics](#dora-metrics--devops-research-and-assessment) | DevOps Research and Assessment | Reliability, operations and continuity |
| [DR / DRP](#dr--drp--disaster-recovery--disaster-recovery-plan) | Disaster Recovery / Disaster Recovery Plan | Reliability, operations and continuity |
| [Drift](#drift) | — | Infrastructure and automation |
| [EA](#ea--enterprise-architecture) | Enterprise Architecture | Requirements and design |
| [Environment](#environment--dev-sit-qa-uat-stg-prod-dr) | DEV, SIT, QA, UAT, STG, PROD, DR | Delivery and release |
| [Error budget](#error-budget) | — | Reliability, operations and continuity |
| [Escalation](#escalation) | — | IT service management and change |
| [Failover / Failback](#failover--failback) | — | Requirements and design |
| [Feature flag (feature toggle)](#feature-flag-feature-toggle) | — | Delivery and release |
| [FinOps](#finops--financial-operations) | Financial Operations | Cost and governance |
| [FR](#fr--functional-requirement) | Functional Requirement | Requirements and design |
| [FRD / FSD](#frd--fsd--functional-requirements--functional-specification-document) | Functional Requirements / Functional Specification Document | Business, engagement and pre-sales |
| [Gap analysis](#gap-analysis) | — | Requirements and design |
| [GitOps](#gitops) | — | Infrastructure and automation |
| [Go / No-Go](#go--no-go) | — | Delivery and release |
| [Go-live / Cutover](#go-live--cutover) | — | Delivery and release |
| [Golden image / Template](#golden-image--template) | — | Infrastructure and automation |
| [Greenfield / Brownfield](#greenfield--brownfield) | — | Requirements and design |
| [HA](#ha--high-availability) | High Availability | Requirements and design |
| [Handover / BAU](#handover--bau--business-as-usual) | Business As Usual | Delivery and release |
| [Hardening / Baseline](#hardening--baseline) | — | Security |
| [HLD](#hld--high-level-design) | High-Level Design | Requirements and design |
| [Hotfix](#hotfix) | — | Delivery and release |
| [Hypercare](#hypercare) | — | Delivery and release |
| [Hypervisor](#hypervisor--type-1--type-2) | Type 1 / Type 2 | Infrastructure and automation |
| [IaC](#iac--infrastructure-as-code) | Infrastructure as Code | Infrastructure and automation |
| [IAM](#iam--identity-and-access-management) | Identity and Access Management | Security |
| [Idempotent](#idempotent) | — | Infrastructure and automation |
| [Immutable infrastructure](#immutable-infrastructure) | — | Infrastructure and automation |
| [Incident](#incident) | — | IT service management and change |
| [ITIL / ITSM](#itil--itsm--information-technology-infrastructure-library--it-service-management) | Information Technology Infrastructure Library / IT Service Management | IT service management and change |
| [KPI](#kpi--key-performance-indicator) | Key Performance Indicator | Business, engagement and pre-sales |
| [LAN / WAN](#lan--wan--local-area-network--wide-area-network) | Local Area Network / Wide Area Network | Networking |
| [LLD](#lld--low-level-design) | Low-Level Design | Requirements and design |
| [Maintenance window / Change freeze](#maintenance-window--change-freeze) | — | IT service management and change |
| [MFA](#mfa--multi-factor-authentication) | Multi-Factor Authentication | Security |
| [Monitoring / Alerting](#monitoring--alerting) | — | Reliability, operations and continuity |
| [MTTR / MTBF / MTTD](#mttr--mtbf--mttd--mean-time-to-recover--between-failures--to-detect) | Mean Time To Recover / Between Failures / To Detect | Reliability, operations and continuity |
| [MVP](#mvp--minimum-viable-product) | Minimum Viable Product | Business, engagement and pre-sales |
| [NAT](#nat--network-address-translation) | Network Address Translation | Networking |
| [NAT traversal / CGNAT](#nat-traversal--cgnat--carrier-grade-nat) | Carrier-Grade NAT | Networking |
| [NFR](#nfr--non-functional-requirement) | Non-Functional Requirement | Requirements and design |
| [Observability](#observability--metrics-logs-traces) | metrics, logs, traces | Reliability, operations and continuity |
| [On-call](#on-call) | — | IT service management and change |
| [Pipeline / Quality gate](#pipeline--quality-gate) | — | Delivery and release |
| [PKI / TLS](#pki--tls--public-key-infrastructure--transport-layer-security) | Public Key Infrastructure / Transport Layer Security | Security |
| [Plan / Apply](#plan--apply) | — | Infrastructure and automation |
| [PoC](#poc--proof-of-concept) | Proof of Concept | Business, engagement and pre-sales |
| [Policy as code](#policy-as-code) | — | Cost and governance |
| [PoLP](#polp--principle-of-least-privilege) | Principle of Least Privilege | Security |
| [Postmortem / PIR](#postmortem--pir--post-incident-review) | Post-Incident Review | IT service management and change |
| [PoV / Pilot](#pov--pilot--proof-of-value--pilot) | Proof of Value / Pilot | Business, engagement and pre-sales |
| [Problem / RCA](#problem--rca--root-cause-analysis) | Root Cause Analysis | IT service management and change |
| [Promotion](#promotion) | — | Delivery and release |
| [Provisioning](#provisioning) | — | Infrastructure and automation |
| [RACI](#raci--responsible-accountable-consulted-informed) | Responsible, Accountable, Consulted, Informed | Business, engagement and pre-sales |
| [RBAC](#rbac--role-based-access-control) | Role-Based Access Control | Security |
| [Reference architecture / Blueprint](#reference-architecture--blueprint) | — | Requirements and design |
| [Release / Deployment](#release--deployment) | — | Delivery and release |
| [Reverse proxy / Load balancer](#reverse-proxy--load-balancer) | — | Networking |
| [RFI](#rfi--request-for-information) | Request for Information | Business, engagement and pre-sales |
| [RFP](#rfp--request-for-proposal) | Request for Proposal | Business, engagement and pre-sales |
| [RFQ](#rfq--request-for-quotation) | Request for Quotation | Business, engagement and pre-sales |
| [Risk register](#risk-register) | — | Cost and governance |
| [Roadmap](#roadmap) | — | Requirements and design |
| [ROI](#roi--return-on-investment) | Return on Investment | Business, engagement and pre-sales |
| [Rollback / Roll-forward](#rollback--roll-forward) | — | Delivery and release |
| [RPO](#rpo--recovery-point-objective) | Recovery Point Objective | Reliability, operations and continuity |
| [RTO](#rto--recovery-time-objective) | Recovery Time Objective | Reliability, operations and continuity |
| [Runbook / Playbook / SOP](#runbook--playbook--sop--standard-operating-procedure) | Standard Operating Procedure | IT service management and change |
| [SAD](#sad--solution-architecture-document) | Solution Architecture Document | Requirements and design |
| [Scalability](#scalability--vertical--horizontal) | vertical / horizontal | Requirements and design |
| [SDLC](#sdlc--software-development-life-cycle) | Software Development Life Cycle | Delivery and release |
| [Secrets management](#secrets-management) | — | Security |
| [Segmentation / Micro-segmentation](#segmentation--micro-segmentation) | — | Security |
| [SemVer](#semver--semantic-versioning) | Semantic Versioning | Delivery and release |
| [Severity / Priority](#severity--priority--sev1sev4--p1p4) | SEV1–SEV4 / P1–P4 | IT service management and change |
| [SIEM](#siem--security-information-and-event-management) | Security Information and Event Management | Security |
| [Site-to-site VPN](#site-to-site-vpn) | — | Networking |
| [SLA / SLO / SLI](#sla--slo--sli--service-level-agreement--objective--indicator) | Service Level Agreement / Objective / Indicator | Reliability, operations and continuity |
| [Smoke test / Sanity test / Regression test](#smoke-test--sanity-test--regression-test) | — | Delivery and release |
| [SOW](#sow--statement-of-work) | Statement of Work | Business, engagement and pre-sales |
| [SPOF](#spof--single-point-of-failure) | Single Point of Failure | Requirements and design |
| [SRE](#sre--site-reliability-engineering) | Site Reliability Engineering | Delivery and release |
| [SSO](#sso--single-sign-on) | Single Sign-On | Security |
| [Stakeholder](#stakeholder) | — | Business, engagement and pre-sales |
| [State (Terraform)](#state-terraform) | — | Infrastructure and automation |
| [Subnet / CIDR](#subnet--cidr--classless-inter-domain-routing) | Classless Inter-Domain Routing | Networking |
| [TCO](#tco--total-cost-of-ownership) | Total Cost of Ownership | Business, engagement and pre-sales |
| [Technical debt](#technical-debt) | — | Requirements and design |
| [Threat model / STRIDE](#threat-model--stride--spoofing-tampering-repudiation-information-disclosure-denial-of-service-elevation-of-privilege) | Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege | Security |
| [TOGAF](#togaf--the-open-group-architecture-framework) | The Open Group Architecture Framework | Requirements and design |
| [Toil](#toil) | — | Reliability, operations and continuity |
| [Trade-off](#trade-off) | — | Requirements and design |
| [Trust boundary](#trust-boundary) | — | Security |
| [UAT](#uat--user-acceptance-testing) | User Acceptance Testing | Delivery and release |
| [VLAN](#vlan--virtual-local-area-network) | Virtual Local Area Network | Networking |
| [VM / Container / LXC](#vm--container--lxc--virtual-machine--linux-containers) | Virtual Machine / Linux Containers | Infrastructure and automation |
| [VPN](#vpn--virtual-private-network) | Virtual Private Network | Security |
| [WAF](#waf--web-application-firewall) | Web Application Firewall | Security |
| [WAF (framework)](#waf-framework--well-architected-framework) | Well-Architected Framework | Requirements and design |
| [Zero Trust / ZTNA](#zero-trust--ztna--zero-trust-network-access) | Zero Trust Network Access | Security |

<!-- INDEX:END -->

---

## 1. Business, engagement and pre-sales

### RFI — Request for Information

- **What:** A document a customer sends to vendors to collect general information about their capabilities, before any formal bid.
- **When / how:** Very early, when the customer is exploring the market. The architect answers technical questions and capabilities honestly and briefly.
- **Related:** RFP, RFQ, Discovery.
- **Example:** Example Corp asks three integrators whether they support Proxmox and Zero Trust remote access.

### RFP — Request for Proposal

- **What:** A formal request for vendors to submit a detailed solution proposal and price.
- **When / how:** After RFI, when the customer has defined requirements. The architect designs the proposed solution (HLD-level), estimates effort and BoM, and lists assumptions.
- **Related:** RFI, RFQ, SOW, BoM, HLD, TCO.
- **Example:** "Proposal for secure office infrastructure: virtualisation, firewall, remote access."

### RFQ — Request for Quotation

- **What:** A request for price only, for items that are already well specified.
- **When / how:** When the customer knows exactly what to buy (e.g. 2 servers of a given spec). Little design work; mostly BoM and pricing.
- **Related:** RFP, BoM.

### SOW — Statement of Work

- **What:** Contract document defining scope, deliverables, timeline, responsibilities, acceptance criteria and price of a project.
- **When / how:** Signed before implementation starts. The architect ensures the technical scope, assumptions and *out-of-scope* items are correct — gaps here become disputes later.
- **Related:** RFP, BRD, RACI, Change request (scope), UAT (acceptance).
- **Example:** "Deliver Proxmox cluster, OPNsense with 4 VLANs, Cloudflare Tunnel for 2 apps; migration of existing VMs is out of scope."

### BRD — Business Requirements Document

- **What:** Describes the business problem, goals and what the business needs — *not* how it is built.
- **When / how:** Produced in discovery, usually by a business analyst with stakeholders. The architect reads it to derive functional requirements and NFRs.
- **Related:** FRD, FR, NFR, Stakeholder, KPI.
- **Example:** "Staff must access internal apps from home securely; downtime costs about USD 500/hour."

### FRD / FSD — Functional Requirements / Functional Specification Document

- **What:** Detailed description of *what the system must do* (features, behaviours, rules).
- **When / how:** After the BRD, before design. The architect checks every function can be met by the design.
- **Related:** BRD, FR, HLD, UAT (tests are written against it).

### PoC — Proof of Concept

- **What:** A small, time-boxed experiment proving one technical idea works.
- **When / how:** When there is technical uncertainty before committing to a design. Define a question, success criteria and a deadline; record findings; feed the result into an ADR.
- **Related:** PoV, Pilot, MVP, Spike, ADR.
- **Example:** "Can Cloudflare Tunnel handle 100 MB uploads to our document app?"

### PoV / Pilot — Proof of Value / Pilot

- **What:** PoV shows *business value* with real users/data; a pilot is a limited production rollout to a small group.
- **When / how:** After a successful PoC, before full rollout — to prove adoption and value, and find operational issues.
- **Related:** PoC, MVP, Go-live, Hypercare.
- **Example:** 5 staff use Tailscale for two weeks before rollout to all 25.

### MVP — Minimum Viable Product

- **What:** The smallest version of a solution that delivers real value and allows learning.
- **When / how:** To deliver early and iterate instead of building everything at once. The architect ensures the MVP architecture can grow (no dead-ends).
- **Related:** PoC, Pilot, Roadmap, Technical debt.

### BoM — Bill of Materials

- **What:** List of all hardware, software, licences and services required, with quantities and prices.
- **When / how:** In proposals and procurement. Derived from capacity planning.
- **Related:** Capacity planning, CAPEX, TCO, RFQ.
- **Example:** 1× server (32 cores, 256 GB RAM), 4× 2 TB NVMe, 1× managed switch, Cloudflare Zero Trust (free tier).

### CAPEX / OPEX — Capital Expenditure / Operating Expenditure

- **What:** CAPEX = one-off investment in assets (servers). OPEX = ongoing costs (subscriptions, power, cloud usage, support).
- **When / how:** In cost estimates and business cases. On-prem is CAPEX-heavy; cloud/SaaS is OPEX-heavy. Finance often prefers one or the other.
- **Related:** TCO, ROI, BoM, FinOps.

### TCO — Total Cost of Ownership

- **What:** All costs of a solution over its lifetime (e.g. 3–5 years): purchase, licences, power, staff time, support, end-of-life.
- **When / how:** Comparing options fairly — "free" open source can have higher staff cost; cheap hardware can have high power cost.
- **Related:** CAPEX/OPEX, ROI, ADR (cost as a decision driver).

### ROI — Return on Investment

- **What:** (Benefit − Cost) ÷ Cost. Shows whether an investment pays back.
- **When / how:** In business cases to justify a project to management.
- **Related:** TCO, KPI, BRD.
- **Example:** Avoiding 10 hours/year of downtime at USD 500/hour = USD 5 000 benefit.

### KPI — Key Performance Indicator

- **What:** A measurable value showing whether a business goal is being achieved.
- **When / how:** Defined with stakeholders to measure solution success after go-live.
- **Related:** SLA, SLO, OKR, ROI.
- **Example:** "Remote-access tickets reduced by 50 % within 3 months."

### RACI — Responsible, Accountable, Consulted, Informed

- **What:** A matrix stating who does the work (R), who owns the outcome (A — only one), who gives input (C), and who is kept updated (I).
- **When / how:** At project start and for operational processes, to avoid "I thought you were doing it".
- **Related:** SOW, Stakeholder, ADR (deciders/consulted/informed), Escalation.
- **Example:** Firewall change — R: network engineer, A: IT manager, C: security, I: helpdesk.

### Stakeholder

- **What:** Anyone affected by or able to influence the solution: users, management, security, operations, finance, vendors.
- **When / how:** Identified in discovery; each has concerns the architecture must address (e.g. security wants auditability, finance wants low OPEX).
- **Related:** RACI, BRD, NFR.

---

## 2. Requirements and design

### FR — Functional Requirement

- **What:** Something the system must *do*.
- **When / how:** Collected in discovery; each FR should be testable and traceable to a design element and a test.
- **Related:** NFR, BRD, FRD, UAT.
- **Example:** "Admins can manage Proxmox from outside the office."

### NFR — Non-Functional Requirement

- **What:** *How well* the system must work: availability, performance, scalability, security, maintainability, compliance, cost. Also called *quality attributes*.
- **When / how:** The architect's main input — NFRs drive most architecture decisions. Make them measurable ("99.5 % monthly availability", not "highly available").
- **Related:** FR, SLA/SLO, RTO/RPO, HA, Trade-off, ADR.
- **Example:** "Public apps must survive the loss of the office internet link for ≤ 4 h (RTO 4 h)."

### Constraint

- **What:** A fixed limit you cannot change: budget, existing hardware, regulations, deadlines, team skills.
- **When / how:** Listed in the HLD; they eliminate options early.
- **Related:** Assumption, NFR, ADR.
- **Example:** "Must reuse the existing single server; budget for new hardware is zero."

### Assumption

- **What:** Something believed true but not verified.
- **When / how:** Documented in HLD and SOW so that if it turns out false, the impact is clear. Validate the risky ones early (often with a PoC).
- **Related:** Constraint, Risk, SOW, PoC.
- **Example:** "The ISP provides a static public IP" (affects WireGuard site-to-site design).

### As-is / To-be — Current state / Target state

- **What:** As-is describes how things work today; to-be describes the desired future architecture.
- **When / how:** Brownfield projects: document as-is, design to-be, then plan the transition (roadmap, migration waves).
- **Related:** Gap analysis, Brownfield, Roadmap, Migration.

### Gap analysis

- **What:** Comparison between as-is and to-be listing what is missing.
- **When / how:** To turn the target design into a list of work items and estimate effort.
- **Related:** As-is/To-be, Roadmap, SOW.

### Greenfield / Brownfield

- **What:** Greenfield = building from scratch. Brownfield = changing an existing, running environment.
- **When / how:** Brownfield requires as-is documentation, compatibility, migration and minimal disruption; greenfield allows cleaner design.
- **Related:** As-is/To-be, Migration, Cutover.

### HLD — High-Level Design

- **What:** The big-picture design: scope, context, main components, interactions, key decisions, how NFRs are met.
- **When / how:** After requirements, reviewed by stakeholders before detailed design. Audience: architects, management, security, operations.
- **Related:** LLD, SAD, C4, ADR, NFR.

### LLD — Low-Level Design

- **What:** Implementation-level detail: IP plan, VLAN IDs, firewall rules, VM sizes, naming, configuration values.
- **When / how:** After HLD approval; used by engineers to build and by operations to support.
- **Related:** HLD, IaC (LLD becomes code), As-built.

### SAD — Solution Architecture Document

- **What:** A single document combining context, requirements, HLD, decisions and views. Some companies use SAD instead of separate HLD/LLD.
- **When / how:** Formal architecture review boards often require one.
- **Related:** HLD, LLD, ARB, ADR.

### As-built documentation

- **What:** Documentation of the system *as it was actually built*, including deviations from the design.
- **When / how:** Delivered at project end / handover to operations. In IaC setups, the code is a large part of the as-built.
- **Related:** LLD, Handover, CMDB, Drift.

### ADR — Architecture Decision Record

- **What:** A short document recording one significant decision, its context, options and consequences.
- **When / how:** Whenever a decision is hard to reverse or had real alternatives. Proposed via PR; superseded, never rewritten.
- **Related:** HLD, Trade-off, PoC, RFC (design).
- **Example:** [ADR-0001](https://github.com/fridayn8/sa-case-studies/blob/main/case-01-example-corp/02-options-decisions/adr/0001-record-architecture-decisions.md).

### ARB — Architecture Review Board

- **What:** A group of senior architects that reviews and approves significant designs for consistency with standards.
- **When / how:** In larger organisations, before a project moves from design to build.
- **Related:** SAD, ADR, CAB (the operational equivalent for changes).

### C4 model — Context, Containers, Components, Code

- **What:** A way to draw architecture at four zoom levels.
- **When / how:** Context for everyone, Container for technical stakeholders, Component/Code for developers. Keep diagrams as code (Mermaid/Structurizr).
- **Related:** HLD, Diagrams as code.

### TOGAF — The Open Group Architecture Framework

- **What:** A widely used *enterprise* architecture framework; its core is the ADM (Architecture Development Method) cycle.
- **When / how:** Enterprise architecture and large organisations. A solution architect should know the vocabulary (baseline/target architecture, gap analysis, architecture building blocks), even if not applying it fully.
- **Related:** EA, As-is/To-be, Gap analysis.

### EA — Enterprise Architecture

- **What:** Architecture at the level of the whole organisation (business, data, application, technology), setting standards and roadmaps.
- **When / how:** Solution architects design individual solutions *within* the EA standards.
- **Related:** TOGAF, ARB, Reference architecture.

### WAF (framework) — Well-Architected Framework

- **What:** Cloud providers' best-practice frameworks (AWS, Azure, Google Cloud) organised in pillars: operational excellence, security, reliability, performance efficiency, cost optimisation, sustainability.
- **When / how:** As a checklist to review a design. Useful even on-prem.
- **Related:** NFR, Trade-off. *Not to be confused with* WAF — Web Application Firewall.

### Reference architecture / Blueprint

- **What:** A reusable, proven design for a class of problems, often with IaC templates.
- **When / how:** Starting new solutions from a known-good baseline instead of from zero.
- **Related:** EA, IaC, Golden image.

### SPOF — Single Point of Failure

- **What:** A component whose failure stops the whole service.
- **When / how:** Identify in every design review; remove (redundancy) or accept and document (cost trade-off + DR plan).
- **Normal vs. incident:** Invisible in normal operation; causes a total outage when it fails.
- **Related:** HA, Redundancy, DR, Risk.
- **Example:** One Proxmox host and one ISP link are SPOFs in Example Corp — accepted, mitigated by backups and Cloudflare-hosted status page.

### HA — High Availability

- **What:** Design that keeps a service running despite component failures (redundancy, automatic failover).
- **When / how:** When NFRs require high uptime. Costs more (2× hardware, complexity) — must be justified by downtime cost.
- **Normal vs. incident:** In normal operation both nodes run; during failure the standby takes over automatically.
- **Related:** SPOF, Failover, Cluster, SLA, DR (HA = within a site; DR = site loss).

### Failover / Failback

- **What:** Failover = switching to a standby component when the primary fails. Failback = returning to the primary after repair.
- **When / how:** Part of HA and DR plans; must be tested regularly (a failover that was never tested often fails).
- **Related:** HA, DR, RTO, Runbook.

### Scalability — vertical / horizontal

- **What:** Ability to handle more load. Vertical (scale up) = bigger machine; horizontal (scale out) = more machines.
- **When / how:** Vertical is simple but limited; horizontal needs stateless design and load balancing.
- **Related:** Capacity planning, Load balancer, NFR.

### Trade-off

- **What:** Accepting less of one quality to gain another (cost vs. availability, security vs. usability, speed vs. quality).
- **When / how:** In every decision — document trade-offs explicitly in ADRs so stakeholders consciously accept them.
- **Related:** ADR, NFR, Constraint.

### Technical debt

- **What:** The future cost of shortcuts taken today.
- **When / how:** Sometimes deliberate (MVP deadline). Track it as issues, and plan to pay it back.
- **Related:** MVP, Refactor, Roadmap.

### Roadmap

- **What:** A time-based plan of what will be delivered and in what order.
- **When / how:** To sequence work from as-is to to-be in phases or releases.
- **Related:** Gap analysis, MVP, Milestone.
- **Example:** [`sa-projects` roadmap](https://github.com/fridayn8/sa-projects/blob/main/ROADMAP.md).

---

## 3. Security

### CIA triad — Confidentiality, Integrity, Availability

- **What:** The three core goals of information security.
- **When / how:** As a lens for threat modelling and classifying the impact of incidents.
- **Related:** STRIDE, Risk, BIA.

### AAA — Authentication, Authorization, Accounting

- **What:** Who are you (authentication), what may you do (authorization), what did you do (accounting/audit).
- **When / how:** Design checklist for every access path (Proxmox UI, SSH, VPN, apps).
- **Related:** IAM, MFA, RBAC, Audit trail.

### IAM — Identity and Access Management

- **What:** Processes and systems that manage identities and their permissions.
- **When / how:** Central identity (e.g. Google Workspace / Entra ID) + SSO for all tools; joiner-mover-leaver process.
- **Related:** SSO, MFA, RBAC, PoLP.

### SSO — Single Sign-On

- **What:** One login (one identity provider) gives access to many applications.
- **When / how:** Tailscale and Cloudflare Access both use SSO via an identity provider (IdP) — disabling a user there removes all access at once.
- **Related:** IAM, MFA, IdP, SAML/OIDC.

### MFA — Multi-Factor Authentication

- **What:** Login requires two or more factors: something you know (password), have (phone, key), are (biometric).
- **When / how:** Mandatory for all admin and remote access.
- **Related:** SSO, IAM, Zero Trust.

### RBAC — Role-Based Access Control

- **What:** Permissions are given to roles (admin, operator, viewer); users get roles.
- **When / how:** Proxmox, Cloudflare and GitHub all support roles. Easier to audit than per-user permissions.
- **Related:** IAM, PoLP, ABAC.

### PoLP — Principle of Least Privilege

- **What:** Give every user, service and token only the minimum permissions required, for the minimum time.
- **When / how:** Scoped API tokens (one Cloudflare zone, DNS edit only), firewall default deny, Tailscale ACLs.
- **Related:** RBAC, Zero Trust, Defense in depth.

### Zero Trust / ZTNA — Zero Trust Network Access

- **What:** "Never trust, always verify": no implicit trust based on network location; every request is authenticated, authorised and encrypted.
- **When / how:** Replacing broad VPN access with per-application access (Cloudflare Access, Tailscale ACLs).
- **Related:** VPN, SSO, MFA, Micro-segmentation, PoLP.

### VPN — Virtual Private Network

- **What:** Encrypted tunnel connecting a device or network to another network over the internet.
- **When / how:** Site-to-site (office ↔ office) or remote access. WireGuard and IPsec are protocols; Tailscale is a WireGuard-based mesh product.
- **Normal vs. incident:** In this design, Tailscale is the normal admin path; plain WireGuard on OPNsense is the **break-glass** path when Tailscale or the IdP is unavailable.
- **Related:** Zero Trust, Site-to-site, Break-glass.

### DMZ — Demilitarized Zone

- **What:** A network segment for services exposed to less-trusted networks, isolated from the internal LAN.
- **When / how:** Place internet-facing components (e.g. `cloudflared`, reverse proxy) in a DMZ VLAN with strict firewall rules towards internal VLANs.
- **Related:** VLAN, Firewall, Segmentation, Trust boundary.

### Segmentation / Micro-segmentation

- **What:** Dividing the network into zones (VLANs/subnets) with controlled traffic between them; micro-segmentation goes down to individual workloads.
- **When / how:** Limit blast radius — a compromised IoT device must not reach Proxmox management.
- **Related:** VLAN, DMZ, Zero Trust, Blast radius.

### Blast radius

- **What:** How much damage a single failure or compromise can cause.
- **When / how:** Reduce it with segmentation, separate credentials, small changes, canary releases.
- **Related:** Segmentation, PoLP, Canary.

### Defense in depth

- **What:** Multiple independent layers of security so one failure doesn't expose everything.
- **When / how:** Cloudflare WAF + Access → OPNsense firewall → VLAN segmentation → host firewall → app auth → backups.
- **Related:** Zero Trust, Segmentation, Hardening.

### WAF — Web Application Firewall

- **What:** Filters HTTP traffic to block attacks such as SQL injection and XSS.
- **When / how:** In front of public web apps (Cloudflare WAF).
- **Related:** DDoS, Defense in depth, OWASP Top 10.

### DDoS — Distributed Denial of Service

- **What:** Attack overwhelming a service with traffic from many sources.
- **When / how:** Mitigated upstream by CDN/edge providers (Cloudflare); an office internet link cannot absorb it alone.
- **Related:** WAF, Availability, CDN.

### Threat model / STRIDE — Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege

- **What:** A structured analysis of what can go wrong; STRIDE is a checklist of threat categories.
- **When / how:** During design and when the architecture changes. Walk every trust boundary through STRIDE, list mitigations.
- **Related:** Trust boundary, Risk, CIA, Defense in depth.

### Trust boundary

- **What:** A point where data or control passes between zones of different trust (internet → DMZ, user VLAN → management).
- **When / how:** Mark them on diagrams; threat-model each one.
- **Related:** Threat model, DMZ, Segmentation.

### Hardening / Baseline

- **What:** Reducing attack surface by disabling unused services, applying secure configuration and patches. A baseline is the agreed minimum configuration (e.g. CIS Benchmarks).
- **When / how:** Built into golden images and Ansible roles so every machine starts hardened.
- **Related:** CIS, Golden image, Configuration management, Vulnerability.

### CVE — Common Vulnerabilities and Exposures

- **What:** Public identifier for a known vulnerability (e.g. CVE-2024-3094). Severity is often scored with CVSS (Common Vulnerability Scoring System, 0–10).
- **When / how:** Vulnerability management: scan, prioritise by CVSS + exposure, patch.
- **Normal vs. incident:** Normally handled in regular patch cycles; a critical, actively exploited CVE triggers an emergency change.
- **Related:** Patch management, Emergency change, Hardening.

### PKI / TLS — Public Key Infrastructure / Transport Layer Security

- **What:** PKI = system of certificates and certificate authorities. TLS = protocol encrypting traffic (HTTPS).
- **When / how:** Certificates for internal services, mTLS between services, certificate expiry monitoring.
- **Related:** Encryption in transit, mTLS, Certificate rotation.

### Secrets management

- **What:** How passwords, API tokens and keys are stored, distributed, rotated and audited.
- **When / how:** Never in plain Git; use SOPS + age, a vault, or CI secret stores. Rotate on staff changes and after leaks.
- **Normal vs. incident:** A leaked secret is an incident: revoke/rotate first, then clean up.
- **Related:** SOPS, PoLP, Rotation, gitleaks.

### SIEM — Security Information and Event Management

- **What:** Central system that collects logs and detects security events.
- **When / how:** Larger organisations; small ones start with centralised logging and alerts.
- **Related:** Audit trail, Observability, SOC.

### Audit trail

- **What:** Tamper-evident record of who did what and when.
- **When / how:** Required for compliance and incident investigation. Git history + PR reviews + CI logs are a strong audit trail for infrastructure changes.
- **Related:** AAA, GitOps, Compliance, Repudiation (STRIDE).

---

## 4. Networking

### LAN / WAN — Local Area Network / Wide Area Network

- **What:** LAN = network inside a site; WAN = connections between sites / to the internet.
- **Related:** VLAN, Site-to-site VPN, ISP.

### VLAN — Virtual Local Area Network

- **What:** Logical separation of one physical network into isolated broadcast domains (IEEE 802.1Q tags).
- **When / how:** Separate management, servers, users, DMZ, IoT, guest. Inter-VLAN traffic goes through the firewall.
- **Related:** Segmentation, Trunk port, Subnet, Firewall rules.
- **Example:** VLAN 10 management `10.10.10.0/24`, VLAN 20 servers `10.10.20.0/24`.

### Subnet / CIDR — Classless Inter-Domain Routing

- **What:** A range of IP addresses; CIDR notation `10.10.20.0/24` = 256 addresses (254 usable hosts).
- **When / how:** IP addressing plan in the LLD; leave room for growth; avoid overlaps with VPN peers and home networks (`192.168.0.0/24`, `192.168.1.0/24` are common at home).
- **Related:** VLAN, IP plan, NAT, Routing.

### NAT — Network Address Translation

- **What:** Rewrites IP addresses, typically letting private networks reach the internet through one public IP.
- **When / how:** Outbound NAT on OPNsense; inbound port-forwarding (avoided in this design thanks to Cloudflare Tunnel).
- **Related:** Port forwarding, CGNAT, NAT traversal.

### NAT traversal / CGNAT — Carrier-Grade NAT

- **What:** NAT traversal = techniques letting peers connect directly behind NAT. CGNAT = the ISP itself NATs you, so you have no public IP.
- **When / how:** Tailscale handles NAT traversal automatically (with relays as fallback); plain WireGuard needs at least one reachable endpoint — a problem behind CGNAT.
- **Related:** NAT, VPN, Tailscale.

### DNS — Domain Name System

- **What:** Translates names to IP addresses. Records: A/AAAA (IP), CNAME (alias), MX (mail), TXT (verification), etc.
- **When / how:** Public DNS on Cloudflare; internal DNS on OPNsense (Unbound). *Split-horizon DNS* returns different answers internally and externally.
- **Normal vs. incident:** "It's always DNS" — DNS misconfigurations are a frequent cause of outages; TTLs control how fast changes propagate.
- **Related:** TTL, Cloudflare, DHCP.

### DHCP — Dynamic Host Configuration Protocol

- **What:** Automatically assigns IP address, gateway and DNS to devices.
- **When / how:** Per VLAN on OPNsense; servers use static IPs or DHCP reservations.
- **Related:** DNS, VLAN, IP plan.

### Reverse proxy / Load balancer

- **What:** A reverse proxy receives client requests and forwards them to backend servers (TLS termination, routing). A load balancer distributes traffic across several backends.
- **When / how:** In front of web apps; Cloudflare Tunnel acts like a reverse proxy at the edge.
- **Related:** HA, Scalability, TLS, WAF.

### Site-to-site VPN

- **What:** A permanent encrypted tunnel connecting two networks.
- **When / how:** Office ↔ branch / data centre. WireGuard or IPsec between firewalls.
- **Related:** VPN, WireGuard, Routing.

### Break-glass access

- **What:** An emergency access path, normally unused, used only when the regular path fails.
- **When / how:** Documented, tested, tightly controlled, and audited when used.
- **Normal vs. incident:** Never used in normal operation; activated during an outage of SSO/Tailscale.
- **Related:** Runbook, Incident, VPN.

---

## 5. Infrastructure and automation

### Hypervisor — Type 1 / Type 2

- **What:** Software running virtual machines. Type 1 (bare-metal: Proxmox VE, ESXi, Hyper-V) runs directly on hardware; Type 2 (VirtualBox, VMware Workstation) runs on top of an OS.
- **When / how:** Type 1 for servers; Type 2 for laptops and labs (e.g. nested Proxmox).
- **Related:** VM, Container, Nested virtualisation.

### VM / Container / LXC — Virtual Machine / Linux Containers

- **What:** A VM emulates a full computer with its own kernel. A container shares the host kernel and isolates processes (Docker, LXC).
- **When / how:** VMs for strong isolation or other OSes (OPNsense); LXC/containers for lightweight Linux services.
- **Related:** Hypervisor, Golden image.

### IaC — Infrastructure as Code

- **What:** Defining infrastructure in code files, applied by tools (OpenTofu/Terraform, Ansible, Packer).
- **When / how:** Every infrastructure change goes through Git and PR review; environments are reproducible.
- **Related:** GitOps, Declarative, Idempotent, Drift, State.

### Declarative / Imperative

- **What:** Declarative = describe the desired end state (Terraform). Imperative = list the steps to execute (shell scripts).
- **Related:** IaC, Idempotent.

### Idempotent

- **What:** Running an operation multiple times gives the same result as running it once.
- **When / how:** Ansible tasks and Terraform applies must be idempotent — a second run should report "no changes".
- **Related:** IaC, Configuration management, Drift.

### State (Terraform)

- **What:** Terraform's record mapping code to real resources. Contains sensitive values.
- **When / how:** Stored in a remote, locked backend (Cloudflare R2/S3); never in Git.
- **Related:** Remote backend, Drift, Plan/Apply.

### Plan / Apply

- **What:** `tofu plan` / `terraform plan` previews changes; `apply` executes them.
- **When / how:** Plan on every PR, reviewed like code; apply only after merge/approval.
- **Related:** CI/CD, Change management, Drift.

### Drift

- **What:** Difference between what code declares and what really exists (e.g. someone changed a firewall rule in the UI).
- **When / how:** Detect with a scheduled `tofu plan`; fix by updating code or re-applying.
- **Normal vs. incident:** During an incident, manual "hotfix" changes create drift — they must be captured in code afterwards.
- **Related:** State, GitOps, ClickOps.

### ClickOps

- **What:** (Informal) making changes manually through web consoles instead of code.
- **When / how:** Acceptable for exploration or emergencies; must be followed by codifying the change.
- **Related:** Drift, IaC.

### Golden image / Template

- **What:** A pre-built, hardened, patched machine image from which VMs are cloned.
- **When / how:** Built automatically — e.g. with Packer, or from an official cloud image plus configuration management (the approach used in Example Corp); rebuilt regularly to include patches.
- **Related:** Immutable infrastructure, Hardening, cloud-init, Packer.

### Immutable infrastructure

- **What:** Servers are never modified after deployment; changes are made by replacing them with new ones from an updated image.
- **When / how:** Reduces drift and "snowflake servers". Requires automation and externalised data.
- **Related:** Golden image, Drift, Pets vs. cattle.

### Configuration management

- **What:** Automating the configuration *inside* machines (packages, files, services) — Ansible, Salt, Puppet, Chef.
- **When / how:** After provisioning; for OPNsense, WireGuard and Linux hardening in Example Corp.
- **Related:** IaC, Idempotent, Provisioning.

### Provisioning

- **What:** Creating infrastructure resources (VMs, networks, DNS records).
- **Related:** IaC, Terraform, Configuration management.

### GitOps

- **What:** Git is the single source of truth for desired state; automation (pipelines or agents) makes reality match Git.
- **When / how:** Changes only via PR; merge triggers apply. Rollback = revert in Git.
- **Related:** IaC, CI/CD, Audit trail, Drift.

### CMDB — Configuration Management Database

- **What:** Inventory of IT assets (configuration items) and their relationships.
- **When / how:** In ITIL organisations, used for impact analysis of changes and incidents. In IaC setups, code + state can serve as a large part of it.
- **Related:** ITSM, Change management, As-built.

---

## 6. Delivery and release

### SDLC — Software Development Life Cycle

- **What:** The phases of building software: plan → analyse → design → build → test → deploy → maintain.
- **Related:** DevOps, Agile, Waterfall.

### Agile / Scrum / Kanban

- **What:** Agile = iterative delivery in small increments with feedback. Scrum = framework with fixed sprints, roles and ceremonies. Kanban = continuous flow with work-in-progress limits.
- **When / how:** The architect works in the same iterations — *just-enough* design up front, refined each sprint.
- **Related:** MVP, Roadmap, Backlog.

### DevOps

- **What:** Culture and practices uniting development and operations: automation, shared ownership, fast feedback. Lifecycle: Plan → Code → Build → Test → Release → Deploy → Operate → Monitor.
- **Related:** CI/CD, SRE, GitOps, IaC.

### SRE — Site Reliability Engineering

- **What:** Google's approach to operations using software engineering: SLOs, error budgets, automation, blameless postmortems.
- **Related:** SLO, Error budget, Postmortem, Toil.

### CI / CD — Continuous Integration / Continuous Delivery or Deployment

- **What:** CI = every change is automatically built and tested. Continuous Delivery = every change is *ready* to release (manual approval to prod). Continuous Deployment = every passing change goes to prod automatically.
- **When / how:** Pipelines in GitHub Actions; quality gates (lint, tests, scans, plan).
- **Related:** Pipeline, Artifact, Environment, GitOps.

### Pipeline / Quality gate

- **What:** Automated sequence of stages (build, test, scan, deploy). A quality gate is a check that must pass before continuing.
- **Related:** CI/CD, Status check, Shift left.

### Artifact

- **What:** The built, versioned output of a pipeline (container image, package, VM template, Terraform plan file).
- **When / how:** *Build once, deploy many* — promote the same artifact through environments.
- **Related:** Promotion, Release, Registry.

### Environment — DEV, SIT, QA, UAT, STG, PROD, DR

- **What:** Isolated copies of the system for different stages: Development, System Integration Testing, Quality Assurance, User Acceptance Testing, Staging, Production, Disaster Recovery.
- **When / how:** Changes are promoted DEV → … → PROD. See [Git 14 — Environments](../git/14-branching-strategies-and-environments.md#4-environments).
- **Related:** Promotion, UAT, Staging, Parity.

### Promotion

- **What:** Moving a release from one environment to the next after it passes checks.
- **Related:** Environment, Artifact, Approval gate.

### UAT — User Acceptance Testing

- **What:** Business users verify the solution meets their requirements, ending in a formal **sign-off**.
- **When / how:** Before go-live; test cases derived from the BRD/FRD.
- **Related:** SOW (acceptance criteria), Go/No-Go, Environment.

### Smoke test / Sanity test / Regression test

- **What:** Smoke = quick check that the main functions work after deployment. Sanity = narrow check that a specific fix works. Regression = check that existing features still work after a change.
- **When / how:** Smoke right after every deploy (manual or automated); regression in CI/QA.
- **Related:** Deployment, Go-live, CI.

### Release / Deployment

- **What:** Deployment = putting a version onto an environment. Release = making functionality available to users.
- **When / how:** Separated by feature flags or blue-green; tagged with SemVer.
- **Related:** SemVer, Feature flag, Blue-green, Change management.

### SemVer — Semantic Versioning

- **What:** `MAJOR.MINOR.PATCH` versions: breaking, feature, fix.
- **Related:** Release, Tag, Conventional Commits. See [Git 09](../git/09-tags-and-releases.md).

### Blue-green / Canary / Rolling deployment

- **What:** Strategies to deploy with little or no downtime — see [Git 14 §6](../git/14-branching-strategies-and-environments.md#6-deployment-strategies-how-a-release-reaches-users).
- **Related:** Rollback, Feature flag, HA.

### Feature flag (feature toggle)

- **What:** A runtime switch that turns functionality on/off without deploying.
- **When / how:** Trunk-based development, gradual rollouts, kill switch during incidents.
- **Normal vs. incident:** Normally used for gradual rollout; in an incident, turning a flag off is often the fastest mitigation.
- **Related:** Trunk-based, Canary, Release.

### Rollback / Roll-forward

- **What:** Rollback = return to the previous working version. Roll-forward = fix by deploying a newer version.
- **When / how:** Every change needs a tested rollback plan; choose roll-forward when rollback is impossible (e.g. irreversible data migration).
- **Related:** Change management, Revert, Blue-green.

### Hotfix

- **What:** An urgent fix deployed to production outside the normal release cycle.
- **When / how:** Branch from what is in production, minimal change, fast-tracked review and emergency change approval, then back-port to the main line.
- **Related:** Incident, Emergency change, ECAB, Git 14 scenario C.

### Go-live / Cutover

- **What:** Go-live = the moment a solution enters production use. Cutover = the planned set of steps switching from the old system to the new one.
- **When / how:** Detailed cutover plan with timings, owners, checkpoints and rollback point; often during a maintenance window.
- **Related:** Go/No-Go, Hypercare, Maintenance window, Migration.

### Go / No-Go

- **What:** A decision meeting/checklist just before go-live or a major change.
- **When / how:** Check: UAT sign-off, tests green, backups done, rollback ready, people available, no freeze.
- **Related:** CAB, UAT, Cutover.

### Hypercare

- **What:** A period of heightened support after go-live (days to weeks) with the project team on standby.
- **Related:** Go-live, Handover, Incident.

### Handover / BAU — Business As Usual

- **What:** Transfer of a delivered solution from the project team to operations (BAU support), with documentation, runbooks and training.
- **Related:** As-built, Runbook, Hypercare.

---

## 7. IT service management and change

### ITIL / ITSM — Information Technology Infrastructure Library / IT Service Management

- **What:** ITSM = managing IT as services for the business. ITIL = the most common ITSM framework (incident, problem, change, service request, configuration management…).
- **When / how:** Many companies' operations run on ITIL processes and tools (ServiceNow, Jira Service Management).
- **Related:** Incident, Problem, Change, CMDB, SLA.

### Change management / RFC — Request for Change

- **What:** Process to plan, approve and record changes to production to minimise risk. An RFC (change request, CR) is the ticket describing one change.
- **When / how:** RFC contains: description, reason, risk/impact, test evidence, implementation plan, **rollback plan**, schedule. Link the PR and plan output.
- **Related:** CAB, Change types, Maintenance window, Rollback.
- *Note:* "RFC" also means the IETF's *Request for Comments* standards documents (e.g. RFC 1918 private IP ranges).

### Change types — Standard / Normal / Emergency

- **What:** Standard = pre-approved, low-risk, repeatable. Normal = assessed and approved (often by CAB). Emergency = must be done urgently to restore service or fix a critical risk.
- **When / how:** Automate standard changes; emergency changes get retrospective review.
- **Normal vs. incident:** Incidents usually lead to emergency changes.
- **Related:** RFC, CAB, ECAB, Hotfix.

### CAB / ECAB — Change Advisory Board / Emergency CAB

- **What:** Group that reviews and approves normal changes; ECAB is a small subset that approves emergency changes quickly.
- **Related:** RFC, ARB, Go/No-Go.

### Maintenance window / Change freeze

- **What:** Maintenance window = agreed time when changes (and possible downtime) are allowed. Change freeze (blackout period) = time when no changes are allowed (e.g. year-end closing).
- **Related:** Change management, SLA, Cutover.

### Incident

- **What:** An unplanned interruption or degradation of a service.
- **When / how:** Goal is to **restore service as fast as possible** (workaround is fine). Classified by severity/priority; managed by an incident commander for major incidents.
- **Related:** Severity, Problem, MTTR, Postmortem, Runbook.

### Severity / Priority — SEV1–SEV4 / P1–P4

- **What:** Severity = technical impact; priority = urgency of response (from impact × urgency). Scales vary per company.
- **Example:** SEV1/P1 — all users cannot work; SEV2/P2 — major function down, workaround exists; SEV3/P3 — minor issue; SEV4/P4 — cosmetic/request.
- **Related:** Incident, SLA (response times per priority), Escalation.

### Problem / RCA — Root Cause Analysis

- **What:** Problem = the underlying cause of one or more incidents. RCA = the investigation that finds it (e.g. *5 Whys*, fishbone diagram).
- **When / how:** After the incident is resolved; leads to a permanent fix. A known cause with a workaround but no fix yet is a *known error*.
- **Related:** Incident, Postmortem, Known error, ADR (if design changes).

### Postmortem / PIR — Post-Incident Review

- **What:** A written review after a significant incident: timeline, impact, root cause, what went well/badly, action items. *Blameless* = focus on systems, not individuals.
- **Related:** RCA, Incident, Runbook updates.

### Escalation

- **What:** Involving higher-level expertise (functional) or management (hierarchical) when an issue can't be solved in time.
- **Related:** RACI, On-call, SLA.

### On-call

- **What:** Rotation of engineers available outside working hours to respond to alerts.
- **Related:** Alerting, Runbook, Escalation.

### Runbook / Playbook / SOP — Standard Operating Procedure

- **What:** Runbook = step-by-step instructions for a specific operational task (restart service, restore backup). Playbook = broader response guide for a scenario (ransomware). SOP = formal standard procedure.
- **When / how:** Written during the project, tested, kept next to the code; automated over time.
- **Related:** Incident, Break-glass, Handover.

---

## 8. Reliability, operations and continuity

### SLA / SLO / SLI — Service Level Agreement / Objective / Indicator

- **What:** SLI = what you measure (e.g. % successful requests). SLO = internal target for the SLI (99.9 %). SLA = contractual promise to customers, usually looser than the SLO, with penalties.
- **When / how:** Define SLIs and SLOs per critical service; alert when SLOs are threatened.
- **Related:** Error budget, Availability, Incident, KPI.

### Availability / "Nines"

- **What:** % of time a service is usable. 99 % ≈ 3.65 days/year down; 99.9 % ≈ 8.8 h/year; 99.99 % ≈ 53 min/year.
- **When / how:** Each extra nine costs much more — choose based on downtime cost (BIA).
- **Related:** SLA, HA, SPOF.

### Error budget

- **What:** 100 % − SLO = allowed unreliability. With a 99.9 % SLO, ~43 minutes/month may fail.
- **When / how:** If the budget is used up, slow down releases and focus on reliability.
- **Related:** SLO, SRE, Change freeze.

### MTTR / MTBF / MTTD — Mean Time To Recover / Between Failures / To Detect

- **What:** MTTD = how fast you notice a problem; MTTR = how fast you restore service; MTBF = average time between failures.
- **When / how:** Improve MTTD with monitoring and alerting; MTTR with runbooks, automation and rollback.
- **Related:** Incident, Observability, DORA metrics.

### DORA metrics — DevOps Research and Assessment

- **What:** Four delivery performance metrics: deployment frequency, lead time for changes, change failure rate, time to restore service.
- **Related:** DevOps, MTTR, CI/CD.

### Observability — metrics, logs, traces

- **What:** Ability to understand system state from outputs: metrics (numbers over time), logs (events), traces (request paths across services).
- **When / how:** Prometheus/Grafana for metrics, central logs, OpenTelemetry for traces.
- **Related:** Monitoring, Alerting, SLI.

### Monitoring / Alerting

- **What:** Monitoring = continuously checking health and metrics. Alerting = notifying people when action is needed.
- **When / how:** Alert on symptoms users feel (SLOs), not every metric; every alert should be actionable and have a runbook.
- **Related:** Observability, On-call, MTTD.

### Capacity planning / Headroom

- **What:** Estimating resources (CPU, RAM, storage, bandwidth) needed now and in future; headroom = spare capacity (often 20–30 %) for peaks and growth.
- **Related:** BoM, Scalability, Cost estimate.

### BCP — Business Continuity Plan

- **What:** How the *business* keeps operating during a disruption (people, processes, alternative ways of working) — broader than IT.
- **Related:** DR, BIA, RTO/RPO.

### DR / DRP — Disaster Recovery / Disaster Recovery Plan

- **What:** Restoring IT services after a major failure (site loss, ransomware, hardware destroyed). DRP = the documented, tested procedure.
- **When / how:** Defines DR site/strategy, backups, roles, runbooks, and is tested regularly (DR drills).
- **Normal vs. incident:** Dormant in normal operation; *invoked* by management decision when an incident becomes a disaster.
- **Related:** RTO, RPO, Backup, BCP, Failover.

### RTO — Recovery Time Objective

- **What:** Maximum acceptable time to restore a service after a disruption.
- **When / how:** Set per service from the BIA; drives the DR strategy (backup restore = hours; warm standby = minutes).
- **Related:** RPO, DR, BIA, MTTR.
- **Example:** File server RTO 8 h; internal web app RTO 4 h.

### RPO — Recovery Point Objective

- **What:** Maximum acceptable data loss, measured in time.
- **When / how:** Drives backup frequency and replication. RPO 24 h → nightly backups are enough; RPO 15 min → frequent snapshots/replication.
- **Related:** RTO, Backup, Replication.

### BIA — Business Impact Analysis

- **What:** Analysis of how much each service's downtime costs the business, used to set RTO/RPO and priorities.
- **Related:** RTO, RPO, BCP, NFR.

### Backup / 3-2-1 rule

- **What:** Copies of data for restore. 3-2-1 = 3 copies, on 2 different media, 1 off-site (modern variants add 1 immutable/offline copy and 0 restore errors: 3-2-1-1-0).
- **When / how:** Proxmox Backup Server + off-site copy; **test restores regularly** — an untested backup is a hope, not a backup.
- **Related:** RPO, DR, Ransomware, Immutable backup.

### Toil

- **What:** Manual, repetitive operational work that scales with load and has no lasting value.
- **When / how:** Measure and automate it away (SRE principle).
- **Related:** Automation, SRE, Runbook.

---

## 9. Cost and governance

### FinOps — Financial Operations

- **What:** Practice of making cost visible and shared between engineering, finance and business.
- **When / how:** Cost estimates per PR (Infracost), tagging resources, monthly reviews.
- **Related:** TCO, CAPEX/OPEX, Capacity planning.

### Compliance / Governance

- **What:** Compliance = meeting laws, regulations and standards (ISO 27001, PCI DSS, local data-protection law). Governance = the rules and decision rights for how IT is run.
- **When / how:** Constraints and NFRs in the design; evidence through audit trails, policies as code, reviews.
- **Related:** Audit trail, Policy as code, ARB, CAB.

### Policy as code

- **What:** Rules written as code and enforced automatically (OPA/Rego, Checkov, Tailscale ACLs).
- **Related:** Compliance, CI/CD, Quality gate.

### Risk register

- **What:** List of risks with likelihood, impact, owner and mitigation.
- **When / how:** Maintained during the project; top risks reported to stakeholders.
- **Related:** Assumption, SPOF, Threat model.

---

## 10. Git and collaboration (summary)

Details in the [Git handbook](../git/README.md).

| Term | Full name / meaning | Where |
|------|---------------------|-------|
| **PR / MR** | Pull Request (GitHub) / Merge Request (GitLab) — proposal to merge a branch, with review and checks | [Git 11](../git/11-github-workflow.md) |
| **main / master / trunk** | Primary long-lived branch | [Git 14](../git/14-branching-strategies-and-environments.md) |
| **GitHub Flow / GitFlow / Trunk-based** | Branching strategies | [Git 14](../git/14-branching-strategies-and-environments.md) |
| **Conventional Commits** | Commit message convention `type(scope): description` | [Git 11](../git/11-github-workflow.md) |
| **CODEOWNERS** | File mapping paths to mandatory reviewers | [Git 11](../git/11-github-workflow.md) |
| **Squash merge** | Combine a PR's commits into one commit on `main` | [Git 03](../git/03-branching-merging.md) |
| **Shift left** | Catch problems earlier (pre-commit, PR checks) | [Git 10](../git/10-advanced.md) |
| **Tag / Release** | Named pointer to a commit / packaged version with notes | [Git 09](../git/09-tags-and-releases.md) |
