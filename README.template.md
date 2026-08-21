# Awesome Agent Runtimes [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint disable table-cell-padding table-pipe-alignment-->

> A curated, comparable map of the software that actually **runs AI agents**:
> persistent agent operating systems, orchestration runtimes, serving layers,
> secure execution environments, and durable workflow substrates.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Catalog entries](https://img.shields.io/badge/entries-{{PROJECT_COUNT}}-5b5bd6.svg)
[![Metadata](https://img.shields.io/badge/metadata-{{UPDATED_AT}}-2ea44f.svg)](data/metrics.json)

This list is for engineers deciding **where an agent loop lives, how it keeps
state, and where its tools execute**. It deliberately does not try to catalog
every chatbot, model SDK, prompt library, or finished agent application.

Metadata was last refreshed on **{{UPDATED_AT}}**. Star counts are snapshots;
the daily workflow records their history in [`data/history.json`](data/history.json).

## Contents

- [Runtime scope](#runtime-scope)
- [Choose a layer](#choose-a-layer)
- [Catalog](#catalog)
  - [Persistent agent runtimes](#persistent-agent-runtimes)
  - [Agent and workflow runtimes](#agent-and-workflow-runtimes)
  - [Serving and control planes](#serving-and-control-planes)
  - [Sandboxes and execution environments](#sandboxes-and-execution-environments)
  - [Durable execution substrates](#durable-execution-substrates)
- [Tracking and data](#tracking-and-data)
- [Related lists](#related-lists)

## Runtime scope

An entry must own at least one part of agent execution: the agent loop,
scheduling and resumption, persistent state, multi-agent coordination,
deployment and serving, or isolated tool/code execution. Generic infrastructure
is included only when it is directly useful as an agent execution substrate.

The list separates layers because they are complementary, not interchangeable.
For example, an orchestration library can run inside a serving platform while
delegating code execution to a sandbox and durable waits to a workflow engine.

## Choose a layer

| If you need to…                                               | Start with…                         |
| ------------------------------------------------------------- | ----------------------------------- |
| Run a persistent assistant or autonomous worker               | Persistent agent runtimes           |
| Embed agent control flow in an application                    | Agent and workflow runtimes         |
| Deploy, operate, and expose agents as a service               | Serving and control planes          |
| Execute untrusted code or browser tasks safely                | Sandboxes and execution environments |
| Survive retries, long waits, restarts, and human approval     | Durable execution substrates        |

Deployment labels are intentionally coarse: `local`, `self-hosted`, `managed`,
and `library`. Tags describe prominent runtime traits, not a complete feature
audit. An **Archived** marker comes directly from GitHub.

## Catalog

<!-- BEGIN GENERATED CATALOG -->
{{CATALOG}}
<!-- END GENERATED CATALOG -->

## Tracking and data

The catalog has one source of truth: [`data/projects.json`](data/projects.json).
[`scripts/update.py`](scripts/update.py) validates every entry, retrieves public
repository metadata from the GitHub API, renders this README, and stores one star
snapshot per UTC day. No third-party Python packages are required.

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
based on runtime relevance, public evidence, maintenance, and a clear license—not
star count or sponsorship.
