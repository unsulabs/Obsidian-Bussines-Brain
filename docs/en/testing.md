# Testing and acceptance

[Español](../es/testing.md) · [Documentation](README.md)

Use the verified Python 3.11+ environment from [onboarding](onboarding.md). Run commands from the repository root. Use synthetic fixtures and isolated temporary paths; never repair a real business vault to make a product test pass.

## Automated checks

```bash
python scripts/cerebro.py doctor
python -m unittest discover -s tests -v
python scripts/check_docs.py
git diff --check
```

`doctor` is read-only and reports what it can observe; it does not install components or prove GUI/Bases functionality. The suite exercises structural behavior and safeguards using its fixtures. Inspect failures and skips rather than treating a process exit alone as proof of every gate.

For a documentation-checker change, the targeted suite is:

```bash
python -m unittest discover -s tests -p 'test_check_docs.py' -v
```

Choose other targeted tests by the changed behavior, then run the full suite for runtime closure. Documentation-only edits need scoped checks and factual review; they do not by themselves require reading a private instance. Verify documented commands against actual `--help` and code. The documentation checker verifies declared pairs, local links, and supported heading anchors, not semantic translation or rendered diagrams.

## What requires separate evidence

| Gate | Evidence required |
| --- | --- |
| Structural integrity | Actual validation/test output with interpreter, checkout state, and relevant paths |
| Obsidian integration | Observed GUI navigation, Bases, links, and available CLI behavior |
| Knowledge architecture | Agent identifies subjects and canonical owners before multi-subject drafting; one justified indivisible note remains valid |
| Semantic retrieval | Fresh session reads authorized originals and answers representative questions with scope, date, and authority |
| Editorial fidelity | Owner recognizes mechanisms, decisions, exceptions, and voice; source-to-note and note-to-source comparison |
| Privacy | Authorized scope, restricted-data negative cases, and inspected public artifacts |
| Recovery | Isolated rehearsal of concurrent-change rejection, backup, apply, and restoration |
| Portability | Independent installation/session evidence where the acceptance scope requires it |

Include negative cases: a missing current source, a general price that must not override an agreement, rejected editorial material that must stay excluded, and a plan that must not become a sale. Preserve uncertainty when evidence does not answer the question. To test a complete business explanation, use an open prompt rather than supplying the desired thesis; save the raw prompt and answer. A leading test can create the very failure being measured.

## Accept an installation or integration change

This campaign is separate from everyday consultation. Resolve and authorize the existing vault before access. Record branch, exact commit, and working-tree state; preserve dirty work and use an appropriate isolated candidate rather than discarding it. From the verified checkout, inspect the dedicated program's arguments:

```bash
python scripts/aceptacion_integracion_local.py --help
```

The procedure uses `--vault`, `--salida`, and `--commit-esperado`. The output must be a new private absolute path outside both Git and the vault. The program inspects the vault without modifying it and produces a sanitized report; it does not install or migrate. Default execution includes tests. Do not describe a skipped suite as passed.

Then check Obsidian GUI and the 16 Bases, rehearse changes on a fully fictional isolated business, and obtain the necessary human review. Vault migration, map publication, and editorial changes retain separate authorization. Report observed PASS, FAIL, or NO_VERIFICADO by gate; passing Python tests is not production or business acceptance.

Detailed Spanish source references: [acceptance criteria](../CRITERIOS_DE_ACEPTACION.md), [integration procedure](../../guia/ACEPTACION_REAL_CODEX_INSTANCIA_EXISTENTE.md), [pilot closure](../CIERRE_DEL_PILOTO_0_3.md), and [recorded product state](../ESTADO_REAL.md). Historical results in those files are not fresh evidence for the current checkout or another instance.
