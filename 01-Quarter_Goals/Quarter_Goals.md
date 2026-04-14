# Q2 2026 Goals (Apr 1 - Jun 30, 2026)

**Status:** Draft (targets pending for security and release cadence KRs)  
**Owner:** [[Marten_Engblom]]  
**Team:** Engineering - Automation / Exchange (L4)

---

## Objective 1: Reduce Exchange Security Risk Exposure

**Objective ID:** 2949683  
**Progress:** 0%

### Key Results

1. **Reduce security risk by reducing critical and high vulnerabilities outside of SLA from X to Y**
   - Owner: [[Marten_Engblom]]
   - Current: 100 → Target: 0
   - Update Frequency: Weekly
   - Progress: 100 of 0

2. **Reduce risk by decreasing the number of repos not using GHX artifact repository from X to Y**
   - Owner: [[Marten_Engblom]]
   - Current: 100 → Target: 0
   - Update Frequency: Weekly
   - Progress: 100 of 0

---

## Objective 2: Increase Exchange Uptime and Availability (Resiliency)

**Objective ID:** 2949635  
**Progress:** 0%

### Key Results

1. **Improve Exchange Resiliency by decreasing database clusters (lower and prod) operating in hosted environments from 20 to 10** (Migrate databases to Atlas)
   - Owner: [[Marten_Engblom]]
   - Current: 20 → Target: 10
   - Update Frequency: Weekly
   - Progress: 20 of 10

2. **Improve Exchange Resiliency by increasing distinct deployments from 4 to 7 across tech apps and products** (Increase modularity)
   - Owner: [[Marten_Engblom]]
   - Current: 4 → Target: 7
   - Update Frequency: Weekly
   - Progress: 4 of 7

3. **Improve Exchange Resiliency by adding 5 Service Level Objectives (SLOs) and reporting that measure the availability of services** (Improve observability)
   - Owner: [[Marten_Engblom]]
   - Current: 0 → Target: 5
   - Update Frequency: Weekly
   - Progress: 0 of 5

4. **Improve Exchange Resiliency by completing 1 DR test in a lower environment and showing an improvement in measured RTO/RPO** (Preparation for Q4 production failover test)
   - Owner: [[Daniel_Milburn]]
   - Current: 0 → Target: 1
   - Update Frequency: Weekly
   - Progress: 0 of 1

5. **Improve Ability to always deliver orders by testing and defining RTO/RPO of the continuity assurance solution** (Industry continuity solution)
   - Owner: [[Ramesh_Rangavithal_Donnipadu]]
   - Current: 0 → Target: 1
   - Update Frequency: Weekly
   - Progress: 0 of 1

---

## Objective 3: Improve the Exchange Release Cadence

**Objective ID:** 2949689  
**Progress:** 0%

### Key Results

1. **Increase revenue by reducing the lead time to change from X to Y days to deliver updates to customers quicker**
   - Owner: [[Marten_Engblom]]
   - Current: 30 → Target: 29
   - Update Frequency: Weekly
   - Progress: 30 of 29

2. **Increase revenue by improving deployment frequency from X to Y per month to deliver more capabilities to customers quicker**
   - Owner: [[Marten_Engblom]]
   - Current: 5 → Target: 10
   - Update Frequency: Weekly
   - Progress: 5 of 10

3. **Reduce the average age of open PRs from X to Y**
   - Owner: [[Marten_Engblom]]
   - Current: 100 → Target: 10
   - Update Frequency: Weekly
   - Progress: 100 of 10

---

## Operational Priorities (Bottom-Up)

**These foundational initiatives enable the formal OKRs above and are equally critical to quarter success.**

### 1. The Organization
**Enables:** All objectives (team capacity is foundational)

- **Fill remaining open roles** — Critical: Principal Data Engineer (Jeff Sherard candidate identified)
- **Onboarding** — Ensure everyone understands vision, priorities, and how their work connects to OKRs
- **Team domain understanding** — Meet with each team to understand their boundaries and domain better

### 2. Exchange Architecture
**Enables:** Resiliency Objective (modularity, observability)

- **Define domain boundaries** — Clear team ownership enables "distinct deployments" KR
- **Define Vision / Target Architecture** — North star for all technical decisions
- **Prioritize foundational/cross-org work:**
  - **Events/Messaging/Service Bus** — Architecture pattern for decoupling
  - **Observability (opinionated approach)** — Directly enables "5 SLOs" KR

### 3. Agile Process Improvements
**Enables:** Release Cadence Objective (lead time, deployment frequency)

#### Intake
- **Everything in Jira** — Single source of truth for all work:
  - Commercial work from Product intake
  - Technical initiatives
  - Vulnerabilities (OSS, VMs)
  - Customer reported defects
  - Incident remediations

#### Visibility
- **Automate Jira ↔ Aha connection:**
  - Define hierarchy: Stories/Epics (eng teams) → Initiative (exec roadmaps)
  - Enable executive reporting without manual reconciliation
- **Create dashboards** for monthly/quarterly company reporting

#### Unplanned Work
- **Respect sprint sanctity** — Too much unplanned work erodes velocity
- **Track and quantify** — Report unplanned work per sprint/quarter
- **Distinguish emergent from unplanned** — Different root causes require different solutions

---

## How They Connect

| Operational Priority | Enables OKR |
|---------------------|-------------|
| Observability (opinionated approach) | Add 5 SLOs (Resiliency KR #3) |
| Domain boundaries + Architecture | Increase deployments 4→7 (Resiliency KR #2) |
| Intake + Visibility | Reduce lead time, increase deploy frequency (Release Cadence) |
| Team meetings + Onboarding | All objectives (foundational) |
| Unplanned work tracking | Release Cadence (removes velocity drag) |

---

## Notes

- **Security KRs:** Baseline numbers (X values) need to be confirmed before WorkBoard entry
- **Release Cadence KRs:** Baseline numbers (X values) need to be confirmed before WorkBoard entry
- **All KRs** set to weekly update frequency in WorkBoard
- **Delegated KRs:** DR testing (Daniel), Continuity assurance (Ramesh)
- **Priority philosophy:** Formal OKRs are top-down commitments; Operational priorities are bottom-up enablers. Both are equally important.
