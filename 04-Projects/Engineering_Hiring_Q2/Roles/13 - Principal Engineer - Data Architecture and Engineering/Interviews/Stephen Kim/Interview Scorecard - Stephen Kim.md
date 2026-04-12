---
tags:
  - interview-scorecard
  - principal-engineer
  - data-architecture
candidate: Stephen Kim
date: 2026-03-23
interviewer: Marten Engblom
stage: hiring-manager-screen
---

# Interview Scorecard: Stephen Kim
**Role:** Principal Engineer - Data Architecture and Engineering
**Date:** 2026-03-23
**Stage:** Hiring Manager Screen (30 minutes)

**Rating Scale:** 1=Definitely Not | 2=No | 3=Mixed | 4=Yes | 5=Strong Yes

---

## Skills Assessment

| Skill | Score | Evidence |
|-------|-------|----------|
| Deep hands-on experience with relational databases (PostgreSQL, SQL Server) | 5 | **Demonstrated:** PostgreSQL "everywhere" at Convera with indexing, object store; SQL Server migrations at multiple companies; Oracle/MySQL experience |
| Deep expertise in NoSQL databases (MongoDB, DynamoDB, DocumentDB) | 2 | **Critical gap:** Cassandra, Neo4j, ElasticSearch on resume; **In interview: MongoDB "It has been a long time..."** |
| Database performance optimization at scale | 4 | Resume: "Performance issues with Hadoop and Hive" led to Cassandra; interview discussed indexing; no deep specific examples |
| Advanced data modeling and schema design | 5 | **Demonstrated:** Multiple data modeling tools listed (Hackolade, pgModeler, ERWin); interview notes: "Seems good at data modelling, especially in RDBMS" |
| Application development skills | 3 | Python at Virta Health (billing automation); more data engineering than application development |
| Can review application code and architecture | 4 | **Interview confirmed:** "Lots of code reviews, and observability (DataDog etc.)" - directly stated in interview |
| Experience evaluating and selecting database technologies | 4 | Multiple database selections across companies; Cassandra over Hadoop for performance; POC with graph database |
| Cloud data platform expertise (AWS, Azure, or GCP) | 5 | **Demonstrated:** AWS and GCP across multiple companies; AWS DMS, SNS/SQS, Lambda, SageMaker; specific services listed |
| Data warehouse design and implementation | 5 | **Demonstrated:** Multiple Snowflake migrations (Convera, ServiceSource, CMS); Redshift at Virta; BigQuery at OCI |
| ETL/ELT pipeline design and data processing architectures | 5 | **Demonstrated:** AWS DMS, dbt, NiFi, Matillion; ETL best practices at Virta; data pipelines at multiple companies |
| Event-driven architectures, CDC, streaming platforms | 5 | **Interview demonstrated:** Kafka pub/sub at Convera with Lambdas as consumers; Kafka at InteliSecure; AWS SNS/SQS |
| Data architecture for ML/LLM applications | 4 | ML fraud detection at Convera, Squire, InteliSecure; SageMaker at Squire; TensorFlow at Neustar; no LLM/RAG experience |
| Zero-downtime data migration and schema evolution | 4 | Multiple migrations (SQL Server to Snowflake); CI/CD for database changes; no specific zero-downtime examples |
| Data quality, monitoring, and observability practices | 5 | **Interview demonstrated:** DataDog, Open Metadata for lineage, data quality as key concern; Apache Superset dashboards |
| Aligning data ownership models with domain boundaries | 4 | **Interview:** Discussed microservices as source of truth, data syndication; domain boundaries in microservices context |
| Hands-on troubleshooting and optimization | 4 | Code reviews, observability; recent roles more architecture but still hands-on technical |
| Proficiency in modern programming languages | 4 | Python demonstrated (Virta Health billing automation); JavaScript, Shell scripting listed |

**Skills Summary:** Strong data architecture fundamentals with deep PostgreSQL, Snowflake, Kafka/event-driven experience. Excellent observability and data quality practices. **Critical gap: MongoDB hands-on experience.** Good code review engagement with teams. More data platform focus than application development.

---

## Qualifications Assessment

| Qualification | Score | Evidence |
|---------------|-------|----------|
| 10+ years of hands-on experience building software applications | 3 | 24+ years in data architecture/engineering; data platform focus more than application development |
| Strong application development background | 2 | Python at Virta (billing automation); primarily data architecture/engineering role, not app development |
| Track record of establishing data standards | 4 | ETL best practices at Virta; Data Engineering playbook at OCI; mentoring engineers on best practices |
| Experience leading data migrations | 5 | **Demonstrated:** Multiple SQL Server to Snowflake migrations (Convera, ServiceSource, CMS); Salesforce to microservices |
| Experience with AI/LLM-assisted development tools | N/A | ML work but no mention of AI-assisted development tools |
| Prior Principal Engineer, Staff Engineer experience | 5 | Principal Enterprise Architect (Convera), Principal Data Architect (InteliSecure), Director roles |
| Bachelor's degree in Computer Science | 4 | BS Management Science from Virginia Tech (not CS but technical degree) |

**Qualifications Summary:** Strong senior technical experience at Principal/Director levels. Excellent data migration track record. Data platform/architecture background more than application development. 24+ years experience with founding team at Virtela (sold $525M).

---

## Personality Traits Assessment

