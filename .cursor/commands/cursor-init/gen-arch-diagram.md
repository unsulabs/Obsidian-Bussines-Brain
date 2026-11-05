# Local adaptation of ai-cursor-init

Adapted from [mgiovani/ai-cursor-init](https://github.com/mgiovani/ai-cursor-init/tree/fc15400e4baab4607f408f5b83fed19263e564e3). MIT attribution and full license: [THIRD_PARTY_NOTICES.md](../../../THIRD_PARTY_NOTICES.md).


Read `AGENTS.md`, `.cursor-init.yaml`, `.cursor/README.md`, and `docs/documentation-map.json` first. These are agent instructions, not a shell command or background service. In Codex, explicitly read this file and perform its steps with available tools; do not assume slash-command discovery. Work only on authorized public product documentation. Never load private vaults or the transcription bank for documentation. Preserve existing edits, skills, contracts, original methodology, IDs and public/private separation. English is primary; update the declared Spanish counterpart in the same change. Keep identifiers, CLI flags and file paths unchanged. Use relative links from each output file.

Inspect `scripts/`, `modelo/`, templates and tests to establish actual components and data flows. Update only the relevant diagram sections in `docs/en/architecture.md` and `docs/es/architecture.md`. Use Mermaid with matching node IDs and translated labels. Distinguish product repository, private source bank, private vault, agent and external Obsidian. Do not invent servers, queues, autonomous workers, ACL enforcement or semantic search. Explain what the arrows mean and label proposals. Use the architecture template as a checklist, not a replacement for existing prose. Run docs checks; rendering remains unverified unless observed.

