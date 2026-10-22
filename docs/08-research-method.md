# How we researched this

Between 12 and 22 October 2026 we researched the problem before designing anything. This page explains what we did, in what order, how we checked it, and where it falls short. Every number here is in the [numbers register](../research/numbers.md), with the file that backs it.

## Our rules for evidence

- **Every item is a real source.** Each one has a link, a date and a word-for-word quote. Nothing is paraphrased inside a quote.
- **Every source is checked a second time where possible.** A separate checking pass re-opened the page and confirmed the quote, the date and that our summary didn't overstate it.
- **Evidence against us counts as much as evidence for us.** We looked for signs that each problem is rare, already solved or too small.
- **Sales pitches are labelled.** Posts by people selling a tool for the problem are marked `promotional` and count for less.
- **We say what we couldn't find.** Gaps are listed at the end of this page.

We ran the searching and checking with AI research assistants, given strict instructions: real links only, word-for-word quotes, dates, and a separate checking pass. Then we read the results, ran our own spot checks, and made every decision ourselves.

## Step 1: Choosing the problem (12–17 October)

We wrote down and scored **35 ideas** for an agentic banking product ([ideas-compared.csv](../research/data/ideas-compared.csv)). They were narrowed in rounds:

| Date | Round | What happened |
|---|---|---|
| 12 Oct | Idea lab | 13 directions scored on 6 criteria (out of 30) |
| 13 Oct | Payment-chain sweep | 33 candidate ideas along the path money takes, grouped into families and scored out of 35 |
| 16–17 Oct | Deep dives | The top families researched in depth and re-scored out of 35 |
| 16–17 Oct | What others are building | We read **57** public repositories, **44** of them entries to this hackathon ([repos-reviewed.csv](../research/data/repos-reviewed.csv)) |
| 21 Oct | Evidence test | The two finalists tested against the evidence (step 2) |

Receive to Reconciled scored highest, or joint highest, in every round it entered.

## Step 2: Testing the evidence (21 October)

For our two finalists, Receive to Reconciled and an agent that times payments to suppliers, we wrote down every claim each idea depended on. Then we tested those claims against **476 sourced items** ([evidence-test-ledger.csv](../research/data/evidence-test-ledger.csv)). The sources were regulators, official surveys, company filings, court records, academic papers, accounting forums, feature requests, job ads and product reviews.

| Check result | Items |
|---|---|
| Re-opened and confirmed exactly as quoted | 299 |
| Re-opened and confirmed with a correction (noted in the file) | 86 |
| Found wrong, and not used | 1 |
| Page couldn't be re-opened | 28 |
| Gathered by the skeptic pass and not re-checked one by one | 62 |

So **385** of the 476 were re-opened and confirmed. A skeptic pass then argued against each idea, and a second round filled the gaps it exposed. Receive to Reconciled came out ahead. Its core claims held up: payments arrive short, one payment covers several invoices, deductions arrive silently, and the payer is often a different company. Its weakest claims were about size and willingness to pay, and we say so in the [risks](07-risks.md).

## Step 3: Mapping the problems (21–22 October)

Once we'd chosen the problem, we mapped every day-to-day problem from the moment an invoice is sent to the moment the books are closed. We split that journey into ten stages and studied eight kinds of business, as defined below. We set out **20 questions** in advance (the hypotheses) and tested them all.

**Eight source families, each with its own checker** (the main run, **325 items**):

| Source family | What it covered |
|---|---|
| Bookkeeper and accountant voices | First-hand stories from accounting forums |
| Feature boards and app reviews | Requests to accounting tools, with vote counts |
| Payment-provider complaints | Problems receiving money through providers and banks |
| Indian exporters, freelancers and accountants | Export paperwork under the 2026 rules |
| Standards, data and Airwallex docs | What information survives a payment, and what Airwallex provides |
| Veteran know-how | Procedures, training, job ads and audit guidance |
| Open-source and developer edge cases | Bug reports in open-source accounting software |
| The payer's side | How customers' accounts teams pay and verify new bank details |

