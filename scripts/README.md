# Scripts

| Script | What it does | Run |
|---|---|---|
| `check_numbers.py` | Recounts every number in the [numbers register](../research/numbers.md) from the record files in `research/data/`, and fails if any has drifted | `python scripts/check_numbers.py` |
| `build_visuals.py` | Regenerates the animated pictures in `assets/`. It counts the research numbers live from `research/data/`, so the visuals can't drift from the records. | `python scripts/build_visuals.py` |
| `sandbox_check.py` | Checks Airwallex's sandbox before the build. It creates or reuses two euro Global Accounts, one per example client, simulates a messy deposit into each, and reads the deposits back to show exactly what a deposit carries. It's a sandbox test, not product code. | `python scripts/sandbox_check.py` |

## Sandbox check setup

1. Create a sandbox account at [sandbox.airwallex.com](https://sandbox.airwallex.com). The business name must be "Sandbox Business" or "New Business Sandbox", or it stays in review ([Builder Guide](https://airwallexdev.com/agentic-banking-builder-guide.md)).
2. Copy `.env.example` to `.env` in the repo root and add your sandbox client ID and API key. `.env` is git-ignored; never commit keys.
3. Run `python scripts/sandbox_check.py`. Add `--no-deposit` to only re-read accounts and deposits.

The script refuses to run against anything but the sandbox. Raw responses are saved to `scripts/out/`, which is git-ignored.
