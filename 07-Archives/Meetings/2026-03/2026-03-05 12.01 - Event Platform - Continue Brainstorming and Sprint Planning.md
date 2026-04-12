---
title: Event Platform - Continue Brainstorming and Sprint Planning
subtitle: meeting notes
date: 03/05/2026 10:00 AM
meeting: 'true'
meeting-location: Microsoft Teams Meeting
meeting-recipients:
  - Christine Zhou
  - Gregory Bank
  - Thiyagarajan Murugan
  - Suresh Kumar
  - Karthi Arumugam
  - Daniel Milburn
  - Ben Ludkiewicz
  - Michael Mitchell
  - Venmathi Vijayakumar
  - Senthil Arunachalam
  - Marten Engblom
  - Balaji Venkatesan
  - Nicole Healy
  - Vignesh Arunachalam
  - Arivazhagan Jeganathan
  - Philippe Scoffie
  - Michael Knarr
meeting-invite: |
  Continue the discussion we had today regrading optimizations, improvement, decoupling, etc in AuditDB and related areas of the system.
  
  Please add your ideas to this wiki - https://prd.hub.ghx.com/wiki/spaces/EX/pages/997326849/Post+AuditDB+Incident+Brainstorming+Session <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fprd.hub.ghx.com%2Fwiki%2Fspaces%2FEX%2Fpages%2F997326849%2FPost%2BAuditDB%2BIncident%2BBrainstorming%2BSession&data=05%7C02%7Cmengblom%40ghx.com%7C47a47044081342880f4308de7a3ded3b%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639082603558852860%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=FaOcO%2Fah1BHJT13ioTgv3TP%2BWRmP0JQ0OvnWoMoHJCg%3D&reserved=0> 
  
  ________________________________________________________________________________
  
  Microsoft Teams Need help? <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2FJoinTeamsMeeting%3Fomkt%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7C47a47044081342880f4308de7a3ded3b%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639082603558899909%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=T7zPAZklVLOapzIpNqkLwG0Z78l54jLaIWo%2Fc1%2BIxlQ%3D&reserved=0>  
  
  Join the meeting now <https://nam02.safelinks.protection.outlook.com/ap/t-59584e83/?url=https%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%253ameeting_YWNmNjQ0ZDEtOWExNS00NjM0LTk3YWYtZjhjN2YxYmNkNDVm%2540thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%25223c2088fe-3969-4873-ac0d-dc9f122866b9%2522%252c%2522Oid%2522%253a%25226fc9f2aa-7ee5-4d19-a6c3-d89fee2c09a5%2522%257d&data=05%7C02%7Cmengblom%40ghx.com%7C47a47044081342880f4308de7a3ded3b%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639082603558935749%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=SuiQiGpOOEZd4Hev7%2BRfk5aHgsd%2F6QJ%2BEYhljKwxoBU%3D&reserved=0> 
  
  Meeting ID: 222 337 327 062 
  
  Passcode: 2iN7wV9F 
  
  ________________________________
  
  Dial in by phone 
  
  +1 719-569-4684,,407166227# <tel:+17195694684,,407166227>  United States, Pueblo 
  
  Find a local number <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2F70057310-1f9b-4a61-8051-5cb24d3bb801%3Fid%3D407166227&data=05%7C02%7Cmengblom%40ghx.com%7C47a47044081342880f4308de7a3ded3b%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639082603558969619%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=Jp63lhWsxdDHzqUNonLZCe0uplzIQ0O0zlu8H6qN7MA%3D&reserved=0> 
  
  Phone conference ID: 407 166 227# 
  
  For organizers: Meeting options <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2FmeetingOptions%2F%3ForganizerId%3D6fc9f2aa-7ee5-4d19-a6c3-d89fee2c09a5%26tenantId%3D3c2088fe-3969-4873-ac0d-dc9f122866b9%26threadId%3D19_meeting_YWNmNjQ0ZDEtOWExNS00NjM0LTk3YWYtZjhjN2YxYmNkNDVm%40thread.v2%26messageId%3D0%26language%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7C47a47044081342880f4308de7a3ded3b%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639082603559005573%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=MZR0HdcwhGytPHF29%2F2lLOHyufEW6fatF2krrfqlF7Y%3D&reserved=0>  | <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2Fusp%2Fpstnconferencing&data=05%7C02%7Cmengblom%40ghx.com%7C47a47044081342880f4308de7a3ded3b%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639082603559042109%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=9MJFhQDUnFRQsgz7Lwhh5j9rVX7164blZWSiirOVbBU%3D&reserved=0> Reset dial-in PIN <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2Fusp%2Fpstnconferencing&data=05%7C02%7Cmengblom%40ghx.com%7C47a47044081342880f4308de7a3ded3b%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639082603559091138%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=eteYbdoYiRbS4qeN%2FdOKqL1TCH%2F36hYgEJ6gen%2B56d4%3D&reserved=0>  
  
  ________________________________________________________________________________
  
  
---
 