---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  h1 {
    color: #2c3e50;
  }
  h2 {
    color: #34495e;
  }
---

<!-- _class: lead -->

# Building a World-Class Engineering Organization

## New Exchange Team Structure & Strategy

**Q1 2026**

<!--
Speaker Notes:
- Welcome everyone
- Today we're going to talk about an exciting transformation
- This is about setting us up for success in the future
-->

---

## Why We're Here Today
### The Challenge: Our Current State

- **We're moving too slowly**
  - Monthly releases with batched changes
  - Poor deployment frequency and lead time for changes

- **Monolithic codebase constraining multiple teams**
  - Shared release processes and dependencies
  - Extensive coordination overhead

- **Heavy testing cycles** due to deployment risk
  - Entire monolith requires regression testing
  - Brittle UI-layer end-to-end integration tests

- **Competing priorities from multiple sources**
  - Shifting marching orders, unclear prioritization

- **Growing backlogs:** incidents, vulnerabilities, technical debt

<!--
Speaker Notes:
- Let's be honest about where we are
- These aren't people problems - they're systems problems
- Engineers deserve better, and so do our customers
-->

---

## Understanding the Root Cause
### The Vicious Cycle

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  Monolithic Codebase                                    │
│         ↓                                               │
│  Massive Blast Radius                                   │
│         ↓                                               │
│  Extended Testing Cycles                                │
│         ↓                                               │
│  Monthly Releases Only                                  │
│         ↓                                               │
│  Changes Batch Up                                       │
│         ↓                                               │
│  Even More Testing Required                             │
│         ↓                                               │
│  (Cycle repeats, getting worse)                         │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

> **"We can't test our way out of this problem"**

<!--
Speaker Notes:
- This is a reinforcing loop
- Each iteration makes the problem worse
- The only way out is to break the cycle at the root cause
-->

---

## The Cost of Our Current State
### What This Means for Teams & Products

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2em;">

<div>

### For Engineering Teams
- Slow feedback loops
- Difficult to own & improve specific areas
- Coordination overhead
- Hard to be a "player-coach"
- **Lack of autonomy**

</div>

<div>

### For Products & Customers
- Poor deployment frequency
- Long lead time for changes
- Slow incident remediation
- Delayed security fixes
- Can't respond quickly to customer needs

</div>

</div>

<!--
Speaker Notes:
- Connect technical problems to human impact
- This affects both team morale and customer satisfaction
-->

---

## The Vision: Autonomous Teams
### Where We're Going

**Core Principle: Autonomy, Mastery, Purpose** _(Daniel Pink)_

### Our Target State:
- **Autonomous teams** with clear ownership boundaries
- Teams **build, deploy, and operate independently**
- Well-defined, **loosely coupled** areas of ownership
- **Player-coach Engineering Manager** per team (6-8 engineers)
- Clear product partnership per team
- **Teams can ship on their own cadence**

_Visual: Independent team units vs. current monolithic dependency web_

<!--
Speaker Notes:
- This is what world-class engineering orgs look like
- Autonomy leads to faster delivery and better morale
- Clear ownership means accountability and pride in work
-->

---

## Strategic Foundation
### Reverse Conway Maneuver

> _"Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations."_
>
> — **Conway's Law**

### Our Approach:
- **Reverse Conway Maneuver:** Structure teams around our **target architecture**
- Shape team boundaries to match the system design we want
- Enable incremental monolith breakup
- Each team owns clear domain boundaries

### This Creates:
✓ Teams that can deploy independently
✓ Reduced coordination overhead
✓ Natural path to service-oriented architecture

<!--
Speaker Notes:
- We're not just reorganizing people - we're aligning to where we want the architecture to go
- This is a proven pattern used by successful engineering orgs
-->

---

## New Team Topology
### Domain Teams + Enabling Teams

<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 2em;">

<div>

### Domain-Based Product Teams
- Clear ownership of business capabilities
- **Full-stack ownership** (build + run)
- **1 Engineering Manager per team** (player-coach)
- Dedicated technical leadership
- Product partnership
- Own Jira board & backlog

