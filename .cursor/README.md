# Documentation agent commands

This is a focused adaptation of [ai-cursor-init](https://github.com/mgiovani/ai-cursor-init/tree/fc15400e4baab4607f408f5b83fed19263e564e3), pinned to that revision. See [attribution and license](../THIRD_PARTY_NOTICES.md).

The Markdown files under `commands/cursor-init/` are agent instructions. They do not install a CLI, daemon, scheduled process or automatic synchronization. In Cursor, select the available custom command using the editor's command interface; discovery depends on the installed editor version. In Codex, ask the agent to read the exact command file and execute its steps. Repository `AGENTS.md` remains the operational contract.

| Task | Instruction file |
| --- | --- |
| Initialize missing paired docs | [init-docs](commands/cursor-init/init-docs.md) |
| Update documentation from code | [update-docs](commands/cursor-init/update-docs.md) |
| Check docs and report limits | [check-docs](commands/cursor-init/check-docs.md) |
| Propose an architectural decision | [adr](commands/cursor-init/adr.md) |
| Update architecture diagrams | [gen-arch-diagram](commands/cursor-init/gen-arch-diagram.md) |

`.cursor-init.yaml` retains upstream documentation categories. Its `local_extension` mapping and bilingual templates are **local extensions**, not documented upstream features. The prompts interpret these settings; the Python checker uses the JSON inventory directly, not YAML.

English lives in `docs/en/` and Spanish in `docs/es/`, with paired entry documents at the root as declared in [the inventory](../docs/documentation-map.json). Existing methodology, contracts, skills and legacy reference files retain their original paths and language. Do not overwrite them with templates. Add ADR/RFC pairs to the inventory when creating them.

Run from the repository root:

```bash
python3 scripts/check_docs.py
python3 -m unittest discover -s tests -p 'test_check_docs.py' -v
```

The checker verifies inventory parity, local inline/reference Markdown links and ATX heading anchors. It skips fenced examples and remote URLs. It does not verify semantic equivalence, source-code accuracy, setext headings, arbitrary HTML anchors, Mermaid rendering or all possible Markdown syntax. Review those explicitly when present.

## Español

Los archivos de comandos son instrucciones para un agente, no ejecutables ni vigilancia automática. En Codex, pide leer el archivo concreto y ejecutar sus pasos. `local_extension` y las plantillas EN/ES son extensiones locales; el validador Python lee el inventario JSON. Mantén ambos idiomas en cada cambio, conserva las fuentes originales y verifica por separado significado, comportamiento real y diagramas.
