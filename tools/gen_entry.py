#!/usr/bin/env python3
"""Build render.html for news-image-20261124 V5 (winner-style redesign +
rich vector illustrations drawn in code).

Reads the 23 Nov render.html and reuses its land-polygon <g> (real Natural
Earth country outlines) verbatim, then writes a front page rebuilt on the
visual system the actual news-image winners use (regian 84.1% and pandya
83.3% on news-image-20261123; gentle-meteor-30 85.9% on news-image-01 —
images downloaded and read from /tmp/winners/):

- Contrasting header: full-width dark-navy band, masthead in white.
- Every story inside a neat framed card: region-coloured stat band on
  top, number badge + location kicker + verification pill, headline,
  body, source line. No bare hairline-separated text.
- Region colour system (8 colours) used consistently in the chips row,
  card stat bands, kicker, map badges/dots and the map legend.
- Footer: red DATE CHECK box + how-sure legend, then a dark-navy
  sources strip.
- Fonts: Playfair Display (masthead/headlines) + Libre Franklin
  (labels/body) + Oswald (stat banners), all Google Fonts under SIL
  OFL 1.1, downloaded locally into fonts/ — no network at render time.

V3 adds what v2 missed — the winners' illustrations (Hap's feedback):
each of the 13 top cards (3 leads + 10 features) gets a flat vector
scene drawn in code (inline SVG, no photos, no AI images), with the
stat ribbon overlaid at the bottom of the scene (pandya's device).
The remaining 19 briefs stay text-only, and the map is labelled
"SCENES 1–13" like regian's.

V5 replaces the v4 Lucide icons with rich vector scenes (Hap's
feedback: icons are only pictograms, "cuman icon aja"): the same 13
scenes, now full layered illustrations drawn in code in the approved
Hormuz-example style (tools/scene-hormuz-preview.html) — environment
background + 2-4 layered elements with scale contrast + one small
detail + the stat ribbon inside the scene. No photos, no AI images,
no icon libraries.

Same 32 stories as v1 (news.md unchanged); only the design changes.
Structure: 3 lead cards + 10 feature cards + map + 19 briefs + 2 also.

Run from the entry directory:  python3 tools/gen_entry.py
Writes: render.html
"""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
OLD = Path('/home/hatch/workspace/makefun/entries/news-image-20261123/render.html')

# Region colours — one colour per region, used everywhere (chips, stat
# bands, kickers, map badges/dots, legend).
REGIONS = {
    'ME':  ('MIDDLE EAST', '#c96a1e'),
    'EUR': ('EUROPE', '#1f5fa8'),
    'AFR': ('AFRICA', '#c0392b'),
    'ASIA': ('ASIA', '#1e8a4c'),
    'NAM': ('N. AMERICA', '#6a4fa3'),
    'SAM': ('S. AMERICA', '#b03a7d'),
    'OCE': ('OCEANIA', '#0e7d8c'),
    'WLD': ('WORLD & SPACE', '#14264d'),
}

# Verification pills — honest reading of each story's sourcing.
# OFFICIAL = on the record (court, government, institution statement).
# CONFIRMED = 2+ outlets / acknowledged by the party involved.
# REPORTED = one outlet's report. CLAIM = one side's word only.
STATUS = {
    'OFFICIAL': '#1e7a46',
    'CONFIRMED': '#1f5fa8',
    'REPORTED': '#a31621',
    'CLAIM': '#b7791f',
}

# Light tints of the region colours — scene backgrounds (v3).
TINTS = {
    'ME': '#f7e3cd', 'EUR': '#d9e7f6', 'AFR': '#f6dbd5', 'ASIA': '#d8ecdf',
    'NAM': '#e5ddf2', 'SAM': '#f3dbe9', 'OCE': '#d3e9ec', 'WLD': '#dde3f0',
}

# ---------------------------------------------------------------------------
# V5 — rich vector scenes drawn in code (tools/scenes_v5.py). The v4
# Lucide icons were only pictograms (Hap: "cuman icon aja"); v5 draws
# full layered scenes per card in the approved Hormuz-example style:
# environment background + 2-4 layered elements with scale contrast +
# one small detail + the stat ribbon inside the scene (pandya's device).
# No photos, no AI images, no icon libraries.
import sys as _sys
_sys.path.insert(0, str(Path(__file__).resolve().parent))
from scenes_v5 import scene_svg as _scene_svg_v5


