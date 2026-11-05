# Testing and acceptance

[Español](../es/testing.md) · [Documentation](README.md)

Use the verified Python 3.11+ environment from [onboarding](onboarding.md). Run commands from the repository root. Use synthetic fixtures and isolated temporary paths; never repair a real business vault to make a product test pass.

## Automated checks

The `Platform installation` GitHub Actions workflow uses standard Ubuntu 24.04,
Windows Server 2022 and macOS 15 runners with Python 3.11. Each fresh checkout
creates and activates `.venv` using the same platform commands in both READMEs,
then installs `requirements.txt`. No UTF-8 environment override is required:
repository text uses explicit UTF-8 and LF; original transcript bytes remain untouched.

`scripts/verify_platform.py tests --output /outside/checkout/evidence` runs full
unittest discovery and reports the commit, executed tests, failures, errors and
every skip. Only the named native macOS alias test may skip off macOS, and the
eight named native Windows filesystem tests may skip off Windows. Their native
jobs must execute them. Any other skip or expected failure fails acceptance.
The `installation` phase checks help, doctor, documentation, package audit,
synthetic creation/validation/state with Unicode and spaces, and exported hashes
and privacy boundaries. Artifacts contain synthetic reports and test logs only.
These headless checks do not establish Obsidian GUI/Bases or business acceptance.

The Windows bank backend requires a local NTFS/ReFS path; it rejects UNC/device
paths, alternate data streams and reparse points. Private directories require a
protected DACL restricted to the owner, SYSTEM and administrators; existing broad
ACLs are rejected rather than silently changed. POSIX keeps its directory-handle,
mode-bit and flock controls. Windows uses native handles, process-death locks,
file flushes and write-through rename; it does not claim POSIX directory-fsync semantics.

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

## Installation regression checks (2026-11-05)

Clean-clone review found three blockers: assisted onboarding required an unavailable external router; validation accepted a missing vault as zero notes without errors; and the package audit rejected the documented ignored local `.venv`. The product now includes a native-registry-verified router, rejects missing/non-directory validation targets, and excludes only an ignored, entirely untracked root `.venv` in a Git checkout from the local audit. A package or tracked environment remains rejected; exports exclude `.venv` at every depth. The doctor recommendation now matches Python 3.11+.

Focused checks passed on macOS 26.5.1 arm64 with Python 3.11.15 using synthetic registries and temporary vaults:

```bash
python -m unittest discover -s tests -p 'test_*boveda_codex.py' -v
python -m unittest discover -s tests -p 'test_entrega.py' -v
python -m unittest discover -s tests -p 'test_exportar_producto.py' -v
python scripts/check_docs.py
git diff --check
```

These checks cover successful explicit selection, ambiguous/missing/malformed registration, native identity mismatch, path traversal/symlinks, read-only resolution, invalid vault CLI exits and environment audit/export boundaries.

Independent clean-clone review of candidate `4444224` ran **460 tests: 458 passed and 2 failed** in 550.845 seconds. Both failures concerned skill documentation links: an incorrect relative path and a link outside the skills-only distribution contract. The links were corrected without changing runtime code or tests; an independent rerun then passed all 29 targeted tests: routing links (7), resolver (9), registration (8) and delivery checks (5). Documentation and whitespace checks also passed after the correction. This is a full run followed by focused verification of the two repairs, not a claim that a second uninterrupted 460-test run passed.

A separate fresh-clone/venv rehearsal passed creation, validation, state and negative cases. On this same macOS machine, already-installed Obsidian 1.15.0 opened the synthetic vault, displayed `Inicio` and the `Ofertas` Base, and assigned the native ID verified by the included registration/resolution commands using an isolated Codex registry. All 72 original vault files remained unchanged; Obsidian created 4 normal `.obsidian` files. The candidate ZIP contained 472 files with every manifest size/hash matching and no private or `.venv` contents.

Limits: this did not test installing Obsidian from scratch, all Bases views, Windows/Linux installation, semantic business usefulness or owner acceptance. Linux/Windows default-path tests use mocks. The GUI observation covers one Base and a synthetic business; it does not establish those remaining gates.

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
