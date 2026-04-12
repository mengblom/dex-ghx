# Meeting Archives

**Permanent storage** for processed meeting notes, organized chronologically by year-month.

## Naming Convention

`YYYY-MM-DD HH.mm - Meeting Subject.md`

Examples:
- `2026-04-11 14.30 - Product Roadmap Review.md`
- `2026-04-11 09.00 - Daniel  Marten 1-1.md`

**Why this format:**
- **Date first** - Chronological sorting
- **24-hour time** - Disambiguation for multiple meetings same day
- **Descriptive subject** - Context at a glance

## Directory Structure

```
07-Archives/Meetings/
  2025-11/
  2025-12/
  2026-01/
  2026-02/
  2026-03/
  2026-04/
  ...
```

**One folder per month** - Keeps directories manageable (typically 10-50 meetings per month).

## Integration with Vault

Meeting notes are **cross-linked** throughout the vault:

- **Person pages** (`05-Areas/People/`) link to meetings with that person
- **Projects** (`04-Projects/`) link to relevant meetings
- **Resources** (`06-Resources/`) reference meetings where decisions were made

**Archives preserve chronology, links provide discoverability.**

## What Gets Archived Here

✅ **1:1 meetings** with direct reports, manager, stakeholders
✅ **Team meetings** (staff meetings, all-hands, planning)
✅ **Project meetings** (kickoffs, reviews, technical deep-dives)
✅ **Customer/partner meetings** (if recorded/transcribed)

❌ **NOT emails** - those go in `07-Archives/YYYY/QX/Correspondence/`
❌ **NOT presentations** - those stay with projects in `04-Projects/`

## Processing Workflow

1. Meeting happens → Captured in `00-Inbox/Meetings/`
2. Format the note:
   - Add attendees
   - Extract key decisions
   - Identify action items
   - Add WikiLinks to people/projects
3. Extract knowledge:
   - Update person pages with context
   - Update project pages with decisions
   - Extract strategic insights to Resources
4. Move to `07-Archives/Meetings/YYYY-MM/`

**Result:** Archives are searchable, cross-linked, and integrated into your knowledge base.
