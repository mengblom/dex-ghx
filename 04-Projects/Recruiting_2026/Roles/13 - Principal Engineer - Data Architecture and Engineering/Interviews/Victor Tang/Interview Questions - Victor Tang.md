---
company: "GHX"
role: "Principal Engineer - Data Architecture and Engineering"
content_type: "interview"
date: "2026-04-01"
topics: ["hiring"]
---

# Principal Engineer - Data Architecture and Engineering Interview - Victor Tang
**Duration:** 30 minutes | **Type:** Hiring Manager Screen | **Date:** 2026-04-01

## Candidate Background
- **Current:** Just left Verizon (March 2010 - Jan 2026) as Principal Engineer/AI Engineer
- **Experience:** 26+ years in software engineering; 16 years at Verizon building data systems, AI/ML workflows, and modernizing legacy applications
- **Key Strengths:** Deep AI/LLM expertise (AWS Bedrock, RAG pipelines, agentic workflows), data architecture (Databricks Medallion, Oracle, Cassandra, MongoDB), application modernization (Spring Boot microservices), performance optimization (25-30% improvements), strong mentorship/leadership
- **Stack:** Python, Java, Spring Boot, React, Oracle, SQL Server, MongoDB, Cassandra, Databricks, AWS/Azure/GCP, RAG pipelines, vector databases

## Interview Questions

### Opening (5 minutes)
1. **Give me a high-level summary of your background and what led you to apply for this role at GHX?**
    - **Current Role:** Principal Engineer at Verizon (March 2010 - Jan 2026, 16 years)
    - **Focus Areas:** Enterprise platform, AI-driven applications, large scale distributed systems
    - **Core Work:**
        - Data architecture design and performance optimization
        - Data platforms supporting AI/ML using RAG pipelines and event-driven architecture
        - Collaborating with application engineers on domain-driven design and scalable microservices
        - Primary languages: Java, Python
    - **Key Project - Data Pipeline Modernization:**
        - Architected Databricks Medallion pipeline to deduplicate multi-source data (Oracle, Cassandra, Informatica)
        - Reduced data processing time significantly to clean data for AI chatbots and BI reporting (Power BI, Tableau)
        - Used adaptive query execution, optimize, Z-ordering indexing for performance
        - Bronze → Silver → Gold stages in Medallion framework
    - **Key Project - Java Modernization:**
        - Upgraded legacy J2EE applications to Spring Boot microservices
        - Used Strangler Fig pattern to gradually replace legacy components
        - Zero-downtime migration strategy with database replication, phased rollouts
        - Tech stack: Spring Boot, React frontend, Rabbit MQ for async communication, AWS for CI/CD with Docker
        - Built rollback strategies in CI/CD pipeline
        - Mapped service dependencies and data flows for high-traffic endpoints, critical databases, external integrations
        - Used Grafana dashboards to monitor latency, throughput, error rates
        - Achieved ~30% performance improvement
    - **Team Structure:** Small team (~10 people), agile methodology (2-week sprints, daily scrums), product manager, couple engineer teams, business stakeholders, QA, project manager
    - **Product Context:** Verizon B2B e-commerce site for enterprise customers (e.g., Bank of America) to order phones/plans online

2. **What are your core strengths? What are you exceptionally good at?**
    - **Flexibility:** Works as principal engineer/architect but also hands-on with teams
    - **Approachable:** Team finds him easy to approach for problem-solving
    - **Technical Depth:**
        - Started as Java developer (many years of experience)
        - Last 4 years: AI initiatives (Java, Python, AWS)
    - **Production Support Leadership:** Led ~5 production support engineers, handles escalations, gets on calls with customers to troubleshoot
    - **Domain SME:** 16 years at Verizon made him the go-to expert for legacy systems
    - **Example - Business Portal Integration:**
        - Worked with business team and middleware vendor to implement SSO-style link for B2B customers to place orders
        - Send orders back for approval, then receive back for fulfillment
        - Handles production escalations, resolves with quick data fixes or code fixes next day

3. **What would you feel most comfortable doing a technical interview on?**
    - **Primary strengths:** Java application development (many years), Python (last 4 years)
    - **Databases:**
        - Oracle (main DB for business portal)
        - Cassandra (NoSQL for downstream systems)
        - Informatica (ETL/data warehouse for batch jobs)
    - **Database Architecture at Verizon:**
        - Oracle: Source of truth for their business portal
        - Cassandra: Downstream systems use it, send data back via ETL/batch jobs for reporting
        - Data flows from Cassandra → Oracle via nightly batch jobs or incremental updates
        - Customers download reports from the portal (device reports, etc.)
        - Also built Looker integration for UI modernization and reporting performance
    - **Performance Tuning:** Adaptive query execution, Z-ordering, indexing, caching, working closely with database team 


4. **You just wrapped up 16 years at Verizon in January - what prompted the move and what are you looking for in your next role?**
    -

### Background & Technical Fit (12 minutes)
5. **This role is specifically for healthcare technology - you come from telecom. What interests you about the healthcare domain, and how do you think about ramping up on a new industry?**
    - *(Not asked)*

