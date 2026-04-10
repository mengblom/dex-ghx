---
title: Atlas Mig Mongo Schedule Review
subtitle: meeting notes
date: 03/12/2026 4:00 PM
meeting: 'true'
meeting-location: Microsoft Teams Meeting
meeting-recipients:
  - Suresh Kumar
  - Ben Ludkiewicz
  - Michael Knarr
  - Philippe Scoffie
  - Jeff Sherard
  - Daniel Milburn
  - Marten Engblom
meeting-invite: |
  AGENDA
  
  *	
  	Review the Mongo schedule & confirm viability
  
  
  ________________________________________________________________________________
  Microsoft Teams meeting 
  Join: https://teams.microsoft.com/meet/29198184836538?p=plrnK2DJiPIrs5k6ca <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2Fmeet%2F29198184836538%3Fp%3DplrnK2DJiPIrs5k6ca&data=05%7C02%7Cmengblom%40ghx.com%7C13a0088bef124c319d9208de80500bd4%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639089278446644687%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=C3IpNXfwkdhc40%2BXSz6%2F49TLRdjm47GoixfxdPFMedI%3D&reserved=0>  
  Meeting ID: 291 981 848 365 38 
  Passcode: uG7fh7W5 
  ________________________________
  
  Need help? <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2FJoinTeamsMeeting%3Fomkt%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7C13a0088bef124c319d9208de80500bd4%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639089278446682400%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=gl81sKV9yxJcJjJ6mAQToVoyR0VSfyoFZ8u7B2Az3pQ%3D&reserved=0>  | System reference <https://nam02.safelinks.protection.outlook.com/ap/t-59584e83/?url=https%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%253ameeting_MGFiYmFlYWMtMTJlYy00YTlhLTg5NDYtNzY0OGNmZmMyOWJj%2540thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%25223c2088fe-3969-4873-ac0d-dc9f122866b9%2522%252c%2522Oid%2522%253a%2522d1daa6c2-3b0b-42c4-b17b-dc43121326db%2522%257d&data=05%7C02%7Cmengblom%40ghx.com%7C13a0088bef124c319d9208de80500bd4%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639089278446721918%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=CaGOyEQXyACX1CwRrK7qm4GM3GubYX74kdEaX6Dpx%2Bs%3D&reserved=0>  
  Dial in by phone 
  +1 719-569-4684,,996526311# <tel:+17195694684,,996526311#>  United States, Pueblo 
  Find a local number <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2F70057310-1f9b-4a61-8051-5cb24d3bb801%3Fid%3D996526311&data=05%7C02%7Cmengblom%40ghx.com%7C13a0088bef124c319d9208de80500bd4%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639089278446758806%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=SyKxgx%2BU%2BCvAuhOViBQvku4jRQRUd9fFRGKwDxVyuQA%3D&reserved=0>  
  Phone conference ID: 996 526 311# 
  For organizers: Meeting options <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2FmeetingOptions%2F%3ForganizerId%3Dd1daa6c2-3b0b-42c4-b17b-dc43121326db%26tenantId%3D3c2088fe-3969-4873-ac0d-dc9f122866b9%26threadId%3D19_meeting_MGFiYmFlYWMtMTJlYy00YTlhLTg5NDYtNzY0OGNmZmMyOWJj%40thread.v2%26messageId%3D0%26language%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7C13a0088bef124c319d9208de80500bd4%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639089278446788300%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=rQ4QFvurV8huHUPVdpW5%2BgCdoSv%2F%2FnEDIG%2BAP1MIhNM%3D&reserved=0>  | Reset dial-in PIN <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2Fusp%2Fpstnconferencing&data=05%7C02%7Cmengblom%40ghx.com%7C13a0088bef124c319d9208de80500bd4%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639089278446813396%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=I8Sip%2B%2BF1RvIvRfV9HGr%2FlKslK74UzygUnTgbsVKgiI%3D&reserved=0>  
  ________________________________________________________________________________
  
---
- Reviewing the Atlas migration timeline / Gantt chart from Mongo
	- 