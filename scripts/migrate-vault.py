#!/usr/bin/env python3
"""
GHX Vault Migration Script
Migrates content from ~/Documents/GHX/ to Dex PARA structure
"""
import os
import re
import shutil
import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import json

# Paths
SOURCE_VAULT = Path.home() / "Documents" / "GHX"
TARGET_VAULT = Path.home() / "Documents" / "dex"
MIGRATION_LOG = TARGET_VAULT / "System" / "migration-log.json"

# State tracking
migration_state = {
    "files_moved": [],
    "people_created": [],
    "links_updated": [],
    "errors": [],
    "decisions_needed": [],
    "statistics": {}
}

def parse_frontmatter(content):
    """Extract YAML frontmatter from markdown content"""
    if not content.startswith("---"):
        return {}, content

    try:
        parts = content.split("---", 2)
        if len(parts) < 3:
            return {}, content

        frontmatter = yaml.safe_load(parts[1])
        body = parts[2].strip()
        return frontmatter or {}, body
    except:
        return {}, content

def extract_people_from_meeting(frontmatter):
    """Extract people names from meeting frontmatter"""
    people = []
    recipients = frontmatter.get("meeting-recipients", [])
    if isinstance(recipients, list):
        for person in recipients:
            if person and person != "Marten Engblom":  # Skip self
                people.append(person)
    return people

def name_to_filename(name):
    """Convert 'First Last' to 'First_Last'"""
    return name.replace(" ", "_")

def is_meeting_note(filepath, frontmatter, content):
    """Determine if file is a meeting note"""
    # Check frontmatter
    if frontmatter.get("meeting") == "true" or frontmatter.get("meeting") == True:
        return True

    # Check filename patterns
    filename = filepath.stem
    # Pattern: YYYY-MM-DD or date-like patterns
    if re.match(r"^\d{4}-\d{2}-\d{2}", filename):
        return True

    # Check for meeting-related keywords in title
    keywords = ["meeting", "call with", "sync", "standup", "1:1", "1-1"]
    filename_lower = filename.lower()
    for keyword in keywords:
        if keyword in filename_lower:
            return True

    return False

def is_daily_note(filepath):
    """Determine if file is a daily note"""
    # From Daily Notes folder
    if "Daily Notes" in str(filepath):
        return True

    # Filename is just a date
    filename = filepath.stem
    if re.match(r"^\d{4}-\d{2}-\d{2}$", filename):
        return True

    return False

def determine_target_path(source_file, frontmatter, content):
    """Determine where a file should go in PARA structure"""
    rel_path = source_file.relative_to(SOURCE_VAULT)
    parts = rel_path.parts

    # Meeting notes
    if is_meeting_note(source_file, frontmatter, content):
        filename = format_meeting_filename(source_file, frontmatter)
        return TARGET_VAULT / "00-Inbox" / "Meetings" / filename

    # Daily notes
    if is_daily_note(source_file):
        # Check if recent (last 90 days)
        try:
            mtime = datetime.fromtimestamp(source_file.stat().st_mtime)
            age_days = (datetime.now() - mtime).days
            if age_days <= 90:
                return TARGET_VAULT / "00-Inbox" / "Daily_Plans" / source_file.name
            else:
                return TARGET_VAULT / "07-Archives" / "Plans" / source_file.name
        except:
            return TARGET_VAULT / "07-Archives" / "Plans" / source_file.name

    # Projects folder
    if len(parts) > 1 and parts[0] == "Projects":
        project_name = parts[1].replace(" ", "_")

        # Archive Laguna Offsite
        if "Laguna" in project_name:
            rest_path = Path(*parts[2:]) if len(parts) > 2 else Path(source_file.name)
            return TARGET_VAULT / "07-Archives" / "Projects" / "Laguna_Offsite_2026" / rest_path

        # Active projects
        rest_path = Path(*parts[2:]) if len(parts) > 2 else Path(source_file.name)
        return TARGET_VAULT / "04-Projects" / project_name / rest_path

    # Recruiting → Project
    if len(parts) > 0 and parts[0] == "Recruiting":
        rest_path = Path(*parts[1:]) if len(parts) > 1 else Path(source_file.name)
        return TARGET_VAULT / "04-Projects" / "Recruiting_2026" / rest_path

    # Planning folder
    if len(parts) > 0 and parts[0] == "Planning":
        # Check file date to determine if current or archive
        try:
            mtime = datetime.fromtimestamp(source_file.stat().st_mtime)
            if mtime.year == 2026 and mtime.month >= 1:
                return TARGET_VAULT / "02-Week_Priorities" / source_file.name
            else:
                return TARGET_VAULT / "07-Archives" / "Plans" / source_file.name
        except:
            return TARGET_VAULT / "07-Archives" / "Plans" / source_file.name

    # Management folder
    if len(parts) > 0 and parts[0] == "Management":
        return TARGET_VAULT / "06-Resources" / "Management" / source_file.name

    # Inbox folder
    if len(parts) > 0 and "Inbox" in parts[0]:
        rest_path = Path(*parts[1:]) if len(parts) > 1 else Path(source_file.name)
        return TARGET_VAULT / "00-Inbox" / rest_path

    # Templates
    if len(parts) > 0 and parts[0] == "Templates":
        return TARGET_VAULT / "System" / "Templates" / source_file.name

    # Root level files - need to categorize
    if len(parts) == 1:
        # Check if meeting note
        if is_meeting_note(source_file, frontmatter, content):
            filename = format_meeting_filename(source_file, frontmatter)
            return TARGET_VAULT / "00-Inbox" / "Meetings" / filename

        # Default to Inbox/Ideas for misc notes
        return TARGET_VAULT / "00-Inbox" / "Ideas" / source_file.name

    # Default: preserve structure in Resources
    return TARGET_VAULT / "06-Resources" / "Legacy" / rel_path