6. **At Verizon you worked on some impressive AI/LLM projects - AWS Bedrock, RAG pipelines, agentic workflows. Walk me through one of those projects and your specific contributions to the architecture?**
    - **AI Initiative for Database Production Support:**
        - Problem: DB production support team monitoring 250+ servers, taking long time to resolve tickets
        - Initial approach: Used in-house LLM with RAG (knowledge base) → created hallucination problems (wrong data)
        - Pivoted: Collaborated with AI engineering team and data science team
        - Solution: AWS Bedrock with agentic autonomous flow
            - Bedrock provides the LLM
            - Used agents to ensure correct data responses
            - Implemented vector database as knowledge base
            - Added filter/content guardrails in Bedrock to control hallucination
            - Implemented human-in-the-loop for data validation and security
            - Data governance and security focus
    - **Rapidly prototyped and deployed to production in 6 months**
    - AWS Bedrock is managed, scalable, helps with security and data governance

7. **You've optimized database performance extensively - Oracle, Cassandra, Databricks pipelines. What's your typical approach when an application team comes to you saying "our queries are slow"?**
    - Adaptive query execution (fine tuning method)
    - Z-ordering indexing
    - Optimize Delta data
    - Working closely with database team
    - Caching techniques
    - For AI area: Query fine-tuning for LLMs, data governance, security

8. **The JD mentions we're looking for someone who works side-by-side with application engineers, not in isolation. How have you typically engaged with application teams at Verizon - are you more embedded or more consultative?**
    - **Consultative across the org**
    - Works with multiple teams simultaneously:
        - Java development team (application side) - still supported before leaving
        - 5-person production team (assigns tickets, triages)
        - AI initiative team for database optimization
        - Business stakeholders and product managers
    - Works closely with business stakeholders and product managers to lay down roadmap and initiatives
    - Gets on calls with customers when there are escalations

### Role Fit & Approach (8 minutes)
9. **We're transitioning to autonomous, stream-aligned teams where application engineers need to make sound data decisions independently. How would you enable teams to be self-sufficient while maintaining good architectural standards?**
    - *(Not asked)*

10. **This role requires PostgreSQL expertise - I see strong Oracle and SQL Server background on your resume. What's your PostgreSQL experience, and how quickly do you typically ramp on a new database technology?**
    - *(Not asked)*

11. **You've led architectural committees and mentored engineers on advanced topics. How do you balance being hands-on with technical work versus enabling and educating others?**
    - *(Not asked)*

### Closing (5 minutes)
12. **What's most important to you in your next engineering leadership role - what would make this a great fit for you?**
    - Emphasized flexibility: able to work on Java development side as well as AI initiatives
    - Wants company going toward AI direction
    - *(Not deeply explored)*

13. **What questions do you have about the role, the team, or GHX?**
    - **How does this role interact with the 10-12 agile teams?** Is it part of one team or across teams?
        - Answer: Reports directly to me, consultative role across all teams
        - Context: Monolithic architecture needs to be broken apart (mentioned strangler fig)
        - Problem: Multiple systems/components talking to same databases
        - Currently stuck on MongoDB for everything (not always the right choice)
        - Teams need help picking and choosing where to store data
    - **What cloud platform are we using?**
        - Answer: AWS
        - Victor's reaction: Similar to Verizon, majority of their deployments in AWS
    - **Are there any AI initiatives?**
        - Answer: Yes, leaning in heavily on both agentic/LLM-assisted development and product initiatives
        - Victor's response: AWS Bedrock is managed, scalable, quickly prototyped and rolled to production in 6 months
    - **What stack does the legacy monolith use?**
        - Answer: Mostly .NET
        - Victor's response: Similar to us (Java), took 6 months to plan and slowly roll out, lots of meetings and planning, achieved 30% performance improvement, CI/CD helped with deployment

---

## Notes

**Strengths:**
- Very experienced (26+ years total, 16 at Verizon)
- Broad technical background: Java, Python, AWS, microservices, data pipelines
- Has worked on relevant technologies: AWS Bedrock, RAG, vector databases, Databricks, event-driven architecture
- Hands-on and takes ownership (production support, customer escalations)
- Experience with modernization (J2EE → Spring Boot, strangler fig pattern, zero-downtime migration)
- Worked across multiple teams and with business stakeholders

**Concerns:**
- **Depth vs. Breadth:** Seems to lean heavily on 16 years of institutional knowledge at Verizon rather than deep technical expertise
- **Database Team Role:** Mentioned multiple times "worked closely with the database team" - this role needs someone who ***was on*** (or ideally ***ran***) the database team, not someone who collaborated with them
- **Application-Focused:** Conversation constantly went to application layer rather than data layer - when asked about databases, talked more about the applications using them
- **Limited Deep Database Expertise:** No PostgreSQL experience, limited depth on database internals, schema design, or advanced optimization techniques beyond "worked with DB team"
- **Communication:** Somewhat unclear at times, hard to follow, repeated himself frequently
    - Misunderstood context (e.g., asked if role is cross-org after I explained it was)
- **Data Architecture vs. Application Architecture:** Background is more application development with data components, not true data architecture role
- **NoSQL Confusion:** Described Cassandra as source of data from "downstream systems" but couldn't clearly explain the data flow or architecture
- **Consultative vs. Embedded:** Role needs someone who can dive deep and be hands-on with teams, not just consultative

**Product Context:**
- Worked on Verizon B2B e-commerce site for enterprise customers to order phones/plans
- Had special features like VIP entry with third-party vendors, reporting, customization for business customers 


---

## Decision

**Recommendation:** ☐ Strong Hire  ☐ Hire  ☐ No Hire

**Key Strengths:**
-
-

**Concerns/Gaps:**
-
-

**Next Steps:**
-
