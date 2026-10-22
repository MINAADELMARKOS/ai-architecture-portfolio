# ADR-03 — Daily Batch vs Real-Time Streaming
**Purpose:** Choose processing freshness appropriate to debit-card inactivity. **Status:** Proposed. **Owner:** Data Engineering.

**Context:** Being inactive for 30 days changes slowly; immediate millisecond updates are unlikely to affect this marketing action. The final send must use current consent and eligibility.

| Option | Pros | Cons |
|---|---|---|
| A. Daily batch | Low cost, simpler recovery, easy schedule | Inactivity score can be up to one day old |
| B. Streaming/event processing | Fresher response to transactions | Kafka/stream workers, replay/duplicate handling and 24/7 monitoring |
| C. Hybrid daily batch + near-real-time triggers | Balance freshness and responsiveness | More components and cross-system coordination |

**Decision:** A for the initial pilot. A nightly job computes debit-card inactivity candidates and selects approved offers. A scheduled campaign worker must **recheck latest consent, customer suppression, offer validity and duplicate-send status immediately before sending**.

**Consequences:** Predictable cost and smaller MVP. Slower reaction to new transactions is mitigated by final eligibility checks. **Revisit:** controlled experiments show significant incremental lift from faster intervention.
