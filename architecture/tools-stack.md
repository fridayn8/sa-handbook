# Tools Stack — Options and Choices

For each category: common options in the industry, **the choice made in the Example Corp case**, its
**licence**, and why. Guiding principles:

- **Everything as code**, rendered on GitHub, verified automatically in CI.
- **Free only** — [ADR-0010](https://github.com/fridayn8/sa-case-studies/blob/main/case-01-example-corp/02-options-decisions/adr/0010-free-only-tooling-policy.md).
- **Open source first** — [ADR-0011](https://github.com/fridayn8/sa-case-studies/blob/main/case-01-example-corp/02-options-decisions/adr/0011-open-source-first.md). Exceptions are the
  platform services chosen by the owner (Proxmox, OPNsense, WireGuard, Tailscale, Cloudflare)
  and GitHub as the code platform; each has a documented open-source fallback.

Legend: 🟢 open source · 🟡 owner-chosen service (proprietary or open-core) with OSS fallback

## Documentation & design

| Category | Common options | Choice | Licence | Why |
|----------|----------------|--------|---------|-----|
| Documents | Markdown, AsciiDoc, Confluence, Notion | **Markdown** | 🟢 open format | Renders on GitHub, reviewable in PRs, portable |
| Docs website | MkDocs Material, Docusaurus, Backstage TechDocs | **MkDocs Material** | 🟢 MIT | Light, Mermaid support |
| Decision records | adr-tools, Log4brains, MADR | **MADR template** | 🟢 CC0/MIT | Standard format, plain Markdown |
| Diagrams | Mermaid, PlantUML, Structurizr, `diagrams` (Python), draw.io | **Mermaid** (+ C4-PlantUML when needed) | 🟢 MIT | Native GitHub rendering |
| Threat modelling | OWASP Threat Dragon, MS Threat Modeling Tool, STRIDE in Markdown | **STRIDE in Markdown** (Threat Dragon optional) | 🟢 Apache-2.0 | Simple, versioned, reviewable |

## Infrastructure

| Category | Common options | Choice | Licence | Why |
|----------|----------------|--------|---------|-----|
| Hypervisor | Proxmox VE, VMware ESXi, Hyper-V, XCP-ng | **Proxmox VE** | 🟢 AGPL-3.0 | KVM + LXC, good API (owner's choice) |
| Lab hypervisor (laptop) | VirtualBox, VMware Workstation, Hyper-V, KVM/virt-manager | **VirtualBox** (fallback Hyper-V/VMware) | 🟢 GPL-3.0 (base package) | Open source, runs on Windows/macOS/Linux |
| Firewall / router | OPNsense, pfSense, MikroTik, Proxmox firewall | **OPNsense** | 🟢 BSD-2-Clause | API, plugins, built-in WireGuard (owner's choice) |
| Site-to-site / fallback VPN | WireGuard, IPsec, OpenVPN | **WireGuard** | 🟢 GPL-2.0 | Fast, small, modern crypto (owner's choice) |
| Admin remote access | Tailscale, Headscale, ZeroTier, NetBird, plain WireGuard | **Tailscale** (fallback **Headscale**) | 🟡 client BSD-3, SaaS control plane | SSO, ACLs as code (owner's choice) |
| Public ingress & DNS | Cloudflare, port-forward + reverse proxy | **Cloudflare** (`cloudflared` Apache-2.0) | 🟡 SaaS | No inbound ports, Zero Trust Access (owner's choice) |
| Guest OS | Debian, Ubuntu, Rocky Linux | **Debian 13** | 🟢 DFSG | Stable, minimal, official cloud images |

## Automation

| Category | Common options | Choice | Licence | Why |
|----------|----------------|--------|---------|-----|
| Provisioning (IaC) | Terraform, OpenTofu, Pulumi, CDK, Bicep | **OpenTofu** | 🟢 MPL-2.0 | Open-source Terraform-language tool, state encryption ([ADR-0012](https://github.com/fridayn8/sa-case-studies/blob/main/case-01-example-corp/02-options-decisions/adr/0012-opentofu-and-cloud-image-templates.md)) |
| Providers | — | `bpg/proxmox`, `cloudflare/cloudflare`, `tailscale/tailscale` | 🟢 MPL-2.0 | Actively maintained |
| VM templates | Packer, cloud images, virt-customize | **Official Debian cloud image + OpenTofu** | 🟢 | No image-build tool needed |
| Configuration management | Ansible, Salt, Chef, Puppet | **Ansible** | 🟢 GPL-3.0 | Agentless, YAML, one baseline for VMs and LXCs |
| Secrets in Git | SOPS + age, Ansible Vault, git-crypt, OpenBao | **SOPS + age** | 🟢 MPL-2.0 / BSD-3 | Encrypts values only |
| State storage | Local, HCP Terraform, S3, Cloudflare R2, GitLab | **Cloudflare R2** + OpenTofu encryption | 🟡 SaaS (free tier) | Off-site, free, state encrypted by us |
| Code platform & CI | GitHub, GitLab, Forgejo + Woodpecker | **GitHub + GitHub Actions** (fallback Forgejo) | 🟡 SaaS | Owner's platform |
| Reaching the lab from CI | Self-hosted runner, Tailscale GitHub Action | **Both (compare in a PoC)** | 🟢 runner MIT | Cloud runners cannot reach a private network |

## Quality & security gates

| Category | Common options | Choice | Licence | Why |
|----------|----------------|--------|---------|-----|
| Local hooks | pre-commit, Husky, lefthook | **pre-commit** | 🟢 MIT | Language-agnostic |
| Secret scanning | gitleaks, trufflehog, GitHub secret scanning | **gitleaks** | 🟢 MIT | Runs locally and in CI |
| IaC lint / security | tflint, Checkov, Trivy | **tflint + Checkov** | 🟢 MPL-2.0 / Apache-2.0 | Quality + security coverage |
| Module docs | terraform-docs | **terraform-docs** | 🟢 MIT | Auto-generated module READMEs |
| Policy as code | OPA/Conftest, Sentinel, Kyverno | **OPA/Conftest** | 🟢 Apache-2.0 | Works on any structured config |
| Markdown lint | markdownlint | **markdownlint** | 🟢 MIT | Consistent docs |
| Commit messages | commitlint, conventional-pre-commit | **conventional-pre-commit** | 🟢 Apache-2.0 | Enforces Conventional Commits |
| Dependency updates | Dependabot, Renovate | **Dependabot** | 🟢 MIT (core) | Built into GitHub |
| Releases | release-please, semantic-release | **release-please** | 🟢 Apache-2.0 | Changelog + SemVer tags |

## APIs, PoCs & operations

| Category | Common options | Choice | Licence | Why |
|----------|----------------|--------|---------|-----|
| API contracts | OpenAPI, AsyncAPI, Protobuf, GraphQL SDL | **OpenAPI 3.1 + AsyncAPI** | 🟢 open specs | Covers REST and events |
| API lint | Spectral, Redocly | **Spectral** | 🟢 Apache-2.0 | API style guides in CI |
| PoC runtime | Docker Desktop, Docker Engine, Podman, kind/k3d | **Docker Engine + Compose or Podman** (not Docker Desktop) | 🟢 Apache-2.0 | Open source; Docker Desktop is proprietary |
| PoC language | Go, Python, Java, TypeScript | **Python or TypeScript** | 🟢 | Fast to prototype |
| Cost | Infracost, cloud calculators, spreadsheets | **Markdown cost model** | 🟢 | Infracost prices only public clouds |
| Observability | OpenTelemetry, Prometheus, Grafana, Uptime Kuma | **Prometheus + Grafana OSS + Uptime Kuma**, OTel for apps | 🟢 Apache-2.0 / AGPL-3.0 / MIT | Open standards |
| External status page | SaaS status pages, Upptime | **Upptime** (GitHub Actions + Pages) | 🟢 MIT | Runs outside the office, free |
| Backup | Proxmox Backup Server, Veeam, restic | **Proxmox Backup Server** | 🟢 AGPL-3.0 | Native, incremental, deduplicated |
| Identity (lab) | Google/GitHub login, Keycloak, Authentik | **Existing account login**; Keycloak if self-hosting | 🟢 Keycloak Apache-2.0 | No extra service to run in the lab |
