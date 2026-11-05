# Obsidian-Bussines-Brain

[Español](README.es.md) · [Documentation](docs/en/README.md) · [MIT license](LICENSE)

A private, source-backed business knowledge workspace for business owners, entrepreneurs, and self-employed people. Work with Codex to turn conversations, decisions, and working methods into useful knowledge in Obsidian.

The repository contains software, methodology, agent instructions, and synthetic examples. Business knowledge lives in a separate private Obsidian vault; original transcripts live in a separate private source bank. This is a local toolkit operated during an agent session, not a hosted service or background worker. Codex and optional connectors have their own access and data-processing conditions.

## Start with your situation

| Your situation | Start here |
| --- | --- |
| First time using the product | [Start here](START_HERE.md) |
| A business vault already exists | [Continue with Codex](CONTINUE_WITH_CODEX.md) |
| Use or update knowledge | [User guide](docs/en/user-guide.md) |
| Change the product | [Development guide](docs/en/development.md) |

You need Python **3.11 or later**, the packages in `requirements.txt`, and Codex with verified file and command access for the assisted workflow. Obsidian Desktop displays the vault; check Bases and CLI availability in your installation. Follow [onboarding](docs/en/onboarding.md) for setup and the new/existing vault split.

**External dependency:** assisted work on an existing vault requires `obsidian-router`, a local destination registry, and verification against Obsidian. Cloning does not install them. If routing cannot be verified, keep authorized work outside the vault and leave vault access pending. An explicit CLI path does not replace the agent's routing checks.

## What you can build

- Preserve authorized sources with provenance, sensitivity, and purpose-specific permissions.
- Develop operating knowledge from evidence and the owner's judgment, keeping proposed and approved content distinct.
- Retrieve passages, maintain revisions, and navigate Markdown notes, Bases views, and Canvas maps.
- Check a real business task and a question that should remain uncertain, separately from structural validation.

No country, currency, tax regime, legal form, departments, or employees are assumed. Unknown context stays unknown. AI output remains a proposal until appropriate verification and decision. The product is under development: automated tests do not establish business accuracy, regulatory compliance, semantic retrieval quality, or GUI compatibility.

## Privacy and distribution

Do not put real sources, personal data, credentials, or client evidence in commits, issues, or pull requests. Sensitivity labels are metadata; Obsidian does not enforce per-note access control. Maps and views are derived navigation, not independent authority. Publication, external uploads, plugins, and integrations require applicable authorization.

Read [contributing](CONTRIBUTING.md), [changes](CHANGELOG.md), and the [documentation index](docs/en/README.md). Methodology originals remain in Spanish and are identified as such. Runtime commands, schema keys, IDs, enums, and vault filenames retain their existing identifiers.
