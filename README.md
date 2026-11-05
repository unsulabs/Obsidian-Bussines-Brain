# Obsidian-Bussines-Brain

**Turn how you work and decide into business knowledge you can use.**

**English** · [Español](README.es.md)

[![License: MIT](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![Python: 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue)](docs/en/onboarding.md) [![Docs: EN / ES](https://img.shields.io/badge/docs-EN%20%2F%20ES-green)](docs/en/README.md)

[Get started](START_HERE.md) · [Continue an existing business](CONTINUE_WITH_CODEX.md) · [Explore the docs](docs/en/README.md) · [Report an issue](https://github.com/unsulabs/Obsidian-Bussines-Brain/issues)

## Contents

- [About the project](#about-the-project)
- [Built with](#built-with)
- [Getting started](#getting-started)
- [Usage](#usage)
- [Privacy and editorial control](#privacy-and-editorial-control)
- [Roadmap and current limits](#roadmap-and-current-limits)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)
- [Acknowledgments](#acknowledgments)

## About the project

Obsidian-Bussines-Brain is a private, source-backed knowledge workspace for business owners, entrepreneurs, and self-employed people. Work with Codex to preserve conversations, explain decisions and exceptions, and develop knowledge your team or agents can use in Obsidian.

Use it to answer “Why do we qualify customers this way?”, prepare an offer from established criteria, or recover what changed between two decisions. The workflow connects original evidence, the owner's judgment, reviewable notes, and the task at hand.

- **Preserve meaning:** keep complete originals and provenance before summarizing; carry reasons, exceptions, and corrections into the resulting knowledge.
- **Develop useful knowledge:** identify subjects and existing notes before drafting, with proposed and approved content kept distinct.
- **Find and maintain it:** retrieve original passages, review revisions, and navigate Markdown notes, Bases views, and Canvas maps.

| Location | What belongs there |
| --- | --- |
| Public product repository | Software, methodology, agent instructions, templates, and synthetic examples |
| Private Obsidian vault | Business knowledge and its review state |
| Private source bank, outside Git and the vault | Original transcripts and their custody records |

This is a local toolkit operated during an agent session. It does not install a hosted service or background worker. Codex and optional connectors have their own access and data-processing conditions.

### Built with

| Component | Role |
| --- | --- |
| Python 3.11+, PyYAML, jsonschema | Local commands and validation; see [dependencies](requirements.txt) |
| Markdown and Obsidian Desktop | Readable notes, Properties, native Bases, and Canvas |
| Codex and repository skills | Assisted source review, knowledge development, and editorial workflow |

See the [architecture guide](docs/en/architecture.md) for component boundaries.

## Getting started

### Prerequisites

- Git and **Python 3.11 or later**.
- Codex with verified filesystem and command access for the assisted workflow.
- Obsidian Desktop to view the vault; verify Bases and CLI availability locally.
- Separate private locations for the business vault and source bank.

**Vault routing is included:** the repository’s [obsidian-router skill](.agents/skills/obsidian-router/SKILL.md) and read-only resolver verify a local destination registry against Obsidian. Follow [registration and resolution](docs/en/onboarding.md#register-and-resolve-the-vault); cloning alone does not register a vault. Before listing or reading vault files, the agent must resolve the destination and read local instructions. An active window or typed CLI path does not replace these checks. If routing is unavailable, continue authorized work outside the vault and leave vault access/integration pending.

### Installation

Prepare the product on macOS or Linux:

```bash
git clone https://github.com/unsulabs/Obsidian-Bussines-Brain.git
cd Obsidian-Bussines-Brain
python3.11 --version
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/cerebro.py doctor
python scripts/cerebro.py --help
```

A newer Python 3 interpreter may be used; CI uses Python 3.11, so verify another version in your environment. On Windows, after cloning and entering the folder, use PowerShell:

```powershell
py -3.11 --version
py -3.11 -m venv .venv
. .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python scripts/cerebro.py doctor
python scripts/cerebro.py --help
```

Package installation may access the network and requires applicable authorization. See [platform checks and storage boundaries](docs/en/testing.md#automated-checks).

`doctor` is read-only and does not install missing components. If imports fail, check the interpreter and existing environments. This quickstart prepares the toolkit; it does not create a vault or verify Obsidian GUI behavior or business usefulness.

### Choose your next step

Open the cloned `Obsidian-Bussines-Brain` folder as a project in Codex. Start a chat there with the [English startup prompt](GET_STARTED_WITH_CODEX.md) or [Spanish startup prompt](PROMPT_INICIO_CODEX.md), or the continuation prompt below for an existing instance. Codex reads `AGENTS.md` and the relevant `.agents/skills/*/SKILL.md` directly from this checkout; no global skill installation is required.

| Your situation | Next step |
| --- | --- |
| No business instance exists | Follow [onboarding](docs/en/onboarding.md#new-business-instance) to create an authorized instance at a new private path, then [develop it with Codex](GET_STARTED_WITH_CODEX.md). |
| A business vault already exists | Use [Continue with Codex](CONTINUE_WITH_CODEX.md). Verify routing; do not run `crear`, copy templates over the vault, or restart the initial interview. |
| Use or update knowledge | Open the [user guide](docs/en/user-guide.md). |
| Change the product | Open the [development guide](docs/en/development.md). |

Installing a template is only the beginning: continue through source review, knowledge architecture, useful writing, review, and a real business task.

## Usage

These **synthetic examples** are prompts for Codex after configuring the private instance and verifying its destination. They are not claims about a real business.

**Add a new conversation**

> This is a new, complete synthetic transcript for the Taller Nube demo: “We offer a diagnostic session before quoting a repair. For returning customers, check the previous diagnosis first. We have not approved a fixed diagnostic price.” Preserve the exact text before analysis. Within this instance's authorization, integrate its source card, access to the full text, and justified connections. Keep the price undecided and show what changed.

The transcript cycle covers every subject, prior evidence, and relevant existing notes. Identify any parts still to come; a link alone is not a captured original. Ordinary documents and long questions retain their requested task and are not automatically ingested as transcripts. See [transcript workflow](docs/en/transcripts.md).

**Ask a business question**

> In the Taller Nube demo, what should we check before quoting a returning customer? Open the relevant original passages and explain the reasons and exceptions. Distinguish approved decisions from proposals. If the diagnostic price is not established, leave it unknown rather than suggesting an agreed price.

**Correct a working note**

> The returning-customer exception applies only when the previous diagnosis covers the same problem. Review the original and related notes, then propose the correction and its impact. Preserve the earlier version and do not silently overwrite approved knowledge.

See the [user guide](docs/en/user-guide.md) and [knowledge workflow](docs/en/knowledge-workflow.md). Check both a useful task and a question that should remain uncertain; structural validation alone does not establish a correct answer.

## Privacy and editorial control

Keep real sources, personal data, credentials, and client evidence out of commits, issues, and pull requests. Permissions are specific to the instance, source, and purpose. Sensitivity labels are metadata; Obsidian does not enforce per-note access control. Publication, external uploads, plugins, and integrations require applicable authorization.

AI output remains a proposal until appropriate verification and decision. Preserve conflicting evidence and history instead of replacing approved decisions with newer statements. Source cards help locate originals; they do not prove the original was read in this session. Maps, views, and links support navigation and do not establish authority.

No country, currency, tax regime, legal form, departments, or employees are assumed. Unknown context stays unknown. See [security and privacy](docs/en/security.md).

## Roadmap and current limits

The product is under development. The [roadmap (Spanish original)](docs/HOJA_DE_RUTA.md) prioritizes installation/recovery across operating systems, independent semantic fidelity review, adapters and external access controls, and migration/restoration tests in isolated copies. These are validation priorities, not delivery commitments.

Transcript search is lexical. Hosted service, automatic ERP/CRM synchronization, multiuser access controls, and universal migrations are not implemented. Automated tests do not establish business accuracy, regulatory compliance, semantic retrieval quality, or GUI compatibility. See [current boundaries](docs/en/architecture.md#alternatives-and-remaining-gates), [acceptance guidance](docs/en/testing.md), and the [changelog](CHANGELOG.md).

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a change. Use synthetic reproductions, sanitized diagnostics, and checks appropriate to the change. Keep English and Spanish guides aligned while preserving runtime commands, schema keys, IDs, enums, and vault filenames.

## License

The product is distributed under the [MIT license](LICENSE). Adapted documentation resources are identified separately in [third-party notices](THIRD_PARTY_NOTICES.md).

## Support

Use [GitHub Issues](https://github.com/unsulabs/Obsidian-Bussines-Brain/issues) for product questions, bug reports, and proposed improvements. Include the relevant version, environment, and a synthetic reproduction; remove private paths, sources, and credentials before posting.

## Acknowledgments

README organization adapts [Best-README-Template](https://github.com/othneildrew/Best-README-Template/tree/fc444eb7b04b2e4863f6080b1507a219e95103fa), published under The Unlicense. Other documentation tooling adapts [ai-cursor-init](https://github.com/mgiovani/ai-cursor-init/tree/fc15400e4baab4607f408f5b83fed19263e564e3). See [attribution and license details](THIRD_PARTY_NOTICES.md).

Original methodology and operational references remain in Spanish; the [English documentation index](docs/en/README.md) provides paired guides and identifies preserved sources.

[Back to top](#obsidian-bussines-brain)
