# Architecture Review Board — Banking Reactivation
**Purpose:** A lightweight review gate before any real-customer pilot. Record **PASS / FAIL / PENDING**, the named reviewer, and an evidence link; do not treat a promise to build as evidence.

| Area | Required question | Evidence / reviewer | Status |
|---|---|---|---|
| Security | Is campaign service limited to approved read-only analytics and approved send gateway? Does AI lack direct-send and account-writing tools? | IAM permission matrix, threat model, negative tests / Security | PENDING |
| Privacy / PDPL | Are direct-marketing purpose and consent documented? Is opt-out enforced before each message, data minimized, retention defined, and supplier/location reviewed? | Consent test, data inventory, DPO assessment / Privacy | PENDING |
| Evaluation | Does a randomized holdout show incremental 30-day debit-card activation? Is 90-day value net of rewards, complaints and opt-outs? Is generated Arabic/English copy reviewed? | Experiment plan, test set, human review records / Data Science + Marketing | PENDING |
| Cost | Are runtime costs, campaign spend, human review and cost per incremental activation within budget? | Finance model, cloud budget alerts / Finance | PENDING |
| Human oversight | Is each campaign copy and audience approved by authorized marketing/compliance reviewers with a kill switch and immutable audit? | Workflow demo and audit trail / Marketing + Compliance | PENDING |

**ARB outcome:** Not yet approved for real customer use. This document proposes review criteria; actual bank owners must supply evidence and sign off. Regulatory applicability depends on the bank and exact processing activity.

**Official references:** SDAIA PDPL Implementing Regulation Article 29: https://sdaia.gov.sa/en/SDAIA/about/Documents/ImplementingRegulation.pdf ; SAMA Cyber Security Framework: https://rulebook.sama.gov.sa/en/cyber-security-framework-2
