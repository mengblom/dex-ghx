#!/usr/bin/env python3
"""
Clean up person pages - keep only people with 3+ meetings
"""
from pathlib import Path
from collections import Counter
import yaml
import shutil

VAULT = Path.home() / "Documents" / "dex"
MEETINGS_DIR = VAULT / "00-Inbox" / "Meetings"
PEOPLE_DIR = VAULT / "05-Areas" / "People" / "Internal"
BACKUP_FILE = VAULT / "System" / "deleted-people-backup.txt"

def count_meeting_appearances():
    """Count how many meetings each person appears in"""
    people_count = Counter()

    for meeting in MEETINGS_DIR.glob("*.md"):
        content = meeting.read_text(encoding="utf-8", errors="ignore")
        if not content.startswith("---"):
            continue

        try:
            parts = content.split("---", 2)
            if len(parts) < 3:
                continue
            frontmatter = yaml.safe_load(parts[1])
            if frontmatter and "meeting-recipients" in frontmatter:
                recipients = frontmatter["meeting-recipients"]
                if isinstance(recipients, list):
                    for person in recipients:
                        if person and person != "Marten Engblom":
                            people_count[person] += 1
        except:
            pass

    return people_count

def name_to_filename(name):
    """Convert 'First Last' to 'First_Last.md'"""
    return name.replace(" ", "_") + ".md"

def main():
    print("Person Page Cleanup")
    print("=" * 60)
    print()

    # Count meetings
    print("Analyzing meetings...")
    people_count = count_meeting_appearances()

    # Categorize
    keep_threshold = 3
    to_keep = {name: count for name, count in people_count.items() if count >= keep_threshold}
    to_delete = {name: count for name, count in people_count.items() if count < keep_threshold}

    print(f"Found {len(people_count)} people total")
    print(f"  Keep (3+ meetings): {len(to_keep)}")
    print(f"  Delete (<3 meetings): {len(to_delete)}")
    print()

    # Find person pages to delete
    pages_to_delete = []
    for person_file in PEOPLE_DIR.glob("*.md"):
        if person_file.name == "README.md":
            continue

        person_name = person_file.stem.replace("_", " ")

        # Check if this person should be deleted
        if person_name in to_delete or person_name not in people_count:
            pages_to_delete.append((person_file, person_name, to_delete.get(person_name, 0)))

    print(f"Will delete {len(pages_to_delete)} person pages")
    print()

    # Show what we're keeping
    print("KEEPING (3+ meetings):")
    print("-" * 60)
    for name, count in sorted(to_keep.items(), key=lambda x: x[1], reverse=True):
        print(f"  {count:2d} meetings: {name}")

    print()
    input("Press Enter to delete person pages (Ctrl+C to cancel)...")
    print()

    # Create backup
    with open(BACKUP_FILE, "w") as f:
        f.write("DELETED PERSON PAGES BACKUP\n")
        f.write("=" * 60 + "\n\n")
        f.write("To restore a person page:\n")
        f.write("1. Create 05-Areas/People/Internal/Firstname_Lastname.md\n")
        f.write("2. Add basic frontmatter and meeting links\n\n")
        f.write("DELETED:\n")
        f.write("-" * 60 + "\n")

        for person_file, person_name, count in sorted(pages_to_delete, key=lambda x: x[1]):
            f.write(f"{person_name} ({count} meetings) - {person_file.name}\n")

    # Delete person pages
    deleted_count = 0
    for person_file, person_name, count in pages_to_delete:
        try:
            person_file.unlink()
            deleted_count += 1
            print(f"  ✓ Deleted: {person_name} ({count} meetings)")
        except Exception as e:
            print(f"  ✗ Error deleting {person_name}: {e}")

    print()
    print("=" * 60)
    print(f"Cleanup complete!")
    print(f"  Deleted: {deleted_count} person pages")
    print(f"  Kept: {len(to_keep)} person pages")
    print(f"  Backup saved to: {BACKUP_FILE.relative_to(VAULT)}")
    print()
    print("Your person pages now only include people you meet with regularly.")

if __name__ == "__main__":
    main()
