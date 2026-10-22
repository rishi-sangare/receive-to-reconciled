# The problem

## In plain words

Small businesses that sell abroad get paid by bank transfer. The money often arrives with **less than the invoice**, from **a different name** than the customer, with **a reference that says nothing useful**. Somebody then has to work out who paid, for which invoices, and why money is missing. Usually it's the founder, a bookkeeper or an accounts clerk, and they do it by hand. The same customers cause the same mess every month, because nothing fixes the reason.

## One payment, step by step *(a made-up example)*

<p align="center"><img src="../assets/gap.svg" width="100%" alt="A €1,000 invoice splits into €930 received, a €50 credit and a €20 bank fee."></p>

A small design agency in Mumbai runs its business through a company in Singapore with an Airwallex account. It sends a client in Germany two invoices, for €600 and €400. One payment arrives: **€930** from "ACME HOLDING BV", reference "MARCH".

| Question | What's true | Why it's hard |
|---|---|---|
| Who paid? | The client's parent company | The name on the payment isn't the name on the invoice |
| For which invoices? | Both | The reference "MARCH" names neither |
| Why €70 short? | €50 credit for a late delivery, plus a €20 fee kept by a bank on the way | Nobody told the agency. The only clue is an email in someone's inbox. |

Each part of this example happens in real life:

- "This happens on maybe 60% of our international wires. Amount received never matches amount sent" ([r/Accounting, 24 Feb 2026](https://www.reddit.com/r/Accounting/comments/1rdaid8/how_do_you_get_paid_in_full_on_international_wire/)). That is one accountant's experience, not a measured rate.
- "In the example of one payment matched to multiple sales invoices, there is usually a remittance provided by the client that we need to file with the payment" ([Xero Product Ideas, 7 May 2024](https://productideas.xero.com/forums/967136-banking-chart-of-accounts/suggestions/48398618-bank-reconciliation-add-attachment-to-find-mat)). A *remittance* is the customer's note saying which invoices a payment covers.

## Why it keeps happening

**1. The money and its explanation travel separately.** The bank shows an amount and a short reference. The breakdown comes later, by email, PDF or the customer's supplier portal, if it comes at all. Large companies employ people to collect it. One cash-application job ad listed the duty to "Utilize shared mailboxes and customer web portals to identify, retrieve and organize remittance details" ([job ad, 21 Jul 2026](https://jobs.anitab.org/companies/amazon-3-60ad394d-c673-4474-9694-344b0cae748f/jobs/86957271-sr-finops-analyst-ar-aws-cash-app-hyd)).

**2. Banks along the way take a cut.** An international transfer (a SWIFT wire) can pass through several banks, and each can keep a fee. "International wire transfers often pass through correspondent banks that deduct $15–$30 in “SWIFT fees” before the money even reaches India" ([Razorpay, 23 Jan 2026](https://razorpay.com/blog/bank-charges-inward-remittance-india/)). A *correspondent bank* is a bank in the middle of the chain.

**3. Customers deduct things without saying so.** Early-payment discounts, credit notes, disputes and tax withheld at source all reduce what arrives. "The issue comes when they pay the lesser amount, i need to create a credit note for the 'missing' amount before i match off the bank payment" ([Xero Product Ideas, 24 Sep 2026](https://productideas.xero.com/forums/967115-invoices-quotes/suggestions/44960470-invoice-prompt-payment-settlement-discount)).

**4. Software handles the clean cases, and people get the rest.** Xero says it is "tackling more complex use cases, like scenarios where a single payment covers multiple invoices" ([Xero blog, 14 Aug 2026](https://blog.xero.com/?p=40102)). In testing that ran for up to ten weeks, one tester reported that Xero's automatic matching "is not able to reconcile part payments made by customer even though the invoice number and customer name is already in the description" ([Digit, 31 Mar 2026](https://digit.business/insights/xero/xero-auto-reconciliation-testing-notes)). Even very large firms struggle: in a Nacha survey of "mega-corporations", "more than half of the respondents reported that a paltry 0%-20% of payments were processed automatically" ([Nacha, 23 Jul 2021](https://www.nacha.org/news/goofus-and-gallant-cash-application)).

**5. For Indian exporters, it's also a legal task.** Export money must be received within "nine months" ([RBI Master Direction](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=10395)). Each payment has to be tied to its export record at the bank, and short payments need explaining. One exporter's bank asked "500+18% GST per invoice" to link 2,000 shipments ([r/CharteredAccountants, 10 Dec 2024](https://reddit.com/r/CharteredAccountants/comments/1haudd7/bank_is_denying_to_issue_irm_for_ebrc_shipments/)). See the [India module](india-module.md).

## What it costs

- **Time.** Matching and chasing by hand, often in a spreadsheet beside the bank statement.
- **Money.** Small gaps get written off without anyone knowing whether they were a fee, a tax that could be reclaimed, or a discount the customer wasn't entitled to.
- **Relationships.** Reminders go to customers who already paid, because their payment wasn't matched.
- **Wrong cash decisions.** Unidentified money looks like money that hasn't arrived, so a business may convert currency it already has, or count the same money twice.
- **Compliance.** For Indian exporters, open export records can block refunds and incentives.

## Who feels it

| Who | Why |
|---|---|
| Small exporters and agencies paid in foreign currency | They do this every month, often at night, with no finance team |
| Bookkeepers serving many small clients | They inherit the mess at month-end, across dozens of businesses |
| Accounts clerks at mid-sized firms | It's their job, and the hard 20% takes most of the time |
| The paying customer's accounts team | They get chased for invoices they already paid |

The full map of 56 problems, scored and linked to their evidence, is in [the pain atlas](05-pain-atlas.md).
