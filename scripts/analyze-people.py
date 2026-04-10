#!/usr/bin/env python3
"""
Analyze person pages to identify significant relationships
"""
import re
from pathlib import Path
from collections import defaultdict

VAULT = Path.home() / "Documents" / "dex"
PEOPLE_DIR = VAULT / "05-Areas" / "People" / "Internal"

def analyze_person_page(person_file):
    """Analyze a person page to determine significance"""
    content = person_file.read_text(encoding="utf-8")

    # Count meeting mentions
    meeting_links = re.findall(r'\[\[([^\]]+)\]\]', content)
    num_meetings = len([m for m in meeting_links if any(c.isdigit() for c in m)])

    # Check if it's a 1:1 meeting
    has_one_on_one = any(re.search(r'1[x:-]1|one.on.one', m, re.IGNORECASE) for m in meeting_links)

    # Check if name appears in filename (indicating it's their dedicated meeting)
    person_name = person_file.stem.replace("_", " ")
    has_dedicated_meeting = any(person_name.lower() in m.lower() for m in meeting_links)

    return {
        "name": person_name,
        "file": person_file,
        "num_meetings": num_meetings,
        "has_one_on_one": has_one_on_one,
        "has_dedicated_meeting": has_dedicated_meeting,
        "meetings": meeting_links
    }

def score_significance(analysis):
    """Score how significant this relationship is"""
    score = 0

    # Multiple meetings = more significant
    if analysis["num_meetings"] >= 5:
        score += 3
    elif analysis["num_meetings"] >= 3:
        score += 2
    elif analysis["num_meetings"] >= 2:
        score += 1

    # 1:1 meetings are very significant
    if analysis["has_one_on_one"]:
        score += 3

    # Dedicated meetings (their name in title) = significant
    if analysis["has_dedicated_meeting"]:
        score += 2

    return score

def main():
    """Analyze all person pages"""
    print("Analyzing Person Pages")
    print("=" * 60)
    print()

    all_people = []

    for person_file in sorted(PEOPLE_DIR.glob("*.md")):
        if person_file.name == "README.md":
            continue

        analysis = analyze_person_page(person_file)
        analysis["score"] = score_significance(analysis)
        all_people.append(analysis)

    # Sort by score (descending)
    all_people.sort(key=lambda x: x["score"], reverse=True)

    # Categorize
    significant = [p for p in all_people if p["score"] >= 3]
    moderate = [p for p in all_people if 1 <= p["score"] < 3]
    minimal = [p for p in all_people if p["score"] == 0]

    print(f"Total people: {len(all_people)}")
    print(f"  Significant relationships (score >= 3): {len(significant)}")
    print(f"  Moderate relationships (score 1-2): {len(moderate)}")
    print(f"  Minimal interaction (score 0): {len(minimal)}")
    print()

    print("=" * 60)
    print("SIGNIFICANT RELATIONSHIPS (Keep These)")
    print("=" * 60)
    for p in significant:
        indicator = ""
        if p["has_one_on_one"]:
            indicator = "1:1"
        elif p["has_dedicated_meeting"]:
            indicator = "dedicated"
        print(f"  [{p['score']}] {p['name']:<40} {p['num_meetings']} meetings {indicator}")

    print()
    print("=" * 60)
    print("MODERATE RELATIONSHIPS (Review These)")
    print("=" * 60)
    for p in moderate[:20]:  # Show first 20
        print(f"  [{p['score']}] {p['name']:<40} {p['num_meetings']} meetings")
    if len(moderate) > 20:
        print(f"  ... and {len(moderate) - 20} more")

    print()
    print("=" * 60)
    print("MINIMAL INTERACTION (Consider Removing)")
    print("=" * 60)
    print(f"  {len(minimal)} people appeared in only 1 meeting")
    print()
    print("  Sample (first 20):")
    for p in minimal[:20]:
        print(f"    - {p['name']}")
    if len(minimal) > 20:
        print(f"  ... and {len(minimal) - 20} more")

    print()
    print("=" * 60)
    print("RECOMMENDATIONS")
    print("=" * 60)
    print()
    print(f"1. KEEP: {len(significant)} significant relationships")
    print(f"   → People you meet with regularly or have 1:1s with")
    print()
    print(f"2. REVIEW: {len(moderate)} moderate relationships")
    print(f"   → Check if these are important to you")
    print()
    print(f"3. REMOVE: {len(minimal)} minimal interactions")
    print(f"   → Just meeting attendees, no real relationship")
    print()
    print("Next steps:")
    print("  - Review the lists above")
    print("  - I can create a cleanup script to archive/remove minimal pages")
    print()

    # Save detailed report
    report_file = VAULT / "System" / "people-analysis.txt"
    with open(report_file, "w") as f:
        f.write("PERSON PAGE ANALYSIS\n")
        f.write("=" * 60 + "\n\n")

        f.write(f"SIGNIFICANT ({len(significant)})\n")
        f.write("-" * 60 + "\n")
        for p in significant:
            f.write(f"{p['name']}: {p['num_meetings']} meetings, score={p['score']}\n")

        f.write(f"\n\nMODERATE ({len(moderate)})\n")
        f.write("-" * 60 + "\n")
        for p in moderate:
            f.write(f"{p['name']}: {p['num_meetings']} meetings, score={p['score']}\n")

        f.write(f"\n\nMINIMAL ({len(minimal)})\n")
        f.write("-" * 60 + "\n")
        for p in minimal:
            f.write(f"{p['name']}: {p['num_meetings']} meetings\n")

    print(f"Detailed report saved to: {report_file.relative_to(VAULT)}")

if __name__ == "__main__":
    main()
