# Hiring Manager Screen - Madhav Ghimire
**Role:** Principal Engineer - Data Architecture and Engineering
**Duration:** 30 minutes
**Date:** 2026-03-23

---

## Opening (2 min)
Brief intro, confirm interest, set agenda for technical/experience discussion.

- Madhav Intro of himself
	- Data architect at Accenture (mainly in healthcare, but also banking etc.)
	- Laid off in February
	- Last 11 years, responsible for data architecture
		- AWS
		- GCP
		- Snowflake
	- Target architecture
	- Data models
	- Work with data engineering teams to create pipelines
	- BI
		- Tableau
		- Databricks (certified Databricks data engineer)
	- Data governances
- Your core expertise?
	- Create the data models
	- But, also BI dashboards
	- Also data governance
	- Again, core expertise is data modelling
- Notes:
	- Somewhat difficult to understand, communication not great
	- Clearly comes from a consultant background, has worked a lot with off the shelf tools, higher level of abstractions, GUI / low-code tools etc. (Microsoft Synapse, AWS Glue)
	- Not enough experience embedding with / working closely with / supporting product teams - more used to project based consulting engagements

---

## Technical Depth & Experience (25 min)

### 1. Application-Embedded Data Architecture (5-6 min)
You mention embedding with application teams and reviewing code. Walk me through a specific example where you reviewed application code and identified data architecture issues.

- What was the problem?
	- *Perform maturity assessment of legacy system*
	- *Leadership wanted to bring data from multiple systems to AWS cloud* for BI purposes
	- *As a manager, I worked on the architecture, data model, and data engineering, and data governance*
- How did you identify it?
- What changes did you recommend?
	- *Change from AWS to Microsoft Azure (Microsoft Fabric)*
- How did the team respond?
- **Note:** _Looking for: hands-on code review skills, ability to spot data anti-patterns in application code, pragmatic guidance_

### 2. Database Performance Optimization (4-5 min)
Describe a specific database performance issue you diagnosed and resolved at scale.

- What was the symptom?
	- 300 VMs
	- Took 12 days to load the data
- How did you troubleshoot? (Tools, approach)
- What was the root cause?
	- Outdated stored procedures
	- Found non-relevant joins in the SPs
- What was your solution?
	- Microsoft synapse 
- Impact/results?
- **Note:** _Looking for: query tuning, indexing strategy, execution plan analysis, systematic approach to performance problems_

### 3. Technology Selection & Trade-offs (4-5 min)
Tell me about a project when you had to use multiple database types in the same project?

- A mix of columnar and non-columnar databases
	- Why?
		- The teams involved had different expertise and their preference (poor answer)

Questions for me?
- Success factors for the first 6-9 months?


***Was not able to get to any questions below the line:***

---

### 4. Team Enablement & Influence (4-5 min)
You've worked with autonomous application teams. How do you balance establishing standards vs. empowering teams to make their own decisions?

- Give an example of a data standard you established
- How did you roll it out?
- How did you handle pushback?
- How do you know when to be prescriptive vs. flexible?
- **Note:** _Looking for: enabling mindset, educates vs. gatekeeps, influence without authority, pragmatic approach to governance_

### 5. Cloud & Modern Data Patterns (3-4 min)
Your resume shows strong Azure experience. We're primarily AWS-based.

- How comfortable are you with AWS data services? (RDS, Aurora, DynamoDB, Redshift)
- Describe your experience with CDC or event-driven data architectures
- Any experience with cost optimization for cloud databases?
- **Note:** _Looking for: AWS familiarity or ability to translate Azure knowledge, CDC/event streaming experience, cloud cost awareness_

### 6. Zero-Downtime Migrations (3-4 min)
You led zero-downtime data migrations. Describe your approach to migrating a production database without downtime.

- What steps do you take?
- How do you handle schema changes?
- How do you validate data integrity?
- How do you roll back if needed?
- **Note:** _Looking for: practical experience with live migrations, risk mitigation, systematic approach, production ownership mindset_

---

## Closing (3 min)

### 7. Role Fit & Motivation
- What excites you about this role specifically?
- You've been at Accenture 11 years - what's driving you to make a change now?
- Any questions for me about the role, team, or GHX?

---

## Key Areas to Assess
- [ ] Hands-on technical depth (not just architecture theory)
- [ ] Experience working embedded with application teams
- [ ] Database performance optimization expertise
- [ ] Pragmatic judgment on technology selection
- [ ] Enabling/teaching mindset vs. gatekeeping
- [ ] AWS familiarity or ability to quickly translate from Azure
- [ ] Production ownership mindset
- [ ] Cultural fit for autonomous team environment

---

## Candidate Strengths (based on resume)
- 11+ years data architecture experience
- Strong NoSQL (MongoDB, Cosmos DB) and relational (SQL Server, PostgreSQL) background
- Healthcare domain experience
- Team enablement focus (workshops, office hours, documentation)
- ML/LLM data architecture (vector DB, RAG patterns)
- Cloud platforms (Azure strong, AWS listed)
- Zero-downtime migrations
- Databricks AI certifications

## Areas to Probe
- AWS depth (resume shows more Azure)
- Application development background (resume is data-focused, JD emphasizes app development roots)
- Specific code review examples with application teams
- Influence without authority in practice
- Why leaving Accenture after 11 years?



---

## Summary for Greenhouse

**Recommendation: Pass**

Madhav has 11 years of data architecture experience at Accenture - solid background with AWS, GCP, Snowflake, Databricks, etc. But several issues came up that make him not a fit for this role:

Communication was rough - hard to understand his responses at times. That's a problem for a Principal level role where you need to influence and work across teams.

Background is heavily consultant/project-based. Lots of work with GUI tools and low-code platforms (Microsoft Synapse, AWS Glue, etc). Doesn't have the hands-on engineering depth we need. When I asked about technology selection trade-offs, his answer was basically "the teams had different preferences" - not the kind of technical reasoning I'd expect.

Limited experience actually embedding with product teams. He's used to consulting engagements, not the kind of ongoing partnership with autonomous product teams that we need here.

Bottom line: The resume looked good on paper, but the interview revealed he's more of a consultant background than the hands-on technical partner our teams need. 