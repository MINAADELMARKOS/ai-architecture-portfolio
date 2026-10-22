# ADR-01 — Campaign Copy: Managed LLM API vs Self-Hosted vs Templates
**Purpose:** Decide whether generative AI is needed for drafting a debit-card reactivation campaign. **Status:** Proposed; vendor approval and testing outstanding. **Owner:** AI/Marketing Architecture.

**Context:** The bank needs multilingual campaign text, but customers must not receive unreviewed offers. No personal customer information is necessary to draft generic copy.

| Option | Pros | Cons |
|---|---|---|
| A. Approved fixed templates only | Low cost, predictable, bank-controlled wording | Slow copy variation and manual workload |
| B. Managed LLM API behind bank gateway | Quick implementation, flexible Arabic/English draft variants | Third-party/vendor risk, variable charges, evaluation requirements |
| C. Self-hosted model | Direct infrastructure/control of inference | GPU investment, specialist maintenance, capacity management |

**Decision:** B *conditional on bank supplier, security and privacy approval*. Only generic segment descriptions and approved product facts may be submitted; no names, card numbers, identifiable records, balances or transaction data. Model output is draft-only and requires marketing/compliance approval. **Fallback:** A if provider is unavailable, unacceptable or not approved.

**Consequences:** Faster content drafting with limited external exposure; still requires legal/vendor assessments, text evaluation, human review and audit trail. No model may trigger send/payment/account operations.

**When to revisit:** Provider approval denied, cost exceeds approved budget, quality is inadequate or volume makes private inference economical.
