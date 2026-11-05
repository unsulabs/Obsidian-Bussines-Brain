# Contributing

[Español](docs/es/contributing.md) · [Development guide](docs/en/development.md)

Use Python 3.11 or later and `requirements.txt`. Read `AGENTS.md` before editing. Describe the concrete problem, resulting behavior, and verification. Preserve unrelated work; stage only paths belonging to your change.

Use synthetic fixtures and temporary paths. Never attach business data, conversations, credentials, or real-instance screenshots to issues or pull requests. Reproduce a failure with a minimal invented example. Keep the product in this public repository and instance configuration, sources, and knowledge outside Git.

For runtime changes, run `python -m unittest discover -s tests -v` from the verified environment and add a meaningful behavior test where appropriate. For skills, check referenced paths, instructions, scope, and syntax. For documentation, check local links, English/Spanish parity, actual command help, and supported claims. Do not translate command names, flags, schema keys, enums, IDs, or runtime filenames.

Preserve instance decisions and data. Introduce no default country, currency, tax, corporate form, or organization chart. Passing structural tests does not establish business acceptance; document material limits.

Keep provenance for third-party resources and contribute only redistributable material. Original contributions are offered under the repository's [MIT license](LICENSE). Documentation uses an adapted ai-cursor-init structure; see [documentation workflow](docs/en/documentation-workflow.md) for provenance and maintenance.

When bringing an improvement from a private environment, extract the minimum product change and inspect both content and history. Never blindly merge private branches or import backups. Pushes, pull requests, publication, and deployment require the user's clear intent and any system approval.