Of the 325, **318** were re-opened by a checker and confirmed, 2 were wrong and 5 couldn't be reached. A skeptic then argued that each problem was rare, already solved or too small. A gap-finder listed what we'd missed, and that led to a **follow-up of 104 items** on the biggest open question: will clients actually switch to new bank details? In the follow-up, each collector re-opened its own sources, and we re-opened **13** key ones by hand.

In total: **429 items**, grouped into **56 distinct problems** ([pains.csv](../research/data/pains.csv)), and **180** practitioners' rules of thumb ([pain-map-items.csv](../research/data/pain-map-items.csv), column `veteran_insight`).

### The ten stages

| ID | Stage | What happens |
|---|---|---|
| S1 | Set up the customer | Terms, currency, which bank details to give |
| S2 | Send the invoice | Invoice details, references, the customer's approval process |
| S3 | Customer pays | Their bank, their route, their choice of who pays fees |
| S4 | Money in transit | Delays, "we paid" claims, holds |
| S5 | Money arrives | Short references, payer names that don't match |
| S6 | Identify and match | Which customer, which invoices |
| S7 | Exceptions and follow-up | Chasing, disputes, refunds, unidentified money |
| S8 | Book it | Accounting entries, fees, exchange-rate differences |
| S9 | Compliance and reporting | Tax certificates, India's export records, audit |
| S10 | Use the money | Keep or convert, cash planning, paying suppliers |

### The eight kinds of business

| ID | Who |
|---|---|
| G1 | Indian software, design and services exporters (5–100 staff) |
| G2 | Indian freelancers paid from abroad |
| G3 | Agencies and consultancies in Singapore, the UK, Australia and Hong Kong |
| G4 | Goods exporters selling to business buyers |
| G5 | Bookkeepers and accountants serving many small clients |
| G6 | Receivables clerks at mid-sized firms |
| G7 | The paying customer's accounts-payable team |
| G8 | Sellers paid out by platforms such as Stripe or Amazon |

The 20 questions and their verdicts (9 confirmed, 11 weakened) are in [hypotheses.csv](../research/data/hypotheses.csv).

## Scoring

Each of the 56 problems is scored from 1 to 5 on six measures:

| Measure | Question | How it's set |
|---|---|---|
| How often | Weekly, monthly or rare? | Judgement against the items |
| How much it hurts | Money lost, hours spent, cash delayed, audit or fraud risk | Judgement against the items |
| How widely it's felt | How many kinds of business report it | Counted from the items |
| How strong the evidence is | Checked, non-promotional items | Counted from the items |
| Unsolved | Do today's tools already handle it? | Judgement, including the skeptic's case |
| Fixable on Airwallex | Can an agent using Airwallex's APIs fix it, or its cause? | Judgement against Airwallex's documentation |

A fix that stops a problem from coming back earns **2 more points**, so the maximum is 32. The build call (build first, build later, mention only, out of scope) was then made with the scores and the skeptic's case side by side. The judgement scores carry a one-line reason in [pains.csv](../research/data/pains.csv).

## What changed our plan

- **Airwallex already lets a business give each customer its own account,** and matches payments that arrive in full. We build on that feature instead of claiming it.
- **Clients switch bank details slowly.** Their accounts teams phone a known contact, ask for signed letters, and sometimes freeze new details for weeks. We designed the switch as a guided process.
- **Not every short payment is a bank fee.** Discounts, deductions, tax and the payer's own recalculations all appear, so the agent looks for evidence before naming a cause.
- **Deciding whether to keep or convert money had little direct evidence.** It stays in the product, but it isn't our headline.

## Limits

- **No study measures how often** small cross-border sellers are paid short. Our frequency scores are judgement, based on first-hand reports.
- **Several sites blocked automated reading.** Reddit was read through a public archive. AccountingWEB, G2 and Capterra were mostly unreachable.
- **Some sources are vendors** writing about problems their products solve. They're labelled, and they count for less.
- **Recent rules change quickly.** India's export rules took effect in 2026 and are still being clarified.
- **The follow-up items had no separate checker.** Each collector re-opened its own sources, and we spot-checked 13.