def format_meeting_filename(source_file, frontmatter):
    """Format meeting note filename to Dex convention"""
    # Try to get date from frontmatter
    date_str = frontmatter.get("date")
    title = frontmatter.get("title", "")

    if date_str:
        # Parse date (format: 03/03/2026 2:30 PM)
        try:
            if "/" in str(date_str):
                parts = str(date_str).split()[0]  # Get date part
                month, day, year = parts.split("/")
                formatted_date = f"{year}-{month.zfill(2)}-{day.zfill(2)}"
            else:
                formatted_date = str(date_str)[:10]  # Assume YYYY-MM-DD

            if title:
                return f"{formatted_date} - {title}.md"
            else:
                return f"{formatted_date} - {source_file.stem}.md"
        except:
            pass

    # Fallback: try to extract date from filename
    filename = source_file.stem
    date_match = re.search(r"(\d{4}-\d{2}-\d{2})", filename)
    if date_match:
        date = date_match.group(1)
        # Remove date from title
        title_part = re.sub(r"\d{4}-\d{2}-\d{2}\s*\d{2}\.\d{2}\s*", "", filename).strip()
        if title_part:
            return f"{date} - {title_part}.md"
        return f"{date} - Meeting.md"

    # Last resort: use original filename
    return source_file.name

def migrate_file(source_file):
    """Migrate a single markdown file"""
    try:
        # Read file
        content = source_file.read_text(encoding="utf-8")
        frontmatter, body = parse_frontmatter(content)

        # Determine target location
        target_path = determine_target_path(source_file, frontmatter, body)

        # Create parent directory
        target_path.parent.mkdir(parents=True, exist_ok=True)

        # Handle duplicates
        if target_path.exists():
            base = target_path.stem
            ext = target_path.suffix
            counter = 1
            while target_path.exists():
                target_path = target_path.parent / f"{base}-{counter}{ext}"
                counter += 1

        # Copy file
        shutil.copy2(source_file, target_path)

        # Track migration
        migration_state["files_moved"].append({
            "source": str(source_file.relative_to(SOURCE_VAULT)),
            "target": str(target_path.relative_to(TARGET_VAULT)),
            "type": categorize_file(source_file, frontmatter, body)
        })

        # Extract people from meeting notes
        if is_meeting_note(source_file, frontmatter, body):
            people = extract_people_from_meeting(frontmatter)
            for person_name in people:
                create_person_page(person_name, target_path)

        return True

    except Exception as e:
        migration_state["errors"].append({
            "file": str(source_file),
            "error": str(e)
        })
        return False

def categorize_file(filepath, frontmatter, content):
    """Categorize file type for reporting"""
    if is_meeting_note(filepath, frontmatter, content):
        return "meeting"
    if is_daily_note(filepath):
        return "daily_note"

    rel_path = filepath.relative_to(SOURCE_VAULT)
    if "Projects" in str(rel_path):
        return "project"
    if "Recruiting" in str(rel_path):
        return "recruiting"
    if "Planning" in str(rel_path):
        return "planning"
    if "Management" in str(rel_path):
        return "management"
    if "Inbox" in str(rel_path):
        return "inbox"

    return "other"

