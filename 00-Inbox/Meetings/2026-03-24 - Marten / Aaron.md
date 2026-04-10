---
title: Marten / Aaron
subtitle: meeting notes
date: 03/24/2026 1:30 PM
meeting: 'true'
meeting-location: Microsoft Teams Meeting
meeting-recipients:
  - Aaron Srivastava
  - Marten Engblom
meeting-invite: |
   
  
  

  
---
### Aaron’s Onboarding & Role Alignment
- New hire joining exchange team focused on AI enablement and developer platform
- Background: Previously built similar platforms, experienced with migrations (BitBucket to GitHub, standardized CI/CD)
- Cautious approach: Avoiding jumping into “easy” tasks that aren’t core responsibilities
- Access pending: GitHub, AWS, Bamboo - blocking full productivity

### Organizational Dynamics & Team Structure
- Multiple “solar systems” emerging around different leaders
    - Greg Wilson: Wants EA as DevSecOps function for software engineering
    - Mark: Focused on software architecture, expects infrastructure handled elsewhere
    - Eric: Leading Jarvis AI initiatives
- Potential personality conflicts anticipated as teams interact more
- Need for better coordination between overlapping functions
### Database & Infrastructure Challenges
- Brought Aaron up to speed on the open role [[Principal Engineer, Data Architecture and Engineering - Job Description]]
### Development Platform Strategy
- Monorepo migration approach: Focus on one service at a time
- Each API team (transaction, user, org) has dedicated engineers and backlogs
- Embed with one team, build skills, then scale to 2-3 services simultaneously
- Standardization challenges: Multiple IaC tools in use (Terraform, CDK, Crossplane)
    - Need collective agreement on technology direction

### AI Enablement & Knowledge Sharing
- Current Jarvis working group meetings too high-level (CTO org-wide)
- Proposal: Internal newsletter for exchange team
    - Weekly/bi-weekly cadence
    - Cover AI, security, operations, infrastructure topics
    - Bridge knowledge gaps across different technology areas
- Aaron meeting with Eric tomorrow to discuss collaboration

### Cost Optimization Opportunities
- Massive AWS spending with limited oversight
- Performance environment equivalent to prod represents significant waste
- Potential for major savings through architecture improvements
    - Example: Moving off MongoDB for eventing
- Goal: Demonstrate measurable cost reductions (e.g., team spending $15k/month reduced to $5k)

- Aaron to provide list of scheduled meetings for review    
- Mårten has bi-weekly with HR BP, one-on-one with Curtis scheduled