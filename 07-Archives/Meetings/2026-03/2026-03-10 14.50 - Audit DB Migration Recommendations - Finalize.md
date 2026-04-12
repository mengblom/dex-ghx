---
title: Audit DB Migration Recommendations - Finalize
subtitle: meeting notes
date: 03/10/2026 2:30 PM
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
  - Selvakumar Samiappan
  - Michael Mitchell
meeting-invite: |
  Context: Direction selected on Monday. Let's finalize the details of the approach
  AGENDA 
  
  *	
  	Discuss app optimizations - Dev effort
  *	
  	Test plan - salient points + metrics
  *	
  	Test boundaries & acceptance margins
  
  
  
  ________________________________________________________________________________
  Microsoft Teams meeting 
  Join: https://teams.microsoft.com/meet/24798274560322?p=DDUcryPAkhNjTi2jjN <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2Fmeet%2F24798274560322%3Fp%3DDDUcryPAkhNjTi2jjN&data=05%7C02%7Cmengblom%40ghx.com%7C69424ab1cd444b9c7e4608de7e225711%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639086883122062302%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=uEXsDQG%2B7Jm93l%2FB9up%2FSEQ1GC4LzWy5mFvVSa9YYlY%3D&reserved=0>  
  Meeting ID: 247 982 745 603 22 
  Passcode: aW6em7W2 
  ________________________________
  
  Need help? <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2FJoinTeamsMeeting%3Fomkt%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7C69424ab1cd444b9c7e4608de7e225711%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639086883122091500%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=9THhntu%2BJGesCEZgfrz5MF2ihNemS91hG5OTT5OLTf0%3D&reserved=0>  | System reference <https://nam02.safelinks.protection.outlook.com/ap/t-59584e83/?url=https%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%253ameeting_Yjc4NjA3NmYtZGU0Yi00NDc0LWJmMmYtYThhODM2ZDkyYmZh%2540thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%25223c2088fe-3969-4873-ac0d-dc9f122866b9%2522%252c%2522Oid%2522%253a%2522d1daa6c2-3b0b-42c4-b17b-dc43121326db%2522%257d&data=05%7C02%7Cmengblom%40ghx.com%7C69424ab1cd444b9c7e4608de7e225711%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639086883122113279%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=FxgoYk9GXi%2BwFvq3P7lHrJoH89lXZ150A8bUE5x7oEg%3D&reserved=0>  
  Dial in by phone 
  +1 719-569-4684,,338336530# <tel:+17195694684,,338336530#>  United States, Pueblo 
  Find a local number <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2F70057310-1f9b-4a61-8051-5cb24d3bb801%3Fid%3D338336530&data=05%7C02%7Cmengblom%40ghx.com%7C69424ab1cd444b9c7e4608de7e225711%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639086883122134822%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=wAC%2FKNIRhZhBlh1YUVtfFEP9aNDafLf6JinpIFVYWWg%3D&reserved=0>  
  Phone conference ID: 338 336 530# 
  For organizers: Meeting options <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2FmeetingOptions%2F%3ForganizerId%3Dd1daa6c2-3b0b-42c4-b17b-dc43121326db%26tenantId%3D3c2088fe-3969-4873-ac0d-dc9f122866b9%26threadId%3D19_meeting_Yjc4NjA3NmYtZGU0Yi00NDc0LWJmMmYtYThhODM2ZDkyYmZh%40thread.v2%26messageId%3D0%26language%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7C69424ab1cd444b9c7e4608de7e225711%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639086883122156092%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=CNf9EjjZk92906CIuBo4%2BE9wflJ0rKXpWAW6yJntPFE%3D&reserved=0>  | Reset dial-in PIN <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2Fusp%2Fpstnconferencing&data=05%7C02%7Cmengblom%40ghx.com%7C69424ab1cd444b9c7e4608de7e225711%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639086883122178683%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=p6I7XLq9XbRA%2BNyMQwgJMgHibSNzZhRgz7kX1ZGHaEg%3D&reserved=0>  
  ________________________________________________________________________________
  
---
