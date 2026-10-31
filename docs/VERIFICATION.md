# Verification record

Review date: 1 November 2026 (Asia/Kolkata).

- Passed: `python -m pytest tests -q`: 1 integration smoke test (4.24 seconds), with no provider calls. It extracts the actual distributed ZIP into a temporary directory and checks health, demo creation, premature approval rejection, analysis/evidence coverage, approval, PRD content, zero provider calls, version history, Markdown/DOCX exports, and an unknown workspace.
- Environment: Windows, Python 3.11.9, pytest 8.3.5, FastAPI 0.162.0, LangGraph 1.2.19, langgraph-checkpoint-sqlite 3.1.3, python-docx 1.2.0, httpx 0.28.1. These were installed for verification from application requirement ranges, not from the archive lockfile.
- Initial sandbox execution stalled creating Python's internal socket pair; the same test passed outside that sandbox. No application correction was needed.
- Not verified: browser interaction, optional Gemini, launcher lockfile installation, cloud deployment, or PostgreSQL. No quality benchmark is claimed.

To repeat: extract the application as instructed in the root README, install its requirements in an isolated environment, then run `python -m pytest tests -q` from the repository root using that environment. The test itself extracts the source and uses temporary runtime storage. Do not set PRODUCTSENSE_CLOUD=true for the local smoke test.
