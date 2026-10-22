# Guide for AI assistants working in this repository

This repository is the team's shared memory for Receive to Reconciled. Read this file first, then the [README](README.md).

## What this project is

An agent for small businesses paid from abroad. It matches each incoming payment to invoices, explains why it's short, fixes the cause, and decides whether to keep or convert currency. It runs on Airwallex. It's being built for the Airwallex Agentic Banking Hackathon (build window 25 Oct – 13 Nov 2026) by a team of two.

## Where the truth lives

| Question | Look here | Don't trust |
|---|---|---|
| What is the product, and why? | `docs/01-problem.md`, `docs/02-solution.md` | Old wording in chat history |
| How does it work? | `docs/03-architecture.md` | |
| What can Airwallex do? | `docs/04-airwallex-integration.md`, then Airwallex's live docs | Memory of the API; check the docs |
| Which problems matter, and why? | `research/data/pains.csv`, `docs/05-pain-atlas.md` | |
| Is a number correct? | `research/numbers.md`; run `python scripts/check_numbers.py` | Any number not in the register |
| Where did a quote come from? | `research/citations.md`, then the CSV row by its ID | |
| What did we decide, and when? | `docs/10-decision-log.md` | |
| What are we building this week? | `docs/06-build-plan.md` | |

## House rules

1. **Every factual claim has a source.** Put an inline link and a date next to it, and add it to `research/citations.md` if it's new. Quotes are word for word, in quotation marks. Never invent a link, quote, number or API field.
2. **Every number goes in the register first.** If you write a new number about our research, add a row to `research/numbers.md` with a recount rule in `scripts/check_numbers.py`, and run the check.
3. **Say what you couldn't confirm.** Write "not confirmed" plainly.
4. **Write in the team's voice ("we"), in plain language.** Explain every finance term on first use, and link to the glossary.
5. **Examples are labelled as examples,** with the arithmetic shown in full.
6. **Architecture principle:** rules in code make every decision about money. A language model only reads messy text, and its output is checked against the numbers. Outside text can never move money.
7. **Decisions go in the decision log** as new rows. Never rewrite history.
8. **Generated files aren't edited by hand:** `docs/05-pain-atlas.md` and everything in `research/data/`. They come from the research export.

## Record files (`research/data/`)

| File | Rows | ID column | What one row is |
|---|---|---|---|
| `ideas-compared.csv` | 35 | `name` | An idea we scored before choosing |
| `repos-reviewed.csv` | 57 | `repo` | A public repository we read (column `entrant`) |
| `evidence-test-ledger.csv` | 476 | `id` (V001…) | A sourced item testing a claim (`claim_id`: R1–R10 for this product) |
| `pain-map-items.csv` | 429 | `id` (L1#0…, F1#0…) | A sourced item about a day-to-day problem; `pain_id` links it to a problem |
| `pains.csv` | 56 | `id` (A01…) | A distinct problem, with scores and the build call |
| `hypotheses.csv` | 20 | `id` (H1…) | A question tested in advance, with its verdict |
| `game-changers-and-non-pains.json` | — | — | Cause-fixing opportunities, and problems judged too small to build for |

Stage IDs (S1–S10) and segment IDs (G1–G8) are defined in `docs/08-research-method.md`.
