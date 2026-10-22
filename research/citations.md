# Sources

This file lists every outside source our repository links to. Every claim in our docs links to a source, and every one of those sources is listed here: what it says, the exact words we quote, how we use it, and how much weight it can carry.

- **C-numbers.** Each source has a number, C01 to C61, so we can refer to it in short ("see C09"). To find the entry for a link in one of our docs, search this page for the link's address.
- **Research records.** Most of our evidence lives in [`data/pain-map-items.csv`](data/pain-map-items.csv) (429 items) and [`data/evidence-test-ledger.csv`](data/evidence-test-ledger.csv) (476 items). Each row there has its own quote, link, date and check result (`verified`, `partly`, `wrong`, `self-checked`, `unreachable` or `unchecked`), with notes in `check_note`. Where a source below is also in those files, its entry gives the row IDs and their results.
- **Dates.** Where a page shows no date we say "undated"; "read 21 Oct 2026" means the date our records say we read it.
- **Weight, in short:** official or regulator text is the strongest; a survey depends on its year and sample; vendor content is about a problem the vendor sells a fix for; a forum post, feature request or job ad is one person's or one company's experience, not a measured rate; news reports what others said.

We re-opened 52 of these sources on 22 Oct 2026 and checked that the words we quote are on the page. The results are at the end of this file.

## Airwallex (official)

### C01 · Building on Airwallex (the Agentic Banking Builder Guide)

- **Publisher / author:** Airwallex, on its developer site airwallexdev.com. **Date:** undated.
- **Link:** https://airwallexdev.com/agentic-banking-builder-guide.md
- **What it says:** Airwallex's guide for hackathon builders. It asks builders to "Choose a finance task that someone repeats and identify the decision inside it", says "The agent should choose differently when a balance, deadline, piece of evidence, or risk changes.", and says of reconciliation, which has no starter kit: "Good territory if you want a problem few other builders will take on". It also has sandbox notes we quote: "a 30-minute bearer token", "A rate is not a quote", "the request takes no `currency` field; if you send one, Airwallex discards it without an error" and "Although the deposit response says PENDING, the balance appears immediately."
- **How we use it:** Why we picked our own Treasury & Ops idea; the decision inside the job; how we log in, what the deposit simulation cannot do, keeping sandbox-only calls replaceable, and using made-up demo data. Cited in [02-solution](../docs/02-solution.md), [03-architecture](../docs/03-architecture.md), [04-airwallex-integration](../docs/04-airwallex-integration.md), [07-risks](../docs/07-risks.md), [10-decision-log](../docs/10-decision-log.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** Official guide from the hackathon's host. It tells us what Airwallex wants to see, not what customers need.
- **Record:** Cited directly; not part of the research records.

### C02 · Airwallex Agentic Banking Hackathon

- **Publisher / author:** Airwallex, hosted on HackerEarth. **Date:** undated (the page gives the event dates Oct 25 – Nov 19, 2026).
- **Link:** https://airwallex.hackerearth.com/
- **What it says:** The hackathon's home page: online and global, with prizes and credits. We quote no words from it.
- **How we use it:** Names the hackathon this repository is for. Cited in [README](../README.md).
- **How much weight it carries:** Official event page; used only to identify the event.
- **Record:** Cited directly; not part of the research records.

### C03 · airwallex developer lab (llms.txt)

- **Publisher / author:** Airwallex, on its developer site airwallexdev.com. **Date:** undated.
- **Link:** https://airwallexdev.com/llms.txt
- **What it says:** A plain-text summary of builder notes. Among its gotchas: "country_code is the account country, not the currency. NL/DE/FR for EUR. BE is rejected.", "required_features is an array of objects, not strings.", "Developer MCP cannot create a Global Account." and "A failed transfer ends in CANCELLED, not FAILED".
- **How we use it:** Sandbox pitfalls we plan around when creating accounts and testing transfers. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official developer notes, short and undated, so we re-test each point in the sandbox.
- **Record:** Cited directly; not part of the research records.

### C04 · Treasury concepts

- **Publisher / author:** Airwallex Docs. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/global-treasury/understanding-global-treasury/treasury-concepts
- **What it says:** Global Accounts "only act as conduits ... and do not hold balances", and "You can create multiple Global Accounts programmatically".
- **How we use it:** What a Global Account is, and that a business can open more than one. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official Airwallex documentation; it says what the product is meant to do, and we still test it in the sandbox. It gives no upper limit.
- **Record:** Cited directly; not part of the research records.

### C05 · Global Accounts

- **Publisher / author:** Airwallex Docs. **Date:** undated (read 21 Oct 2026).
- **Link:** https://www.airwallex.com/docs/accounts/get-started/global-accounts
- **What it says:** Says "If your business requires a large number of Global Accounts, please contact your Airwallex Account Manager", and that a nickname is "for your own record keeping only, and will not show up on bank statements".
- **How we use it:** Why we plan for a handful of per-customer accounts, not one per invoice; what a nickname does. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official Airwallex documentation; it says what the product is meant to do, and we still test it in the sandbox. No hard limit on the number of accounts is published.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L5#16 (partly), L5#19 (partly), F2#11 (self-checked).

### C06 · Manage Global Accounts

- **Publisher / author:** Airwallex Docs. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/global-treasury/get-started/global-accounts/manage-global-accounts
- **What it says:** After creation, "Other account details cannot be changed". You cannot close "the first Global Account opened under your Airwallex account", and for late payments to a closed account "the amount returned may be less than the original amount".
- **How we use it:** What can change after an account is opened, and the risk of closing one. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official Airwallex documentation; it says what the product is meant to do, and we still test it in the sandbox.
- **Record:** Cited directly; not part of the research records.

### C07 · Market & infrastructure coverage

- **Publisher / author:** Airwallex Docs. **Date:** Global Accounts table marked "Updated on Aug 15, 2025" (shown on the web page; the .md copy shows no date).
- **Link:** https://www.airwallex.com/docs/global-treasury/market-and-infrastructure-coverage (also cited as https://www.airwallex.com/docs/global-treasury/market-and-infrastructure-coverage.md)
- **What it says:** A table of where Global Accounts can be opened and how they receive money. Germany and the Netherlands take EUR by SEPA, with SWIFT "No"; Singapore takes 13 currencies, with local methods for SGD; India is not a receiving region.
- **How we use it:** Local routes versus SWIFT; why there is no rupee account on Airwallex. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md), [india-module](../docs/india-module.md).
- **How much weight it carries:** Official table. It lists where accounts sit, not which accounts a business registered in a given country may open (see record L5#17).
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L5#17 (partly), L5#18 (partly).

### C08 · Eligible Countries and Territories

- **Publisher / author:** Airwallex Help Centre. **Date:** undated.
- **Link:** https://help.airwallex.com/hc/en-gb/articles/4408591334937
- **What it says:** A table that maps each country of registration to the Airwallex entity that serves it. India maps to Singapore. We quote no words from it.
- **How we use it:** India-registered businesses are onboarded through Airwallex Singapore. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md), [india-module](../docs/india-module.md).
- **How much weight it carries:** Official help page. It shows the mapping, not which accounts that entity lets an Indian business open.
- **Record:** Cited directly; not part of the research records.

