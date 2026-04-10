#### Thoughts backlog ####
- Large releases with lots of testing are actually riskier than small releases with little testing
- Large releases are not only hard to release, they are also hard to roll back
- If a service still requires constant coordination, shared releases, or shared DB changes, it is probably not a real boundary.
- Decoupling a monolith is like untying a knot:
	- You can't start with the core
	- It gets easier and easier
- Getting to Easy Releases Requires More...
	- Ownership of the code and systems (break the monolith)
	- Ownership and control of the release process
	- Ownership and agency of the infrastructure
	- Local leadership (EM, PO) - remember, to move autonomously you need the ability/agency to make decisions autonomously 
- Lots of end-to-end / UI tests (brittle, difficult to maintain)
- The monolith also has other direct costs - Perf Environment

#### ToDo ####
1. Change / Simplify slide 12
2. Add "figure our ownership" to slide 15
3. 
4. Draw schematic Exchange System Diagram/Teams
5. Add DB aspect
6. Illustrate dependencies
	1. DB dependencies
	2. The risk of regression (change in 1 corner affects another)
7. Illustrate Monolith vs Services
	1. Something like https://nordicapis.com/whats-the-difference-microservice-macroservice-monolith/
8. Incorporate Strangler Pattern - touch on what the direction to the teams will be

#### Outline ####
1. Title Slide
	1. Building Autonomous Engineering Teams
		1. New Exchange Organization Structure Q2 2026
2. Why we are here today
	1. We are moving too slowly
		1. Monthly releases
		2. Huge batched changes
		3. 2+ week testing cycles
	2. It all comes back to the monolith
		1. Difficult code base
		2. Lots of dependencies
		3. Unpredictable side effects
		4. Difficult to test individual components
3. Our Monolith (show what it looks like)
	1. Picture of the actual Products and Applications (from the City Map exercise)
	2. *TALKTRACK: So, right now we have:*
		1. *~100 engineers that need to coordinate development and releases across* 
		2. *19 Products, 57 Applications*
4. Why are we here today: The vicious cycle
	1. Huge Releases
	2. Massive Blast Radius
	3. Extended Testing Cycles
	4. Monthly Releases Only
	5. Changes Batch Up
	6. Even More Testing Required
5. The cost of our current state
	1. For Engineering Teams
		1. Slow feedback loops
		2. Things that should be easy are now high risk and difficult
		3. Coordination overhead
		4. Lack of autonomy
		5. Difficult to prioritize and manage mixed work streams
	2. For Product & Customers
		1. Poor deployment frequency
		2. Long lead time for changes
		3. Slow incident remediation
		4. Delayed security fixes
		5. Cannot respond quickly to customer needs
6. The cost of our current state: Examples
	- 30 day release cycle
	- Top heavy (maybe even inverted??) Testing Pyramid
	- SFTP down as a result of Audit DB problems
	- Domino effect of Elastic upgrade (holding up other unrelated teams etc.)
	- Slow OSS vulnerabilities remediation
7. In Other Words...:
	1. Releasing is Hard -> Release Seldom -> Releasing becomes harder -> ...
	2. Releasing is Easy -> Release Often -> Releasing becomes easier -> ...
8. Monolith vs. Services owned by Autonomous Teams
	1. ... but releasing 19 products / 57 applications together is never going to be easy
	2. So, we need to get from :
		1. ~100 engineers that need to coordinate across 
		2. 19 Products, 57 Applications
	3. ...to:
		1. ~5-10 engineers that own 1-3 Products, can release each app separately
9. How can the Exchange monolith be broken apart?
	1. It is actually fairly easy to see how Exchange breaks up into parts that are more manageable
		1. Apps/services that accomplish something encapsulated...
	2. But again, these pieces are currently strongly coupled, intertwined, share databases etc...
10. The approach / Strategy (i.e. how are we going to get there)
	1. Reverse Conway Maneuver
	2. Shape team boundaries to match the system design we want
		1. Areas of ownership
		2. Component boundaries / loose coupling
		3. Each team owns clear domain boundaries
		4. Teams can deploy independently
		5. Reduced coordination overhead
11. The vision: Autonomous Teams
	1. Clear ownership boundaries
	2. Teams **build, deploy, and operate independently**
	3. Well-defined, **loosely coupled** areas of ownership
	4. Clear product partnership per team
	5. **Teams can ship on their own cadence** 
	6. Run their agile process independently
12. The Vision: Why Autonomous Teams Matter (i.e. there are other benefits too)
	1. It is more fun and fulfilling to work in a autonomous team
		1. You can make decisions locally
		2. You can move fast, you know the consequences of actions/changes
		3. You have true ownership & accountability
		4. Autonomy, Mastery, Purpose (i.e. great for culture, morale etc.)
13. Other problems / Opportunities
	1. The Monolith
	2. Databases, data architecture, the right database for the right job
	3. AI Native development environment and process
	4. The Agile Process
		1. Just like we will have dedicated EMs, we need dedicated POs
