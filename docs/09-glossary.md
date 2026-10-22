# Glossary

Our docs use a lot of finance, banking and software words. This page gives each one a plain meaning, with a small example where it helps, so you can read the rest of the repository without a finance background. Other pages link here. Terms are grouped by topic and listed A to Z within each group, and under each term we note which docs use it. These are plain explanations, not legal or tax advice. For India's rules, the [India module](india-module.md) has the sources.

## Getting paid

**Accounts team (accounts payable)**: The team at a customer's company that pays suppliers' invoices. It also checks any request to change a supplier's bank details before it uses them, which can slow down a switch to new details.\
*Used in: [README](../README.md), [Problem](01-problem.md), [Solution](02-solution.md), [Architecture](03-architecture.md), [Pain atlas](05-pain-atlas.md), [Risks](07-risks.md), [Research method](08-research-method.md), [Decision log](10-decision-log.md)*

**Advance payment**: Money a customer pays before the work is done or before the final invoice exists. Example: a 30% up-front deposit sits as an unexplained bank line for weeks, because there is no invoice yet to match it to.\
*Used in: [Pain atlas](05-pain-atlas.md), [India module](india-module.md)*

**Bundled payment**: One payment that covers several invoices. Example: a single payment of €930 for two invoices of €600 and €400, after deductions.\
*Used in: [README](../README.md), [Problem](01-problem.md), [Solution](02-solution.md), [Pain atlas](05-pain-atlas.md), [Risks](07-risks.md), [Research method](08-research-method.md), [Decision log](10-decision-log.md)*

**Credit note**: A document from the seller that reduces what a customer owes, for example after a late delivery or a returned item. Example: a €50 credit note against a €1,000 invoice means €950 is due.\
*Used in: [Problem](01-problem.md), [Solution](02-solution.md), [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Risks](07-risks.md)*

**Deduction**: Any amount a customer takes off an invoice before paying: a discount, a credit, a disputed item or tax withheld. Deductions often arrive with no explanation.\
*Used in: [Problem](01-problem.md), [Solution](02-solution.md), [Architecture](03-architecture.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Risks](07-risks.md), [Research method](08-research-method.md), [India module](india-module.md)*

**Discount (early-payment discount)**: A price reduction, often offered for paying quickly. Example: a German client takes 2% off for paying early, so a €1,000 invoice is paid as €980.\
*Used in: [README](../README.md), [Problem](01-problem.md), [Solution](02-solution.md), [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Risks](07-risks.md), [Research method](08-research-method.md), [India module](india-module.md)*

**Dispute**: A disagreement about an invoice, for example over the quality or amount of work. A customer may hold back the disputed part and pay the rest.\
*Used in: [README](../README.md), [Problem](01-problem.md), [Solution](02-solution.md), [Architecture](03-architecture.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Research method](08-research-method.md)*

**Escrow**: A middleman that holds money and passes it on when conditions are met. The payment then shows the escrow firm's name, not the client's. Example: on Upwork, the payer shown can be "Payment Escrow Inc." rather than the client.\
*Used in: [Pain atlas](05-pain-atlas.md), [India module](india-module.md)*

**Overpayment**: A customer paying more than it owes, or paying the same invoice twice. Someone has to decide whether to refund the extra or keep it as credit for future invoices.\
*Used in: [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md)*

**Part payment (instalment)**: Paying one invoice in several smaller amounts. Example: $100 a month against a $1,200 invoice. After three payments, $900 is still owed.\
*Used in: [README](../README.md), [Problem](01-problem.md), [Solution](02-solution.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md)*

**Payer**: The person or company that actually sends the money. It is not always the customer named on the invoice. It can be a parent company, a person or an escrow firm. Example: "ACME HOLDING BV" pays invoices addressed to its subsidiary, Acme Digital.\
*Used in: [Solution](02-solution.md), [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Risks](07-risks.md), [Research method](08-research-method.md), [India module](india-module.md)*

