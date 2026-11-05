# User guide

[Español](../es/user-guide.md) · [Documentation](README.md)

## Build knowledge for a real task

Start with a question or task: explain how you qualify a customer, prepare an offer, deliver work, or make a decision. The product serves businesses and self-employment without assuming departments or employees.

1. Recover authorized original sources and the owner's judgment. Keep facts, proposals, hypotheses, historical statements, and approved decisions distinct.
2. Identify the subjects and existing canonical notes. For several subjects, show the knowledge architecture before drafting. D01–D07 and X01–X07 organize synthesis and dossiers; they are not a quota of empty files.
3. Develop mechanisms, reasons, exceptions, and alternatives. Materialize authorized work with stable IDs, source links, review state, history, and backups where applicable.
4. Use the knowledge for the actual task, then ask a question that should remain uncertain. Compare source → note and note → answer before claiming usefulness.
5. Record corrections and a continuation point. A first note or structural validation is not acceptance of the entire business knowledge system.

## Continue an existing instance

Use [Continue with Codex](../../CONTINUE_WITH_CODEX.md). The agent verifies routing before accessing the vault, then reads local instructions, `Como_usar`, `Inicio`, and relevant notes and original passages. It does not recreate the vault or repeat the initial interview. Reading a source card does not prove the original was read in this session.

## Add a conversation or transcript

Identify the material as a conversation/transcript and state whether more parts will follow. The default cycle preserves each delivery exactly before analysis, records provenance/sensitivity/completeness, reviews all subjects and antecedents, then integrates the source card, access to the full text, and justified connections within the instance's authorization.

A link alone is not a captured original. Missing access or parts remain pending. Ordinary documents, code, GitHub links, and long questions retain their requested task; their length does not authorize transcript ingestion. Permissions belong to this instance and purpose, not to another customer's profile. See [transcripts](transcripts.md).

## Correct knowledge and navigate it

A correction triggers source review and an explicit change proposal; it does not silently overwrite approved knowledge or rewrite history. If new evidence conflicts with an approved decision, preserve both and present the material decision. Rejected business writing must not return as authority through summaries.

Bases and maps help navigation; links do not prove a relationship. Preview a map before publication, which needs its own authorization, hashes, and external private backup. No automatic migration or recurring processing is implied. See [knowledge workflow](knowledge-workflow.md) and [operations](operations.md).

## Check status and get help

After activating the Python environment and verifying the vault destination:

```bash
python scripts/cerebro.py estado --vault /private/path/MyBusiness
python scripts/cerebro.py validar --vault /private/path/MyBusiness
```

These are structural checks, not proof of semantic accuracy or GUI behavior. If routing fails, keep authorized work outside the vault. If dependencies fail, verify the interpreter and existing environment. If an answer loses meaning, reopen the original and trace the source-to-answer chain rather than editing notes to make a test pass.

For a product issue, provide a synthetic reproduction and sanitized diagnostics under [contributing](../../CONTRIBUTING.md). Never attach real business sources or credentials. See [security](security.md) for privacy boundaries.
