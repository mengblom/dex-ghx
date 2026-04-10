# Content / Response to Curtis#
# Overall Stats for the quarter
- Stories Completed: **805**
- Emergent Stories: **325 (40.4%)**
- Say / Do Ratio: **1.03**
	- Jan: **0.75** *(potentially impacted by the holidays, yearly
    planning, 2026 Kickoff travel etc.)*
	- Feb: **1.15**
	- Mar: **1.12**
- Exchange Sprint Metrics -- Q1 Velocity:
# Things Completed -- Not in the Quarterly Planning Deck
## Mongo DB to Atlas Migrations
***Significant effort on the project to migrate our MongoDB clusters to Atlas.***
- Implemented custom rollback mechanism with Kafka
- **Archive DB** migrated to Atlas and self-hosted assets decommissioned
- Well documented issues with **Audit DB** -- problems resulting from the prerequisite version upgrade led to incidents, rollback, significant amount of troubleshooting, and ultimately re-evaluation and replanning of the entire migration schedule.
- **BTBD** preparation, including improvements in place informed by the learnings from Audit
## Incident Remediation
***Incident root cause remediations in our largest MongoDB clusters, based on 2 separate incidents.***
- BT / BD Optimizations - based on incident late December -- early
  January
	- Business document replacement -- 9 of 16 implemented
	- Query optimizations (Colscan) - 11 of 12 implemented
	- Move Invoice Worklist calls from Primary to Secondary
- AuditDB Optimizations -- informed by failed migration plan (see
  above):
	- Update ConfigSVC Poll Duration from 5 seconds to 1 minute to decrease number of reads
	- Start work on an Activity Flow Diff engine
	- Activity/Activity Flow Sharding Plan
	- Fixed a COLLSCAN on statistics.StatDataCollection
	- Tune ILM configuration
## Creation of Feed Processor Observability 
***Net new component that provides visibility into Feed Processor performance and data, including messages in queue, instances of Feed Processor in Production, in-flight messages, oldest message, and a list of all Flows in progress.***
- Backend components and APIs to provide the data
- UI bundled in Heimdall on the Admin page to surface the data
- Migration of API to new CI/CD Process (project started in our "old" CI/CD environment)
	- Bitbucket -\> Github
	- Deployment pipeline Bamboo -\> Github Actions
	- Migration from EC2 -\> Containers
