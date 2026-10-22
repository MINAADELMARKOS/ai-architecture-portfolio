# ADR-02 — Vector Database for the MVP
**Purpose:** Avoid introducing a storage service the banking use case does not need. **Status:** Proposed. **Owner:** Data Architecture.

**Context:** The MVP scores card inactivity and chooses among an approved, structured list of offers. It does not require natural-language retrieval of thousands of documents.

| Option | Pros | Cons |
|---|---|---|
| A. SQL + approved templates, no vectors | Simple controls, few dependencies, easy audit | No semantic document search |
| B. PostgreSQL + pgvector | Existing relational metadata can be combined with embeddings | Embedding/index management, tuning and evaluation |
| C. Dedicated vector search DB | Dedicated semantic-search capability and scaling options | New operations, governance and cost |

**Decision:** A. Use relational offer eligibility rules and approved copy templates. No vector database is required for the MVP. This is a deliberate architecture decision, not a missing component.

**Consequences:** Less infrastructure and a clearer audit path; limited semantic search. **Revisit:** a future approved use case requires RAG over unstructured product policy documents, with measured retrieval quality, access filtering and cost.
