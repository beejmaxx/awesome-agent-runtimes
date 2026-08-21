# Awesome Agent Runtimes [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint disable table-cell-padding table-pipe-alignment-->

> A curated, comparable map of the software that actually **runs AI agents**:
> persistent agent operating systems, coding-agent harnesses, orchestration
> runtimes, serving layers, secure execution environments, and durable workflows.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Catalog entries](https://img.shields.io/badge/entries-47-5b5bd6.svg)
[![Metadata](https://img.shields.io/badge/metadata-2026-08-21-2ea44f.svg)](data/metrics.json)

This list is for engineers deciding **where an agent loop lives, how it keeps
state, and where its tools execute**. It deliberately does not try to catalog
every chatbot, model SDK, prompt library, or finished agent application.

Metadata was last refreshed on **2026-08-21**. Star counts are snapshots;
the daily workflow records their history in `data/history.json`.

**High signal, not exhaustive.** Established adoption is the default bar. A
smaller project is included only when it contributes a distinct runtime design
and has credible maintainership, documentation, and licensing. There are no paid
placements and stars never determine ordering.

## Contents

- [Runtime scope](#runtime-scope)
- [Quality bar](#quality-bar)
- [Choose a layer](#choose-a-layer)
- [Catalog](#catalog)
  - [Persistent agent runtimes](#persistent-agent-runtimes)
  - [Coding agent runtimes](#coding-agent-runtimes)
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

## Quality bar

Every entry must have a meaningful public implementation, identifiable
maintainers, usable documentation, and evidence that it owns part of runtime
execution. Projects are reviewed for scope, maintenance, license visibility, and
distinctiveness. See [`METHODOLOGY.md`](METHODOLOGY.md) for lifecycle rules,
metadata limitations, and the correction process.

## Choose a layer

| If you need to…                                               | Start with…                         |
| ------------------------------------------------------------- | ----------------------------------- |
| Run a persistent assistant or autonomous worker               | Persistent agent runtimes           |
| Run an agent against a software repository                    | Coding agent runtimes               |
| Embed agent control flow in an application                    | Agent and workflow runtimes         |
| Deploy, operate, and expose agents as a service               | Serving and control planes          |
| Execute untrusted code or browser tasks safely                | Sandboxes and execution environments |
| Survive retries, long waits, restarts, and human approval     | Durable execution substrates        |

Deployment labels are intentionally coarse: `local`, `self-hosted`, `managed`,
and `library`. Tags describe prominent runtime traits, not a complete feature
audit. An **Archived** marker comes directly from GitHub.

## Catalog

<!-- BEGIN GENERATED CATALOG -->
### Persistent agent runtimes

Complete environments for long-lived assistants and autonomous workers.

| Project                                                      | Stars     | Runtime fit                                                                                                                                                           | Stack            | Deploy               | Last push  |
| ------------------------------------------------------------ | --------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------- | ---------- |
| [Agent Zero](https://github.com/agent0ai/agent-zero)         | ⭐ 18,921  | General-purpose autonomous agent runtime with an interactive UI, subordinate agents, and executable tools. `multi-agent` `code-execution` `memory`                    | Python           | local, self-hosted   | 2026-08-19 |
| [AIOS](https://github.com/agiresearch/AIOS)                  | ⭐ 6,261   | Research agent operating-system kernel for scheduling LLM calls, memory, storage, and tools. `scheduler` `memory` `research`                                          | Python           | local, library       | 2026-07-20 |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)   | ⭐ 186,710 | Platform for creating, deploying, and continuously running autonomous agents. `continuous` `builder` `marketplace`                                                    | Python           | self-hosted, managed | 2026-08-21 |
| [ElizaOS](https://github.com/elizaOS/eliza)                  | ⭐ 19,113  | Agent operating system with persistent identities, multi-agent coordination, and a plugin ecosystem. `multi-agent` `plugins` `memory`                                 | TypeScript · MIT | local, self-hosted   | 2026-08-21 |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | ⭐ 233,848 | Persistent agent runtime with learned skills, cross-session memory, schedules, messaging gateways, and subagents. `self-improving` `skills` `scheduler` `multi-agent` | Python · MIT     | local, self-hosted   | 2026-08-21 |
| [Letta](https://github.com/letta-ai/letta)                   | ⭐ 24,331  | Stateful agent server centered on persistent memory, context management, and long-lived identities. `memory` `server` `stateful`                                      | Apache-2.0       | self-hosted, managed | 2026-08-16 |
| [OpenClaw](https://github.com/openclaw/openclaw)             | ⭐ 387,025 | Personal agent runtime with messaging channels, schedules, memory, skills, and tool execution. `personal-agent` `scheduler` `tools`                                   | TypeScript       | local, self-hosted   | 2026-08-21 |

### Coding agent runtimes

Agent harnesses that own the software-engineering loop, workspace, tools, and sessions.

| Project                                                                | Stars     | Runtime fit                                                                                                                                    | Stack                   | Deploy                      | Last push  |
| ---------------------------------------------------------------------- | --------: | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | --------------------------- | ---------- |
| [Aider](https://github.com/Aider-AI/aider)                             | ⭐ 48,382  | Terminal coding-agent runtime built around repository maps, editable worktrees, and Git-native sessions. `coding` `terminal` `git`             | Python · Apache-2.0     | local                       | 2026-05-22 |
| [Cline](https://github.com/cline/cline)                                | ⭐ 66,598  | Autonomous coding-agent runtime available as an IDE extension, CLI, and embeddable SDK. `coding` `IDE` `human-in-the-loop`                     | TypeScript · Apache-2.0 | local, library              | 2026-08-21 |
| [Codex](https://github.com/openai/codex)                               | ⭐ 110,805 | Local coding-agent runtime and CLI with sandboxed command execution, approvals, and automation modes. `coding` `sandbox` `terminal`            | Rust · Apache-2.0       | local                       | 2026-08-21 |
| [Crush](https://github.com/charmbracelet/crush)                        | ⭐ 27,554  | Terminal coding-agent runtime with multi-model support, language-server integration, and extensible tools. `coding` `terminal` `LSP`           | Go                      | local                       | 2026-08-21 |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli)              | ⭐ 106,598 | Terminal agent runtime for coding and general automation with tools, extensions, and MCP support. `coding` `terminal` `MCP`                    | TypeScript · Apache-2.0 | local                       | 2026-08-21 |
| [Goose](https://github.com/aaif-goose/goose)                           | ⭐ 53,151  | Local extensible agent runtime that automates engineering tasks through MCP tools. `coding` `MCP` `desktop`                                    | Rust · Apache-2.0       | local                       | 2026-08-21 |
| [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | ⭐ 68,097  | Local coding-agent runtime for open models with computer tools and executable workflows. `coding` `computer-use` `local-models`                | Rust · Apache-2.0       | local                       | 2026-08-20 |
| [OpenCode](https://github.com/anomalyco/opencode)                      | ⭐ 199,829 | Open-source coding-agent runtime for terminal, desktop, and IDE clients with parallel sessions. `coding` `client-server` `multi-session`       | TypeScript · MIT        | local, self-hosted          | 2026-08-21 |
| [OpenHands](https://github.com/OpenHands/OpenHands)                    | ⭐ 84,702  | Software-development agent platform with a runtime for executing tools in isolated workspaces. `coding` `sandbox` `multi-agent`                | TypeScript · MIT        | local, self-hosted, managed | 2026-08-21 |
| [Pi](https://github.com/earendil-works/pi)                             | ⭐ 94,928  | Extensible coding-agent toolkit and CLI with persistent sessions, a unified model API, and UI libraries. `coding` `extensible` `sessions`      | TypeScript · MIT        | local, library              | 2026-08-21 |
| [Roo Code](https://github.com/RooCodeInc/Roo-Code) **Archived**        | ⭐ 24,329  | IDE coding-agent runtime with specialized modes, tool use, and multi-agent orchestration. `coding` `IDE` `multi-agent`                         | TypeScript · Apache-2.0 | local                       | 2026-05-15 |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent)                    | ⭐ 20,095  | Research-backed software-engineering agent runtime for resolving repository issues in controlled environments. `coding` `research` `benchmark` | Python · MIT            | local, self-hosted          | 2026-08-17 |

### Agent and workflow runtimes

Libraries and kernels that own the agent loop, state transitions, or multi-agent coordination.

| Project                                                                   | Stars    | Runtime fit                                                                                                                              | Stack               | Deploy                        | Last push  |
| ------------------------------------------------------------------------- | -------: | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------------- | ---------- |
| [AgentScope](https://github.com/agentscope-ai/agentscope)                 | ⭐ 29,150 | Developer framework for tool-using and multi-agent applications with runtime services. `multi-agent` `tools` `distributed`               | Python · Apache-2.0 | library, self-hosted          | 2026-08-21 |
| [Agno](https://github.com/agno-agi/agno)                                  | ⭐ 41,822 | Python framework and AgentOS runtime for building, serving, and monitoring agent systems. `multi-agent` `memory` `observability`         | Python · Apache-2.0 | library, self-hosted, managed | 2026-08-21 |
| [AutoGen](https://github.com/microsoft/autogen)                           | ⭐ 60,559 | Event-driven framework for conversational, tool-using, and multi-agent applications. `multi-agent` `event-driven` `tools`                | Python · CC-BY-4.0  | library, self-hosted          | 2026-04-15 |
| [CAMEL](https://github.com/camel-ai/camel)                                | ⭐ 17,614 | Multi-agent framework and research platform for agent societies, tools, memory, and task execution. `multi-agent` `research` `memory`    | Python · Apache-2.0 | library, self-hosted          | 2026-08-21 |
| [CrewAI](https://github.com/crewAIInc/crewAI)                             | ⭐ 57,425 | Role-based multi-agent runtime for coordinating crews and event-driven flows. `multi-agent` `flows` `observability`                      | Python · MIT        | library, self-hosted, managed | 2026-08-21 |
| [Dapr Agents](https://github.com/dapr/dapr-agents)                        | ⭐ 740    | Agent framework built on Dapr actors and durable workflows for resilient distributed execution. `durable` `actors` `distributed`         | Python · Apache-2.0 | library, self-hosted          | 2026-08-17 |
| [Google Agent Development Kit](https://github.com/google/adk-python)      | ⭐ 21,216 | Code-first agent framework with sessions, tools, evaluation, and local or managed runtime options. `multi-agent` `evaluation` `tools`    | Python · Apache-2.0 | library, local, managed       | 2026-08-21 |
| [LangGraph](https://github.com/langchain-ai/langgraph)                    | ⭐ 40,175 | Graph-based runtime for stateful, durable, and human-in-the-loop agent workflows. `durable` `human-in-the-loop` `graph`                  | Python · MIT        | library, self-hosted, managed | 2026-08-20 |
| [Mastra](https://github.com/mastra-ai/mastra)                             | ⭐ 27,351 | TypeScript agent framework with workflows, memory, evaluation, and observability. `workflows` `memory` `observability`                   | TypeScript          | library, self-hosted, managed | 2026-08-21 |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | ⭐ 13,024 | Microsoft framework for building agents and graph workflows with middleware and state management. `workflows` `multi-agent` `middleware` | Python · MIT        | library, self-hosted, managed | 2026-08-21 |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python)       | ⭐ 28,830 | Lightweight Python runtime for agent loops, handoffs, guardrails, sessions, and tracing. `handoffs` `guardrails` `tracing`               | Python · MIT        | library                       | 2026-08-21 |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai)                    | ⭐ 19,430 | Typed Python agent framework with tools, durable execution integrations, graphs, and evaluation. `typed` `durable` `evaluation`          | Python · MIT        | library, self-hosted          | 2026-08-21 |

### Serving and control planes

Systems for packaging, deploying, exposing, and operating agent workloads.

| Project                                                      | Stars     | Runtime fit                                                                                                                                  | Stack            | Deploy                      | Last push  |
| ------------------------------------------------------------ | --------: | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------------------------- | ---------- |
| [Dify](https://github.com/langgenius/dify)                   | ⭐ 153,122 | Visual platform for building and operating agentic applications, workflows, and model services. `low-code` `workflows` `observability`       | TypeScript       | self-hosted, managed        | 2026-08-21 |
| [Docker Agent](https://github.com/docker/docker-agent)       | ⭐ 3,279   | Declarative runtime and CLI for packaging and running agents with models, MCP tools, and subagents. `containers` `MCP` `multi-agent`         | Go · Apache-2.0  | local, self-hosted          | 2026-08-21 |
| [Flowise](https://github.com/FlowiseAI/Flowise) **Archived** | ⭐ 55,383  | Visual builder and serving platform for agent flows, assistants, and tool integrations. `low-code` `builder` `tools`                         | TypeScript       | self-hosted, managed        | 2026-08-13 |
| [Langflow](https://github.com/langflow-ai/langflow)          | ⭐ 153,529 | Visual Python framework for composing and serving agent workflows with an API. `low-code` `builder` `API`                                    | Python · MIT     | local, self-hosted, managed | 2026-08-21 |
| [LlamaDeploy](https://github.com/run-llama/llama_deploy)     | ⭐ 2,068   | Deployment system for running agent workflows as scalable, event-driven services. `event-driven` `services` `scaling`                        | Python · MIT     | self-hosted                 | 2026-04-06 |
| [T3 Code](https://github.com/pingdotgg/t3code)               | ⭐ 19,894  | Local control plane for operating existing coding-agent CLIs from web, desktop, and mobile clients. `control-plane` `coding` `remote-access` | TypeScript · MIT | local, self-hosted          | 2026-08-21 |

### Sandboxes and execution environments

Isolated environments in which agents can safely run code, commands, and tools.

| Project                                                         | Stars    | Runtime fit                                                                                                                      | Stack               | Deploy               | Last push  |
| --------------------------------------------------------------- | -------: | -------------------------------------------------------------------------------------------------------------------------------- | ------------------- | -------------------- | ---------- |
| [Daytona](https://github.com/daytonaio/daytona)                 | ⭐ 71,932 | Secure infrastructure for programmatically creating and managing agent execution sandboxes. `sandbox` `code-execution` `API`     | —                   | self-hosted, managed | 2026-07-24 |
| [E2B](https://github.com/e2b-dev/E2B)                           | ⭐ 13,506 | Open-source infrastructure for running agent-generated code in isolated cloud sandboxes. `sandbox` `code-execution` `API`        | Python · Apache-2.0 | self-hosted, managed | 2026-08-21 |
| [Microsandbox](https://github.com/superradcompany/microsandbox) | ⭐ 7,841  | Self-hosted microVM platform for secure, fast, and isolated user or agent code execution. `microVM` `isolation` `code-execution` | Rust · Apache-2.0   | local, self-hosted   | 2026-08-21 |
| [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell)         | ⭐ 8,302  | Policy-governed runtime for running autonomous agents inside private sandboxes. `sandbox` `policy` `privacy`                     | Rust · Apache-2.0   | local, self-hosted   | 2026-08-21 |
| [SandboxFusion](https://github.com/bytedance/SandboxFusion)     | ⭐ 1,059  | Execution service for isolated code evaluation across many programming languages. `sandbox` `code-execution` `multi-language`    | Python · Apache-2.0 | self-hosted          | 2026-07-14 |

### Durable execution substrates

Agent-adjacent workflow engines used for retries, resumability, schedules, and long-running work.

| Project                                                     | Stars    | Runtime fit                                                                                                                                    | Stack                   | Deploy                        | Last push  |
| ----------------------------------------------------------- | -------: | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ----------------------------- | ---------- |
| [DBOS](https://github.com/dbos-inc/dbos-transact-py)        | ⭐ 1,539  | Python durable-execution library for workflows that recover state and resume after failures. `durable` `workflows` `recovery`                  | Python · MIT            | library, self-hosted, managed | 2026-08-20 |
| [Hatchet](https://github.com/hatchet-dev/hatchet)           | ⭐ 7,772  | Task orchestration platform for durable workflows, queues, retries, concurrency, and monitoring. `durable` `workflows` `observability`         | Go · MIT                | self-hosted, managed          | 2026-08-21 |
| [Inngest](https://github.com/inngest/inngest)               | ⭐ 5,752  | Event-driven durable execution platform for step functions, scheduling, retries, and agent workflows. `durable` `event-driven` `workflows`     | Go                      | self-hosted, managed          | 2026-08-21 |
| [Temporal](https://github.com/temporalio/temporal)          | ⭐ 22,438 | General durable-execution platform commonly used to make long-running agent workflows resilient. `durable` `workflows` `recovery`              | Go · MIT                | self-hosted, managed          | 2026-08-21 |
| [Trigger.dev](https://github.com/triggerdotdev/trigger.dev) | ⭐ 16,084 | TypeScript background-job platform for long-running AI tasks with retries, queues, and monitoring. `durable` `background-jobs` `observability` | TypeScript · Apache-2.0 | self-hosted, managed          | 2026-08-21 |
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
