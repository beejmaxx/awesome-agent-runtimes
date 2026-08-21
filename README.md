# Awesome Agent Runtimes [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint disable table-cell-padding table-pipe-alignment-->

> A curated, comparable map of the software that actually **runs AI agents**:
> persistent agent operating systems, orchestration runtimes, serving layers,
> secure execution environments, and durable workflow substrates.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Catalog entries](https://img.shields.io/badge/entries-39-5b5bd6.svg)
[![Metadata](https://img.shields.io/badge/metadata-2026-08-21-2ea44f.svg)](data/metrics.json)

This list is for engineers deciding **where an agent loop lives, how it keeps
state, and where its tools execute**. It deliberately does not try to catalog
every chatbot, model SDK, prompt library, or finished agent application.

Metadata was last refreshed on **2026-08-21**. Star counts are snapshots;
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
### Persistent agent runtimes

Complete environments for long-lived assistants, autonomous workers, or coding agents.

| Project                                                      | Stars                                                                   | Runtime fit                                                                                                                                                           | Stack             | Deploy                      |
| ------------------------------------------------------------ | ----------------------------------------------------------------------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------------------------- |
| [Agent Zero](https://github.com/agent0ai/agent-zero)         | [⭐ 18,921](https://github.com/agent0ai/agent-zero/stargazers)           | General-purpose autonomous agent runtime with an interactive UI, subordinate agents, and executable tools. `multi-agent` `code-execution` `memory`                    | Python            | local, self-hosted          |
| [AIOS](https://github.com/agiresearch/AIOS)                  | [⭐ 6,261](https://github.com/agiresearch/AIOS/stargazers)               | Research agent operating-system kernel for scheduling LLM calls, memory, storage, and tools. `scheduler` `memory` `research`                                          | Python            | local, library              |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)   | [⭐ 186,709](https://github.com/Significant-Gravitas/AutoGPT/stargazers) | Platform for creating, deploying, and continuously running autonomous agents. `continuous` `builder` `marketplace`                                                    | Python            | self-hosted, managed        |
| [Goose](https://github.com/aaif-goose/goose)                 | [⭐ 53,151](https://github.com/aaif-goose/goose/stargazers)              | Local extensible agent runtime that automates engineering tasks through MCP tools. `coding` `MCP` `desktop`                                                           | Rust · Apache-2.0 | local                       |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | [⭐ 233,842](https://github.com/NousResearch/hermes-agent/stargazers)    | Persistent agent runtime with learned skills, cross-session memory, schedules, messaging gateways, and subagents. `self-improving` `skills` `scheduler` `multi-agent` | Python · MIT      | local, self-hosted          |
| [Letta](https://github.com/letta-ai/letta)                   | [⭐ 24,331](https://github.com/letta-ai/letta/stargazers)                | Stateful agent server centered on persistent memory, context management, and long-lived identities. `memory` `server` `stateful`                                      | Apache-2.0        | self-hosted, managed        |
| [OpenClaw](https://github.com/openclaw/openclaw)             | [⭐ 387,024](https://github.com/openclaw/openclaw/stargazers)            | Personal agent runtime with messaging channels, schedules, memory, skills, and tool execution. `personal-agent` `scheduler` `tools`                                   | TypeScript        | local, self-hosted          |
| [OpenCode](https://github.com/anomalyco/opencode)            | [⭐ 199,823](https://github.com/anomalyco/opencode/stargazers)           | Open-source coding-agent runtime for terminal, desktop, and IDE clients with parallel sessions. `coding` `client-server` `multi-session`                              | TypeScript · MIT  | local, self-hosted          |
| [OpenHands](https://github.com/OpenHands/OpenHands)          | [⭐ 84,701](https://github.com/OpenHands/OpenHands/stargazers)           | Software-development agent platform with a runtime for executing tools in isolated workspaces. `coding` `sandbox` `multi-agent`                                       | TypeScript · MIT  | local, self-hosted, managed |
| [Pi](https://github.com/earendil-works/pi)                   | [⭐ 94,927](https://github.com/earendil-works/pi/stargazers)             | Extensible coding-agent toolkit and CLI with persistent sessions, a unified model API, and UI libraries. `coding` `extensible` `sessions`                             | TypeScript · MIT  | local, library              |

### Agent and workflow runtimes

Libraries and kernels that own the agent loop, state transitions, or multi-agent coordination.

| Project                                                                   | Stars                                                                 | Runtime fit                                                                                                                              | Stack               | Deploy                        |
| ------------------------------------------------------------------------- | --------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------------- |
| [AgentScope](https://github.com/agentscope-ai/agentscope)                 | [⭐ 29,150](https://github.com/agentscope-ai/agentscope/stargazers)    | Developer framework for tool-using and multi-agent applications with runtime services. `multi-agent` `tools` `distributed`               | Python · Apache-2.0 | library, self-hosted          |
| [Agno](https://github.com/agno-agi/agno)                                  | [⭐ 41,822](https://github.com/agno-agi/agno/stargazers)               | Python framework and AgentOS runtime for building, serving, and monitoring agent systems. `multi-agent` `memory` `observability`         | Python · Apache-2.0 | library, self-hosted, managed |
| [AutoGen](https://github.com/microsoft/autogen)                           | [⭐ 60,559](https://github.com/microsoft/autogen/stargazers)           | Event-driven framework for conversational, tool-using, and multi-agent applications. `multi-agent` `event-driven` `tools`                | Python · CC-BY-4.0  | library, self-hosted          |
| [CAMEL](https://github.com/camel-ai/camel)                                | [⭐ 17,614](https://github.com/camel-ai/camel/stargazers)              | Multi-agent framework and research platform for agent societies, tools, memory, and task execution. `multi-agent` `research` `memory`    | Python · Apache-2.0 | library, self-hosted          |
| [CrewAI](https://github.com/crewAIInc/crewAI)                             | [⭐ 57,425](https://github.com/crewAIInc/crewAI/stargazers)            | Role-based multi-agent runtime for coordinating crews and event-driven flows. `multi-agent` `flows` `observability`                      | Python · MIT        | library, self-hosted, managed |
| [Dapr Agents](https://github.com/dapr/dapr-agents)                        | [⭐ 740](https://github.com/dapr/dapr-agents/stargazers)               | Agent framework built on Dapr actors and durable workflows for resilient distributed execution. `durable` `actors` `distributed`         | Python · Apache-2.0 | library, self-hosted          |
| [Google Agent Development Kit](https://github.com/google/adk-python)      | [⭐ 21,216](https://github.com/google/adk-python/stargazers)           | Code-first agent framework with sessions, tools, evaluation, and local or managed runtime options. `multi-agent` `evaluation` `tools`    | Python · Apache-2.0 | library, local, managed       |
| [LangGraph](https://github.com/langchain-ai/langgraph)                    | [⭐ 40,175](https://github.com/langchain-ai/langgraph/stargazers)      | Graph-based runtime for stateful, durable, and human-in-the-loop agent workflows. `durable` `human-in-the-loop` `graph`                  | Python · MIT        | library, self-hosted, managed |
| [Mastra](https://github.com/mastra-ai/mastra)                             | [⭐ 27,351](https://github.com/mastra-ai/mastra/stargazers)            | TypeScript agent framework with workflows, memory, evaluation, and observability. `workflows` `memory` `observability`                   | TypeScript          | library, self-hosted, managed |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | [⭐ 13,024](https://github.com/microsoft/agent-framework/stargazers)   | Microsoft framework for building agents and graph workflows with middleware and state management. `workflows` `multi-agent` `middleware` | Python · MIT        | library, self-hosted, managed |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python)       | [⭐ 28,830](https://github.com/openai/openai-agents-python/stargazers) | Lightweight Python runtime for agent loops, handoffs, guardrails, sessions, and tracing. `handoffs` `guardrails` `tracing`               | Python · MIT        | library                       |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai)                    | [⭐ 19,430](https://github.com/pydantic/pydantic-ai/stargazers)        | Typed Python agent framework with tools, durable execution integrations, graphs, and evaluation. `typed` `durable` `evaluation`          | Python · MIT        | library, self-hosted          |

### Serving and control planes

Systems for packaging, deploying, exposing, and operating agent workloads.

| Project                                                      | Stars                                                           | Runtime fit                                                                                                                                  | Stack            | Deploy                      |
| ------------------------------------------------------------ | --------------------------------------------------------------: | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------------------------- |
| [Dify](https://github.com/langgenius/dify)                   | [⭐ 153,122](https://github.com/langgenius/dify/stargazers)      | Visual platform for building and operating agentic applications, workflows, and model services. `low-code` `workflows` `observability`       | TypeScript       | self-hosted, managed        |
| [Docker Agent](https://github.com/docker/docker-agent)       | [⭐ 3,279](https://github.com/docker/docker-agent/stargazers)    | Declarative runtime and CLI for packaging and running agents with models, MCP tools, and subagents. `containers` `MCP` `multi-agent`         | Go · Apache-2.0  | local, self-hosted          |
| [Flowise](https://github.com/FlowiseAI/Flowise) **Archived** | [⭐ 55,383](https://github.com/FlowiseAI/Flowise/stargazers)     | Visual builder and serving platform for agent flows, assistants, and tool integrations. `low-code` `builder` `tools`                         | TypeScript       | self-hosted, managed        |
| [Langflow](https://github.com/langflow-ai/langflow)          | [⭐ 153,529](https://github.com/langflow-ai/langflow/stargazers) | Visual Python framework for composing and serving agent workflows with an API. `low-code` `builder` `API`                                    | Python · MIT     | local, self-hosted, managed |
| [LlamaDeploy](https://github.com/run-llama/llama_deploy)     | [⭐ 2,068](https://github.com/run-llama/llama_deploy/stargazers) | Deployment system for running agent workflows as scalable, event-driven services. `event-driven` `services` `scaling`                        | Python · MIT     | self-hosted                 |
| [T3 Code](https://github.com/pingdotgg/t3code)               | [⭐ 19,894](https://github.com/pingdotgg/t3code/stargazers)      | Local control plane for operating existing coding-agent CLIs from web, desktop, and mobile clients. `control-plane` `coding` `remote-access` | TypeScript · MIT | local, self-hosted          |

### Sandboxes and execution environments

Isolated environments in which agents can safely run code, commands, and tools.

| Project                                                                | Stars                                                                     | Runtime fit                                                                                                                      | Stack               | Deploy               |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------: | -------------------------------------------------------------------------------------------------------------------------------- | ------------------- | -------------------- |
| [CubeSandbox](https://github.com/TencentCloudAgentRuntime/CubeSandbox) | [⭐ 0](https://github.com/TencentCloudAgentRuntime/CubeSandbox/stargazers) | High-performance microVM sandbox runtime for concurrent AI-agent workloads. `microVM` `isolation` `code-execution`               | Go                  | self-hosted          |
| [Daytona](https://github.com/daytonaio/daytona)                        | [⭐ 71,933](https://github.com/daytonaio/daytona/stargazers)               | Secure infrastructure for programmatically creating and managing agent execution sandboxes. `sandbox` `code-execution` `API`     | —                   | self-hosted, managed |
| [E2B](https://github.com/e2b-dev/E2B)                                  | [⭐ 13,506](https://github.com/e2b-dev/E2B/stargazers)                     | Open-source infrastructure for running agent-generated code in isolated cloud sandboxes. `sandbox` `code-execution` `API`        | Python · Apache-2.0 | self-hosted, managed |
| [Microsandbox](https://github.com/superradcompany/microsandbox)        | [⭐ 7,841](https://github.com/superradcompany/microsandbox/stargazers)     | Self-hosted microVM platform for secure, fast, and isolated user or agent code execution. `microVM` `isolation` `code-execution` | Rust · Apache-2.0   | local, self-hosted   |
| [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell)                | [⭐ 8,302](https://github.com/NVIDIA/OpenShell/stargazers)                 | Policy-governed runtime for running autonomous agents inside private sandboxes. `sandbox` `policy` `privacy`                     | Rust · Apache-2.0   | local, self-hosted   |
| [SandboxFusion](https://github.com/bytedance/SandboxFusion)            | [⭐ 1,059](https://github.com/bytedance/SandboxFusion/stargazers)          | Execution service for isolated code evaluation across many programming languages. `sandbox` `code-execution` `multi-language`    | Python · Apache-2.0 | self-hosted          |

### Durable execution substrates

Agent-adjacent workflow engines used for retries, resumability, schedules, and long-running work.

| Project                                                     | Stars                                                               | Runtime fit                                                                                                                                    | Stack                   | Deploy                        |
| ----------------------------------------------------------- | ------------------------------------------------------------------: | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ----------------------------- |
| [DBOS](https://github.com/dbos-inc/dbos-transact-py)        | [⭐ 1,539](https://github.com/dbos-inc/dbos-transact-py/stargazers)  | Python durable-execution library for workflows that recover state and resume after failures. `durable` `workflows` `recovery`                  | Python · MIT            | library, self-hosted, managed |
| [Hatchet](https://github.com/hatchet-dev/hatchet)           | [⭐ 7,772](https://github.com/hatchet-dev/hatchet/stargazers)        | Task orchestration platform for durable workflows, queues, retries, concurrency, and monitoring. `durable` `workflows` `observability`         | Go · MIT                | self-hosted, managed          |
| [Inngest](https://github.com/inngest/inngest)               | [⭐ 5,752](https://github.com/inngest/inngest/stargazers)            | Event-driven durable execution platform for step functions, scheduling, retries, and agent workflows. `durable` `event-driven` `workflows`     | Go                      | self-hosted, managed          |
| [Temporal](https://github.com/temporalio/temporal)          | [⭐ 22,438](https://github.com/temporalio/temporal/stargazers)       | General durable-execution platform commonly used to make long-running agent workflows resilient. `durable` `workflows` `recovery`              | Go · MIT                | self-hosted, managed          |
| [Trigger.dev](https://github.com/triggerdotdev/trigger.dev) | [⭐ 16,084](https://github.com/triggerdotdev/trigger.dev/stargazers) | TypeScript background-job platform for long-running AI tasks with retries, queues, and monitoring. `durable` `background-jobs` `observability` | TypeScript · Apache-2.0 | self-hosted, managed          |
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
