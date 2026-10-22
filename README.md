# AI Architecture Portfolio

This repository tracks the design of a **read-only internal knowledge assistant** for a fictional mid-sized company. Employees ask questions about HR and IT policies; the assistant retrieves approved documents, answers with citations, and directs uncertain or sensitive requests to a human owner.

The scenario is illustrative. It is a design exercise, not a deployed service or a claim about any real company's data.

## Starting assumptions

| Area | Working assumption |
| --- | --- |
| Users | About 500 employees with company single sign-on (SSO) |
| Sources | Versioned, approved HR and IT policy documents |
| Access | Answers respect each employee's document permissions |
| Data | No payroll, medical records, or customer data in the initial scope |
| Behavior | Read-only answers with source links; no autonomous changes to company systems |
| Quality | The assistant can abstain and route questions to a document owner |

These assumptions should be validated with stakeholders before implementation. Cost, latency, retention, and availability targets are deliberately left as open questions until requirements are gathered.

## How to read this repository

1. Start with [`docs/01-framing.md`](docs/01-framing.md) for the problem, users, boundaries, and success measures.
2. Read [`docs/02-building-blocks.md`](docs/02-building-blocks.md) alongside the [architecture diagram](diagrams/knowledge-assistant.svg).
3. Review numbered [architecture decision records](adr/README.md) for decisions, alternatives, and tradeoffs.
4. Use [`capstone/README.md`](capstone/README.md) to track the final architecture PDF and presentation as the course progresses.

## Course assignments

- [Session 01 — Banking debit-card reactivation](assignments/session-01/README.md): a separate, illustrative mini-project with an editable wiki, diagram, three ADRs, review checklist, and policy guardrail. Its banking scenario is distinct from the portfolio's internal knowledge-assistant example.

Each future course session should add one numbered file under `docs/`. Diagrams should keep an editable source file and an exported SVG or PNG. Decisions should receive their own numbered ADR, including rejected alternatives and a revisit trigger.

## Current status

This is an initial working draft for the course. Review the scenario and decisions against your own reasoning as sessions progress. The Session 02 notes and model-hosting choice are provisional; the capstone deliverables will be added after the architecture has been reviewed. The repository is public and is intended to remain public through the course's final project deadline on 13 December 2026.
