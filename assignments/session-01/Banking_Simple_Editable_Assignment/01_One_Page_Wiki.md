# Banking AI Governance — Debit Card Customer Reactivation
*Session 1 | One-page wiki | Proposed design, not an implemented banking system*

**Business challenge.** Debit-card customers inactive for 30+ days who stop transacting reduce fee contribution and may move everyday spending elsewhere. Today, the bank uses generic promotions with slow manual preparation. **Goal:** reactivate eligible inactive debit-card users through suitable, consented offers at controlled cost. **Non-goals:** credit decisions, lending, payments execution, changing accounts or autonomous message sending.

**Measurable value (ILLUSTRATIVE; not actual bank data).** A randomized pilot treats 50,000 eligible, consenting customers (with a separate control group). Baseline 30-day reactivation=4.0%; treatment=5.2%; *incremental* reactivations=50,000×(0.052−0.040)=**600**. Assumed 90-day net contribution per incremental reactivated user=**SAR 45** → **SAR 27,000**. Saved campaign work=25 h×SAR 160=**SAR 4,000**. Incremental platform/campaign operating cost=**SAR 9,000**. **Modeled net benefit = SAR 22,000 per monthly cohort** (before fixed build cost). Validate all assumptions with Finance and randomized control tests; avoid double-counting repeat customers.

## Architecture principles (purpose: durable rules, each tied to a goal)
- **P1 — Purpose & consent before marketing.** *Goal: trust, lawful reach.* Use purpose-restricted features and validate current consent/opt-out before each send; suppress ineligible accounts.
- **P2 — People authorize campaigns.** *Goal: prevent harmful or misleading offers.* AI may draft generic text; marketing and compliance approve final copy and segment. No AI access to bank transaction/write APIs.
- **P3 — Trace and measure outcomes.** *Goal: measurable incremental activation.* Record campaign/offer/model versions, eligibility reason, approvals, deliveries, opt-outs and 30-day outcomes; compare against a randomized control group.
- **P4 — Simplest reliable solution.** *Goal: quick, affordable delivery.* Daily batch scoring, deterministic offer rules, and preapproved templates as fallback; do not use LLMs in customer-facing decision paths.

## Three ADRs (purpose: document alternatives, decision and trade-off)
**ADR-01 | Campaign text: templates vs managed LLM vs self-hosted.** Templates = safe/cheap but rigid; managed API = fast setup but supplier/data-processing risks; self-host = greater control but GPU/operations cost. **Decision:** Use approved managed LLM **only for generic, non-personal campaign drafts**, subject to bank/vendor approval; otherwise use templates. All drafts require human approval. *Revisit:* approval fails, quality tests fail, or managed cost exceeds budget.

**ADR-02 | Semantic vector search: none vs pgvector vs dedicated DB.** No vector store = simplest but no semantic retrieval; pgvector = reuses SQL infrastructure but adds indexing/tuning; dedicated DB = specialized scale but extra operations. **Decision:** **No vector DB in MVP**—offers and rules are structured SQL and approved templates. *Revisit:* unstructured policy documents become a validated retrieval requirement.

**ADR-03 | Daily batch vs streaming vs hybrid.** Daily batch = low-cost but 24h scoring lag; streaming = fresher but complex; hybrid = balances them with extra components. **Decision:** **Daily batch** inactivity detection and scheduled campaign sending; recheck consent and eligibility immediately before dispatch. *Revisit:* experiment establishes that faster intervention materially lifts activation.

## ARB checklist (purpose: evidence-based approval; record PASS / FAIL / PENDING)
- **Security:** Bank SSO/RBAC; least-privilege analytics; no write access for AI; tested audit trail and secret handling.
- **Privacy — Saudi PDPL:** documented marketing purpose/consent; opt-out honored; data minimization; retention and location/vendor transfer assessment; DPO sign-off.
- **Evals:** randomized 30-day reactivation uplift; 90-day financial contribution; Arabic/English copy checks; complaints/opt-outs tracked; no unsupported claims.
- **Cost:** cost per incremental reactivation, monthly spending limit and Finance-validated 90-day contribution; compare with manual baseline.
- **Human oversight:** marketing + compliance sign-off before dispatch; versioned approval, kill switch and owner for incidents.

**Optional automated guardrail (purpose: prevent unsafe configuration).** CI checks `architecture_policy.json` against P1/P2/P4: marketing consent gate enabled; AI direct-send disabled; PII in LLM prompts disabled; review required; batch mode selected. Fail deployment on violations. **Human ARB review remains mandatory.**

**Diagram key:** Bank data → daily detection → eligible customer/offer list; marketer → optional AI draft → human approval; both reach a final consent+eligibility gate → messages → measured outcomes. All metrics above are hypotheses awaiting a banking pilot.

**Regulatory references:** Saudi PDPL implementing regulations (SDAIA): https://dgp.sdaia.gov.sa/ ; SAMA Cyber Security Framework: https://rulebook.sama.gov.sa/en/cyber-security-framework-2
