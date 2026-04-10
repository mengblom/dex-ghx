---
company: "GHX"
role: "Principal Engineer - Data Architecture and Engineering"
content_type: "interview"
date: "2026-04-01"
topics: ["hiring"]
---

# Principal Engineer - Data Architecture and Engineering Interview - Alex Nyffeler
**Duration:** 30 minutes | **Type:** Hiring Manager Screen | **Date:** 2026-04-01

## Candidate Background
- **Current:** Contractor at Deloitte/Green Dot Bank (Nov 2025 - Present); previously Sr. Staff Data Engineer at Northrop Grumman (Jul 2023 - Nov 2025)
- **Experience:** 15+ years as Principal Data Engineer & Architect across defense, finance, manufacturing; strong cloud (Azure/AWS), data orchestration, ETL/ELT pipelines, team leadership
- **Key Strengths:** Metadata-driven orchestration platforms, performance optimization (24h→30min ETL), real-time streaming (Kafka/Databricks), team leadership (led 11 engineers), established engineering standards
- **Stack:** Python, C#.NET, Java, SQL Server, Oracle, MongoDB, Azure, AWS, Databricks, Kafka, Denodo

## Interview Questions

### Opening (5 minutes)
1. **Walk me through your background and what attracted you to this Principal Engineer role at GHX?**
    - Started in SCADA systems (industrial control) for ~10 years
	    - Client-server architecture, networking, VPNs, HMI screens, database work
	    - Legacy programming: VBA, VB.NET, hardware integrations
	    - Found older languages frustrating
	- Moved to contract work: accounting, finance, inventory management for manufacturing
		- Wanted experience with cloud, Python, C#, newer protocols/frameworks
		- Focus on programming vs. infrastructure/networking
    - Experience with hypervisors, containerization
    - Built applications for compliance systems, rule sets for ETL (batch and real-time)
    - Worked with Databricks, Kafka, OPC drivers → real-time databases → historical systems → reports
    - **Consistent theme:** Databases and SQL throughout career
    - Languages: Java, Python, C#, some web programming
    - Home lab: hypervisor running containers, web servers, IoT projects (garden pump automation)
    - **Leadership:** Led teams of different sizes through migrations, code reviews, mentorship programs, office hours for framework standards

    **Northrop Grumman (Staff Engineer, ~30 dev team):**
	- Ran office hours, set project methodology standards
	- Integrated with larger org infrastructure, reporting, analytics, AI
	- **Major project:** Evaluated cloud platforms (Snowflake, Databricks, AWS, Azure, Planet Tier)
		- Led team through use cases for all platforms
		- Chose Databricks on AWS
		- Claims "good understanding of what all different cloud platforms offer other than Google"
	- Projects with Kinesis, Kubernetes (OpenShift)
	- Set Docker standards for Python ETL containers
	- Streamlit for data entry - designed UI standards (button clicks, tables, formatting, styling)
	- Built central library for API calls with adapters for different APIs (batching, rate limiting, different auth methods)
		- SOAP (legacy internal API transitioning to OAuth 2) and OAuth 2 (Salesforce)
		- ODBC connections

    **Core strengths when asked:**
	- Programming: T-SQL, Python
	- Troubleshooting code
	- SCADA background = dealing with black boxes, calling vendors for bug fixes, getting 3 vendors on phone to debug integration issues

2. **You're currently contracting at Deloitte - are you looking for a full-time role, and if so, what's driving that shift?**
    - *NOT ASKED*

### Data Architecture & Technical Fit (12 minutes)
3. **At Northrop Grumman you built a metadata-driven orchestration platform. Walk me through the architecture and your specific design decisions?**
    - *NOT ASKED DIRECTLY*
    - Related info from Northrop cloud platform evaluation discussion:
	    - **Evaluation criteria:** Git integration, API connectivity for sample projects, data lineage visibility, data quality, CLI/SDK functionality, deployment ease and automation, integration with SAP and Salesforce
	    - **Migration context:** Moving from OpenShift running SSIS jobs (basic stuff) to Python for everything non-ODBC
	    - SAP data moved to Python for more real-time processing vs. batch
	    - Built continuous loop: check last modified date on dataset, run if data changed, pause if nothing to process
	    - **Source system:** EC2 machines running SQL Server
	    - **Target:** Medallion architecture on Databricks Delta Lake

4. **I see strong SQL Server and Oracle experience - the JD emphasizes PostgreSQL and MongoDB. What's your depth with those technologies specifically?**
    - **MongoDB:** Main NoSQL experience
	    - Used at PwC for migration project from on-prem to Azure cloud
	    - Stored Kafka messages in MongoDB
	    - "Might use more for JSON document storage"
	    - "Holding area for messaging"
	    - Used for "availability"
    - **Other databases mentioned:**
	    - OPC historical data from SCADA systems
	    - **Postgres:** "My own Postgres at home" (no detail)
	    - Oracle, SAP (relational)
	    - **Redis:** "Done some homework with Redis"
    - **Relational vs. NoSQL philosophy:**
	    - Relational as downstream to collect, analyze, sort data for reporting and application rules
	    - NoSQL for availability and real-time data handling
	    - Noted CDC has gotten better for real-time data handling

5. **You reduced ETL runtime from 24+ hours to 30 minutes at BMO Harris - that's impressive. What was your approach, and how do you typically diagnose performance bottlenecks?**
    - *NOT ASKED*

6. **The role requires working directly with application teams, not just building data systems. How have you typically collaborated with full-stack or backend engineers in past roles?**
    - *NOT ASKED DIRECTLY - but touched on in closing questions*

