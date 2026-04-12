# Audit DB Migration

**Status:** Critical Priority  
**Pillar:** Exchange Platform Architecture  
**Started:** 2026-03-02  
**Target:** TBD  
**Owner:** Marten Engblom  

---

## Overview

Critical database migration work following Audit DB incident. Top priority until "done."

Related Confluence: [Post AuditDB Incident Brainstorming Session](https://prd.hub.ghx.com/wiki/spaces/EX/pages/997326849/Post+AuditDB+Incident+Brainstorming+Session)

---

## Critical Decisions Needed

### 1. Firm Decision on Plan & Approach
- **Which route:** Sharding or cluster splitting?
- **Who does what** for application improvements above the cutline?
  - Jira stories required
  - Effort / ETA estimates required

### 2. Test Plan (Must Be Detailed)
Build confidence for ourselves and management:

- **PERF Testing:**
  - How are we testing this in PERF?
  - What is the delta between PROD and PERF?
  - How do we explain we cannot fully replicate PROD issues?
  - How do we bridge that gap?

- **Metrics & Indicators:**
  - What metrics will we watch in PERF testing?
  - With benefit of hindsight, what should we have paid attention to last time?
  - Define success criteria BEFORE testing

- **Green vs Red Results:**
  - What constitutes green test results?
  - What constitutes red test results?
  - Document criteria upfront

### 3. Impact to Atlas Migration Schedule
- Roadmap impact
- Cost impact

---

## Tasks

- [ ] Finalize decision: sharding vs. cluster splitting
- [ ] Create Jira stories for application improvements
- [ ] Estimate effort/ETA for all application work
- [ ] Write detailed test plan
- [ ] Document PERF vs PROD deltas
- [ ] Define success metrics for PERF testing
- [ ] Define green/red test criteria
- [ ] Assess impact to Atlas migration schedule
- [ ] Update Atlas migration cost estimates
- [ ] Answer outstanding questions in Confluence brainstorming doc

---

## Meeting History

- [[2026-03-02 14.38 - Audit DB Migration Recommendations + Look ahead]]
- [[2026-03-06 12.53 - Touchbase on DB Migration]]
- [[2026-03-09 15.37 - Audit DB Migration Recommendations - Follow-up]]
- [[2026-03-10 14.50 - Audit DB Migration Recommendations - Finalize]]
- [[2026-03-11 16.55 - 2026-03-11 Audit DB - Atlas Migration Update]]
- [[2026-03-12 16.02 - Atlas Mig Mongo Schedule Review]]
- [[2026-03-25 14.37 - Accelerate database migration]]

---

## Related Projects

- [[Exchange_Architecture_Transformation]] - DB depressurization is critical enabler for service extraction

## Stakeholders

- [[CJ_Singh]] - Asking for urgency and clarity
- [[Curtis_Nielsen]] - Org alignment
- [[Daniel_Milburn]] - Technical lead

---

## Status Updates

*Track key decisions and progress here*

---

## Related Correspondence

- [[Email regarding Audit DB migration]]
- [[DB Migration Touchbase Email]]
- [[Prep for Touchbase on DB Migration]]
