# Awesome Agent Runtimes [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint disable table-cell-padding table-pipe-alignment-->

> A curated, comparable map of the software that **owns part of agent execution**—
> from cognition and supervision to continuity, isolation, and durable recovery.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Catalog entries](https://img.shields.io/badge/entries-{{PROJECT_COUNT}}-5b5bd6.svg)
[![Metadata](https://img.shields.io/badge/metadata-{{UPDATED_AT}}-2ea44f.svg)](data/metrics.json)

This list is for engineers deciding **who owns the intelligence and who owns
operational truth** when an agent acts. It deliberately does not treat every
framework, host, workflow engine, sandbox, and memory system as the same kind
of "agent runtime."

Metadata was last refreshed on **{{UPDATED_AT}}**. Star counts are snapshots;
the daily workflow records their history in `data/history.json`.

**High signal, not exhaustive.** The core catalog enforces a 5,000-star adoption
floor in addition to age, activity, documentation, licensing, and scope review.
Crossing the floor makes a project eligible, not automatically included. There
are no paid placements and stars never determine ordering.

## Contents

- [Runtime scope](#runtime-scope)
- [Ownership boundaries](#ownership-boundaries)
- [Quality bar](#quality-bar)
- [Choose a layer](#choose-a-layer)
- [Catalog](#catalog)
  - [Agent cognition — coding harnesses](#agent-cognition--coding-harnesses)
  - [Agent cognition — construction SDKs](#agent-cognition--construction-sdks)
  - [Agent cognition — browser and computer use](#agent-cognition--browser-and-computer-use)
  - [Agent hosts and supervisors](#agent-hosts-and-supervisors)
  - [Durable orchestration](#durable-orchestration)
  - [Personal agent OSes and continuity](#personal-agent-oses-and-continuity)
  - [Execution and isolation](#execution-and-isolation)
  - [Application platforms and infrastructure](#application-platforms-and-infrastructure)
- [Tracking and data](#tracking-and-data)
- [Related lists](#related-lists)

## Runtime scope

An entry must own at least one consequential part of agent execution: cognition,
supervision, scheduling and recovery, long-lived continuity, deployment, or
isolated tool and code execution. Generic infrastructure is included only when
it materially changes how agents run.

The list separates layers because they are complementary, not interchangeable.
For example, a coding harness can run inside an agent host, delegate commands to
a sandbox, and rely on a workflow engine for durable waits.

## Ownership boundaries

| Layer | Owns | Does not automatically own |
| --- | --- | --- |
| Agent cognition | Model/tool loop, planning, context assembly | Process recovery or durable work truth |
| Agent host and supervisor | Agent lifecycle, identity, environment, event stream, reconnect | The agent's reasoning strategy |
| Durable orchestration | Checkpoints, retries, timers, recovery, reconciliation | Agent semantics or execution isolation |
| Execution and isolation | Processes, containers, browsers, microVMs, resource limits | Approval policy or user intent |
| Authority and safety | Credentials, capabilities, approvals, effect policy | The sandbox implementation |
| Work state and continuity | Projects, tasks, artifacts, decisions, context across agents | Merely storing chat history or embeddings |
| Supporting infrastructure | Protocols, gateways, observability, deployment | Ownership of the end-to-end agent experience |

The last distinction matters: **memory is not the same as durable project
state**. A transcript or vector store can help an agent recall information
without owning tasks, artifacts, decisions, outcomes, or reconciliation. The
broader [architecture map](STACK.md#the-host-and-work-state-gaps) keeps this boundary visible
even where no project yet clears the core catalog's maturity bar.

## Quality bar

Every entry must have a meaningful public implementation, identifiable
maintainers, usable documentation, and evidence that it owns part of runtime
execution. Projects are reviewed for scope, maintenance, license visibility, and
distinctiveness. See [`METHODOLOGY.md`](METHODOLOGY.md) for lifecycle rules,
metadata limitations, and the correction process.

## Choose a layer

| If you need to…                                           | Start with…                                  |
| --------------------------------------------------------- | -------------------------------------------- |
| Give an agent a coding or general reasoning loop          | Agent cognition                              |
| Start, reconnect to, and supervise heterogeneous agents   | Agent hosts and supervisors                  |
| Survive retries, long waits, restarts, and unknown states | Durable orchestration                        |
| Run a long-lived personal assistant across interactions   | Personal agent OSes and continuity           |
| Execute agent-controlled code or browser tasks safely     | Execution and isolation                      |
| Build and operate complete agent applications             | Application platforms and infrastructure     |
| Preserve tasks, artifacts, and decisions across agents    | [Work state and continuity](STACK.md#layer-map)      |

Deployment labels are intentionally coarse: `local`, `self-hosted`, `managed`,
and `library`. Tags describe prominent runtime traits, not a complete feature
audit. An **Archived** marker comes directly from GitHub.

## Catalog

<!-- BEGIN GENERATED CATALOG -->
{{CATALOG}}
<!-- END GENERATED CATALOG -->

## Tracking and data

The catalog has one editorial source of truth:
[`data/projects.json`](data/projects.json). [`scripts/update.py`](scripts/update.py)
validates every entry, retrieves public repository metadata from the GitHub API,
renders the human and machine views, and stores one star snapshot per UTC day.
No third-party Python packages are required.

| Artifact | Purpose |
| --- | --- |
| [`data/catalog.json`](data/catalog.json) | Curated fields joined with current GitHub metadata |
| [`data/catalog.csv`](data/catalog.csv) | Spreadsheet-ready flat export |
| [`llms.txt`](llms.txt) | Compact agent-readable catalog |
| [`TAGS.md`](TAGS.md) | Generated capability index |
| [`data/history.json`](data/history.json) | Daily star history for trend analysis |
| [`data/schema.json`](data/schema.json) | Source catalog JSON Schema |

Coverage is audited against the trusted upstream lists in
[`data/sources.json`](data/sources.json). The reproducible funnel and unreviewed
candidate queue are documented in [`DISCOVERY.md`](DISCOVERY.md). Production
layers that matter but are not themselves core entries—including protocols,
authority, observability, and work-state primitives—are mapped separately in
[`STACK.md`](STACK.md).

```bash
# Validate the catalog and generated files without using the network
python3 scripts/update.py --check

# Render after editorial changes while keeping the current metadata snapshot
python3 scripts/update.py --render-only

# Refresh GitHub metadata, README, and today's history snapshot
GITHUB_TOKEN=... python3 scripts/update.py
```

The scheduled workflow performs the refresh daily. Forks can run it without a
token locally, subject to GitHub's lower anonymous API rate limit.

## Related lists

- [Awesome AI Agent Runtimes](https://github.com/pandastack-io/awesome-ai-agent-runtimes) - The closest existing list, focused mainly on sandboxes and execution environments.
- [Awesome Agent Frameworks](https://github.com/alexbevi/awesome-agent-frameworks) - A broader directory spanning frameworks and supporting tools.
- [Awesome Agents](https://github.com/kyrolabs/awesome-agents) - Agents, products, frameworks, and application categories.
- [Awesome AI Agents](https://github.com/e2b-dev/awesome-ai-agents) - A broad collection of autonomous-agent projects.

## Contributing

Additions, corrections, and taxonomy debates are welcome. Read
[`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request. Inclusion is
based on runtime relevance, public evidence, maintenance, licensing, and the
published adoption floor—not sponsorship.
