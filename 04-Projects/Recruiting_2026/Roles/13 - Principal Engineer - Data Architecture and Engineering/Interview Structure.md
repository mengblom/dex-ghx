### 1) Hiring Manager Screen

- Principal-level scope: evidence of driving cross-team/org-wide data outcomes
- Application engineering context: APIs, service design, deployment/SDLC awareness
- Datastore strategy judgment: choosing stores based on workload + tradeoffs
- Enablement mindset: empowering teams with guardrails and paved roads vs gatekeeping

### 2) Coding Interview (Data + App Patterns)
- Interviewers
	- Ali Inam
	- Ben Ludkiewicz
	- Pratik Panchal

- Understanding of application data-access anti-patterns (N+1, chatty calls, pagination/sorting, ORM pitfalls)
- Query performance depth: execution plans, cardinality/selectivity, query shaping, indexing strategy
- Safe evolution: zero-downtime schema/index changes, backfills, rollout/rollback thinking, write amplification tradeoffs
- Data movement fundamentals: CDC/outbox patterns, idempotency/dedup, replay/backfill, operational failure modes

### 3) System Design (Datastore Strategy + Distributed Data)
- Interviewers
	- Ali Inam
	- Ben Ludkiewicz
	- Pratik Panchal

- Workload-based datastore selection: hot/warm/cold/archive, OLTP vs analytics fit, cost/perf tradeoffs
- Distributed data strategy: system-of-record boundaries, avoiding shared DB coupling, shared reference data handling
- Cross-service data patterns: events/CDC, read models/materialized views, data contracts and versioning
- Reliability and scale: HA/DR, RPO/RTO, clustering/replication, partitioning/sharding, caching/connection management
- ML/LLM data architecture (lightweight): vector storage choices, embedding lifecycle, RAG patterns and boundaries

### 4) Behavioral / Culture / Team Fit
- Interviewers
	- Marten Engblom
	- Daniel Milburn
	- Curtis Nielsen
	- Mike Mitchell

- Influence and collaboration: working with strong app engineers, handling disagreement, aligning stakeholders
- Ownership and operational maturity: incident behavior, postmortem mindset, prioritization under pressure
- Teaching/enablement orientation: workshops, documentation, office hours, raising org capability
- Communication clarity: explaining tradeoffs to engineers and leaders; decision transparency

### 5) Architecture, Leadership & Influencing
- Interviewers
	- Marten Engblom
	- Daniel Milburn
	- Roger Andelin
	- Curtis Nielsen
	- Mike Mitchell

- Setting standards at scale: principles, guardrails, and adoption strategies that preserve autonomy
- Decision-making under tradeoffs: preventing datastore sprawl while avoiding centralized bottlenecks
- Org-level risk management: preventing OLTP misuse, performance degradation, and data quality drift
- Leading modernization: complex migrations, reliability improvements, and driving sustained change via mechanisms (patterns, templates, metrics)