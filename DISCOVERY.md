# Discovery and Coverage Audits

The catalog is intentionally curated, but its coverage should be measurable.
Discovery therefore uses a repeatable funnel rather than ad hoc GitHub search.

## Funnel

1. Take the union of repository links from the trusted lists in
   [`data/sources.json`](data/sources.json).
2. Run boundary-specific GitHub searches from
   [`data/searches.json`](data/searches.json), so new categories do not depend on
   appearing in an existing awesome list.
3. Normalize renamed and redirected repositories through the GitHub API.
4. Remove projects already cataloged, watched, excluded, forked, or archived.
5. Require repeated appearance across list and search signals.
6. Apply adoption, age, and freshness floors.
7. Manually verify scope, architecture, license, maintainership, and category.

The automated stages produce a review queue, not automatic additions. Repetition
across lists can reflect copying, overlapping searches are not independent
endorsements, and stars can reflect hype or an earlier project that occupied the
same repository.

## Run an audit

```bash
GITHUB_TOKEN=... python3 scripts/discover.py
```

Defaults require at least 5,000 stars, two discovery signals, activity within the
last year, at least 180 days of public history, and a non-archived, non-fork
repository. Signals include trusted-list mentions and boundary-specific searches.
The generated
[`data/candidates.json`](data/candidates.json) file clearly marks candidates as
unreviewed.

Useful stricter passes:

```bash
# Consensus candidates with substantial adoption
python3 scripts/discover.py --min-stars 10000 --min-sources 3

# Emerging architectures for an occasional manual review
python3 scripts/discover.py --min-stars 2000 --min-sources 2 --max-stale-days 180
```

## Manual review questions

- Which ownership boundary does the project actually implement: cognition,
  supervision, recovery, isolation, authority, continuity, or infrastructure?
- Does it own durable work objects, or only transcripts, checkpoints, or memory?
- Is that component usable in the public repository?
- Is it an alternative to an existing entry, or merely an integration?
- Are deployment, persistence, isolation, and license claims supported by primary
  documentation?
- Does adoption belong to the current runtime, rather than a previous repository
  identity?
- Would removing this entry leave a meaningful architecture or operational model
  unrepresented?

Projects that fail runtime scope but matter to production stacks can be documented
in [`STACK.md`](STACK.md) without inflating the core catalog.
