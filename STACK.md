# Agent Stack Ownership Map

"Agent runtime" is overloaded. Frameworks, supervisors, sandboxes, workflow
engines, protocols, memory systems, and work ledgers own different parts of the
stack. This map asks two sharper questions: **who owns the intelligence, and who
owns operational truth when it acts?**

Projects on this page are tracked with the same GitHub metadata and star history
as the core catalog, but they are not mislabeled as runtimes. Low-star exceptions
are limited to official standards or mature architectural primitives and are
explained inline.

## Contents

- [Layer map](#layer-map)
- [Tracked supporting projects](#tracked-supporting-projects)
- [The host and work-state boundaries](#the-host-and-work-state-boundaries)
- [Architectural boundary questions](#architectural-boundary-questions)
- [Scope notes](#scope-notes)

## Layer map

| Layer | What it owns | Core or supporting examples |
| --- | --- | --- |
| Agent cognition | Model/tool loop, context assembly, planning, routing | OpenCode, Pi, PydanticAI |
| Agent host and supervisor | Start, identity, environment, event stream, control, reconnect, failure supervision | T3 Code, OpenHands, Gas Town |
| Durable orchestration | Checkpoints, retries, durable timers, recovery, unknown outcomes, reconciliation | Temporal, LangGraph, Hatchet |
| Execution and isolation | Process, container, browser, or microVM execution boundary | E2B, CUA, Firecracker, gVisor |
| Authority and safety | Credentials, capabilities, approvals, effect policy, containment | Open Policy Agent, Cedar, Superagent |
| Work state and continuity | Projects, tasks, artifacts, decisions, dependencies, and outcomes across agents | Beads, Planning with Files |
| Personal agent OS and daemon | Long-lived identity, connections, schedules, notifications, memory | Hermes Agent, OpenClaw, ElizaOS |
| Memory and context | Recall, retrieval, knowledge graphs, and context assembly | Mem0, Graphiti, Cognee |
| Agent interaction and UI | Shared application state, human approvals, generative interfaces, and agent-user events | CopilotKit |
| Protocols and portable formats | Tool discovery, agent exchange, client control, skills, and repository instructions | MCP, A2A, ACP, AG-UI, Agent Skills, AGENTS.md |
| Integrations | Authentication, tool catalogs, and managed external actions | Composio |
| Model gateway | Provider routing, credentials, budgets, and fallback | LiteLLM |
| Observability | Traces, causality, metrics, and post-incident explanation | OpenTelemetry, Langfuse, Phoenix |
| Evaluation and assurance | Behavioral tests, red teaming, vulnerability scanning, and quality gates | Promptfoo, DeepEval |
| Deployment and compute | Placement, scaling, networking, and service lifecycle | Kubernetes, Modal |

## Tracked supporting projects

<!-- BEGIN GENERATED STACK CATALOG -->
### Work state and continuity

Durable projects, tasks, artifacts, decisions, dependencies, and outcomes that survive agent and session boundaries.

| Project                                                                 | Stars    | 30d | Role                                                                                                                                                                                         | License | Last push  |
| ----------------------------------------------------------------------- | -------: | --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| [Beads](https://github.com/gastownhall/beads)                           | ⭐ 26,868 | —   | Distributed graph issue tracker for agents with persistent tasks, dependencies, claims, and cross-machine synchronization. [evidence](https://github.com/gastownhall/beads#readme)           | MIT     | 2026-09-03 |
| [Planning with Files](https://github.com/OthmanAdi/planning-with-files) | ⭐ 26,619 | —   | Portable file-backed planning skill that preserves task plans, findings, and progress across context resets and crashes. [evidence](https://github.com/OthmanAdi/planning-with-files#readme) | MIT     | 2026-09-02 |

### Memory and context

Recall, retrieval, and context substrates; useful to agents but distinct from durable work state.

| Project                                                | Stars    | 30d | Role                                                                                                                                                                          | License    | Last push  |
| ------------------------------------------------------ | -------: | --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- |
| [Claude-Mem](https://github.com/thedotmack/claude-mem) | ⭐ 93,132 | —   | Cross-agent session capture and context-injection system backed by structured observations and local persistence. [evidence](https://github.com/thedotmack/claude-mem#readme) | Apache-2.0 | 2026-09-03 |
| [Cognee](https://github.com/topoteretes/cognee)        | ⭐ 30,453 | —   | Self-hosted agent memory and context engine built around knowledge graphs. [evidence](https://github.com/topoteretes/cognee#readme)                                           | Apache-2.0 | 2026-09-04 |
| [Graphiti](https://github.com/getzep/graphiti)         | ⭐ 30,579 | —   | Temporal knowledge-graph framework for continuously updated agent memory. [evidence](https://github.com/getzep/graphiti#readme)                                               | Apache-2.0 | 2026-09-03 |
| [Mem0](https://github.com/mem0ai/mem0)                 | ⭐ 64,683 | —   | Memory layer for retaining and retrieving information across agent interactions. [evidence](https://github.com/mem0ai/mem0#readme)                                            | Apache-2.0 | 2026-09-04 |

### Tool execution and integrations

Authentication, tool catalogs, and managed action execution across external applications.

| Project                                            | Stars    | 30d | Role                                                                                                                                      | License | Last push  |
| -------------------------------------------------- | -------: | --: | ----------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| [Composio](https://github.com/ComposioHQ/composio) | ⭐ 30,036 | —   | Tool catalog, authentication layer, and managed execution workbench for agents. [evidence](https://github.com/ComposioHQ/composio#readme) | MIT     | 2026-09-04 |

### Agent interaction and user interfaces

Application frameworks that connect agents to people, shared UI state, approvals, and generative interfaces.

| Project                                                | Stars    | 30d | Role                                                                                                                                                                                | License | Last push  |
| ------------------------------------------------------ | -------: | --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| [CopilotKit](https://github.com/CopilotKit/CopilotKit) | ⭐ 37,192 | —   | Full-stack framework for connecting agents to web, mobile, messaging, generative UI, shared state, and human approvals. [evidence](https://github.com/CopilotKit/CopilotKit#readme) | MIT     | 2026-09-03 |

### Protocols and portable formats

Open interfaces and repository formats for tools, agents, clients, applications, skills, and instructions.

| Project                                                                                | Stars    | 30d | Role                                                                                                                                                                                                                                                       | License                     | Last push  |
| -------------------------------------------------------------------------------------- | -------: | --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- | ---------- |
| [AG-UI](https://github.com/ag-ui-protocol/ag-ui)                                       | ⭐ 15,716 | —   | Event protocol connecting agent backends with user-facing applications. [evidence](https://github.com/ag-ui-protocol/ag-ui#readme)                                                                                                                         | MIT                         | 2026-09-03 |
| [Agent Client Protocol](https://github.com/agentclientprotocol/agent-client-protocol)  | ⭐ 4,148  | —   | Protocol for communication between code editors or clients and coding agents. [evidence](https://github.com/agentclientprotocol/agent-client-protocol#readme) **Scope note:** Official protocol boundary; tracked despite being below the core star floor. | Apache-2.0                  | 2026-09-03 |
| [Agent Skills](https://github.com/agentskills/agentskills)                             | ⭐ 25,018 | —   | Open specification for packaging portable instructions, scripts, and resources as agent skills. [evidence](https://github.com/agentskills/agentskills#readme)                                                                                              | Apache-2.0                  | 2026-08-09 |
| [Agent2Agent](https://github.com/a2aproject/A2A)                                       | ⭐ 25,622 | —   | Open protocol for communication and interoperability between opaque agent applications. [evidence](https://github.com/a2aproject/A2A#readme)                                                                                                               | Apache-2.0                  | 2026-09-01 |
| [AGENTS.md](https://github.com/agentsmd/agents.md)                                     | ⭐ 24,116 | —   | Open repository format for supplying durable project instructions to coding agents. [evidence](https://github.com/agentsmd/agents.md#readme)                                                                                                               | MIT                         | 2026-08-25 |
| [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol) | ⭐ 9,132  | —   | Open protocol for connecting AI applications to tools and context providers. [evidence](https://github.com/modelcontextprotocol/modelcontextprotocol#readme)                                                                                               | Apache-2.0 / MIT transition | 2026-09-04 |

### Authority and policy

General policy engines used to express credentials, capabilities, approvals, and effect boundaries.

| Project                                                       | Stars    | 30d | Role                                                                                                                                                                                                                            | License    | Last push  |
| ------------------------------------------------------------- | -------: | --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- |
| [Cedar](https://github.com/cedar-policy/cedar)                | ⭐ 1,706  | —   | Policy language and evaluation engine for fine-grained authorization. [evidence](https://github.com/cedar-policy/cedar#readme) **Scope note:** Mature authorization primitive; tracked despite being below the core star floor. | Apache-2.0 | 2026-09-03 |
| [Open Policy Agent](https://github.com/open-policy-agent/opa) | ⭐ 12,192 | —   | General-purpose policy engine for expressing and evaluating authorization decisions. [evidence](https://github.com/open-policy-agent/opa#readme)                                                                                | Apache-2.0 | 2026-09-04 |
| [Superagent](https://github.com/superagent-ai/superagent)     | ⭐ 6,726  | —   | Agent-safety SDK for prompt-injection blocking, sensitive-data redaction, repository threat scanning, and red-team scenarios. [evidence](https://github.com/superagent-ai/superagent#readme)                                    | MIT        | 2026-08-25 |

### Durable execution references

Durable execution systems kept as architectural references when licensing or scope excludes them from the core catalog.

| Project                                          | Stars   | 30d | Role                                                                                                                                                                                                                                      | License | Last push  |
| ------------------------------------------------ | ------: | --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ---------- |
| [Restate](https://github.com/restatedev/restate) | ⭐ 4,376 | —   | Durable execution system with state, retries, promises, and recovery semantics. [evidence](https://github.com/restatedev/restate#readme) **Scope note:** Architecturally relevant source-available reference; not an OSI-open core entry. | BSL-1.1 | 2026-09-04 |

### Observability

Tracing, causality, metrics, and post-incident explanation for agent behavior.

| Project                                                                                      | Stars    | 30d | Role                                                                                                                                                                                                                                                  | License     | Last push  |
| -------------------------------------------------------------------------------------------- | -------: | --: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| [Langfuse](https://github.com/langfuse/langfuse)                                             | ⭐ 34,187 | —   | LLM engineering platform for traces, evaluations, metrics, prompts, and datasets. [evidence](https://github.com/langfuse/langfuse#readme)                                                                                                             | MIT (core)  | 2026-09-04 |
| [OpenTelemetry Semantic Conventions](https://github.com/open-telemetry/semantic-conventions) | ⭐ 643    | —   | Standard semantic conventions, including GenAI and agent telemetry attributes. [evidence](https://github.com/open-telemetry/semantic-conventions#readme) **Scope note:** Official standard; repository stars do not represent OpenTelemetry adoption. | Apache-2.0  | 2026-09-04 |
| [Phoenix](https://github.com/Arize-ai/phoenix)                                               | ⭐ 11,319 | —   | Agent and LLM observability and evaluation platform built around traces and experiments. [evidence](https://github.com/Arize-ai/phoenix#readme)                                                                                                       | Elastic-2.0 | 2026-09-04 |

### Evaluation and assurance

Behavioral tests, red teaming, vulnerability scanning, and repeatable quality gates for agents.

| Project                                              | Stars    | 30d | Role                                                                                                                                                               | License    | Last push  |
| ---------------------------------------------------- | -------: | --: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- | ---------- |
| [DeepEval](https://github.com/confident-ai/deepeval) | ⭐ 18,097 | —   | Testing framework for repeatable LLM and agent evaluations with metrics, datasets, and CI integration. [evidence](https://github.com/confident-ai/deepeval#readme) | Apache-2.0 | 2026-09-03 |
| [Promptfoo](https://github.com/promptfoo/promptfoo)  | ⭐ 24,803 | —   | CLI and library for agent evaluations, red teaming, pentesting, and vulnerability scanning. [evidence](https://github.com/promptfoo/promptfoo#readme)              | MIT        | 2026-09-04 |

### Model gateways

Provider routing, credentials, budgets, fallback, and model-facing policy.

| Project                                       | Stars    | 30d | Role                                                                                                                                                | License    | Last push  |
| --------------------------------------------- | -------: | --: | --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- |
| [LiteLLM](https://github.com/BerriAI/litellm) | ⭐ 58,006 | —   | Model gateway and SDK for provider routing, budgets, load balancing, guardrails, and logging. [evidence](https://github.com/BerriAI/litellm#readme) | MIT (core) | 2026-09-04 |

### Deployment and compute

Placement, scaling, networking, and service lifecycle for agent workloads.

| Project                                                | Stars     | 30d | Role                                                                                                                                                                                                                                                                 | License    | Last push  |
| ------------------------------------------------------ | --------: | --: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- |
| [Kubernetes](https://github.com/kubernetes/kubernetes) | ⭐ 126,330 | —   | Container orchestration platform and reference implementation of desired-state reconciliation. [evidence](https://github.com/kubernetes/kubernetes#readme)                                                                                                           | Apache-2.0 | 2026-09-04 |
| [Modal](https://github.com/modal-labs/modal-client)    | ⭐ 512     | —   | Client and SDK for running containerized workloads on Modal's managed compute platform. [evidence](https://github.com/modal-labs/modal-client#readme) **Scope note:** Official SDK for a widely used managed platform; repository stars understate service adoption. | Apache-2.0 | 2026-09-03 |

### Execution primitives

Generic microVM and userspace-kernel isolation beneath agent-specific sandboxes.

| Project                                                           | Stars    | 30d | Role                                                                                                                                                       | License    | Last push  |
| ----------------------------------------------------------------- | -------: | --: | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- |
| [Firecracker](https://github.com/firecracker-microvm/firecracker) | ⭐ 36,523 | —   | MicroVM monitor used to provide lightweight hardware-virtualized workload isolation. [evidence](https://github.com/firecracker-microvm/firecracker#readme) | Apache-2.0 | 2026-09-04 |
| [gVisor](https://github.com/google/gvisor)                        | ⭐ 19,226 | —   | Userspace application kernel that adds an isolation boundary around containers. [evidence](https://github.com/google/gvisor#readme)                        | Apache-2.0 | 2026-09-04 |
<!-- END GENERATED STACK CATALOG -->

## The host and work-state boundaries

An **agent host or supervisor** sits around one or more replaceable agent brains.
It starts the agent, attaches identity and environment, streams structured events,
enforces control boundaries, reconnects clients, and reconciles failures. It is
not just a framework, workflow engine, or sandbox.

**Work state and continuity** is different from both hosting and memory. It owns
the durable objects of work—projects, tasks, artifacts, decisions, blockers,
accepted outcomes, and their causal history—across agents and sessions. A chat
transcript, vector store, or workflow checkpoint can support this layer without
replacing it. Beads is tracked here as a proven work-state implementation rather
than being forced into the runtime catalog.

## Architectural boundary questions

- Which component owns the agent's reasoning, and which owns whether the work actually happened?
- Does the host own execution safety, or only policy and delegation?
- Is state a transcript, workflow checkpoint, durable work object, or reconciled desired state?
- Who resolves an unknown outcome after a timeout or process crash?
- Which credentials can a task exercise, for how long, and with whose approval?
- Can an operator reconstruct why an action happened from traces and durable state?
- Can the agent brain be replaced without losing projects, decisions, artifacts, and history?

Kubernetes controller patterns remain useful even when Kubernetes itself is not
deployed: declare desired state, observe reality, and continuously reconcile the
difference. That pattern is often more useful for long-running work than treating
each prompt as an isolated request.

## Scope notes

The adjacent map does not imply endorsement or license equivalence. Restate is
included as a source-available architectural reference; its server uses BSL-1.1.
Generic primitives and official protocols can appear here below the core catalog's
5,000-star floor when their relevance and adoption are not represented accurately
by repository stars. Every exception is explicit in the generated table.

Source data: [`data/stack-projects.json`](data/stack-projects.json). Machine views:
[`data/stack-catalog.json`](data/stack-catalog.json) and
[`data/stack-catalog.csv`](data/stack-catalog.csv).
