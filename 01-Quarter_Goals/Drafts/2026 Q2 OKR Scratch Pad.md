### My Priorities... regardless of OKRs ###
- The Organization
	- Fill remaining open roles
	- Onboarding, make sure everyone understands the vision, priorities etc.
- Exchange Architecture
	- Define domain boundaries for each team
	- Define Vision / Target Architecture
	- Prioritize / stack rank foundational / cross-org work
		- Events / Messaging / Service Bus
		- Observability - need an opinionated approach
- Agile Process Improvements
	- Intake
		- Need everything in Jira
	- Visibility
		- Dashboards, connection with Aha
	- Get a handle on unplanned work - The Sanctity of a Sprint

### Feedback & Suggested Changes to Curtis's Draft OKRs ###
1. Express DB migration in terms of decrease of hosted clusters
	1. Since we are splitting clusters while migrating, this makes more sense - the target is 0 regardless.
2. Replace "Reduce open PRs..." with "Reduce the average age of PRs..."
	1. *The reason is, as teams start to operate more autonomously, and we increase modularity, and we increase AI assisted development, we should have a lot PRs in the system... not open for a long time, but still...*
3. The following are tentative - I need to discuss with the team to what extent this is feasible in Q2:
	1. Improve Exchange Resiliency by adding 5 Service Level Objectives (SLOs) and reporting that measure the availability of services (Improve observability)
	2. 

### Questions / Clarifications Needed ###
- Daniel:
	- Can we commit to doing another DR test in Q2, just to see where we are at with the experience of having done it once before? What is the effort associated with this; if it is extremely onerous, we should discuss?
		- *Improve Exchange Resiliency by completing a DR test in a lower environment and showing an improvement in measured RTO/RPO in preparation for a production failover test in Q4. (Disaster Recovery) (from 0 to 1)*
	- Do we have a easy and reliable way to count EOL technologies?
		- *Reduce time to market risk by reducing EOL technologies in product from X to Y*
	- How do we manage container storage today? Are we not using a registry?
		- *Reduce security risk by decreasing # of containers NOT stored in GHX Container Registry from X to Y*
	- 