**Platform payout**: One lump sum from a platform such as Stripe, Shopify or Amazon, covering many sales, after the platform has taken its fees. Example: one Stripe deposit covers 137 transactions. This is outside our first build.\
*Used in: [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md)*

**Purchase order (PO)**: The customer's own internal order for what it is buying. If the invoice lacks the PO number, or the PO carries the wrong terms, payment can be held or cut. Example: a client's payment is on hold because the invoice is missing its purchase-order number.\
*Used in: [Solution](02-solution.md), [Pain atlas](05-pain-atlas.md)*

**Reference (payment reference)**: The short text that travels with a payment, such as an invoice number. It is often cut short or says nothing useful. Example: "INV-1043 ACME" arrives as "INV-10", or the reference is just "MARCH".\
*Used in: [README](../README.md), [Problem](01-problem.md), [Solution](02-solution.md), [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Risks](07-risks.md), [India module](india-module.md)*

**Remittance (remittance advice)**: The customer's note saying which invoices a payment covers and why anything was taken off. It usually travels separately from the money, by email, PDF or a supplier portal, if it comes at all.\
*Used in: [Problem](01-problem.md), [Solution](02-solution.md), [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md)*

**Short payment**: A payment that is smaller than the invoice. We call the difference "the gap". Example: €1,000 invoiced, €930 received, so there is a €70 gap to explain.\
*Used in: [README](../README.md), [Problem](01-problem.md), [Solution](02-solution.md), [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Risks](07-risks.md), [Research method](08-research-method.md), [Decision log](10-decision-log.md), [India module](india-module.md)*

**Supplier portal**: A website run by a large customer where its suppliers upload invoices and keep their bank details. New bank details entered there may need the customer's approval before any payment goes to them.\
*Used in: [Problem](01-problem.md), [Solution](02-solution.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Risks](07-risks.md), [Decision log](10-decision-log.md)*

**TDS (Tax Deducted at Source)**: India's form of withholding tax. An Indian client may deduct TDS from a payment, so less arrives than the invoice says.\
*Used in: [Pain atlas](05-pain-atlas.md)*

**Withholding tax (withheld tax)**: Tax that a customer keeps back from a payment and pays to its tax authority instead of to the seller. It often shows up as a round percentage of the invoice, and the seller asks the customer for the tax certificate as proof. Example: exactly 10% missing from a €1,000 invoice.\
*Used in: [Problem](01-problem.md), [Solution](02-solution.md), [Architecture](03-architecture.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Risks](07-risks.md)*

## Matching and bookkeeping

**Automatic matching (auto-reconcile)**: A feature in accounting or payment software that pairs incoming money with open invoices without a person. It handles clean one-to-one cases. Part payments, bundled payments and deductions usually still need a person, and wrong automatic matches have to be undone by hand.\
*Used in: [Problem](01-problem.md), [Solution](02-solution.md), [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md), [Risks](07-risks.md), [India module](india-module.md)*

**Bank feed**: A link that copies a bank's transactions into accounting software automatically. Some feeds cut the reference or leave the payer blank. A *bank rule* is a saved instruction in that software, such as "payments from this name belong to this customer".\
*Used in: [Solution](02-solution.md), [Pain atlas](05-pain-atlas.md)*

**Cash application**: The job of applying each incoming payment to the right invoices, so they show as paid. Large companies have staff whose whole job is this.\
*Used in: [Problem](01-problem.md)*

**Cash forecast (cash plan)**: An estimate of how much money will be available, and when, compared with the bills that are due. Our cash planner separates money that is certain from money that is only expected, and notes how strong the evidence is for each.\
*Used in: [Architecture](03-architecture.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Research method](08-research-method.md)*

**Clearing account**: A temporary holding account in the books. Money is parked there, then moved out to its proper places. Example: a platform payout is booked to a clearing account, then split into sales and fees.\
*Used in: [Pain atlas](05-pain-atlas.md)*

**Currency gain or loss (FX gain or loss)**: The difference that appears when an invoice is in one currency and the money is valued or received at a different exchange rate. Example: an invoice worth ₹83,000 on the day it was issued brings in ₹82,500 when paid, a ₹500 loss.\
*Used in: [Pain atlas](05-pain-atlas.md), [Research method](08-research-method.md), [India module](india-module.md)*

