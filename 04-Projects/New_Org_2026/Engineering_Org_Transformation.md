# Engineering Org Transformation

**Status:** Active  
**Pillar:** Engineering Organization  
**Started:** 2026-02-27  
**Goal:** Transform Exchange organization into autonomous teams with independent release capabilities

---

## Vision

### How We Want to Operate
- Release small parts of the system independently, with little or no coordination
- Release very often with very low risk

### Target System Architecture
- Small encapsulated services
- Loosely coupled services
- Fault tolerant services - small blast radius
- No shared release dependencies

### Target Team Structure
Teams that can make decisions autonomously:
- Build It
- Test It
- Deploy It
- Operate It
- Evolve It

**Result:** Autonomy, Mastery & Purpose

---

## Current State - The Vicious Cycle

1. Monolithic Code Base
2. Massive Blast Radius
3. Extended Testing Cycles
4. Monthly Releases Only
5. Changes Batch Up
6. Even More Testing Required

### The Cost

**For Product, Stakeholders & Customers:**
- Slow time to market
- Long feedback cycles

**For Engineering Teams:**
- Lack of autonomy
- Coordination overhead
- Testing burden

---

## Strategy

### Reverse Conway Maneuver
Form teams and give them ownership of parts of the system

### Team Goals
1. Decouple
2. Encapsulate (compute, storage, infra)
3. Take ownership of their testing
4. Take ownership of their releases

### Team Strategies
- Use the Strangler Pattern (not big-bang rewrites)
- Take ownership of your data
- Don't start with the hardest or most central part
  - "It's like untying a knot - you can't start with the core"

---

## Success Metrics

- **Deployment frequency** - How often teams can deploy
- **Lead time to change** - Time from commit to production
- **Compliance to SLOs** - Higher resiliency (scalability, stability, fault tolerance, security)
- **Cost reduction** - Labor and infrastructure efficiency

---

## Key Principles

- Large releases with lots of testing are actually riskier than small releases with little testing
- Large releases are hard to release AND hard to roll back
- If a service still requires constant coordination, shared releases, or shared DB changes, it's probably not a real boundary
- Decoupling a monolith is like untying a knot - it gets easier and easier
- For true autonomy, teams need:
  - Dedicated EM (hands-on, committing code)
  - Dedicated Product Owner
  - Full-stack engineers

---

## Organization Design

See [[New Exchange Org Structure]] (2026-03-30 meeting with [[CJ_Singh]] and [[Curtis_Nielsen]])

### Key Requirements from Leadership
1. **Frame as outcomes**
   - Higher resiliency (measured by SLO compliance)
   - Higher speed (deployment frequency, lead time)
   - Lower cost (labor + infrastructure)

2. **What's Different Now**
   - EMs are hands-on (committing code to production)
   - [Additional differentiators to be documented]

3. **Target Architecture**
   - Define what's top-down vs. what's left to teams

4. **Team Accountability**
   - Each team writes down what they're accountable for
   - Clear service metrics
   - Adoption metrics (e.g., "Is everyone using our SSO solution?")

---

## Tasks

- [ ] Add slide on hands-on EM expectation to All Hands deck
- [ ] Add Goals/Objectives slide after slide 15 or 20
- [ ] Document reasons for org exceptions (Mike/Aaron reporting structures)
- [ ] Align EM expectations with Eric's AI team model
- [ ] Define "hands-on" clearly (commit code to production)
- [ ] Create 1-pager summarizing outcomes and what's different
- [ ] Document target architecture (top-down vs. team-level decisions)
- [ ] Clarify alignment with Infrastructure (Aaron & [[Arshad_Mahammad]])
- [ ] Clarify alignment with Product
- [ ] Confirm: No non-engineering roles in Engineering org
- [ ] Each team documents their accountability, service metrics, adoption metrics

---

## Related

**Connected Project:**
- [[Exchange_Architecture_Transformation]] - Technical platform side of transformation (autonomous deployments, breaking monolith)

**Stakeholders:**
- [[CJ_Singh]] - Executive sponsor
- [[Curtis_Nielsen]] - Org design partner
- [[Aaron_Srivastava]] - Developer Platform & AI Enablement lead
- [[Arshad_Mahammad]] - Infrastructure alignment
