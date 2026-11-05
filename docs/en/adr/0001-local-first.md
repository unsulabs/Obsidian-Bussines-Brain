# ADR 0001 — Separate local business knowledge from the product

[Español](../../es/adr/0001-local-first.md) · [Architecture](../architecture.md)

## Status

Record of the current repository contract and implementation, not a new approval or a claim that a particular installation has passed acceptance. No historical approval date is asserted.

## Context

The public product must be reusable across businesses without carrying customer content or instance permissions. The agent, product checkout, Obsidian vault, and source bank have different responsibilities and access boundaries.

## Decision

Keep reusable software, methodology, instructions, and synthetic examples in Git. Store each business's knowledge in a private vault separate from the product and keep its transcript bank outside both. Use explicit paths in the CLI; assisted access to an existing vault additionally requires the external `obsidian-router`, native Obsidian registration verification, and local instructions. Never select a vault by the active window alone.

Updating the product does not authorize copying templates into an existing vault. Work runs during an agent session; the repository does not create a hosted service or background monitor. Optional connectors retain their own authorization and access requirements.

## Alternatives and consequences

Keeping real instance data in the product repository or treating a private Git remote as permission would mix distribution and business authority; the current contract excludes both. A hosted shared data service is not the implemented architecture.

Local storage supports readable files and controlled backups, but does not itself provide encryption, per-note ACLs, verified restoration, or semantic correctness. Users must maintain appropriate storage controls; agents must verify destinations and permissions. Missing routing can block vault access without blocking independently authorized work elsewhere.

## Evidence

[Repository contract](../../../AGENTS.md), [onboarding](../onboarding.md), [security](../security.md), [CLI entry](../../../scripts/cerebro.py), and [exporter](../../../scripts/exportar_producto.py). Preserved Spanish source: [GitHub and privacy](../../GITHUB_Y_PRIVACIDAD.md). Related: [source custody](0002-source-custody.md).