**ERP (Enterprise Resource Planning)**: Business software that runs accounts, sales and other operations in one system. ERPNext is one example.\
*Used in: [Pain atlas](05-pain-atlas.md), [India module](india-module.md)*

**Journal entry**: A manual accounting record that moves amounts between accounts, often used to fix or adjust the books. Example: a "manual FX journal" to record a currency difference.\
*Used in: [Pain atlas](05-pain-atlas.md)*

**Ledger**: The book of record for money events. In Receive to Reconciled, the ledger holds customers, invoices, known payer names, deposits, matches, gaps, approvals and every action taken.\
*Used in: [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Build plan](06-build-plan.md)*

**Liability account**: An account for money the business owes to someone else. An overpayment that may have to be refunded is sometimes held there.\
*Used in: [Pain atlas](05-pain-atlas.md)*

**Month-end close**: The routine of finishing the books for a month: matching every receipt, booking fees and checking balances. Receipts that can't be matched hold it up.\
*Used in: [Problem](01-problem.md), [Solution](02-solution.md), [Pain atlas](05-pain-atlas.md), [Numbers register](../research/numbers.md)*

**Reconciliation**: Checking that two records agree. Here it means making sure every receipt in the bank is matched to invoices, and every invoice marked paid has money behind it.\
*Used in: [README](../README.md), [Problem](01-problem.md), [Solution](02-solution.md), [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md), [Risks](07-risks.md), [Decision log](10-decision-log.md)*

**Revenue recognition**: The accounting rules for when income counts as earned, which is not always when the cash arrives. Leapfin, which Airwallex bought, works on this and on reconciliation at the accounting end.\
*Used in: [Solution](02-solution.md), [Airwallex integration](04-airwallex-integration.md)*

**Suspense account**: An account where money nobody can identify yet is parked. Items can stay there for years. Example: a council found unmatched cash from 2011 still in suspense.\
*Used in: [Pain atlas](05-pain-atlas.md)*

**Tolerance**: An allowed margin. Our matching engine accepts a combination of invoices when the gap fits set ranges for bank fees, tax or exchange-rate differences. Even then, the explained parts must add up exactly to the payment.\
*Used in: [Solution](02-solution.md), [Architecture](03-architecture.md), [Build plan](06-build-plan.md)*

**Undeposited Funds**: A holding account in some accounting software for payments received but not yet grouped into a bank deposit. Bookkeepers use it as a workaround when one payment covers many invoices.\
*Used in: [Pain atlas](05-pain-atlas.md)*

**Unidentified money (unidentified cash)**: Money that has arrived but that nobody has linked to a customer or invoice yet. It can look as if the money never arrived, which leads to wrong reminders and wrong cash decisions.\
*Used in: [Problem](01-problem.md), [Solution](02-solution.md), [Architecture](03-architecture.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Research method](08-research-method.md)*

**Write-off**: Recording an amount as lost and closing the invoice. Small gaps are often written off without anyone knowing whether they were a bank fee, a tax that could be reclaimed, or a discount the customer wasn't entitled to. In Receive to Reconciled, any write-off bigger than a small fee needs a person.\
*Used in: [README](../README.md), [Problem](01-problem.md), [Solution](02-solution.md), [Pain atlas](05-pain-atlas.md)*

## Banks and payment routes

**Account number and routing code**: The bank details a payer needs. The account number identifies the account. The routing code identifies the bank, and its format depends on the country. Some countries use an IBAN instead.\
*Used in: [Airwallex integration](04-airwallex-integration.md)*

**ACH (Automated Clearing House)**: The United States' system for local bank transfers.\
*Used in: [Airwallex integration](04-airwallex-integration.md)*

**Bank-change check (callback)**: The checks a customer's accounts team runs before paying into new bank details: phoning a contact it already has on file, asking for a signed letter, and getting internal approvals. Some freeze payments in the meantime. Example: a callback, then a two-week wait before the new account is used.\
*Used in: [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Risks](07-risks.md), [Research method](08-research-method.md), [Decision log](10-decision-log.md)*

