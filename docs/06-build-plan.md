# Build plan: 25 October to 13 November 2026

We have three weeks, two people and modern AI coding tools. That changes what is realistic. We don't plan one feature a week. We plan to have **the whole product working end to end in week 1**, to **widen and test it hard in week 2**, and to **refine it into something a business would trust in week 3**.

The plan is built in layers. Each layer works on its own before the next one starts, so if anything slips, we lose a layer at the top, not a half-built feature in the middle.

**Who does what.** Two tracks run side by side every day:

- **Builder A, the engine:** the Airwallex connector, ledger, matching, gap explainer, rules and limits, cash planner.
- **Builder B, the product:** the document reader, dashboard, approval cards, cause-fix workflow, India module, demo and documentation.

We'll assign names on day 1. Both builders review each other's work every evening.

## At a glance

| Week | Goal | By the end of the week, you can see… |
|---|---|---|
| **Week 1 (Sun 25 – Sat 31 Oct)** | The whole product, end to end | A messy payment arrives in the Airwallex sandbox. It is matched and its gap explained. An unclear case reaches a person. A client is given its own account. Euros are kept or converted, and a supplier is paid. |
| **Week 2 (Sun 1 – Sat 7 Nov)** | Every important case, and tested hard | The India module, more kinds of short payments, more than 40 realistic test payments, attack tests, and feedback from real bookkeepers and exporters |
| **Week 3 (Sun 8 – Fri 13 Nov)** | Refined, trustworthy, presented | A clean dashboard, clear explanations, a hardened service, setup instructions, a demo video under 5 minutes, submitted on Thu 12 Nov with a day to spare |

## Week 1: build the whole product

| Day | Builder A: the engine | Builder B: the product | Done when |
|---|---|---|---|
| **Sun 25 Oct** | Sandbox account and API keys. Run the [smoke test](../scripts/README.md): create two euro Global Accounts, simulate deposits, read them back. Record exactly what a deposit carries. | Repo set up for code: project skeleton, linting, tests and CI. Write the 40 test payments from the [pain atlas](05-pain-atlas.md) as data files (amount, payer name, reference, client email, expected result). | We know from real sandbox responses what Airwallex gives us. The test payments exist before the code does. |
| **Mon 26 Oct** | Airwallex connector: login and token refresh, the deposits list, webhook receiver with signature check and duplicate protection, re-reading recent deposits on a timer. | Ledger tables: clients, invoices, known payer names, deposits, matches, gap parts, approvals, audit log. Seed one demo business with clients and invoices. | A simulated deposit appears in our ledger within seconds, exactly once. |
| **Tue 27 Oct** | Matching engine: account first, then reference, then known payer name, then a bounded search over combinations within tolerances. Confidence levels. | Document reader: take a client email or PDF and extract invoice numbers, amounts and deductions, each pointing to its source words. Checks that reject anything that doesn't add up. | The €930 example matches to the right two invoices, and the client's email is read correctly. |
| **Wed 28 Oct** | Gap explainer: fee bands per route, credit notes and discounts on file, round-percentage tax, unknown remainder. Parts must sum to the cent. Rules and limits for when a person is needed. | Dashboard, first version: exception queue, approval card (amount, evidence, the suggested answer), audit trail for each deposit. | A gap is split correctly or sent to a person with a clear question. A person can approve in the dashboard. |
| **Thu 29 Oct** | Cause-fix rules: client scorecard (short payments, missing references, route), triggers, cheapest fix first. Open a Global Account for a client through the API. | The bank-change pack: a letter with old and new details, contacts on file for the callback, steps for supplier portals. The switch tracker, with its states. | A client with three short payments is offered its own account, and the pack is ready for the owner to approve. |
| **Fri 30 Oct** | Cash planner: what's certain, what's expected and how strong the evidence is, bills due. Keep-or-convert decision, locked FX quote, conversion, transfer to a supplier. | "Before any reminder" check. Notifications for the owner. Dashboard views for the cash plan and approvals. | The example week runs: Monday's plan, Tuesday's deposit, Wednesday's delay, the revised plan, Friday's payment. |
| **Sat 31 Oct** | End-to-end run of all 40 test payments; fix what fails. | End-to-end run from the dashboard; fix what's confusing. Write down every gap we found. | **The whole loop works in the sandbox.** Everything after this is widening and refining. |

