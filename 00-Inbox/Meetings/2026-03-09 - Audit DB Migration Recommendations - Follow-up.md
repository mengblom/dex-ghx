---
title: Audit DB Migration Recommendations - Follow-up
subtitle: meeting notes
date: 03/09/2026 2:30 PM
meeting: 'true'
meeting-location: Microsoft Teams Meeting
meeting-recipients:
  - Michael Knarr
  - Daniel Milburn
  - Thiyagarajan Murugan
  - Philippe Scoffie
  - Ben Ludkiewicz
  - Ali Inam
  - Arivazhagan Jeganathan
  - Arshad Mahammad
  - Jeff Sherard
  - Suresh Kumar
  - Marten Engblom
  - Gregory Bank
  - Michael Mitchell
meeting-invite: |
  AGENDA
  
  *	
  	Review the recommendations _ LOEs + assumptions 
  *	
  	Draft of a potential timeline
  
  
  ________________________________________________________________________________
  Microsoft Teams meeting 
  Join: https://teams.microsoft.com/meet/25537825294209?p=Ul9dAFcxaJwGGfqfXi <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2Fmeet%2F25537825294209%3Fp%3DUl9dAFcxaJwGGfqfXi&data=05%7C02%7Cmengblom%40ghx.com%7C2eb452a635a34ac33c1508de78ab28da%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639080873674244568%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=s1tI8UcK5B6R5MefUllO8ndX3CQpo3GX%2Bvy8Wa0tIi0%3D&reserved=0>  
  Meeting ID: 255 378 252 942 09 
  Passcode: mZ7qD6Pn 
  ________________________________
  
  Need help? <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2FJoinTeamsMeeting%3Fomkt%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7C2eb452a635a34ac33c1508de78ab28da%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639080873674270511%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=B%2BLznm9HLarXwYzwy78HRb74%2FOaEJmHiivTYjIdi67I%3D&reserved=0>  | System reference <https://nam02.safelinks.protection.outlook.com/ap/t-59584e83/?url=https%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%253ameeting_NWM2MTkyNjktZWJjMi00NTdkLTlhOTYtMzFiZTNlOTUwMTIy%2540thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%25223c2088fe-3969-4873-ac0d-dc9f122866b9%2522%252c%2522Oid%2522%253a%2522d1daa6c2-3b0b-42c4-b17b-dc43121326db%2522%257d&data=05%7C02%7Cmengblom%40ghx.com%7C2eb452a635a34ac33c1508de78ab28da%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639080873674291659%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=dKuKEBb1ckoD3E8rW6xbtwQ6nYYD61Y%2Fz6oDoLoOZzc%3D&reserved=0>  
  Dial in by phone 
  +1 719-569-4684,,184614760# <tel:+17195694684,,184614760#>  United States, Pueblo 
  Find a local number <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2F70057310-1f9b-4a61-8051-5cb24d3bb801%3Fid%3D184614760&data=05%7C02%7Cmengblom%40ghx.com%7C2eb452a635a34ac33c1508de78ab28da%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639080873674317991%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=lRlHADfXaBNR3hu3Z%2Bm%2BrFoj8fNzn7Mmt6l6D9NDmT4%3D&reserved=0>  
  Phone conference ID: 184 614 760# 
  For organizers: Meeting options <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2FmeetingOptions%2F%3ForganizerId%3Dd1daa6c2-3b0b-42c4-b17b-dc43121326db%26tenantId%3D3c2088fe-3969-4873-ac0d-dc9f122866b9%26threadId%3D19_meeting_NWM2MTkyNjktZWJjMi00NTdkLTlhOTYtMzFiZTNlOTUwMTIy%40thread.v2%26messageId%3D0%26language%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7C2eb452a635a34ac33c1508de78ab28da%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639080873674339485%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=v0%2B7RTfRhCd8jeOO0%2BJsFNKsSTO1Z5Vz74CL%2FB0qFHk%3D&reserved=0>  | Reset dial-in PIN <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2Fusp%2Fpstnconferencing&data=05%7C02%7Cmengblom%40ghx.com%7C2eb452a635a34ac33c1508de78ab28da%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639080873674360970%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=cUQO69i6xSOBQxAjSwe52G5rb09tydYuyDJV8yhFwm0%3D&reserved=0>  
  ________________________________________________________________________________
  
---
- Have decided together with Mongo consultants that Database Isolation is the best route (not sharding)
	- Mailbox
	- Notification
	- Statistics
	- Reasons:
		- Mailbox and Notification contributes 30-40% of the load
- Discussed whether we really need lower environments to be split onto multiple clusters
	- DEV - definitely not
	- STAGE - I would think not... although some argue that we still do some performance testing there. I would ask "why" since we have PERF
	- PERF - yes, for now
	- INT - Don't think so...?