| Trait | Score | Evidence |
|-------|-------|----------|
| Enabling mindset - succeeds by making others successful | 4 | Mentors engineers globally (US, India, Australia); created ETL playbooks; code reviews with teams |
| Educates and empowers rather than gatekeeps | 4 | Mentoring emphasis across multiple companies; published playbooks; "good thoughts" in interview |
| Hands-on and takes ownership | 4 | Code reviews, DataDog observability, hands-on in interview discussion; recent role still technical |
| Can influence without authority | 4 | Consultant roles require influence; worked with exec teams; global team coordination |
| Pragmatic judgment - speed vs. perfection | N/A | Not assessed in interview |
| Comfortable with ambiguity and building from scratch | 5 | **Demonstrated:** Founding team member at Virtela (startup to $525M exit); multiple greenfield projects |
| Works effectively in agile/iterative processes | N/A | Not mentioned or assessed |
| Collaborates across teams | 4 | Interview: works with application teams via code reviews; cross-functional at multiple companies |
| Communicates technical concepts effectively | 4 | Interview notes: "Good interview rapport - ran long due to quality technical discussions" |

**Personality Summary:** Strong enablement mindset with mentoring across global teams. Comfortable building from scratch (Virtela founding team). Good technical communication and collaboration.

---

## Other/Details

| Item | Score | Evidence |
|------|-------|----------|
| Healthcare or EDI domain knowledge | 5 | **Demonstrated:** CMS (Medicare/Medicaid) project with HIPAA; Virta Health (PHI handling); compliance-driven design |
| Experience in enabling team or platform team models | 3 | Mentoring and code reviews; more traditional architecture role than platform team enablement |
| Experience with autonomous or cross-functional teams | 3 | Microservices architecture suggests domain ownership; not explicitly autonomous team model |

---

## Overall Assessment

**Key Strengths:**
- **Strong PostgreSQL expertise** - "PostgreSQL everywhere" at Convera with hands-on indexing, optimization
- **Proven Snowflake migration leader** - Multiple successful SQL Server to Snowflake migrations
- **Excellent event-driven architecture** - Kafka pub/sub with Lambdas, demonstrated in interview
- **Strong observability practices** - DataDog, Open Metadata (data lineage), data quality focus
- **Healthcare/compliance experience** - CMS (HIPAA), Virta Health (PHI), compliance across 70+ countries
- **Code review engagement** - Works directly with application teams via code reviews and observability
- **Founding team success** - Core founding team at Virtela (startup → $525M exit to NTT)
- **Global team leadership** - Managed engineers in US, India, Australia, Romania, Philippines, Ukraine
- **Great interview rapport** - Quality technical discussions, ran long due to depth
- **Multi-tenancy architecture** - Relevant to GHX needs (AWS Cognito, Verified Permissions)

**Key Concerns:**
- **MongoDB hands-on gap** - Interview quote: "It has been a long time..." - **Critical for role per JD**
  - Has Cassandra, Neo4j, ElasticSearch but not recent MongoDB
  - Understands document DBs conceptually but lacks MongoDB-specific experience
  - Question: Can MongoDB gap be addressed via 1-3 month ramp given strong fundamentals?
- **Application development background** - More data platform/architecture than app development
  - Python billing automation at Virta (2018-2019) but not primary focus
  - Role requires working embedded with application engineers
- **Leaving Convera after short time** - Feb 2024 start, looking after ~1 year
  - Reason given: PE firm offshoring to India, challenging timezone coverage (Australia/India/Europe)
  - Started as consultant, converted to FTE in May 2024
  - "Sees writing on wall" with offshoring direction

**Decision Context from Interview:**
Interview decision was **HOLD** to evaluate against other candidates in pipeline. Key question: Does MongoDB gap outweigh strong fundamentals?

**Fit for Role:** 3 (Mixed)

**Reasoning:** Stephen has exceptional data architecture fundamentals - PostgreSQL, Snowflake, Kafka, event-driven, observability, healthcare compliance. He demonstrates strong technical depth and would add immediate value in many areas. **However, the role specifically requires "Deep expertise in NoSQL databases (MongoDB, DynamoDB, DocumentDB)" and MongoDB is used "heavily" at GHX.** His MongoDB gap is significant given it's not just preferred but core to the role.

**Tradeoff Analysis:**
- **Strong immediate value:** PostgreSQL optimization, Snowflake, Kafka/event-driven, healthcare compliance, code reviews
- **Ramp time needed:** MongoDB-specific patterns, document modeling, performance tuning in MongoDB
- **Risk:** Can he ramp MongoDB in 1-3 months while adding value elsewhere, or will MongoDB gap create bottlenecks?

**Recommendation:** ☐ Strong Advance  ☐ Advance  ☑ **HOLD** ☐ Pass

**Rationale for HOLD:**
- Strong candidate who could add immediate value in PostgreSQL, Snowflake, event-driven, observability
- MongoDB gap is concerning given "heavily" used at GHX and "deep expertise" required in JD
- Recommend holding to evaluate against other candidates:
  - If pipeline has strong MongoDB candidates → likely pass
  - If pipeline is weak → consider advancing with clear MongoDB ramp plan
- Decision should weigh: MongoDB criticality vs. his strong fundamentals in other core areas

**Next Steps:**
- Evaluate strength of other candidates in pipeline (especially MongoDB expertise)
- If advancing: Technical Deep Dive to probe data architecture depth further
- If advancing: Get explicit commitment on MongoDB ramp timeline (1-3 months)
- Assess: How critical is MongoDB-specific expertise vs. general NoSQL + strong fundamentals?
