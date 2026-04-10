---
company: "GHX"
role: "Principal Engineer - Data Architecture and Engineering"
content_type: "interview"
date: "2026-03-23"
topics: ["hiring"]
---

# Principal Engineer - Data Architecture and Engineering Interview - Stephen Kim
**Duration:** 30 minutes | **Type:** Hiring Manager Screen | **Date:** 2026-03-23

## Candidate Background
- **Current:** Principal Enterprise Architect at Convera (fintech/payments)
- **Experience:** 24+ years in data architecture, engineering, and leadership. Core founding team at Virtela (sold $525M). Led data teams globally.
- **Key Strengths:** Microservices data architecture, healthcare/compliance (HIPAA, HITRUST, CMS project), Snowflake migrations, Kafka/event-driven, multi-tenancy security, ML/fraud detection
- **Stack:** Snowflake, PostgreSQL, Cassandra, Neo4j, ElasticSearch, AWS/GCP, Kafka, Python, dbt, AWS DMS, SageMaker

## Interview Questions

Intro from Stephen
- Industry agnostic - worked in multiple different businesses
- Good at building solutions, not just
- Have done lots of work with startups, cleaning up their data solutions, data warehouses etc.
- Want a full time job, but contract also works
- Reason for leaving Convera after short time:
	- New PE firm, moving most work to India - can see the writing on the wall in terms of direction (although believes his position is safe)
	- Work with a boss in Australia, engineers in India and Europe - challenging time differences that he has to accommodate 
- Earlier did lots of SQL Server, Oracle
- Lately more Snowflake, Redshift
- Have made a career on creating relationships with business stakeholders
- Lately worked on creating a multitenant architecture

What is Convera?
- Cross boarder payments (used to be part of Transunion)
- Lots of compliance, regulatory, GDPR
- Legacy stack almost 20 years old

Notes
- Seems good at data modelling, especially in RDBMS
- Understands why Document DBs are attractive for engineers
	- Relational models requires a bit of discipline... 
- Doesn't have much of MongoDB experience... not sure if I can look past this...
- 

### Opening (5 minutes)
1. **Walk me through your background and current role at Convera?**
    - Transition to multitenant architecture
    - Hierarchal structure of customer accounts
	    - Access, observability etc.

2. SKIPPED: **What drew you to apply for this Principal Engineer role at GHX?**
    -

### Technical Depth - Data Architecture & Application Teams (15 minutes)
3. **At Convera, you're migrating a legacy Salesforce system to microservices. How are you approaching data architecture for that transition?**

	- Pub sub using Kafka
		- Consumers are Lambdas
	- Postgres everywhere ()
		- Indexing
		- Object store with JSON
	- Microservices are the source of truth, then data is syndicated back out also via microservices
		- Problems with this?
			- Data quality - observability is key here
			- Data lineage (we use Open Metadata by Uber)
		- What about data consistency?
			- Replicate data from both publisher and subscriber into Snowflake, then run comparisons
			- 

    - Follow-up: How do you handle data ownership boundaries across services?

4. **The role emphasizes working directly with application teams, not in isolation. Walk me through how you typically engage with an application team on a data problem?**
    - Lots of code reviews, and observability (DataDog etc.)
    - Very good thoughts on ""

5. **You've done several SQL Server to Snowflake migrations. We use MongoDB heavily and are building autonomous teams. How do you approach evaluating when to use document stores like MongoDB versus relational databases?**
    - Follow-up: What's your hands-on experience with MongoDB specifically?
		- It has been a long time... 

6. SKIPPED: **Tell me about a time you optimized database performance at scale. What was the problem and how did you solve it?**
    -

7. SKIPPED: **You worked on healthcare projects at CMS and Virta Health. What data challenges are unique to healthcare, and how did you handle PHI compliance?**
    -

8. SKIPPED: **This role requires reviewing application code with a focus on data access patterns. How hands-on are you with code versus purely architecture?**
    -

### Enabling Teams & Philosophy (7 minutes)
9. SKIPPED: **We're transitioning to stream-aligned, autonomous teams. The data architect role is about enabling teams to make sound decisions independently, not gatekeeping. How does that align with your approach?**
    -

10. SKIPPED: **You've led global teams across multiple countries. How do you mentor and educate engineers on data best practices without creating bottlenecks?**
    -

### Motivation & Fit (3 minutes)
11. SKIPPED: **Why are you looking to leave Convera after just over a year?**
    -

12. SKIPPED: **What questions do you have about the role, team, or GHX?**
    -

---

## Decision

**Recommendation:** ☐ Strong Hire  ☐ Hire  ☐ No Hire  ☒ **HOLD - Evaluate Against Other Candidates**

**Key Strengths:**
- Strong RDBMS and data architecture expertise (24+ years, PostgreSQL, Snowflake, SQL Server, Oracle)
- Solid microservices data architecture approach using Kafka pub/sub, event-driven patterns, data syndication
- Good understanding of observability, data lineage (Open Metadata), and data quality practices
- Engages well with application teams via code reviews and DataDog observability
- Healthcare/compliance experience (CMS, Virta Health) with HIPAA/PHI handling
- Strong stakeholder relationship skills across multiple industries
- Good interview rapport - ran long due to quality technical discussions
- Multi-tenancy architecture experience (relevant to GHX needs)
- Proactive about Convera departure (PE firm offshoring, challenging timezone coverage) - sees writing on wall

**Concerns/Gaps:**
- **Primary concern: Limited MongoDB hands-on experience** ("It has been a long time...") - needs evaluation against role requirements
- Could MongoDB gap be addressed via 1-3 month ramp given strong data architecture fundamentals?
- Role requires deep NoSQL expertise per JD, but how critical is MongoDB-specific vs general NoSQL/data architecture strength?

**Next Steps:**
- **HOLD for a few days** to evaluate strength of other candidates in pipeline
- Decision point: Does MongoDB gap outweigh strong fundamentals, or can he add immediate value in other areas while ramping on MongoDB specifics?
- If candidate pool is weak, consider advancing to Technical Deep Dive to probe data architecture depth further
- If strong MongoDB-experienced candidates emerge, this may be a pass

