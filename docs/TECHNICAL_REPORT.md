# ProductSense technical report

## Product and workflow

ProductSense is a local FastAPI application with a browser interface, LangGraph orchestration, SQLite session/version persistence, and optional Gemini generation. The saved offline path works without an API key. Its workflow groups feedback, presents opportunities for review, requires explicit scope approval, drafts and reviews a PRD, and supports editing, scoped revisions, version history and Markdown/Word/CSV exports.

Before approval, a user can open a selected opportunity's evidence ledger. It separates reported feedback, user constraints, open questions and candidate warnings; opening it does not select/approve scope or create a PRD. The Evidence & Review screen exposes requirement-to-evidence and requirement-to-acceptance-criteria links, review flags and version comparison. An optional dataset/saved-run view is mounted only when PRODUCTSENSE_RESEARCH_MODE=1; public-demo mode denies research routes. The static folder is canonical and scripts/build_static.py rebuilds public assets.

## Evidence and safeguards

Feedback, context and corrections are untrusted input. User-visible strings are escaped. Existing visitor ownership, CSV validation, request limits, approval checks and saved-demo controls remain in place. The archive contains source code, a small attributed/paraphrased application demo, dependency files, MIT license and attribution notices. It excludes research datasets and raw issue responses, private ledgers/runtime databases, author drafts and credentials.

Evidence IDs, acceptance links and automated warnings provide structural review support only. They cannot establish that a citation semantically entails a requirement. Historical issue reports can be outdated and should not be read as proof of a current product gap. Human review is required; no automated accuracy percentage is claimed.

## Research and claims

An earlier exploratory study had 28 evaluation slots, including duplicates, and 18 unique PRD texts. Its limited same-model assessments do not establish agentic workflow superiority. A separate 22-case, seven-product dataset is prepared; the new live v3 comparison has not been run. The offline seeded-defect study found target checks missed wrong-but-valid citation swaps and negated requirements; the checker was amended after those observations, so the result is not a held-out real-world accuracy estimate. This source update did not rerun research or call Gemini.

## Verification summary — 10 November 2026

The updated local workflow was exercised in the browser with the saved demo: feedback analysis, opportunities, pre-approval ledger, explicit approval, offline PRD/review, traceability and local research view. Automated tests passed for ledger/traceability/static behavior (13 tests), selected app/security/research/paper behavior (34 passed, 1 skipped because pdflatex was unavailable), and frontend safety/recovery/traceability (12 and 3 assertions plus the traceability suite). Historical integrity verified 717 study-v2 checksums. The manuscript number audit reported 65 matches, 0 mismatches and 9 informational notes. No paper compilation is claimed. The complete command/output checkpoint is in [verification record](VERIFICATION.md).

These results establish only the tested local implementation and structural behavior. They do not establish live Gemini behavior for this update, independent reviewer agreement, semantic citation correctness, deployment readiness, user time savings or product/business impact.
