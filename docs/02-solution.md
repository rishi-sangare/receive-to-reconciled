# The solution

## What Receive to Reconciled does

Receive to Reconciled is an agent that runs alongside a business's Airwallex account. For every payment that arrives, it:

1. **works out who paid and which invoices the payment covers;**
2. **explains any gap,** to the cent: bank fee, credit note, discount, withheld tax or dispute;
3. **records it,** or asks a person when it isn't sure;
4. **fixes the cause,** so the same client doesn't cause the same problem next month;
5. **decides where the money should sit:** keep it in that currency for bills due, or convert only what's missing.

## The decision inside the job

Airwallex's [Builder Guide](https://airwallexdev.com/agentic-banking-builder-guide.md) asks builders to "Choose a finance task that someone repeats and identify the decision inside it", where "The agent should choose differently when a balance, deadline, piece of evidence, or risk changes." Our repeated task is every incoming payment. Our decisions, and what changes them:

| Decision | What changes it |
|---|---|
| Which invoices does this payment settle? | A remittance email arrives; a payer name is confirmed |
| What is each part of the gap? | The client's email names a credit note; a gap turns out to be a round percentage, which points to withheld tax |
| Record it automatically, or ask a person? | Confidence drops; the amount is above a limit |
| Chase the client, or hold back? | Unmatched money from that client is already waiting |
| Change how this client pays? | The third short payment by international wire this quarter |
| Keep the currency or convert it? | Another client's payment is delayed; a bill is due on Friday |

## Step by step

<p align="center"><img src="../assets/journey.svg" width="100%" alt="This month a wire loses €20 on the way; the agent explains it and opens the client its own local account; next month €1,000 arrives in full."></p>

1. **Notices the payment.** Airwallex notifies the agent the moment money lands, with the amount, the payer's name when the sending bank provides it, the reference, and the account it arrived in. [Airwallex integration](04-airwallex-integration.md) lists exactly what a deposit carries.
2. **Works out who paid and for what.** The agent checks, in order: which account the money landed in, an exact invoice reference, then payer names it has learned ("ACME HOLDING BV" is our client Acme Digital, confirmed once by a person). Then it searches for which open invoices add up to the payment, within set tolerances for fees, tax and exchange rates. If two answers fit equally well, a person chooses.
3. **Explains the gap.** For example: €1,000 − €50 credit for late delivery − €20 bank fee = €930. If the client sent an email or PDF, the agent reads it and links each figure to the words it came from.
4. **Records it, or asks.**
   - Small, clear bank fees are recorded automatically.
   - Anything else goes to a person, with a question for the client already written.
   - Half-finished matches are saved, not lost.
   - No reminder goes out while unexplained money from that client is waiting.
5. **Fixes the cause.**
   - It starts with the cheapest fix, such as clearer payment details on the invoice.
   - If a client's bank keeps cutting the reference, or the route keeps costing fees, the agent gives that client its own local bank account through Airwallex. For a German client, that's a euro account they can pay by an ordinary local transfer.
   - Clients' accounts teams check new bank details carefully, so the agent prepares what they'll ask for: a letter naming the old and new details, a known contact to call, and the update for their supplier portal.
   - The old details keep working until the first payment lands on the new account.
6. **Decides where the money sits.** Knowing exactly what has arrived, the agent keeps euros needed for euro bills, converts only the real gap at a locked exchange rate, and pays the supplier. Above a set limit, the owner approves first.

## An example week *(made up, with the arithmetic shown)*

The agency holds €2,000 and some US dollars. It must pay a Berlin animation studio €4,000 on Friday. It is expecting €1,000 from Acme and €1,500 from a second client.

| Day | What happens | What the agent decides |
|---|---|---|
| Monday | Plan the week | €2,000 + €1,000 + €1,500 = €4,500, which covers €4,000. Convert nothing. |
| Tuesday | €930 arrives from "ACME HOLDING BV", reference "MARCH" | Matches both invoices and explains the €70 gap. Cancels Tuesday's reminder to Acme. Acme has now paid short by international wire three times, so it offers Acme its own euro account. |
| Wednesday | The second client emails: its payment is on hold for a missing purchase-order number | Only €2,000 + €930 = €2,930 is certain by Friday, so €1,070 is missing. Convert just €1,070. Re-send the second client's invoice with the purchase-order number instead of a reminder. The conversion is above the agent's limit, so the owner approves it, seeing the amount, the rate and the reasons. |
| Friday | Payment day | €2,930 + €1,070 = €4,000 goes to Berlin on time. The dollar balance stays above its safety cushion. |

Without the agent, the €930 would sit unidentified, Acme would get a wrong reminder, and the agency would either convert too much or come up short on Friday.

## The seven problems we solve first

From the [56 problems we mapped](05-pain-atlas.md), these seven held up best against the evidence, aren't solved by today's tools, and can be fixed with Airwallex's APIs.

| ID | The problem | What the agent does | Rules in code decide | A person decides |
|---|---|---|---|---|
| A01 | Banks along the way take fees, so international payments arrive short | Works out the fee from the gap; offers clients who keep paying this way a local account | Whether the gap fits known fee ranges for that route | Writing off anything bigger than a small fee, or switching the client |
| A10 | A payment can't be matched halfway | Records the parts it's sure of and parks the rest | Records a match only when the parts add up | Unclear lines |
| A13 | One invoice paid in several parts | Keeps a running balance per invoice | What's still owed | Closing an invoice that's still short |
| A26 | Payments matched to the wrong client | Matches only when the account, reference and amount agree | The three-way agreement | When two matches are equally likely |
| A28 | The payment reference gets cut off | Reads the full payment details from Airwallex, not a bank feed | Matching on the full reference and account | Anything still unmatched |
| A38 | Clients are slow to switch to new bank details | Prepares the bank-change pack and confirms the first payment | Fills in the old and new details and the last payments made | Before any request goes to the client |
| A47 | Indian export records stay open after payment | Links each payment to its export record and drafts the note to the bank | Mapping and shortfall | Before the note goes to the bank |

## How it fits with what already exists

| What exists | What it does | What it leaves to a person |
|---|---|---|
| Airwallex's per-customer accounts | A business can give each customer its own account number, and payments that arrive in full are matched ([Airwallex docs](https://www.airwallex.com/docs/payments/payment-methods/global/bank-transfer/dedicated-account-per-customer)) | A transfer too small to cover a payment leaves it "pending". Choosing which clients to move, and getting them to switch. |
| Airwallex and Leapfin | Adds "reconciliation, revenue recognition and broader record-to-report processes" at the accounting end ([IT Brief Australia, 8 Jun 2026](https://itbrief.com.au/story/airwallex-buys-leapfin-to-add-accounting-automation)) | Why a receipt is short, and how the client pays |
| Accounting software's automatic matching | Clean one-to-one matches | Part payments, one payment for many invoices, deductions (see [the problem](01-problem.md)) |

Our agent sits between the money arriving and the books closing. It builds on Airwallex's accounts and adds the explanation, the choice of which clients to move, and the follow-through.

## What a person always controls

- Any write-off above a small fee
- Any amount above the agent's limit
- Any message to a client about new bank details
- Any match where two answers fit equally well
- Anything going to a bank or a tax office

The design behind this is in [Architecture](03-architecture.md).
