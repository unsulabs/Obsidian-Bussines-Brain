# ADR 0003 — Paired English and Spanish documentation

[Español](../../es/adr/0003-bilingual-documentation.md) · [Documentation workflow](../documentation-workflow.md)

## Status

Record of the documentation layout in this working product. This file does not certify complete translation of every historical source or release publication. No historical approval date is asserted.

## Context

Public usage and development guidance needs a consistent English entry and equivalent Spanish guidance. Existing methodology, contracts, operational references, and runtime identifiers carry versioned meaning that cannot safely be replaced by renamed translations.

## Decision

Use English as the primary public entry, with declared Spanish counterparts. Keep localized pages in `docs/en/` and `docs/es/` and root entry pairs as listed in `docs/documentation-map.json`. Update each pair together with equivalent steps, permissions, limitations, examples, and links.

Preserve command names, flags, schema keys, enums, stable IDs, skills, and vault filenames. Identify original Spanish references explicitly from English guidance; preserve their paths, language, and historical identity. A topic guide summarizes and navigates its references; it does not claim line-by-line translation or replacement.

Adapt ai-cursor-init instructions and templates to the inspected product, retaining its pinned provenance and MIT notice. Bilingual inventory and templates are local extensions. Use the Python checker for declared coverage and supported local links, with human/agent review for meaning and implementation accuracy.

## Alternatives and consequences

English-only guidance would omit the Spanish counterpart. Renaming runtime files or silently overwriting original methodology would break identity and provenance. Copying generic framework claims would misrepresent the product.

Paired pages add maintenance work and can drift semantically even when links pass. Changes must review both meanings, commands, and guards; historical references remain explicitly outside the full bilingual parity claim. The adaptation is agent-driven, not automatic synchronization or a new runtime service.

## Evidence

[Inventory](../../documentation-map.json), [local framework](../../../.cursor/README.md), [checker](../../../scripts/check_docs.py), [third-party notice](../../../THIRD_PARTY_NOTICES.md), [methodology guide](../methodology.md), and [documentation workflow](../documentation-workflow.md).
