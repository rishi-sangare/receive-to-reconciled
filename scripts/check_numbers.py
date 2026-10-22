"""Recount every number in research/numbers.md from the record files, and fail if any has drifted.

Usage: python scripts/check_numbers.py
Each row of the register has a `key`. This script computes that key from the CSV files in research/data/
and compares it with the value written in the register.
"""
import csv, re, sys
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parent.parent
D = root / 'research' / 'data'

def rows(name):
    with open(D / name, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))

ideas, repos, ledger = rows('ideas-compared.csv'), rows('repos-reviewed.csv'), rows('evidence-test-ledger.csv')
items, pains, hyps = rows('pain-map-items.csv'), rows('pains.csv'), rows('hypotheses.csv')
main = [r for r in items if r['round'].startswith('main')]
follow = [r for r in items if r['round'].startswith('follow')]
lc, mc, fc = Counter(r['check'] for r in ledger), Counter(r['check'] for r in main), Counter(r['check'] for r in follow)
bc, hc = Counter(r['build_call'] for r in pains), Counter(r['verdict'] for r in hyps)

actual = {
    'ideas_compared': len(ideas),
    'repos_reviewed': len(repos),
    'repos_entrants': sum(r['entrant'] == 'yes' for r in repos),
    'evidence_items': len(ledger),
    'evidence_items_r2r': sum(r['problem'] == 'Receive to Reconciled' for r in ledger),
    'evidence_rechecked_ok': lc['verified'] + lc['partly'],
    'evidence_verified_exact': lc['verified'],
    'evidence_verified_corrected': lc['partly'],
    'evidence_wrong': lc['wrong'],
    'evidence_unreachable': lc['unreachable'],
    'evidence_not_rechecked': lc['unchecked'],
    'pain_items': len(items),
    'pain_items_main': len(main),
    'pain_items_followup': len(follow),
    'pain_main_rechecked_ok': mc['verified'] + mc['partly'],
    'pain_main_wrong': mc['wrong'],
    'pain_main_unreachable': mc['unreachable'],
    'pain_followup_hand_checked': fc['verified'],
    'pains': len(pains),
    'pains_build_first': bc['build_first'],
    'pains_build_later': bc['build_later'],
    'pains_mention_only': bc['mention_only'],
    'pains_out_of_scope': bc['out_of_scope'],
    'hypotheses': len(hyps),
    'hypotheses_confirmed': hc['confirmed'],
    'hypotheses_weakened': hc['weakened'],
    'veteran_insights': sum(bool(r['veteran_insight']) for r in items),
    'sources_cited': len(re.findall(r'^### C\d+', (root / 'research' / 'citations.md').read_text(encoding='utf-8'), re.M)),
    'glossary_terms': len(re.findall(r'^\*\*[^*]+\*\*:', (root / 'docs' / '09-glossary.md').read_text(encoding='utf-8'), re.M)),
}

register = (root / 'research' / 'numbers.md').read_text(encoding='utf-8')
written = {k: int(v.replace(',', '')) for k, v in re.findall(r'^\|\s*`([a-z0-9_]+)`\s*\|\s*\*\*([\d,]+)\*\*', register, re.M)}
bad = 0
for k, v in actual.items():
    w = written.get(k)
    status = 'ok' if w == v else 'MISMATCH'
    bad += status != 'ok'
    print(f'{status:9} {k:32} register={w} recount={v}')
missing = set(written) - set(actual)
for k in sorted(missing):
    print(f'UNKNOWN   {k} is in the register but has no recount rule')
sys.exit(1 if bad or missing else 0)
