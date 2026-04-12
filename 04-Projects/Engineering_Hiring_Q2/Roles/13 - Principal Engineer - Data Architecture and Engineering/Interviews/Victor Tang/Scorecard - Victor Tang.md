---
tags:
  - interview-scorecard
  - principal-engineer
  - data-architecture
candidate: "Victor Tang"
role: "Principal Engineer - Data Architecture and Engineering"
interviewer: "Morton Engblom"
date: 2026-04-01
interview-type: "Hiring Manager Screen"
---

# Scorecard: Victor Tang - Principal Engineer - Data Architecture and Engineering

**Rating Scale:** 1 = Definitely Not | 2 = No | 3 = Mixed | 4 = Yes | 5 = Strong Yes | N/A = Not Enough Information

---

## Skills Assessment

### Database Technologies
| Criteria                                                                    | Score | Notes                                                                                                                                                                       |
| --------------------------------------------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deep hands-on experience with relational databases (PostgreSQL, SQL Server) | 2     | Has Oracle and SQL Server experience, but no PostgreSQL mentioned. Strong Oracle background but limited depth demonstrated.                                                 |
| Deep expertise in NoSQL databases (MongoDB, DynamoDB, DocumentDB)           | 2     | Mentioned Cassandra but not MongoDB specifically. Struggled to clearly explain Cassandra architecture and data flow.                                                        |
| Database performance optimization at scale                                  | 2     | Mentioned adaptive query execution, Z-ordering, indexing. However, repeatedly said "worked closely with database team" suggesting he wasn't the one doing the optimization. |
| Advanced data modeling and schema design                                    | N/A   | Not discussed in sufficient detail during interview.                                                                                                                        |

### Data Architecture & Engineering
| Criteria                                                                             | Score | Notes                                                                                                                     |
| ------------------------------------------------------------------------------------ | ----- | ------------------------------------------------------------------------------------------------------------------------- |
| Application development skills (full-stack, backend, or data-intensive applications) | 4     | Strong Java background, Spring Boot, React, microservices. This is his core strength.                                     |
| Can review application code and architecture with focus on data access patterns      | 4     | Yes, worked on microservices architecture, strangler fig pattern, service dependencies.                                   |
| Experience evaluating and selecting database technologies                            | N/A   | Not discussed. Architecture decisions at Verizon seemed to be already established.                                        |
| Cloud data platform expertise (AWS, Azure, or GCP) with cost optimization focus      | 3     | AWS experience shown but mostly at surface level (Bedrock, CI/CD, Docker). Cost optimization not discussed.               |
| Data warehouse design and implementation                                             | 3     | Mentioned Informatica, data warehouse, ETL work. Limited depth shown.                                                     |
| ETL/ELT pipeline design and data processing architectures                            | 3     | Databricks Medallion framework, Informatica batch jobs. Some experience but not core expertise.                           |
| Event-driven architectures, change data capture, and streaming platforms             | 3     | Mentioned event-driven architecture, Rabbit MQ for async communication. Limited depth.                                    |
| Data architecture for ML/LLM applications                                            | 4     | Strong - AWS Bedrock, RAG pipelines, vector databases, guardrails. Recent work (last 4 years).                            |
| Zero-downtime data migration and schema evolution strategies                         | 2     | Mentioned zero-downtime migration with strangler fig, database replication. Application-focused rather than data-focused. |
| Data quality, monitoring, and observability practices                                | 2     | Mentioned Grafana dashboards, data governance, human-in-the-loop. Basic understanding only.                               |
| Aligning data ownership models with domain boundaries                                | N/A   | Not discussed in interview.                                                                                               |
| Hands-on troubleshooting and optimization of production data systems                 | 3     | Production support, escalations, customer calls. But for application issues, not deep data system optimization.           |
| Proficiency in modern programming languages                                          | 4     | Java (many years), Python (last 4 years). Solid.                                                                          |

---

## Personality Traits Assessment

