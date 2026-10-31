# ProductSense

ProductSense turns small feedback samples into evidence-linked product opportunities and editable product requirements documents (PRDs). It supports explicit scope approval, review, revisions, version history, and Markdown/Word exports.

## Problem and scope

Feedback analysis often loses the connection between source reports and proposed requirements. This application retains feedback IDs through grouping, prioritization, and drafting. Its scores help navigate the supplied sample; they do not estimate market demand, revenue, or implementation effort.

The reviewed application is distributed in [ProductSense-reviewed-app-source.zip](ProductSense-reviewed-app-source.zip). Extract it before running commands. The archive contains the application, dependency lockfile, sample feedback, MIT license, and third-party notices. No verified public deployment is available.

## Implemented workflow

- Load the saved historical Excalidraw example or upload CSV feedback.
- Group evidence locally in demo mode or through optional Gemini generation.
- Compare opportunities, edit context, and approve scope before drafting.
- Review and edit a PRD, approve scoped revisions, inspect versions, and export documents.
- Keep application records and LangGraph checkpoints in local SQLite databases.

Saved templates are examples, not newly generated AI outputs. Historical issues do not demonstrate current missing features. The code validates evidence IDs, but generated requirements still need human review.

## Architecture and methodology

FastAPI serves a browser interface written in JavaScript/CSS. `app/workflow.py` implements a checkpointed LangGraph workflow with an approval interrupt; `app/changes.py` handles scoped revisions. `app/store.py` persists sessions and versions. `app/provider.py` bounds optional Gemini calls. Lexical grouping and prioritization provide the credential-free path. Visitor cookies restrict workspace access; export important work and retain your browser cookies.

## Run locally

Use Python 3.11 or 3.12. Clone, extract, and open PowerShell in the extracted folder:

```powershell
git clone https://github.com/adityahaa/productsense.git
cd productsense
Expand-Archive ProductSense-reviewed-app-source.zip -DestinationPath application
cd application
py -3.11 launch.py setup
py -3.11 launch.py check
py -3.11 launch.py start
```

Open http://127.0.0.1:8001. The saved demo requires no API key. Optional Gemini settings are documented in the archive's `.env.example`; copy it privately to `.env`. Do not submit confidential or customer-identifying feedback. Provider availability and quota are external prerequisites.

## Evidence and limitations

The archived-demo API smoke test passed without provider calls: evidence grouping, approval, PRD generation, history, and Markdown/Word exports. See the [technical report](docs/TECHNICAL_REPORT.md) and [verification log](docs/VERIFICATION.md). The sample is a small, attributed set of paraphrased public reports, not a representative evaluation dataset. No controlled comparison, measured PRD-quality score, publication, or business impact is claimed. PostgreSQL integration and cloud deployment are not established by this source release. The launcher's `review` command references an author-evaluation module absent from the public archive; use `start` for the public application.

## Attribution

Maintained in Aditya Hambire's repository. Preserve the archive's MIT `LICENSE`, `NOTICE.md`, and feedback source URLs. Third-party reports and dependencies retain their authors' rights. Git history remains the record of repository contributions.
