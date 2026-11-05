# Onboarding

[Español](../es/onboarding.md) · [Documentation](README.md)

## Prerequisites and storage

Use Python 3.11 or later, Git for a checkout, and the packages in `requirements.txt`. Assisted work needs Codex with verified filesystem and command access. Viewing the vault needs Obsidian Desktop; verify Bases and CLI availability locally. Optional connectors need their own credentials and authorization.

Keep three separate locations: this public product repository, a private business vault, and a private transcript bank outside both. Never initialize a business using another customer's files. No country, currency, tax regime, legal structure, or staff is preconfigured.

## Prepare the product

Run from a local checkout. Package installation may access the network; an agent must have the applicable authorization.

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

A newer Python 3 interpreter is also supported; verify its version before creating the environment. On Windows, use `py -3.11 -m venv .venv` and activate with `.venv\Scripts\Activate.ps1` in PowerShell instead of `source`. After activation, the `python` commands are the same.

`doctor` is read-only; it does not install missing components. If imports fail, check the interpreter and existing environments before concluding that the product cannot run. Passing this check does not verify GUI or business usefulness.

## New business instance

Only when no instance exists and creation is authorized, choose a new private path outside Git. Replace the example path with your own absolute path; `crear` rejects an existing destination.

```bash
python scripts/cerebro.py crear --id MY-BUSINESS --nombre "My business" --dest /private/path/MyBusiness
python scripts/cerebro.py validar --vault /private/path/MyBusiness
python scripts/cerebro.py estado --vault /private/path/MyBusiness
```

On Windows use an absolute local destination such as `C:\Private\MyBusiness`. Open the created vault in Obsidian Desktop and verify it there. Before the agent accesses it as an existing vault, configure and verify the external `obsidian-router` and local destination registry. Cloning this repository does not install that skill or register a vault.

Use [the startup prompt](../../GET_STARTED_WITH_CODEX.md) to continue through discovery, source review, knowledge architecture, useful writing, review, and a real task. A template or provisional capture does not finish this work.

## Existing business instance

Do not run `crear`, copy templates over the vault, or restart the initial interview. Use [the continuation prompt](../../CONTINUE_WITH_CODEX.md). Before listing or reading inside the vault, resolve it through `obsidian-router`, verify native Obsidian registration, and read its local instructions. An active window or a typed path is not sufficient verification.

If routing is unavailable, preserve authorized work outside the vault and leave vault access/integration pending. Do not invent a registry or claim the environment was checked. Routine use does not require a full installation acceptance campaign.

## Verify the appropriate outcome

For product development, run the tests in [development](development.md). For installation or integration acceptance, use [testing](testing.md) and the dedicated acceptance procedure. Verify structural integrity, Obsidian GUI, semantic retrieval, and business usefulness separately. A synthetic test cannot approve a real business decision.

Next: [User guide](user-guide.md).