**Bank-detail fraud**: A scam in which fraudsters send a seller's customers fake "new bank details", so payments go to the fraudster. It is why customers check new details so carefully, and why Receive to Reconciled confirms any change through contacts already on file.\
*Used in: [Architecture](03-architecture.md), [Pain atlas](05-pain-atlas.md), [Research method](08-research-method.md)*

**Confirmation of Payee (CoP)**: A check some payers' banks run before sending money. It compares the name the payer typed with the name on the receiving account and may warn of a "no match" or "close match". Airwallex describes it for payers in Australia, where the warning never blocks the payment. What payers in the UK and EU see when paying a new Airwallex account is one of our open questions.\
*Used in: [Airwallex integration](04-airwallex-integration.md)*

**Correspondent bank (intermediary bank)**: A bank in the middle of an international transfer, passing the money between the sender's bank and the receiver's bank. Each one may keep a fee, so less arrives. Example: a €20 fee kept by a bank on the way.\
*Used in: [README](../README.md), [Problem](01-problem.md), [Solution](02-solution.md), [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md), [India module](india-module.md)*

**IBAN (International Bank Account Number)**: A standard account number format, used across Europe and in many other countries, that combines the country, the bank and the account in one string.\
*Used in: [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md)*

**Local transfer (local rails)**: A payment made through a country's own payment system instead of across borders. Those systems are called local rails: SEPA in the euro area, ACH in the US. A local transfer doesn't pass along the chain of intermediary banks that a SWIFT wire can, so it avoids their fees. Example: a German client pays a euro account by an ordinary local transfer.\
*Used in: [Solution](02-solution.md), [Airwallex integration](04-airwallex-integration.md)*

**MT103**: The standard SWIFT message for a customer's international payment. A payer can share it as proof that a payment was sent, which helps trace a wire that hasn't arrived.\
*Used in: [Pain atlas](05-pain-atlas.md)*

**OUR (fee instruction)**: A choice the payer makes when sending an international wire, meaning "the sender pays all the fees", so the full amount should reach the seller. A common workaround for short payments is to ask payers to choose OUR. The other choices share the fees or pass them to the receiver.\
*Used in: [Pain atlas](05-pain-atlas.md)*

**Returned payment (bounced payment)**: A payment sent back to the payer, for example because the receiving account is wrong or closed. A bank may keep a fee, so less comes back. Example: a $500 wire to a wrong account returns as $480.\
*Used in: [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md)*

**SEPA (Single Euro Payments Area)**: The euro area's system for local bank transfers in euros. Airwallex's Dutch and German euro accounts receive euros by SEPA only.\
*Used in: [Airwallex integration](04-airwallex-integration.md)*

**SWIFT (Society for Worldwide Interbank Financial Telecommunication)**: The international network banks use to send payments to each other across borders. A SWIFT wire can pass through several intermediary banks on the way.\
*Used in: [Problem](01-problem.md), [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md)*

**Verification of Payee (VoP)**: The EU's name check, similar to Confirmation of Payee: the payer's bank compares the name entered with the name on the account before sending. Airwallex documents it only for transfers going out of Airwallex.\
*Used in: [Airwallex integration](04-airwallex-integration.md)*

**Wire transfer (international wire)**: A bank-to-bank transfer. In our docs it usually means an international one, sent over SWIFT.\
*Used in: [README](../README.md), [Problem](01-problem.md), [Solution](02-solution.md), [Pain atlas](05-pain-atlas.md), [Risks](07-risks.md)*

## Airwallex

**Beneficiary**: A saved payee, such as a supplier, whose bank details are stored so it can be paid. On Airwallex it is created with `POST /api/v1/beneficiaries/create`.\
*Used in: [Airwallex integration](04-airwallex-integration.md)*

