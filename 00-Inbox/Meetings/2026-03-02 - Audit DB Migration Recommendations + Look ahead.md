---
title: Audit DB Migration Recommendations + Look ahead
subtitle: meeting notes
date: 03/02/2026 2:30 PM
meeting: "true"
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
meeting-invite: |-
  AGENDA

  *	
  	Review the options for migrating Audit DB + considerations for the rest of the migrations
  *	
  	Review recommendations and rationale
  *	
  	Next Steps 


  ________________________________________________________________________________
  Microsoft Teams meeting 
  Join: https://teams.microsoft.com/meet/21027290400202?p=BdtCPbpn4skhof0RjK <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2Fmeet%2F21027290400202%3Fp%3DBdtCPbpn4skhof0RjK&data=05%7C02%7Cmengblom%40ghx.com%7C4891dadec6644b20111f08de765b4b03%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639078331652542103%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=FD%2FnoG%2BdPEXej5We2q3x1xlN8iRS3UqTdkZAz3JgfX0%3D&reserved=0>  
  Meeting ID: 210 272 904 002 02 
  Passcode: vw78wd2t 
  ________________________________

  Need help? <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2FJoinTeamsMeeting%3Fomkt%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7C4891dadec6644b20111f08de765b4b03%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639078331652572465%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=IaMaA4z06E%2BNV45CS53n4rAszO69rkO7UscSs3f8Na0%3D&reserved=0>  | System reference <https://nam02.safelinks.protection.outlook.com/ap/t-59584e83/?url=https%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%253ameeting_MTFlOWI1MjMtOWVlZC00MTYwLTk1NWEtNjMzMDE0MmJiYjk0%2540thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%25223c2088fe-3969-4873-ac0d-dc9f122866b9%2522%252c%2522Oid%2522%253a%2522d1daa6c2-3b0b-42c4-b17b-dc43121326db%2522%257d&data=05%7C02%7Cmengblom%40ghx.com%7C4891dadec6644b20111f08de765b4b03%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639078331652593846%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=bzK3UX2QS07w6iLK9IVmVGoYorgK9KDXMdklyi2eVJs%3D&reserved=0>  
  Dial in by phone 
  +1 719-569-4684,,660645639# <tel:+17195694684,,660645639#>  United States, Pueblo 
  Find a local number <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2F70057310-1f9b-4a61-8051-5cb24d3bb801%3Fid%3D660645639&data=05%7C02%7Cmengblom%40ghx.com%7C4891dadec6644b20111f08de765b4b03%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639078331652615028%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=A1nBpODDoiWe%2BC7SFXWN%2Bb6v9K2ROAJa56cnnpQwJ%2B0%3D&reserved=0>  
  Phone conference ID: 660 645 639# 
  For organizers: Meeting options <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2FmeetingOptions%2F%3ForganizerId%3Dd1daa6c2-3b0b-42c4-b17b-dc43121326db%26tenantId%3D3c2088fe-3969-4873-ac0d-dc9f122866b9%26threadId%3D19_meeting_MTFlOWI1MjMtOWVlZC00MTYwLTk1NWEtNjMzMDE0MmJiYjk0%40thread.v2%26messageId%3D0%26language%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7C4891dadec6644b20111f08de765b4b03%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639078331652636104%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=yW%2BZlWz5SbNY1qEfjZ4cXqsq%2FcT6aeDCnIZ2qwC7dnE%3D&reserved=0>  | Reset dial-in PIN <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2Fusp%2Fpstnconferencing&data=05%7C02%7Cmengblom%40ghx.com%7C4891dadec6644b20111f08de765b4b03%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639078331652657256%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=QxdK6KKdf5mYiJXs7937ZFca8P4TCT6D29%2FSJ6TQXyo%3D&reserved=0>  
  ________________________________________________________________________________
---
Discuss options for Migrating Audit DB:
[Audit DB Incidents impacting Atlas migration (Feb 2026) - Global Exchange Development - Confluence](https://prd.hub.ghx.com/wiki/spaces/EX/pages/975437830/Audit+DB+Incidents+impacting+Atlas+migration+Feb+2026)

