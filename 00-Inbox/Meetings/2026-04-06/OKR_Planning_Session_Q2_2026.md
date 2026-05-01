# OKR Planning Session - Q2 2026

**Date:** 2026-04-06  
**Duration:** ~2 hours

## Summary

Comprehensive OKR planning session refining objectives and key results for Q2 2026. Focused on aligning work to three business outcomes (increase revenue, reduce costs, reduce risk) and ensuring engineering OKRs are measurable and outcome-based. Major themes: exchange resiliency, cybersecurity compliance, and delivery efficiency (reframed from "Jarvis"). Several KRs deprioritized or rewritten for clarity.

## OKR Philosophy & Structure

- **Goal:** align all communication and work to 3 business outcomes (deduced, not handed down)
  - Increase revenue
  - Reduce costs
  - Reduce risk
- **Current OKR rollup is broken** — groups write "cross-functional OKRs" and ping others, rather than each team owning their portion
- **Engineering work types** (Roger's framework): maintenance, tech debt, new features
  - Every story/epic should map to both a business outcome and a work type
  - Two pie charts as the reporting output
- **OKRs will sit at the pod level only** — no individual-level OKRs for now
  - Rollup to engineering manager level is aspirational but not working yet
  - Hiring OKR is appropriate to include (e.g., "15 of 11 roles hired" format worked well last quarter)

## Exchange Resiliency OKRs

**5 key areas under exchange resiliency** — these are full-year KRs, not Q1-only

### Observability
- **Target:** define and track 3–5 SLOs this quarter, get them on a status page
- Focus at API/service level only — not internal metrics like query times
- Start small: automate heartbeat reporting, wrap IO engine or notification engine
- Mental model: Obsidian-style status page expanded across exchange services
- **"Reduce mean time to detect" KR to be removed** — too premature

### Distinct Deployments
- Straightforward KR, no concerns

### Database Migration
- Straightforward KR, no concerns

### Disaster Recovery
- **RTO/RPO gap closure KR should be rewritten as an outcome:** "reduce recovery time from 13hrs to Xhr"
- Realistic target: Q3 at earliest (databases not yet working correctly)
- **DR test:** run a lightweight failover test in lower environment — target 4–8 hrs total effort
  - Happiest Minds team can run it; no hard dependency on new FTE hire
  - [[Ramesh_Unknown|Ramesh]] to reach out to Jenna to scope

## Cybersecurity OKRs

### Artifact Repository (JFrog)
- **Problem:** supply chain attack risk from unscanned open-source packages; also, internal libraries currently copied between repos manually
- JFrog instance exists but barely used
- **Better KR:** reduce number of repos not pulling from JFrog artifact repository to zero (with quarterly targets)
- Ownership: infrastructure owns the repo, works with security on scanning rules

### Container Registry
- Same concept — zero containers outside of registry
- Currently using ECS; XDP registry exists but maturity unclear
- Likely already compliant — needs a check before writing a KR

### Offshore Compliance
- **Removed from Q2 scope**
  - Can't comply given current architecture without major re-platforming
  - To be raised separately with Tina; other pods (Marketplace, Analysis) have handled it via data anonymization

## Delivery Efficiency OKRs (replacing "Jarvis" framing)

- **Reframe as a standing "improve delivery efficiency" objective** — not AI-specific
  - Applies to every pod area (credentialing, analysis, marketplace, etc.)
- **Core KRs:** lead time to change + deployment frequency (DORA metrics)
- **PR age as a potential third KR** — reduce PRs open >30 days
  - KPMD dashboard exists (built by Mike Mitchell + India team) but currently tracks time-to-approve, not time-to-deploy
  - Data collection may need adjustment before this KR is usable
- **Key constraint:** deployment frequency is bottlenecked by monthly monolith release cycle, not team throughput
  - "Distinct deployments" KR elsewhere already addresses this
- **AI productivity measurement:** pushing back on AI-specific metrics; normal delivery metrics are sufficient

## Items Deprioritized or Deferred

- **Complex order automation:** no known engineering backlog; Josh's team onboarding pilot customers away from engineering
  - Watch for reactive defects; [[Laura_Unknown|Laura]]'s team may already have this covered
- **Reducing customer friction / defect count:** framed as a product KR, not an engineering KR
  - MTTR here = customer resolution time, not system recovery time
- **"Offshore compliance" KR:** dropped (see above)

## WorkBoard & OKR Tooling

- WorkBoard is the mandated reporting tool but poorly organized — pod-level pages hard to find
- Automation pod page exists but permissions/visibility issues for Mårten
- Jacqueline and Jamie are the WorkBoard admins for permissions
- **Interim plan:** enter OKRs on personal page; admins consolidate into pod-level scorecard

## Action Items

### For Me

- [ ] Sync with [[Daniel_Milburn|Daniel]] on observability OKR — what 3–5 SLOs are feasible this quarter ^task-20260406-003
- [ ] Check with Daniel + [[Ramesh_Unknown|Ramesh]] on JFrog artifact repository usage across teams ^task-20260406-004
- [ ] Check container registry status — likely already in ECS, may not need a KR ^task-20260406-005
- [ ] Check in on complex order automation — confirm no major engineering backlog ^task-20260406-006
- [ ] Ping Daniel re: monthly cyber sync — let Daniel attend and escalate as needed ^task-20260406-007
- [x] Draft OKRs into WorkBoard (personal page as interim); connect with Jacqueline/Jamie on pod-level permissions ^task-20260406-008 ✅ 2026-04-14 16:50

### For Other Party (likely manager/CTO)

- Rewrite RTO/RPO KR as outcome-based ("reduce recovery time from 13hrs to Xhr")
- Edit Jarvis section → rename to "improve delivery efficiency"; remove AI-specific KRs
- Fix cybersecurity OKR wording for consistency across pods
- Move PDF content to Confluence page for collaborative editing
- Have Ramesh reach out to Jenna to scope DR failover test in lower environment
- Ping WorkBoard admins (Jacqueline/Jamie) to locate/fix automation pod page
- Align with [[Eric_Arrington|Eric]] on AI/engineering training KRs separately

## Strategic Insights

- Pod-level OKRs are the right granularity; individual OKRs don't scale
- Outcome-based KRs (reduce recovery time from X to Y) are better than process KRs (close the gap)
- Delivery efficiency metrics should replace AI-specific metrics
- Several cybersecurity compliance items need infrastructure work before they're KR-ready

## Links

- [Granola Chat](https://notes.granola.ai/t/a72ccf59-79e5-4f6c-9de6-fb8395c698e7)

---
*Processed from Granola on 2026-04-12*
