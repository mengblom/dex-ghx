---
title: Touchbase on DB Migration
subtitle: meeting notes
date: 03/06/2026 12:35 PM
meeting: 'true'
meeting-location: Microsoft Teams Meeting
meeting-recipients:
  - CJ Singh
  - Marten Engblom
  - Arshad Mahammad
  - Curtis Nielsen
meeting-invite: |
  
  ________________________________________________________________________________
  Microsoft Teams meeting 
  Join: https://teams.microsoft.com/meet/28141351928875?p=BJyvBGOeuWonhfVtWP <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2Fmeet%2F28141351928875%3Fp%3DBJyvBGOeuWonhfVtWP&data=05%7C02%7Cmengblom%40ghx.com%7Cd4b8e9fc09a84129957708de79ff6865%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639082335033254723%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=q4ErPcA%2BNzx1cZLHfJmMPtZfh%2F5V8zPMdKMtTZLksZk%3D&reserved=0>  
  Meeting ID: 281 413 519 288 75 
  Passcode: Mw7Np9Y3 
  ________________________________
  
  Need help? <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2FJoinTeamsMeeting%3Fomkt%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7Cd4b8e9fc09a84129957708de79ff6865%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639082335033280465%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=Bc58n2AN%2FfQk3jEMS6T5rhVOdqBazZiloYR8CdexOBg%3D&reserved=0>  | System reference <https://nam02.safelinks.protection.outlook.com/ap/t-59584e83/?url=https%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%253ameeting_N2M5NzE3OGMtNGUzNi00NzRjLWIzMDAtYzVjOGFkMDI1NDlk%2540thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%25223c2088fe-3969-4873-ac0d-dc9f122866b9%2522%252c%2522Oid%2522%253a%252279bc4844-1b13-4905-a442-9fd75a182a87%2522%257d&data=05%7C02%7Cmengblom%40ghx.com%7Cd4b8e9fc09a84129957708de79ff6865%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639082335033301320%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=F3y%2FCtypwoSGwKwMnZm6cjOyWwzqQbVXzB9%2BDSdPmSw%3D&reserved=0>  
  Dial in by phone 
  +1 719-569-4684,,858119804# <tel:+17195694684,,858119804#>  United States, Pueblo 
  Find a local number <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2F70057310-1f9b-4a61-8051-5cb24d3bb801%3Fid%3D858119804&data=05%7C02%7Cmengblom%40ghx.com%7Cd4b8e9fc09a84129957708de79ff6865%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639082335033322552%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=lTIKC1yJZgfX3u9Pz6a%2BNuVtGaSfhii4h1dT996Uahk%3D&reserved=0>  
  Phone conference ID: 858 119 804# 
  For organizers: Meeting options <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2FmeetingOptions%2F%3ForganizerId%3D79bc4844-1b13-4905-a442-9fd75a182a87%26tenantId%3D3c2088fe-3969-4873-ac0d-dc9f122866b9%26threadId%3D19_meeting_N2M5NzE3OGMtNGUzNi00NzRjLWIzMDAtYzVjOGFkMDI1NDlk%40thread.v2%26messageId%3D0%26language%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7Cd4b8e9fc09a84129957708de79ff6865%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639082335033349514%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=Bn9EWk7BX9Dr6g%2FnKbN7YVppmCiq3r8ZC96TwNZu4FI%3D&reserved=0>  | Reset dial-in PIN <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2Fusp%2Fpstnconferencing&data=05%7C02%7Cmengblom%40ghx.com%7Cd4b8e9fc09a84129957708de79ff6865%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639082335033370700%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=rlYPHQQBKfBcqsdnf%2FlWay7ahJoa%2Ft64W3DjXQ4XCyo%3D&reserved=0>  
  ________________________________________________________________________________
  
---
- Testing
	- How do we gain confidence in Perf environment
	- What are the metrics that were "yellow-ish" last time, that we should now be paying attention to
	- In general: What is a high confidence test plan, to build confidence in this strategy
- Communication
	- To the same audience as usual for DB upgrades
	- Keep it simple and stupid, but be clear
	- Timing
	- What to expect