def scene_svg(n, reg, stat, label, lead):
    return _scene_svg_v5(n, reg, stat, label, lead, REGIONS, TINTS)


# (n, region, kicker, headline, body, lat, lon, badge_x, badge_y,
#  stat, stat_label, status, source)
LEADS = [
    (1, 'ASIA', 'HUAWEI — LEAD',
     'US jury finds Huawei guilty — but not of racketeering',
     'Convicted of trade-secret theft and bank fraud; sentencing set for '
     'September 2027.',
     40.7, -74.0, 310, 24, '10 OF 12', 'COUNTS — GUILTY', 'OFFICIAL', 'Reuters'),
    (2, 'ME', 'HORMUZ — LEAD',
     'Four tankers hit mines in the Strait of Hormuz',
     'Iran says the mines struck despite US escorts; Tehran orders the '
     'strait closed day by day.',
     26.5, 56.3, 664, 39, '4 TANKERS', 'HIT BY MINES', 'REPORTED', 'IRGC · JMIC'),
    (3, 'ASIA', 'ICJ — LEAD',
     'World court: Myanmar committed genocide',
     'The ICJ rules 9\u20136 the 2017 Rohingya operations were genocide '
     '\u2014 the first time a state is found responsible.',
     52.1, 4.3, 526, 12, '9–6', 'GENOCIDE RULING', 'OFFICIAL', 'ICJ'),
]

