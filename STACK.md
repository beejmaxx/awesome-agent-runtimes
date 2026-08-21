# Agent Stack Ownership Map

"Agent runtime" is overloaded. Frameworks, supervisors, sandboxes, workflow
engines, protocols, and memory systems all appear under that label, even though
they own different parts of the stack. This map asks two sharper questions:
**who owns the intelligence, and who owns operational truth when it acts?**

The core catalog groups comparable implementations. This page also includes
adjacent layers and conceptual patterns that matter architecturally but are not
themselves agent runtimes.

## Layer map

| Layer | What it owns | Proven references |
| --- | --- | --- |
| Agent cognition | Model/tool loop, context assembly, planning, routing | [OpenCode](https://github.com/anomalyco/opencode), [Pi](https://github.com/earendil-works/pi), [PydanticAI](https://github.com/pydantic/pydantic-ai) |
| Agent host and supervisor | Start, identity, environment, event stream, control, reconnect, failure supervision | [T3 Code](https://github.com/pingdotgg/t3code), [OpenHands](https://github.com/OpenHands/OpenHands), [Cloudflare Agents](https://github.com/cloudflare/agents) |
| Durable orchestration | Checkpoints, retries, durable timers, recovery, unknown outcomes, reconciliation | [Temporal](https://github.com/temporalio/temporal), [LangGraph](https://github.com/langchain-ai/langgraph), [Hatchet](https://github.com/hatchet-dev/hatchet), [Restate](https://github.com/restatedev/restate) |
| Execution and isolation | Process, container, browser, or microVM execution boundary | [E2B](https://github.com/e2b-dev/E2B), [Daytona](https://github.com/daytonaio/daytona), [Firecracker](https://github.com/firecracker-microvm/firecracker), [gVisor](https://github.com/google/gvisor) |
| Authority and safety | Credentials, capabilities, approvals, effect policy, containment | [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell), [Open Policy Agent](https://github.com/open-policy-agent/opa), [Cedar](https://github.com/cedar-policy/cedar) |
| Work state and continuity | Projects, tasks, artifacts, decisions, context, and outcomes across heterogeneous agents | **Ecosystem gap:** no vendor-neutral project currently clears this catalog's adoption and maturity bar |
| Personal agent OS and daemon | Long-lived identity, connections, schedules, notifications, memory | [Hermes Agent](https://github.com/NousResearch/hermes-agent), [OpenClaw](https://github.com/openclaw/openclaw), [ElizaOS](https://github.com/elizaOS/eliza) |
| Tool and agent protocol | Tool discovery, transport, and agent/client interoperability | [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol), [A2A](https://github.com/a2aproject/A2A), [Agent Client Protocol](https://github.com/agentclientprotocol/agent-client-protocol) |
| Model gateway | Provider routing, credentials, budgets, and fallback | [LiteLLM](https://github.com/BerriAI/litellm) |
| Observability | Traces, evaluations, causality, and post-incident explanation | [OpenTelemetry semantic conventions](https://github.com/open-telemetry/semantic-conventions), [Langfuse](https://github.com/langfuse/langfuse), [Phoenix](https://github.com/Arize-ai/phoenix) |
| Deployment and compute | Placement, scaling, networking, and service lifecycle | [Kubernetes](https://github.com/kubernetes/kubernetes), [Modal](https://github.com/modal-labs/modal-client) |

## The host and work-state gaps

An **agent host or supervisor** sits around one or more replaceable agent brains.
It starts the agent, attaches identity and environment, streams structured events,
enforces control boundaries, reconnects clients, and reconciles failures. It is
not just a framework, workflow engine, or sandbox.

**Work state and continuity** is different from both hosting and memory. It owns
the durable objects of work—projects, tasks, artifacts, decisions, blockers,
accepted outcomes, and their causal history—across agents and sessions. A chat
transcript, vector store, or checkpoint can support this layer without replacing
it. The absence of a proven neutral implementation is recorded as a gap instead
of being filled with a low-adoption repository.

## Architectural boundary questions

Use the map to ask ownership questions, not to assemble every product at once:

- Which component owns the agent's reasoning, and which component owns whether the work actually happened?
- Does the host own execution safety, or only policy and delegation?
- Is state a conversation transcript, a workflow checkpoint, a durable work object, or reconciled desired state?
- Who resolves an unknown outcome after a timeout or process crash?
- Which credentials can a task exercise, for how long, and with whose approval?
- Can an operator reconstruct why an action happened from traces and durable state?
- Can the agent brain be replaced without losing projects, decisions, artifacts, and history?

Kubernetes controller patterns are an important conceptual reference even when
Kubernetes itself is not deployed: declare desired state, observe reality, and
continuously reconcile the difference. That pattern is often more useful for
long-running work than treating each prompt as an isolated request.

## Scope notes

This page does not imply endorsement or license equivalence. In particular,
Restate's server uses the Business Source License rather than an OSI-approved
open-source license. Generic primitives such as Firecracker, gVisor, OPA,
Cedar, Kubernetes, and OpenTelemetry appear as architectural references, not
core agent-runtime entries. Agent Client Protocol currently falls below the
core catalog's 5,000-star floor and is listed only because it defines a protocol
boundary, not as a popularity-qualified runtime.
