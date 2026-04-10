# Objective 1: Level up to a World Class Engineering Organization

- # Objective 1: Level up to a World Class Engineering Organization
    
    - Intent
        - Build a high-performing, product-centric engineering org with clear ownership, strong leadership, and disciplined execution.
        - Autonomous teams
        - Cloud first
    - KRs
        - Team topology
        - Team composition
        - High hiring bar
        - India strategy
      
    - Build the right team structure
        - Reverse Conway Maneuver
        - Finalize a target team topology
        - Establish a **“crystal clear” ownership model**.
    -   
        
    
- Hiring & Team Building
    - Clear Goal Team structure & Areas of Responsibility
        - Have a crystal clear picture of the team structure we are going for, and each team's area of responsibility, systems they own etc. We are doing a Reverse Conway Maneuver
    - Hold the bar high for hiring
        - Review the requirements and job descriptions
        - Review the hiring / interview process
    - Hiring challenges in India
        - Compensation - are we in the right place
        - We need a Product Engineering mindset, not a Service Engineering Mindset
        - Is there a different strategy - e.g. double down in strong managers/leaders + lower the requirements on less senior ICs (less experience, less of a perfect skill match, but hire eager learners for the long run etc.)
        - Is hiring/converting the consultants from Happiest Minds an option?
- Autonomy, Mastery, Purpose
    - In the new org, we need 1 player-coach manager for each team
        - People manager of ~6-8 engineers
        - Strong architect
    - Need clear areas of ownership per team
- Assess and hone the SDLC Process
    - Agile Maturity Model?
        - Create one (a radar) based on Henrik Kniberg's checklist?￼[Scrum checklist.pptx](https://scruminc.wpenginepowered.com/wp-content/uploads/2019/05/scrum-checklist.pdf)
- Squad health checks?
    - [Squad Health Check model – visualizing what to improve | Spotify Engineering](https://engineering.atspotify.com/2014/09/squad-health-check-model)

## Product Delivery / Value Delivery

- ## Product Delivery / Value Delivery
    
    - Elevate Engineering / Product Partnership
        - Monthly(?) Roadmap Meeting
    - Work organization & reporting
        - Need Initiative level in Jira?
        - Need comprehensive roadmap (Product owns this)
        - Need complete and easy overview of **everything** in progress and **everything** on the backlog
        - All work needs to be reflected in Jira
            - Create stories for everything - UNPLANNED?
    - AI Native Development
- World Class Engineering Team

# Delighting customers

- # Delighting customers
    
    - ## Stability & Reliability
        
        - **Healthscore**
        - Sev 1-3 Incidents goes down
        - Incident tickets are resolved (don’t have true count)
        - Customer support bugs / tickets are resolved quickly
        - % of documents delivered within 5 minute SLO.
    - ## Databases
        
        - Need a complete inventory and usage etc.
        - Stabilizing
        - Optimizing
        - No ORMs for bulk operations / set queries / analytics queries etc.
    - ## Vulnerabilities
        
- # Longer term technology initiatives
    
    - ## Break apart the Monolith
        
        - Carve out 1 piece and rebuild according to "what good looks like"
    - ## A few areas of concern for replacing / getting rid of
        
        - Homegrown IdP (aka SSO)
        - Homegrown service bus
    - ## Cost of running GHX Exchange
        

## Stability & Reliability

## Databases

## Vulnerabilities

# Longer term technology initiatives

## Break apart the Monolith

## A few areas of concern for replacing / getting rid of

## Cost of running GHX Exchange

- Pivot to a World Class Product-Centric Engineering Organization
    - _Intent:_
        - _A modern software development organization is typically flat, agile, and product-centric, using cross-functional, autonomous teams (like Squads, Tribes, Chapters) focused on end-to-end product ownership, driven by DevOps principles, automation, and continuous delivery (CI/CD) for rapid, high-quality software releases, prioritizing customer value and iterative improvement over rigid hierarchies._
    - Team Topology
        - _Establish a team topology with a crystal clear ownership model, aligned to our future target architecture_
        - _Align on a team topology with a crystal clear ownership model (each team has a clear scope of ownership and mission statement)_
    - Team structure
        - _Ensure each team has all roles needed to build, maintain and evolve the components they own_
        - _Build the right team structure (1 EM per team, dedicated PO per team,…)_
    - Fill X% of open roles
    - Ensure each team operates according to proven agile best practices
        - Agile Maturity Model?
            - Create one (a radar) based on Henrik Kniberg's checklist?￼[Scrum checklist.pptx](https://scruminc.wpenginepowered.com/wp-content/uploads/2019/05/scrum-checklist.pdf)
    - AI Native Development
        - _Establish way of measuring_
- Delight Stakeholders with Better Product/Value Delivery
    - Elevate Engineering / Product Partnership
    - Provide complete insight and transparency (roadmaps, backlogs, bugs, mapping etc.)
        - _All teams have a published board/backlog etc._
    - Carve out 1 component from the monolith into a cloud native, stand alone service
- Delight Customers with better Exchange stability & reliability
    - _Intent_
        - _This objective is a combination of more effectively measure and communicate on the stability and reliability of the platform, and making meaningful progress on current known problems/impediments/detractors._
    - Establish and socialize a health score for the GHX Exchange
        - _Establish a health score for GHX Exchange that encompasses "all" aspects that makes up the "health" of the GHX Exchange system._
        - _This should include things like DORA metrics, incidents, root cause resolution, root cause backlog depth, OSS Scan vulnerabilities, VM vulnerabilities_
    - 100% MongoDB instances migrated to Atlas
    - Database fleet assessment to inform performance and scalability improvements
        - Data analysis (volume, structure)
        - Workload
        - Access patterns
    - 100% SLA for Critical OSS vulnerabilities
    - ??% SLA for High OSS vulnerabilities
    - 100% SLA for Critical VM vulnerabilities
    - ??% SLA for High VM vulnerabilities
- \<orphans\>?
    - A few areas of concern for replacing / getting rid of
        - Homegrown IdP (aka SSO)
            - Workshop on current solution and alternatives
        - Homegrown service bus
            - Workshop on current solution and alternatives
    - Cost of running exchange
        - Measure, calculate, report/publish