GRID = [
    (4, 'ME', 'RIYADH', 'Houthi strike hits Riyadh\u2019s PIF tower; 11 hurt',
     'Second hit on the Saudi fund\u2019s HQ in under a week.',
     24.7, 46.7, 640, 78, '11 HURT', 'PIF TOWER HIT', 'REPORTED', 'DSO'),
    (5, 'ME', 'YEMEN', 'Houthis 60 km from Aden and \u201cready to attack\u201d',
     'Army says a defence line holds north and west of the temporary capital.',
     12.8, 45.0, 600, 88, '60 KM', 'FROM ADEN', 'REPORTED', 'DSO'),
    (6, 'ME', 'GAZA', 'Israel kills Hamas security chief in Gaza strike',
     'Nahel dies with six others in separate strikes, despite the October ceasefire.',
     31.5, 34.45, 556, 71, '7 KILLED', 'IN GAZA STRIKES', 'REPORTED', 'DSO'),
    (7, 'ME', 'HORMUZ', 'IRGC says it hit a container ship in the Strait',
     'The ship had switched off its navigation systems, Tehran says.',
     26.5, 56.3, 663, 74, '1 SHIP', 'TARGETED', 'CLAIM', 'DSO'),
    (8, 'EUR', 'FINLAND', 'Ukraine hits Russian ship Sparta II in the Gulf',
     'Crew evacuated; Kyiv also claims a corvette sunk off Libya.',
     59.8, 24.7, 546, 34, '16 SAVED', 'CREW EVACUATED', 'CONFIRMED', 'DSO'),
    (9, 'AFR', 'LIBYA', 'Tripoli demands answers from Kyiv over ship strikes',
     'Haftar visits Turkey for the first time, to meet Erdogan in Ankara.',
     32.1, 20.1, 523, 68, '1ST VISIT', 'HAFTAR IN ANKARA', 'REPORTED', 'DSO'),
    (10, 'EUR', 'NATO', 'Rutte vows defence against threats in space',
     'Reports say Russia may launch a nuclear-armed satellite within 60 days.',
     50.85, 4.35, 486, 52, '60 DAYS', 'SATELLITE WARNING', 'OFFICIAL', 'DSO'),
    (11, 'EUR', 'TURKEY', 'Air Force helicopter crash kills five in Eskisehir',
     'Second such crash in 12 days; the cause is not yet known.',
     39.8, 30.5, 559, 17, '5 KILLED', 'HELICOPTER CRASH', 'REPORTED', 'DSO'),
    (12, 'SAM', 'COLOMBIA', 'Gunmen hold 25 hostage in Cartagena supermarket',
     'Five older women freed; the airport briefly halts landings.',
     10.4, -75.5, 252, 61, '25 HELD', 'HOSTAGE IN CARTAGENA', 'REPORTED', 'DSO'),
    (13, 'SAM', 'COLOMBIA', 'Car bomb outside offices in Villavicencio; 23 hurt',
     'President blames narcoterrorism on the eve of the FARC deal\u2019s 10th anniversary.',
     4.15, -73.6, 318, 92, '23 HURT', 'CAR BOMB', 'REPORTED', 'DSO'),
    (14, 'ME', 'IRAQ', 'Baghdad orders federal control of Kurdish oilfields',
     'Barzani calls the move \u201ccompletely unacceptable\u201d.',
     33.3, 44.4, 614, 29, '4 FIELDS', 'UNDER FEDERAL CONTROL', 'OFFICIAL', 'DSO'),
    (15, 'AFR', 'DR CONGO', 'Cargo plane missing; rebels claim a shootdown',
     'Four aboard near Minembwe; pilots said captured, Uganda denies a role.',
     -3.9, 29.1, 530, 116, '4 ABOARD', 'PLANE MISSING', 'CLAIM', 'DSO'),
    (16, 'ASIA', 'VIETNAM', 'Hanoi hot-pot blast kills at least six',
     'A suspected gas leak hits a packed restaurant in Dong Da.',
     21.0, 105.8, 812, 82, '6 KILLED', 'HOT-POT BLAST', 'REPORTED', 'DSO'),
    (17, 'ASIA', 'MALAYSIA', 'Malaysia to send thousands of migrants to Myanmar',
     '1,500 by naval ships in December; Anwar says hosting is unaffordable.',
     3.1, 101.7, 752, 97, '1,500', 'TO BE SENT BACK', 'OFFICIAL', 'DSO'),
    (18, 'ASIA', 'INDONESIA', 'Prabowo names two candidates to replace VP Gibran',
     'Amran Sulaiman and Sugiono nominated after the Nov 12 resignation.',
     -6.2, 106.8, 806, 108, '2 NAMES', 'FOR VP', 'OFFICIAL', 'DSO'),
    (19, 'ASIA', 'CHINA', 'Official sentenced to death for spying',
     'Ma gave 35 state secrets for over 1m yuan, state media report.',
     39.9, 116.4, 838, 24, '35 SECRETS', 'FOR 1M YUAN', 'OFFICIAL', 'DSO'),
    (20, 'ASIA', 'S. KOREA', 'Russian jets near Ulleungdo; shelter order issued',
     'Fighters scrambled as aircraft enter the air defence zone.',
     37.5, 130.9, 872, 58, 'SHELTER', 'ORDER ON ULLEUNGDO', 'OFFICIAL', 'DSO'),
    (21, 'WLD', 'SPACE', 'Shenzhou-24 carries Pakistan\u2019s first astronaut',
     'Zeeshan Ali joins China\u2019s Tiangong station crew.',
     40.9, 100.3, 748, 22, '1ST', 'PAKISTANI IN SPACE', 'OFFICIAL', 'Astrova'),
    (22, 'NAM', 'USA', 'Pentagon rebukes Canada over defence spending',
     'Only 41.9% of its air force fleet is serviceable.',
     38.9, -77.0, 262, 44, '41.9%', 'FLEET SERVICEABLE', 'OFFICIAL', 'DSO'),
    (23, 'ASIA', 'SINGAPORE', 'US blacklists Megaspeed in Nvidia chip scandal',
     'Seven Southeast Asian firms hit with licence rules.',
     1.35, 103.8, 800, 64, '7 FIRMS', 'BLACKLISTED', 'OFFICIAL', 'DSO'),
    (24, 'NAM', 'MEXICO', 'US drone helps capture \u201cEl Chapo Isidro\u201d',
     'Four soldiers and 16 gunmen die; Mexico will try him at home.',
     25.6, -108.5, 178, 70, '20 KILLED', 'IN SINALOA RAID', 'CONFIRMED', 'DSO'),
    (25, 'NAM', 'HAITI', 'Bukele names three soldiers killed in Haiti blast',
     'Families get $200,000 plus a monthly income.',
     18.5, -72.3, 316, 52, '$200,000', 'FOR EACH FAMILY', 'OFFICIAL', 'DSO'),
    (26, 'ASIA', 'BANGLADESH', 'Hasina plans return from exile on Dec 16',
     'Dhaka says the convicted ex-PM should be extradited instead.',
     23.8, 90.4, 718, 42, 'DEC 16', 'RETURN PLANNED', 'REPORTED', 'DSO'),
    (27, 'EUR', 'UK', 'Britain sanctions the Houthis and four officials',
     'Asset freezes and travel bans over Red Sea attacks.',
     51.5, -0.1, 470, 12, '4 NAMED', 'SANCTIONED', 'OFFICIAL', 'DSO'),
    (28, 'EUR', 'UKRAINE', 'Zelenskyy urges four-party talks \u201cas soon as possible\u201d',
     'Kyiv repeats its call for full NATO membership.',
     50.45, 30.5, 596, 12, '4-PARTY', 'TALKS URGED', 'OFFICIAL', 'DSO'),
    (29, 'AFR', 'SUDAN', 'RSF spy chief defects to the army',
     'Al-Tayeb Jabara switches sides in the civil war.',
     15.6, 32.5, 567, 84, 'TOP SPY', 'DEFECTS TO ARMY', 'REPORTED', 'One Turn'),
    (30, 'ASIA', 'NEPAL', '5.6 quake strikes Nepal near the Chinese border',
     'Tremors felt in India, Bhutan and Bangladesh.',
     27.3, 87.5, 752, 40, '5.6', 'QUAKE IN NEPAL', 'CONFIRMED', 'Horizon'),
    (31, 'OCE', 'AUSTRALIA', 'Australia to fine tech giants 5% of global revenue',
     'Canberra targets the biggest platforms.',
     -35.3, 149.1, 880, 108, '5%', 'OF GLOBAL REVENUE', 'REPORTED', 'Astrova'),
    (32, 'AFR', 'SPORT', 'Senegal regain the Africa Cup title',
     'A sports court appeal hands back the crown.',
     14.7, -17.4, 424, 84, 'TITLE', 'BACK TO SENEGAL', 'CONFIRMED', 'DSO'),
]

