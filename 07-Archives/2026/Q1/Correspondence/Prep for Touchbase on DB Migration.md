- Recommendations from Mongo support team:
	- Phase 1: Index Optimizations
	- Phase 2:
		- Option A: Application optimizations
		- Option B: Migrate to MVP sharded cluster (recommended option)
			1. Stand up a new Atlas cluster
			2. Start the data mirroring
			3. Shard the new cluster (or maybe this happens before mirroring starts?)
			4. Now we are in a situation where:
			    1. Our current on-prem cluster is unchanged (4.2, not sharded)
			    2. In Atlas we are on v8, sharded
			5. Now we cut over to the new v8, sharded, Atlas clusters.
- Recommendations from GHX
	- Agree with Mongo recommendations (Phase 1 + Phase 2.B.)
	- In addition, we want to do some application and/or architecture changes:
		1. Increase the poll time to the CONFIGURATION collection from 5s to 5 minutes
		2. Do field-level updates instead of full document replace
			- Need to enumerate all the places needing update
			- Doesn't have to be all or nothing, can be done gradually, if there are multiple places in the code that needs to change
		3. Adjust the timing of batch processing
			- Don't have good catalog of jobs (~100 of them) and their timing 
		4. Move collections out of Audit 
			- Easy on the application side, unknown DBA effort
			- Candidates collections:
				- MAILBOX collection to separate cluster (remove dependency)
					- Noisy neighbor - isolate the STFP endpoint from issues
					- Still TBD:
						- need to determine if there other dependencies 
				- NOTIFICATIONS database out of Audit
					- The source of heavy queries
					- Might have been alleviated with the new indexes (need to check with DBAs)
				- STATISTICS collection to separate cluster	
- Timeline
	- Not 100% known
	- Mongo is validating their recommended approach, but are saying  saying 1-2 months
	- GHX is validating / effort sizing the application level improvements; BUT my recommendation is that we timebox these efforts to the timeline for Phase 2.B.