"""Sync the README count with the contribution calendar visitors see on GitHub."""

import os
import re
from pathlib import Path
from urllib.request import Request, urlopen


USERNAME = os.getenv("GITHUB_REPOSITORY_OWNER", "signaloninternet")
README = Path(__file__).resolve().parents[2] / "README.md"
GRAPH_HEADING = "js-contribution-activity-description"


def contribution_count():
    request = Request(
        f"https://github.com/users/{USERNAME}/contributions",
        headers={"Accept-Language": "en-US", "User-Agent": "profile-readme-refresh"},
    )
    with urlopen(request, timeout=30) as response:
        calendar = response.read().decode("utf-8")

    heading = re.search(
        rf'<h2\b[^>]*\bid="{GRAPH_HEADING}"[^>]*>\s*([0-9][0-9,]*)\s+'
        r'contributions?\s+in the last year\s*</h2>',
        calendar,
    )
    if heading is None:
        raise ValueError("GitHub's annual contribution total was missing from the calendar")
    return int(heading[1].replace(",", ""))


def main():
    count = contribution_count()
    label = "contribution" if count == 1 else "contributions"
    line = (
        f"[{count:,} GitHub {label} in the last year]"
        f"(https://github.com/{USERNAME}#{GRAPH_HEADING})"
    )

    readme = README.read_text(encoding="utf-8")
    updated, matches = re.subn(r"(?m)^.*(?= <!-- github-contributions -->$)", line, readme)
    if matches != 1:
        raise ValueError("Expected exactly one GitHub contribution line in the README")
    if updated != readme:
        README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