# Feature cards (10): the most visual / highest-news-value grid stories.
FEATURES = [4, 8, 12, 15, 16, 20, 22, 24, 28, 30]

# One-line briefs for the rest (numeric order), then the two ALSO TODAY items.
# One-line briefs: headline in .bt, short source in .bs (a long .bs with
# white-space:nowrap squeezes the headline to zero width and blows the
# column up — keep sources to one short token).
ALSO = [
    ('Real Madrid hit five past PSV in Europe', 'Astrova'),
    ('Leaked data: 490,000 Russian war deaths', 'One Turn'),
]


def proj(lat, lon):
    """Equirectangular, same as DESIGN.md: lon -180..180 -> x 0..984; lat 75..-52 -> y 0..144."""
    x = (lon + 180.0) / 360.0 * 984.0
    y = (75.0 - lat) / 127.0 * 144.0
    return round(x, 1), round(y, 1)


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('"', '&quot;'))


def region_of(n):
    for row in LEADS + GRID:
        if row[0] == n:
            return row[1]
    return 'WLD'


def main():
    old = OLD.read_text()
    start = old.index('<g fill="#c9bd93"')
    end = old.index('</g>', start) + len('</g>')
    land = old[start:end]

    stories = {r[0]: r for r in GRID}
    counts = {}
    for r in LEADS + GRID:
        counts[r[1]] = counts.get(r[1], 0) + 1

    # --- map: dots + badges coloured by region ---
    dots, badges = [], []
    for r in LEADS + GRID:
        n, reg = r[0], r[1]
        lat, lon, bx, by = r[5], r[6], r[7], r[8]
        col = REGIONS[reg][1]
        ax, ay = proj(lat, lon)
        dots.append(
            f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{col}" stroke-width="1"/>\n'
            f'<circle cx="{ax}" cy="{ay}" r="2.4" fill="{col}"/>')
        badges.append(
            f'<g font-family="Libre Franklin","DejaVu Sans",sans-serif font-size="9.5" '
            f'font-weight="bold" text-anchor="middle">'
            f'<circle cx="{bx}" cy="{by}" r="7.5" fill="{col}" stroke="#fff" '
            f'stroke-width="1.4"/><text x="{bx}" y="{by + 3.5}" fill="#fff">{n}</text></g>')

    # --- lead cards ---
    lead_html = []
    for r in LEADS:
        n, reg, k, h, b = r[0], r[1], r[2], r[3], r[4]
        stat, label, status, src = r[9], r[10], r[11], r[12]
        col = REGIONS[reg][1]
        scol = STATUS[status]
        lead_html.append(
            f'<article class="card lead-card">'
            f'{scene_svg(n, reg, stat, label, lead=True)}'
            f'<div class="kickrow"><span class="num" style="background:{col}">{n}</span>'
            f'<span class="loc" style="color:{col}">{esc(k)}</span>'
            f'<span class="pill" style="border-color:{scol};color:{scol}">{status}</span></div>'
            f'<h2>{esc(h)}</h2><p>{esc(b)}</p>'
            f'<div class="src">{esc(src)}</div></article>')

    # --- feature cards ---
    feat_html = []
    for n in FEATURES:
        r = stories[n]
        reg, k, h, b = r[1], r[2], r[3], r[4]
        stat, label, status, src = r[9], r[10], r[11], r[12]
        col = REGIONS[reg][1]
        scol = STATUS[status]
        feat_html.append(
            f'<article class="card feat-card">'
            f'{scene_svg(n, reg, stat, label, lead=False)}'
            f'<div class="kickrow"><span class="num" style="background:{col}">{n}</span>'
            f'<span class="loc" style="color:{col}">{esc(k)}</span>'
            f'<span class="pill" style="border-color:{scol};color:{scol}">{status}</span></div>'
            f'<h4>{esc(h)}</h4><p>{esc(b)}</p>'
            f'<div class="src">{esc(src)}</div></article>')

    # --- also list: remaining grid stories (one line each) + ALSO TODAY ---
    briefs = []
    for r in GRID:
        if r[0] in FEATURES:
            continue
        n, reg, k, h = r[0], r[1], r[2], r[3]
        col = REGIONS[reg][1]
        # Shorten the three briefs that wrapped to 2 lines: the kicker already
        # names the place, so drop the repeated location word from the text.
        if n == 17:
            h = 'to send thousands of migrants to Myanmar'
        if n == 18:
            h = 'Prabowo names two VP candidates'
        if n == 31:
            h = 'to fine tech giants 5% of revenue'
        briefs.append(
            f'<div class="brief"><span class="num" style="background:{col}">{n}</span>'
            f'<span class="bt"><b>{esc(k)}:</b> {esc(h)}</span>'
            f'<span class="bs">{esc(r[12])}</span></div>')
    for h, b in ALSO:
        briefs.append(
            f'<div class="brief"><span class="num" style="background:#a31621">\u2605</span>'
            f'<span class="bt"><b>ALSO TODAY:</b> {esc(h)}</span>'
            f'<span class="bs">{esc(b)}</span></div>')
    cols, per = [], 7
    for i in range(0, len(briefs), per):
        cols.append('<div class="bcol">' + ''.join(briefs[i:i + per]) + '</div>')

    # --- region chips ---
    chips = ''.join(
        f'<span class="chip" style="background:{REGIONS[r][1]}">'
        f'{REGIONS[r][0]} {counts[r]}</span>'
        for r in ['ME', 'EUR', 'AFR', 'ASIA', 'NAM', 'SAM', 'OCE', 'WLD'])

    # --- map legend ---
    legend = ''.join(
        f'<span class="lg"><i style="background:{REGIONS[r][1]}"></i>'
        f'{REGIONS[r][0]} {counts[r]}</span>'
        for r in ['ME', 'EUR', 'AFR', 'ASIA', 'NAM', 'SAM', 'OCE', 'WLD'])

    css = '''/* Design tokens v2 — winner system, see DESIGN.md. */
/* Fonts: Playfair Display + Libre Franklin + Oswald, Google Fonts, SIL OFL 1.1
   (free for commercial use), downloaded locally into fonts/ — no network. */
@font-face{font-family:"Playfair Display";font-style:normal;font-weight:700 900;font-display:swap;src:url(fonts/PlayfairDisplay-700.woff2) format("woff2")}
@font-face{font-family:"Libre Franklin";font-style:normal;font-weight:400 700;font-display:swap;src:url(fonts/LibreFranklin-400.woff2) format("woff2")}
@font-face{font-family:"Oswald";font-style:normal;font-weight:500 700;font-display:swap;src:url(fonts/Oswald-600.woff2) format("woff2")}
:root{
  --paper:#f7f1de; --ink:#141414; --body:#262626; --muted:#5c5540;
  --accent:#a31621; --navy:#14264d; --gold:#d8b45a; --card:#fffdf4;
  --frame:#d8cfb0; --hairline:#cfc7a4; --land:#c9bd93; --mapbg:#ece5cb;
  --serif:"Playfair Display","Liberation Serif","DejaVu Serif",serif;
  --sans:"Libre Franklin","Liberation Sans","DejaVu Sans",sans-serif;
  --cond:"Oswald","Liberation Sans","DejaVu Sans",sans-serif;
}
*{margin:0;padding:0;box-sizing:border-box}
body{width:1024px;height:1024px;background:var(--paper);color:var(--ink);font-family:var(--sans);overflow:hidden}
.page{width:1024px;height:1024px;padding:0 20px;display:flex;flex-direction:column}
/* Header — full-width navy band, white masthead, gold kicker (winner: gentle-meteor) */
.head{margin:0 -20px;background:var(--navy);color:#fff;padding:6px 20px 7px;border-bottom:3px solid var(--gold);text-align:center}
.head .top{display:flex;justify-content:space-between;font-size:10px;letter-spacing:2.5px;font-weight:bold}
.head .top .l{color:var(--gold)}
.head .top .r{color:#fff}
.head h1{font-family:var(--serif);font-size:48px;line-height:1;font-weight:900;letter-spacing:2px;margin-top:3px}
/* Red headline strip — the 3 leads, red serif on paper (winner: regian/pandya) */
.strip{padding:5px 0 4px;text-align:center;border-bottom:1px solid var(--hairline);
  font-family:var(--serif);font-size:13px;font-weight:bold;color:var(--accent)}
.strip i{font-style:normal;color:var(--ink);padding:0 6px}
/* Region chips — one colour per region, counts (winner: regian/pandya) */
.chips{display:flex;gap:6px;padding:5px 0 6px}
.chip{flex:1;text-align:center;color:#fff;font-size:9px;font-weight:bold;letter-spacing:1px;padding:3px 0}
/* Cards — every story in a neat frame: coloured stat band, badge+kicker+pill, headline, body, source */
.leads{display:flex;gap:10px;margin-bottom:8px}
.feats{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-bottom:8px}
.card{background:var(--card);border:1px solid var(--frame);display:flex;flex-direction:column;overflow:hidden}
.lead-card{flex:1}
/* v5 — rich vector scene with the stat ribbon at its bottom (pandya's
   device); replaces the v2 stat band, so a card grows only by the
   artwork height: +27px lead, +18px per feature row. */
.scene{display:block;width:100%;height:auto}
.kickrow{display:flex;align-items:center;gap:6px;padding:7px 9px 0}
.num{width:16px;height:16px;border-radius:50%;color:#fff;font-size:9.5px;font-weight:bold;text-align:center;line-height:16px;flex:none}
.feat-card .num{width:14px;height:14px;font-size:8.5px;line-height:14px}
.loc{font-size:9px;font-weight:bold;letter-spacing:1.5px}
.feat-card .loc{font-size:8px}
.pill{margin-left:auto;font-size:7.5px;font-weight:bold;letter-spacing:1px;padding:2px 5px;border:1.5px solid}
.lead-card h2{font-family:var(--serif);font-size:15.5px;line-height:1.18;font-weight:bold;padding:5px 9px 0;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.lead-card p{font-size:10.5px;line-height:1.35;color:var(--body);padding:4px 9px 0;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.feat-card h4{font-family:var(--serif);font-size:11px;line-height:1.2;font-weight:bold;padding:5px 8px 0;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.feat-card p{font-size:9px;line-height:1.3;color:var(--body);padding:3px 8px 0;
  display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.src{font-size:8px;color:var(--muted);letter-spacing:.5px;padding:5px 9px 8px;margin-top:auto}
.feat-card .src{font-size:7.5px;padding:4px 8px 7px}
/* Section labels */
.seclab{display:flex;align-items:center;gap:10px;font-size:10.5px;font-weight:bold;letter-spacing:3px;margin:0 0 5px}
.seclab::before,.seclab::after{content:"";flex:1;border-top:2px solid var(--ink)}
/* Map — framed panel, region-coloured badges + legend */
.map{border:1px solid var(--frame);background:var(--card);padding:5px 10px 5px;margin-bottom:6px}
.map h3{font-size:10.5px;letter-spacing:2.5px;text-align:center;margin-bottom:4px;font-weight:bold}
.map h3 span{color:var(--accent)}
.map .legend{display:flex;justify-content:center;gap:12px;margin-top:4px;font-size:8.5px;font-weight:bold;letter-spacing:1px;color:var(--body)}
.map .legend .lg i{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:4px}
/* Also list — numbered briefs in 3 columns, region badges */
.also{flex:1;min-height:0;display:flex;flex-direction:column}
.briefs{display:flex;gap:16px;flex:1}
.bcol{flex:1;min-width:0;display:flex;flex-direction:column;justify-content:space-between}
.brief{display:flex;align-items:baseline;gap:6px;padding:1.5px 0;border-bottom:1px solid #e2dcc0}
.brief .num{width:15px;height:15px;font-size:8.5px;line-height:15px}
.brief .bt{font-size:9.3px;line-height:1.25;color:var(--body);min-width:0}
.brief .bt b{color:var(--ink)}
.brief .bs{margin-left:auto;font-size:8px;color:var(--muted);white-space:nowrap}
/* Footer — red DATE CHECK box, then navy sources strip */
.foot{margin:0 -20px}
.datecheck{background:var(--accent);color:#fff;display:flex;gap:10px;align-items:flex-start;
  padding:6px 20px;font-size:9.5px;line-height:1.35}
.datecheck b{font-family:var(--cond);font-size:11px;letter-spacing:2px;white-space:nowrap;padding-top:1px}
.datecheck .how{margin-left:auto;text-align:right;font-size:8.5px;white-space:nowrap}
.datecheck .how i{font-style:normal;border:1.5px solid #fff;padding:1px 4px;margin-left:3px;font-size:7.5px;font-weight:bold}
.srcs{background:var(--navy);color:#fff;text-align:center;font-size:9px;letter-spacing:1px;padding:5px 20px}'''

    map_svg = (
        '<svg width="964" height="126" viewBox="0 0 984 144" preserveAspectRatio="xMidYMid meet">\n'
        '<rect width="984" height="144" fill="#e9e2c8"/>\n' + land + '\n'
        '<line x1="0" y1="85.0" x2="984" y2="85.0" stroke="#b7ab7d" stroke-width="0.5" stroke-dasharray="3 4"/>\n'
        '<line x1="0" y1="58.5" x2="984" y2="58.5" stroke="#b7ab7d" stroke-width="0.5" stroke-dasharray="3 4"/>\n'
        '<line x1="0" y1="111.6" x2="984" y2="111.6" stroke="#b7ab7d" stroke-width="0.5" stroke-dasharray="3 4"/>\n'
        '<text x="185" y="14" font-family="Libre Franklin","DejaVu Sans",sans-serif font-size="9" letter-spacing="1.5" fill="#6b5f33" text-anchor="middle">N. AMERICA</text>\n'
        '<text x="335" y="118" font-family="Libre Franklin","DejaVu Sans",sans-serif font-size="9" letter-spacing="1.5" fill="#6b5f33" text-anchor="middle">S. AMERICA</text>\n'
        '<text x="470" y="35" font-family="Libre Franklin","DejaVu Sans",sans-serif font-size="9" letter-spacing="1.5" fill="#6b5f33" text-anchor="middle">EUROPE</text>\n'
        '<text x="570" y="100" font-family="Libre Franklin","DejaVu Sans",sans-serif font-size="9" letter-spacing="1.5" fill="#6b5f33" text-anchor="middle">AFRICA</text>\n'
        '<text x="795" y="28" font-family="Libre Franklin","DejaVu Sans",sans-serif font-size="9" letter-spacing="1.5" fill="#6b5f33" text-anchor="middle">ASIA</text>\n'
        '<text x="862" y="128" font-family="Libre Franklin","DejaVu Sans",sans-serif font-size="9" letter-spacing="1.5" fill="#6b5f33" text-anchor="middle">AUSTRALIA</text>\n'
        + '\n'.join(dots) + '\n' + '\n'.join(badges) + '\n</svg>')

    html = ('<!DOCTYPE html>\n<html><head><meta charset="utf-8"><style>\n' + css +
            '\n</style></head><body><div class="page">\n'
            '<div class="head"><div class="top"><span class="l">THE WORLD IN ONE DAY</span>'
            '<span class="r">TUESDAY 24 NOVEMBER 2026 &nbsp;\u2022&nbsp; 32 STORIES '
            '&nbsp;\u2022&nbsp; 6 CONTINENTS</span></div>'
            '<h1>THE WORLD TODAY</h1></div>\n'
            '<div class="strip">US jury finds Huawei guilty \u2014 but not of racketeering'
            '<i>\u2022</i>Four tankers hit mines in the Strait of Hormuz'
            '<i>\u2022</i>World court: Myanmar committed genocide</div>\n'
            '<div class="chips">' + chips + '</div>\n'
            '<div class="leads">\n' + '\n'.join(lead_html) + '\n</div>\n'
            '<div class="seclab">THE DAY IN 10 MORE</div>\n'
            '<div class="feats">\n' + '\n'.join(feat_html) + '\n</div>\n'
            '<div class="map"><h3>WHERE IT HAPPENED <span>\u2014 SCENES 1\u201313</span> '
            '&nbsp;\u2022&nbsp; NUMBERS MATCH THE STORIES ABOVE</h3>\n' + map_svg +
            '\n<div class="legend">' + legend + '</div></div>\n'
            '<div class="also"><div class="seclab">ALSO ON TUESDAY 24 NOVEMBER \u2014 19 MORE STORIES</div>'
            '<div class="briefs">\n' + '\n'.join(cols) + '\n</div></div>\n'
            '<div class="foot"><div class="datecheck"><b>DATE CHECK</b>'
            '<span>Every story here happened, or was first reported, on '
            'Tuesday 24 November 2026.</span>'
            '<span class="how">HOW SURE <i>CONFIRMED</i> 2+ outlets '
            '<i>OFFICIAL</i> on the record <i>REPORTED</i> one outlet '
            '<i>CLAIM</i> one side\u2019s word</span></div>'
            '<div class="srcs">SOURCES: AP \u2022 REUTERS \u2022 BBC \u2022 DAILY SUMMARY OF WORLD '
            '(DSO) \u2022 THE GLOBAL EYE \u2022 ONETURN.NEWS \u2022 PICTURES AND MAP '
            'DRAWN IN CODE, NOT PHOTOS</div></div>\n'
            '</div></body></html>\n')

    (HERE / 'render.html').write_text(html)
    print('wrote', HERE / 'render.html', len(html), 'bytes')
    # sanity: badge pairs at least 15px apart
    pts = [(r[0], r[7], r[8]) for r in LEADS + GRID]
    bad = []
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            d = ((pts[i][1] - pts[j][1]) ** 2 + (pts[i][2] - pts[j][2]) ** 2) ** 0.5
            if d < 15:
                bad.append((pts[i][0], pts[j][0], round(d, 1)))
    print('badge collisions <15px:', bad if bad else 'none')


if __name__ == '__main__':
    main()
