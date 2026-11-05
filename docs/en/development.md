# Development guide

[Español](../es/development.md) · [Documentation](README.md)

## Set up and inspect

Follow [onboarding](onboarding.md) for Python 3.11+, the virtual environment, and dependencies. Read `AGENTS.md`, inspect Git status, and preserve existing work before editing. This is a Python CLI and an agent-guidance product: no development server, database setup, or hosted API is required for the core workflow.

| Path | Role |
| --- | --- |
| `scripts/` | CLI, validation, controlled mutations, acceptance, export |
| `tests/` | Automated tests and synthetic fixtures |
| `contratos/`, `modelo/` | Structural contracts, schemas, and entity distinctions |
| `.agents/skills/` | Intent-specific agent workflows |
| `plantilla_boveda/` | New-instance template, not an existing-vault upgrade |
| `metodologia/` | Preserved methodology originals |
| `docs/en/`, `docs/es/` | Paired usage and development documentation |

See [architecture](architecture.md), [data model](data-model.md), and [CLI reference](cli-reference.md). Business data, private permissions, and transcript banks belong outside the public product.

## Change and verify

Reproduce runtime failures with synthetic data, make the smallest relevant change, and test the affected behavior. Before closing runtime changes, run:

```bash
python scripts/cerebro.py --help
python -m unittest discover -s tests -v
git diff --check
```

Use the activated environment from onboarding. For documentation-only changes, check links, code examples, language parity, and documented behavior rather than claiming a runtime acceptance result. Preserve literal CLI names, flags, schema keys, enums, IDs, and vault filenames across translations. Check the [documentation workflow](documentation-workflow.md) for the documentation checker and template provenance.

Automated checks do not verify Obsidian GUI, semantic retrieval, editorial approval, or business usefulness. Record each separately; see [testing](testing.md).

## Export and integration

The exporter requires a Git checkout with a commit and exports allowlisted files from **HEAD**, not uncommitted working-tree changes:

```bash
python scripts/exportar_producto.py --dest /private/path/product.zip
```

Use a destination outside the repository. Its manifest uses the exported files' hashes. Private instances must remain excluded. An export is a local artifact; it does not publish a release.

Updating product code does not authorize copying it over a live business vault. Installation, migration, or integration acceptance uses a dedicated read-only report and isolated synthetic rehearsal before any separately authorized real-vault changes. Routine continuation does not require that campaign. Read [operations](operations.md), [testing](testing.md), and [contributing](../../CONTRIBUTING.md).
