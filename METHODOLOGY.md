# Methodology

Awesome Agent Runtimes is a curated decision map, not a GitHub search result.
This document makes its editorial choices auditable.

## Scope

A runtime owns at least one consequential part of agent execution:

- The model/tool loop and its approval boundaries.
- Persistent state, checkpointing, resumption, or scheduling.
- Multi-agent routing and coordination.
- Packaging, serving, or operating agent workloads.
- Isolated code, command, browser, or tool execution.

Model clients, prompt collections, memory databases, observability products,
MCP directories, and finished single-purpose agents are out of scope unless they
also own execution. Generic workflow or compute infrastructure is included only
when it is widely used as an agent substrate and materially changes reliability
or isolation.

## Inclusion bar

Inclusion requires all of the following:

1. A meaningful public implementation—not only a landing page or thin example.
2. Documentation sufficient to understand and run the relevant component.
3. Identifiable maintainers and a visible license or usage grant.
4. Evidence that the project owns a runtime responsibility in the scope above.
5. Either established adoption or a genuinely distinct, credible architecture.

Stars are a useful adoption signal, not a quality score. They can be inflated,
inherited after a repository pivot, or unrelated to the runtime component. Newer
projects with limited adoption receive extra scrutiny and are included sparingly.
There are no paid placements.

The operational floor for the core catalog is currently 5,000 GitHub stars,
180 days of public repository history, and activity within the last year. The
star floor is enforced automatically; age, maintenance quality, repository pivots,
and runtime scope are reviewed editorially. Crossing the floor makes a project
eligible for review, not entitled to inclusion.

## Classification

Projects are placed by their primary runtime responsibility:

- **Persistent agent runtimes** run long-lived assistants or autonomous workers.
- **Coding agent runtimes** own repository sessions, coding tools, and workspaces.
- **Browser and computer-use runtimes** own perception and action loops over user interfaces.
- **Agent and workflow runtimes** embed agent loops or control flow in applications.
- **Serving and control planes** package, deploy, expose, or operate agents.
- **Sandboxes and execution environments** isolate agent-controlled execution.
- **Durable execution substrates** provide recovery, retries, waits, and scheduling.

A project may span several layers. It appears once, in the category most useful
for comparing alternatives. Tags expose important secondary capabilities.

## Metadata and freshness

The daily workflow reads the GitHub repository API. Stars, forks, issue counts,
primary language, detected license, archive state, default branch, homepage, and
last push are snapshots rather than editorial claims. GitHub's primary-language
and license detection can be incomplete. A recent push indicates repository
activity, not necessarily a release or healthy maintenance.

Archived repositories remain only when historically important or when users may
still encounter them. They are marked automatically and should not be treated as
default recommendations.

## Descriptions and corrections

Descriptions are concise paraphrases of project READMEs and official
documentation. They avoid unverified performance, security, and production-readiness
claims. Maintainer corrections are welcome, but affiliation must be disclosed.
Category changes should explain which alternatives become easier to compare.

The catalog is reviewed through pull requests. Automated checks validate its
schema-like constraints, regenerate every derived artifact, and run the canonical
Awesome list linter before merge.

Coverage audits union the trusted lists in `data/sources.json`, normalize renamed
repositories, and create a popularity-and-freshness-filtered review queue. See
`DISCOVERY.md`; appearance in that queue is not an endorsement.
