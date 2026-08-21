# Contributing

Thanks for helping make the agent-runtime landscape easier to navigate.

## Inclusion criteria

A project should:

- Own a meaningful part of agent execution: cognition, lifecycle supervision,
  durable orchestration, long-lived continuity, serving, or isolated execution.
- Have a public repository, documentation, and an identifiable license.
- Be usable beyond a single demo or narrowly finished agent application.
- Show ongoing maintenance, or be historically important and clearly marked as
  archived.
- Add a distinct implementation or operational tradeoff to the catalog.
- Link primary documentation supporting the description and ownership boundary.

Established adoption is required. Star count is not sufficient for inclusion;
projects must also show a distinct architecture, credible maintainership, real
usability, and evidence for their claimed ownership boundary. Paid products are
eligible only when the linked repository contains a meaningful open-source
runtime component. See `METHODOLOGY.md` for the full editorial policy.

Active core entries must clear the current 5,000-star, 180-day-age, one-year
activity, and license-visibility gates. These are noise-control thresholds, not
rankings or automatic acceptance rules. Archived projects belong in the
historical category. Adjacent infrastructure belongs in `data/stack-projects.json`.

## Add or update a project

1. Edit `data/projects.json`; do not edit `README.md`, `TAGS.md`, `llms.txt`, or
   the generated `data/catalog.*` exports.
2. Keep the description factual, concise, and free of marketing superlatives.
3. Choose the layer that owns the project's primary runtime responsibility.
4. Use one to four short tags and only the documented deployment values.
5. Run `python3 scripts/update.py` to refresh metadata and every generated view.
6. Run `python3 scripts/update.py --check` before opening a pull request.

Projects that are promising but not mature enough belong in
`data/watchlist.json`. Notable rejections belong in `data/exclusions.json` with a
concrete condition under which maintainers should reconsider them.

Please keep entries alphabetic within their category conceptually; the renderer
sorts them automatically. A pull request should add one project or one coherent
group of closely related corrections.

## Pull request evidence

Link to documentation supporting the runtime behavior and deployment modes you
claim. Disclose affiliations with a submitted project. Maintainers may recategorize,
rewrite, or decline entries to preserve the scope and signal-to-noise ratio.

## Taxonomy changes

Open an issue before making broad category or schema changes. Explain which
existing projects are hard to classify and how the change improves comparisons.