### Domain & Role Fit (8 minutes)
7. **Your background is defense, finance, manufacturing - no healthcare. What draws you to healthcare tech, and how do you approach ramping up in a new domain?**
    - *NOT ASKED*

8. **We're moving to autonomous, stream-aligned teams where application engineers make data decisions independently. How would you enable teams to be self-sufficient while maintaining good standards?**
    - **Asked in context of splitting monolith into business domains with common architecture**
    - Alex's response focused on understanding the challenge:
	    - Need different integrations between teams
	    - If two domains have conflicting solutions/standards, how to mediate?
	    - Example: batch vs. streaming - if everyone doing streaming with same standards, but two domains have conflicting standards, how to advance architecture for both teams to meet requirements?
    - **Follow-up: Experience working with product, stakeholders, customers**
	    - **SCADA side:** Factory acceptance testing with clients, taking requirements, validation, demos
	    - **Internal groups:** Working with different departments: "These are your requirements, but these are my standards. I can only give you X, Y, Z. Maybe later we can add features."
		    - Help them understand constraints and stages to get there
		    - Define roadmap for capabilities
		    - Communicate what's possible now vs. future
		    - Give time estimates but be realistic
		    - Get team input on velocity and feasibility
	    - **Approach:** "Find sweet spot of delivering now and delivering for future"
		    - Often prototypes newer features himself first
		    - Slowly brings rest of team on to enhance capabilities
		    - Has them start with running, troubleshooting
		    - They answer bugs/features from clients
		    - As they grow understanding, work side-by-side scaling infrastructure

9. **The JD mentions ML/LLM applications, vector databases, RAG patterns - I don't see AI/LLM work on your resume. What's your exposure to that space?**
    - *NOT ASKED*

### Closing (5 minutes)
10. **You've led teams and mentored engineers extensively - how do you balance hands-on technical work versus enabling and educating others?**
    - *NOT ASKED DIRECTLY*
    - Related info from earlier: Prototypes features himself, then brings team along gradually (see #8)

11. **What questions do you have about the role, the team, or GHX?**
    - Asked about system and future direction
    - Noted role is about "expanding to a more uniform system with combining a bunch of different departments for standards"
    - Question: "What is the overall vision for that kind of system? What is the current state and what is it going to try to be?"
    - Asked follow-up about splitting monolith and common architecture
    - Asked about project methodology changes needed when moving away from monolith
    - Closed with: "This just seems like a very interesting system and project. I was excited to interview for this."

---

## Additional Technical Discussion

### Change Data Capture (CDC) Confusion
- Asked about CDC experience with SQL Server
- Response was confusing - talked about APIs triggering publication of new result sets
- Mentioned SAP at Northrop for manufacturing floor order data
- **Major confusion:** Mixed up CDC with OLTP (Online Transaction Processing)
    - Initially said: "Making sure bucket size grew in relation to total table size as we were growing that CDC table"
    - When questioned, clarified meant "bucket count for SQL Server" for CDC size
    - Then said "Real time data. So that's OLDP sorry OLTP. I always get those two together"
    - Corrected to: "Not CDC, OLTP" - admitted confusing the two concepts
- Interviewer had to probe multiple times to understand what candidate meant

### Kafka Experience
- Set up ~20 topics
- Streaming service into PySpark Streams that took data off Kafka topics
- Continuously running stream for new messages
- Formatted data based on JSON message content
- Routed to different predefined functions
- Ran through different rule sets for compliance

### Why Left Northrop
- **Laid off** - new CTO came in
- 2-3 departments let go at the same time
- Reported to Director of Data Engineering

---

## Notes
- **Communication style:** Extremely strange. Call started with "hello" and then just waited with no pleasantries or initiative
- **Major red flag:** Very strong suspicion candidate is faking experience
    - Multiple instances of technical word salad without substance
    - Caught using technical terms incorrectly (CDC/OLTP confusion most egregious)
    - Vague, circular explanations when pressed for details
    - Cannot find LinkedIn page for someone claiming 20 years experience
- **Pattern:** Seems to know buzzwords but struggles to explain actual implementation details or design decisions
- **Technical depth concerns:** When asked about core expertise, gave very generic answers (T-SQL, Python, troubleshooting) without specific examples of complex problem-solving 




---

## Decision

**Recommendation:** ☐ Strong Hire  ☐ Hire  ☒ No Hire

**Key Strengths:**
- Broad exposure to various technologies (SQL Server, MongoDB, Kafka, Databricks, cloud platforms)
- Some leadership/mentorship experience mentioned
- Articulated reasonable approach to prototyping and team enablement

**Concerns/Gaps:**
- **Critical authenticity concern:** Strong suspicion of fabricated or exaggerated experience
    - Confused fundamental concepts (CDC vs. OLTP) despite claiming deep database expertise
    - Technical explanations were vague word salad without substance
    - Could not provide clear details when pressed
    - No LinkedIn profile for someone claiming 20 years experience
- **Lack of depth:** Generic answers to core competency questions; no specific examples of complex problem-solving
- **Communication issues:** Strange interaction style, passive engagement
- **Missing critical skills:** No PostgreSQL depth (just "home lab"), superficial MongoDB experience, no ML/LLM exposure
- **No healthcare domain knowledge** and didn't express interest in the space
- **Principal-level concerns:** Answers lacked the architectural thinking and technical depth expected at this level

**Next Steps:**
- Do not advance to next round
- Pattern of responses suggests candidate may not have authentic experience matching resume claims
