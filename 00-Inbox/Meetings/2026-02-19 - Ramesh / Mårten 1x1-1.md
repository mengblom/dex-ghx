---
title: Ramesh / Mårten 1x1
subtitle: meeting notes
date: 02/19/2026 7:30 AM
meeting: 'true'
meeting-location: Microsoft Teams Meeting
meeting-recipients:
  - Ramesh Donnipadu
  - Marten Engblom
meeting-invite: |
  Setting up time for a weekly 1x1. I am flexible on time and day, let me know if you prefer a different time slot.
  
   
  
  ________________________________________________________________________________
  
  Microsoft Teams Need help? <https://aka.ms/JoinTeamsMeeting?omkt=en-US>  
  
  Join the meeting now <https://teams.microsoft.com/l/meetup-join/19%3ameeting_NTUxZWVkOTAtMzk1Yy00Yjc3LTlkZWItMTBmYjcyNzJlNDlj%40thread.v2/0?context=%7b%22Tid%22%3a%223c2088fe-3969-4873-ac0d-dc9f122866b9%22%2c%22Oid%22%3a%22e242dbd6-3608-410e-ade7-60c283b92b98%22%7d>  
  
  Meeting ID: 290 503 997 455 06 
  
  Passcode: MG6vq6oq 
  
  ________________________________
  
  Dial in by phone 
  
  +1 719-569-4684,,378903007# <tel:+17195694684,,378903007>  United States, Pueblo 
  
  Find a local number <https://dialin.teams.microsoft.com/70057310-1f9b-4a61-8051-5cb24d3bb801?id=378903007>  
  
  Phone conference ID: 378 903 007# 
  
  For organizers: Meeting options <https://teams.microsoft.com/meetingOptions/?organizerId=e242dbd6-3608-410e-ade7-60c283b92b98&tenantId=3c2088fe-3969-4873-ac0d-dc9f122866b9&threadId=19_meeting_NTUxZWVkOTAtMzk1Yy00Yjc3LTlkZWItMTBmYjcyNzJlNDlj@thread.v2&messageId=0&language=en-US>  | Reset dial-in PIN <https://dialin.teams.microsoft.com/usp/pstnconferencing>  
  
  ________________________________________________________________________________
  
   
  
  
---
- Ramesh had conversation with Laura Taylor about releasing often. Pushback from Laura "don't want to 'disturb' the customer every week"
	- We have to start getting our users used to this
	- Feature flags might be the solution?
	
- eInvoicing - Created Dataflow Diagram for data ingestion for feeds that enable smoothing of invoices. 
	- Files:
		- SELL file
			- Daily
			- Aka Vendor Master File
		- RMTX file
			- Daily
		- APO (Active Purchase Orders)
			- Daily
			- Can be really big... 500,000 rows, they send it every day.
			- Complete dump from their ERP, including POs completely unrelated to GHX
		- POHX
			- Daily
			- PO History of the last 60-90 days
			- Directly ingested in IPA and FS databases
		- Affiliate List
			- Ship-to-location of orgs who may have changed ownership
			- Excel file
			- Intermittent, not very often
	- All except Affiliate List comes to CoreX
	- Questions:
		- Why can't SELL, RTMX, Affiliate information be stored in Reg Center (TPM Database)
	- With that background:
		- Recent POC using Claude for document understanding
		- Looks very promising
	- Next steps?​
		- 
    
- Bautomate business case review is setup on 03/19 with Chrystie, CJ. I am trying to add Claude Code as an option. Would you or Curtis like to attend?​
	- Yes, I want to attend.
	- But questionable... given the Claude results (see above)
    
- Should we split the AWS assets per team (at least for IPA and Managed Services)? Or keep it aggregated under autona/autoeu?​
	- Definitely split it out
	- AWS costs should be tracked granularly, at least down to the service or product
     
- Hiring:​
    - EM for ICS team – local to Hyderabad requirement?​
	    - Have had bad experiences where people accept, then don't join
	    - Ramesh is willing to look at relocation candidates, but we need to apply some common sense 
    - IPA engineers – raise compensation or lower requirements?
	    - Since we already have 4 engineering UIPath experince, AND our intention might be to move away from UIPath, we can drop the UI Path requirement 