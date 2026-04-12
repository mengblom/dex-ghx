# IPA - Introduction to MSOT and PriceSync workflows

**Date:** 2026-04-10  
**Participants:** [[Aaron_Srivastava|Aaron]], [[Ramesh_Unknown|Ramesh]], Sadhana, Ashoka  
**Company:** GHX - IPA Team  
**Duration:** ~40 minutes

## Summary

Deep dive into IPA team's automation work beyond document understanding. Covered two major workflows: MSOT (Managed Services Order Trust) portal automation and Price Sync value-added services. Discussion revealed significant technical debt and integration challenges with legacy systems (Nuvia) and opportunities for modernization through CDP/EBI consolidation.

## Key Topics

### IPA Team Scope & Responsibilities

- Team handles more than just document understanding/extraction
- Current focus areas:
  - Document understanding (classification/extraction from POs and invoices)
  - Modernizing UI Path ML models to LLMs
  - Regular process automation workflows
  - Managed Services Order Trust (MSOT) portal automation
  - Price Sync workflow automation

### MSOT Workflow Overview

- **Managed services** = value-added service for exchange customers
  - Customers pay for research on PO placement issues, missing acknowledgments, invoice problems
  - Alternative to self-service tools for customers preferring hands-off approach
- Current automation scope:
  - Email correlation to corresponding purchase orders
  - Basic PO validation and automatic acknowledgment generation
  - POA/855 documents provide delivery assurance to customers

### Price Sync Workflow Details

- **Value-added service** alerting providers to overpayments
  - Compares actual payments vs purchase agreements between hospitals/vendors
  - Weekly reports sent to providers
  - Leverages historical PO and agreement data
- Current state (UI-based automation):
  - Downloads reports from Nuvia, Exchange applications, CDP S3 files
  - Bot logs into applications like human (Okta authentication, date range selection)
  - Generates **50 decks weekly for 50 providers** (Fridays 1:30-6:00 IST)
  - Creates 15-16 slide presentations covering:
    1. Spend categories and exception rates
    2. Agreement vs actual comparisons
    3. Item-wise and vendor-wise spend analysis
    4. Historical data from last 7 weeks (stored in RDS)
  - Two deck versions:
    - **Light version** (reduced slides for package customers)
    - **Full version** (complete 15-16 slide analysis)

### Data Sources & Applications

**Nuvia application:**
- Legacy content solution (20-25 years old)
- Item master enrichment with attributes (latex content, sizing, unit counts)
- Helps customers avoid ERP-level maintenance overhead
- Provides HCPCS/spec codes for reimbursements

**Data Connect:**
- Modern replacement for Nuvia (5-6 years development)
- Cloud-focused, similar enrichment functionality
- Some customers still on Nuvia, others migrated to Data Connect

**Exchange application:**
- Source for price exception data
- Three-point validation: PO, POA/invoice, contract price
- Flags mismatches as contract/price exceptions

### Future State & Next Steps

**Eliminating manual configuration processes:**
- Moving from spreadsheet configs to EBI console
- Delivery managers can update configurations directly

**Data source consolidation:**
- CDP/EBI team providing S3 bucket access
- Eliminating UI-based report downloads from Exchange/Nuvia
- IPA will focus on deck generation and email distribution

**Business impact achieved:**
- **40% headcount reduction** in managed services team
- Eliminated data disclosure issues from manual processes

## Action Items

### For Me

- [ ] Continue discussion in-person Wednesday in Hyderabad ^task-20260410-001
- [ ] Explore Nuvia team technical architecture meeting (Scott owns Nuvia and CDP systems) ^task-20260410-002

## Notes

- Scott owns Nuvia and CDP systems
- [[Aaron_Srivastava|Aaron]] joining the team, this was a fire drill meeting to get him up to speed
- Discussion revealed significant opportunities for improvement - current PowerPoint-based workflow is a stopgap until proper dashboarding is built
- Customers receive these decks weekly (not just internal use)

## Links

- [Granola Chat](https://notes.granola.ai/t/e58970ba-b860-4b12-a70e-b154f2245b4a)

---
*Processed from Granola on 2026-04-12*
