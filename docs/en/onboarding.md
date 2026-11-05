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

A newer Python 3 interpreter may be used; CI uses Python 3.11, so verify another version in your environment. On Windows, after cloning and entering the folder, use PowerShell:

```powershell
py -3.11 --version
py -3.11 -m venv .venv
. .venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python scripts/cerebro.py doctor
python scripts/cerebro.py --help
```

On Windows, use a local NTFS/ReFS path for the transcript bank. Choose a new bank directory so the product can create its protected private ACL; an existing directory with broader permissions or an unprotected ACL is rejected. Network shares and junctions are outside this backend's supported storage scope. See [platform checks and limits](testing.md#automated-checks).

`doctor` is read-only; it does not install missing components. If imports fail, check the interpreter and existing environments before concluding that the product cannot run. Passing this check does not verify GUI or business usefulness.

## New business instance

Only when no instance exists and creation is authorized, choose a new private path outside Git. Replace the example path with your own absolute path; `crear` rejects an existing destination.

```bash
python scripts/cerebro.py crear --id MY-BUSINESS --nombre "My business" --dest /private/path/MyBusiness
python scripts/cerebro.py validar --vault /private/path/MyBusiness
python scripts/cerebro.py estado --vault /private/path/MyBusiness
```

On Windows use an absolute local destination such as `C:\Private\MyBusiness`. Open the created vault in Obsidian Desktop and verify it there. Complete the registration below before the agent accesses it as an existing vault.

## Register and resolve the vault

The [included routing skill](../../.agents/skills/obsidian-router/SKILL.md) works from this checkout without a global installation. After opening your chosen folder as a vault in Obsidian, replace the example path, name and ID with your own:

```bash
python scripts/registrar_boveda_codex.py --vault /private/path/MyBusiness --nombre "My business" --alias MY-BUSINESS
python scripts/resolver_boveda_codex.py --selector /private/path/MyBusiness
```

Registration verifies the native Obsidian ID and writes only `~/.codex/obsidian/vaults.json`, backing up an existing registry. It never writes the vault or Obsidian's registry. Resolution is read-only: require exit 0, `status: selected` and `native_registry_verified: true`, then read the returned `instructions` before the `entrypoint`. Missing or conflicting registration fails closed; do not fabricate IDs or edit JSON to bypass it. For an existing registered vault, start with resolution. A new registration of an existing vault requires the owner's intended destination and authorization.

Native registry defaults are macOS `~/Library/Application Support/obsidian/obsidian.json`, Linux `$XDG_CONFIG_HOME/obsidian/obsidian.json` (or `~/.config/obsidian/obsidian.json`), and Windows `%APPDATA%/obsidian/obsidian.json`. For a nonstandard installation, verify the real native location and use `--nativo "PATH"` on both commands. Use `--registro "PATH"` only for an explicitly selected alternative local registry. These paths are defaults, not proof that Obsidian is installed or running.

Optionally add `--proyecto "/absolute/CodexProject"` to registration, then resolve with `python scripts/resolver_boveda_codex.py --project "/absolute/CodexProject"`. The explicit project or a child path must match exactly one registered association; there is no implicit current-folder or active-window selection.

Use [the startup prompt](../../GET_STARTED_WITH_CODEX.md) to continue through discovery, source review, knowledge architecture, useful writing, review, and a real task. A template or provisional capture does not finish this work.

## Existing business instance

Do not run `crear`, copy templates over the vault, or restart the initial interview. Use [the continuation prompt](../../CONTINUE_WITH_CODEX.md). Before listing or reading inside the vault, resolve it through `obsidian-router`, verify native Obsidian registration, and read its local instructions. An active window or a typed path is not sufficient verification.

If routing is unavailable, preserve authorized work outside the vault and leave vault access/integration pending. Do not invent a registry or claim the environment was checked. Routine use does not require a full installation acceptance campaign.

## Verify the appropriate outcome

For product development, run the tests in [development](development.md). For installation or integration acceptance, use [testing](testing.md) and the dedicated acceptance procedure. Verify structural integrity, Obsidian GUI, semantic retrieval, and business usefulness separately. A synthetic test cannot approve a real business decision.

Next: [User guide](user-guide.md).