### C09 · Dedicated Account per Customer

- **Publisher / author:** Airwallex Docs. **Date:** undated (read 21 Oct 2026).
- **Link:** https://www.airwallex.com/docs/payments/payment-methods/global/bank-transfer/dedicated-account-per-customer
- **What it says:** In Airwallex Payments, each customer can get its own bank account, and "we automatically reconcile incoming transfers with your outstanding payments". With no reference it settles "as many payments as possible that can be fully funded"; in its example "Payment 3 remains pending, as the remaining 90 USD is not enough to fully fund it". A customer balance is "Coming soon".
- **How we use it:** What Airwallex already does (per-customer accounts, matching payments that arrive in full) and what it leaves to a person (a short payment stays "pending"). Cited in [README](../README.md), [02-solution](../docs/02-solution.md), [04-airwallex-integration](../docs/04-airwallex-integration.md), [07-risks](../docs/07-risks.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** Official documentation of a feature that overlaps with ours. We use it to avoid claiming what Airwallex already offers.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L5#12 (verified), L5#13 (partly).

### C10 · Bank transfer

- **Publisher / author:** Airwallex Docs. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/payments/payment-methods/global/bank-transfer
- **What it says:** Overview of bank transfers in Airwallex Payments. Its table says "Available for businesses registered in" "CN, HK, EU, AU, CA, NZ, SG, UK, US", and you must "contact your Airwallex Account Manager to select your preferred model".
- **How we use it:** Who can use the per-customer account feature, and that it needs an account manager. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official Airwallex documentation; it says what the product is meant to do, and we still test it in the sandbox. Our quote joins two cells of one table row.
- **Record:** Cited directly; not part of the research records.

### C11 · Accept SWIFT bank transfers

- **Publisher / author:** Airwallex Docs. **Date:** undated (read 21 Oct 2026).
- **Link:** https://www.airwallex.com/docs/payments/payment-methods/global/bank-transfer/accept-swift-bank-transfers
- **What it says:** Airwallex warns that "customers may believe they have paid the full amount, while you receive less than expected due to fees deducted during the transfer".
- **How we use it:** Airwallex itself says SWIFT receipts can arrive short, and deposits do not show the fee taken. Cited in [07-risks](../docs/07-risks.md).
- **How much weight it carries:** Official documentation; it confirms the problem exists but gives no rate. Record L5#11 (marked wrong) is a different claim from this page, not the quote we use.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L3#22 (verified), L5#10 (verified), L5#11 (wrong).

### C12 · Retrieve your deposits

- **Publisher / author:** Airwallex Docs. **Date:** undated (read 21 Oct 2026).
- **Link:** https://www.airwallex.com/docs/global-treasury/receive-funds/receive-bank-transfers-to-global-accounts/retrieve-your-deposits
- **What it says:** Says "the availability of deposit details (e.g. payer name, payer bank account number etc.) will vary".
- **How we use it:** Payer details on a deposit may be missing, so the agent cannot rely on them. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official Airwallex documentation; it says what the product is meant to do, and we still test it in the sandbox.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L5#1 (verified).

### C13 · Bank transfer deposit statuses

- **Publisher / author:** Airwallex Docs. **Date:** undated (read 21 Oct 2026).
- **Link:** https://www.airwallex.com/docs/global-treasury/receive-funds/receive-bank-transfers-to-global-accounts/bank-transfer-deposit-statuses
- **What it says:** PENDING means "Deposit has arrived and is on hold for review. Most deposits are auto-cleared and moved into the settled state".
- **How we use it:** A held deposit has arrived but cannot be used yet. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official Airwallex documentation; it says what the product is meant to do, and we still test it in the sandbox. It gives no maximum hold time (see record L5#3).
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L5#3 (partly), F3#16 (verified).

### C14 · My incoming deposit is not settled or missing

- **Publisher / author:** Airwallex Help Centre. **Date:** undated (read 21 Oct 2026).
- **Link:** https://help.airwallex.com/hc/en-gb/articles/900006978063-My-incoming-deposit-is-not-settled-or-missing
- **What it says:** Review "usually takes less than one business day", and a deposit tagged "RFI requires response" waits until the business replies.
- **How we use it:** How long holds last, and when they need a reply. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official help page; "usually" is Airwallex's own description, not a measured figure.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L5#7 (verified), L5#8 (verified), F3#17 (verified), F3#18 (self-checked), F3#19 (self-checked), F3#20 (self-checked).

### C15 · Handle Transaction RFI

- **Publisher / author:** Airwallex Docs. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/global-treasury/risk/rfi-%28request-for-information%29/handle-transaction-rfi
- **What it says:** An RFI (request for information) is "commonly a request for supporting documents" "such as invoices or contracts".
- **How we use it:** Why the agent can help by attaching the matching invoice to a held deposit. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official Airwallex documentation; it says what the product is meant to do, and we still test it in the sandbox.
- **Record:** Cited directly; not part of the research records.

### C16 · Deposits (webhook events)

- **Publisher / author:** Airwallex Docs. **Date:** undated (read 21 Oct 2026).
- **Link:** https://www.airwallex.com/docs/developer-tools/webhooks/listen-for-webhook-events/deposits
- **What it says:** Lists deposit.pending, deposit.settled, deposit.rejected and deposit.reversed; reversed means "recalled by the payer's bank after the funds were settled to your Wallet".
- **How we use it:** Which live alerts start the agent's work. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official documentation. The reversed example on the page is a direct debit, so it does not show that bank transfers get reversed (see record L5#4).
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L3#23 (partly), L5#4 (partly).

### C17 · Confirmation of Payee in Australia

- **Publisher / author:** Airwallex Help Centre. **Date:** 25 Sep 2026 (from our records; the page shows no date).
- **Link:** https://help.airwallex.com/hc/en-gb/articles/12899686813839-Confirmation-of-Payee-in-Australia
- **What it says:** A payer who types "your common business name instead of the official account name" may see a "no match" or "close match" warning, and Airwallex "will never stop you from completing a payment".
- **How we use it:** What a payer sees when we ask a client to pay into new account details. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official help page, for Australia only.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) F2#0 (verified), F2#1 (verified), F4#36 (verified), F4#37 (verified).

### C18 · Verify a beneficiary account

- **Publisher / author:** Airwallex Docs. **Date:** undated (read 21 Oct 2026).
- **Link:** https://www.airwallex.com/docs/payouts/beneficiaries/verify-a-beneficiary-account
- **What it says:** Describes Confirmation of Payee (UK) and Verification of Payee (EU) checks for Airwallex's own outgoing transfers. We quote no words from it.
- **How we use it:** We do not know what a payer's bank shows for UK and EU receiving accounts. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official documentation; it covers outgoing payments only, so it supports a gap in our knowledge, not a fact.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) F2#2 (self-checked), F2#3 (self-checked), F2#6 (self-checked).

### C19 · Create a Global Account

- **Publisher / author:** Airwallex API reference. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/api/core_resources/global_accounts/create
- **What it says:** The create call takes country_code, request_id, required_features and an optional nick_name. We quote no sentences from it.
- **How we use it:** How the agent gives a problem client its own local account. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** Official API reference; it lists the fields and calls, and we test them in the sandbox on day 1.
- **Record:** Cited directly; not part of the research records.

### C20 · List all Global Accounts

- **Publisher / author:** Airwallex API reference. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/api/core_resources/global_accounts/list
- **What it says:** The list call can filter by currency, nickname and status. We quote no sentences from it.
- **How we use it:** Finding a client's account again. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official API reference; it lists the fields and calls, and we test them in the sandbox on day 1.
- **Record:** Cited directly; not part of the research records.

### C21 · Close a Global Account

- **Publisher / author:** Airwallex API reference. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/api/core_resources/global_accounts/close
- **What it says:** The call that closes a Global Account. We quote no sentences from it.
- **How we use it:** Closing an account we no longer need. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official API reference; it lists the fields and calls, and we test them in the sandbox on day 1.
- **Record:** Cited directly; not part of the research records.

### C22 · List all Deposits

- **Publisher / author:** Airwallex API reference. **Date:** undated (read 21 Oct 2026).
- **Link:** https://www.airwallex.com/docs/api/core_resources/deposits/list
- **What it says:** Lists the fields of a deposit: amount, currency, fee, payer, reference ("A user specific reference that will be displayed to the bank account owner on the bank statement"), status and failure_details ("Empty unless the deposit is in a failure status (`REJECTED`, `REVERSED`)").
- **How we use it:** What the agent learns when money lands, and that no field shows the amount originally sent or fees taken on the way. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** Official API reference; it lists the fields and calls, and we test them in the sandbox on day 1. "No field" is our reading of the field list. Record L5#5 notes that the error codes point to a direct-debit list.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L5#0 (verified), L5#5 (partly), L5#9 (verified).

### C23 · Create a Global Account Deposit (simulation)

- **Publisher / author:** Airwallex API reference. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/api/simulation/deposits/create
- **What it says:** The sandbox call that fakes an incoming payment, with amount, payer_name, payer_bankname, payer_country, reference, statement_ref and status (PENDING, REJECTED or SETTLED). We quote no sentences from it.
- **How we use it:** Staging short, mixed and mislabelled payments for the demo. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official API reference; it lists the fields and calls, and we test them in the sandbox on day 1.
- **Record:** Cited directly; not part of the research records.

### C24 · List all Current Balances

- **Publisher / author:** Airwallex API reference. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/api/core_resources/balances/current
- **What it says:** The call that returns current balances. We quote no sentences from it.
- **How we use it:** Knowing how much of each currency the business holds. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official API reference; it lists the fields and calls, and we test them in the sandbox on day 1.
- **Record:** Cited directly; not part of the research records.

### C25 · Retrieve a Current Rate

- **Publisher / author:** Airwallex API reference. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/api/transactional_fx/rates/current
- **What it says:** The call that returns a current exchange rate. We quote no sentences from it.
- **How we use it:** Checking a rate before deciding to keep or convert. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official API reference; it lists the fields and calls, and we test them in the sandbox on day 1.
- **Record:** Cited directly; not part of the research records.

### C26 · Create a Quote

- **Publisher / author:** Airwallex API reference. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/api/transactional_fx/quotes/create
- **What it says:** A quote gives "a guaranteed rate for an agreed period of time", with validity from MIN_1 to HR_24.
- **How we use it:** Fixing the rate before a conversion. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official API reference; it lists the fields and calls, and we test them in the sandbox on day 1.
- **Record:** Cited directly; not part of the research records.

### C27 · Create a Conversion

- **Publisher / author:** Airwallex API reference. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/api/transactional_fx/conversion/create
- **What it says:** The call that books a currency exchange. We quote no sentences from it.
- **How we use it:** Converting only what is really needed. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official API reference; it lists the fields and calls, and we test them in the sandbox on day 1.
- **Record:** Cited directly; not part of the research records.

### C28 · Create a Beneficiary

- **Publisher / author:** Airwallex API reference. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/api/payouts/beneficiaries/create
- **What it says:** The call that saves a supplier's bank details. We quote no sentences from it.
- **How we use it:** Paying a supplier from the currency already held. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official API reference; it lists the fields and calls, and we test them in the sandbox on day 1.
- **Record:** Cited directly; not part of the research records.

### C29 · Create a Transfer

- **Publisher / author:** Airwallex API reference. **Date:** undated (read 21 Oct 2026).
- **Link:** https://www.airwallex.com/docs/api/payouts/transfers/create
- **What it says:** The payout call, with transfer_method (LOCAL or SWIFT) and an optional quote_id. It says requests with a request_id used in the past 7 days are treated as duplicates. We quote no sentences from it.
- **How we use it:** Paying suppliers, and never paying twice. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official API reference; it lists the fields and calls, and we test them in the sandbox on day 1.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L5#25 (verified).

### C30 · Transition Transfer Status (simulation)

- **Publisher / author:** Airwallex API reference. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/api/simulation/transfers/transition
- **What it says:** The sandbox call that moves a test transfer to SENT, PAID, FAILED and other states. We quote no sentences from it.
- **How we use it:** Testing what happens when a payout succeeds or fails. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official API reference; it lists the fields and calls, and we test them in the sandbox on day 1.
- **Record:** Cited directly; not part of the research records.

### C31 · Listen for webhook events

- **Publisher / author:** Airwallex Docs. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/developer-tools/webhooks/listen-for-webhook-events
- **What it says:** Each webhook carries an x-signature, "The HMAC hex digest of the concatenated timestamp and request body".
- **How we use it:** Checking that each alert really comes from Airwallex. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official Airwallex documentation; it says what the product is meant to do, and we still test it in the sandbox.
- **Record:** Cited directly; not part of the research records.

### C32 · Webhooks overview

- **Publisher / author:** Airwallex Docs. **Date:** undated.
- **Link:** https://www.airwallex.com/docs/developer-tools/webhooks/webhooks-overview
- **What it says:** "Your endpoint may receive the same event more than once", and Airwallex "does not guarantee that events are delivered in the order they were generated".
- **How we use it:** Handling repeated and out-of-order alerts. Cited in [04-airwallex-integration](../docs/04-airwallex-integration.md).
- **How much weight it carries:** Official Airwallex documentation; it says what the product is meant to do, and we still test it in the sandbox.
- **Record:** Cited directly; not part of the research records.

## Regulators and official bodies (India and others)

### C33 · Foreign Exchange Management (Export and Import of Goods and Services) Regulations, 2026 (Notification FEMA 23(R)/2026-RB)

- **Publisher / author:** Reserve Bank of India. **Date:** 13 Jan 2026, amended up to 22 Sep 2026.
- **Link:** https://www.rbi.org.in/Scripts/BS_FemaNotifications.aspx?Id=13277
- **What it says:** India's new export rules. They "shall come into force from October 01, 2026". Money must arrive within "nine months" (an amendment replaced "fifteen months" and "eighteen months"). A services EDF is filed "within 30 days from the end of month in which invoice for services has been raised". Entries up to ₹10 lakh "may be closed based on a declaration from the exporter"; above that the bank must be "satisfied of the reasons cited". Long-unpaid exporters may export only "against receipt of full advance or an irrevocable Letter of Credit", and bank charges must be "reasonable and proportional".
- **How we use it:** All the current India rules in the India module: deadlines, declarations, reductions and bank policies. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** Primary regulator text. It is new (in force 1 Oct 2026), and RBI has said it will clarify it in an FAQ.
- **Record:** [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V373 (verified), V374 (verified), V445 (verified), V446 (verified), V447 (verified), V448 (verified), V449 (verified).

### C34 · Master Direction – Export of Goods and Services

- **Publisher / author:** Reserve Bank of India. **Date:** updated as on 17 Jul 2026.
- **Link:** https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10395
- **What it says:** RBI's older export rules. Money must be received within "nine months"; eBRCs are generated "only from the data available in EDPMS"; a reduction should not "exceed 25 per cent of invoice value", with no ceiling for established exporters.
- **How we use it:** The nine-month deadline, the eBRC rule, the old 25% reduction limit, and that India's export rules changed recently. Cited in [01-problem](../docs/01-problem.md), [07-risks](../docs/07-risks.md), [india-module](../docs/india-module.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** Primary regulator text, but it governs transactions from before 1 Oct 2026. For new exports the 2026 Regulations apply.
- **Record:** [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V011 (partly), V018 (verified), V019 (verified), V022 (partly), V023 (verified), V024 (verified).

### C35 · Export Data Processing and Monitoring System (EDPMS) – reconciliation of export/import entries – Review of Guidelines (RBI/2025-26/89, A.P. (DIR Series) Circular No. 12)

- **Publisher / author:** Reserve Bank of India. **Date:** 1 Oct 2025.
- **Link:** https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12908
- **What it says:** The circular that first let banks close small export entries on the exporter's declaration. We quote no words from it.
- **How we use it:** Where the ₹10 lakh declaration route started. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** Primary regulator text.
- **Record:** [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V055 (verified).

### C36 · Circular No. 33/2019-Customs: clarification regarding duty drawback allowed in cases of short realisation of export proceeds due to bank charges deducted by foreign banks

- **Publisher / author:** Central Board of Indirect Taxes and Customs (CBIC), Ministry of Finance; copy hosted by TaxGuru. **Date:** 19 Sep 2019.
- **Link:** https://taxguru.in/custom-duty/clarification-duty-drawback-allowed-cases-short-realisation-export-proceeds-due-bank-charges-deducted-foreign-banks.html
- **What it says:** Some customs offices issued "show cause notices" to recover drawback when foreign banks had deducted charges. CBIC said officers may accept a "bank's confirmation regarding foreign bank charges".
- **How we use it:** Short payments caused by bank fees can put an exporter's customs refund at risk. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** Official circular, read on a third-party copy; it dates from 2019.
- **Record:** [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V082 (verified).

## Industry surveys, standards and data

### C37 · The Goofus and Gallant of Cash Application

- **Publisher / author:** Nacha (Robert Unger, Senior Director, Product Management). **Date:** 23 Jul 2021.
- **Link:** https://www.nacha.org/news/goofus-and-gallant-cash-application
- **What it says:** Reports a survey Nacha ran with the Credit Research Foundation, where "more than half of the respondents reported that a paltry 0%-20% of payments were processed automatically".
- **How we use it:** Automatic matching of incoming payments is still rare. Cited in [01-problem](../docs/01-problem.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** A 2021 survey of very large companies (the article says "mega-corporations"), not small businesses; the sample size is not stated in the article.
- **Record:** [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V089 (verified).

### C38 · Trade Services – General Schedule of Features and Charges (GSFC)

- **Publisher / author:** Kotak Mahindra Bank. **Date:** with effect from 12 Oct 2026.
- **Link:** https://www.kotak.bank.in/content/dam/Kotak/gsfcfiles/trade/trade-services-final-12thOCT-new.pdf
- **What it says:** Kotak's price list for trade services, which lists "Reduction in the export realization 1000" (rupees).
- **How we use it:** Indian banks charge exporters to record a short payment. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** One bank's published price list; other banks charge differently.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L4#26 (verified).

## Accounting software and vendors

### C39 · What's new in Auto Bank Reconciliation

- **Publisher / author:** Xero Blog (Eli Danziger, SVP Product, Xero). **Date:** 14 Aug 2026 (last updated 19 Aug 2026).
- **Link:** https://blog.xero.com/?p=40102
- **What it says:** Xero says it is "tackling more complex use cases, like scenarios where a single payment covers multiple invoices".
- **How we use it:** Accounting software still leaves the hard cases, such as one payment for several invoices, to people. Cited in [01-problem](../docs/01-problem.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** A vendor describing the limits of its own product, which makes it a fair admission; it gives no figures.
- **Record:** [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V440 (verified).

### C40 · Xero Auto-Reconciliation: Notes From Our Testing

- **Publisher / author:** Digit, a Xero partner firm (Andrew Erkins). **Date:** 31 Mar 2026.
- **Link:** https://digit.business/insights/xero/xero-auto-reconciliation-testing-notes
- **What it says:** Digit tested Xero's automatic matching on its own client files and reports that it "is not able to reconcile part payments made by customer even though the invoice number and customer name is already in the description".
- **How we use it:** Automatic matching fails on part payments. Cited in [01-problem](../docs/01-problem.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** One firm's test on its own clients (January to March 2026, for up to ten weeks); the quoted line is a tester's remark reported by the firm (see record V345).
- **Record:** [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V344 (partly), V345 (verified), V346 (verified).

### C41 · Account Validation Requirements for Supplier Payment Accounts (Coupa Compass: supplier remit-to account validations)

- **Publisher / author:** Coupa. **Date:** published 16 Feb 2023, last edited 1 Sep 2025.
- **Link:** https://compass.coupa.com/en-us/products/product-documentation/supplier-resources/for-suppliers/coupa-supplier-portal/set-up-the-csp/financial-setup/supplier-remit-to-account-validations
- **What it says:** Coupa tells suppliers that new bank details "must be approved by your customer prior to receiving payment".
- **How we use it:** Clients cannot switch to new bank details instantly; there is an approval step. Cited in [07-risks](../docs/07-risks.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** One procurement platform's documented rule; it shows the step, not how long it takes.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L8#21 (verified).

### C42 · Bank Charges for Inward Remittance in India: 2026 Fee Guide

- **Publisher / author:** Razorpay. **Date:** 23 Jan 2026.
- **Link:** https://razorpay.com/blog/bank-charges-inward-remittance-india/
- **What it says:** Says "International wire transfers often pass through correspondent banks that deduct $15–$30 in “SWIFT fees” before the money even reaches India".
- **How we use it:** Banks along the way take fees, so less arrives than was sent. Cited in [01-problem](../docs/01-problem.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** Vendor content about a problem it sells a fix for; the $15–$30 range is the vendor's own figure.
- **Record:** [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V062 (verified).

### C43 · EDPMS Entry Not Closed: Causes, Fixes & Closure Steps

- **Publisher / author:** Skydo (Awadhesh Ranjan). **Date:** 12 Oct 2026.
- **Link:** https://www.skydo.com/blog/edpms-entry-not-closed
- **What it says:** Says the commonest reason an export entry stays open is that "the money arrived, but the bank was never told which bill it settles", and that short payments from "bank charges, or an agreed reduction" cannot be auto-matched.
- **How we use it:** Why Indian export entries stay open after payment. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** Vendor content about a problem it sells a fix for (Skydo handles export payments); it agrees with the regulator text but gives no measured rate.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L4#19 (verified), L4#47 (verified); [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V049 (partly), V056 (verified), V057 (verified), V058 (partly), V077 (verified), V078 (verified), V079 (partly), V080 (verified), V081 (verified).

## Practitioner voices (forums, feature requests, job ads, videos)

### C44 · How do you get paid in full on international wire transfers? customer paid full amount but we keep receiving less!!

- **Publisher / author:** r/Accounting (Reddit): original poster and commenters. **Date:** 24 Feb 2026 (post); 26 Feb 2026 (the $40 comment).
- **Link:** https://www.reddit.com/r/Accounting/comments/1rdaid8/how_do_you_get_paid_in_full_on_international_wire/
- **What it says:** The poster writes "This happens on maybe 60% of our international wires. Amount received never matches amount sent". A commenter replies "We frequently get foreign wires for over $100,000 and pay a less than $40 fee".
- **How we use it:** Short international payments are common and frustrating; and the counterpoint that each fee is small. Cited in [README](../README.md), [01-problem](../docs/01-problem.md), [07-risks](../docs/07-risks.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** One accountant's experience, not a measured rate; the same thread holds the counter-view, which we also quote.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L1#1 (verified), L1#2 (verified); [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V470 (verified), V471 (verified).

### C45 · Comment p9zs0po in "Im trusting nothing in our AP inbox after a vendor changed their bank details"

- **Publisher / author:** r/Accounting (Reddit), user ForGodandForProfit. **Date:** 15 Sep 2026.
- **Link:** https://www.reddit.com/comments/1wf74ra/_/p9zs0po
- **What it says:** An accounts team calls a known number and then applies "a 2 week freeze" before paying new bank details.
- **How we use it:** Clients are slow to accept new bank details. Cited in [07-risks](../docs/07-risks.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** One commenter's practice (comment score 1), not a measured rate.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L8#1 (verified).

### C46 · Invoice - Prompt Payment / Settlement Discount

- **Publisher / author:** Xero Product Ideas, comment by Ica Hill. **Date:** 24 Sep 2026.
- **Link:** https://productideas.xero.com/forums/967115-invoices-quotes/suggestions/44960470-invoice-prompt-payment-settlement-discount
- **What it says:** A user writes: "The issue comes when they pay the lesser amount, i need to create a credit note for the 'missing' amount before i match off the bank payment".
- **How we use it:** Clients deduct discounts without saying so, and someone has to fix the books by hand. Cited in [01-problem](../docs/01-problem.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** One user's feature request; it shows the problem exists, not how often.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L2#18 (verified).

### C47 · Bank reconciliation - Add attachment to Find & Match (multiple match) transactions

- **Publisher / author:** Xero Product Ideas, idea by Chloe Ziola. **Date:** 7 May 2024.
- **Link:** https://productideas.xero.com/forums/967136-banking-chart-of-accounts/suggestions/48398618-bank-reconciliation-add-attachment-to-find-mat
- **What it says:** "In the example of one payment matched to multiple sales invoices, there is usually a remittance provided by the client that we need to file with the payment".
- **How we use it:** One payment often covers several invoices, and the breakdown arrives separately. Cited in [01-problem](../docs/01-problem.md).
- **How much weight it carries:** One user's feature request; it shows the problem exists, not how often.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L2#6 (verified).

### C48 · JAX | Auto reconcile - Ability to set parameters

- **Publisher / author:** Xero Product Ideas, comment by Jean-Luc Tostee. **Date:** 16 Oct 2026.
- **Link:** https://productideas.xero.com/forums/966939-automatic-bank-reconciliation-beta/suggestions/50822483-jax-auto-reconcile-ability-to-set-parameters
- **What it says:** A user says the automatic matcher "matches to the same wrong customers often".
- **How we use it:** Accountants distrust automatic matching, so we show the evidence and never force a match. Cited in [07-risks](../docs/07-risks.md).
- **How much weight it carries:** One user's complaint, not a measured error rate.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L2#10 (verified).

### C49 · Sr.FinOps Analyst - AR, AWS cash app Hyd

- **Publisher / author:** Amazon, listed on the anitab.org job board. **Date:** posted 21 Jul 2026.
- **Link:** https://jobs.anitab.org/companies/amazon-3-60ad394d-c673-4474-9694-344b0cae748f/jobs/86957271-sr-finops-analyst-ar-aws-cash-app-hyd
- **What it says:** A cash-application job whose duties include: "Utilize shared mailboxes and customer web portals to identify, retrieve and organize remittance details". The page now says the job is no longer accepting applications, and gives the location as Pune although the title says Hyd.
- **How we use it:** Large companies pay people to collect the explanation that travels separately from the money. Cited in [01-problem](../docs/01-problem.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** One job ad at a very large company; it shows the task exists, not what it costs a small firm.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L6#12 (verified).

### C50 · Bank is denying to issue IRM for eBRC Shipments

- **Publisher / author:** r/CharteredAccountants (Reddit), a goods e-commerce exporter. **Date:** 10 Dec 2024.
- **Link:** https://reddit.com/r/CharteredAccountants/comments/1haudd7/bank_is_denying_to_issue_irm_for_ebrc_shipments/
- **What it says:** An exporter with 2,000 shipments says the bank is "charging 500+18% GST per invoice" to link payments to shipments.
- **How we use it:** Indian exporters pay banks per invoice to link receipts; the closest thing we found to proof that this work is worth paying for. Cited in [01-problem](../docs/01-problem.md), [07-risks](../docs/07-risks.md), [india-module](../docs/india-module.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** One exporter's experience with one bank, not a measured rate.
- **Record:** [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V379 (verified).

### C51 · GST Refund filing, advice needed

- **Publisher / author:** r/IndiaTax (Reddit), user batman6t9. **Date:** 29 Aug 2026.
- **Link:** https://reddit.com/r/IndiaTax/comments/1w1cvw0/gst_refund_filing_advice_needed/
- **What it says:** A poster mapped many inward remittance messages (IRMs) to one shipping bill by mistake and is stuck fixing it. We quote no words from it.
- **How we use it:** An example of what an IRM is and how it is mapped to export bills. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** One post; used only to illustrate a term.
- **Record:** [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V377 (verified).

### C52 · Comment pduc0sq in "Wise Business payout: e-FIRC is from Citi, INR hits my own bank. Where do I file the new EDF?"

- **Publisher / author:** r/IndiaTax (Reddit), user AgentVB34. **Date:** 4 Oct 2026.
- **Link:** https://reddit.com/r/IndiaTax/comments/1wx772c/wise_business_payout_efirc_is_from_citi_inr_hits/pduc0sq/
- **What it says:** A freelancer paid via Airwallex says they must "manually mail Yes Bank(AD) to provide FIRA" for each payment.
- **How we use it:** Airwallex payments to India still need manual paperwork at the Indian bank. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** One freelancer's experience.
- **Record:** [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V368 (verified).

### C53 · EDF for Freelancers: RBI's New Export Declaration Rule from 1 October 2026

- **Publisher / author:** r/IndiaTax (Reddit), user Responsible-Bad-6624. **Date:** 4 Oct 2026 UTC (5 Oct 2026 in India).
- **Link:** https://www.reddit.com/r/IndiaTax/comments/1wxtw13/edf_for_freelancers_rbis_new_export_declaration/
- **What it says:** An explainer post that warns the bank "is not barred from asking for more if something looks off".
- **How we use it:** The ₹10 lakh declaration route is up to each bank. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** One experienced practitioner's reading of the rules, not official guidance.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L4#8 (verified), L4#9 (verified), L4#10 (verified); [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V366 (verified), V381 (partly).

### C54 · Comment pe6elvt in "EDF for Freelancers: RBI's New Export Declaration Rule from 1 October 2026"

- **Publisher / author:** r/IndiaTax (Reddit), a commenter. **Date:** 6 Oct 2026.
- **Link:** https://www.reddit.com/r/IndiaTax/comments/1wxtw13/edf_for_freelancers_rbis_new_export_declaration/pe6elvt/
- **What it says:** On Upwork, "the remiiter name will be Payment Escrow Inc." (spelling as in the original), not the client.
- **How we use it:** The payer's name on a receipt often differs from the client on the invoice. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** One commenter's experience.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L4#4 (verified).

### C55 · Comment ped5j8t in "EDF for Freelancers: RBI's New Export Declaration Rule from 1 October 2026"

- **Publisher / author:** r/IndiaTax (Reddit), a commenter. **Date:** 7 Oct 2026.
- **Link:** https://www.reddit.com/r/IndiaTax/comments/1wxtw13/edf_for_freelancers_rbis_new_export_declaration/ped5j8t/
- **What it says:** A commenter paid through Skydo asks: "How can it close anything on the epdms when it doesn't have anything open?"
- **How we use it:** Payout services that pay out in rupees break the link between payment and export record. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** One commenter's experience.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L4#5 (verified).

### C56 · Comment pgorrfy in the thread "Software exporter: with EDF from Oct 2026..." (title shortened in our record)

- **Publisher / author:** r/IndiaTax (Reddit), user CrumpledMemories. **Date:** 14 Oct 2026.
- **Link:** https://reddit.com/r/IndiaTax/comments/1x5q6tz/_/pgorrfy
- **What it says:** Says "RBI has left the finer details to the bank".
- **How we use it:** Each Indian bank applies the new rules its own way. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** One commenter's view; others in the thread say their banks have already shared formats (see record V376).
- **Record:** [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V376 (verified).

### C57 · FIRC vs FIRA - which is needed for GST export of services

- **Publisher / author:** CAclubindia forum; question by Shanthi, reply by Aashok Kumar Sharma. **Date:** 14 Aug 2025 (reply; question posted 25 Jul 2023).
- **Link:** https://www.caclubindia.com/forum/firc-vs-fira-which-is-needed-for-gst-export-of-services-601534.asp
- **What it says:** A consultant replies that "Many GST officers accept FIRA".
- **How we use it:** Tax officers differ on which bank certificate they accept. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** One consultant's view on a forum.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L4#43 (verified).

### C58 · Mandatory Documentary Evidence for Export Realisation

- **Publisher / author:** TaxTMI forum; question by ChandraShekar MN. **Date:** 16 May 2025.
- **Link:** https://www.taxtmi.com/forum/issue?id=120022
- **What it says:** An exporter writes that "The Department is insisting for FIRC or e-BRC instead of FIRA".
- **How we use it:** Tax officers differ on which bank certificate they accept. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** One exporter's case.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L4#41 (verified).

### C59 · RBI EDPMS ₹10 Lakh Export-Bill Closure in 2026: Declarations, Realisation, GST and Accounting

- **Publisher / author:** TaxGuru, CA Sandeep Kanoi. **Date:** 17 Oct 2026.
- **Link:** https://taxguru.in/finance/rbi-edpms-rs-10-lakh-export-bill-closure-2026-declarations-realisation-gst-accounting.html
- **What it says:** Says "An accounting ERP may show an invoice as settled while EDPMS remains open" when the bank lacks the right reference.
- **How we use it:** The books and the bank's export record can disagree. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** One chartered accountant's explainer article, not official guidance.
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L4#16 (verified), L4#17 (verified), L4#18 (verified).

## News

### C60 · Airwallex buys Leapfin to add accounting automation

- **Publisher / author:** IT Brief Australia (Karen Joy Bacudo). **Date:** 8 Jun 2026.
- **Link:** https://itbrief.com.au/story/airwallex-buys-leapfin-to-add-accounting-automation
- **What it says:** Reports that Airwallex bought Leapfin, which adds "reconciliation, revenue recognition and broader record-to-report processes".
- **How we use it:** Airwallex is building reconciliation at the accounting end; we work earlier, when the money lands. Cited in [README](../README.md), [02-solution](../docs/02-solution.md), [04-airwallex-integration](../docs/04-airwallex-integration.md), [07-risks](../docs/07-risks.md), our HackerEarth idea submission (kept outside this repo).
- **How much weight it carries:** Trade-press news report of a company announcement.
- **Record:** Cited directly; not part of the research records.

### C61 · RBI to clarify forex reporting rules soon

- **Publisher / author:** Mint (Apoorva Ajith). **Date:** 7 Oct 2026.
- **Link:** https://www.livemint.com/news/india/rbi-to-clarify-forex-reporting-rules-soon/amp-11791369703116.html
- **What it says:** Reports that RBI's deputy governor said RBI "would clarify the matter shortly through an FAQ".
- **How we use it:** India's new rules are still being clarified. Cited in [india-module](../docs/india-module.md).
- **How much weight it carries:** News report of an RBI press conference. The same article reports the Governor saying some small service exporters may not need to report (see records L4#46 and V390).
- **Record:** [pain-map-items.csv](data/pain-map-items.csv) L4#46 (partly); [evidence-test-ledger.csv](data/evidence-test-ledger.csv) V390 (partly).

## Spot-check, 22 Oct 2026

We fetched 52 sources again and searched each page for the words we quote (or, where we quote nothing, for the field and call names we rely on): C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C22, C23, C24, C25, C26, C27, C28, C29, C30, C31, C32, C33, C34, C35, C36, C37, C38, C39, C40, C41, C42, C43, C46, C47, C48, C49, C57, C58, C59, C60, C61. The quoted words were found on every one. Two notes: the Kotak price list (C38) is a PDF, so we checked its extracted text; and the "Updated on Aug 15, 2025" stamp on the coverage table (C07) shows on the web page, not on its .md copy.

Reddit pages cannot be fetched from our machine, so for C44, C45, C50, C51, C52, C53, C54, C55, C56 we rely on the check results in the research records. Each quote we use from them appears word for word in the `quote` column of a row marked `verified`.

## Quotes that need attention

None. Every quote in our docs and submission that we checked appears on its page.

A few points where the words around a quote could be sharper. **All four were fixed on 22 Oct 2026**; the notes are kept as a record:

- **C37 Nacha.** [01-problem](../docs/01-problem.md) and our submission say "In a Nacha survey". The article says it was "a survey of mega-corporations", which matters because we build for small businesses.
- **C40 Digit.** [01-problem](../docs/01-problem.md) and our submission say "A 10-week test". The page says testing ran January to March 2026 "for up to ten weeks", and the line we quote is one tester's remark reported by the firm.
- **C34 RBI Master Direction.** [07-risks](../docs/07-risks.md) cites it for "The 2026 export rules took effect this year and are still being clarified", and our submission for "India's export rules changed recently". That page is the older rulebook. The change itself is in the 2026 Regulations (C33), and "still being clarified" comes from Mint (C61).
- **C49 Job ad.** Our submission says Amazon Web Services "advertises" the job. The listing now says it is no longer accepting applications, and it gives Pune as the location while the title says Hyd.

## How to add a source

- Link the exact page next to the claim it supports, and quote the page's own words in quotation marks, copied exactly. Give the date shown on the page, or say "undated".
- Add an entry here under the right heading and fill in every field: publisher, date, link, what it says (with the exact words we quote), how we use it, an honest weight, and its research-record IDs if it has any. Keep the C-numbers in order.
- Before merging, open the page and check that the quoted words are there. If they are not, fix the doc or list the quote under "Quotes that need attention".