14. So what does this org look like?
	1. The Exchange teams
	2. There are a few other teams:
		1. Customer Enablement (current mapping solution)
		2. Continuity Assure
		3. Document Understanding
		4. Managed Services
		5. Data Architecture & Engineering
		6. Developer Platform & AI Enablement
		7. Performance Environment ()
15. The approach / Strategy RECAP:
	1. Reverse Conway Maneuver
	2. Set the teams up for autonomy (dedicated EM)
		1. Side note - really need dedicated PO as well
	3. The ask / direction from the teams
		1. Make sure the agile process 101 is in place (need this for many reasons, including ability to make decisions locally, ability to measure progress, ...)
		2. Work towards autonomy (carve out the code, create your own DevOps & CI/CD, testing ...)
		3. Start shifting towards infra you can own (cloud native)
		4. AI-native / agentic development - great opportunity while building "your" environment
		5. Don't boil the ocean! Use the strangler pattern!
		6. Demonstrate: clear ownership, independent deployment, operational readiness (this can be done service by service... again, strangler pattern)
16. Measuring Success:
	1. Deployment Frequency - symptomatic of your batch size, coupling, release friction, and organizational autonomy
		   *Low frequency often points to shared release trains, heavy manual approvals, brittle testing, risky changes, or too much coordination across teams. High frequency usually suggests smaller changes, better automation, and teams that can release with less ceremony.*
	2. Lead time for change - symptomatic of your end-to-end flow efficiency
		   *Long lead time usually signals queues, handoffs, slow PR review, test bottlenecks, environment friction, slow CI, or release processes that delay otherwise-ready code. In other words, it tells us more about process and system friction than about coding speed alone.*
17. New Team Topology
	1. Product Teams (stream aligned teams):
		1. Exchange IO 
		2. Exchange Core
		3. Exchange Analytics
		4. Exchange Actions & Rules
		5. Exchange Mapping
		6. Exchange Customer Enablement (current Mapping)
		7. Exchange Document Understanding
		8. Exchange Customer Visibility
		9. Organizations Platform
		10. Users Platform
		11. Continuity Assure
	2. Enabling Teams:
		1. Developer Platform & AI Enablement
		2. Data Architecture & Engineering
	3. Complicated Subsystem Teams:
		1. Exchange Performance Environment
18. Org structure
	1. These are bigger and deeper changes, more audacious goals than just KTLO 
	2. Need deeper involvement from in each area -> narrower focus
		1. One EM per team
		2. Narrower Director responsibilities
		3. Help from enabling teams
		4. Org:
			1. Marten (ED)
				1. Daniel Milburn (Director, Engineering)
					1. Exchange IO 
					2. Exchange Core
					3. Exchange Analytics
					4. Exchange Actions & Rules
					5. Exchange Performance Environment
				2. Mike Mitchell (Sr. Engineering Manager)
					1. Organizations Platform
					2. Users Platform
				3. Ramesh Donnipadu (Director, Engineering)
					1. Exchange Mapping
					2. Exchange Customer Enablement (current Mapping)
					3. Exchange Document Understanding
					4. Exchange Customer Visibility
					5. Continuity Assure
				4. New Hire (Director Developer Platform & AI Enablement)
				5. New Hire (Principle Engineer, Data Architecture & Engineering)
19. Org Structure Rationale
	1. Why This Structure?
		1. Bigger and deeper changes than just KTLO
		2. More audacious goals require focus
	2. What This Enables:
		1. One EM per team - dedicated leadership
		2. Narrower Director responsibilities - deeper engagement
		3. Help from enabling teams - platform support
20. Summary of changes:
	1. Autonomous Teams that own "everything"
	2. Dedicated EM Per Team
	3. A couple of enabling teams


21. Team Model / How your team will operate
	1. Dedicated EM (player-coach)
	2. Each team/product will have their own SDLC
	3. Product partnership and agile ways of working 
22. Coordination / Planning / Roadmaps / Product
	1. Product and Engineering partnership model
	2. Cross-team coordination where needed
	3. All work visible in Jira
23. Initial Team Missions
	1. Work aggressively towards autonomy
	2. Cloud native
	3. AI-native / agentic development
	4. Demonstrate: clear ownership, independent deployment, operational readiness

24. Immediate steps / what happens next
	1. Teams are forming NOW
		1. Some teams already partially staffed (existing employees)
		2. Some teams building from scratch (EM + senior ICs first)
		3. All teams begin autonomy work immediately
	2. Aggressive hiring already in progress (40+ open roles)
		1. Director of Engineering, Developer Platform & AI Enablement (US)
		2. Principal Engineer, Data Architecture & Engineering (US)
		3. Engineering Manager (4 US, 5 India)
		4. Staff Engineer (2 US, 2 India)
		5. Senior Engineer (2 US, 11 India)
		6. Engineer III (3 US, 5 India)
		7. Engineer II (4 US, 5 India)
		8. QA III (1 India)
		9. QA II (1 India)
	3. Dual track approach
		1. Continue delivering on existing commitments
		2. Work towards autonomy in parallel (cloud native, independent deployment, operational ownership)
