CJ,

Here is an update on the Audit DB migration, and Atlas Migration schedule.

Please treat this information as ***tentative*** for now - there is a **meeting tomorrow at 11:00 to do a final review and commit to the plan**.

- **Audit DB migration approach**  – The approach remains: immediate index optimizations + Atlas migration from 1 hosted cluster to multiple managed Atlas clusters (database splitting). This is a change in direction (from sharding) based on DB profiling and analysis.
	- Will reduce load significantly (spread it over 3 clusters instead of 1)
	- Will decouple some current unfortunate dependencies, most notably the SFTP mailbox database
	- Implementing application improvements in parallel. 
- **Testing** - The details are still being finalized but:
	- The schedule includes an extended period of testing on PERF and STG.
	- Working on pre-set metric targets for what constitutes green vs. red tests.
	- Testing includes scaling down the PERF instances to the same size as on Atlas
- **Cutover** - planned for **4/18 in EU** and **4/25 in US**

**The overall Atlas Migration schedule:**
- The latest version goes to **Aug 27**
- There is **performance / load mitigation work to do on BT/BD** similar to Audit (although BT/BD has a different load profile, and we have not seen any issues here, even while being on v4.4)
- We cannot sync data during quiet periods in Production. **No activities planned between June 21 and July 5th**.

I will follow up with another update tomorrow.

Marten
