Hello CJ,

Here is a summary of the current work in progress. We are scheduled to come back together at 2pm mountain time to regroup.

1. Rolling Restart Runbook & Decision Criteria
	1. *Zach Knarr* is putting this together
	2. We really only need to look at 1 datapoint: Dirty Cache > 20%, this is a sure sign we are heading for an unrecoverable situation. We typically see this before there is any impact to document transaction times, and we should hence be able to avoid customer impact of that nature.
	3. We are still working on qualifying and quantifying the risk of (or lack thereof) customer impact as a result of a rolling restart. 
2. Short term performance improvements to Notification queries
	1. **Deploy hotfix to remove misdirected query hint**. In testing this improved query performance from minutes to sub-second, which naturally has a positive impact on DB load. *Suresh is working on this.* 
	2. **Add index targeted to the Notification queries.** Even with a much better performance per above, unnecessary collection scans are taking place, which this added index will resolve. *Jeff is working on this.*
	3. **Add mechanism to halt Notification queries if needed** (dedicated DB user for which we can revoke permissions). *Suresh and Jeff are working on this.*
	4. **Further log analysis and identification of additional short term improvements**. *MongoDB Support is working on this.*
3. Preparation and readiness assessment for Atlas upgrade
	1. Deeper risk/benefit opinion, confidence level, rollback options etc. *Mongo Support is working on this.*
	2. When is the soonest we can be ready with confidence. *Jeff + others on the GHX side are working on this.*

Happy to talk through anything or everything.

Marten
