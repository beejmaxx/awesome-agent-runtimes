# Awesome Agent Runtimes [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<!--lint disable table-cell-padding table-pipe-alignment-->

> A curated, comparable map of the software that **owns part of agent execution**—
> from cognition and supervision to continuity, isolation, and durable recovery.

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Catalog entries](https://img.shields.io/badge/entries-64-5b5bd6.svg)
[![Metadata](https://img.shields.io/badge/metadata-2026-09-04-2ea44f.svg)](data/metrics.json)

This list is for engineers deciding **who owns the intelligence and who owns
operational truth** when an agent acts. It deliberately does not treat every
framework, host, workflow engine, sandbox, and memory system as the same kind
of "agent runtime."

Metadata was last refreshed on **2026-09-04**. Star counts are snapshots;
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
  - [Agent cognition — realtime voice and multimodal](#agent-cognition--realtime-voice-and-multimodal)
  - [Agent cognition — browser and computer use](#agent-cognition--browser-and-computer-use)
  - [Agent hosts and supervisors](#agent-hosts-and-supervisors)
  - [Durable orchestration](#durable-orchestration)
  - [Personal agent OSes and continuity](#personal-agent-oses-and-continuity)
  - [Execution and isolation](#execution-and-isolation)
  - [Application platforms and infrastructure](#application-platforms-and-infrastructure)
  - [Historical projects](#historical-projects)
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
| Agent interaction and UI | Shared application state, human approvals, and generative interfaces | Agent reasoning or runtime lifecycle |
| Evaluation and assurance | Behavioral tests, red teaming, and quality or security gates | Live operational tracing |
| Supporting infrastructure | Protocols, portable formats, gateways, observability, deployment | Ownership of the end-to-end agent experience |

The last distinction matters: **memory is not the same as durable project
state**. A transcript or vector store can help an agent recall information
without owning tasks, artifacts, decisions, outcomes, or reconciliation. The
broader [architecture map](STACK.md#the-host-and-work-state-boundaries) keeps this boundary visible
without mislabeling supporting work-state systems as agent runtimes.

## Quality bar

Every entry must have a meaningful public implementation, identifiable
maintainers, usable documentation, and evidence that it owns part of runtime
execution. Projects are reviewed for scope, maintenance, license visibility, and
distinctiveness. See [`METHODOLOGY.md`](METHODOLOGY.md) for lifecycle rules,
metadata limitations, and the correction process.

The validator enforces the 5,000-star floor, 180 days of public history, activity
within the last year, a visible license or reviewed license override, and a
separate historical category for archived projects.

## Choose a layer

| If you need to…                                           | Start with…                                  |
| --------------------------------------------------------- | -------------------------------------------- |
| Give an agent a coding or general reasoning loop          | Agent cognition                              |
| Build realtime voice, video, or telephony agents          | Realtime voice and multimodal                |
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

| Project                                                                | Stars     | 30d | Runtime fit                                                                                                                                                                                                | Stack                   | Deploy             | Last push  |
| ---------------------------------------------------------------------- | --------: | --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------ | ---------- |
| [Aider](https://github.com/Aider-AI/aider)                             | ⭐ 48,729  | —   | Terminal coding-agent runtime built around repository maps, editable worktrees, and Git-native sessions. [evidence](https://github.com/Aider-AI/aider#readme) `coding` `terminal` `git`                    | Python · Apache-2.0     | local              | 2026-05-22 |
| [Cline](https://github.com/cline/cline)                                | ⭐ 67,449  | —   | Autonomous coding-agent runtime available as an IDE extension, CLI, and embeddable SDK. [evidence](https://github.com/cline/cline#readme) `coding` `IDE` `human-in-the-loop`                               | TypeScript · Apache-2.0 | local, library     | 2026-09-04 |
| [Codex](https://github.com/openai/codex)                               | ⭐ 121,398 | —   | Local coding-agent runtime and CLI with sandboxed command execution, approvals, and automation modes. [evidence](https://github.com/openai/codex#readme) `coding` `sandbox` `terminal`                     | Rust · Apache-2.0       | local              | 2026-09-04 |
| [Continue](https://github.com/continuedev/continue)                    | ⭐ 35,754  | —   | Open-source coding-agent runtime spanning IDE, CLI, and continuous repository automation. [evidence](https://github.com/continuedev/continue#readme) `coding` `IDE` `automation`                           | TypeScript · Apache-2.0 | local, self-hosted | 2026-09-03 |
| [Crush](https://github.com/charmbracelet/crush)                        | ⭐ 27,896  | —   | Terminal coding-agent runtime with multi-model support, language-server integration, and extensible tools. [evidence](https://github.com/charmbracelet/crush#readme) `coding` `terminal` `LSP`             | Go · FSL-1.1-MIT        | local              | 2026-09-04 |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli)              | ⭐ 106,809 | —   | Terminal agent runtime for coding and general automation with tools, extensions, and MCP support. [evidence](https://github.com/google-gemini/gemini-cli#readme) `coding` `terminal` `MCP`                 | TypeScript · Apache-2.0 | local              | 2026-09-04 |
| [Goose](https://github.com/aaif-goose/goose)                           | ⭐ 53,897  | —   | Local extensible agent runtime that automates engineering tasks through MCP tools. [evidence](https://github.com/aaif-goose/goose#readme) `coding` `MCP` `desktop`                                         | Rust · Apache-2.0       | local              | 2026-09-04 |
| [Kilo Code](https://github.com/Kilo-Org/kilocode)                      | ⭐ 27,170  | —   | Open-source coding agent for IDEs and the terminal with multiple models, specialized agents, and a managed cloud option. [evidence](https://github.com/Kilo-Org/kilocode#readme) `coding` `IDE` `terminal` | TypeScript · MIT        | local, managed     | 2026-09-04 |
| [Open Interpreter](https://github.com/openinterpreter/openinterpreter) | ⭐ 68,233  | —   | Local coding-agent runtime for open models with computer tools and executable workflows. [evidence](https://github.com/openinterpreter/openinterpreter#readme) `coding` `computer-use` `local-models`      | Rust · Apache-2.0       | local              | 2026-08-20 |
| [OpenCode](https://github.com/anomalyco/opencode)                      | ⭐ 203,667 | —   | Open-source coding-agent runtime for terminal, desktop, and IDE clients with parallel sessions. [evidence](https://github.com/anomalyco/opencode#readme) `coding` `client-server` `multi-session`          | TypeScript · MIT        | local, self-hosted | 2026-09-04 |
| [Pi](https://github.com/earendil-works/pi)                             | ⭐ 101,632 | —   | Extensible coding-agent toolkit and CLI with persistent sessions, a unified model API, and UI libraries. [evidence](https://github.com/earendil-works/pi#readme) `coding` `extensible` `sessions`          | TypeScript · MIT        | local, library     | 2026-09-04 |
| [Qwen Code](https://github.com/QwenLM/qwen-code)                       | ⭐ 27,635  | —   | Open-source terminal coding-agent runtime with tools, extensibility, and model-provider support. [evidence](https://github.com/QwenLM/qwen-code#readme) `coding` `terminal` `tools`                        | TypeScript · Apache-2.0 | local              | 2026-09-04 |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent)                    | ⭐ 20,215  | —   | Research-backed software-engineering agent runtime for resolving repository issues in controlled environments. [evidence](https://github.com/SWE-agent/SWE-agent#readme) `coding` `research` `benchmark`   | Python · MIT            | local, self-hosted | 2026-08-31 |

### Agent cognition — construction SDKs

Libraries for constructing model/tool loops, routing, state transitions, and multi-agent behavior.

| Project                                                                   | Stars     | 30d | Runtime fit                                                                                                                                                                                                  | Stack                          | Deploy                        | Last push  |
| ------------------------------------------------------------------------- | --------: | --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------ | ----------------------------- | ---------- |
| [AgentScope](https://github.com/agentscope-ai/agentscope)                 | ⭐ 30,622  | —   | Developer framework for tool-using and multi-agent applications with runtime services. [evidence](https://github.com/agentscope-ai/agentscope#readme) `multi-agent` `tools` `distributed`                    | Python · Apache-2.0            | library, self-hosted          | 2026-09-04 |
| [Agno](https://github.com/agno-agi/agno)                                  | ⭐ 42,042  | —   | Python framework and AgentOS runtime for building, serving, and monitoring agent systems. [evidence](https://github.com/agno-agi/agno#readme) `multi-agent` `memory` `observability`                         | Python · Apache-2.0            | library, self-hosted, managed | 2026-09-04 |
| [AutoGen](https://github.com/microsoft/autogen)                           | ⭐ 60,797  | —   | Event-driven framework for conversational, tool-using, and multi-agent applications. [evidence](https://github.com/microsoft/autogen#readme) `multi-agent` `event-driven` `tools`                            | Python · CC-BY-4.0             | library, self-hosted          | 2026-04-15 |
| [CAMEL](https://github.com/camel-ai/camel)                                | ⭐ 17,670  | —   | Multi-agent framework and research platform for agent societies, tools, memory, and task execution. [evidence](https://github.com/camel-ai/camel#readme) `multi-agent` `research` `memory`                   | Python · Apache-2.0            | library, self-hosted          | 2026-09-03 |
| [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python) | ⭐ 8,036   | —   | Anthropic's Python SDK for building agents with Claude Code's tools, sessions, and execution loop. [evidence](https://github.com/anthropics/claude-agent-sdk-python#readme) `tools` `sessions` `SDK`         | Python · MIT                   | library, self-hosted          | 2026-09-03 |
| [CrewAI](https://github.com/crewAIInc/crewAI)                             | ⭐ 58,076  | —   | Role-based multi-agent runtime for coordinating crews and event-driven flows. [evidence](https://github.com/crewAIInc/crewAI#readme) `multi-agent` `flows` `observability`                                   | Python · MIT                   | library, self-hosted, managed | 2026-09-04 |
| [Deep Agents](https://github.com/langchain-ai/deepagents)                 | ⭐ 28,940  | —   | Batteries-included agent harness with planning, filesystems, subagents, and long-term memory. [evidence](https://github.com/langchain-ai/deepagents#readme) `planning` `multi-agent` `memory`                | Python · MIT                   | library, self-hosted          | 2026-09-04 |
| [Google Agent Development Kit](https://github.com/google/adk-python)      | ⭐ 21,404  | —   | Code-first agent framework with sessions, tools, evaluation, and local or managed runtime options. [evidence](https://github.com/google/adk-python#readme) `multi-agent` `evaluation` `tools`                | Python · Apache-2.0            | library, local, managed       | 2026-09-04 |
| [LangChain](https://github.com/langchain-ai/langchain)                    | ⭐ 145,621 | —   | Established agent application framework with model, tool, middleware, and agent-loop abstractions. [evidence](https://github.com/langchain-ai/langchain#readme) `tools` `middleware` `ecosystem`             | Python · MIT                   | library, self-hosted          | 2026-09-04 |
| [LlamaIndex](https://github.com/run-llama/llama_index)                    | ⭐ 52,012  | —   | Data-centric agent framework with workflows, tools, retrieval, memory, and multi-agent patterns. [evidence](https://github.com/run-llama/llama_index#readme) `data` `workflows` `retrieval`                  | Python · MIT                   | library, self-hosted, managed | 2026-09-03 |
| [Mastra](https://github.com/mastra-ai/mastra)                             | ⭐ 27,688  | —   | TypeScript agent framework with workflows, memory, evaluation, and observability. [evidence](https://github.com/mastra-ai/mastra#readme) `workflows` `memory` `observability`                                | TypeScript · Apache-2.0 (core) | library, self-hosted, managed | 2026-09-04 |
| [MetaGPT](https://github.com/FoundationAgents/MetaGPT)                    | ⭐ 70,211  | —   | Multi-agent software-company framework that coordinates role-based agents through structured workflows. [evidence](https://github.com/FoundationAgents/MetaGPT#readme) `multi-agent` `roles` `workflows`     | Python · MIT                   | library, local                | 2026-01-21 |
| [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) | ⭐ 13,320  | —   | Microsoft framework for building agents and graph workflows with middleware and state management. [evidence](https://github.com/microsoft/agent-framework#readme) `workflows` `multi-agent` `middleware`     | Python · MIT                   | library, self-hosted, managed | 2026-09-04 |
| [OpenAI Agents SDK](https://github.com/openai/openai-agents-python)       | ⭐ 29,186  | —   | Lightweight Python runtime for agent loops, handoffs, guardrails, sessions, and tracing. [evidence](https://github.com/openai/openai-agents-python#readme) `handoffs` `guardrails` `tracing`                 | Python · MIT                   | library                       | 2026-09-02 |
| [Pydantic AI](https://github.com/pydantic/pydantic-ai)                    | ⭐ 19,715  | —   | Typed Python agent framework with tools, durable execution integrations, graphs, and evaluation. [evidence](https://github.com/pydantic/pydantic-ai#readme) `typed` `durable` `evaluation`                   | Python · MIT                   | library, self-hosted          | 2026-09-04 |
| [Semantic Kernel](https://github.com/microsoft/semantic-kernel)           | ⭐ 28,528  | —   | Microsoft agent SDK with plugins, process orchestration, memory integrations, and multi-agent patterns. [evidence](https://github.com/microsoft/semantic-kernel#readme) `plugins` `multi-agent` `enterprise` | C# · MIT                       | library, self-hosted, managed | 2026-09-03 |
| [smolagents](https://github.com/huggingface/smolagents)                   | ⭐ 29,149  | —   | Compact Hugging Face agent library centered on code-executing agents and composable tools. [evidence](https://github.com/huggingface/smolagents#readme) `code-agents` `tools` `lightweight`                  | Python · Apache-2.0            | library, local                | 2026-08-25 |

### Agent cognition — realtime voice and multimodal

Frameworks and runtimes for low-latency voice, video, telephony, and multimodal agent interactions.

| Project                                             | Stars    | 30d | Runtime fit                                                                                                                                                                                                                       | Stack                 | Deploy                        | Last push  |
| --------------------------------------------------- | -------: | --: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ----------------------------- | ---------- |
| [LiveKit Agents](https://github.com/livekit/agents) | ⭐ 14,001 | —   | Server-side framework for realtime voice and multimodal agents with job dispatch, telephony, testing, and provider integrations. [evidence](https://github.com/livekit/agents#readme) `voice` `multimodal` `realtime` `telephony` | Python · Apache-2.0   | library, self-hosted, managed | 2026-09-04 |
| [Pipecat](https://github.com/pipecat-ai/pipecat)    | ⭐ 15,198 | —   | Python framework for realtime voice and multimodal agents with streaming pipelines and multi-agent coordination. [evidence](https://github.com/pipecat-ai/pipecat#readme) `voice` `multimodal` `realtime` `multi-agent`           | Python · BSD-2-Clause | library, self-hosted, managed | 2026-09-04 |

### Agent cognition — browser and computer use

Harnesses and SDKs that own perception and action loops over browsers or desktop interfaces.

| Project                                                   | Stars     | 30d | Runtime fit                                                                                                                                                                                          | Stack               | Deploy                        | Last push  |
| --------------------------------------------------------- | --------: | --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------------- | ---------- |
| [Agent-S](https://github.com/simular-ai/Agent-S)          | ⭐ 12,222  | —   | Open computer-use agent framework for planning and executing tasks across desktop operating systems. [evidence](https://github.com/simular-ai/Agent-S#readme) `computer-use` `desktop` `research`    | Python · Apache-2.0 | library, local                | 2026-08-01 |
| [Browser Use](https://github.com/browser-use/browser-use) | ⭐ 112,227 | —   | Browser-agent framework and runtime for perception, action, sessions, and web task automation. [evidence](https://github.com/browser-use/browser-use#readme) `browser` `automation` `tools`          | Python · MIT        | library, local, managed       | 2026-09-04 |
| [Skyvern](https://github.com/Skyvern-AI/skyvern)          | ⭐ 22,929  | —   | Browser workflow runtime using visual and language-model reasoning instead of site-specific selectors. [evidence](https://github.com/Skyvern-AI/skyvern#readme) `browser` `workflows` `computer-use` | Python · AGPL-3.0   | self-hosted, managed          | 2026-09-04 |
| [Stagehand](https://github.com/browserbase/stagehand)     | ⭐ 24,138  | —   | Browser-agent SDK that combines natural-language actions with deterministic browser automation. [evidence](https://github.com/browserbase/stagehand#readme) `browser` `automation` `SDK`             | TypeScript · MIT    | library, self-hosted, managed | 2026-09-03 |
| [UFO](https://github.com/microsoft/UFO)                   | ⭐ 9,630   | —   | Microsoft agent framework for automating Windows applications and multi-device desktop workflows. [evidence](https://github.com/microsoft/UFO#readme) `computer-use` `desktop` `multi-agent`         | Python · MIT        | local                         | 2026-09-02 |

### Agent hosts and supervisors

Systems that start agents, provide environments and identity, stream events, supervise sessions, and recover failures.

| Project                                                    | Stars     | 30d | Runtime fit                                                                                                                                                                                                                          | Stack                                 | Deploy                      | Last push  |
| ---------------------------------------------------------- | --------: | --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- | --------------------------- | ---------- |
| [Agent Zero](https://github.com/agent0ai/agent-zero)       | ⭐ 19,082  | —   | General-purpose autonomous agent runtime with an interactive UI, subordinate agents, and executable tools. [evidence](https://github.com/agent0ai/agent-zero#readme) `multi-agent` `code-execution` `memory`                         | Python · MIT                          | local, self-hosted          | 2026-09-03 |
| [AionUi](https://github.com/iOfficeAI/AionUi)              | ⭐ 32,556  | —   | Cross-platform cowork application for supervising built-in and external CLI agents with remote access and persistent automation. [evidence](https://github.com/iOfficeAI/AionUi#readme) `control-plane` `multi-agent` `automation`   | TypeScript · Apache-2.0               | local, self-hosted          | 2026-09-02 |
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | ⭐ 187,110 | —   | Platform for creating, deploying, and continuously running autonomous agents. [evidence](https://github.com/Significant-Gravitas/AutoGPT#readme) `continuous` `builder` `marketplace`                                                | Python · Mixed: MIT / PolyForm Shield | self-hosted, managed        | 2026-09-04 |
| [Claude Squad](https://github.com/smtg-ai/claude-squad)    | ⭐ 8,422   | —   | Terminal supervisor for running multiple coding agents concurrently in isolated Git workspaces. [evidence](https://github.com/smtg-ai/claude-squad#readme) `supervisor` `coding` `worktrees`                                         | Go · AGPL-3.0                         | local                       | 2026-08-20 |
| [Cloudflare Agents](https://github.com/cloudflare/agents)  | ⭐ 5,515   | —   | Stateful agent SDK built on Durable Objects with identity, persistence, scheduling, and realtime connections. [evidence](https://github.com/cloudflare/agents#readme) `stateful` `serverless` `realtime`                             | TypeScript · MIT                      | library, managed            | 2026-09-03 |
| [DeerFlow](https://github.com/bytedance/deer-flow)         | ⭐ 81,342  | —   | Long-horizon agent harness with sandboxes, memory, skills, subagents, and a messaging gateway. [evidence](https://github.com/bytedance/deer-flow#readme) `long-running` `skills` `multi-agent`                                       | Python · MIT                          | local, self-hosted          | 2026-09-04 |
| [Gas Town](https://github.com/gastownhall/gastown)         | ⭐ 17,924  | —   | Multi-agent workspace manager with persistent work tracking, agent identities, mailboxes, handoffs, and Git worktrees. [evidence](https://github.com/gastownhall/gastown#readme) `supervisor` `work-state` `multi-agent` `worktrees` | Go · MIT                              | local                       | 2026-09-03 |
| [OpenHands](https://github.com/OpenHands/OpenHands)        | ⭐ 86,143  | —   | Software-development agent platform with a runtime for executing tools in isolated workspaces. [evidence](https://github.com/OpenHands/OpenHands#readme) `coding` `sandbox` `multi-agent`                                            | TypeScript · MIT                      | local, self-hosted, managed | 2026-09-04 |
| [T3 Code](https://github.com/pingdotgg/t3code)             | ⭐ 21,641  | —   | Local control plane for operating existing coding-agent CLIs from web, desktop, and mobile clients. [evidence](https://github.com/pingdotgg/t3code#readme) `control-plane` `coding` `remote-access`                                  | TypeScript · MIT                      | local, self-hosted          | 2026-09-04 |

### Durable orchestration

Workflow and state-machine substrates for checkpoints, retries, waits, schedules, recovery, and reconciliation.

| Project                                                     | Stars    | 30d | Runtime fit                                                                                                                                                                                                    | Stack                             | Deploy                        | Last push  |
| ----------------------------------------------------------- | -------: | --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | ----------------------------- | ---------- |
| [Hatchet](https://github.com/hatchet-dev/hatchet)           | ⭐ 7,860  | —   | Task orchestration platform for durable workflows, queues, retries, concurrency, and monitoring. [evidence](https://github.com/hatchet-dev/hatchet#readme) `durable` `workflows` `observability`               | Go · MIT                          | self-hosted, managed          | 2026-09-04 |
| [Inngest](https://github.com/inngest/inngest)               | ⭐ 5,804  | —   | Event-driven durable execution platform for step functions, scheduling, retries, and agent workflows. [evidence](https://github.com/inngest/inngest#readme) `durable` `event-driven` `workflows`               | Go · SSPL-1.0 / Apache-2.0 future | self-hosted, managed          | 2026-09-04 |
| [LangGraph](https://github.com/langchain-ai/langgraph)      | ⭐ 41,031 | —   | Graph-based runtime for stateful, durable, and human-in-the-loop agent workflows. [evidence](https://github.com/langchain-ai/langgraph#readme) `durable` `human-in-the-loop` `graph`                           | Python · MIT                      | library, self-hosted, managed | 2026-09-03 |
| [Temporal](https://github.com/temporalio/temporal)          | ⭐ 22,819 | —   | General durable-execution platform commonly used to make long-running agent workflows resilient. [evidence](https://github.com/temporalio/temporal#readme) `durable` `workflows` `recovery`                    | Go · MIT                          | self-hosted, managed          | 2026-09-04 |
| [Trigger.dev](https://github.com/triggerdotdev/trigger.dev) | ⭐ 16,211 | —   | TypeScript background-job platform for long-running AI tasks with retries, queues, and monitoring. [evidence](https://github.com/triggerdotdev/trigger.dev#readme) `durable` `background-jobs` `observability` | TypeScript · Apache-2.0           | self-hosted, managed          | 2026-09-04 |

### Personal agent OSes and continuity

Long-lived personal agents that own identity, sessions, memory, schedules, connections, or notifications across interactions.

| Project                                                      | Stars     | 30d | Runtime fit                                                                                                                                                                                                                           | Stack            | Deploy               | Last push  |
| ------------------------------------------------------------ | --------: | --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | -------------------- | ---------- |
| [ElizaOS](https://github.com/elizaOS/eliza)                  | ⭐ 19,242  | —   | Agent operating system with persistent identities, multi-agent coordination, and a plugin ecosystem. [evidence](https://github.com/elizaOS/eliza#readme) `multi-agent` `plugins` `memory`                                             | TypeScript · MIT | local, self-hosted   | 2026-09-04 |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | ⭐ 241,113 | —   | Persistent agent runtime with learned skills, cross-session memory, schedules, messaging gateways, and subagents. [evidence](https://github.com/NousResearch/hermes-agent#readme) `self-improving` `skills` `scheduler` `multi-agent` | Python · MIT     | local, self-hosted   | 2026-09-04 |
| [Letta](https://github.com/letta-ai/letta)                   | ⭐ 24,615  | —   | Stateful agent server centered on persistent memory, context management, and long-lived identities. [evidence](https://github.com/letta-ai/letta#readme) `memory` `server` `stateful`                                                 | Apache-2.0       | self-hosted, managed | 2026-08-23 |
| [Nanobot](https://github.com/HKUDS/nanobot)                  | ⭐ 47,703  | —   | Lightweight self-hosted personal agent with tools, memory, MCP, automations, and chat integrations. [evidence](https://github.com/HKUDS/nanobot#readme) `personal-agent` `MCP` `automation`                                           | Python · MIT     | local, self-hosted   | 2026-09-04 |
| [NanoClaw](https://github.com/nanocoai/nanoclaw)             | ⭐ 30,693  | —   | Container-isolated personal agent runtime with messaging channels, memory, skills, and scheduled jobs. [evidence](https://github.com/nanocoai/nanoclaw#readme) `personal-agent` `containers` `scheduler`                              | TypeScript · MIT | local, self-hosted   | 2026-09-04 |
| [OpenClaw](https://github.com/openclaw/openclaw)             | ⭐ 388,808 | —   | Personal agent runtime with messaging channels, schedules, memory, skills, and tool execution. [evidence](https://github.com/openclaw/openclaw#readme) `personal-agent` `scheduler` `tools`                                           | TypeScript · MIT | local, self-hosted   | 2026-09-04 |

### Execution and isolation

Sandboxes and controlled environments in which agents run code, commands, browsers, and tools.

| Project                                                         | Stars    | 30d | Runtime fit                                                                                                                                                                                                               | Stack               | Deploy                  | Last push  |
| --------------------------------------------------------------- | -------: | --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ----------------------- | ---------- |
| [CUA](https://github.com/trycua/cua)                            | ⭐ 22,177 | —   | Cross-platform computer-use infrastructure with background drivers, agent-ready VM and container sandboxes, and fleet tooling. [evidence](https://github.com/trycua/cua#readme) `computer-use` `sandbox` `virtualization` | HTML · MIT          | library, local, managed | 2026-09-03 |
| [E2B](https://github.com/e2b-dev/E2B)                           | ⭐ 13,667 | —   | Open-source infrastructure for running agent-generated code in isolated cloud sandboxes. [evidence](https://github.com/e2b-dev/E2B#readme) `sandbox` `code-execution` `API`                                               | Python · Apache-2.0 | self-hosted, managed    | 2026-09-04 |
| [Microsandbox](https://github.com/superradcompany/microsandbox) | ⭐ 8,076  | —   | Self-hosted microVM platform for secure, fast, and isolated user or agent code execution. [evidence](https://github.com/superradcompany/microsandbox#readme) `microVM` `isolation` `code-execution`                       | Rust · Apache-2.0   | local, self-hosted      | 2026-09-04 |

### Application platforms and infrastructure

Platforms for building, packaging, exposing, and operating agent applications.

| Project                                             | Stars     | 30d | Runtime fit                                                                                                                                                                                  | Stack                            | Deploy                      | Last push  |
| --------------------------------------------------- | --------: | --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | --------------------------- | ---------- |
| [Dify](https://github.com/langgenius/dify)          | ⭐ 154,412 | —   | Visual platform for building and operating agentic applications, workflows, and model services. [evidence](https://github.com/langgenius/dify#readme) `low-code` `workflows` `observability` | TypeScript · Modified Apache-2.0 | self-hosted, managed        | 2026-09-04 |
| [Langflow](https://github.com/langflow-ai/langflow) | ⭐ 154,230 | —   | Visual Python framework for composing and serving agent workflows with an API. [evidence](https://github.com/langflow-ai/langflow#readme) `low-code` `builder` `API`                         | Python · MIT                     | local, self-hosted, managed | 2026-09-04 |

### Historical projects

Popular, influential implementations that are now archived or formally discontinued; retained for historical comparison, not recommended for new deployments.

| Project                                                         | Stars    | 30d | Runtime fit                                                                                                                                                                               | Stack                          | Deploy               | Last push  |
| --------------------------------------------------------------- | -------: | --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ | -------------------- | ---------- |
| [Flowise](https://github.com/FlowiseAI/Flowise) **Archived**    | ⭐ 55,411 | —   | Archived visual builder and serving platform for agent flows, assistants, and tool integrations. [evidence](https://github.com/FlowiseAI/Flowise#readme) `low-code` `builder` `tools`     | TypeScript · Apache-2.0 (core) | self-hosted, managed | 2026-08-13 |
| [Roo Code](https://github.com/RooCodeInc/Roo-Code) **Archived** | ⭐ 24,312 | —   | Archived IDE coding-agent runtime with specialized modes, tool use, and multi-agent orchestration. [evidence](https://github.com/RooCodeInc/Roo-Code#readme) `coding` `IDE` `multi-agent` | TypeScript · Apache-2.0        | local                | 2026-05-15 |
<!-- END GENERATED CATALOG -->

## Tracking and data

The core and supporting catalogs have separate editorial sources of truth:
[`data/projects.json`](data/projects.json) and
[`data/stack-projects.json`](data/stack-projects.json).
[`scripts/update.py`](scripts/update.py) validates every entry, retrieves public
repository metadata from the GitHub API, renders the human and machine views,
and stores one star snapshot per UTC day. No third-party Python packages are
required.

| Artifact | Purpose |
| --- | --- |
| [`data/catalog.json`](data/catalog.json) | Core entries joined with current GitHub metadata and evidence URLs |
| [`data/catalog.csv`](data/catalog.csv) | Spreadsheet-ready core catalog |
| [`data/stack-catalog.json`](data/stack-catalog.json) | Adjacent stack projects with the same metadata tracking |
| [`data/stack-catalog.csv`](data/stack-catalog.csv) | Spreadsheet-ready adjacent stack map |
| [`llms.txt`](llms.txt) | Compact agent-readable catalog |
| [`TAGS.md`](TAGS.md) | Generated capability index |
| [`data/history.json`](data/history.json) | Daily star history for trend analysis |
| [`data/trends.json`](data/trends.json) | Computed 7-, 30-, and 90-day star changes |
| [`data/watchlist.json`](data/watchlist.json) | Deferred projects and scheduled review dates |
| [`data/exclusions.json`](data/exclusions.json) | Reviewed exclusions and reconsideration conditions |
| [`data/schema.json`](data/schema.json) | Source catalog JSON Schema |

Coverage is audited against the trusted upstream lists in
[`data/sources.json`](data/sources.json). The reproducible funnel and unreviewed
candidate queue are documented in [`DISCOVERY.md`](DISCOVERY.md). Production
layers that matter but are not themselves core entries—including protocols,
portable formats, interaction, authority, evaluation, observability, and
work-state primitives—are mapped separately in
[`STACK.md`](STACK.md). Deliberate deferrals and rejections are recorded in
[`WATCHLIST.md`](WATCHLIST.md) and [`EXCLUSIONS.md`](EXCLUSIONS.md).

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
