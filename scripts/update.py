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
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PROJECTS_PATH = ROOT / "data" / "projects.json"
METRICS_PATH = ROOT / "data" / "metrics.json"
HISTORY_PATH = ROOT / "data" / "history.json"
CATALOG_PATH = ROOT / "data" / "catalog.json"
CSV_PATH = ROOT / "data" / "catalog.csv"
LLMS_PATH = ROOT / "llms.txt"
TAGS_PATH = ROOT / "TAGS.md"
TEMPLATE_PATH = ROOT / "README.template.md"
README_PATH = ROOT / "README.md"
REPO_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
ALLOWED_DEPLOYMENTS = {"library", "local", "self-hosted", "managed"}
MINIMUM_STARS = 5000


def load_json(path: Path, default: Any = None) -> Any:
    if not path.exists() and default is not None:
        return default
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def dump_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


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


def validate_metrics(catalog: dict[str, Any], metrics: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    metadata = metrics.get("repositories", {})
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
    return errors


def refresh(catalog: dict[str, Any], old_metrics: dict[str, Any]) -> dict[str, Any]:
    token = os.environ.get("GITHUB_TOKEN")
    old_by_repo = old_metrics.get("repositories", {})
    repositories: dict[str, Any] = {}
    failures: list[str] = []
    for project in catalog["projects"]:
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
    missing = [project["repo"] for project in catalog["projects"] if project["repo"] not in repositories]
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


def render_catalog(catalog: dict[str, Any], metrics: dict[str, Any]) -> str:
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
            license_name = item.get("license")
            if license_name == "NOASSERTION":
                license_name = None
            stack_parts = [part for part in (item.get("language"), license_name) if part]
            stack = " · ".join(stack_parts) or "—"
            fit = f"{project['description']} `{'` `'.join(project['tags'])}`"
            deploy = ", ".join(project["deployment"])
            activity = item.get("pushed_at", "")[:10] or "—"
            rows.append([project_name, star_text, escape_cell(fit), escape_cell(stack), escape_cell(deploy), activity])
        sections.extend(markdown_table(["Project", "Stars", "Runtime fit", "Stack", "Deploy", "Last push"], rows, {1}))
        sections.append("")
    return "\n".join(sections).rstrip()


def render_readme(catalog: dict[str, Any], metrics: dict[str, Any]) -> str:
    fetched_at = metrics.get("fetched_at", "unavailable")
    updated = fetched_at[:10] if fetched_at != "unavailable" else fetched_at
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    return (
        template.replace("{{PROJECT_COUNT}}", str(len(catalog["projects"])))
        .replace("{{UPDATED_AT}}", updated)
        .replace("{{CATALOG}}", render_catalog(catalog, metrics))
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
                "github": {
                    key: item.get(key)
                    for key in (
                        "stars",
                        "forks",
                        "open_issues",
                        "language",
                        "license",
                        "archived",
                        "created_at",
                        "pushed_at",
                        "homepage",
                        "default_branch",
                    )
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
                "stars": item.get("stars", ""),
                "forks": item.get("forks", ""),
                "language": item.get("language") or "",
                "license": item.get("license") or "",
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
        "A curated map of software that owns AI-agent execution, state, serving, or isolation.",
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
            lines.append(f"- [{project['name']}](https://github.com/{project['repo']}) - {project['description']}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def generated_files(catalog: dict[str, Any], metrics: dict[str, Any]) -> dict[Path, str]:
    return {
        README_PATH: render_readme(catalog, metrics),
        CATALOG_PATH: json.dumps(merged_catalog(catalog, metrics), indent=2, ensure_ascii=False) + "\n",
        CSV_PATH: render_csv(catalog, metrics),
        LLMS_PATH: render_llms(catalog, metrics),
        TAGS_PATH: render_tags(catalog),
    }


def write_generated_files(catalog: dict[str, Any], metrics: dict[str, Any]) -> None:
    for path, content in generated_files(catalog, metrics).items():
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
    errors = validate(catalog)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    if args.check:
        metrics = load_json(METRICS_PATH)
        metric_errors = validate_metrics(catalog, metrics)
        if metric_errors:
            for error in metric_errors:
                print(f"error: {error}", file=sys.stderr)
            return 1
        stale = [
            str(path.relative_to(ROOT))
            for path, expected in generated_files(catalog, metrics).items()
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
        write_generated_files(catalog, metrics)
        print(f"rendered {len(catalog['projects'])} projects")
        return 0

    old_metrics = load_json(METRICS_PATH, {"repositories": {}})
    try:
        metrics = refresh(catalog, old_metrics)
    except RuntimeError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    metric_errors = validate_metrics(catalog, metrics)
    if metric_errors:
        for error in metric_errors:
            print(f"error: {error}", file=sys.stderr)
        return 1
    dump_json(METRICS_PATH, metrics)
    if not args.no_history:
        update_history(metrics)
    write_generated_files(catalog, metrics)
    print(f"updated {len(catalog['projects'])} projects")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
