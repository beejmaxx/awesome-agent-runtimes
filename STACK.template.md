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
{{STACK_CATALOG}}
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
