"""Read the same contribution calendar that visitors see on GitHub."""

import argparse
import json
import os
import re
from pathlib import Path
from urllib.request import Request, urlopen


USERNAME = os.getenv("GITHUB_REPOSITORY_OWNER", "signaloninternet")
README = Path(__file__).resolve().parents[2] / "README.md"
GRAPH_HEADING = "js-contribution-activity-description"


def fetch_calendar():
    request = Request(
        f"https://github.com/users/{USERNAME}/contributions",
        headers={"Accept-Language": "en-US", "User-Agent": "profile-readme-refresh"},
    )
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8")


def contribution_count(calendar):
    heading = re.search(
        rf'<h2\b[^>]*\bid="{GRAPH_HEADING}"[^>]*>\s*([0-9][0-9,]*)\s+'
        r'contributions?\s+in the last year\s*</h2>',
        calendar,
    )
    if heading is None:
        raise ValueError("GitHub's annual contribution total was missing from the calendar")
    return int(heading[1].replace(",", ""))


def contribution_days(calendar, total):
    cells = re.findall(
        r'<td\b(?=[^>]*\bdata-date="(\d{4}-\d{2}-\d{2})")[^>]*\bid="(contribution-day-component-[^"]+)"[^>]*>',
        calendar,
    )
    tooltips = dict(re.findall(
        r'<tool-tip\b[^>]*\bfor="(contribution-day-component-[^"]+)"[^>]*>\s*'
        r'(No|[0-9][0-9,]*)\s+contributions?\s+on\b',
        calendar,
    ))
    if not cells or len({date for date, _ in cells}) != len(cells):
        raise ValueError("GitHub's contribution calendar is missing days or contains duplicates")
    if any(cell not in tooltips for _, cell in cells):
        raise ValueError("GitHub's contribution calendar is missing daily counts")

    days = [
        {"date": date, "count": 0 if tooltips[cell] == "No" else int(tooltips[cell].replace(",", ""))}
        for date, cell in sorted(cells)
    ]
    if sum(day["count"] for day in days) != total:
        raise ValueError("Daily contribution counts do not match GitHub's annual total")
    return days


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--calendar", type=Path, help="write public daily counts to a JSON file")
    args = parser.parse_args()

    calendar = fetch_calendar()
    count = contribution_count(calendar)
    label = "contribution" if count == 1 else "contributions"
    line = (
        f"[{count:,} GitHub {label} in the last year]"
        f"(https://github.com/{USERNAME}#{GRAPH_HEADING})"
    )

    readme = README.read_text(encoding="utf-8")
    updated, matches = re.subn(r"(?m)^.*(?= <!-- github-contributions -->$)", line, readme)
    if matches != 1:
        raise ValueError("Expected exactly one GitHub contribution line in the README")
    if args.calendar:
        days = contribution_days(calendar, count)
        args.calendar.write_text(json.dumps(days), encoding="utf-8")
    if updated != readme:
        README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
