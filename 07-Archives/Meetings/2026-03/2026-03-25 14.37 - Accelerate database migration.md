---
title: Accelerate database migration
subtitle: meeting notes
date: 03/25/2026 2:05 PM
meeting: 'true'
meeting-location: Microsoft Teams Meeting
meeting-recipients:
  - Arshad Mahammad
  - Curtis Nielsen
  - Laura Voegerl
  - Marten Engblom
meeting-invite: |
  Follow up on discussion on exchange database migration acceleration
  
  *	
  	Marten review possibility of adding Elastic migration in April/May timeframe
  *	
  	Arshad, review possibility of tightening Mongo timeline
  *	
  	Laura, any further budget implications
  
  
  Summary from prior call
  
  *	
  	Arshad budget implications is solely from additional compute costs, not change in savings.
  *	
  	Split of Audit DB from 1 to 4 database clusters
  *	
  	Split of Mongo from 1 to 3 database clusters
  
  
  ________________________________________________________________________________
  Microsoft Teams meeting 
  Join: https://teams.microsoft.com/meet/29901688687109?p=16d46tbVFiyTOS7dOs <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2Fmeet%2F29901688687109%3Fp%3D16d46tbVFiyTOS7dOs&data=05%7C02%7Cmengblom%40ghx.com%7C5defa412d58941d8243d08de892f937e%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639099034525889642%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=iHK3qts%2FiS4oMgjhDwt4PuQLREfqyL3QqpBb7%2BmQ8rk%3D&reserved=0>  
  Meeting ID: 299 016 886 871 09 
  Passcode: LK7Ek2Ce 
  ________________________________
  
  Need help? <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2FJoinTeamsMeeting%3Fomkt%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7C5defa412d58941d8243d08de892f937e%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639099034525920094%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=Sj1K%2BGxk6o29hZDKKpJwrFALqxogWHZBbcPLy35vE9Y%3D&reserved=0>  | System reference <https://nam02.safelinks.protection.outlook.com/ap/t-59584e83/?url=https%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%253ameeting_ZjQ5ZDUyMDEtZTI3OC00MWM4LWFhMWMtZmQwMGUzMzRlOWVj%2540thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%25223c2088fe-3969-4873-ac0d-dc9f122866b9%2522%252c%2522Oid%2522%253a%2522415bb1b0-61a7-4d69-aff4-ab30265c90f7%2522%257d&data=05%7C02%7Cmengblom%40ghx.com%7C5defa412d58941d8243d08de892f937e%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639099034525943988%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=7l6JAilKQlnLAhojVw2jaZTrVs2F28KcpglJXZxOxio%3D&reserved=0>  
  Dial in by phone 
  +1 719-569-4684,,994595107# <tel:+17195694684,,994595107#>  United States, Pueblo 
  Find a local number <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2F70057310-1f9b-4a61-8051-5cb24d3bb801%3Fid%3D994595107&data=05%7C02%7Cmengblom%40ghx.com%7C5defa412d58941d8243d08de892f937e%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639099034525969053%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=FFaC%2FgFA9mnwjQg%2F3wNgXrniNPw3WOGbE0ydQTvrQjc%3D&reserved=0>  
  Phone conference ID: 994 595 107# 
  For organizers: Meeting options <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2FmeetingOptions%2F%3ForganizerId%3D415bb1b0-61a7-4d69-aff4-ab30265c90f7%26tenantId%3D3c2088fe-3969-4873-ac0d-dc9f122866b9%26threadId%3D19_meeting_ZjQ5ZDUyMDEtZTI3OC00MWM4LWFhMWMtZmQwMGUzMzRlOWVj%40thread.v2%26messageId%3D0%26language%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7C5defa412d58941d8243d08de892f937e%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639099034525994602%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=hSIDvaVcHY%2B1MEUIm0b4tmo7NYXwb7haUoc3V2AwEz0%3D&reserved=0>  | Reset dial-in PIN <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2Fusp%2Fpstnconferencing&data=05%7C02%7Cmengblom%40ghx.com%7C5defa412d58941d8243d08de892f937e%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639099034526019015%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=jF8K%2BMOaHfqM1p4to2IXLsAl1UWLmsSjR758H0nRONY%3D&reserved=0>  
  ________________________________________________________________________________
  
---
Discussion about shortening the migrations:
- MongoDB to Atlas
- Elasticsearch to Elastic Cloud

Notes:
	- Currently the Elastic migration is scheduled to happen after MongoDB migration, which is scheduled to complete Aug 29.
	- Agreement that there is no real opportunity to shorten the MongoDB migration schedule