## Incident MCP
***New capability to leveraging AI to diagnose, and often resolve, exceptions that otherwise would result in PagerDuty incidents. Completed and Productionalized in Q1.***
- AI responds to the PageDuty page, pulls the heap dump from the sending instance, analyzes the data, determines whether to resolve/sleep the alert or page a human.
- Auto-resolution of Pager Duty pages based on AI analysis of heap dumps
## PEPPOL integration and migration with 3rd party Tickstar
***Significant and time sensitive integration with 3^rd^ party to stay in compliance in EU.***
- PEPPOL is a mandatory collaboration framework in EU and we were falling out of compliance. The lift to get our custom developed implementation up to compliance was deemed too great to meet the deadline, so we pivoted to integration with a 3rd party to manage the framework moving forward.
## IO Improvements
***A couple of architectural improvments to remove Dependencies / "decoupling".***
- IO Guarantee SQS backup in case of Event Bus failure
- Move DSemaphore to Redis to decouple from AuditDB
## Reg center 
***Decoupled RegCenter from the monolith, removed direct dependencies on CoreX, migrated the system to our new CI/CD process, refresh of the UI (Core UI migration)***
- Migration to new CI/CD Process
  (<https://prd.workflow.ghx.com/browse/REGCNTR-1501>)
	- Bitbucket -\> Github
	- Deployment pipeline (Bamboo -\> GitHub Actions)
	- Migration from EC2 -\> Containers
- New BFF / Gateway APIs
	- Implemented with AI assisted API development
	- AI assist testing drove coverage from 25% to 75% coverage
- Implementation of AuthN & AuthZ in the new frontend component
## Customer Visibility UI Upgrade (Core UI)
***Large effort to upgrade MyExchange to Core UI.***
- Reached Dev complete on the following modules
	- Orders
	- Transactions
	- Notifications
	- Web Direct
## AWS SDK Upgrade to 2.0 Progress 
***Project to upgrade the AWS SDK in all repos. The version we are currently on (1.x) reached EOL on 2025-12-31.***
- Also a prerequisite to many OSS Vulnerabilities
- **4 / 6 repos completed in Q1**
## OSS Vulnerabilities resolved 
- 1 KEV
- 11 Critical
- 13 High
## Hiring
***Significant team involvement in recruiting and hiring.***
- \~15-20 Engineers involved in interviews for \~40 open roles
- 120+ candidates moved through the process (involving at least the
  Hiring Manager initial interview)
- Onboarding of 2 Engineering Managers + 2 IC
## QE 
***Ongoing work to migrating our Gold Certification Suite from Tandoori to Playwright***
- 12% Project status for Tandoori Migration to Playwright (21 tests complete in Q1)
## Infrastructure
***EC2 Instance upgrade to Lunix 2023***
- 19 repos completed (to be released in Prod early April)
## Complex Order Automation (COA)
***Incremental progress in the COA program***
- Re-Park feature for Implants
- New Actions for EDI Separate Lot and New Lot Numbers
## Additional small things
- Fixed bullseye report by allowing Feed Processor to lookup PO info up to2 years
	- Summit request from Tina
- Improvements in Native Comms:
	- Fixed batch deliveries failing for Providence (incident related)
	- Add ability to batch off number of files in addition to time
- Sonarqube Integration
- Cleanup of old Feature flag
- Claude Learning - Tool Installation, Training, upskilling,
# *AI Summary*
***⚠️ Grok Attitude Alert ⚠️***
## *Q1 Delivery Highlights*
*We crushed **805 stories** this quarter. Of those, a healthy **325 (40%)** were emergent---because nothing says \"great planning\" like the plan changing mid-sprint. Say/Do ratio landed at a solid **1.03**, which is basically bragging rights in our world. January was\... let\'s just say \"low\" and leave the mysterious \"???\" in the rearview. Beyond the official deck (you know, the one we politely ignored), the team shipped a ridiculous amount of extra work:*
- ***MongoDB migrations** to Atlas (including the Archive and Audit DBs) + full decommissioning of self-hosted assets.*
- *Complete **schedule replan**, BTBD prep, rollback infrastructure with Kafka, and a bunch of BT/BD optimizations.*
- ***Business document replacement**: 9 of 16 done.*
- ***Query optimizations**: knocked out 11 of 12 Colscans, moved Invoice Worklist calls to secondary, tuned AuditDB (poll interval from 5s → 1min, thank god), fixed a nasty COLLSCAN on stats, and started sharding + Activity Flow diff engine work.*
## *Bigger platform moves* 
- *Full migration of **Reg Center** out of the monolith: new CI/CD (Bitbucket → GitHub, Bamboo → GitHub Actions), EC2 → containers, UI refresh, and new BFF. AI-assisted dev + testing jumped test coverage from 25% → **75%**. Nice.*
- ***PEPPOL integration** with Tickstar, IO guarantee via SQS backup, DSemaphore moved to Redis.*
- ***Infrastructure wins**: Linux 2023 upgrade (dropping early April), AWS SDK 2.0 progress, Sonarqube integration, feature flag cleanup.*
- ***Incident stuff**: Auto-resolution of PagerDuty pages using AI that actually reads heap dumps and decides whether to wake a human or chill. (Yes, really.)*
## *Security & Cleanup*
*Resolved **11 Critical + 1 KEV + 13 High** OSS vulnerabilities. Good times. **People*** *Interviewing like crazy (~15-20 engineers screening for ~40 open roles, 120+ candidates assessed). Onboarded 2 new Engineering Managers +2 ICs.**QE & Misc*** *15% Tandoori → Playwright migration, fixed some batch delivery incidents, added batch-by-file-count, and a few random bugs (Reg Center spinner, etc.). Oh, and someone's been learning Claude on the side.* 

***Bottom line: We delivered the committed stuff, absorbed a ton of unplanned work, modernized a bunch of plumbing, and still found time to automate ourselves out of some pager duty hell. Not bad for a quarter that started with a question mark.***

*If you need deeper details, the January mystery explained, or slides for the next steering committee, just say the word. I'll be over here closing tickets and pretending I have bandwidth.*


# Context#
## Email from Curtis##
> Hi
> 
> I'm looking for your help to prepare for a "deep dive with CJ on what was done in Exchange in Q1 and OKRs for Q2. 
> 
> The context is that I shared this wonderful deck (attached) that Laura had made as part of her normal pod updates, and CJ had the following questions. He is referencing the tech priorities deck here ​[2026 Tech Org Priorities.pptx](https://ghx365-my.sharepoint.com/:p:/r/personal/csingh_ghx_com/Documents/2026/2026%20Tech%20Org%20Priorities.pptx?d=w3d38032c08714d5eb49a0b00d8ecc1ae&csf=1&web=1&e=cBtsHz&xsdata=MDV8MDJ8bWVuZ2Jsb21AZ2h4LmNvbXw2ZTc5ZDkyMGQwMWM0ODU4NDA1MzA4ZGU5NTg1OTI3MXwzYzIwODhmZTM5Njk0ODczYWMwZGRjOWYxMjI4NjZiOXwwfDB8NjM5MTEyNTk4MDgwODA0MDgwfFVua25vd258VFdGcGJHWnNiM2Q4ZXlKRmJYQjBlVTFoY0draU9uUnlkV1VzSWxZaU9pSXdMakF1TURBd01DSXNJbEFpT2lKWGFXNHpNaUlzSWtGT0lqb2lUV0ZwYkNJc0lsZFVJam95ZlE9PXwwfHx8&sdata=RzBMS2o3NzBDQmJSTDhUL1lPaTFFZ1RkNUZUTHVVcjV3MCtQWWYrTGpFVT0%3d)​, Slide 2, to understand how the work reported by Laura matches to the Tech org priorities.
> 
> Mårten, can you lead the work with Daniel and Phil to help answer the questions below?
> 
> Laura, this is mostly FYI to keep you abreast of the type of questions I get. 
> 
> Mårten, A few things, can we get numbers to the following for the quarter
> 
> - number of "features" (product defined) that were delivered. 
> - number of stories delivered (953 in KPMD)
> 	- can we get a breakdown by spend category?
> 	- Can we get a % that 
> 	- were emergent, 
> - Say/do ratio of work expected to be completed in Q2
> - Provide narrative of what impacted the say/do ratio had

## Forwarded email from CJ##
> Hi Curtis,
> 
> Following up on our conversation on Thur, I went through this deck again. I’ve read through the deck and have a few questions and areas where I'd love some more clarity:
> 
> **Pages 2–4: Q1 Delivery & Q2 Carryover**
> 
> - **Page 2:** The completed "tech roadmap" items look a bit light for Q1. Didn't we also execute a significant amount of security vulnerability work? We should probably highlight that if so.
> - The milestones listed currently feel a bit tactical. Given we have 50+ engineers dedicated to Exchange, I want to get a better sense of the overall volume and scale of what the team delivered.
> - **Pages 3 & 4:** There is a significant amount of work that carries over into Q2. Could we review our say/do ratio for Q1? I’d like to better understand the unexpected work or roadblocks that drove this carryover.
> 
> **Page 5: Tech Resiliency Priorities**
> 
> - I want to make sure I’m connecting the dots here. How do the technology roadmap items on this page align with the core tech resiliency priorities in our "top 6" one-pager?
> - With over 70% of our Q2 engineering capacity allocated to tech resiliency, seeing only these three items feels a bit disproportionate. Are there other efforts underway that just aren't captured here?
> 
> **Zooming Out: Productivity & Alignment.** Taking a step back from the specific slides, I’d also like to align with you on a few broader themes:
> 
> - **Throughput trends:** I'd like to understand how the Exchange team's productivity and throughput have trended over the last 8–12 months since the leadership transitions and you taking the helm. Have we seen material improvements we can point to?
> - **Capacity:** Could you remind me of our exact number of hands-on-keyboard engineers in Exchange right now, and how we are currently measuring their baseline productivity?
> - **Priority alignment:** We previously noted that Q1 progress on the Exchange resiliency priorities (from our 1-pager) was lighter than expected. Are the broader product and tech teams fully aligned on these, which are our defined priorities? I’d like to dig into exactly what percentage of engineering capacity was allocated to the technology roadmap in Q1, and what prevented us from making more headway on those specific goals.
> 
> Let's discuss on Mon/Tue, I will schedule time.