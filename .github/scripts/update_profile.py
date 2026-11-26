"""Refresh the public GitHub stats on the profile card and its alt text."""

import json
import os
import re
from datetime import datetime, time, timedelta
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo


USERNAME = os.getenv("GITHUB_REPOSITORY_OWNER", "signaloninternet")
TIME_ZONE = ZoneInfo("Asia/Kolkata")
ROOT = Path(__file__).resolve().parents[2]
README = ROOT / "README.md"
CARD = ROOT / "assets/profile-header.svg"
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



def replace_one(source, pattern, replacement):
    updated, count = re.subn(pattern, replacement, source)
    if count != 1:
        raise ValueError(f"Expected one match for {pattern}")
    return updated


def main():
    today = datetime.now(TIME_ZONE).date()
    start = today - timedelta(days=365)
    end = today - timedelta(days=1)

    commits = set()
    for item in public_commits(start, end):
        date = item["commit"]["author"]["date"].replace("Z", "+00:00")
        authored = datetime.fromisoformat(date).astimezone(TIME_ZONE)
        if start <= authored.date() <= end and not item["repository"]["private"]:
            commits.add(item["sha"])

    repositories = owned_repositories()
    stars = sum(repo["stargazers_count"] for repo in repositories)
    followers = github(f"/users/{USERNAME}")["followers"]
    stats = {
        "repo-count": len(repositories),
        "commit-count": len(commits),
        "star-count": stars,
        "follower-count": followers,
    }

    card = CARD.read_text(encoding="utf-8")
    updated_card = card
    for field, value in stats.items():
        updated_card = replace_one(
            updated_card,
            rf'(<text id="{field}"[^>]*>)[0-9,]+(</text>)',
            lambda match: f"{match[1]}{value:,}{match[2]}",
        )

    star_label = "star" if stars == 1 else "stars"
    commits_label = "commit" if len(commits) == 1 else "commits"
    repo_label = "repository" if len(repositories) == 1 else "repositories"
    follower_label = "follower" if followers == 1 else "followers"
    summary = (
        f"GitHub stats: {len(repositories):,} public {repo_label}, {stars:,} {star_label}, "
        f"{len(commits):,} public {commits_label} in the past 365 days, "
        f"and {followers:,} {follower_label}."
    )
    readme = README.read_text(encoding="utf-8")
    updated_readme = replace_one(readme, r'GitHub stats: [^".]+\.', summary)

    if updated_card != card:
        CARD.write_text(updated_card, encoding="utf-8")
    if updated_readme != readme:
        README.write_text(updated_readme, encoding="utf-8")


if __name__ == "__main__":
    main()
