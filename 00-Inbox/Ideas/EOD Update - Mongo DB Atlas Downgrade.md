		End of Day Update after executing the actions in [[Sync with MongoDB Support]]

All,

Here is an update, this is intended to be the last communication on this issue today (which is a great thing!)

Earlier this afternoon, Mongo DB Support came back to us an confirmed that a downgrade from v4.4 to 4.2 is indeed supported, and does remove the Durable History feature that has been identified as the culprit ever since we upgraded ~3 weeks ago. 

Here are the high level steps we have gone through:
1. Mongo DB Support provided us with a detailed runbook for the downgrade process
2. We tested the downgrade in our Performance environment. This went well.
3. At ~5:30pm we made the GO decision and started the downgrade on our Production Audit DB.
4. At 6:58pm we were done with the downgrade. Everything seems healthy at this point, and looks to be in a better and more stable state than before the downgrade.

We have also created an operations runbook targeted at taking much more aggressive steps (restarting our Audit DB cluster), as soon as we see signs of performance degrading towards a non-recoverable state, ***before*** there is any impact to the customers. We will use these more aggressive procedures for the foreseeable future if/when needed, although we think that we will not need them after the 4.2 downgrade.

In addition we have taken a couple of performance optimization steps:
- Added new indexes targeted at Notification queries that were performing poorly and added load to the system
- Released a hotfix to the Notifications application to take advantage of the indexes. The previously poorly performing queries are now executing <1s as opposed to several minutes in the past. This is definitely removing load from the DB, exactly how much is difficult to tell. 

As far as our Atlas migration plans:
- The Atlas migration for Audit DB US scheduled for this weekend is cancelled. We will regroup over the next few days to decide how to proceed, but the idea is that we will need to make some application/architecture/design changes before we migrate Audit DB US (which are desperately needed anyway)
- We are leaving the rest of the schedule intact for now. We will revisit over the next few days.