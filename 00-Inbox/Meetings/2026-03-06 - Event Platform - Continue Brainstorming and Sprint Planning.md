---
title: Event Platform - Continue Brainstorming and Sprint Planning
subtitle: meeting notes
date: 03/06/2026 9:00 AM
meeting: 'true'
meeting-location: Microsoft Teams Meeting
meeting-recipients:
  - Suresh Kumar
  - Daniel Milburn
  - Karthi Arumugam
  - Arivazhagan Jeganathan
  - Gregory Bank
  - Christine Zhou
  - Thiyagarajan Murugan
  - Michael Knarr
  - Michael Mitchell
  - Venmathi Vijayakumar
  - Senthil Arunachalam
  - Marten Engblom
  - Balaji Venkatesan
  - Ben Ludkiewicz
  - Vignesh Arunachalam
  - Philippe Scoffie
  - Nicole Healy
meeting-invite: |
  Continue the discussion we had today regrading optimizations, improvement, decoupling, etc in AuditDB and related areas of the system.
  
  Please add your ideas to this wiki - https://prd.hub.ghx.com/wiki/spaces/EX/pages/997326849/Post+AuditDB+Incident+Brainstorming+Session <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fprd.hub.ghx.com%2Fwiki%2Fspaces%2FEX%2Fpages%2F997326849%2FPost%2BAuditDB%2BIncident%2BBrainstorming%2BSession&data=05%7C02%7Cmengblom%40ghx.com%7Cfd93504bc7cb4dcc4e6708de7affe855%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639083436721403858%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=zwzuR1e6uUVukV3VaNz70NcutENTTEHiUsGMxdSaN3E%3D&reserved=0> 
  
  ________________________________________________________________________________
  
  Microsoft Teams Need help? <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2FJoinTeamsMeeting%3Fomkt%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7Cfd93504bc7cb4dcc4e6708de7affe855%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639083436721429341%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=lxVv%2BKfvCW3kmC2ao0lyw7HBrBcKhrnJWqPk%2BevAIRk%3D&reserved=0>  
  
  Join the meeting now <https://nam02.safelinks.protection.outlook.com/ap/t-59584e83/?url=https%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%253ameeting_YWNmNjQ0ZDEtOWExNS00NjM0LTk3YWYtZjhjN2YxYmNkNDVm%2540thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%25223c2088fe-3969-4873-ac0d-dc9f122866b9%2522%252c%2522Oid%2522%253a%25226fc9f2aa-7ee5-4d19-a6c3-d89fee2c09a5%2522%257d&data=05%7C02%7Cmengblom%40ghx.com%7Cfd93504bc7cb4dcc4e6708de7affe855%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639083436721449965%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=HGWkNLWQwbYJAKkhVyJ%2BTdOk1mYiTvEqqoohrJpp07M%3D&reserved=0> 
  
  Meeting ID: 222 337 327 062 
  
  Passcode: 2iN7wV9F 
  
  ________________________________
  
  Dial in by phone 
  
  +1 719-569-4684,,407166227# <tel:+17195694684,,407166227>  United States, Pueblo 
  
  Find a local number <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2F70057310-1f9b-4a61-8051-5cb24d3bb801%3Fid%3D407166227&data=05%7C02%7Cmengblom%40ghx.com%7Cfd93504bc7cb4dcc4e6708de7affe855%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639083436721473099%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=cG1rivthObx7adv0FGtLCpR1o0kC9G1dSE2r4VlS00w%3D&reserved=0> 
  
  Phone conference ID: 407 166 227# 
  
  For organizers: Meeting options <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2FmeetingOptions%2F%3ForganizerId%3D6fc9f2aa-7ee5-4d19-a6c3-d89fee2c09a5%26tenantId%3D3c2088fe-3969-4873-ac0d-dc9f122866b9%26threadId%3D19_meeting_YWNmNjQ0ZDEtOWExNS00NjM0LTk3YWYtZjhjN2YxYmNkNDVm%40thread.v2%26messageId%3D0%26language%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7Cfd93504bc7cb4dcc4e6708de7affe855%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639083436721493560%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=pRaw9kktcroy0HiiBTDJgow8eisJu%2B8dG%2BLRp5TQZR4%3D&reserved=0>  | <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2Fusp%2Fpstnconferencing&data=05%7C02%7Cmengblom%40ghx.com%7Cfd93504bc7cb4dcc4e6708de7affe855%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639083436721513988%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=CEH5IXxaEaSVCTGJLJzxaDIyEblfZBXzLCsjkv0pokM%3D&reserved=0> Reset dial-in PIN <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2Fusp%2Fpstnconferencing&data=05%7C02%7Cmengblom%40ghx.com%7Cfd93504bc7cb4dcc4e6708de7affe855%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639083436721535940%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=GI72QiHRgl1zDLvAp4jpI0icPf%2F5jKmVZFLa8EpS1dE%3D&reserved=0>  
  
  ________________________________________________________________________________
  
  
---
Discussing 