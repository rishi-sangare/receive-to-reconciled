# Numbers register

Every number we quote about our research is listed here, with what it means and the file you can open to check it. `python scripts/check_numbers.py` recounts each one from the files and fails if any number here has drifted.

If you write a new number in the README, the docs or a submission, add a row here first.

## Choosing the problem (12–17 October 2026)

| Key | Number | What it means | Record |
|---|---|---|---|
| `ideas_compared` | **35** | Distinct ideas for an agentic banking product we described and scored before choosing | [ideas-compared.csv](data/ideas-compared.csv) |
| `repos_reviewed` | **57** | Public GitHub repositories we read on 16–17 October to see what others were building | [repos-reviewed.csv](data/repos-reviewed.csv) |
| `repos_entrants` | **44** | Of those, repositories that identify themselves as entries to this hackathon. The rest are reference builds or unrelated projects. | [repos-reviewed.csv](data/repos-reviewed.csv), column `entrant` |

## Testing the evidence for the two finalists (21 October 2026)

| Key | Number | What it means | Record |
|---|---|---|---|
| `evidence_items` | **476** | Sourced items collected to test the claims behind our two finalist ideas, Receive to Reconciled and a payables-timing agent. Each has a quote, a link and a date. | [evidence-test-ledger.csv](data/evidence-test-ledger.csv) |
| `evidence_items_r2r` | **226** | Of those, items about Receive to Reconciled | same file, column `problem` |
| `evidence_rechecked_ok` | **385** | Items re-opened in a separate checking pass and confirmed: exactly as quoted (299) or confirmed with a correction (86) | same file, column `check` |
| `evidence_verified_exact` | **299** | Confirmed exactly as quoted | same file, `check` = verified |
| `evidence_verified_corrected` | **86** | Confirmed with a correction, which is recorded in `check_note` | same file, `check` = partly |
| `evidence_wrong` | **1** | Found to be wrong on re-checking, and not used | same file, `check` = wrong |
| `evidence_unreachable` | **28** | The page could not be re-opened during checking | same file, `check` = unreachable |
| `evidence_not_rechecked` | **62** | Items gathered by the skeptic pass that were not re-checked one by one. Their key claims were re-checked in a second round. | same file, `check` = unchecked |

## Mapping the problems (21–22 October 2026)

| Key | Number | What it means | Record |
|---|---|---|---|
| `pain_items` | **429** | Sourced items describing day-to-day problems, from sending an invoice to closing the books | [pain-map-items.csv](data/pain-map-items.csv) |
| `pain_items_main` | **325** | Items from the main run, eight source families each with its own checker | same file, `round` = main |
| `pain_main_rechecked_ok` | **318** | Main-run items re-opened by a checker and confirmed, exactly or with a correction | same file, `check` = verified or partly |
| `pain_main_wrong` | **2** | Main-run items found wrong on checking | same file, `check` = wrong |
| `pain_main_unreachable` | **5** | Main-run items whose page could not be re-opened | same file, `check` = unreachable |
| `pain_items_followup` | **104** | Items from a follow-up on whether clients switch bank details. Each collector re-opened its own sources. | same file, `round` = follow-up |
| `pain_followup_hand_checked` | **13** | Follow-up items we re-opened by hand, or that an earlier checker had confirmed on the same page | same file, follow-up rows with `check` = verified |
| `veteran_insights` | **180** | Items that record a practitioner's rule of thumb (for example, "don't chase tiny gaps") | same file, column `veteran_insight` |
| `pains` | **56** | Distinct problems after grouping the items | [pains.csv](data/pains.csv) |
| `pains_build_first` | **7** | Problems we build for first | same file, `build_call` |
| `pains_build_later` | **11** | Problems for after the core works | same file |
| `pains_mention_only` | **20** | Real, but not worth a feature now | same file |
| `pains_out_of_scope` | **18** | Too rare, too small, or outside our customers | same file |
| `hypotheses` | **20** | Questions we set out to test before collecting | [hypotheses.csv](data/hypotheses.csv) |
| `hypotheses_confirmed` | **9** | Confirmed by the evidence | same file |
| `hypotheses_weakened` | **11** | Weakened: real but smaller, rarer, partly solved, or thinly evidenced | same file |

## Numbers in our examples

The worked examples (the €930 payment, the example week) are made up to show how the agent behaves. They are labelled as examples wherever they appear, and their arithmetic is shown in full.
