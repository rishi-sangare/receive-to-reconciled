# Decision log

The decisions that shaped Receive to Reconciled, newest first, each with its date and reason. When we change our minds, we add a new entry here rather than editing an old one.

| Date | Decision | Why | Evidence |
|---|---|---|---|
| 22 Oct 2026 | Plan the build as "whole product in week 1, widen and test in week 2, refine in week 3" | With modern AI coding tools, a working end-to-end loop in the first week is realistic. Layering means a slip costs the top layer, not the core. | [Build plan](06-build-plan.md) |
| 22 Oct 2026 | Language models only read messy text; rules in code make every decision | Money decisions must be exact and explainable. Outside text must never be able to move money. | [Architecture](03-architecture.md) |
| 22 Oct 2026 | Move "incoming payments held for review" from build-first to build-later | A follow-up found 13 of 171 Airwallex reviews describing a hold on an incoming payment, mostly later or large payments, and Airwallex makes the hold decision itself | [pain-map-items.csv](../research/data/pain-map-items.csv), lane "Follow-up: holds on first deposits" |
| 22 Oct 2026 | Treat the switch to a client's own account as a guided process, not a single message | Clients' accounts teams verify new bank details by phone, letters and portal approvals, sometimes freezing them for two weeks | [Risks](07-risks.md); pain A38 in [pains.csv](../research/data/pains.csv) |
| 22 Oct 2026 | Build on Airwallex's per-customer accounts instead of claiming the idea as new | Airwallex already offers per-customer accounts that match full payments | [Airwallex integration](04-airwallex-integration.md) |
| 22 Oct 2026 | Build first for 7 of the 56 problems | They survived the skeptic, aren't solved today, and can be fixed with Airwallex's APIs | [Pain atlas](05-pain-atlas.md) |
| 21 Oct 2026 | Keep-or-convert stays in, but isn't the headline | The evidence for "converting money twice" as a pain was weak; the decision is still needed to finish the loop with money moving | [evidence-test-ledger.csv](../research/data/evidence-test-ledger.csv), claim R6 |
| 21 Oct 2026 | Choose Receive to Reconciled over the payables-timing agent | It had a clearer, current gap (short, partial and bundled payments; India's export records). The alternative's cost to the buyer turned out small. | [Research method](08-research-method.md#step-2-testing-the-evidence-21-october) |
| 21 Oct 2026 | Narrow the idea to "the exception desk for cross-border receipts" | Normal tools match the easy cases; the value is in the ones they can't | Same |
| 17 Oct 2026 | Fold an "export proceeds guardian" idea into this one, as the India module | Same customers, same data, same moment in the money's journey | [ideas-compared.csv](../research/data/ideas-compared.csv) |
| 12–17 Oct 2026 | Pick our own idea in the Treasury & Ops area rather than a starter kit | The Builder Guide says reconciliation has no kit yet and calls it "Good territory if you want a problem few other builders will take on" | [Builder Guide](https://airwallexdev.com/agentic-banking-builder-guide.md) |
