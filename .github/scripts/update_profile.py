"""Refresh the public activity sections in the GitHub profile README."""

import json
import os
import re
from calendar import day_name
from collections import Counter
from datetime import datetime, time, timedelta
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo


USERNAME = os.getenv("GITHUB_REPOSITORY_OWNER", "signaloninternet")
TIME_ZONE = ZoneInfo("Asia/Kolkata")
README = Path(__file__).resolve().parents[2] / "README.md"
PAGE_SIZE = 100
SEARCH_LIMIT = 1000


def github(path, **params):
    url = "https://api.github.com" + path
    if params:
        url += "?" + urlencode(params)

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "signaloninternet-profile-readme",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    with urlopen(Request(url, headers=headers), timeout=30) as response:
        return json.load(response)


def owned_repositories():
    repositories = []
    page = 1
    while True:
        batch = github(f"/users/{USERNAME}/repos", type="owner", per_page=PAGE_SIZE, page=page)
        repositories.extend(repo for repo in batch if not repo["private"])
        if len(batch) < PAGE_SIZE:
            return repositories
        page += 1


def public_commits(start, end):
    since = datetime.combine(start, time.min, TIME_ZONE).isoformat()
    until = datetime.combine(end, time(23, 59, 59), TIME_ZONE).isoformat()
    params = {
        "q": f"author:{USERNAME} is:public author-date:{since}..{until}",
        "sort": "author-date",
        "order": "asc",
        "per_page": PAGE_SIZE,
    }
    first = github("/search/commits", **params)
    count = first["total_count"]
    if first["incomplete_results"] or count > SEARCH_LIMIT:
        if start == end:
            raise RuntimeError(f"GitHub returned incomplete commit search results for {start}")
        midpoint = start + (end - start) // 2
        return public_commits(start, midpoint) + public_commits(midpoint + timedelta(days=1), end)

    items = first["items"]
    for offset in range(PAGE_SIZE, count, PAGE_SIZE):
        batch = github("/search/commits", page=offset // PAGE_SIZE + 1, **params)
        if batch["incomplete_results"] or batch["total_count"] != count:
            raise RuntimeError("GitHub commit search changed during pagination")
        items.extend(batch["items"])

    if len({(item["sha"], item["repository"]["id"]) for item in items}) != count:
        raise RuntimeError("GitHub returned missing or duplicate commit search results")
    return items


def chart(rows, total, show_count=False):
    rows = list(rows)
    if not total:
        return "_No public data in this period._"

    name_width = max(len(name) for name, _ in rows)
    count_width = max(len(f"{value:,}") for _, value in rows) if show_count else 0
    bar_width = 11
    lines = []
    for name, value in rows:
        share = round(value / total, 3)
        full_blocks, fraction = divmod(round(share * bar_width * 8), 8)
        partial_block = "▏▎▍▌▋▊▉"[fraction - 1] if fraction else ""
        bar = ("█" * full_blocks + partial_block).ljust(bar_width, "░")
        count = f" {value:>{count_width},}" if show_count else ""
        lines.append(f"{name:<{name_width}}{count} {bar} {share:>5.1%}")
    return "```text\n" + "\n".join(lines) + "\n```"


def display_date(day):
    return f"{day.day} {day:%b %Y}"


def github_activity(today):
    start = today - timedelta(days=365)
    end = today - timedelta(days=1)

    commits = {}
    active_repos = set()
    for item in public_commits(start, end):
        date = item["commit"]["author"]["date"].replace("Z", "+00:00")
        authored = datetime.fromisoformat(date).astimezone(TIME_ZONE)
        if start <= authored.date() <= end and not item["repository"]["private"]:
            commits[item["sha"]] = authored
            active_repos.add(item["repository"]["full_name"])

    repositories = owned_repositories()
    languages = Counter()
    for repo in repositories:
        if not repo["fork"]:
            languages.update(github(f"/repos/{repo['full_name']}/languages"))

    followers = github(f"/users/{USERNAME}")["followers"]
    stars = sum(repo["stargazers_count"] for repo in repositories)
    total = len(commits)
    repository_count = len(active_repos)
    commit_label = "commit" if total == 1 else "commits"
    repository_label = "repository" if repository_count == 1 else "repositories"
    weekdays = Counter(authored.weekday() for authored in commits.values())
    periods = Counter(authored.hour // 6 for authored in commits.values())
    day_rows = [(day_name[index], weekdays[index]) for index in range(7)]
    time_rows = [
        ("Morning", periods[1]),
        ("Daytime", periods[2]),
        ("Evening", periods[3]),
        ("Night", periods[0]),
    ]
    language_rows = sorted(languages.items(), key=lambda entry: (-entry[1], entry[0]))
    language_total = sum(languages.values())
    top_languages = language_rows[:5]
    remainder = language_total - sum(value for _, value in top_languages)
    if remainder:
        top_languages.append(("Other", remainder))

    return f"""**Public repos** {len(repositories):,} · **Stars earned** {stars:,} · **Followers** {followers:,}

### Public commit activity

**{total:,}** {commit_label} across **{repository_count:,}** {repository_label} · {display_date(start)} to {display_date(end)}

Times are in **Asia/Kolkata (IST)**. Counts cover distinct authored commits indexed by GitHub on public default branches.

**By time of day** · Four 6-hour windows starting at 06:00 IST

{chart(time_rows, total, show_count=True)}

**By weekday**

{chart(day_rows, total, show_count=True)}

### Languages in public repositories

Share of code by byte count, across owned public repositories excluding forks.

{chart(top_languages, language_total)}

_Updated {display_date(today)} via the GitHub API._"""


def coding_time():
    # Create a public language chart at https://wakatime.com/share, then use its
    # SVG URL as the WAKATIME_LANGUAGES_EMBED_URL repository variable.
    url = os.getenv("WAKATIME_LANGUAGES_EMBED_URL", "").strip()
    if not url:
        return ""
    if not re.fullmatch(r"https://wakatime\.com/share/@?[A-Za-z0-9_.-]+/[A-Fa-f0-9-]+\.svg", url):
        raise ValueError("WAKATIME_LANGUAGES_EMBED_URL must be a WakaTime share SVG URL")
    return f"### Tracked coding time\n\n![Coding time by language from WakaTime]({url})"


def replace_section(readme, name, content):
    start = f"<!-- {name}:start -->"
    end = f"<!-- {name}:end -->"
    if readme.count(start) != 1 or readme.count(end) != 1 or readme.index(end) < readme.index(start):
        raise ValueError(f"Expected one ordered pair of README markers for {name}")

    head, _, rest = readme.partition(start)
    _, _, tail = rest.partition(end)
    body = f"\n\n{content}\n\n" if content else "\n"
    return head + start + body + end + tail


def main():
    readme = README.read_text(encoding="utf-8")
    tracked_time = coding_time()
    today = datetime.now(TIME_ZONE).date()
    updated = replace_section(readme, "github-activity", github_activity(today))
    updated = replace_section(updated, "coding-time", tracked_time)
    if updated != readme:
        README.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
