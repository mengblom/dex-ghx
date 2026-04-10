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
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

<!-- _class: lead -->

# Building Autonomous Engineering Teams

## New Exchange Organization Structure

**Q1 2026**

---

## Why We Are Here Today

### We Are Moving Too Slowly
- Monthly releases
- Huge batched changes
- 2+ week testing cycles

### It All Comes Back to the Monolith
- Difficult code base
- Lots of dependencies
- Unpredictable side effects
- Difficult to test individual components

<!--
Speaker Notes:
- We need to be honest about where we are
- These are system problems, not people problems
- The monolith constrains us
-->

---

## Why We Are Here Today (continued)

### The Vicious Cycle

- Huge releases
- Lots of end-to-end / UI tests (brittle, difficult to maintain)
- Very long test cycles
- Leads to even larger releases
- **Vicious cycle**

> We can't test our way out of this problem

<!--
Speaker Notes:
- Each iteration makes the problem worse
- The only way out is to break the cycle
- Need architectural change, not just process change
-->

---

## The Cost of Our Current State

<div class="columns">

<div>

### For Engineering Teams
- Slow feedback loops
- Things that should be easy are now high risk and difficult
- Coordination overhead
- Lack of autonomy
- Difficult to prioritize and manage mixed work streams

</div>

<div>

### For Product & Customers
- Poor deployment frequency
- Long lead time for changes
- Slow incident remediation
- Delayed security fixes
- Cannot respond quickly to customer needs

</div>

</div>

<!--
Speaker Notes:
- Technical problems have real human and customer impact
- Affects both team morale and customer satisfaction
- This is why change is necessary
-->

---

## The Vision: Autonomous Teams

### Where We're Going

- Clear ownership boundaries
- Teams **build, deploy, and operate independently**
- Well-defined, **loosely coupled** areas of ownership
- Clear product partnership per team
- **Teams can ship on their own cadence**
- All work in one place (Jira)

<!--
Speaker Notes:
- This is what world-class engineering organizations look like
- Autonomy leads to faster delivery and better morale
- Clear ownership means accountability and pride
-->

---

## The Approach / Strategy

### Reverse Conway Maneuver

> _"Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations."_
> — **Conway's Law**

**What this means:** Systems tend to mirror team's ownership boundaries and how they communicate

**Our strategy:** Structure teams to match the architecture we want
- Clear team boundaries → Clear component boundaries
- Minimal cross-team coordination → Loose coupling
- Independent teams → Independent deployable services

<!--
Speaker Notes:
- Conway's Law: Your architecture inevitably mirrors your org structure
- Current state: Shared codebase = everyone talks to everyone = monolith
- Reverse Conway: Design org with clear boundaries first
- Teams with minimal dependencies will build systems with minimal dependencies
- We're using Conway's Law to our advantage, not fighting it
-->

---

## New Team Topology

<div class="columns">

<div>

### Product Teams (Stream-Aligned)
1. Exchange IO
2. Exchange Core
3. Exchange Analytics
4. Exchange Actions & Rules
5. Exchange Mapping
6. Exchange Customer Enablement
7. Exchange Document Understanding
8. Exchange Customer Visibility
9. Organizations Platform
10. Users Platform
11. Continuity Assure

</div>

<div>

### Enabling Teams
- Developer Platform & AI Enablement
- Data Architecture & Engineering

### Complicated Subsystem Teams
- Exchange Performance Environment

</div>

</div>

<!--
Speaker Notes:
- Product teams own business capabilities end-to-end
- Enabling teams help product teams be more effective
- Performance team handles specialized technical domain
-->

---

## Team Model / How Your Team Will Operate

### What This Means for You

1. **Dedicated EM (player-coach)**
   - Engineering Manager focused on your team

2. **Each team/product will have their own SDLC**
   - Own your delivery process

3. **Product partnership and agile ways of working**
   - Collaborative, iterative development

<!--
Speaker Notes:
- Clear ownership and accountability
- Flexibility to optimize your own processes
- Strong partnership between engineering and product
-->

---

## Coordination / Planning / Roadmaps / Product

### How We'll Work Together