</div>

<div>

### Enabling Teams
**Developer Platform & AI Enablement**
- CI/CD, tooling
- AI development practices
- Embed with teams

**Data Architecture & Engineering**
- Database optimization
- Data architecture patterns

</div>

</div>

<!--
Speaker Notes:
- Domain teams own business outcomes end-to-end
- Enabling teams help product teams be more effective
- Everyone has clear roles and responsibilities
-->

---

## What This Means for You
### How Teams Will Operate

### Your Team Will Have:
- ✓ Dedicated Engineering Manager (player-coach)
- ✓ Clear ownership boundaries & mission
- ✓ Technical leadership (Principal/Staff engineers)
- ✓ Product partnership
- ✓ Your own Jira board & backlog

### Your Team Will:
- ✓ Own the full lifecycle: **build → deploy → operate**
- ✓ Make decisions locally within your domain
- ✓ Prioritize work with your product partner
- ✓ Work in **protected sprints**
- ✓ Define and hit your own sprint goals

**Protected Time:** No unplanned work mid-sprint

<!--
Speaker Notes:
- This is about empowering YOU
- Clear ownership means you can make decisions
- Protected sprints mean you can focus and deliver
-->

---

## How We'll Work Together
### Improved Ways of Working

### Single Source of Truth:
- **All work in Jira** (commercial, defects, incidents, vulnerabilities, tech debt)
- Single prioritization against one backlog
- **100% work visibility**

### Agile Best Practices:
- **Agile Maturity Model** baseline and continuous improvement
- Sprint goals with clear outcomes
- Better sprint reviews (more engaging, more celebration)
- Retrospectives that drive real improvements

### Engineering-Product Partnership:
- Monthly shared roadmap review
- Clear initiative tracking
- Transparent prioritization

<!--
Speaker Notes:
- No more shadow work or competing priorities
- Everyone can see what's important and why
- Product and Engineering working as partners
-->

---

## Technology Evolution
### Breaking Free from the Monolith

### Near-Term (Q1-Q2 2026):
- Test automation improvements (Tandori → Playwright)
- MongoDB Atlas migration (2 of 4 databases)
- Database fleet assessment
- AI-native development tools adoption

### Strategic Initiative:
**Service-Oriented Architecture POC**
- Carve out one component from monolith
- Rebuild as cloud-native, standalone service
- Demonstrate: clear ownership, independent deployment, operational readiness

### The Long Game:
Incremental monolith breakup, one service at a time

<!--
Speaker Notes:
- We're not boiling the ocean
- Quick wins + strategic moves + long-term vision
- Each step makes the next one easier
-->

---

## Q1 2026 Focus & OKRs
### What Success Looks Like This Quarter

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 1em; font-size: 0.85em;">

<div>

### Objective 1
**World-Class Product-Centric Org**

✓ Target team topology with 100% coverage
✓ All teams have critical roles defined
✓ Agile Maturity Model baseline
✓ AI development tools access for 100% of engineers

</div>

<div>

### Objective 2
**Better Product/Value Delivery**

✓ Single shared roadmap
✓ 100% work visibility in Jira
✓ Service-oriented architecture POC
✓ Increase deployment frequency

</div>

<div>

### Objective 3
**Better Stability & Reliability**

✓ Exchange Health Score defined
✓ 2 MongoDB databases to Atlas
✓ Critical vulnerability remediation (100% SLA)
✓ Incident root cause dashboard

</div>

</div>

<!--
Speaker Notes:
- These are measurable, achievable goals
- Each objective supports the overall transformation
- We'll track progress transparently
-->

---

## What Happens Next
### Your Next Steps

### Immediate (This Week):
- ✓ Team assignments announced
- ✓ Meet with your new Engineering Manager
- ✓ Understand your team's ownership boundaries

### Coming Soon (Next 2-4 Weeks):
- ✓ Team mission statements & ownership documentation
- ✓ Jira board setup for your team
- ✓ Agile Maturity Model assessment
- ✓ AI development tools onboarding

