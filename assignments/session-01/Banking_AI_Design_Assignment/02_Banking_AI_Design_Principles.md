# Architecture Principles — Banking Debit-Card Reactivation
**Purpose of this file:** Explain the four durable design rules, the business outcomes they support, and how to verify them. The one-page wiki contains their concise submission versions.

| ID | Principle | Business goal | Practical implementation | Evidence / verification |
|---|---|---|---|---|
| P1 | Purpose and consent before marketing | Protect trust; reduce unlawful contact | Consent and opt-out source is authoritative; suppress customer at send time; keep only approved transaction-derived features | Pre-send authorization tests, consent logs, DPO-approved data map |
| P2 | Humans authorize campaigns | Avoid inappropriate products and brand risk | LLM generates generic text only; marketing/compliance sign off on audience and copy; AI has no send or transaction-write permission | Approval audit trail; deny unauthorized tool-action tests |
| P3 | Trace and measure outcomes | Increase incremental reactivation, not just messages sent | Holdout control; campaign, offer, model, approval and response identifiers | Experiment report, sample trace, opt-out and complaint metrics |
| P4 | Simplicity and reliable fallback | Deliver value quickly without costly AI infra | Daily feature refresh and SQL eligibility; approved templates when LLM unavailable; no runtime LLM in customer journey | Dependency diagram, cost test, batch rerun and fallback exercise |

## Why these four?
One principle addresses lawful customer treatment; one controls automation; one proves business gain; one keeps the MVP maintainable. They are intentionally more durable than vendor choices.

## Important limits
Not all inactive customers are appropriate for marketing. Exclude customers without valid direct-marketing consent or who fail marketing eligibility, including any mandatory suppression rules. Do not use protected or sensitive personal data for targeting. Refer actual Saudi PDPL interpretation and bank-specific SAMA obligations to the bank's Legal/DPO and Security teams.
