#!/usr/bin/env python3
"""Find proven catalog candidates repeated across trusted upstream lists."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SOURCES_PATH = ROOT / "data" / "sources.json"
PROJECTS_PATH = ROOT / "data" / "projects.json"
STACK_PROJECTS_PATH = ROOT / "data" / "stack-projects.json"
WATCHLIST_PATH = ROOT / "data" / "watchlist.json"
EXCLUSIONS_PATH = ROOT / "data" / "exclusions.json"
SEARCHES_PATH = ROOT / "data" / "searches.json"
OUTPUT_PATH = ROOT / "data" / "candidates.json"
GITHUB_REPO_URL = re.compile(
    r"https?://github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)", re.IGNORECASE
)
NON_REPOSITORY_OWNERS = {"apps", "features", "marketplace", "orgs", "sponsors", "topics"}


def load_json(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def github_request(path: str, accept: str = "application/vnd.github+json") -> Any:
    token = os.environ.get("GITHUB_TOKEN")
    request = urllib.request.Request(
        f"https://api.github.com/{path}",
        headers={
            "Accept": accept,
            "User-Agent": "awesome-agent-runtimes-discovery-audit",
            "X-GitHub-Api-Version": "2022-11-28",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        if "raw" in accept:
            return response.read().decode("utf-8")
        return json.load(response)


def normalize_link(owner: str, name: str) -> str | None:
    if owner.casefold() in NON_REPOSITORY_OWNERS:
        return None
    cleaned = name.rstrip(".,;:)'\"]}")
    if cleaned.endswith(".git"):
        cleaned = cleaned[:-4]
    return f"{owner}/{cleaned}" if cleaned else None


def parse_time(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-stars", type=int, default=5000)
    parser.add_argument("--min-sources", type=int, default=2)
    parser.add_argument("--min-age-days", type=int, default=180)
    parser.add_argument("--max-stale-days", type=int, default=365)
    parser.add_argument("--search-limit", type=int, default=50)
    parser.add_argument("--output", type=Path, default=OUTPUT_PATH)
    args = parser.parse_args()

    sources = load_json(SOURCES_PATH)["sources"]
    reviewed = {
        item["repo"].casefold()
        for source_path in (PROJECTS_PATH, STACK_PROJECTS_PATH, WATCHLIST_PATH, EXCLUSIONS_PATH)
        for item in load_json(source_path)["projects"]
    }
    mentions: dict[str, set[str]] = defaultdict(set)
    original_names: dict[str, str] = {}

    for source in sources:
        repo = source["repo"]
        try:
            readme = github_request(f"repos/{repo}/readme", "application/vnd.github.raw+json")
        except urllib.error.URLError as error:
            print(f"warning: could not read {repo}: {error}", file=sys.stderr)
            continue
        found: set[str] = set()
        for match in GITHUB_REPO_URL.finditer(readme):
            candidate = normalize_link(match.group(1), match.group(2))
            if candidate and candidate.casefold() not in reviewed:
                found.add(candidate.casefold())
                original_names.setdefault(candidate.casefold(), candidate)
        for candidate in found:
            mentions[candidate].add(repo)

    searches = load_json(SEARCHES_PATH)["queries"]
    for search in searches:
        query = urllib.parse.urlencode(
            {"q": search["query"], "sort": "stars", "order": "desc", "per_page": args.search_limit}
        )
        try:
            result = github_request(f"search/repositories?{query}")
        except urllib.error.URLError as error:
            print(f"warning: could not run search {search['id']}: {error}", file=sys.stderr)
            continue
        source_name = f"github-search:{search['id']}"
        for item in result.get("items", []):
            candidate = item.get("full_name")
            if not isinstance(candidate, str) or candidate.casefold() in reviewed:
                continue
            key = candidate.casefold()
            original_names.setdefault(key, candidate)
            mentions[key].add(source_name)

    repeated = [repo for repo, found_in in mentions.items() if len(found_in) >= args.min_sources]
    now = dt.datetime.now(dt.timezone.utc)
    candidates_by_canonical: dict[str, dict[str, Any]] = {}
    failures: list[str] = []
    for index, key in enumerate(sorted(repeated), start=1):
        requested = original_names[key]
        try:
            item = github_request(f"repos/{requested}")
        except urllib.error.URLError as error:
            failures.append(f"{requested}: {error}")
            continue
        canonical = item["full_name"]
        canonical_key = canonical.casefold()
        if canonical_key in reviewed or item["fork"] or item["archived"]:
            continue
        pushed_at = parse_time(item["pushed_at"])
        created_at = parse_time(item["created_at"])
        age_days = (now - created_at).days
        if (
            item["stargazers_count"] < args.min_stars
            or age_days < args.min_age_days
            or (now - pushed_at).days > args.max_stale_days
        ):
            continue
        sources_for_candidate = set(mentions[key])
        existing = candidates_by_canonical.get(canonical_key)
        if existing:
            sources_for_candidate.update(existing["sources"])
        candidates_by_canonical[canonical_key] = {
            "repo": canonical,
            "stars": item["stargazers_count"],
            "forks": item["forks_count"],
            "language": item["language"],
            "license": (item.get("license") or {}).get("spdx_id"),
            "created_at": item["created_at"],
            "pushed_at": item["pushed_at"],
            "age_days": age_days,
            "days_since_push": (now - pushed_at).days,
            "source_mentions": len(sources_for_candidate),
            "sources": sorted(sources_for_candidate, key=str.casefold),
            "description": item.get("description"),
        }
        print(f"reviewed {index}/{len(repeated)}: {requested}", file=sys.stderr)

    candidates = sorted(
        candidates_by_canonical.values(),
        key=lambda item: (-item["source_mentions"], -item["stars"], item["repo"].casefold()),
    )
    result = {
        "schema_version": 1,
        "generated_at": now.replace(microsecond=0).isoformat(),
        "notice": "Discovery candidates are not endorsed catalog entries; every item requires a manual scope review.",
        "criteria": {
            "minimum_stars": args.min_stars,
            "minimum_source_mentions": args.min_sources,
            "minimum_repository_age_days": args.min_age_days,
            "maximum_days_since_push": args.max_stale_days,
            "archived_repositories": "excluded",
            "forks": "excluded",
        },
        "source_count": len(sources),
        "search_count": len(searches),
        "candidate_count": len(candidates),
        "candidates": candidates,
    }
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if failures:
        print("warning: repository metadata failures:", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
    print(f"wrote {len(candidates)} candidates to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
