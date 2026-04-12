![Exported image](Exported%20image%2020260225175945-0.png)

[Mårten Daniel Various Topics | Microsoft Whiteboard](https://whiteboard.cloud.microsoft/me/whiteboards/p/c3BvOmh0dHBzOi8vZ2h4MzY1LW15LnNoYXJlcG9pbnQuY29tL3BlcnNvbmFsL2RtaWxidXJuX2doeF9jb20%3d/b!389IV-03O0qFapiQxNdJzZQzmejkq6tKlJ_pVZs6Z0p7O7xyq1zPSZ51-4_Dfo1j/01AVJT62QQPPKRYJS5URFLRMD55REFKMYI?sharingv2=true&fromShare=true&fromShare=true&at=9&clickparams=eyAiWC1BcHBOYW1lIiA6ICJNaWNyb3NvZnQgT3V0bG9vayIsICJYLUFwcFZlcnNpb24iIDogIjE2LjAuMTkzMjguMjAyNjYiLCAiT1MiIDogIldpbmRvd3MiIH0%3D&LOF=1&CID=756de2a1-60fe-b000-0093-480f7517f14f&cidOR=SPO)
   

- Mapping Team
    - Actions execute as part of Processing Engine
        - 5 actions have been converted to Lambdas
        - 1 special action wraps the mapps
    - Maps are either Contivo or [Smooks](https://www.smooks.org/)
        - Contivo maps compile into libraries that execute in lambdas
 
- IPA
    - Used to spend $5M with First Source on manually digitizing documents from "non integrated customers"
    - Created automated solution
    - Digitize Pos and Invoices
    - ~300 customers
    - Started off as cost savings - has become part of value proposition
    - Gfax - 45-50% automated
    - Invoicing - 15%
    - ![Exported image](Exported%20image%2020260225175945-1.png)
 
- Visibility Team
    - AOR: Self service portal for Exchange
        - Angular / Tomcat
        - Springboot
    - Environment
        - Local application
        - Shared Dev DBs
- Doc Enrichment Team
    - Doc enrichment
        - File identification
    - Rules engine
    - Actions framework
    - IBR
    - Tooling (Smooks, Contivo)
    - Odin
    - Pulling dref out of the Monlith
    - User Data out of TPM
    - Heavilyt involved in Complex Ordering (Comercial roadmap item)