**Subject: DB Migration Update - Touchbase Pre-Read**

Ahead of our touchbase, here's a summary of our Audit DB migration approach and timeline:

**RECOMMENDED APPROACH**

Working with MongoDB support and GHX, we've aligned on a two-phase strategy:

- **Phase 1: Index Optimizations  
    **_low effort, potential medium/large impact, low risk_
- **Phase 2: Migrate to Sharded Atlas Cluster (MVP), without intermediate upgrade step (i.e. avoid v4.4):**

- Approach:

1. Stand up new Atlas cluster (v8)
2. Start data mirroring from current on-prem cluster (4.2)
3. Shard the new cluster
4. Cut over to the new v8, sharded Atlas environment

- _This bypasses immediate application-level changes._
- _Pressure relief can be validated in performance testing._
- _Once sharded on Atlas, optimization and refactoring can be done with a live feedback loop, enabling faster recommendations and updates from RCE, DBA, and Technical Support._
- **_Remaining concerns are v8 has the Durable History feature, and Atlas is running on smaller instances. These are mitigated by optimizations from multiple major version upgrade (4-8), the sharded workload + other improvements._**

**PARALLEL APPLICATION IMPROVEMENTS**

**_In addition,_** to optimize performance and support the migration, we're pursuing these application-level changes (timeboxed to Phase 2 timeline):

1. **Configuration polling** - Increase poll interval from 5s → 5 minutes  
    _low effort, low risk_
2. **Update strategy** - Implement field-level updates vs. full document replace  
    _low/medium effort, potential high impact, low risk, gradual approach possible_
3. **Batch processing timing** - Adjust ~100 batch jobs scheduling (requires cataloging effort)  
    _low effort, low risk, unknown benefit, gradual approach possible_
4. **Collection isolation** - Move high-impact collections to separate clusters:  
    _medium effort (at least), medium impact, medium risk_
	- MAILBOX collection (eliminate noisy neighbor issues for SFTP endpoint)
	- NOTIFICATIONS collection (source of heavy queries; may be resolved by new indexes)
	- STATISTICS collection

**TIMELINE**

- **MongoDB** team is validating the approach: **1-2 months** estimate as of now
- **GHX** is sizing application improvement efforts, timeboxed to Phase 2 delivery
	- DBA input on effort standing up new clusters
	- Evaluation of application engineering efforts
	- Cataloging and evaluating current batch process schedule and load
