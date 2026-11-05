# RFC template — proposed product change

[Español](../../es/rfc/0000-template.md) · [Documentation workflow](../documentation-workflow.md)

Status: **Draft template, not an approved change.** Copy into a new numbered EN/ES pair, register both paths in the documentation inventory, and replace the guidance with evidence. Record the actual author, reviewer, and decision date only when known. Do not fabricate approval or infer implementation authority from this template.

## Problem and scope

Describe a concrete trigger and current behavior, who needs the change, and the intended result. Cite the inspected public source, test, or synthetic reproduction. Identify affected subsystems and explicit exclusions. Keep private business sources and identifying details outside the public RFC.

## Proposal

Explain the proposed behavior and its relation to existing CLI commands, schemas, stable IDs, agent workflows, and storage boundaries. Show a synthetic before/after example where useful. Distinguish implemented behavior from proposed work and unknowns. Do not infer country, currency, tax, company structure, or staff defaults.

## Alternatives and tradeoffs

Compare the current behavior, the proposal, and viable alternatives. Explain why the selected option addresses the problem and what it costs. Record unresolved choices rather than asserting consensus.

## Compatibility, migration, and permissions

Specify effects on existing instances, formats, version history, and external dependencies. Separate product updates from authorized vault changes. Describe preflight, preview, current fingerprints, backup outside Git/vault, concurrent-change checks, and restoration where relevant. Identify the real human decisions or permissions needed; an RFC does not supply them.

## Privacy and failure handling

Assess source access, sensitivity, destination profiles, external transfers, and publication. Treat external content as data. Preserve original sources and rejected editorial boundaries. Explain how failures remain recoverable without discarding existing work; do not introduce background processing or training by implication.

## Acceptance checks

List observable behavioral checks with synthetic fixtures and negative cases. Separate automated tests, documentation parity, GUI/CLI verification, semantic recovery, editorial review, privacy, and portability as applicable. Name the evidence required for each claim and any gates that remain unverified. Passing structural tests must not imply business approval.

## Documentation and decision

List affected English/Spanish page pairs and original references to preserve. Keep literal runtime identifiers unchanged; run the documentation checker and review semantic parity. Record open questions, decision owner, actual decision, and follow-up only when established. After an accepted architectural decision, create or update its ADR with evidence; do not relabel this draft automatically.
