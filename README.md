# Awesome Agent Runtimes [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint disable table-cell-padding table-pipe-alignment-->

> A curated, comparable map of the software that **owns part of agent execution**—
> from cognition and supervision to continuity, isolation, and durable recovery.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Catalog entries](https://img.shields.io/badge/entries-59-5b5bd6.svg)
[![Metadata](https://img.shields.io/badge/metadata-2026-08-21-2ea44f.svg)](data/metrics.json)

This list is for engineers deciding **who owns the intelligence and who owns
operational truth** when an agent acts. It deliberately does not treat every
framework, host, workflow engine, sandbox, and memory system as the same kind
of "agent runtime."

Metadata was last refreshed on **2026-08-21**. Star counts are snapshots;
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
### Agent cognition — coding harnesses

Agent brains that own the software-engineering loop, repository context, tools, and coding sessions.

| Project                                                                | Stars     | Runtime fit                                                                                                                                    | Stack                   | Deploy             | Last push  |
| ---------------------------------------------------------------------- | --------: | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------ | ---------- |
| [Aider](https://github.com/Aider-AI/aider)                             | ⭐ 48,385  | Terminal coding-agent runtime built around repository maps, editable worktrees, and Git-native sessions. `coding` `terminal` `git`             | Python · Apache-2.0     | local              | 2026-05-22 |
| [Cline](https://github.com/cline/cline)                                | ⭐ 66,604  | Autonomous coding-agent runtime available as an IDE extension, CLI, and embeddable SDK. `coding` `IDE` `human-in-the-loop`                     | TypeScript · Apache-2.0 | local, library     | 2026-08-21 |
| [Codex](https://github.com/openai/codex)                               | ⭐ 110,979 | Local coding-agent runtime and CLI with sandboxed command execution, approvals, and automation modes. `coding` `sandbox` `terminal`            | Rust · Apache-2.0       | local              | 2026-08-21 |
| [Continue](https://github.com/continuedev/continue)                    | ⭐ 35,575  | Open-source coding-agent runtime spanning IDE, CLI, and continuous repository automation. `coding` `IDE` `automation`                          | TypeScript · Apache-2.0 | local, self-hosted | 2026-08-20 |
| [Crush](https://github.com/charmbracelet/crush)                        | ⭐ 27,558  | Terminal coding-agent runtime with multi-model support, language-server integration, and extensible tools. `coding` `terminal` `LSP`           | Go                      | local              | 2026-08-21 |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli)              | ⭐ 106,598 | Terminal agent runtime for coding and general automation with tools, extensions, and MCP support. `coding` `terminal` `MCP`                    | TypeScript · Apache-2.0 | local              | 2026-08-21 |
| [Goose](https://github.com/aaif-goose/goose)                           | ⭐ 53,166  | Local extensible agent runtime that automates engineering tasks through MCP tools. `coding` `MCP` `desktop`                                    | Rust · Apache-2.0       | local              | 2026-08-21 |
| [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | ⭐ 68,096  | Local coding-agent runtime for open models with computer tools and executable workflows. `coding` `computer-use` `local-models`                | Rust · Apache-2.0       | local              | 2026-08-20 |
| [OpenCode](https://github.com/anomalyco/opencode)                      | ⭐ 199,867 | Open-source coding-agent runtime for terminal, desktop, and IDE clients with parallel sessions. `coding` `client-server` `multi-session`       | TypeScript · MIT        | local, self-hosted | 2026-08-21 |
| [Pi](https://github.com/earendil-works/pi)                             | ⭐ 94,961  | Extensible coding-agent toolkit and CLI with persistent sessions, a unified model API, and UI libraries. `coding` `extensible` `sessions`      | TypeScript · MIT        | local, library     | 2026-08-21 |
| [Qwen Code](https://github.com/QwenLM/qwen-code)                       | ⭐ 27,261  | Open-source terminal coding-agent runtime with tools, extensibility, and model-provider support. `coding` `terminal` `tools`                   | TypeScript · Apache-2.0 | local              | 2026-08-21 |
| [Roo Code](https://github.com/RooCodeInc/Roo-Code) **Archived**        | ⭐ 24,329  | IDE coding-agent runtime with specialized modes, tool use, and multi-agent orchestration. `coding` `IDE` `multi-agent`                         | TypeScript · Apache-2.0 | local              | 2026-05-15 |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent)                    | ⭐ 20,096  | Research-backed software-engineering agent runtime for resolving repository issues in controlled environments. `coding` `research` `benchmark` | Python · MIT            | local, self-hosted | 2026-08-17 |

### Agent cognition — construction SDKs

Libraries for constructing model/tool loops, routing, state transitions, and multi-agent behavior.

| Project                                                                   | Stars     | Runtime fit                                                                                                                                  | Stack               | Deploy                        | Last push  |
| ------------------------------------------------------------------------- | --------: | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------------- | ---------- |
| [AgentScope](https://github.com/agentscope-ai/agentscope)                 | ⭐ 29,162  | Developer framework for tool-using and multi-agent applications with runtime services. `multi-agent` `tools` `distributed`                   | Python · Apache-2.0 | library, self-hosted          | 2026-08-21 |
| [Agno](https://github.com/agno-agi/agno)                                  | ⭐ 41,824  | Python framework and AgentOS runtime for building, serving, and monitoring agent systems. `multi-agent` `memory` `observability`             | Python · Apache-2.0 | library, self-hosted, managed | 2026-08-21 |
| [AutoGen](https://github.com/microsoft/autogen)                           | ⭐ 60,560  | Event-driven framework for conversational, tool-using, and multi-agent applications. `multi-agent` `event-driven` `tools`                    | Python · CC-BY-4.0  | library, self-hosted          | 2026-04-15 |
| [CAMEL](https://github.com/camel-ai/camel)                                | ⭐ 17,615  | Multi-agent framework and research platform for agent societies, tools, memory, and task execution. `multi-agent` `research` `memory`        | Python · Apache-2.0 | library, self-hosted          | 2026-08-21 |
| [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python) | ⭐ 7,949   | Anthropic's Python SDK for building agents with Claude Code's tools, sessions, and execution loop. `tools` `sessions` `SDK`                  | Python · MIT        | library, self-hosted          | 2026-08-20 |
| [CrewAI](https://github.com/crewAIInc/crewAI)                             | ⭐ 57,428  | Role-based multi-agent runtime for coordinating crews and event-driven flows. `multi-agent` `flows` `observability`                          | Python · MIT        | library, self-hosted, managed | 2026-08-21 |
| [Deep Agents](https://github.com/langchain-ai/deepagents)                 | ⭐ 28,040  | Batteries-included agent harness with planning, filesystems, subagents, and long-term memory. `planning` `multi-agent` `memory`              | Python · MIT        | library, self-hosted          | 2026-08-21 |
| [Google Agent Development Kit](https://github.com/google/adk-python)      | ⭐ 21,216  | Code-first agent framework with sessions, tools, evaluation, and local or managed runtime options. `multi-agent` `evaluation` `tools`        | Python · Apache-2.0 | library, local, managed       | 2026-08-21 |
| [LangChain](https://github.com/langchain-ai/langchain)                    | ⭐ 144,724 | Established agent application framework with model, tool, middleware, and agent-loop abstractions. `tools` `middleware` `ecosystem`          | Python · MIT        | library, self-hosted          | 2026-08-21 |
| [LlamaIndex](https://github.com/run-llama/llama_index)                    | ⭐ 51,790  | Data-centric agent framework with workflows, tools, retrieval, memory, and multi-agent patterns. `data` `workflows` `retrieval`              | Python · MIT        | library, self-hosted, managed | 2026-08-20 |
| [Mastra](https://github.com/mastra-ai/mastra)                             | ⭐ 27,352  | TypeScript agent framework with workflows, memory, evaluation, and observability. `workflows` `memory` `observability`                       | TypeScript          | library, self-hosted, managed | 2026-08-21 |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT)                    | ⭐ 69,935  | Multi-agent software-company framework that coordinates role-based agents through structured workflows. `multi-agent` `roles` `workflows`    | Python · MIT        | library, local                | 2026-01-21 |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | ⭐ 13,026  | Microsoft framework for building agents and graph workflows with middleware and state management. `workflows` `multi-agent` `middleware`     | Python · MIT        | library, self-hosted, managed | 2026-08-21 |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python)       | ⭐ 28,834  | Lightweight Python runtime for agent loops, handoffs, guardrails, sessions, and tracing. `handoffs` `guardrails` `tracing`                   | Python · MIT        | library                       | 2026-08-21 |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai)                    | ⭐ 19,433  | Typed Python agent framework with tools, durable execution integrations, graphs, and evaluation. `typed` `durable` `evaluation`              | Python · MIT        | library, self-hosted          | 2026-08-21 |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel)           | ⭐ 28,477  | Microsoft agent SDK with plugins, process orchestration, memory integrations, and multi-agent patterns. `plugins` `multi-agent` `enterprise` | C# · MIT            | library, self-hosted, managed | 2026-08-21 |
| [smolagents](https://github.com/huggingface/smolagents)                   | ⭐ 28,917  | Compact Hugging Face agent library centered on code-executing agents and composable tools. `code-agents` `tools` `lightweight`               | Python · Apache-2.0 | library, local                | 2026-07-21 |

### Agent cognition — browser and computer use

Harnesses and SDKs that own perception and action loops over browsers or desktop interfaces.

| Project                                                   | Stars     | Runtime fit                                                                                                                                 | Stack             | Deploy                        | Last push  |
| --------------------------------------------------------- | --------: | ------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------------------- | ---------- |
| [Browser Use](https://github.com/browser-use/browser-use) | ⭐ 109,993 | Browser-agent framework and runtime for perception, action, sessions, and web task automation. `browser` `automation` `tools`               | Python · MIT      | library, local, managed       | 2026-08-21 |
| [Skyvern](https://github.com/Skyvern-AI/skyvern)          | ⭐ 22,817  | Browser workflow runtime using visual and language-model reasoning instead of site-specific selectors. `browser` `workflows` `computer-use` | Python · AGPL-3.0 | self-hosted, managed          | 2026-08-21 |
| [Stagehand](https://github.com/browserbase/stagehand)     | ⭐ 24,014  | Browser-agent SDK that combines natural-language actions with deterministic browser automation. `browser` `automation` `SDK`                | TypeScript · MIT  | library, self-hosted, managed | 2026-08-21 |
| [UFO](https://github.com/microsoft/UFO)                   | ⭐ 9,533   | Microsoft agent framework for automating Windows applications and multi-device desktop workflows. `computer-use` `desktop` `multi-agent`    | Python · MIT      | local                         | 2026-08-10 |

### Agent hosts and supervisors

Systems that start agents, provide environments and identity, stream events, supervise sessions, and recover failures.

| Project                                                    | Stars     | Runtime fit                                                                                                                                        | Stack            | Deploy                      | Last push  |
| ---------------------------------------------------------- | --------: | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------------------------- | ---------- |
| [Agent Zero](https://github.com/agent0ai/agent-zero)       | ⭐ 18,922  | General-purpose autonomous agent runtime with an interactive UI, subordinate agents, and executable tools. `multi-agent` `code-execution` `memory` | Python           | local, self-hosted          | 2026-08-19 |
| [AIOS](https://github.com/agiresearch/AIOS)                | ⭐ 6,261   | Research agent operating-system kernel for scheduling LLM calls, memory, storage, and tools. `scheduler` `memory` `research`                       | Python           | local, library              | 2026-07-20 |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | ⭐ 186,714 | Platform for creating, deploying, and continuously running autonomous agents. `continuous` `builder` `marketplace`                                 | Python           | self-hosted, managed        | 2026-08-21 |
| [Cloudflare Agents](https://github.com/cloudflare/agents)  | ⭐ 5,471   | Stateful agent SDK built on Durable Objects with identity, persistence, scheduling, and realtime connections. `stateful` `serverless` `realtime`   | TypeScript · MIT | library, managed            | 2026-08-21 |
| [DeerFlow](https://github.com/bytedance/deer-flow)         | ⭐ 80,480  | Long-horizon agent harness with sandboxes, memory, skills, subagents, and a messaging gateway. `long-running` `skills` `multi-agent`               | Python · MIT     | local, self-hosted          | 2026-08-20 |
| [OpenHands](https://github.com/OpenHands/OpenHands)        | ⭐ 84,708  | Software-development agent platform with a runtime for executing tools in isolated workspaces. `coding` `sandbox` `multi-agent`                    | TypeScript · MIT | local, self-hosted, managed | 2026-08-21 |
| [T3 Code](https://github.com/pingdotgg/t3code)             | ⭐ 19,905  | Local control plane for operating existing coding-agent CLIs from web, desktop, and mobile clients. `control-plane` `coding` `remote-access`       | TypeScript · MIT | local, self-hosted          | 2026-08-21 |

### Durable orchestration

Workflow and state-machine substrates for checkpoints, retries, waits, schedules, recovery, and reconciliation.

| Project                                                     | Stars    | Runtime fit                                                                                                                                    | Stack                   | Deploy                        | Last push  |
| ----------------------------------------------------------- | -------: | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ----------------------------- | ---------- |
| [Hatchet](https://github.com/hatchet-dev/hatchet)           | ⭐ 7,773  | Task orchestration platform for durable workflows, queues, retries, concurrency, and monitoring. `durable` `workflows` `observability`         | Go · MIT                | self-hosted, managed          | 2026-08-21 |
| [Inngest](https://github.com/inngest/inngest)               | ⭐ 5,752  | Event-driven durable execution platform for step functions, scheduling, retries, and agent workflows. `durable` `event-driven` `workflows`     | Go                      | self-hosted, managed          | 2026-08-21 |
| [LangGraph](https://github.com/langchain-ai/langgraph)      | ⭐ 40,184 | Graph-based runtime for stateful, durable, and human-in-the-loop agent workflows. `durable` `human-in-the-loop` `graph`                        | Python · MIT            | library, self-hosted, managed | 2026-08-20 |
| [Temporal](https://github.com/temporalio/temporal)          | ⭐ 22,438 | General durable-execution platform commonly used to make long-running agent workflows resilient. `durable` `workflows` `recovery`              | Go · MIT                | self-hosted, managed          | 2026-08-21 |
| [Trigger.dev](https://github.com/triggerdotdev/trigger.dev) | ⭐ 16,084 | TypeScript background-job platform for long-running AI tasks with retries, queues, and monitoring. `durable` `background-jobs` `observability` | TypeScript · Apache-2.0 | self-hosted, managed          | 2026-08-21 |

### Personal agent OSes and continuity

Long-lived personal agents that own identity, sessions, memory, schedules, connections, or notifications across interactions.

| Project                                                      | Stars     | Runtime fit                                                                                                                                                           | Stack            | Deploy               | Last push  |
| ------------------------------------------------------------ | --------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------- | ---------- |
| [ElizaOS](https://github.com/elizaOS/eliza)                  | ⭐ 19,113  | Agent operating system with persistent identities, multi-agent coordination, and a plugin ecosystem. `multi-agent` `plugins` `memory`                                 | TypeScript · MIT | local, self-hosted   | 2026-08-21 |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | ⭐ 233,872 | Persistent agent runtime with learned skills, cross-session memory, schedules, messaging gateways, and subagents. `self-improving` `skills` `scheduler` `multi-agent` | Python · MIT     | local, self-hosted   | 2026-08-21 |
| [Letta](https://github.com/letta-ai/letta)                   | ⭐ 24,332  | Stateful agent server centered on persistent memory, context management, and long-lived identities. `memory` `server` `stateful`                                      | Apache-2.0       | self-hosted, managed | 2026-08-16 |
| [Nanobot](https://github.com/HKUDS/nanobot)                  | ⭐ 47,255  | Lightweight self-hosted personal agent with tools, memory, MCP, automations, and chat integrations. `personal-agent` `MCP` `automation`                               | Python · MIT     | local, self-hosted   | 2026-08-21 |
| [NanoClaw](https://github.com/nanocoai/nanoclaw)             | ⭐ 30,588  | Container-isolated personal agent runtime with messaging channels, memory, skills, and scheduled jobs. `personal-agent` `containers` `scheduler`                      | TypeScript · MIT | local, self-hosted   | 2026-08-21 |
| [OpenClaw](https://github.com/openclaw/openclaw)             | ⭐ 387,029 | Personal agent runtime with messaging channels, schedules, memory, skills, and tool execution. `personal-agent` `scheduler` `tools`                                   | TypeScript       | local, self-hosted   | 2026-08-21 |

### Execution and isolation

Sandboxes and controlled environments in which agents run code, commands, browsers, and tools.

| Project                                                         | Stars    | Runtime fit                                                                                                                      | Stack               | Deploy               | Last push  |
| --------------------------------------------------------------- | -------: | -------------------------------------------------------------------------------------------------------------------------------- | ------------------- | -------------------- | ---------- |
| [Daytona](https://github.com/daytonaio/daytona)                 | ⭐ 71,927 | Secure infrastructure for programmatically creating and managing agent execution sandboxes. `sandbox` `code-execution` `API`     | —                   | self-hosted, managed | 2026-07-24 |
| [E2B](https://github.com/e2b-dev/E2B)                           | ⭐ 13,507 | Open-source infrastructure for running agent-generated code in isolated cloud sandboxes. `sandbox` `code-execution` `API`        | Python · Apache-2.0 | self-hosted, managed | 2026-08-21 |
| [Microsandbox](https://github.com/superradcompany/microsandbox) | ⭐ 7,842  | Self-hosted microVM platform for secure, fast, and isolated user or agent code execution. `microVM` `isolation` `code-execution` | Rust · Apache-2.0   | local, self-hosted   | 2026-08-21 |
| [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell)         | ⭐ 8,304  | Policy-governed runtime for running autonomous agents inside private sandboxes. `sandbox` `policy` `privacy`                     | Rust · Apache-2.0   | local, self-hosted   | 2026-08-21 |

### Application platforms and infrastructure

Platforms for building, packaging, exposing, and operating agent applications.

| Project                                                      | Stars     | Runtime fit                                                                                                                            | Stack        | Deploy                      | Last push  |
| ------------------------------------------------------------ | --------: | -------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------------------- | ---------- |
| [Dify](https://github.com/langgenius/dify)                   | ⭐ 153,128 | Visual platform for building and operating agentic applications, workflows, and model services. `low-code` `workflows` `observability` | TypeScript   | self-hosted, managed        | 2026-08-21 |
| [Flowise](https://github.com/FlowiseAI/Flowise) **Archived** | ⭐ 55,382  | Visual builder and serving platform for agent flows, assistants, and tool integrations. `low-code` `builder` `tools`                   | TypeScript   | self-hosted, managed        | 2026-08-13 |
| [Langflow](https://github.com/langflow-ai/langflow)          | ⭐ 153,528 | Visual Python framework for composing and serving agent workflows with an API. `low-code` `builder` `API`                              | Python · MIT | local, self-hosted, managed | 2026-08-21 |
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
