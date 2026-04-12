# Principal Software Engineer - Java Interview Questions
**Duration:** 45 minutes | **Candidate:** Justin Hancock


## Intro
- Marten 
	- went through GHX
- Justin:
	- Full stack
	- Wears a lot hats
	- Like to stay in the code
	- Worked in 
		- Healthcare
		- Startups
		- Currently in the defense industry
			- SpaceForce project
			- 2 years as a contractor, they want to bring me on full time now
		- Tech lead + Scrum Master + DBA (Posgres)

Your core strengths?
- Leadership on the team
- Scrum master
- Reporting to stakeholders
- IC as well as confident when it comes to designing something the right way
- One of the architects on the team (although that is not a formal designation)
- Anything Database, Open API, Springboot I need to be involved
- If they need to gripe about anything, get a reality checl


## Technical Screening Questions (30-35 minutes)

### 2. Microservices & RESTful APIs (5-7 minutes)
**Q:** You're tasked with breaking down a monolithic Java application into microservices. What's your approach? What patterns would you use for service communication, and how would you handle distributed transactions?

Answer:
- Looking at it from a future state - where do I want to be, to be able to deliver things quickly.
	- From a business / tech perspective: what can be carved off into its own service? Things need to keep functioning the same way from the customer's perspective
	- Having teams to be owners / stewards of groups of features that somewhat related.
- What patterns would you use for service communication?
	- I am not much of platform operator guy... but everything seems to be ephemeral Kubernetes these days
	- Microservices would use API gateway - Open API 
- Direct point to point or async?

Notes:
- I had to push really hard for him to start thinking about APIs - started talking about the network layer etc. Which is strange given that he mentioned Open API earlier...
- Seemed confused when I asked about point-to-point - didn't really seems to think there was an alternative.

*Follow-up: How do you handle service discovery and API versioning in your microservices architecture?*

**Looking for:** Microservices patterns (API gateway, circuit breaker, saga pattern), REST best practices, practical experience with service decomposition

---

### 3. Database Design & Polyglot Persistence (4-6 minutes)
**Q:** The job requires experience with MySQL, MongoDB, and ElasticSearch. Can you describe a scenario where you might use all three in a single system architecture? How would you ensure data consistency across these different data stores?

Answer:
- If I am working with true relational data that I need to query on -> RDBMS
	- Structured data
	- You also get SPs, functions
	- Also a lot of people with experience in the industry
	- If the data is relational in nature
	- What would push you away from relational? Why can we not store all data in a RDBMS?
		- Complex joins, loading a lot of data into a relational schema can take time
- Document DBs (MongoDB / DynamoDB)
	- Less rigid, provides more flexibility
	- Don't know how Mongo scales... have heard horror stories would have to do some
	- If we don't need heavy querying, we could use DynamoDB
- How do you ensure consistency?
	- Needs to be transactional
	- How can you use transactions across multiple databases?

Notes:
- Again pretty disappointed in how hard it was to get Justin to go deeper
- When asked about consistency, and challenged about transactions, I could not get him anywhere near CAP theorem etc.

**Looking for:** Understanding of polyglot persistence, CAP theorem, eventual consistency, appropriate database selection for use cases

---

### 4. Performance & Scalability (4-6 minutes)
**Q:** Describe a situation where you've had to improve the performance and scalability of a Java application. What tools did you use to identify bottlenecks, and what optimizations did you implement?

- Look at physical/hardware metrics (CPU, memory)
- Look at logs
- Turn on a profiler to get more insights... could be good input for whether throwing more money/hardware at the problem temporarily. 
- Logs from the datastore (long running queries etc. )

How would this inform whether we scale up or out?
- Depends on the tech we are running on
- I.e. EC2 we would need to scale up
- If we have the opportunity to scale out, we should do that (Kubernetes etc.)

Notes:
- Pretty good on the scaling out vs,. scaling up topic. Seems to understand this.

**Looking for:** Profiling tools, JVM tuning, caching strategies, database optimization, horizontal vs vertical scaling

---

### 6. AI-Assisted Development & Code Generation (4-6 minutes)
**Q:** How are you currently using LLMs and AI coding assistants (like GitHub Copilot, Claude, ChatGPT) in your development workflow? Can you describe a scenario where AI assistance significantly improved your productivity or code quality?

Answer:
- Interestingly there is a lot of discussion right now whether it is safe to use in the defense industry
	- We are forbidden from using AI at General Dynamics
	- We have an internal model we are allowed to use, but it is not integrated into IDEs etc. 
- We are currently using an internal model (based on Sonnet 3.7) model with Claude
- Scary in the sense that "with great power comes great responsibility" - i.e. if you don't know what you are doing, you can get into deep trouble
- Concern about Junior developers not understanding what the AI is producing

*Follow-up: What are the risks or limitations you've encountered with AI-generated code, and how do you mitigate them?*

**Looking for:** Practical experience with modern AI tools, critical thinking about AI limitations, understanding of code review practices for AI-generated code, awareness of security/licensing concerns

---

## Behavioral Questions (10-15 minutes)

### 9. Cross-functional Collaboration
**Q:** The role requires working with Product Management, QA, Operations, and vendor/offshore teams. Describe a challenging cross-functional project you've worked on. What made it challenging, and how did you ensure alignment across teams?

Answer:
- I did a lift and shift for FutureScript (pharma spin off from BC/BC) over to the new company.
	- Not offshore team
	- Team included DBAs, Developers
	- Lots of different people involved, communicated with lots of different stakeholders

Notes:
- Again difficult to get to go deep.

**Looking for:** Communication skills, stakeholder management, ability to translate technical concepts for non-technical audiences

---

## Closing Questions (5 minutes)

- What questions do you have about the role, team, or GHX?
	- 4 months in (read my LinkedIn profile), how do you like it?

---

## Interview Tips

**Technical Depth:** For Principal level, expect detailed technical discussions. Don't hesitate to go deeper on topics where the candidate shows expertise.

**Leadership Assessment:** Principal ICs should demonstrate technical leadership even without direct reports. Look for evidence of influencing technical direction and elevating team capabilities.

**Red Flags to Watch:**
- Inability to articulate architectural trade-offs
- No experience with distributed systems or cloud platforms
- Poor communication or inability to explain complex concepts clearly
- Lack of mentoring or leadership examples

**Green Flags:**
- Asks clarifying questions before answering
- Discusses trade-offs and context
- Shows curiosity about GHX's technical challenges
- Provides specific, detailed examples from experience