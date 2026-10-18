# Session 01 — Framing

## Scenario

Employees spend time finding the current HR or IT policy and confirming which version applies. The proposed assistant helps them locate approved guidance and answer routine questions with citations. It does not make policy decisions or perform account changes.

## Users and stakeholders

- **Employees:** need fast, trustworthy answers within their access rights.
- **Document owners:** approve source material, resolve ambiguity, and maintain policies.
- **Security and privacy teams:** approve data handling, access control, and audit design.
- **IT operations:** own availability, incident response, and cost monitoring.

## Initial scope

- Search approved policy documents and return an answer with source links and document version.
- Enforce SSO and document-level permissions during retrieval.
- Abstain or escalate when sources are missing, conflicting, stale, or outside scope.
- Capture feedback and limited audit metadata for improvement.

## Out of scope

- Changing accounts, submitting HR requests, or taking other actions on behalf of employees.
- Processing payroll, medical, customer, or other highly sensitive records.
- Treating generated text as the authoritative policy when it conflicts with a source document.

## Measures to validate

| Measure | How it would be checked |
| --- | --- |
| Grounded answers | Human review of answer and citation against the cited source |
| Permission safety | Tests that restricted documents never appear in unauthorized retrieval or answers |
| Appropriate abstention | Evaluation set containing missing, ambiguous, and conflicting policy questions |
| Usefulness | Employee feedback and task completion for representative questions |
| Operations | Latency, error rate, cost per answered question, and escalation volume |

Numeric targets will be agreed with stakeholders after a baseline study. The first evaluation set should contain both common questions and known failure cases before any pilot.

## Open questions

1. Which document system is authoritative, and how are permissions exposed?
2. What retention and regional data processing requirements apply?
3. Which languages must the assistant support?
4. Who signs off on source updates and escalations?
