---
tags:
  - team-charter
  - enabling-team
  - data-architecture
  - 2026-org
created: 2026-03-12
team-type: enabling
---

# Data Architecture and Engineering - Team Charter

## Purpose

Provide data architecture expertise and leadership to enable autonomous teams to make sound data decisions. Establish patterns, standards, and best practices for data modeling, storage, processing, and access across the organization.

## Core Responsibilities

### Data Architecture & Modeling
- Design and review data models (including bi-temporal models, normalization strategies)
- Schema design and evolution strategies (versioning, backward compatibility)
- Data modeling for scale (sharding, partitioning, purging strategies)
- Define data domain boundaries and ownership

### Technology Strategy & Standards
- Evaluate and recommend data storage technologies (SQL, NoSQL, document stores, time-series, graph)
- Consider read/write patterns, data volumes, access patterns when selecting technologies
- Establish technology standards and evaluation criteria
- Proof-of-concept new data technologies
- Cost optimization for data services

### Performance & Optimization
- Query optimization, indexing strategies, execution plan analysis
- Database performance tuning and resource management
- Caching strategies and trade-offs
- ORM vs direct SQL guidance

### Data Platforms & Integration
- Define data access patterns (APIs, direct access, events, file-based)
- Data replication and syndication strategies (CDC, event streaming, batch)
- Analytics platforms, warehouses, and read replicas
- ETL/ELT pipelines and data processing patterns
- Data integration between systems and teams

### Operational Excellence
- Data quality standards and validation
- Monitoring, alerting, and observability for data systems
- Data migration strategies (zero-downtime, blue-green deployments)
- Incident response for data-related issues
- SLOs for data services

### Team Enablement
- Consult with application teams on data architecture decisions
- Code and architecture reviews
- Knowledge sharing (workshops, documentation, office hours)
- Create reusable patterns and reference implementations

## Team Model

**Enabling team approach:**
- Consult and educate, not gatekeep or mandate
- Embed with teams for complex problems, then transfer knowledge
- Office hours for questions and quick consultations
- Architecture reviews as learning opportunities
- Success = teams make good data decisions independently

## Initial Priorities (First 90 Days)

1. **Assessment**: Inventory current data systems, identify pain points and quick wins
2. **Standards**: Document existing patterns, establish guidelines for common scenarios
3. **Engagement**: Meet with each team, understand needs, establish consultation model
4. **Tooling**: Evaluate data tooling landscape, recommend standards, identify gaps

## Success Metrics

- Teams confidently make data decisions without us for routine scenarios
- Data-related incidents are rare and quickly resolved
- Teams deploy data changes independently and safely
- Common data anti-patterns are avoided
- Data architecture patterns are documented and adopted
- We're consulted for novel/complex problems, not routine decisions

## Team Composition

**Initial**: One Principal Engineer

**Growth**: 2-4 person team with expertise across SQL/NoSQL, data processing, analytics, and cloud data services

---

*Living document - will evolve as team and organization mature.*
