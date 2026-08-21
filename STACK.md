# Agent Stack Layers

The core catalog stays narrow: every entry must own agent execution. This map
shows the adjacent production layers that answer a different question—who owns
truth, authority, recovery, connectivity, and explanation when an agent acts?

## Layer map

| Layer | Runtime responsibility | Proven references |
| --- | --- | --- |
| Agent harness | Model/tool loop, context, planning, approvals | [Core runtime catalog](README.md#catalog) |
| Runtime operations | Sessions, workers, identity, deployment, control surfaces | [T3 Code](https://github.com/pingdotgg/t3code), [OpenHands](https://github.com/OpenHands/OpenHands), [Cloudflare Agents](https://github.com/cloudflare/agents) |
| Execution environment | Process, container, browser, or microVM isolation | [E2B](https://github.com/e2b-dev/E2B), [Daytona](https://github.com/daytonaio/daytona), [Firecracker](https://github.com/firecracker-microvm/firecracker), [gVisor](https://github.com/google/gvisor) |
| Tool protocol | Tool discovery and agent-to-agent interoperability | [Model Context Protocol](https://github.com/modelcontextprotocol/modelcontextprotocol), [MCP Registry](https://github.com/modelcontextprotocol/registry), [A2A](https://github.com/a2aproject/A2A) |
| Authority and security | Policy, credentials, approvals, and containment | [NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell), [Open Policy Agent](https://github.com/open-policy-agent/opa), [Cedar](https://github.com/cedar-policy/cedar) |
| Durable workflow | Retries, durable timers, recovery, and reconciliation | [Temporal](https://github.com/temporalio/temporal), [Restate](https://github.com/restatedev/restate), [DBOS](https://github.com/dbos-inc/dbos-transact-py) |
| User and project continuity | Identity, memory, schedules, notifications, and long-lived state | [Hermes Agent](https://github.com/NousResearch/hermes-agent), [OpenClaw](https://github.com/openclaw/openclaw), [Letta](https://github.com/letta-ai/letta) |
| Observability | Traces, evaluations, causality, and post-incident explanation | [OpenTelemetry semantic conventions](https://github.com/open-telemetry/semantic-conventions), [Langfuse](https://github.com/langfuse/langfuse), [Phoenix](https://github.com/Arize-ai/phoenix) |

## Architectural boundary questions

Use the map to ask ownership questions, not to assemble every product at once:

- Does the agent runtime own execution safety, or only policy and delegation?
- Is state a conversation transcript, a durable object, or reconciled desired state?
- Who resolves an unknown outcome after a timeout or process crash?
- Which credentials can a task exercise, for how long, and with whose approval?
- Can an operator reconstruct why an action happened from traces and durable state?
- Which state deserves to survive a user session, machine restart, or deployment?

Kubernetes controller patterns are an important conceptual reference even when
Kubernetes itself is not in the stack: declare desired state, observe reality,
and continuously reconcile the difference. That pattern is often more useful for
long-running agents than treating each prompt as an isolated request.

## Scope notes

This page does not imply endorsement or license equivalence. In particular,
Restate's server uses the Business Source License rather than an OSI-approved
open-source license. Generic primitives such as Firecracker, gVisor, OPA, and
Cedar appear here as architectural references, not core agent-runtime entries.