**Builder Guide**: Airwallex's guide for builders in this hackathon. It asks builders to choose a finance task someone repeats and identify the decision inside it. It also asks for synthetic data and recommends keeping sandbox-only calls replaceable.\
*Used in: [Solution](02-solution.md), [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Build plan](06-build-plan.md), [Risks](07-risks.md), [Decision log](10-decision-log.md)*

**Conversion**: Exchanging money from one currency into another inside Airwallex. It is booked with `POST /api/v1/fx/conversions/create` and can use the `quote_id` of an FX quote, so the rate is the one that was agreed.\
*Used in: [README](../README.md), [Problem](01-problem.md), [Solution](02-solution.md), [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Risks](07-risks.md), [Research method](08-research-method.md), [Decision log](10-decision-log.md)*

**Dedicated Account per Customer**: A feature of Airwallex's Payments product that gives each customer its own bank account and automatically matches incoming transfers to open payments. Airwallex's own example: open payments of 210, 200 and 100 USD, and the customer sends 500. The first two are paid. The third stays pending, because the remaining 90 USD doesn't cover it. Leftovers are refunded. It is available for businesses registered in certain countries, through an Airwallex Account Manager.\
*Used in: [README](../README.md), [Solution](02-solution.md), [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md), [Risks](07-risks.md), [Research method](08-research-method.md), [Decision log](10-decision-log.md)*

**Deposit**: One incoming payment into a Global Account. Airwallex records its amount, currency, Airwallex's own fee, the payer's details when the sending bank provides them, the reference and the status. It does not show how much the payer originally sent or what fees were taken on the way.\
*Used in: [Solution](02-solution.md), [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Risks](07-risks.md), [Decision log](10-decision-log.md)*

**Deposit status**: Where a deposit stands. PENDING means it has arrived and is on hold for review (most clear automatically). SETTLED means it has been credited. REJECTED means it was refused. REVERSED means the payer's bank recalled it after it was settled. Airwallex sends a webhook for each of these.\
*Used in: [Airwallex integration](04-airwallex-integration.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Decision log](10-decision-log.md)*

**FX quote**: A guaranteed exchange rate for an agreed period, which on Airwallex ranges from `MIN_1` to `HR_24`. Converting at a quote means the rate can't move between deciding and booking.\
*Used in: [Solution](02-solution.md), [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Build plan](06-build-plan.md)*

**FX rate**: FX means foreign exchange. An FX rate is the current price of one currency in another. On Airwallex, "a rate is not a quote": the rate shown is not locked.\
*Used in: [Solution](02-solution.md), [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md)*

**Global Account**: A set of local bank details (an account number and routing code, or an IBAN) that point into a business's Airwallex wallet. The account doesn't hold money itself. A business can create several, so a customer that keeps causing problems can get its own. Example: a euro account that a German client can pay by an ordinary local transfer.\
*Used in: [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Build plan](06-build-plan.md), [India module](india-module.md)*

**Leapfin**: A revenue-recognition and reconciliation tool for accounting teams, bought by Airwallex (reported in June 2026). It works at the accounting end. Receive to Reconciled works earlier, when the money lands.\
*Used in: [README](../README.md), [Solution](02-solution.md), [Airwallex integration](04-airwallex-integration.md), [Risks](07-risks.md)*

**RFI (Request for Information)**: Airwallex asking the business for supporting documents, such as invoices or contracts, about a payment under review. A deposit tagged "RFI requires response" waits until the business replies.\
*Used in: [Airwallex integration](04-airwallex-integration.md)*

**Sandbox**: Airwallex's test environment: fake money, real APIs. Our build and demo run there.\
*Used in: [README](../README.md), [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Build plan](06-build-plan.md), [Risks](07-risks.md)*

**Simulation**: Sandbox-only calls that create test events. Examples: a fake incoming deposit with a chosen amount, payer name and reference, or a test transfer moved to states such as SENT or PAID. The deposit simulation can't set the currency.\
*Used in: [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Build plan](06-build-plan.md)*

**Transfer**: A payment out of Airwallex to a beneficiary, sent by the LOCAL or SWIFT method, optionally at an FX quote.\
*Used in: [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Build plan](06-build-plan.md)*

