# Local adaptation of ai-cursor-init

Adapted from [mgiovani/ai-cursor-init](https://github.com/mgiovani/ai-cursor-init/tree/fc15400e4baab4607f408f5b83fed19263e564e3). MIT attribution and full license: [THIRD_PARTY_NOTICES.md](../../../THIRD_PARTY_NOTICES.md).


Read `AGENTS.md`, `.cursor-init.yaml`, `.cursor/README.md`, and `docs/documentation-map.json` first. These are agent instructions, not a shell command or background service. In Codex, explicitly read this file and perform its steps with available tools; do not assume slash-command discovery. Work only on authorized public product documentation. Never load private vaults or the transcription bank for documentation. Preserve existing edits, skills, contracts, original methodology, IDs and public/private separation. English is primary; update the declared Spanish counterpart in the same change. Keep identifiers, CLI flags and file paths unchanged. Use relative links from each output file.

Run `python3 scripts/check_docs.py` from repository root. This deterministic check covers declared pairs, unregistered localized Markdown, local links and Markdown heading anchors. It does not certify translation meaning, remote URLs, Mermaid rendering, or factual freshness. Separately compare EN/ES meaning and inspect current source/tests for behavioral claims. Render diagrams in an available renderer before claiming visual validity. Report each observed failure with file and evidence; do not invent freshness scores or claim checks that were not run.

