#!/usr/bin/env python3
"""Validate the catalog, refresh GitHub metadata, and render README.md."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROJECTS_PATH = ROOT / "data" / "projects.json"
STACK_PROJECTS_PATH = ROOT / "data" / "stack-projects.json"
WATCHLIST_PATH = ROOT / "data" / "watchlist.json"
EXCLUSIONS_PATH = ROOT / "data" / "exclusions.json"
METRICS_PATH = ROOT / "data" / "metrics.json"
HISTORY_PATH = ROOT / "data" / "history.json"
TRENDS_PATH = ROOT / "data" / "trends.json"
CATALOG_PATH = ROOT / "data" / "catalog.json"
CSV_PATH = ROOT / "data" / "catalog.csv"
STACK_CATALOG_PATH = ROOT / "data" / "stack-catalog.json"
STACK_CSV_PATH = ROOT / "data" / "stack-catalog.csv"
LLMS_PATH = ROOT / "llms.txt"
TAGS_PATH = ROOT / "TAGS.md"
TEMPLATE_PATH = ROOT / "README.template.md"
README_PATH = ROOT / "README.md"
STACK_TEMPLATE_PATH = ROOT / "STACK.template.md"
STACK_PATH = ROOT / "STACK.md"
WATCHLIST_MD_PATH = ROOT / "WATCHLIST.md"
EXCLUSIONS_MD_PATH = ROOT / "EXCLUSIONS.md"
REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
ALLOWED_DEPLOYMENTS = {"library", "local", "self-hosted", "managed"}
MINIMUM_STARS = 5000
MINIMUM_AGE_DAYS = 180
MAXIMUM_STALE_DAYS = 365


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists() and default is not None:
        return default
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def dump_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def parse_time(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def effective_license(project: dict[str, Any], metadata: dict[str, Any]) -> str | None:
    detected = metadata.get("license")
    if detected == "NOASSERTION":
        detected = None
    return project.get("license_override") or detected


def validate(catalog: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    category_ids = [item.get("id") for item in catalog.get("categories", [])]
    if len(category_ids) != len(set(category_ids)):
        errors.append("category IDs must be unique")

    seen_names: set[str] = set()
    seen_repos: set[str] = set()
    for index, project in enumerate(catalog.get("projects", []), start=1):
        label = project.get("name") or f"project #{index}"
        required = {"name", "repo", "category", "description", "deployment", "tags"}
        missing = sorted(required - project.keys())
        if missing:
            errors.append(f"{label}: missing {', '.join(missing)}")
            continue
        if project["name"].casefold() in seen_names:
            errors.append(f"{label}: duplicate name")
        seen_names.add(project["name"].casefold())
        if project["repo"].casefold() in seen_repos:
            errors.append(f"{label}: duplicate repository")
        seen_repos.add(project["repo"].casefold())
        if not REPO_RE.fullmatch(project["repo"]):
            errors.append(f"{label}: repo must be owner/name")
        if project["category"] not in category_ids:
            errors.append(f"{label}: unknown category {project['category']!r}")
        if not project["description"].endswith("."):
            errors.append(f"{label}: description must end with a period")
        if "license_override" in project and not isinstance(project["license_override"], str):
            errors.append(f"{label}: license_override must be a string")
        deployments = project["deployment"]
        if not isinstance(deployments, list) or not deployments:
            errors.append(f"{label}: deployment must be a non-empty list")
        elif invalid := sorted(set(deployments) - ALLOWED_DEPLOYMENTS):
            errors.append(f"{label}: invalid deployment values: {', '.join(invalid)}")
        tags = project["tags"]
        if not isinstance(tags, list) or not (1 <= len(tags) <= 4):
            errors.append(f"{label}: provide between one and four tags")

    if not catalog.get("projects"):
        errors.append("catalog must contain at least one project")
    return errors


def validate_stack(stack: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    category_ids = [item.get("id") for item in stack.get("categories", [])]
    if len(category_ids) != len(set(category_ids)):
        errors.append("stack category IDs must be unique")
    seen: set[str] = set()
    for project in stack.get("projects", []):
        label = project.get("name", "unnamed stack project")
        required = {"name", "repo", "category", "description", "tags"}
        if missing := sorted(required - project.keys()):
            errors.append(f"{label}: missing {', '.join(missing)}")
            continue
        if project["repo"].casefold() in seen:
            errors.append(f"{label}: duplicate stack repository")
        seen.add(project["repo"].casefold())
        if not REPO_RE.fullmatch(project["repo"]):
            errors.append(f"{label}: repo must be owner/name")
        if project["category"] not in category_ids:
            errors.append(f"{label}: unknown stack category {project['category']!r}")
        if not project["description"].endswith("."):
            errors.append(f"{label}: description must end with a period")
        if not isinstance(project["tags"], list) or not (1 <= len(project["tags"]) <= 4):
            errors.append(f"{label}: provide between one and four tags")
    return errors


def validate_watchlist(watchlist: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for project in watchlist.get("projects", []):
        label = project.get("name", "unnamed watchlist project")
        required = {"name", "repo", "boundary", "review_after", "reason"}
        if missing := sorted(required - project.keys()):
            errors.append(f"{label}: missing {', '.join(missing)}")
            continue
        if project["repo"].casefold() in seen:
            errors.append(f"{label}: duplicate watchlist repository")
        seen.add(project["repo"].casefold())
        if not REPO_RE.fullmatch(project["repo"]):
            errors.append(f"{label}: repo must be owner/name")
        try:
            dt.date.fromisoformat(project["review_after"])
        except (TypeError, ValueError):
            errors.append(f"{label}: review_after must be YYYY-MM-DD")
    return errors


def validate_exclusions(exclusions: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    seen: set[str] = set()
    for project in exclusions.get("projects", []):
        label = project.get("name", "unnamed excluded project")
        required = {"name", "repo", "reviewed_at", "reason", "reconsider_when"}
        if missing := sorted(required - project.keys()):
            errors.append(f"{label}: missing {', '.join(missing)}")
            continue
        if project["repo"].casefold() in seen:
            errors.append(f"{label}: duplicate excluded repository")
        seen.add(project["repo"].casefold())
        if not REPO_RE.fullmatch(project["repo"]):
            errors.append(f"{label}: repo must be owner/name")
    return errors


def tracked_projects(
    catalog: dict[str, Any], stack: dict[str, Any], watchlist: dict[str, Any]
) -> list[dict[str, Any]]:
    by_repo: dict[str, dict[str, Any]] = {}
    for project in [*catalog["projects"], *stack["projects"], *watchlist["projects"]]:
        by_repo.setdefault(project["repo"].casefold(), project)
    return list(by_repo.values())


def github_metadata(repo: str, token: str | None) -> dict[str, Any]:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-agent-runtimes-metadata-refresh",
            "X-GitHub-Api-Version": "2022-11-28",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        payload = json.load(response)
    return {
        "repo": payload["full_name"],
        "stars": payload["stargazers_count"],
        "forks": payload["forks_count"],
        "open_issues": payload["open_issues_count"],
        "language": payload["language"],
        "license": (payload.get("license") or {}).get("spdx_id"),
        "archived": payload["archived"],
        "created_at": payload["created_at"],
        "pushed_at": payload["pushed_at"],
        "homepage": payload.get("homepage") or None,
        "default_branch": payload["default_branch"],
    }


def validate_metrics(
    catalog: dict[str, Any],
    stack: dict[str, Any],
    watchlist: dict[str, Any],
    metrics: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    metadata = metrics.get("repositories", {})
    now = dt.datetime.now(dt.timezone.utc)
    for project in catalog["projects"]:
        repo = project["repo"]
        item = metadata.get(repo)
        if not item:
            errors.append(f"{repo}: missing GitHub metadata")
            continue
        stars = item.get("stars")
        if not isinstance(stars, int) or stars < MINIMUM_STARS:
            errors.append(f"{repo}: requires at least {MINIMUM_STARS:,} stars (found {stars!r})")
        canonical = item.get("repo")
        if not isinstance(canonical, str) or canonical.casefold() != repo.casefold():
            errors.append(f"{repo}: source should use canonical repository name {canonical!r}")
        if not effective_license(project, item):
            errors.append(f"{repo}: requires a detected license or an editorial license_override")
        if project["category"] == "historical":
            if not item.get("archived"):
                errors.append(f"{repo}: historical entries must be archived on GitHub")
            continue
        if item.get("archived"):
            errors.append(f"{repo}: archived projects must move to the historical category")
        created_at = item.get("created_at")
        pushed_at = item.get("pushed_at")
        if not isinstance(created_at, str):
            errors.append(f"{repo}: missing repository creation timestamp")
        elif (now - parse_time(created_at)).days < MINIMUM_AGE_DAYS:
            errors.append(f"{repo}: requires at least {MINIMUM_AGE_DAYS} days of public history")
        if not isinstance(pushed_at, str):
            errors.append(f"{repo}: missing last-push timestamp")
        elif (now - parse_time(pushed_at)).days > MAXIMUM_STALE_DAYS:
            errors.append(f"{repo}: no push within the last {MAXIMUM_STALE_DAYS} days")

    for project in [*stack["projects"], *watchlist["projects"]]:
        repo = project["repo"]
        item = metadata.get(repo)
        if not item:
            errors.append(f"{repo}: missing tracked metadata")
            continue
        canonical = item.get("repo")
        if not isinstance(canonical, str) or canonical.casefold() != repo.casefold():
            errors.append(f"{repo}: source should use canonical repository name {canonical!r}")
    return errors


def refresh(projects: list[dict[str, Any]], old_metrics: dict[str, Any]) -> dict[str, Any]:
    token = os.environ.get("GITHUB_TOKEN")
    old_by_repo = old_metrics.get("repositories", {})
    repositories: dict[str, Any] = {}
    failures: list[str] = []
    for project in projects:
        repo = project["repo"]
        try:
            repositories[repo] = github_metadata(repo, token)
            print(f"refreshed {repo}", file=sys.stderr)
        except (urllib.error.URLError, TimeoutError, KeyError, json.JSONDecodeError) as error:
            if repo in old_by_repo:
                repositories[repo] = old_by_repo[repo]
                failures.append(f"{repo} (kept previous metadata: {error})")
            else:
                failures.append(f"{repo} ({error})")
    if failures:
        print("Metadata refresh failures:", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
    missing = [project["repo"] for project in projects if project["repo"] not in repositories]
    if missing:
        raise RuntimeError("no metadata available for: " + ", ".join(missing))
    return {
        "schema_version": 1,
        "fetched_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "repositories": repositories,
    }


def escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def markdown_table(headers: list[str], rows: list[list[str]], right_aligned: set[int] | None = None) -> list[str]:
    """Render a pipe-aligned table accepted by awesome-lint."""
    right_aligned = right_aligned or set()
    widths = [
        max(3, len(headers[index]), *(len(row[index]) for row in rows))
        for index in range(len(headers))
    ]

    def row_line(cells: list[str]) -> str:
        return "| " + " | ".join(cell.ljust(widths[index]) for index, cell in enumerate(cells)) + " |"

    separators = [
        ("-" * (width - 1) + ":") if index in right_aligned else ("-" * width)
        for index, width in enumerate(widths)
    ]
    return [row_line(headers), row_line(separators), *(row_line(row) for row in rows)]


def build_trends(history: dict[str, Any], metrics: dict[str, Any]) -> dict[str, Any]:
    fetched_at = metrics.get("fetched_at")
    if not isinstance(fetched_at, str):
        return {"schema_version": 1, "generated_at": None, "repositories": {}}
    current_date = parse_time(fetched_at).date()
    snapshots = sorted(history.get("snapshots", []), key=lambda item: item.get("date", ""))
    repositories: dict[str, dict[str, int | None]] = {}
    for repo, item in metrics.get("repositories", {}).items():
        current = item.get("stars")
        if not isinstance(current, int):
            continue
        deltas: dict[str, int | None] = {}
        for days in (7, 30, 90):
            target = current_date - dt.timedelta(days=days)
            prior = next(
                (
                    snapshot.get("stars", {}).get(repo)
                    for snapshot in reversed(snapshots)
                    if snapshot.get("date", "") <= target.isoformat()
                    and isinstance(snapshot.get("stars", {}).get(repo), int)
                ),
                None,
            )
            deltas[f"{days}d"] = current - prior if isinstance(prior, int) else None
        repositories[repo] = deltas
    return {"schema_version": 1, "generated_at": fetched_at, "repositories": repositories}


def trend_text(trends: dict[str, Any], repo: str, window: str = "30d") -> str:
    value = trends.get("repositories", {}).get(repo, {}).get(window)
    if not isinstance(value, int):
        return "—"
    return f"{value:+,}"


def render_catalog(catalog: dict[str, Any], metrics: dict[str, Any], trends: dict[str, Any]) -> str:
    metadata = metrics.get("repositories", {})
    sections: list[str] = []
    for category in catalog["categories"]:
        sections.extend([f"### {category['title']}", "", category["description"], ""])
        rows: list[list[str]] = []
        projects = sorted(
            (item for item in catalog["projects"] if item["category"] == category["id"]),
            key=lambda item: item["name"].casefold(),
        )
        for project in projects:
            repo = project["repo"]
            item = metadata.get(repo, {})
            project_name = f"[{escape_cell(project['name'])}](https://github.com/{repo})"
            if item.get("archived"):
                project_name += " **Archived**"
            stars = item.get("stars")
            star_text = f"⭐ {stars:,}" if isinstance(stars, int) else "—"
            license_name = effective_license(project, item)
            stack_parts = [part for part in (item.get("language"), license_name) if part]
            stack = " · ".join(stack_parts) or "—"
            evidence = f"https://github.com/{repo}#readme"
            fit = f"{project['description']} [evidence]({evidence}) `{'` `'.join(project['tags'])}`"
            deploy = ", ".join(project["deployment"])
            activity = item.get("pushed_at", "")[:10] or "—"
            rows.append(
                [
                    project_name,
                    star_text,
                    trend_text(trends, repo),
                    escape_cell(fit),
                    escape_cell(stack),
                    escape_cell(deploy),
                    activity,
                ]
            )
        sections.extend(
            markdown_table(
                ["Project", "Stars", "30d", "Runtime fit", "Stack", "Deploy", "Last push"],
                rows,
                {1, 2},
            )
        )
        sections.append("")
    return "\n".join(sections).rstrip()


def render_readme(catalog: dict[str, Any], metrics: dict[str, Any], trends: dict[str, Any]) -> str:
    fetched_at = metrics.get("fetched_at", "unavailable")
    updated = fetched_at[:10] if fetched_at != "unavailable" else fetched_at
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    return (
        template.replace("{{PROJECT_COUNT}}", str(len(catalog["projects"])))
        .replace("{{UPDATED_AT}}", updated)
        .replace("{{CATALOG}}", render_catalog(catalog, metrics, trends))
    )


def merged_catalog(catalog: dict[str, Any], metrics: dict[str, Any]) -> dict[str, Any]:
    """Return the curated catalog joined with its latest GitHub metadata."""
    metadata = metrics.get("repositories", {})
    projects: list[dict[str, Any]] = []
    for project in catalog["projects"]:
        repo = project["repo"]
        item = metadata.get(repo, {})
        projects.append(
            {
                **project,
                "repository_url": f"https://github.com/{repo}",
                "evidence_url": f"https://github.com/{repo}#readme",
                "github": {
                    **{
                        key: item.get(key)
                        for key in (
                            "stars",
                            "forks",
                            "open_issues",
                            "language",
                            "archived",
                            "created_at",
                            "pushed_at",
                            "homepage",
                            "default_branch",
                        )
                    },
                    "license": effective_license(project, item),
                },
            }
        )
    return {
        "schema_version": 1,
        "generated_at": metrics.get("fetched_at"),
        "categories": catalog["categories"],
        "projects": sorted(projects, key=lambda item: item["name"].casefold()),
    }


def render_csv(catalog: dict[str, Any], metrics: dict[str, Any]) -> str:
    output = io.StringIO(newline="")
    fields = [
        "name",
        "category",
        "repository",
        "description",
        "evidence",
        "stars",
        "forks",
        "language",
        "license",
        "archived",
        "created_at",
        "last_push",
        "deployment",
        "tags",
    ]
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    metadata = metrics.get("repositories", {})
    for project in sorted(catalog["projects"], key=lambda item: item["name"].casefold()):
        item = metadata.get(project["repo"], {})
        writer.writerow(
            {
                "name": project["name"],
                "category": project["category"],
                "repository": f"https://github.com/{project['repo']}",
                "description": project["description"],
                "evidence": f"https://github.com/{project['repo']}#readme",
                "stars": item.get("stars", ""),
                "forks": item.get("forks", ""),
                "language": item.get("language") or "",
                "license": effective_license(project, item) or "",
                "archived": str(bool(item.get("archived"))).lower(),
                "created_at": item.get("created_at") or "",
                "last_push": item.get("pushed_at") or "",
                "deployment": ";".join(project["deployment"]),
                "tags": ";".join(project["tags"]),
            }
        )
    return output.getvalue()


def render_llms(catalog: dict[str, Any], metrics: dict[str, Any]) -> str:
    metadata = metrics.get("repositories", {})
    lines = [
        "# Awesome Agent Runtimes",
        "",
        "A curated ownership map for agent cognition, supervision, continuity, isolation, and durable recovery.",
        f"Generated: {metrics.get('fetched_at', 'unavailable')}",
        "Source: https://github.com/beejmaxx/awesome-agent-runtimes",
        "Methodology: https://github.com/beejmaxx/awesome-agent-runtimes/blob/main/METHODOLOGY.md",
        "",
    ]
    for category in catalog["categories"]:
        lines.extend([f"## {category['title']}", "", category["description"], ""])
        projects = sorted(
            (project for project in catalog["projects"] if project["category"] == category["id"]),
            key=lambda item: item["name"].casefold(),
        )
        for project in projects:
            item = metadata.get(project["repo"], {})
            stars = f"{item['stars']:,} stars" if isinstance(item.get("stars"), int) else "stars unavailable"
            state = "archived; " if item.get("archived") else ""
            labels = ", ".join([*project["deployment"], *project["tags"]])
            lines.append(
                f"- {project['name']} (https://github.com/{project['repo']}): "
                f"{project['description']} [{state}{stars}; {labels}]"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_tags(catalog: dict[str, Any]) -> str:
    by_tag: dict[str, list[dict[str, Any]]] = {}
    for project in catalog["projects"]:
        for tag in project["tags"]:
            by_tag.setdefault(tag, []).append(project)
    lines = [
        "# Agent Runtime Capability Index",
        "",
        "Generated from [`data/projects.json`](data/projects.json). Edit the source catalog, not this file.",
        "",
    ]
    for tag in sorted(by_tag, key=str.casefold):
        lines.extend([f"## {tag}", ""])
        for project in sorted(by_tag[tag], key=lambda item: item["name"].casefold()):
            status = " **Archived**" if project["category"] == "historical" else ""
            lines.append(
                f"- [{project['name']}](https://github.com/{project['repo']}){status} - "
                f"{project['description']}"
            )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def merged_stack(stack: dict[str, Any], metrics: dict[str, Any]) -> dict[str, Any]:
    metadata = metrics.get("repositories", {})
    projects: list[dict[str, Any]] = []
    for project in stack["projects"]:
        repo = project["repo"]
        item = metadata.get(repo, {})
        projects.append(
            {
                **project,
                "repository_url": f"https://github.com/{repo}",
                "evidence_url": f"https://github.com/{repo}#readme",
                "github": {
                    "stars": item.get("stars"),
                    "forks": item.get("forks"),
                    "language": item.get("language"),
                    "license": effective_license(project, item),
                    "archived": item.get("archived"),
                    "created_at": item.get("created_at"),
                    "pushed_at": item.get("pushed_at"),
                },
            }
        )
    return {
        "schema_version": 1,
        "generated_at": metrics.get("fetched_at"),
        "categories": stack["categories"],
        "projects": sorted(projects, key=lambda item: item["name"].casefold()),
    }


def render_stack_catalog(stack: dict[str, Any], metrics: dict[str, Any], trends: dict[str, Any]) -> str:
    metadata = metrics.get("repositories", {})
    sections: list[str] = []
    for category in stack["categories"]:
        sections.extend([f"### {category['title']}", "", category["description"], ""])
        rows: list[list[str]] = []
        projects = sorted(
            (project for project in stack["projects"] if project["category"] == category["id"]),
            key=lambda item: item["name"].casefold(),
        )
        for project in projects:
            repo = project["repo"]
            item = metadata.get(repo, {})
            stars = item.get("stars")
            role = f"{project['description']} [evidence](https://github.com/{repo}#readme)"
            if project.get("exception"):
                role += f" **Scope note:** {project['exception']}"
            license_name = effective_license(project, item) or "—"
            rows.append(
                [
                    f"[{escape_cell(project['name'])}](https://github.com/{repo})",
                    f"⭐ {stars:,}" if isinstance(stars, int) else "—",
                    trend_text(trends, repo),
                    escape_cell(role),
                    escape_cell(license_name),
                    item.get("pushed_at", "")[:10] or "—",
                ]
            )
        sections.extend(
            markdown_table(["Project", "Stars", "30d", "Role", "License", "Last push"], rows, {1, 2})
        )
        sections.append("")
    return "\n".join(sections).rstrip()


def render_stack(stack: dict[str, Any], metrics: dict[str, Any], trends: dict[str, Any]) -> str:
    template = STACK_TEMPLATE_PATH.read_text(encoding="utf-8")
    return template.replace("{{STACK_CATALOG}}", render_stack_catalog(stack, metrics, trends))


def render_stack_csv(stack: dict[str, Any], metrics: dict[str, Any]) -> str:
    output = io.StringIO(newline="")
    fields = [
        "name",
        "category",
        "repository",
        "description",
        "evidence",
        "stars",
        "language",
        "license",
        "last_push",
        "tags",
        "exception",
    ]
    writer = csv.DictWriter(output, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    metadata = metrics.get("repositories", {})
    for project in sorted(stack["projects"], key=lambda item: item["name"].casefold()):
        item = metadata.get(project["repo"], {})
        writer.writerow(
            {
                "name": project["name"],
                "category": project["category"],
                "repository": f"https://github.com/{project['repo']}",
                "description": project["description"],
                "evidence": f"https://github.com/{project['repo']}#readme",
                "stars": item.get("stars", ""),
                "language": item.get("language") or "",
                "license": effective_license(project, item) or "",
                "last_push": item.get("pushed_at") or "",
                "tags": ";".join(project["tags"]),
                "exception": project.get("exception", ""),
            }
        )
    return output.getvalue()


def render_watchlist(watchlist: dict[str, Any], metrics: dict[str, Any]) -> str:
    rows: list[list[str]] = []
    metadata = metrics.get("repositories", {})
    for project in sorted(watchlist["projects"], key=lambda item: (item["review_after"], item["name"].casefold())):
        repo = project["repo"]
        item = metadata.get(repo, {})
        stars = item.get("stars")
        created_at = item.get("created_at")
        age_gate = "—"
        if isinstance(created_at, str):
            eligible_at = parse_time(created_at) + dt.timedelta(days=MINIMUM_AGE_DAYS)
            age_gate = eligible_at.strftime("%Y-%m-%d %H:%M UTC")
        rows.append(
            [
                f"[{project['name']}](https://github.com/{repo})",
                f"⭐ {stars:,}" if isinstance(stars, int) else "—",
                project["boundary"],
                age_gate,
                project["review_after"],
                project["reason"],
            ]
        )
    lines = [
        "# Project Watchlist",
        "",
        "Projects here are deliberately not core entries yet. Review dates are triggers for fresh evidence checks, not automatic promotion dates.",
        "",
        *markdown_table(
            ["Project", "Stars", "Boundary", "Age gate", "Review after", "Reason"], rows, {1}
        ),
        "",
        "Generated from [`data/watchlist.json`](data/watchlist.json).",
        "",
    ]
    return "\n".join(lines)


def render_exclusions(exclusions: dict[str, Any]) -> str:
    rows = [
        [
            f"[{project['name']}](https://github.com/{project['repo']})",
            project["reviewed_at"],
            project["reason"],
            project["reconsider_when"],
        ]
        for project in sorted(exclusions["projects"], key=lambda item: item["name"].casefold())
    ]
    lines = [
        "# Reviewed Exclusions",
        "",
        "This ledger records notable projects that were investigated and intentionally excluded. It prevents repeated review and makes corrections auditable.",
        "",
        *markdown_table(["Project", "Reviewed", "Why excluded", "Reconsider when"], rows),
        "",
        "Generated from [`data/exclusions.json`](data/exclusions.json).",
        "",
    ]
    return "\n".join(lines)


def generated_files(
    catalog: dict[str, Any],
    stack: dict[str, Any],
    watchlist: dict[str, Any],
    exclusions: dict[str, Any],
    metrics: dict[str, Any],
    history: dict[str, Any],
) -> dict[Path, str]:
    trends = build_trends(history, metrics)
    return {
        README_PATH: render_readme(catalog, metrics, trends),
        CATALOG_PATH: json.dumps(merged_catalog(catalog, metrics), indent=2, ensure_ascii=False) + "\n",
        CSV_PATH: render_csv(catalog, metrics),
        STACK_PATH: render_stack(stack, metrics, trends),
        STACK_CATALOG_PATH: json.dumps(merged_stack(stack, metrics), indent=2, ensure_ascii=False) + "\n",
        STACK_CSV_PATH: render_stack_csv(stack, metrics),
        WATCHLIST_MD_PATH: render_watchlist(watchlist, metrics),
        EXCLUSIONS_MD_PATH: render_exclusions(exclusions),
        TRENDS_PATH: json.dumps(trends, indent=2, ensure_ascii=False) + "\n",
        LLMS_PATH: render_llms(catalog, metrics),
        TAGS_PATH: render_tags(catalog),
    }


def write_generated_files(
    catalog: dict[str, Any],
    stack: dict[str, Any],
    watchlist: dict[str, Any],
    exclusions: dict[str, Any],
    metrics: dict[str, Any],
    history: dict[str, Any],
) -> None:
    for path, content in generated_files(catalog, stack, watchlist, exclusions, metrics, history).items():
        path.write_text(content, encoding="utf-8")


def update_history(metrics: dict[str, Any]) -> None:
    history = load_json(HISTORY_PATH, {"schema_version": 1, "snapshots": []})
    date = metrics["fetched_at"][:10]
    snapshot = {
        "date": date,
        "stars": {
            repo: item["stars"]
            for repo, item in sorted(metrics["repositories"].items())
            if isinstance(item.get("stars"), int)
        },
    }
    snapshots = [item for item in history.get("snapshots", []) if item.get("date") != date]
    snapshots.append(snapshot)
    history["snapshots"] = sorted(snapshots, key=lambda item: item["date"])
    dump_json(HISTORY_PATH, history)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without network access or file changes")
    parser.add_argument("--render-only", action="store_true", help="render README from existing metadata without network access")
    parser.add_argument("--no-history", action="store_true", help="do not store today's star snapshot")
    args = parser.parse_args()

    catalog = load_json(PROJECTS_PATH)
    stack = load_json(STACK_PROJECTS_PATH)
    watchlist = load_json(WATCHLIST_PATH)
    exclusions = load_json(EXCLUSIONS_PATH)
    errors = [
        *validate(catalog),
        *validate_stack(stack),
        *validate_watchlist(watchlist),
        *validate_exclusions(exclusions),
    ]
    scopes = {
        "core": {project["repo"].casefold() for project in catalog["projects"]},
        "stack": {project["repo"].casefold() for project in stack["projects"]},
        "watchlist": {project["repo"].casefold() for project in watchlist["projects"]},
        "excluded": {project["repo"].casefold() for project in exclusions["projects"]},
    }
    scope_names = list(scopes)
    for index, left in enumerate(scope_names):
        for right in scope_names[index + 1 :]:
            if overlap := sorted(scopes[left] & scopes[right]):
                errors.append(f"repositories cannot appear in both {left} and {right}: {', '.join(overlap)}")
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    if args.check:
        metrics = load_json(METRICS_PATH)
        history = load_json(HISTORY_PATH, {"schema_version": 1, "snapshots": []})
        metric_errors = validate_metrics(catalog, stack, watchlist, metrics)
        if metric_errors:
            for error in metric_errors:
                print(f"error: {error}", file=sys.stderr)
            return 1
        stale = [
            str(path.relative_to(ROOT))
            for path, expected in generated_files(
                catalog, stack, watchlist, exclusions, metrics, history
            ).items()
            if not path.exists() or path.read_text(encoding="utf-8") != expected
        ]
        if stale:
            print(f"error: generated files are stale: {', '.join(stale)}", file=sys.stderr)
            print("run python3 scripts/update.py --render-only", file=sys.stderr)
            return 1
        print(f"catalog valid: {len(catalog['projects'])} projects")
        return 0

    if args.render_only:
        metrics = load_json(METRICS_PATH)
        history = load_json(HISTORY_PATH, {"schema_version": 1, "snapshots": []})
        write_generated_files(catalog, stack, watchlist, exclusions, metrics, history)
        print(f"rendered {len(catalog['projects'])} core and {len(stack['projects'])} stack projects")
        return 0

    old_metrics = load_json(METRICS_PATH, {"repositories": {}})
    try:
        metrics = refresh(tracked_projects(catalog, stack, watchlist), old_metrics)
    except RuntimeError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    metric_errors = validate_metrics(catalog, stack, watchlist, metrics)
    if metric_errors:
        for error in metric_errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    dump_json(METRICS_PATH, metrics)
    if not args.no_history:
        update_history(metrics)
    history = load_json(HISTORY_PATH, {"schema_version": 1, "snapshots": []})
    write_generated_files(catalog, stack, watchlist, exclusions, metrics, history)
    print(f"updated {len(catalog['projects'])} core and {len(stack['projects'])} stack projects")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