**Treasury & Ops**: The hackathon area this project is entered in. Treasury means managing a business's cash: what it holds, in which currency, and what it has to pay.\
*Used in: [README](../README.md), [Decision log](10-decision-log.md)*

**Wallet**: Where a business's money sits in Airwallex, one balance per currency. Global Accounts are routes into it.\
*Used in: [Airwallex integration](04-airwallex-integration.md)*

## India's export rules

**AD bank (Authorised Dealer bank)**: An Indian bank licensed by RBI to handle foreign money. It receives export payments and keeps the export records.\
*Used in: [India module](india-module.md)*

**CA (Chartered Accountant)**: A qualified, licensed accountant in India.\
*Used in: [Pain atlas](05-pain-atlas.md), [India module](india-module.md)*

**Declaration route (₹10 lakh)**: For a bill or invoice of up to ₹10 lakh, the bank "may" close the export record on the exporter's own declaration, including a quarterly bulk closure. A reduced value may also be accepted on declaration. "May" means the bank chooses.\
*Used in: [India module](india-module.md)*

**Drawback (duty drawback)**: A customs refund of duties paid on inputs used in exported goods. Some customs offices sent exporters "show cause notices" to recover drawback when foreign banks had deducted charges. CBIC (the Central Board of Indirect Taxes and Customs) said officers may accept a bank's confirmation of those charges.\
*Used in: [India module](india-module.md)*

**eBRC (electronic Bank Realisation Certificate)**: A bank's proof that an export was paid. Banks must generate it only from the data in EDPMS.\
*Used in: [India module](india-module.md)*

**EDF (Export Declaration Form)**: The exporter's declaration of what it exported and its full value. For services, it is filed within 30 days from the end of the month in which the invoice was raised, and one EDF can cover a whole month. For goods through electronic ports, the shipping bill counts as the EDF.\
*Used in: [Pain atlas](05-pain-atlas.md), [India module](india-module.md)*

**EDPMS (Export Data Processing and Monitoring System)**: RBI's system where banks track every export until it is paid. Each export has an entry that stays open until the bank is satisfied the full amount has arrived.\
*Used in: [India module](india-module.md)*

**Export record (export bill)**: The bank's entry for one export, which stays open until a payment is mapped to it. Example: a $1,000 bill paid as $980 stays open until the exporter explains the missing $20.\
*Used in: [Problem](01-problem.md), [Solution](02-solution.md), [Architecture](03-architecture.md), [Pain atlas](05-pain-atlas.md), [Build plan](06-build-plan.md), [Risks](07-risks.md), [Research method](08-research-method.md), [Decision log](10-decision-log.md), [India module](india-module.md)*

**FEMA (Foreign Exchange Management Act)**: India's law on foreign money. Under it, the Foreign Exchange Management (Export and Import of Goods and Services) Regulations, 2026 came into force on 1 October 2026.\
*Used in: [India module](india-module.md)*

**FIRA and FIRC (e-FIRC)**: FIRA is a Foreign Inward Remittance Advice. FIRC is a Foreign Inward Remittance Certificate (e-FIRC when electronic). Both are a bank's proof that foreign money came in. Exporters use them to claim GST refunds. Banks now issue FIRA, and some tax officers still insist on FIRC or eBRC.\
*Used in: [Pain atlas](05-pain-atlas.md), [India module](india-module.md)*

**GST (Goods and Services Tax)**: India's sales tax. Exports carry no GST.\
*Used in: [Problem](01-problem.md), [Pain atlas](05-pain-atlas.md), [India module](india-module.md)*

**GST refund**: Because exports carry no GST, exporters can claim back the GST they paid on their own costs. The claim needs proof the export was paid, such as a FIRA or eBRC, and open export records can block it.\
*Used in: [Problem](01-problem.md), [Pain atlas](05-pain-atlas.md), [India module](india-module.md)*

**IEC (Importer-Exporter Code)**: An Indian business's code for importing and exporting. Some Indian banks won't credit a foreign payment until the export form is filed or the IEC is supplied.\
*Used in: [Pain atlas](05-pain-atlas.md)*

