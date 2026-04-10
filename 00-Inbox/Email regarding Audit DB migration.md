Partially due to CJ's ask: [[Quick call with CJ]]

All,

I think it goes without saying that this is a top priority for this week, and frankly until we are “done”. Here are some things we are going to need to get crisp on:

1. Firm decision on the plan and approach:
	1. Which route are we going – **sharding or cluster splitting**?
	2. **Who is doing what with respect to the application improvements?** I.e. items above the cutline here: [Post AuditDB Incident Brainstorming Session - Global Exchange Development - Confluence](https://prd.hub.ghx.com/wiki/spaces/EX/pages/997326849/Post+AuditDB+Incident+Brainstorming+Session)
		1. Jira stories
		2. Effort / ETA estimates
2. **What is the test plan** – we need this to be detailed both to build confidence for ourselves, and with management
	1. How are we **testing this in PERF**?
	2. **What is the delta between PROD and PERF**, i.e. how do we explain that we cannot fully replicated the issues experienced in PROD? And how to we bridge that gap?
	3. **What are the metrics/indicators we will look at in PERF testing?** With the benefit of hindsight, what are the metrics/indicators we should have paid more attention to last time around?
	4. Regarding all of the above, we should hold ourselves accountable with what we are looking for before we do the testing; i.e. **what will constitute green test results vs red test results?**
3. What is the **impact to the Atlas migration schedule?** Both in terms of roadmap and cost.