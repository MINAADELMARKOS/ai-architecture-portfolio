# Session 02 — Building blocks

The [editable diagram source](../diagrams/knowledge-assistant.mmd) and [SVG export](../diagrams/knowledge-assistant.svg) show the proposed first version.

## Request path

1. An employee signs in through company SSO and sends a question to the assistant UI.
2. An API checks the session, applies rate limits, and passes the user's identity to the orchestration layer.
3. Retrieval searches an index of approved documents and filters results by the user's permissions.
4. The orchestrator builds a bounded prompt from permitted passages and asks a hosted model for an answer.
5. A response gate checks citation coverage and handles refusal or escalation. The UI displays the answer with links to the source versions.

## Document path

Document owners approve policies in the source system. An ingestion job imports changes, records version and owner metadata, extracts text, and updates the search index. Removed or newly restricted documents must stop being retrievable; that behavior needs explicit tests.

## Cross-cutting controls

- **Identity and authorization:** use SSO identity and source permissions at query time.
- **Data minimization:** send only relevant approved passages to the model; keep sensitive sources out of the initial index.
- **Observability:** record request IDs, retrieval results, citation checks, errors, and costs without storing more employee content than policy allows.
- **Evaluation:** maintain representative questions, expected source documents, permission cases, and abstention cases.
- **Resilience:** timeouts, bounded retries, and a graceful route to the source document or human owner.

## Risks to resolve before a pilot

| Risk | Design response |
| --- | --- |
| Hallucinated or stale answer | Require citations, show version metadata, evaluate against approved documents, and abstain when evidence is weak |
| Unauthorized disclosure | Filter at retrieval time, test permission changes, and avoid relying on the model to enforce access |
| Prompt injection in documents | Treat retrieved text as untrusted data, separate instructions from source content, and test adversarial documents |
| Unexpected cost or latency | Limit retrieved context, monitor usage, and set budgets and timeouts |

The components are conceptual. Vendor and deployment choices remain open except for the provisional model-hosting decision in [ADR 0001](../adr/0001-model-hosting.md).