| Criteria | Score | Notes |
|----------|-------|-------|
| Enabling mindset - succeeds by making others successful | 2 | Claims to be approachable and helps team, but difficult to verify from interview. Limited evidence of enabling mindset. |
| Educates and empowers rather than gatekeeps | N/A | Not enough information to assess. Didn't discuss how he mentors or enables others. |
| Hands-on and takes ownership | 2 | Yes on production support and escalations. However, on database work seemed more collaborative than hands-on owner. Role needs data ownership, not collaboration. |
| Can influence without authority | N/A | Not discussed. |
| Pragmatic judgment - knows when to optimize for speed vs. perfection | N/A | Not clear from interview. Mentioned 6-month planning periods. |
| Comfortable with ambiguity and building from scratch | N/A | Not discussed in detail. |
| Works effectively in modern agile/iterative development processes | 3 | Mentioned using agile, 2-week sprints, daily scrums. Standard agile practices. |
| Collaborates effectively across teams | 2 | Worked across Java dev team, production support, AI team, business stakeholders. More consultative than embedded, which doesn't fit this role's need for hands-on collaboration. |
| Communicates technical concepts effectively to executives and non-technical stakeholders | 2 | Communication was unclear at times during interview. Repeated himself frequently, misunderstood questions, struggled to explain technical concepts clearly (e.g., Cassandra data flow). |

---

## Qualifications Assessment

| Criteria                                                                                         | Score | Notes                                                                                                                      |
| ------------------------------------------------------------------------------------------------ | ----- | -------------------------------------------------------------------------------------------------------------------------- |
| 10+ years of hands-on experience building software applications with heavy focus on data systems | 3     | Yes - 26+ years total, 16 years at Verizon. However, focus is clearly more on applications than data systems specifically. |
| Strong application development background (not just database administration)                     | 4     | Yes - strong Java developer background. This is his core strength.                                                         |
| Track record of establishing data standards and patterns across engineering organizations        | N/A   | Not discussed in interview.                                                                                                |
| Experience leading data migrations and infrastructure modernization initiatives                  | 2     | Yes - strangler fig pattern, J2EE to Spring Boot. However, more application modernization than data migration.             |
| Experience with AI/LLM-assisted development tools and agentic software engineering practices     | 4     | Yes - AWS Bedrock, RAG, agentic flows. Recent work (last 4 years).                                                         |
| Prior Principal Engineer, Staff Engineer, or senior technical leadership experience              | 5     | Yes - Principal Engineer at Verizon.                                                                                       |
| Bachelor's degree in Computer Science or equivalent practical experience                         | N/A   | Not discussed, but 26+ years experience suggests yes.                                                                      |

---

## Other/Details Assessment

| Criteria | Score | Notes |
|----------|-------|-------|
| Healthcare or EDI (Electronic Data Interchange) domain knowledge | 1 | No healthcare experience. Telecom/e-commerce background. No EDI mentioned. |
| Experience in enabling team or platform team models | 2 | Led production support team but limited evidence of enabling/platform model experience. |
| Experience with autonomous or cross-functional team environments | 2 | Worked in agile teams with product, QA, engineering. Standard cross-functional setup, not autonomous team model. |

---

## Overall Assessment

**Summary Scores:**
- **Skills:** Average ~2.9 (No to Mixed range)
- **Personality Traits:** Average ~2.3 (No range)
- **Qualifications:** Average ~3.6 (Mixed to Yes range)
- **Other/Details:** Average ~1.7 (Definitely Not to No range)

**Key Strengths:**
1. Extensive experience (26+ years, 16 at Verizon)
2. Strong application development background (Java, Spring Boot, microservices) - this is his core competency
3. Recent AI/ML/LLM experience (AWS Bedrock, RAG, vector databases)
4. Production support experience with customer-facing troubleshooting
5. Familiar with modernization patterns (strangler fig, microservices)

**Key Concerns:**
1. **Not a data architect** - background is application development with data components, not deep data architecture expertise
2. **Limited database depth** - repeatedly said "worked with database team" rather than being the database expert
3. **Communication issues** - unclear explanations, misunderstood questions, struggled with technical concepts
4. **Application-focused mindset** - conversation kept drifting to application layer instead of data layer
5. **No PostgreSQL experience** - role requires it, only has Oracle/SQL Server
6. **No healthcare/EDI experience** - domain knowledge gap
7. **Consultative approach** - role needs embedded, hands-on work, not just consultative

**Recommendation:** ☐ Strong Hire  ☐ Hire  ☒ No Hire

**Rationale:**
Victor is an experienced application developer with some data experience, but he's not the deep data architect this role requires. The role needs someone who is THE database expert that teams come to, not someone who "works closely with the database team." His background is primarily Java application development with recent AI/ML work, which is valuable but doesn't match the core data architecture focus we need. Communication challenges and tendency to focus on application layer rather than data layer are additional concerns. He would be a better fit for a senior/principal application engineer role with AI/ML focus, not a data architecture role.

**Next Steps:**
- Pass on candidate for this role
- Could potentially consider for application/AI engineering roles if those open up