**IRM (Inward Remittance Message)**: The bank's record of one incoming foreign payment. It gets mapped to export bills so that they can be closed.\
*Used in: [Pain atlas](05-pain-atlas.md), [India module](india-module.md)*

**Lakh**: An Indian unit of counting: 1 lakh is 100,000. So ₹10 lakh is ₹1,000,000.\
*Used in: [Pain atlas](05-pain-atlas.md), [India module](india-module.md)*

**Letter of credit (irrevocable)**: A bank's promise to pay the exporter once agreed conditions are met. Irrevocable means it can't be cancelled without agreement. If export money is unpaid for over a year past the due date, the exporter may export only against full advance payment or an irrevocable letter of credit.\
*Used in: [India module](india-module.md)*

**Master Direction (RBI)**: RBI's older, consolidated instructions on exports, last updated 17 July 2026. It still governs transactions from before 1 October 2026.\
*Used in: [Problem](01-problem.md), [Risks](07-risks.md), [India module](india-module.md)*

**Nine-month rule**: Export money must arrive within nine months of shipment (goods) or of the invoice date (services), or twelve months if invoiced or settled in rupees. The bank may extend this. Older articles that quote fifteen months are out of date.\
*Used in: [Problem](01-problem.md), [India module](india-module.md)*

**NOC (No Objection Certificate)**: A letter saying the issuer has no objection to something. Some exporters paid through platforms ask the platform for one when their bank can't see a foreign payment to close the export record against.\
*Used in: [Pain atlas](05-pain-atlas.md)*

**RBI (Reserve Bank of India)**: India's central bank. It sets the rules for receiving money from exports.\
*Used in: [Problem](01-problem.md), [Risks](07-risks.md), [India module](india-module.md)*

**Realisation**: The bank's word for export money actually being received. It appears in the name of the eBRC (Bank Realisation Certificate) and in bank fees such as a charge for a "reduction in the export realization".\
*Used in: [India module](india-module.md)*

**Reduction**: Accepting a lower value for an export than was declared, for example because bank charges came off. Up to ₹10 lakh it can be accepted on the exporter's declaration. Above that, the bank must be satisfied with the reasons. RBI's older Master Direction capped reductions at 25% of invoice value, with exceptions. The 2026 regulations name no percentage and leave it to each bank's policy, and we have not confirmed whether 25% still applies to new exports.\
*Used in: [India module](india-module.md)*

**Shipping bill**: The customs document filed when goods leave India. For goods through electronic ports, it counts as the EDF.\
*Used in: [India module](india-module.md)*

**SOFTEX**: The older declaration form for software exports, certified by STPI (Software Technology Parks of India). Under the 2026 regulations, software counts as a service.\
*Used in: [India module](india-module.md)*

**Third-party payment**: A payment from someone other than the customer on the invoice. An Indian bank may hold it until the exporter proves the payer and the customer are the same business. Example: a designer's payment is held until she proves her brand name and legal name belong to the same entity.\
*Used in: [Pain atlas](05-pain-atlas.md)*

## How the software works

**Agent**: Software that works towards a goal on its own: it takes steps, makes decisions within set limits, and hands anything unclear to a person. Receive to Reconciled runs all day alongside an Airwallex account. It isn't a chatbot.\
*Used in: [README](../README.md), [Solution](02-solution.md), [Architecture](03-architecture.md), [Build plan](06-build-plan.md), [Risks](07-risks.md), [Research method](08-research-method.md), [Decision log](10-decision-log.md), [Numbers register](../research/numbers.md)*

**API (Application Programming Interface)**: A way for one program to use another. Receive to Reconciled calls Airwallex's REST API (requests sent over the web, authorised with API keys) to read deposits, open accounts, convert money and pay suppliers.\
*Used in: [Solution](02-solution.md), [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Build plan](06-build-plan.md), [Research method](08-research-method.md), [Decision log](10-decision-log.md)*

