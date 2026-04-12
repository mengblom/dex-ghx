# Kooper Frahm - Engineering Manager Interview Summary

**Position:** Engineering Manager
**Date:** 2026-03-12
**Interviewer:** Maren & Daniel
**Duration:** ~60 minutes

---

## Overall Assessment

Kooper Frahm demonstrated **strong technical depth combined with thoughtful leadership experience** across distributed teams in fintech. He showed excellent understanding of engineering management principles, IC progression, hands-on technical leadership, and team dynamics within product organizations. His 6 years of management experience scaling from 1 to 3 teams, combined with 10 years as a backend-focused IC, provides solid foundation for modern engineering leadership.

**Key Highlights:**
- **Excellent communication** - articulate, thoughtful, well-paced delivery, easy to follow
- **Hands-on technical leadership** - adapts involvement based on team experience, stays technical through architecture reviews
- **Strong backend depth** - Java expert, Python, NodeJS, full-stack capable with UI experience
- **AI/ML experience** - model as a service in pricing domain, architected AI-powered search platform, POC to production
- **Real monolith migration experience** - strangler pattern, strong opinions from 18-month journey
- **Clear IC progression framework** - Sr→Staff→Principal expectations (independence, mentorship, SME, architecture)
- **Pragmatic accountability model** - rooted in clear expectations, 1x1 feedback, rarely escalates to performance management
- **Strong product/engineering dynamics** - experienced with triad model, ancillary teams, both org structures
- **Polyglot database expertise** - clear decision criteria across SQL, DynamoDB, MongoDB, Elasticsearch
- **Modern practices advocate** - DORA metrics, observability, automation, AI tooling (Cursor)

---

## Key Strengths

### 1. **Technical Leadership & Hands-On Approach**
- **Adapts technical involvement to team needs:**
  - 3 teams → more abstracted, strategic
  - 1 team (especially juniors) → closer collaboration
  - Always involved in architecture reviews and design
- **Backend-weighted full-stack capability:**
  - Very strong in Java (primary language)
  - Python, NodeJS proficiency
  - UI experience but prefers backend
- **Stays technical deliberately** - values technical credibility as a manager

### 2. **AI/ML Engineering Experience**
- Built **model as a service** in pricing domain at Geico
- Architected **AI-powered search replacement** from ground up
- POC to production experience with cost considerations
- Active AI tool user (Cursor) for development
- Integrating AI systems into production environments

### 3. **IC Career Development Framework**
- **Sr → Staff progression criteria:**
  - Independence in execution
  - Mentorship of others (not just SME, but helping others)
  - Ticket writing and task estimation
  - Architecture reviews participation
  - Setting and enforcing conventions
- **Process:** Understand aspirations → dissect level guidelines → 6-month plan
- Recognizes most seniors don't see it as terminal level

### 4. **Accountability & Ownership Philosophy**
- **Ownership defined:**
  - Don't let things languish
  - Seek clarification when needed
  - Make educated assumptions
- **Accountability approach:**
  - Root: Clear expectations first
  - 1x1 feedback when expectations aren't met
  - Rarely escalates to performance management with proper feedback
- Proactive and preventative rather than reactive

### 5. **Polyglot Database Architecture**
- **Clear selection criteria:**
  - High throughput → **DynamoDB**
  - Transactional data, consistency, complex queries → **SQL (Postgres)**
  - Semi-structured documents, structured queries → **MongoDB** (harder to horizontally scale)
  - In-memory searching, vectorization for RAG → **Elasticsearch**
- Understands horizontal scaling characteristics (NoSQL advantage)
- Use-case driven decision making

### 6. **Monolith Migration Experience (Strong Opinions)**
- **Real battle scars:** 6-month plan → 18-month reality
- **Strangler pattern execution** but identified critical mistake:
  - Team scaffolded data back to monolith
  - Polluted new services with monolith-specific fields
  - **Kooper's recommendation:** Don't scaffold back, build new, verify I/O
- Discussed modular monolith vs. microservices trade-offs
- Recent, deep, relevant experience

### 7. **Product Organization Dynamics**
- **Core triad:** Engineering - Product - Design
- **Ancillary teams:** Data Engineering, Data Science, BI
- Experienced with both models:
  - Product within Engineering
  - Product as separate org
- Strong, articulate thoughts on EM role in broader context
- Great understanding of cross-functional collaboration

### 8. **Performance & Reliability Mindset**
- **Core competency:** Performance, availability, scalability (DORA metrics)
- **Reliability blockers identified:**
  - Poor observability, logging, alerting (balancing noise vs signal)
  - Team inexperience with debugging/issue finding
  - CI/CD process issues (makes remediation harder)
  - **Architecture not typically the blocker** (interesting perspective)
- Systems thinking approach to reliability

### 9. **Management Philosophy & Scale**
- **Org impact driver:** Drove 20% revenue increase project across 3 teams
- **Thoughtful about scale:** Wants to grow to larger org, but deliberately
- **Strategic preference:** Likes strategic aspects of leadership at scale
- **Occasional IC pull:** Acknowledges wondering about returning to IC (healthy self-awareness)
- Net: Committed to management path with growth ambitions

### 10. **Status & Communication Preferences**
- **Frequent updates** but values autonomy
- Too detailed status can be burdensome
- 1x1s with key stakeholders as needed
- **Automation advocate:** Mining status from Jira, tooling
- Asked about reporting expectations (shows awareness of variance across orgs)

---

## Areas Not Fully Explored

- Conflict resolution examples (team conflicts, stakeholder disagreements)
- Production incident response and postmortem processes
- Specific metrics/KPIs tracked for team health and delivery
- Hiring and talent assessment approach
- Remote/hybrid team management experience
- Budget/cost management experience
- Concrete mentorship outcomes and success stories

---

## Hire Recommendation

**Strong Hire** - Kooper demonstrates excellent communication, deep technical credibility (backend/AI), thoughtful leadership philosophy, and highly relevant experience (monolith migration, IC progression, product dynamics). His experience scaling to 3 teams, combined with hands-on technical approach, aligns well with GHX's needs for modern engineering leadership.

### Confidence Level
**High** - Interview covered critical management dimensions (IC development, accountability, technical involvement, product collaboration), demonstrated strong communication, and showed relevant battle scars (monolith migration). Would benefit from reference checks on team feedback and stakeholder collaboration.

### Recommended Next Steps
1. **Reference checks** - focus on team satisfaction, peer feedback, delivery consistency
2. **Panel interview** with potential peer managers and senior engineers
3. **Final conversation** with hiring manager on motivations, questions, scope expectations
4. **Cultural fit assessment** with product/design partners

---

## Notable Quotes/Observations

- **Communication:** "Articulate, thoughtful, well-paced way of speaking. Super easy to follow."
- **Relevance:** "Very relevant experience, both for what we are trying to do / problems to solve, and from a what good looks like / modern engineering ways of working perspective."
- **Accountability:** "The root of accountability is expectations - make sure the expectations are clear."
- **Hands-on:** "I like to stay as technical as possible"
- **Monolith lesson:** Suggested not scaffolding back to monolith, "just build new and verify the input-output"
- **Observability:** Recognizes "tricky to get right - noise vs signal"
- Strong opinions on architecture decisions (DynamoDB vs SQL, monolith approach)
- Asked thoughtful questions about Daniel's management style and reporting expectations