def create_person_page(person_name, meeting_file):
    """Create or update person page"""
    if person_name in [p["name"] for p in migration_state["people_created"]]:
        return  # Already created

    filename = name_to_filename(person_name)
    person_page = TARGET_VAULT / "05-Areas" / "People" / "Internal" / f"{filename}.md"

    # Create if doesn't exist
    if not person_page.exists():
        person_page.parent.mkdir(parents=True, exist_ok=True)

        content = f"""---
name: {person_name}
company: GHX
internal: true
---

## Context
[Add context about {person_name}]

## Meetings
- [[{meeting_file.stem}]]

## Related Projects

## Action Items
"""
        person_page.write_text(content)

        migration_state["people_created"].append({
            "name": person_name,
            "file": str(person_page.relative_to(TARGET_VAULT))
        })

def migrate_attachments():
    """Consolidate attachment folders"""
    attachment_sources = [
        SOURCE_VAULT / "_attachments",
        SOURCE_VAULT / "attachments",
        SOURCE_VAULT / "Attachments 1"
    ]

    target_attachments = TARGET_VAULT / "_attachments"
    target_attachments.mkdir(exist_ok=True)

    for source_dir in attachment_sources:
        if not source_dir.exists():
            continue

        for item in source_dir.rglob("*"):
            if item.is_file():
                relative_path = item.relative_to(source_dir)
                target_path = target_attachments / relative_path
                target_path.parent.mkdir(parents=True, exist_ok=True)

                # Handle duplicates
                if target_path.exists():
                    base = target_path.stem
                    ext = target_path.suffix
                    counter = 1
                    while target_path.exists():
                        target_path = target_path.parent / f"{base}-{counter}{ext}"
                        counter += 1

                shutil.copy2(item, target_path)

def generate_report():
    """Generate migration report"""
    stats = defaultdict(int)
    for item in migration_state["files_moved"]:
        stats[item["type"]] += 1

    migration_state["statistics"] = dict(stats)

    report = f"""
# Migration Report
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary
- Total files migrated: {len(migration_state['files_moved'])}
- People pages created: {len(migration_state['people_created'])}
- Errors encountered: {len(migration_state['errors'])}

## File Type Breakdown
"""
    for file_type, count in sorted(stats.items()):
        report += f"- {file_type}: {count} files\n"

    report += f"""

## People Created
"""
    for person in migration_state["people_created"]:
        report += f"- {person['name']} → {person['file']}\n"

    if migration_state["errors"]:
        report += f"""

## Errors
"""
        for error in migration_state["errors"]:
            report += f"- {error['file']}: {error['error']}\n"

    report += f"""

## Next Steps
1. Review migrated files in Obsidian
2. Check person pages in 05-Areas/People/Internal/
3. Run wiki link conversion: `node .scripts/auto-link-people.cjs --today`
4. Verify project structure in 04-Projects/
5. Run git commit to save migration

## Full Migration Log
See: System/migration-log.json
"""

    return report

def main():
    """Main migration process"""
    print("GHX Vault Migration")
    print("=" * 50)
    print(f"Source: {SOURCE_VAULT}")
    print(f"Target: {TARGET_VAULT}")
    print()

    # Verify source exists
    if not SOURCE_VAULT.exists():
        print(f"Error: Source vault not found at {SOURCE_VAULT}")
        return

    # Prompt for confirmation
    input("Press Enter to start migration (Ctrl+C to cancel)...")
    print()

    # Find all markdown files
    md_files = list(SOURCE_VAULT.rglob("*.md"))

    # Exclude some folders
    exclude_patterns = [".obsidian", ".claude", ".git"]
    md_files = [f for f in md_files if not any(pattern in str(f) for pattern in exclude_patterns)]

    print(f"Found {len(md_files)} markdown files to migrate")
    print()

    # Migrate files
    print("Migrating files...")
    for i, md_file in enumerate(md_files, 1):
        print(f"  [{i}/{len(md_files)}] {md_file.name}")
        migrate_file(md_file)

    print()
    print("Migrating attachments...")
    migrate_attachments()

    print()
    print("Generating report...")

    # Save migration log
    MIGRATION_LOG.parent.mkdir(parents=True, exist_ok=True)
    with open(MIGRATION_LOG, "w") as f:
        json.dump(migration_state, f, indent=2)

    # Generate and save report
    report = generate_report()
    report_file = TARGET_VAULT / "System" / "migration-report.md"
    report_file.write_text(report)

    print()
    print("=" * 50)
    print("Migration Complete!")
    print()
    print(f"Report saved to: {report_file.relative_to(TARGET_VAULT)}")
    print(f"Log saved to: {MIGRATION_LOG.relative_to(TARGET_VAULT)}")
    print()
    print("Next steps:")
    print("1. Review the migration report")
    print("2. Check migrated files in Obsidian")
    print("3. Run: node .scripts/auto-link-people.cjs --today")
    print("4. Commit changes: git add . && git commit -m 'Migrate GHX vault content'")

if __name__ == "__main__":
    main()
