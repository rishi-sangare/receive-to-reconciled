"""Generate the animated SVG visuals in assets/ for the README and docs.

Every number shown in a visual is either part of a labelled worked example or is counted live from
research/data/*.csv, so the pictures can never drift from the records.

Usage: python scripts/build_visuals.py
"""
import csv
from collections import Counter
from pathlib import Path

root = Path(__file__).resolve().parent.parent
out = root / 'assets'
out.mkdir(exist_ok=True)

# Palette: a ledger at night. Navy paper, teal for money that reconciles, amber for credits,
# coral for money lost on the way, violet for the agent's own work.
C = dict(bg0='#0A1324', bg1='#0F1F3A', card='#0E1A30', line='#22324F', rule='#16243F', text='#E7EEF8',
         muted='#8C9DBA', teal='#2DD4BF', teal2='#14B8A6', amber='#F6B94C', coral='#F7776E',
         green='#4ADE80', violet='#A78BFA', blue='#60A5FA')
SANS = "'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
MONO = "ui-monospace, 'SFMono-Regular', 'Cascadia Mono', Menlo, Consolas, monospace"


def esc(s):
    return str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


class Anim:
    """Collects CSS keyframes so each element can appear and disappear at chosen points of one loop."""

    def __init__(self, T):
        self.T, self.rules, self.n = T, [], 0

    def show(self, s, e, fade=1.5):
        """Class name for an element visible from s% to e% of the loop (hidden otherwise)."""
        self.n += 1
        k = f'a{self.n}'
        a, b = max(s, 0.01), min(s + fade, e)
        c, d = e, min(e + fade, 99.99)
        self.rules.append(f'@keyframes {k}{{0%,{a:.2f}%{{opacity:0}}{b:.2f}%,{c:.2f}%{{opacity:1}}{d:.2f}%,100%{{opacity:0}}}}'
                          f'.{k}{{animation:{k} {self.T}s linear infinite}}')
        return k

    def grow(self, s, e, end=96, axis='X'):
        """Class name for an element that scales from 0 to full between s% and e%, holds, then resets."""
        self.n += 1
        k = f'g{self.n}'
        self.rules.append(f'@keyframes {k}{{0%,{s:.2f}%{{transform:scale{axis}(0)}}{e:.2f}%,{end:.2f}%{{transform:scale{axis}(1)}}'
                          f'{min(end + 2, 99.9):.2f}%,100%{{transform:scale{axis}(0)}}}}'
                          f'.{k}{{transform-box:fill-box;transform-origin:{"left center" if axis == "X" else "center bottom"};'
                          f'animation:{k} {self.T}s cubic-bezier(.2,.7,.2,1) infinite}}')
        return k

    def pulse(self, s, e):
        self.n += 1
        k = f'p{self.n}'
        steps = ''.join(f'{s + (e - s) * i / 6:.2f}%{{opacity:{1 if i % 2 == 0 else .35}}}' for i in range(7))
        self.rules.append(f'@keyframes {k}{{0%{{opacity:1}}{steps}100%{{opacity:1}}}}.{k}{{animation:{k} {self.T}s linear infinite}}')
        return k

    def css(self):
        return ('\n'.join(self.rules) +
                '\n@media (prefers-reduced-motion: reduce){*{animation:none!important}}')