- **Product and Engineering partnership model**
  - Still evolving, being established

- **Cross-team coordination where needed**
  - For dependencies and shared initiatives

- **All work visible in Jira**
  - Single source of truth for all work

<!--
Speaker Notes:
- We're establishing these patterns as we go
- Transparency is key
- No shadow work or hidden priorities
-->

---

## Initial Team Missions

### Your Team's First Objectives

1. **Work aggressively towards autonomy**
   - Break dependencies, own your domain

2. **Cloud native**
   - Modern cloud infrastructure and practices

3. **AI-native / agentic development**
   - Leverage AI tools for productivity

4. **Demonstrate: clear ownership, independent deployment, operational readiness**
   - Show you can build, ship, and run independently

<!--
Speaker Notes:
- These are the foundational goals for all teams
- Not optional - these enable everything else
- We'll support you in achieving these
-->

---

## Org Structure

### Leadership and Reporting

**Marten Engblom (Executive Director)**

- **Daniel Milburn** (Director, Engineering)
  - Exchange IO, Exchange Core, Exchange Analytics
  - Exchange Actions & Rules, Exchange Performance Environment

- **Mike Mitchell** (Sr. Engineering Manager)
  - Organizations Platform, Users Platform

<!--
Speaker Notes:
- Clear reporting structure
- Narrower spans for deeper engagement
- Directors can focus on specific domains
-->

---

## Org Structure (continued)

**Marten Engblom (Executive Director)**

- **Ramesh Donnipadu** (Director, Engineering)
  - Exchange Mapping, Exchange Customer Enablement
  - Exchange Document Understanding, Exchange Customer Visibility
  - Continuity Assure

- **New Hire** (Director, Developer Platform & AI Enablement)

- **New Hire** (Principal Engineer, Data Architecture & Engineering)

<!--
Speaker Notes:
- Enabling teams being built out
- Critical hires to support transformation
- Platform and data expertise to accelerate teams
-->

---

## Org Structure: Rationale

### Why This Structure?

- **Bigger and deeper changes** than just KTLO
- **More audacious goals** require focus

### What This Enables:
- **One EM per team** - dedicated leadership
- **Narrower Director responsibilities** - deeper engagement
- **Help from enabling teams** - platform support

<!--
Speaker Notes:
- Not just maintaining the status quo
- Real transformation requires dedicated focus
- Enabling teams multiply effectiveness
-->

---

## Immediate Steps / What Happens Next

### Teams Are Forming NOW

- Some teams **already partially staffed** (existing employees)
- Some teams **building from scratch** (EM + senior ICs first)
- **All teams begin autonomy work immediately**

> We're not waiting. The transformation starts today.

<!--
Speaker Notes:
- This isn't a future state - it's happening now
- You may already know your team assignment
- Work begins immediately, in parallel with existing commitments
-->

---

## Immediate Steps / What Happens Next

### Aggressive Hiring Already in Progress

**40+ open roles:**
- Director of Engineering, Developer Platform & AI Enablement (US)
- Principal Engineer, Data Architecture & Engineering (US)
- Engineering Manager (4 US, 5 India)
- Staff Engineer (2 US, 2 India)
- Senior Engineer (2 US, 11 India)
- Engineer III (3 US, 5 India)
- Engineer II (4 US, 5 India)
- QA III (1 India)
- QA II (1 India)

<!--
Speaker Notes:
- Significant investment in team growth
- Prioritizing leadership and senior technical roles
- Help us spread the word
-->

---

## Immediate Steps / What Happens Next

### Dual Track Approach

1. **Continue delivering on existing commitments**
   - Business as usual work continues
   - Customer commitments remain priorities

2. **Work towards autonomy in parallel**
   - Cloud native
   - Independent deployment
   - Operational ownership

> We deliver value while we transform

<!--
Speaker Notes:
- Not a "stop the world" reorganization
- Both tracks matter
- This is hard but achievable
-->

---

<!-- _class: lead -->

# Questions?

## Let's build something great together

<!--
Speaker Notes:
- Open floor for questions
- Address concerns and clarifications
- This is a conversation, not a decree
-->