## Week 2: widen it and test it hard

| Days | Builder A: the engine | Builder B: the product | Done when |
|---|---|---|---|
| **Sun 1 – Mon 2 Nov** | Short-payment causes beyond fees: withheld tax (ask for the certificate), early-payment discounts, deductions, disputes. Overpayments and duplicates, with a proposed refund or credit. | India module: import the bank's list of open export records, link each payment to its record, compute shortfalls, draft the note to the bank. | Each cause in the [pain atlas](05-pain-atlas.md) marked "build first" or "build later" has at least one passing test. |
| **Tue 3 Nov** | Part payments and instalments: a running balance per invoice. Saving half-done matches. Payer-name learning after one confirmation. | Remittances that arrive later than the money: attach them to waiting deposits automatically. | A payment that arrives before its explanation is matched when the explanation comes. |
| **Wed 4 Nov** | Held deposits: handle Airwallex's pending and review states, and prepare the documents usually asked for. Currency mismatch: an invoice in USD paid in EUR. | Unidentified money: aged by week, with a monthly list of likely owners. Dashboard filters and search. | Nothing is ever silently lost. Every deposit is matched, waiting with a reason, or with a person. |
| **Thu 5 Nov** | Attack tests: instructions hidden in PDFs and emails, duplicate and out-of-order webhooks, retries after timeouts, tampered approvals, approval after the quote expires. | Usability pass: every screen explains itself in plain words; every number links to its evidence. | All attack tests pass. No path lets text from outside move money. |
| **Fri 6 – Sat 7 Nov** | Load and timing: a month of payments for 50 clients replayed in minutes. Fix slow paths. | Feedback sessions with 3–5 bookkeepers or exporters on the dashboard. Capture what confused them. | Real users have tried it. We have a list of what to fix in week 3. |

## Week 3: refine, harden, present

| Days | Builder A: the engine | Builder B: the product | Done when |
|---|---|---|---|
| **Sun 8 – Mon 9 Nov** | Fix everything from the feedback sessions. Tighten the rules where users disagreed with the agent. | Fix everything from the feedback sessions. Polish the approval card and the client scorecard ("fees lost to bank charges this quarter: €105"). | The feedback list is empty or explained. |
| **Tue 10 Nov** | Hardening: secrets handling, logging, error recovery, a full replay of the demo from an empty database. | README, setup instructions, architecture diagrams updated to match the code. | A stranger can set it up from the README alone. |
| **Wed 11 Nov** | Demo data and script locked. Rehearse the example week three times. | Record the demo video, under 5 minutes: goal, plan, new information, revised decision, money moved. | The video tells the story without narration over code. |
| **Thu 12 Nov** | Final checks: every test passes, and the sandbox demo runs cleanly. | Submit: repo link, video, setup instructions. | **Submitted, one day early.** |
| **Fri 13 Nov** | Buffer for anything that broke. | Buffer. | Deadline 23:59 IST. |

## What we will not build in these three weeks

These problems are real, but they're either solved elsewhere or too far from the core. They stay on the roadmap ([pain atlas](05-pain-atlas.md), "Mention only" and "Out of scope").

- Payouts from platforms such as Stripe, PayPal and Amazon. These are already served by tools like A2X. We may add one payout-shaped test payment if time allows.
- A dashboard for bookkeepers who manage many client businesses.
- Tracking SWIFT payments in transit.
- Any filing on behalf of the business with tax authorities or banks. We draft; people file.

## Risks to the plan, and what we'd drop first

| If this happens | We do this |
|---|---|
| The sandbox doesn't allow several euro accounts, or one per client | Demonstrate the switch with one account per currency, and note it as a production step |
| A sandbox deposit can't carry the details we need | Use the simulation interface for realistic data, kept behind one interface as the Builder Guide recommends |
| Week 1 runs over | Drop load testing first, then the India module's bank-note drafting. The core loop always stays. |
| Feedback sessions can't be arranged | Use the practitioner rules of thumb from our research as review criteria |