def svg(w, h, body, anim, title, desc):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">
<title id="t">{esc(title)}</title>
<desc id="d">{esc(desc)}</desc>
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{C['bg0']}"/><stop offset="1" stop-color="{C['bg1']}"/></linearGradient>
<linearGradient id="tealgrad" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{C['teal']}"/><stop offset="1" stop-color="{C['blue']}"/></linearGradient>
<pattern id="ledger" width="{w}" height="28" patternUnits="userSpaceOnUse"><line x1="0" y1="27.5" x2="{w}" y2="27.5" stroke="{C['rule']}" stroke-width="1"/></pattern>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{C['muted']}"/></marker>
<marker id="arrowteal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{C['teal']}"/></marker>
</defs>
<style>
.sans{{font-family:{SANS}}} .mono{{font-family:{MONO}}}
{anim.css()}
</style>
<rect width="{w}" height="{h}" rx="24" fill="url(#bg)"/>
<rect width="{w}" height="{h}" rx="24" fill="url(#ledger)" opacity=".55"/>
{body}
</svg>
'''


def text(x, y, s, size=16, fill=None, weight=400, cls='sans', anchor='start', extra=''):
    return (f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" font-weight="{weight}" fill="{fill or C["text"]}" '
            f'text-anchor="{anchor}" {extra}>{esc(s)}</text>')


def pill(x, y, label, color, w=None, cls=''):
    w = w or 18 + 8.4 * len(label)
    return (f'<g class="{cls}"><rect x="{x}" y="{y}" width="{w}" height="30" rx="15" fill="{color}" fill-opacity=".14" stroke="{color}" stroke-opacity=".7"/>'
            f'{text(x + w / 2, y + 20, label, 14, color, 600, anchor="middle")}</g>')


# ---------------------------------------------------------------- 1. Hero: one deposit, decoded
def hero():
    A = Anim(14)
    W, H = 1280, 440
    b = []
    b.append(text(64, 92, 'AIRWALLEX AGENTIC BANKING HACKATHON · TREASURY &amp; OPS'.replace('&amp;', '&'), 14, C['muted'], 600, 'mono', extra='letter-spacing="1.5"'))
    b.append(text(60, 172, 'Receive to', 72, C['text'], 800))
    b.append(f'<text x="60" y="250" class="sans" font-size="72" font-weight="800" fill="url(#tealgrad)">Reconciled</text>')
    b.append(text(64, 300, 'An agent that explains every short cross-border', 22, C['muted']))
    b.append(text(64, 330, 'payment, then fixes why it happened. On Airwallex.', 22, C['muted']))
    x = 64
    for label, col, s, e in [('Matches', C['blue'], 30, 46), ('Explains', C['amber'], 46, 66), ('Fixes the cause', C['violet'], 66, 80), ('Moves the money', C['teal'], 80, 94)]:
        w = 18 + 8.6 * len(label)
        b.append(f'<g>{pill(x, 362, label, C["muted"], w)}</g>')
        b.append(f'<g class="{A.show(s, e)}" filter="url(#glow)">{pill(x, 362, label, col, w)}</g>')
        x += w + 12
    # The deposit card
    cx, cy, cw, ch = 700, 52, 520, 336
    b.append(f'<rect x="{cx}" y="{cy}" width="{cw}" height="{ch}" rx="18" fill="{C["card"]}" stroke="{C["line"]}"/>')
    b.append(text(cx + 28, cy + 38, 'DEPOSIT RECEIVED · EUR', 13, C['muted'], 600, 'mono', extra='letter-spacing="1.2"'))
    b.append(text(cx + cw - 28, cy + 46, '€930.00', 34, C['text'], 700, 'mono', 'end'))
    b.append(text(cx + 28, cy + 74, 'ACME HOLDING BV', 18, C['text'], 600, 'mono'))
    b.append(text(cx + 28, cy + 100, 'reference: "MARCH"', 15, C['muted'], 400, 'mono'))
    b.append(f'<g class="{A.pulse(2, 24)}"><g class="{A.show(0.5, 70)}">{text(cx + cw - 28, cy + 84, "expected €1,000.00", 14, C["muted"], 400, "mono", "end")}'
             f'{text(cx + cw - 28, cy + 106, "−€70.00 ?", 18, C["coral"], 700, "mono", "end")}</g></g>')
    b.append(f'<g class="{A.show(70, 95)}">{text(cx + cw - 28, cy + 84, "every euro explained", 14, C["muted"], 400, "mono", "end")}'
             f'{text(cx + cw - 28, cy + 106, "€70.00 ✓", 18, C["green"], 700, "mono", "end")}</g>')
    b.append(f'<line x1="{cx + 24}" y1="{cy + 124}" x2="{cx + cw - 24}" y2="{cy + 124}" stroke="{C["line"]}" stroke-dasharray="4 6"/>')
    # Reading sweep
    A.rules.append(f'@keyframes sweep{{0%,17%{{transform:translateY(0);opacity:0}}18%{{opacity:.9}}26%{{transform:translateY(190px);opacity:.9}}27%,100%{{transform:translateY(190px);opacity:0}}}}'
                   f'.sweep{{animation:sweep 14s ease-in-out infinite}}')
    b.append(f'<rect class="sweep" x="{cx + 20}" y="{cy + 130}" width="{cw - 40}" height="3" rx="1.5" fill="{C["violet"]}" filter="url(#glow)"/>')
    rows = [('payer', 'Acme Digital (parent company)', C['blue'], ''),
            ('INV-101', '€600.00 ✓', C['text'], C['green']),
            ('INV-102', '€400.00 ✓', C['text'], C['green']),
            ('credit, late delivery', '−€50.00', C['amber'], C['amber']),
            ('bank fee on the way', '−€20.00', C['coral'], C['coral'])]
    y = cy + 158
    for i, (k, v, kc, vc) in enumerate(rows):
        s = 27 + i * 7
        b.append(f'<g class="{A.show(s, 95)}">{text(cx + 28, y, "→ " + k, 15, C["muted"], 400, "mono")}'
                 f'{text(cx + cw - 28, y, v, 15, vc or kc, 600, "mono", "end")}</g>')
        y += 27
    b.append(f'<g class="{A.show(64, 95)}"><rect x="{cx + 24}" y="{y - 14}" width="{cw - 48}" height="40" rx="10" fill="{C["green"]}" fill-opacity=".12" stroke="{C["green"]}" stroke-opacity=".6"/>'
             f'{text(cx + 44, y + 12, "= €930.00", 17, C["green"], 700, "mono")}{text(cx + cw - 44, y + 12, "Reconciled ✓", 17, C["green"], 700, "sans", "end")}</g>')
    (out / 'hero.svg').write_text(svg(W, H, '\n'.join(b), A, 'Receive to Reconciled',
        'A deposit of €930 from ACME HOLDING BV with reference MARCH is decoded line by line: the payer is the client\'s parent company, '
        'it pays INV-101 (€600) and INV-102 (€400), minus a €50 credit for late delivery and a €20 bank fee, equals €930, reconciled.'), encoding='utf-8')


# ---------------------------------------------------------------- 2. Journey: one client, two months
def journey():
    T = 18
    A = Anim(T)
    W, H = 1280, 600
    b = [text(48, 56, 'One client, two months', 30, C['text'], 800),
         text(48, 86, 'The agent doesn\'t just clean up a short payment. It removes the reason it was short.', 17, C['muted'])]
    nw, nh = 230, 66
    xs = [48, 356, 664, 980]

    def node(x, y, title, sub, color, cls=''):
        return (f'<g class="{cls}"><rect x="{x}" y="{y}" width="{nw}" height="{nh}" rx="14" fill="{C["card"]}" stroke="{color}" stroke-opacity=".8"/>'
                f'{text(x + 16, y + 28, title, 16, C["text"], 700)}{text(x + 16, y + 50, sub, 13, C["muted"])}</g>')

    # Lane 1: this month, international wire
    y1 = 150
    b.append(text(48, y1 - 18, 'THIS MONTH · INTERNATIONAL WIRE', 13, C['coral'], 700, 'mono', extra='letter-spacing="1.3"'))
    b.append(node(xs[0], y1, "Client's bank", 'Germany · sends €1,000', C['line']))
    b.append(node(xs[1], y1, 'Bank in the middle', 'keeps a fee, says nothing', C['coral']))
    b.append(node(xs[2], y1, 'Agency on Airwallex', 'deposit arrives', C['blue']))
    b.append(node(xs[3], y1, 'Receive to Reconciled', 'matches, explains, decides', C['violet']))
    for i in range(3):
        b.append(f'<line x1="{xs[i] + nw}" y1="{y1 + 33}" x2="{xs[i + 1] - 4}" y2="{y1 + 33}" stroke="{C["muted"]}" stroke-width="2" marker-end="url(#arrow)"/>')
    b.append(f'<g class="{A.show(12, 30)}">{text(xs[1] + nw / 2, y1 - 2, "−€20 fee", 16, C["coral"], 700, "mono", "middle")}</g>')
    for i, (s, label, col) in enumerate([(37, 'payer: Acme Digital', C['blue']), (40, 'INV-301 paid · €20 bank fee', C['amber']),
                                         (43, "Acme's 3rd short wire this quarter", C['coral'])]):
        b.append(f'<g class="{A.show(s, 96)}">{text(xs[3] + 8, y1 + nh + 26 + i * 22, "✓ " + label if i < 2 else "! " + label, 14, col, 600)}</g>')
    # Coin on lane 1: €1,000 until the middle bank, then €980
    p1 = f'M {xs[0] + nw - 10},{y1 + 33} L {xs[3] + 20},{y1 + 33}'
    b.append(f'<g class="{A.show(3, 36, 1)}"><g>'
             f'<circle r="27" fill="{C["amber"]}" fill-opacity=".18" stroke="{C["amber"]}" stroke-width="2" filter="url(#glow)"/>'
             f'<g class="{A.show(3, 14, .5)}">{text(0, 5, "€1,000", 13, C["amber"], 700, "mono", "middle")}</g>'
             f'<g class="{A.show(14, 36, .5)}">{text(0, 5, "€980", 14, C["coral"], 700, "mono", "middle")}</g>'
             f'<animateMotion dur="{T}s" repeatCount="indefinite" calcMode="linear" keyPoints="0;0;1;1" keyTimes="0;0.04;0.35;1" path="{p1}"/></g></g>')
    # The fix: an arrow from the agent down to the client's new account
    y2 = 410
    fix1 = text(xs[2] + nw / 2 - 24, y2 - 78, "fixes the cause: opens Acme's own euro account", 15, C['teal'], 700, anchor='end')
    fix2 = text(xs[2] + nw / 2 - 24, y2 - 57, "and prepares the bank-change pack for Acme's accounts team", 13, C['muted'], anchor='end')
    lane2 = text(48, y2 - 18, "NEXT MONTH · LOCAL TRANSFER INTO ACME'S OWN ACCOUNT", 13, C['teal'], 700, 'mono', extra='letter-spacing="1.3"')
    bank2 = node(xs[0], y2, "Client's bank", 'Germany · sends €1,000', C['line'])
    acct2 = node(xs[2], y2, "Acme's own account", 'a local euro IBAN on Airwallex', C['teal'])
    b.append(f'<g class="{A.show(47, 96)}"><path d="M {xs[3] + nw / 2},{y1 + nh + 92} C {xs[3] + nw / 2},{y2 - 50} {xs[2] + nw / 2 + 40},{y2 - 80} {xs[2] + nw / 2},{y2 - 6}" '
             f'fill="none" stroke="{C["teal"]}" stroke-width="2.5" stroke-dasharray="7 6" marker-end="url(#arrowteal)"/>{fix1}{fix2}</g>')
    # Lane 2: next month, local transfer into the client's own account
    b.append(f'<g class="{A.show(52, 96)}">{lane2}</g>')
    b.append(f'<g class="{A.show(52, 96)}">{bank2}</g>')
    b.append(f'<g class="{A.show(52, 96)}"><rect x="{xs[1]}" y="{y2}" width="{nw}" height="{nh}" rx="14" fill="none" stroke="{C["muted"]}" stroke-opacity=".35" stroke-dasharray="5 6"/>'
             f'{text(xs[1] + nw / 2, y2 + 30, "no bank in the middle", 15, C["muted"], 600, anchor="middle")}{text(xs[1] + nw / 2, y2 + 50, "ordinary SEPA transfer", 13, C["muted"], anchor="middle")}</g>')
    b.append(f'<g class="{A.show(50, 96)}">{acct2}</g>')
    b.append(f'<g class="{A.show(52, 96)}">{node(xs[3], y2, "Receive to Reconciled", "knows who paid by the account", C["violet"])}</g>')
    b.append(f'<g class="{A.show(52, 96)}"><line x1="{xs[0] + nw}" y1="{y2 + 33}" x2="{xs[2] - 4}" y2="{y2 + 33}" stroke="{C["teal"]}" stroke-width="2" marker-end="url(#arrowteal)"/>'
             f'<line x1="{xs[2] + nw}" y1="{y2 + 33}" x2="{xs[3] - 4}" y2="{y2 + 33}" stroke="{C["teal"]}" stroke-width="2" marker-end="url(#arrowteal)"/></g>')
    p2 = f'M {xs[0] + nw - 10},{y2 + 33} L {xs[3] + 20},{y2 + 33}'
    b.append(f'<g class="{A.show(57, 84, 1)}"><g>'
             f'<circle r="27" fill="{C["teal"]}" fill-opacity=".18" stroke="{C["teal"]}" stroke-width="2" filter="url(#glow)"/>'
             f'{text(0, 5, "€1,000", 13, C["teal"], 700, "mono", "middle")}'
             f'<animateMotion dur="{T}s" repeatCount="indefinite" calcMode="linear" keyPoints="0;0;1;1" keyTimes="0;0.57;0.83;1" path="{p2}"/></g></g>')
    for i, (s, label) in enumerate([(85, 'matched by account, in full'), (88, 'no fee, no guesswork, no chasing')]):
        b.append(f'<g class="{A.show(s, 96)}">{text(xs[3] + 8, y2 + nh + 26 + i * 22, "✓ " + label, 14, C["green"], 600)}</g>')
    b.append(text(48, H - 26, 'Illustration of the agent\'s behaviour. Clients\' accounts teams verify new bank details first, so the agent runs the switch as a guided process.', 13, C['muted']))
    (out / 'journey.svg').write_text(svg(W, H, '\n'.join(b), A, 'One client, two months',
        'This month a €1,000 international wire loses €20 to a bank in the middle and arrives as €980. The agent matches it, explains the fee, '
        'notices it is the client\'s third short wire, and opens the client its own euro account on Airwallex. Next month the client pays by an '
        'ordinary local transfer, €1,000 arrives in full, and it is matched by the account it landed in.'), encoding='utf-8')


# ---------------------------------------------------------------- 3. The gap, explained to the cent
def gap():
    A = Anim(12)
    W, H = 1280, 384
    x0, y, h = 140, 176, 46
    b = [text(48, 56, 'Where did €70 go?', 30, C['text'], 800),
         text(48, 86, 'Every gap is split into named parts that add up to the cent. Each part points to its evidence.', 17, C['muted'])]
    b.append(f'<g class="{A.show(1, 95)}">{text(x0, y - 18, "Invoiced: INV-101 €600 + INV-102 €400 = €1,000", 15, C["muted"], 600, "mono")}'
             f'<rect x="{x0}" y="{y}" width="1000" height="{h}" rx="8" fill="{C["line"]}" fill-opacity=".6"/></g>')
    b.append(f'<rect class="{A.grow(8, 26, 95)}" x="{x0}" y="{y}" width="930" height="{h}" rx="8" fill="{C["teal"]}" fill-opacity=".85"/>')
    b.append(f'<g class="{A.show(24, 95)}">{text(x0 + 24, y + 30, "€930 received", 18, C["bg0"], 800, "mono")}</g>')
    credit_src = text(x0 + 934, y - 24, "from the client's email", 13, C['muted'], anchor='end')
    b.append(f'<g class="{A.show(34, 95)}"><rect x="{x0 + 930}" y="{y}" width="50" height="{h}" fill="{C["amber"]}"/>'
             f'<path d="M {x0 + 955},{y} L {x0 + 955},{y - 40} L {x0 + 940},{y - 40}" fill="none" stroke="{C["amber"]}" stroke-width="1.5"/>'
             f'{text(x0 + 934, y - 44, "€50 credit for late delivery", 15, C["amber"], 700, anchor="end")}{credit_src}</g>')
    b.append(f'<g class="{A.show(46, 95)}"><rect x="{x0 + 980}" y="{y}" width="20" height="{h}" rx="3" fill="{C["coral"]}"/>'
             f'<path d="M {x0 + 990},{y + h} L {x0 + 990},{y + h + 34} L {x0 + 960},{y + h + 34}" fill="none" stroke="{C["coral"]}" stroke-width="1.5"/>'
             f'{text(x0 + 954, y + h + 40, "€20 bank fee taken on the way", 15, C["coral"], 700, anchor="end")}{text(x0 + 954, y + h + 60, "inferred from the route; booked as a fee", 13, C["muted"], anchor="end")}</g>')
    b.append(f'<g class="{A.show(60, 95)}"><rect x="{x0}" y="{H - 66}" width="1000" height="44" rx="12" fill="{C["green"]}" fill-opacity=".1" stroke="{C["green"]}" stroke-opacity=".5"/>'
             f'{text(x0 + 500, H - 37, "€1,000 − €50 credit − €20 bank fee = €930   ✓ every euro accounted for", 17, C["green"], 700, "mono", "middle")}</g>')
    (out / 'gap.svg').write_text(svg(W, H, '\n'.join(b), A, 'Where did €70 go?',
        'A bar for €1,000 invoiced splits into €930 received, a €50 credit for late delivery found in the client\'s email, and a €20 bank fee '
        'taken on the way. €1,000 minus €50 minus €20 equals €930.'), encoding='utf-8')


# ---------------------------------------------------------------- 4. Research, counted from the records
def rows(name):
    with open(root / 'research' / 'data' / name, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def research():
    ideas, repos, ledger = rows('ideas-compared.csv'), rows('repos-reviewed.csv'), rows('evidence-test-ledger.csv')
    items, pains = rows('pain-map-items.csv'), rows('pains.csv')
    n_ideas, n_repos = len(ideas), len(repos)
    n_entr = sum(r['entrant'] == 'yes' for r in repos)
    lc = Counter(r['check'] for r in ledger)
    n_led, n_ok = len(ledger), lc['verified'] + lc['partly']
    n_items, n_pains = len(items), len(pains)
    n_first = sum(p['build_call'] == 'build_first' for p in pains)
    T = 13
    A = Anim(T)
    W, H = 1280, 470
    b = [text(48, 56, 'Built on evidence, with every number on the record', 30, C['text'], 800),
         text(48, 86, 'Counted live from the CSV files in research/data. Recount them yourself: python scripts/check_numbers.py', 17, C['muted'])]
    colw, gap_, top = 280, 20, 120
    cols = [48 + i * (colw + gap_) for i in range(4)]

    def head(i, big, color, l1, l2, s):
        x = cols[i]
        return (f'<g class="{A.show(s, 96)}"><rect x="{x}" y="{top}" width="{colw}" height="300" rx="18" fill="{C["card"]}" stroke="{C["line"]}"/>'
                f'{text(x + 24, top + 66, big, 54, color, 800, "mono")}{text(x + 24, top + 98, l1, 16, C["text"], 700)}'
                f'{text(x + 24, top + 120, l2, 14, C["muted"])}</g>')

    # 1. Ideas: a grid of dots, one lights up
    b.append(head(0, f'{n_ideas}', C['blue'], 'ideas compared', 'before choosing this one', 2))
    for k in range(n_ideas):
        cx, cy = cols[0] + 34 + (k % 7) * 34, top + 160 + (k // 7) * 26
        chosen = k == 0
        glow = ' filter="url(#glow)"' if chosen else ''
        b.append(f'<circle class="{A.show(4 + k * .25, 96, .8)}" cx="{cx}" cy="{cy}" r="{8 if chosen else 6}" fill="{C["teal"] if chosen else C["line"]}"{glow}/>')
    b.append(f'<g class="{A.show(16, 96)}">{text(cols[0] + 24, top + 286, "→ 1 chosen: Receive to Reconciled", 13, C["teal"], 700)}</g>')
    # 2. Repos: squares, entrants filled
    b.append(head(1, f'{n_repos}', C['violet'], 'public repositories read', f'{n_entr} of them hackathon entries', 18))
    for k in range(n_repos):
        sx, sy = cols[1] + 26 + (k % 12) * 19, top + 150 + (k // 12) * 19
        fill = C['violet'] if k < n_entr else 'none'
        b.append(f'<rect class="{A.show(20 + k * .2, 96, .8)}" x="{sx}" y="{sy}" width="13" height="13" rx="3" fill="{fill}" fill-opacity=".8" stroke="{C["violet"]}" stroke-opacity=".6"/>')
    b.append(f'<g class="{A.show(32, 96)}">{text(cols[1] + 24, top + 286, "to avoid building what others are", 13, C["violet"], 700)}</g>')
    # 3. Evidence test: a bar, the re-checked part grows
    b.append(head(2, f'{n_led}', C['amber'], 'sourced items tested', 'the claims behind 2 finalists', 34))
    bx, bw = cols[2] + 24, colw - 48
    b.append(f'<g class="{A.show(36, 96)}"><rect x="{bx}" y="{top + 170}" width="{bw}" height="22" rx="6" fill="{C["line"]}"/></g>')
    b.append(f'<rect class="{A.grow(38, 52, 96)}" x="{bx}" y="{top + 170}" width="{bw * n_ok / n_led:.1f}" height="22" rx="6" fill="{C["green"]}" fill-opacity=".85"/>')
    b.append(f'<g class="{A.show(50, 96)}">{text(bx, top + 220, f"{n_ok} re-opened and confirmed", 15, C["green"], 700, "mono")}'
             f'{text(bx, top + 242, "by a separate checking pass", 13, C["muted"])}</g>')
    b.append(f'<g class="{A.show(54, 96)}">{text(cols[2] + 24, top + 286, "quote, link and date on every row", 13, C["amber"], 700)}</g>')
    # 4. Pain map: a funnel 429 -> 56 -> 7
    b.append(head(3, f'{n_items}', C['teal'], 'sourced items on daily pain', 'from invoice sent to books closed', 56))
    fx, fw = cols[3] + 24, colw - 48
    for j, (val, label, col, s) in enumerate([(n_items, f'{n_items} items', C['teal'], 58), (n_pains, f'{n_pains} distinct problems', C['blue'], 64), (n_first, f'{n_first} we build first', C['green'], 70)]):
        wv = max((fw - 96) * (val / n_items) ** .5, 26)
        yy = top + 150 + j * 40
        b.append(f'<rect class="{A.grow(s, s + 6, 96)}" x="{fx}" y="{yy}" width="{wv:.1f}" height="26" rx="6" fill="{col}" fill-opacity=".8"/>')
        b.append(f'<g class="{A.show(s + 4, 96)}">{text(fx + wv + 10, yy + 18, label, 13, C["text"], 600, "mono")}</g>')
    b.append(f'<g class="{A.show(76, 96)}">{text(cols[3] + 24, top + 286, "scored, then argued against", 13, C["teal"], 700)}</g>')
    (out / 'research.svg').write_text(svg(W, H, '\n'.join(b), A, 'Built on evidence',
        f'{n_ideas} ideas compared and 1 chosen; {n_repos} public repositories read, {n_entr} of them hackathon entries; {n_led} sourced items tested '
        f'the claims behind two finalists, {n_ok} re-opened and confirmed; {n_items} sourced items on daily pain grouped into {n_pains} problems, '
        f'{n_first} of which we build first.'), encoding='utf-8')
    return dict(n_ideas=n_ideas, n_repos=n_repos, n_entr=n_entr, n_led=n_led, n_ok=n_ok, n_items=n_items, n_pains=n_pains, n_first=n_first)


# ---------------------------------------------------------------- 5. Build timeline
def timeline():
    T = 12
    A = Anim(T)
    W, H = 1280, 360
    b = [text(48, 56, 'Three weeks, three layers', 30, C['text'], 800),
         text(48, 86, 'The whole product works end to end by day 7. Everything after that widens it, tests it and refines it.', 17, C['muted'])]
    x0, step, ya = 80, 56, 238
    days = ['25', '26', '27', '28', '29', '30', '31', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']
    xend = x0 + step * (len(days) - 1)
    weeks = [(0, 6, 'Week 1 · the whole product', 'end to end in the sandbox', C['teal']),
             (7, 13, 'Week 2 · widen it, test it hard', 'every case, attacks, real users', C['violet']),
             (14, 19, 'Week 3 · refine and present', 'polish, harden, demo video', C['amber'])]
    for a, z, t1, t2, col in weeks:
        xa, xz = x0 + a * step - 22, x0 + z * step + 22
        b.append(f'<rect x="{xa}" y="118" width="{xz - xa}" height="78" rx="14" fill="{col}" fill-opacity=".1" stroke="{col}" stroke-opacity=".55"/>'
                 f'{text(xa + 18, 150, t1, 17, col, 700)}{text(xa + 18, 174, t2, 14, C["muted"])}')
    b.append(f'<line x1="{x0}" y1="{ya}" x2="{xend}" y2="{ya}" stroke="{C["line"]}" stroke-width="6" stroke-linecap="round"/>')
    b.append(f'<rect class="{A.grow(2, 74, 94)}" x="{x0}" y="{ya - 3}" width="{xend - x0}" height="6" rx="3" fill="url(#tealgrad)" filter="url(#glow)"/>')
    for i, d in enumerate(days):
        x = x0 + i * step
        month = 'Oct' if i < 7 else 'Nov'
        lab = f'{d} {month}' if i in (0, 7, 19) else d
        b.append(f'<circle cx="{x}" cy="{ya}" r="3.5" fill="{C["muted"]}"/>{text(x, ya + 26, lab, 12, C["muted"], 500, "mono", "middle")}')
    for i, l1, l2, col in [(6, '31 Oct', 'the whole loop works', C['teal']), (13, '7 Nov', 'real users have tried it', C['violet']),
                            (18, '12 Nov', 'submitted, a day early', C['green']), (19, '13 Nov', 'deadline', C['coral'])]:
        x = x0 + i * step
        s = 2 + 72 * i / (len(days) - 1)
        anchor = 'end' if i >= 18 else 'middle'
        dx = -(10 if i == 18 else 0) + (12 if i == 19 else 0)
        b.append(f'<g class="{A.show(s, 94)}"><rect x="{x - 9}" y="{ya - 9}" width="18" height="18" transform="rotate(45 {x} {ya})" fill="{col}" filter="url(#glow)"/>'
                 f'{text(x + dx, ya + 62 + (22 if i == 19 else 0), l1, 14, col, 700, "mono", anchor)}{text(x + dx, ya + 80 + (22 if i == 19 else 0), l2, 13, C["text"], 500, "sans", anchor)}</g>')
    (out / 'timeline.svg').write_text(svg(W, H, '\n'.join(b), A, 'Three weeks, three layers',
        'Build plan from 25 October to 13 November 2026. Week 1 builds the whole product end to end, ending 31 October with the loop working in the '
        'sandbox. Week 2 widens and tests it, ending 7 November after real users have tried it. Week 3 refines and presents it; submission on 12 November, '
        'a day before the 13 November deadline.'), encoding='utf-8')


if __name__ == '__main__':
    hero()
    journey()
    gap()
    counts = research()
    timeline()
    print('wrote', sorted(p.name for p in out.glob('*.svg')), counts)
