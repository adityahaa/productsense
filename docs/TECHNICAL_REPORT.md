# ProductSense technical report

## Problem and system

The system converts supplied feedback into reviewable product proposals while retaining evidence IDs. It combines FastAPI, a static browser client, SQLite session/version storage, and checkpointed LangGraph execution. Analysis and prioritization lead to a human approval interrupt, PRD drafting, review, at most one automatic model revision, and completion. Separate revision routes require scope approval.

## Data and approach

The archive includes demo CSV/JSON and saved outputs. Excalidraw examples paraphrase historical public issues and preserve source links; see archived NOTICE.md. They are not unique-user counts or current product requirements. Demo grouping uses topic/keyword rules; priority uses sample and lexical signals rather than estimated business impact. Gemini is optional and evidence IDs are checked for omissions, duplicates, and invention. Saved-template mode is a deterministic demonstration path, not an AI baseline quality experiment.

## Evaluation methodology and limitations

Verify the saved-demo lifecycle without credentials: create session, analyze, inspect evidence coverage, approve an opportunity, poll until completion, inspect PRD, and export Markdown/Word. Restart with the same runtime directory to check persistence. Check unknown IDs and missing approvals as negative cases. Functional success does not measure factuality, usefulness, or stakeholder agreement. No labeled PRD benchmark, inter-rater study, provider comparison, or measured business result is supplied.

## Reproduction

Use the root README extraction and launcher commands. Dependencies are specified in the archive, with a lockfile for the launcher. Preserve .env and runtime databases privately. The archived launcher also exposes a review command referencing an absent evaluation.author_review module; that path is not part of the reproducible public release. Cloud/PostgreSQL integration is not demonstrated here. See [verification record](VERIFICATION.md) for this review's executed checks.