**Approval card**: A screen in our dashboard that shows a person exactly what they are approving: the amount, currency, FX quote, payee, evidence and the suggested answer. The approval counts only for those exact terms. If any of them changes, it has to be approved again.\
*Used in: [Architecture](03-architecture.md), [Build plan](06-build-plan.md)*

**Attack test**: A test that tries to trick or break the system on purpose. Examples: instructions hidden in a PDF or email, duplicate or out-of-order webhooks, retries after timeouts, tampered approvals, and an approval given after its FX quote has expired.\
*Used in: [Build plan](06-build-plan.md)*

**Audit log (audit trail)**: A record of every action and decision: what was seen, which rule applied and who approved it. Ours is append-only: entries can be added but never changed or deleted.\
*Used in: [Architecture](03-architecture.md), [Build plan](06-build-plan.md)*

**Bank-change pack**: What Receive to Reconciled prepares when a client is moved to new bank details: a letter naming the old and new details, contacts on file for the callback, and the update for the client's supplier portal. Nothing goes to the client until the owner approves it.\
*Used in: [Solution](02-solution.md), [Architecture](03-architecture.md), [Build plan](06-build-plan.md)*

**Bearer token**: A temporary pass that a program shows with each request to prove it has logged in. Airwallex's lasts 30 minutes, so our connector refreshes it.\
*Used in: [Airwallex integration](04-airwallex-integration.md), [Build plan](06-build-plan.md)*

**Confidence level**: How sure the matching engine is about a match. When confidence is low, the agent asks a person instead of recording the match.\
*Used in: [Solution](02-solution.md), [Build plan](06-build-plan.md), [India module](india-module.md)*

**Exception queue**: The list of payments the agent couldn't settle on its own. Each one waits for a person, with the question already written.\
*Used in: [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Build plan](06-build-plan.md)*

**Idempotency (request ID)**: Making sure that repeating a request doesn't repeat its effect. Every money-moving call to Airwallex carries a unique `request_id`, reused only to retry that same call, so a retry after a timeout can't pay a supplier twice.\
*Used in: [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md)*

**Language model (LLM, large language model)**: AI software that reads and writes text. We use one only to read messy text, such as a client's email or PDF, and to draft the wording of messages. Code checks every figure it reads against the numbers, and it has no tools to move money or change records.\
*Used in: [README](../README.md), [Architecture](03-architecture.md), [Pain atlas](05-pain-atlas.md), [Decision log](10-decision-log.md), [India module](india-module.md)*

**MCP (Model Context Protocol)**: A standard way for AI assistants to use outside tools. Airwallex offers a developer MCP, but it can't create a Global Account, so we use the REST API.\
*Used in: [Airwallex integration](04-airwallex-integration.md)*

**Smoke test**: A quick first test that the basics work. Ours, on day 1: create two euro Global Accounts in the sandbox, simulate deposits and read them back.\
*Used in: [Build plan](06-build-plan.md)*

**State**: The stage something has reached, which can only change along set paths. Example: a deposit starts as Received, can move to Matched, Proposed or Unidentified, and later to NeedsPerson or Returned. Every move is written to the audit log.\
*Used in: [Architecture](03-architecture.md), [Build plan](06-build-plan.md), [Risks](07-risks.md)*

**Synthetic data**: Made-up data that looks realistic, used for testing and demos instead of real customers' records. Our test payments are synthetic, built from real situations in our evidence and labelled as examples.\
*Used in: [Risks](07-risks.md)*

**Webhook**: A message one system sends another automatically when something happens. Airwallex sends one when a deposit arrives or changes status. Webhooks can arrive twice or out of order, so we record each event once and re-read the deposit before acting.\
*Used in: [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Build plan](06-build-plan.md)*

**Webhook signature (HMAC)**: A code attached to each webhook that proves it came from Airwallex and wasn't changed on the way. HMAC (Hash-based Message Authentication Code) is a code made with a shared secret. We recompute it and reject any webhook where it doesn't match.\
*Used in: [Architecture](03-architecture.md), [Airwallex integration](04-airwallex-integration.md), [Build plan](06-build-plan.md)*
