# ADR 0001 — Model hosting

**Status:** Proposed  
**Date:** 2026-10-18

## Context

The assistant needs reliable text generation over retrieved, permission-filtered policy passages. The team has not yet validated data processing requirements, volume, or model quality on a representative evaluation set. A hosting choice should therefore be easy to revisit.

## Decision

Start the pilot with a managed model API behind an internal model gateway. The gateway will centralize authentication, prompt templates, timeouts, usage limits, request logging, and provider configuration. Use a provider only after security, privacy, and contractual review confirms the permitted data flow.

This is a pilot architecture choice, not a selection of a particular vendor or model.

## Alternatives considered

| Option | Tradeoff |
| --- | --- |
| Self-host an open-weight model | Greater control over runtime and data location, but requires serving, scaling, patching, and quality tuning capacity |
| Managed model API | Faster pilot and less serving work, with provider dependency and data processing requirements |
| Hybrid routing | Can optimize different workloads, but adds operational and evaluation complexity before demand is known |

## Consequences

- The application needs a gateway interface so models can be changed without rewriting retrieval and policy logic.
- Security review must cover data transfer, retention, region, access, and incident handling before real documents are used.
- Evaluation must compare answer quality, groundedness, latency, and cost on the same question set.
- Provider outages or policy changes need a fallback path that directs employees to the source documents or human owners.

## Revisit when

Requirements rule out external processing, pilot cost or latency exceeds agreed limits, a quality evaluation favors another model, or usage volume makes self-hosting practical.
