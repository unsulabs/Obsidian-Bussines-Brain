# Documentation workflow

[Español](../es/documentation-workflow.md) · [Documentation](README.md)

This repository adapts [mgiovani/ai-cursor-init at fc15400e4baab4607f408f5b83fed19263e564e3](https://github.com/mgiovani/ai-cursor-init/tree/fc15400e4baab4607f408f5b83fed19263e564e3). The adaptation uses project-specific agent instructions, bilingual templates, and a deterministic local checker. It does not install an upstream executable, hosted service, or background synchronization. The upstream MIT notice and license are preserved in [THIRD_PARTY_NOTICES.md](../../THIRD_PARTY_NOTICES.md).

## Choose the instruction

| Task | Local instruction |
| --- | --- |
| Initialize missing paired pages | [init-docs](../../.cursor/commands/cursor-init/init-docs.md) |
| Update from changed code | [update-docs](../../.cursor/commands/cursor-init/update-docs.md) |
| Validate and report limitations | [check-docs](../../.cursor/commands/cursor-init/check-docs.md) |
| Draft an architecture decision | [adr](../../.cursor/commands/cursor-init/adr.md) |
| Update architecture diagrams | [gen-arch-diagram](../../.cursor/commands/cursor-init/gen-arch-diagram.md) |

In Cursor, select the available custom command through the editor's command interface; discovery depends on the installed version. These Markdown files are instructions for an agent, not shell commands. In Codex, explicitly ask the agent to read the exact instruction file and carry out its steps with available tools. Do not assume Cursor slash-command discovery in Codex. `AGENTS.md` remains the repository contract.

## Update from evidence

1. Read `AGENTS.md`, [framework notes](../../.cursor/README.md), [.cursor-init.yaml](../../.cursor-init.yaml), and the [documentation inventory](../documentation-map.json). Inspect the scoped diff, current source, tests, and relevant command help.
2. Identify affected page pairs. Write English and Spanish changes together, preserving commands, flags, schema keys, enums, IDs, runtime filenames, and relative-link meaning. Read only relevant public product sources; do not access a private vault or transcript bank to write product documentation.
3. Use the [English](../../.cursor/cursor-init/templates/en/) and [Spanish](../../.cursor/cursor-init/templates/es/) templates for missing pages or structure. Replace prompts with verified content. Do not infer a database, web API, deployment service, branch policy, or performance promise from a generic template. Do not replace existing methodology, contracts, or skills with templates.
4. Add new ADR/RFC pairs to the inventory. Describe current decisions from evidence without inventing approval dates; an RFC is a proposal until a real decision changes its status.
5. Run checks, compare meaning and guards across languages, inspect code examples, and review diagrams separately. Report observed results and limits.

`.cursor-init.yaml` preserves upstream categories; its `local_extension` mapping and bilingual paths/templates are local extensions interpreted by the prompts. The Python checker reads JSON inventory directly, not YAML. There is no automatic synchronization process.

## Check and report

After activating the verified Python environment, run from the repository root:

```bash
python scripts/check_docs.py
python -m unittest discover -s tests -p 'test_check_docs.py' -v
git diff --check
```

The checker detects missing/duplicate declared pairs, unregistered localized Markdown, unsafe paths, local inline/reference links, and supported heading anchors. It skips fenced examples and remote URLs. It cannot certify semantic equivalence, behavior against code, all Markdown syntax, visual rendering, or external URL availability. Review those separately and do not describe an unrendered diagram as visually verified.

The inventory identifies preserved Spanish source references and their topic guides. A topic guide is not a line-by-line translation or replacement of its original. Label Spanish references when linking from English, preserve their paths and historical identity, and distinguish historical results or plans from current implementation. See [methodology](methodology.md) and [the bilingual ADR](adr/0003-bilingual-documentation.md).
