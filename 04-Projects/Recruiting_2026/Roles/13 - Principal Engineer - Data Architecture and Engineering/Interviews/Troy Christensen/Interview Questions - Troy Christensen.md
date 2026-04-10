---
company: "GHX"
role: "Principal Engineer - Data Architecture and Engineering"
content_type: "interview"
date: "2026-03-24"
topics: ["hiring"]
---

# Principal Engineer - Data Architecture and Engineering Interview - Troy Christensen
**Duration:** 30 minutes | **Type:** Hiring Manager Screen | **Date:** 2026-03-24

## Candidate Background
- **Current:** Enterprise Data Modeler at Platte River Power Authority (Sept 2025 - March 2026, contract ended)
- **Experience:** 15+ years in master data management, data governance, data architecture, and data modeling
- **Key Strengths:** MDM/governance frameworks, Azure/Fabric/Databricks data platforms, data classification automation, SAP data integration, large enterprise experience
- **Stack:** Azure, Fabric, Databricks, SAP, Snowflake, SQL (Oracle/SQL Server/DB2), NoSQL (Cassandra/MongoDB), Python/PySpark, Unity Catalog

## Interview Questions

### Opening (5 minutes)

1. **High level summary of your background?**
    - In the data field  for 20 years
    - Worked on some excited projects
	    - BP
	    - Run towards problems, not away from them.
	- Have been a DBA - that is what I started out as
	- At IBM, focus was data governance
	- The last tier of my journey was architecture
	- 

2. **Walk me through your recent work at First Horizon Bank and Platte River - what were you building?**
    -

### Data Architecture & Application Context (10 minutes)

3. **This role works side-by-side with application engineers building products. Tell me about your experience working directly with application development teams?**
    - Follow-up: How do you engage with backend/full-stack engineers on data decisions?
    -

4. **At First Horizon, you designed medallion-style data platforms. Walk me through how you approached data architecture for a specific application or service?**
    - Follow-up: How did you balance data modeling for analytical vs operational needs?
    -

5. **We're heavy on MongoDB and PostgreSQL. You mention MongoDB on your resume - tell me about your experience with NoSQL databases in production?**
    - At First Verizon Bank
	    - Had large dataset
	    - Traditional DBs don't handle read caches really well for large DBs
	    - Management wanted to stick with Microsoft - Cosmos DB
	    - Stepped in and argued we shouldn't lock ourselves into Microsoft
		    - Used MongoDB connectors to Cosmos DB
			    - Any downsides to this? No, not performance wise. Perhaps cleaner code etc. And developers need to understand both Mongo and Cosmos - perhaps operationally more complex
			    - 
    - Follow-up: How do you decide between NoSQL vs relational for a given use case?
	    - Quality - speed -price
		    - What is the ideal DB for the task?
		    - How easy / hard will it be to ensure quality
		    - Operationally - what are we already invested in
		- Here he again went into the MongoDB vs Cosmos question - completely missed the database type/technology aspect
		- What about the type of DB?
			- Is the data structure or unstructured?
			- Are the queries similar or not?
			- Is latency an issue, then you lean towards unstructured
			- He started talking about file formats (parquet etc.)... not sure what this was all about...
			- Very poor answer here... really seemed like he didn't know, or at least had no structure thinking around this.

6. **Tell me about a time you had to optimize database performance at scale - query tuning, indexing, that sort of thing?**
    - On-prem / traditional RDMBS:
	    - Looking at indexes, query plans, how tables are getting scanned etc.
	    - Important to understand how the users are going to query the data
	    - No silver bullets - for example, cannot just keep throwing indexes at it, it will slow down writes
	    - On the read side: Goal is to prevent table scans. Read caches work well too.
	    - On the write side: Trying to use replication. 

### Team Enablement & Collaboration (8 minutes)

7. **We're transitioning to autonomous, stream-aligned teams who own their data. How do you see your role enabling teams vs being a gatekeeper?**
    -

8. **Tell me about a complex problem you solved, something you're proud of?**
    -

9. **You've worked at large enterprises - First Horizon, Schlumberger, Honeywell. How do you influence engineering decisions when you don't have direct authority?**
    - I try to understand the objectives of the teams.
    - Try to understand tradeoffs (quality - speed - cost)
    - More "collaborate" rather than "influence"

### Motivation & Fit (5 minutes)

10. **Why are you looking for something new? What drew you to apply for this role?**
    -

11. **What are some important qualities of the company and team around you?**
    -

### Closing (2 minutes)

12. **What questions do you have about the role, team, or GHX?**
    - 

---

## Notes
*Use this space for overall impressions, concerns, strengths*




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
