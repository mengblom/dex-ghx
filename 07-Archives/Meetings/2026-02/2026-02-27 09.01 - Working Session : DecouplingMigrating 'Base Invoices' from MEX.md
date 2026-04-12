---
title: "Working Session : Decoupling/Migrating 'Base Invoices' from MEX"
subtitle: meeting notes
date: 02/27/2026 9:00 AM
meeting: "true"
meeting-location: Microsoft Teams Meeting
meeting-recipients:
  - Annie Leong
  - Prashanth Garlapati
  - Brian Moran
  - Marten Engblom
  - Laura Taylor
  - Ramesh Donnipadu
  - Matthew D. Gibson
  - Jaimin Shah
  - Alexis Hull-Stone
  - Radha Krishna Mannemala
  - Glenn Sorensen
  - Leela Mohan Macharla
  - Hari Prasad Narasapu
meeting-invite: |-
  Hello Team,

   

  It is challenging to find a common time that works across teams and regions; based on availability, I’ve identified this as the best possible slot and would appreciate your participation.

   

  Following up on the earlier eMail communication around UI decoupling for Invoices and eInvoicing, I’d like to schedule a working session to align on scope and ownership so we can move forward without ambiguity.

  As part of the broader MEX UI decoupling strategy, we are separating the UI layer from the monolithic repository while keeping backend services unchanged. This approach has worked well for other apps, but for Invoices and eInvoicing we need clear functional and UI boundaries to proceed confidently.

   

  Proposed Discussion Highlights

  *	UI Ownership & Boundaries

  	*	Which screens and flows belong to Invoices UI vs eInvoicing UI
  	*	Whether UIs should live in separate repositories or a shared one
  	*	Expected ownership model from a product and UI perspective

  *	Decoupling Expectations

  	*	Avoiding UI-level dependencies between Invoices and eInvoicing
  	*	Supporting independent UI-only deployments
  	*	Aligning with long-term maintainability and product ownership

  *	Domain & Deployment Alignment

  	*	UI deployment strategy, routing, and URL structure
  	*	Navigation or cross-app linking considerations

  *	Domain Walkthrough

  	*	Screen-level walkthrough from a product/domain expert
  	*	Identification of shared or overlapping flows that need special handling

   

  Please let us know your availability or suggest an alternate time if needed. Having the right product and engineering context in this discussion will help us converge quickly.

   

  Please feel free to add your team members if any.

   

   

   

  Thanks,

  Prashanth Garlapati

   

  ________________________________________________________________________________

  Microsoft Teams meeting 

  Join: https://teams.microsoft.com/meet/28047864038715?p=h7LYhg0BbjHJXUxhZH <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2Fmeet%2F28047864038715%3Fp%3Dh7LYhg0BbjHJXUxhZH&data=05%7C02%7Cmengblom%40ghx.com%7Cc3cfb3d331cc46dafb3908de73ad3b4c%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639075385019736691%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=p19Us5xxKJPQA1GHAQo%2BffM5lLM7KI1Sq5QG0YMRZ%2BQ%3D&reserved=0>  

  Meeting ID: 280 478 640 387 15 

  Passcode: ZQ3w6tY3 

  ________________________________

  Need help? <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Faka.ms%2FJoinTeamsMeeting%3Fomkt%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7Cc3cfb3d331cc46dafb3908de73ad3b4c%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639075385019785847%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=z33EUQ5sxkDmwZPrku5bS1Foigh9Wbezt%2F1XO3qvPDQ%3D&reserved=0>  | System reference <https://nam02.safelinks.protection.outlook.com/ap/t-59584e83/?url=https%3A%2F%2Fteams.microsoft.com%2Fl%2Fmeetup-join%2F19%253ameeting_MmQwODM3Y2UtNjQ0ZS00OWVjLWE3YzItOTI2ZjhjZWMwZGFj%2540thread.v2%2F0%3Fcontext%3D%257b%2522Tid%2522%253a%25223c2088fe-3969-4873-ac0d-dc9f122866b9%2522%252c%2522Oid%2522%253a%25226dd314ee-4b56-48b4-8363-ec84964524a2%2522%257d&data=05%7C02%7Cmengblom%40ghx.com%7Cc3cfb3d331cc46dafb3908de73ad3b4c%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639075385019818426%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=1Nzbxbe9IRhNl1P5PyQtAf5LFVYVrgBoszJVz6QNKw4%3D&reserved=0>  

  Dial in by phone 

  +1 719-569-4684,,487038312# <tel:+17195694684,,487038312>  United States, Pueblo 

  Find a local number <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2F70057310-1f9b-4a61-8051-5cb24d3bb801%3Fid%3D487038312&data=05%7C02%7Cmengblom%40ghx.com%7Cc3cfb3d331cc46dafb3908de73ad3b4c%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639075385019849692%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=uFfb%2FGom3WY0ctIysz9ve3QHj2K7G1LqKLsdct9yzS4%3D&reserved=0>  

  Phone conference ID: 487 038 312# 

  For organizers: Meeting options <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fteams.microsoft.com%2FmeetingOptions%2F%3ForganizerId%3D6dd314ee-4b56-48b4-8363-ec84964524a2%26tenantId%3D3c2088fe-3969-4873-ac0d-dc9f122866b9%26threadId%3D19_meeting_MmQwODM3Y2UtNjQ0ZS00OWVjLWE3YzItOTI2ZjhjZWMwZGFj%40thread.v2%26messageId%3D0%26language%3Den-US&data=05%7C02%7Cmengblom%40ghx.com%7Cc3cfb3d331cc46dafb3908de73ad3b4c%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639075385019880688%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=mn%2FPIyL%2FcOPwgAVEMuRUxWYfL8QduXwQsd4M6SKdkrU%3D&reserved=0>  | Reset dial-in PIN <https://nam02.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdialin.teams.microsoft.com%2Fusp%2Fpstnconferencing&data=05%7C02%7Cmengblom%40ghx.com%7Cc3cfb3d331cc46dafb3908de73ad3b4c%7C3c2088fe39694873ac0ddc9f122866b9%7C0%7C0%7C639075385020717683%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=bXaU%2FKr%2FfR99Ao%2FDtOGkqa%2BPx72sgrNUun7opIpW1qw%3D&reserved=0>  

  ________________________________________________________________________________
