1. Current State - The Vicious Cycle
	1. Monolithic Code Base
	2. Massive Blast Radius
	3. Extended Testing Cycles
	4. Monthly Releases Only
	5. Changes Batch Up
	6. Even More Testing Required
2. The Cost of our current state
	1. For Product, Stakeholders & Customers
	2. For Engineering Teams
3. The Vision
	1. How we operate
		1. We can release small parts of the system independently, with little or no coordination
		2. We can release very often with very low risk
	2. How the system looks
		1. Small encapsulated services
		2. Loosely coupled services
		3. Fault tolerant services - small blast radius
		4. No shared release dependenceies
	3. The teams???
		1. Can make decisions on their own and operate autonomously
			1. Built It
			2. Test It
			3. Deploy It
			4. Operate It
			5. Evolve It
		2. Autonomy, Mastery & Purpose
4. How we get there
	1. Reverse Conway maneuver 
		1. Form teams and give them ownership of parts of the system
	2. Team Goals
		1. Decouple
		2. Encapsulate (compute, storage, infra)
		3. Take ownership of their testing
		4. Take ownership of their releases
	3. Team Strategies
		1. Use the Strangler Pattern as opposed to big-bang rewrites
		2. Take ownership of your data
		3. Do not start with the hardest or most central part just because it is important.
			1. It is like untying a know
5. How do we measure progress
	1. Deployment frequency
	2. 


#### Other Thoughts to potentially incorporate ####
- Large releases with lots of testing are actually riskier than small releases with little testing
- Large releases are not only hard to release, they are also hard to roll back
- If a service still requires constant coordination, shared releases, or shared DB changes, it is probably not a real boundary.
- Decoupling a monolith is like untying a knot:
	- You can't start with the core
	- It gets easier and easier
- For true autonomy the team needs to have all the roles, not just engineers covering the full stack, but also:
	- Dedicated EM
	- Dedicated Product Owner
