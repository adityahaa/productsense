# Verification record

Review date: 10 November 2026 (Asia/Kolkata). This record describes the latest reviewed local source update; it does not represent live Gemini verification or a deployment test.

## Executed checks

- pytest tests/test_ledger_preview.py tests/test_traceability.py tests/test_static_sync.py -q: 13 passed. Covers selected-opportunity ledger retrieval before approval, no scope mutation, invalid choice, visitor ownership, traceability and generated static synchronization.
- pytest tests/test_research_view_and_csv.py tests/test_visitor_security.py tests/test_paper_consistency.py -q: 34 passed, 1 skipped. The skip is manuscript PDF compilation because pdflatex was unavailable.
- Frontend Node suites: safety 12 assertions passed; recovery 3 assertions passed; traceability suite passed.
- Historical integrity verifier completed successfully: 717 study-v2 checksums matched. Manuscript number audit: 65 matches, 0 mismatches, 9 informational notes.
- Browser inspection used the saved offline demo: feedback analysis, opportunities, pre-approval evidence ledger, explicit approval, offline PRD/review, traceability and local research view. This was not a Gemini call; saved output was labelled as an example.

## Limits

No new Gemini calls, study reruns, paper compilation, independent human scoring, or ProductSense cloud/deployment tests were performed. Structural checks do not establish semantic citation support or PRD quality. The optional research view depends on prepared local data that is deliberately excluded from the public app archive.

The checks above were run in the complete local extraction of ProductSense_Codex_Ready.zip. They are not all rerunnable from the privacy-filtered GitHub application archive because prepared research data and some full-project fixtures are intentionally excluded. This record is verification evidence, not a complete research reproduction bundle.