---
## Notes
Invoicing = "old school" EDI document based invocing
eInvoicing = electronic invoicing

Questions:
1. Can customers (suppliers & providers) use both Invoicing (EDI) and eInvoicing?
	1. Yes, this is very common
	2. GHX can bridge the gap between EDI invoicing and eInvoicing (i.e. a provider is using eInvoicing and the supplier does not)

Key Question: Should Invoicing and eInvoicing really be 2 separate products / end user experiences?
- I don't hear anyone saying "no"

---

## Meeting Summary

**Key Discussion Points**

**1. Current State of Invoicing Architecture**
- Invoicing and E-Invoicing share a heavily integrated codebase within Exchange
- Single application (einvoicing.ghx.com) with conditional logic to display features based on product subscriptions
- Originally designed with domain-driven design principles - one platform serving multiple products
- Very fine-grained overlap between base invoicing and E-Invoicing functionality

**2. Product Differences Explained**
- Base Invoicing: Traditional EDI-based document trading (810 documents), core Exchange functionality
- E-Invoicing: Value-add features including proof of delivery, alternate delivery paths (email, portal), workflow, GL coding, data capture, and smoothing
- Key Insight: Customers can use both simultaneously - E-Invoicing is an upgrade/enhancement, not a replacement

**3. Organizational Challenges**
- Invoicing responsibility was separated from Exchange team ~1.5-2 years ago during pod reorganization
- E-Invoicing team cannot independently update shared libraries - depends on Exchange team approval
- No separate repo or environment for E-Invoicing team testing
- PR approval bottlenecks and deployment dependencies create friction
- Small E-Invoicing team (5-7 members) with limited capacity

**4. Critical Realization**
- Marten's key observation: Rather than decoupling Invoicing vs E-Invoicing, the teams should consider **unifying** them as a single product
- Both Brian and Alexis agreed with this direction
- Proposal: Entire invoicing domain (base + E-Invoicing) should be owned by one team as a unified product
- In EU, there's no distinction - it's all E-Invoicing, suggesting natural unification

**5. Angular Upgrade Discussion**
- Current Angular version is extremely outdated (Angular JS 1.x vs market standard v20)
- Security vulnerabilities and tech debt driving urgent need for upgrade
- Originally planned as Exchange roadmap item with joint effort

**Three Possible Paths Forward**
1. Deprioritize E-Invoicing commercial work to enable true joint effort on Angular upgrade
2. Exchange team takes full ownership of Angular upgrade
3. Pause upgrade until product unification strategy is resolved

**Action Items**
- Regroup next week -  (Thursday/Friday) to continue discussion
- Laura to provide guidance on prioritization between commercial work and technical upgrade
- Product leadership to evaluate whether Invoicing and E-Invoicing should be unified as single product
- Consider escalation to senior leadership (Curtis, Bharat) if prioritization conflicts can't be resolved at current level

**Strategic Recommendations**
- Short-term: Decide on Angular upgrade approach (joint effort, ownership, or pause)
- Medium-term: Evaluate product unification strategy from end-user perspective
- Long-term: Address broader decoupling goals while maintaining team autonomy and reducing deployment risk
 