### Ongoing:
- ✓ Sprint planning in your team boundaries
- ✓ Regular sprint reviews & retrospectives
- ✓ Monthly roadmap alignment
- ✓ Quarterly OKR reviews

**Questions?** Open forum for discussion

<!--
Speaker Notes:
- Change can feel uncertain - these steps provide clarity
- You're not alone in this transition
- Open for questions and discussion
-->

---

<!-- _class: lead -->

# Appendix

## Deep Dive Materials

---

## Appendix A: The Monolith Problem (Detailed)
### Technical Architecture Challenges

### Root Cause: Monolithic Codebase
- Single, tightly-coupled codebase with extreme dependencies
- Shared databases where many system components access the same data
- **Forces monolithic deployment** — any change deploys the entire application

### Initial Impact: Massive Blast Radius
- Every deployment affects the entire system, even for small changes
- Enormous surface area to test
- Multiple engineers touching same codebase increases merge conflicts
- Hidden dependencies create unknown side effects
- Steep learning curve creates uncertainty about change impacts

### Defensive Response: Extended Testing Cycles
- Large blast radius forces very careful, lengthy testing processes
- Difficulty achieving trusted automated test coverage
- Heavy reliance on manual, time-intensive testing
- **High consequences of failure** — rolling back or fixing monolithic deployments is difficult and risky

---

## Appendix B: Team Ownership Model Details
### Clear Boundaries and Responsibilities

### Ownership Dimensions:
1. **Business Domain** — Which business capabilities does the team own?
2. **Systems & Services** — Which applications, services, and components?
3. **Data** — Which databases, schemas, and data models?
4. **APIs & Integrations** — Which endpoints and external integrations?

### Responsibility Model:
- **Build:** Design, develop, and test new features
- **Run:** Deploy, monitor, and operate in production
- **Evolve:** Refactor, upgrade, and improve over time
- **Support:** Respond to incidents and customer issues in your domain

### Crystal Clear Ownership:
Each team will have documented:
- Mission statement
- System/component inventory
- Domain boundaries (what's in, what's out)
- Interface contracts with other teams
- Escalation paths

---

## Appendix C: Agile Maturity Model Framework
### Measuring and Improving Our Process

### Key Dimensions:
1. **Sprint Discipline** — Planning, reviews, retrospectives, protected sprint time
2. **Product Partnership** — Collaboration, roadmap alignment, prioritization
3. **Testing & Quality** — Automated testing, test coverage, quality gates
4. **Deployment & Release** — Frequency, automation, rollback capability
5. **Monitoring & Observability** — Instrumentation, alerting, incident response
6. **Technical Excellence** — Code review, documentation, tech debt management

### Maturity Levels (1-5):
- **Level 1:** Ad-hoc, inconsistent
- **Level 2:** Repeatable, some structure
- **Level 3:** Defined, standard process
- **Level 4:** Managed, measured & controlled
- **Level 5:** Optimizing, continuous improvement

### Approach:
- Baseline assessment for all teams in Q1
- Team-specific improvement plans
- Quarterly reassessment
- Share learnings across teams

---

## Appendix D: Success Metrics & Health Score
### How We'll Measure Progress

### DORA Metrics:
- **Deployment Frequency** — How often do we deploy to production?
- **Lead Time for Changes** — Time from commit to production
- **Change Failure Rate** — % of deployments causing failures
- **Time to Restore Service** — Mean time to recover from incidents

### Exchange Health Score Components:
- **Availability** — Uptime and reliability
- **Incident Frequency** — Number and severity of incidents
- **Incident Resolution** — Time to resolve and root cause analysis completion
- **Performance** — Response times, throughput, SLO compliance
- **Security Posture** — Vulnerability remediation SLAs, security scan results
- **Technical Health** — Test coverage, deployment frequency, tech debt tracking

### Metrics Visibility:
- **Team-level metrics** — For teams to track their own improvements
- **Org-level metrics** — For overall Exchange platform health
- **Public dashboards** — Transparent visibility to all stakeholders

---

<!-- _class: lead -->

# Thank You

## Questions & Discussion

**Let's build something great together.**
