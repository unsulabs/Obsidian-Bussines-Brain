# Documentation

[Español](../es/README.md) · [Project overview](../../README.md)

English is the primary language for public usage and development guidance. Each page below has a Spanish counterpart. Commands, schema keys, enums, IDs, skill names, and vault filenames keep their runtime identifiers in both languages.

## Use the product

- [Start here](../../START_HERE.md): choose a new or existing business instance.
- [Onboarding](onboarding.md): prerequisites, private storage, setup, and verified routing.
- [User guide](user-guide.md): develop knowledge, use it, add sources, and correct it.
- [Transcripts](transcripts.md): custody, analysis, permissions, and integration.
- [Knowledge workflow](knowledge-workflow.md): architecture, authority, and editorial decisions.
- [Operations](operations.md): existing instances, changes, backups, and acceptance.
- [Security](security.md): privacy and authorization boundaries.
- [Methodology](methodology.md): how to use the preserved Spanish originals.

## Develop and maintain

- [Development](development.md) and [contributing](../../CONTRIBUTING.md).
- [Architecture](architecture.md), [data model](data-model.md), and [CLI reference](cli-reference.md).
- [Testing](testing.md): distinguish structural checks from real acceptance.
- [Documentation workflow](documentation-workflow.md): adapted ai-cursor-init templates and bilingual checks.
- Decisions: [local storage](adr/0001-local-first.md), [source custody](adr/0002-source-custody.md), [bilingual documentation](adr/0003-bilingual-documentation.md).
- [Proposal template](rfc/0000-template.md) and [changelog](../../CHANGELOG.md).

## Originals and reference material

Methodology originals under `metodologia/` and `contratos/`, and historical design/research material, retain their original Spanish wording and version identity. Spanish operational references under `guia/`, legacy `docs/` paths, and skill references may still be linked explicitly as Spanish. They preserve detail and provenance; they do not turn historical plans into implemented capabilities. Start with the current guides above and open originals only when the task needs them.

The repository is the product; it contains no customer vault or transcript corpus. Read `AGENTS.md` before agent work and resolve an existing vault with the included `obsidian-router` before accessing it.
