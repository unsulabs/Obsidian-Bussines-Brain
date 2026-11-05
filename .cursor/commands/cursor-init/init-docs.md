# Local adaptation of ai-cursor-init

Adapted from [mgiovani/ai-cursor-init](https://github.com/mgiovani/ai-cursor-init/tree/fc15400e4baab4607f408f5b83fed19263e564e3). MIT attribution and full license: [THIRD_PARTY_NOTICES.md](../../../THIRD_PARTY_NOTICES.md).


Read `AGENTS.md`, `.cursor-init.yaml`, `.cursor/README.md`, and `docs/documentation-map.json` first. These are agent instructions, not a shell command or background service. In Codex, explicitly read this file and perform its steps with available tools; do not assume slash-command discovery. Work only on authorized public product documentation. Never load private vaults or the transcription bank for documentation. Preserve existing edits, skills, contracts, original methodology, IDs and public/private separation. English is primary; update the declared Spanish counterpart in the same change. Keep identifiers, CLI flags and file paths unchanged. Use relative links from each output file.

Initialize missing documentation only. Inspect code, CLI help, tests, and current docs to determine actual behavior. Use the local templates in `.cursor/cursor-init/templates/en/` and `/es/`. Create only missing authorized pairs; merge focused updates into existing documents without replacing them with templates. Register each pair in the inventory. Distinguish implemented, proposed and externally verified behavior. Run `python3 scripts/check_docs.py` and relevant code examples; report remaining human or GUI verification.

