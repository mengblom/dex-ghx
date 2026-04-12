Follow to [[Audit Mongo DB Status & Update to CJ]]

* Update from Mongo:
	* New Info: We are back to Downgrading to 4.2 (4.2.23, or 4.2.13)
		* Recommendation is to go to the latest patch (4.2.23)
			* This is the downgrade that has been most tested
		* Removes the Durable History files
		* Confident, this comes from the engineering team
		* Upgrade Process:
			* Set FCB to 4.2
			* Stop 1 node
			* Replace binaries
			* Bring it back up
			* Will take 2.5 - 3 hours
		* The plans is to write up the playbook, test in our Performance Environment, take a go/no-go decision for production downgrade
		* Plans to get to Atlas will be revisited after we are stable
			* There is now a path straight from 4.2 to Atlas, but potentially with some drawbacks
	* Mongo Support Analyzed yesterday's logs uploaded overnight
		* 3 collections where the number of index keys modified (11,000+)
			* Each index keys means 1 page that becomes dirty and has to be updated
				* Notifications.Alerts
				* Notifications.AlertMessages
				* Statistics.AccountUtilizations
* Short term performance improvements to Notification queries 
	* New Notifications indexes have been applied
	* Hot Fix is being built, ETA for PROD is 4:30pm
	* 