# Report — news-image-20261124 (practice entry, 25 Nov 2026)

**Entry v4:** `~/workspace/makefun/entries/news-image-20261124/entry.png`
**Size:** 277,280 bytes · PNG 1024×1024 RGB · SHA-256
`2a82328ae8e62ea28f539b9b614f1058e97a4c48323235364f93277d8f5589ab`
**Entry v3 (archived):** `entry-v3.png`, 278,859 bytes, SHA-256
`e46a5170e938a17a121ec11d6573425ed733a368b0cbef9e7ab45a0f62e73009`
**Entry v2 (archived):** `entry-v2.png`, 281,383 bytes, SHA-256
`990278d8078bd26d07fac158a285b317deb8e3606c63865dfb12a7c2fb81d437`
**Entry v1 (archived):** `entry-v1.png`, 286,617 bytes, SHA-256
`995ba009bcaa345cc958321ff381e3ac392845c536dfb7ba6160e855d555b73b`
**Status:** PRACTICE ONLY. Not submitted to make.fun, no GitHub repo
created, nothing pushed. For Hap to grade.

## What I learned from the winners

From `~/workspace/makefun/study/04-pola-pemenang.md`,
`winners_summary.md`, and the news-image-01 winner (gentle-meteor-30,
judge 85.9%, 92W-6D-9L, cost $0.30, 1 session / 49 turns):

1. **Specific and dense beats generic.** Winners pack 33–35 stories,
   6 continents, one front page + a map. The judge compares two images
   at a time and picks the one that best sums up the day — countable
   density (more real stories, more places) wins pairwise comparisons.
   → This entry: 32 stories + 2 "Also today", 6 continents, front page +
   world map, same as the 23 Nov entry.
2. **Consistency above 75% matters, not perfection.** Winner judge win
   rates are 77–89%. A clean, complete, readable page beats a clever
   page with one broken element. → This entry keeps the 23 Nov layout
   Hap already approved and changes only what improves it (fonts, one
   unified red, two small fixes).
3. **Cheap arenas can win.** The winner cost $0.30 in one focused
   session. → Built in one session, reusing the proven pipeline
   (no new tooling, no paid services).
4. **Winners iterate (v2+).** The 23 Nov entry only became good after
   Hap rejected the blob map and the layout was reworked. → This entry
   was rendered twice; the first render was inspected at 2× zoom and
   two flaws fixed (badge 15's leader line crossing the AFRICA label;
   story 22's "F- / 35s" line break).
5. **Transcripts and authorship are part of winning.** (Not applicable
   to this practice — no bundle built, no submission.)

## The 32 stories — why these

All events happened, or were first reported, on Tuesday 24 November
2026. Sources: Daily Summary Of (30 stories, 64 sources), The Global
Eye, One Turn, AP, Astrova News, Horizon. Full notes in `news.md`.

**Leads (the three stories a picture editor would lead with):**
1. **HUAWEI** — a US jury convicts Huawei of trade-secret theft and
   bank fraud (10 of 12 counts) but acquits on racketeering. The
   biggest US–China tech story of the day; the split verdict is the
   nuance that makes it a lead.
2. **HORMUZ** — four tankers hit mines in the Strait of Hormuz; Iran
   orders the strait closed day by day. The day's most dangerous
   escalation — energy, shipping, and a possible US–Iran confrontation.
3. **ICJ** — the world court finds Myanmar guilty of genocide, 9–6 —
   the first time any state has been found responsible. A historic
   legal first; it anchors the edition.

**Grid (breadth across 6 continents, politics / conflict / law /
tech / science / sport):**
- Middle East & Gulf (4, 5, 6, 7, 14): Riyadh PIF-tower strike,
  Houthis 60 km from Aden, Gaza security-chief killing, IRGC ship
  attack, Baghdad vs Kurdish oilfields — the day's dominant region,
  five stories because the news was genuinely concentrated there.
- Europe & Russia–Ukraine (8, 9, 10, 11, 27, 28): Sparta II strike,
  Libya–Kyiv row, NATO space defence, Turkish helicopter crash,
  UK Houthi sanctions, Zelenskyy's four-party talks.
- Americas (12, 13, 22, 24, 25): Cartagena hostage siege, Villavicencio
  car bomb, Pentagon vs Canada, "El Chapo Isidro" capture, Haiti blast.
- Asia (16, 17, 18, 19, 20, 21, 23, 26, 30): Hanoi blast, Malaysia's
  migrant returns, Indonesia's VP candidates, China's spy death
  sentence, Russian jets near Ulleungdo, Shenzhou-24 + Pakistan's first
  astronaut, Singapore's Nvidia-scandal blacklist, Hasina's return,
  Nepal earthquake.
- Africa (15, 29, 32): Congo plane shootdown claim, RSF spy chief's
  defection, Senegal's Africa Cup title (sport).
- Oceania (31): Australia's 5%-of-revenue tech fines.
- **Also today:** Real Madrid's 5–1 Champions League comeback
  (City 2–2 Napoli, Arsenal 2–2 Dortmund) and the leaked 490,000
  Russian war-death figure + EU's 22nd sanctions package.

**What was left out (alternates in `news.md`):** Gaza meningitis
alert, German school bomb threats, Trump's Iran remarks, US Section
301 tariffs, 2031 Women's World Cup hosts, Indonesia factory fire —
all real, but weaker than the 32 chosen on news value for a
one-image summary.

## Design changes vs 23 Nov (approved layout kept)
- **Fonts:** Playfair Display (masthead/headlines) + Libre Franklin
  (body/labels), both Google Fonts under SIL OFL 1.1, downloaded as
  local woff2 variable fonts — free for commercial use, no network at
  render time. The masthead now reads as a classic newspaper.
- **One red:** map dots/badges unified from inline #b91c1c to the
  design-system accent #a31621.
- **Generator:** `tools/gen_entry.py` now builds `render.html` from
  story data + badge positions, reusing the 251 real Natural Earth
  country polygons from 23 Nov verbatim; it auto-checks every badge
  pair (≥ 15px apart).
- **Two fixes after the first render:** badge 15 moved so its leader
  line misses the AFRICA label; story 22 headline reworded to avoid a
  bad "F- / 35s" break.

## Verification
- PNG 1024×1024, 281,383 bytes (< 1 MiB). ✔
- `main.ts` run twice → identical SHA-256 (`990278d8…`), matching entry.png. ✔
- Visual inspection at full size and 2× map zoom: real world map,
  all 32 badges legible, no overflow, no clipped text, columns even,
  footer on one line. ✔

## V2 — what Hap's feedback changed (25 Nov 2026, evening)

Hap graded v1 "lumayan" and described the WINNING entries:
header/footer with contrasting backgrounds, neat layout, every story
in a neat box frame, good colors, right font choice — and told me to
determine those factors myself. So before redesigning I studied the
actual winning entry images, not just the written patterns.

### What I learned from the winner visuals

Downloaded the real winning artifacts via the make.fun API and read
them visually (`/tmp/winners/`; leaderboard JSONs at `/tmp/lb23.json`,
`/tmp/lb01.json`):
- **regian**, news-image-20261123 winner, judge **84.07%** (44W-9D-1L):
  white header with red kicker "THE WORLD IN ONE DAY", huge navy serif
  masthead, red headline strip, 9 region color chips, dark navy UTC
  timeline strip, 3 lead cards (light bg, **colored top strip**,
  OFFICIAL/REPORTED pill, vector scene, red stat banner like
  "60 BANKS · 70 TANKERS"), 10 feature cards in **visible frames**,
  map panel + "ALSO ON..." 22 briefs in a 2-column numbered list,
  red DATE CHECK footer box + "HOW SURE" legend.
- **pandya**, 20261123 rank 2, judge **83.29%**, 38 stories: dark navy
  header band with white text, huge navy masthead on cream, red
  headline strip, region chips, navy UTC strip, 3 lead cards with big
  vector illustrations, "THE DAY IN 8 MORE" (8 cards with colored
  illustration/stat bands), "ALSO ON..." 27 stories in a 3-column
  numbered list, red DATE CHECK box + legend pills
  (CONFIRMED/OFFICIAL/REPORTED/CLAIM).
- **gentle-meteor-30**, news-image-01 winner, judge **85.9%**
  (92W-6D-9L): full dark navy header band (gold kicker "THE DAY IN
  WORLD NEWS" + white serif masthead), 11 top story cards in a
  4-column grid (each with an illustration band, region-colored number
  badge, headline, body, **visible thin frame**), map panel + ALSO
  list (stories 12–35), single-line italic footer with sources.
- Ranks 3–5 of 20261123: mellow-beacon-21-5983 (78.34%),
  hitorijitsumu (76.93%), crisp-ibis-37-9613 (76.27%).

**Common factors, determined by me from the images:**
1. **Contrast at the edges:** a dark navy header band and a red +
   navy footer — the page is "bookended" by strong color, paper in
   the middle. V1 had a thin navy masthead only; the footer was a
   thin strip. The winners make the header and footer carry weight.
2. **Every story in a visible frame:** every card has a 1px border
   and a light background, so the page reads as a grid of boxes, not
   flowing text. V1's grid stories had no border — just hairlines.
3. **A colored band on every card:** a region-colored stat band on
   top of each card (big number + short label) does three jobs at
   once — it colors the page, it makes each card scannable, and it
   carries a countable fact. This is the winners' single most
   consistent device (regian's "60 BANKS · 70 TANKERS", pandya's
   "22nd", "74 LASHES", "8 KILLED", "-3.3%").
4. **One color per region, used everywhere:** the same 8 region
   colors appear in the chips row, the card bands, the kickers, the
   map badges/dots and the legend. Color is the navigation system.
5. **Verification pills + date-check footer:** CONFIRMED / OFFICIAL /
   REPORTED / CLAIM pills on every card and a red DATE CHECK box in
   the footer — the judge can see sourcing at a glance.
6. **Fonts:** a heavy black serif for the masthead and headlines,
   a clean grotesque for labels/body, and a condensed sans for the
   stat bands (the winners' stat numbers look condensed/tall). Three
   fonts, three jobs — never mixed up.

### Design decisions in v2 (and why)
- **Header:** full-width dark navy band `#14264d` with gold kicker
  `#d8b45a` ("THE WORLD IN ONE DAY" / "TUESDAY 24 NOVEMBER 2026 ·
  32 STORIES · 6 CONTINENTS"), masthead "THE WORLD TODAY" in white
  Playfair 900 48px, gold bottom rule. Navy-on-gold-on-white is the
  winners' header recipe (gentle-meteor-30's navy band + gold kicker).
- **Red headline strip** below the header: the 3 lead headlines in
  red Playfair bold — same device as regian/pandya.
- **Region color system** (8 colors, used in chips, card bands,
  kickers, map badges/dots, legend): Middle East `#c96a1e` orange
  (6), Europe `#1f5fa8` blue (5), Africa `#c0392b` red (4),
  Asia `#1e8a4c` green (10), N. America `#6a4fa3` purple (3),
  S. America `#b03a7d` magenta (2), Oceania `#0e7d8c` teal (1),
  World & Space `#14264d` navy (1). Total 32.
- **Every story in a frame:** 1px `#d8cfb0` border, `#fffdf4`
  background, consistent padding — 3 lead cards + 10 feature cards
  (5×2 grid under "THE DAY IN 10 MORE") + 19 briefs in the ALSO
  list + 2 ALSO TODAY items. No story sits on bare paper anymore.
- **Stat band on every card:** region-colored band with a big
  Oswald number + short label ("10 OF 12", "4 TANKERS", "9–6",
  "11 HURT", "41.9%", "5.6", "SHELTER", "20 KILLED", "4-PARTY",
  "25 HELD", "16 SAVED", "6 KILLED", "4 ABOARD"). Oswald is a
  Google Font (SIL OFL 1.1), downloaded locally as
  `fonts/Oswald-600.woff2` (21,472 bytes) — the condensed sans the
  winners' stat numbers call for.
- **Verification pills:** OFFICIAL (green), CONFIRMED (blue),
  REPORTED (red), CLAIM (amber) — assigned honestly from each
  story's sourcing; DSO = Daily Summary Of, defined in the footer.
- **Footer:** red DATE CHECK box (`#a31621`, white text: "Every story
  here happened, or was first reported, on Tuesday 24 November 2026."
  + "HOW SURE" legend) above a dark navy sources strip (white text).
  The two contrasting footer bands mirror the header — the page is
  bookended, as in the winners.
- **Fonts (all Google Fonts, SIL OFL 1.1, local woff2):** Playfair
  Display (masthead/headlines), Libre Franklin (labels/body), Oswald
  (stat banners). Same typefaces as v1 plus Oswald for the bands.
- **Same 32 stories** (`news.md` unchanged) — the focus is purely
  design, so v1 and v2 are directly comparable.

### What changed from v1
| | v1 | v2 |
|---|---|---|
| Header | thin navy masthead line | full navy band, gold kicker, gold rule |
| Footer | thin strip | red DATE CHECK box + navy sources strip |
| Grid stories | hairline separators, no border | framed cards, 1px border, light bg |
| Stat band | none | region-colored band + Oswald number on every card |
| Region color | only on map dots | chips + bands + kickers + map + legend |
| Verification | date-check line only | pills on every card + legend in footer |
| Features | 4×4 grid, no title | "THE DAY IN 10 MORE", 5×2 grid |
| ALSO list | 4-column flowing text | 3-column numbered briefs, even |
| Fonts | Playfair + Libre Franklin | + Oswald (condensed, stat bands) |

### Fixes found in the first v2 render (one full iteration round)
1. **Lead bodies clipped mid-word** ("Huawei wi…", "Washington…")
   by the 2-line clamp → trimmed all three lead bodies to ~110
   characters so they fit 2 lines.
2. **ALSO list overflow — the real bug:** only 11 of 21 briefs were
   visible; the rest were hidden behind the footer. Measured: page
   content was 177px over 1024. Root cause: the two ALSO TODAY items
   carried a long description in the `.bs` span, which has
   `white-space:nowrap` — it squeezed the headline to zero width and
   blew each brief up to 109–134px tall, stretching the columns to
   ~360px. Fixed by making ALSO items one-line briefs with a short
   source token (details stay in `news.md`).
3. **Two briefs wrapped to 2 lines** (Malaysia, Australia) →
   shortened by dropping the location word the kicker already gives.
4. **Recovered ~55px of vertical space** (masthead 52→48px, tighter
   paddings/margins, briefs 9.8→9.3px) so the page fits with slack.
   After the fixes: all 21 briefs visible, max brief bottom exactly
   at the footer top (y=975), every section within 1024px.

## Verification (v2)
- PNG 1024×1024, 281,383 bytes (< 1 MiB). ✔
- `main.ts` run twice → identical SHA-256, matching entry.png. ✔
- Visual inspection at full size, 2× leads zoom and 2× map zoom:
  navy header + red footer contrast reads strongly; all 13 cards in
  neat frames with colored stat bands; lead bodies complete (no
  clipping); map is real world outlines with all 32 badges legible,
  no badge collisions; ALSO list 3 even columns, all 21 items
  visible; footer on two lines. ✔

---

# v3 — illustrations (25 Nov 2026, malam)

Hap graded v2 "udah rapi" but asked the right question: "kok gak ada
illustrasinya ya?" — and told me to look at how top 1 designs it and
study it from the data and visual sides. So before redesigning I
re-read the actual winner images (`/tmp/winners/`, regian + pandya)
specifically for their illustrations.

## What I learned from the winners' illustrations

**Data side:**
- regian (top 1, 84.07%): 35 stories, but only the top 13 (3 leads +
  10 features) are illustrated — the other 22 are text-only briefs.
  The map panel is titled "WHERE IT HAPPENED · SCENES 1–13" and its
  caption says "Pins 1–13 locate the illustrated lead & feature
  stories". Illustration is a scarce resource spent on the 13 most
  important stories, not spread over all 35.
- pandya (rank 2, 83.29%): same pattern — 3 leads + 8 features
  illustrated, 27 briefs text-only. Its footer states the rule:
  "pictures and map drawn in code, not photos".

**Visual side:**
- Every illustrated card has a **flat vector scene band on top of the
  card**: simple geometric shapes, 2–4 flat colours per scene
  (region colour + dark navy/black + white, on a light tint), no
  gradients, no photos. One strong motif per scene — a ship, a bank,
  a drone, a satellite, a bar chart, a trophy, a padlock, flags.
- The scene is **always paired with the stat band**: regian puts a
  red stat banner under the scene ("60 BANKS · 70 TANKERS"); pandya
  puts the big stat *inside* the scene ("7 SEA DRONES" over the night
  sea, "0 FLIGHTS" over the grounded planes). The scene makes the
  card a picture; the stat makes it countable.
- The scene never carries the headline or body — it is a visual
  label for the story, ~1/3 of the card height. Text below it is
  untouched.

## Design decisions in v3 (and why)
- **Scene + stat ribbon in one band (pandya's device):** the stat
  ribbon is overlaid at the bottom of the scene SVG, so the scene
  replaces the v2 stat band and each card grows only by the artwork
  height: +27px for the lead row, +18px per feature row (+63px
  total). Paid for by tightening: map SVG 141→126px, chips/seclab/
  brief paddings, map panel padding.
- **One motif per card, drawn in code** (inline SVG in
  `tools/gen_entry.py`, `SCENES` dict + `scene_svg()`; no photos, no
  AI images, no external assets):
  - 1 Huawei — microchip + scales of justice (verdict on a tech firm)
  - 2 Hormuz — tanker on waves + spiked sea mine + explosion star
  - 3 ICJ — courthouse facade with columns
  - 4 Riyadh — twisted tower + sun + skyline blocks
  - 8 Finland — ship on waves + orange life ring
  - 12 Colombia — supermarket storefront, striped magenta awning
  - 15 DR Congo — plane on a dashed flight path over mountains
  - 16 Vietnam — steaming hot-pot, chopsticks, small flame
  - 20 S. Korea — fighter jets + radar arcs
  - 22 USA — Pentagon building + flag
  - 24 Mexico — quadcopter drone over desert + cactus
  - 28 Ukraine — Ukraine + EU flags over a negotiation table
  - 30 Nepal — snow-capped mountains + red seismic zigzag
- **Scene background:** a light tint of the card's region colour
  (`TINTS` in the generator), so the scene is coloured by the same
  navigation system as the chips, bands, map badges and legend.
- **Map retitled** "WHERE IT HAPPENED — SCENES 1–13", like regian.
- **Everything else kept from v2** (navy header + gold kicker, red
  DATE CHECK footer, framed cards, region colours, three fonts) and
  the same 32 stories (`news.md` unchanged).

### What changed from v2
| | v2 | v3 |
|---|---|---|
| Top of each card | plain region-colored stat band | flat vector scene + stat ribbon inside it |
| Map title | "A MAP OF TUESDAY" | "SCENES 1–13" |
| Map height | 141px | 126px |
| Brief 18 (Indonesia) | wrapped to 2 lines | shortened to "Prabowo names two VP candidates" |

### Fixes found in the first v3 render (one full iteration round)
1. **ALSO list overflow again:** last brief row (13 Colombia, 25
   Haiti, ALSO TODAY leaked deaths) was hidden behind the red footer
   — measured 10px over. Cause: brief 18 wrapped to 2 lines (28px
   row) after the scenes pushed the page down. Fixed by shortening
   brief 18 to one line and shrinking the map SVG 134→126px.
   After the fix: all 21 briefs single-line, max brief bottom exactly
   at the footer top (y=975), same as v2.
2. **Riyadh tower too small/abstract** (read as a little hat) →
   enlarged and centred, with skyline blocks and sun.
3. **DR Congo plane too small** → enlarged fuselage/wings, dashed
   path re-routed under it.

## Verification (v3)
- PNG 1024×1024, 278,859 bytes (< 1 MiB). ✔
- `main.ts` run twice (two output dirs) → identical SHA-256
  `e46a5170e938a17a121ec11d6573425ed733a368b0cbef9e7ab45a0f62e73009`,
  matching entry.png. Deterministic. ✔
- Layout measurement (Playwright): head 79, strip 27, chips 28,
  leads 178, feats 292, map 173, also 158, foot 49; all 21 ALSO
  briefs visible, max brief bottom y=975 = footer top. ✔
- Visual inspection at full size, 2× leads zoom, 2× features zoom,
  2× map zoom: all 13 scenes legible and relevant (chip+scales,
  tanker+mine, courthouse, tower, ship+ring, storefront, plane,
  hot-pot, jets, Pentagon, drone, flags, mountains+seismic); stat
  ribbons readable inside every scene; no text clipped or
  overlapping; map is real world outlines with all 32 badges legible;
  ALSO list complete above the footer. ✔

## v4 — illustrations from free Lucide icons (25 Nov 2026, night)

Hap's feedback on v3: "Lumayan sih, cuman untuk illustrasinya bisa gak
pakai icon svg gratis diluar sana? Ingat ya yg free commercial." So the
hand-drawn v3 scenes were replaced with real icons from a free,
commercial-free library.

### Library choice — Lucide
- **Lucide** (https://lucide.dev,
  https://github.com/lucide-icons/lucide): 1,500+ icons, one consistent
  24×24 stroke style (stroke-width 2, round caps/joins). **License:
  ISC** — "Permission to use, copy, modify, and/or distribute this
  software for any purpose with or without fee" — free for commercial
  use, no attribution required. Verified from the official repo's
  LICENSE file (copied to `icons/LICENSE`). Chosen over the other
  candidates (Heroicons/Tabler/Phosphor are also MIT): Lucide had every
  icon needed in the same outline style (including `drone`, `soup`,
  `plane-takeoff`, `handshake`, `life-buoy`); the only miss was
  `building-2` (404) — covered by `building`. One set only, no mixing
  libraries.
- **Downloaded locally** into `icons/` (18 SVGs, 248–645 bytes each)
  and inlined at build time — no CDN hotlink, render stays deterministic
  with no network.
- **Recolouring:** Lucide icons are stroke-only (`fill="none"`,
  `stroke="currentColor"`); the generator wraps each icon's inner paths
  in a `<g>` with the card's palette (navy #14264d + region colour +
  ink), stroke-width 2.2, so the icons read as part of the design, not
  pasted clip-art.

### Icons per scene (13)
| # | Story | Icons |
|---|---|---|
| 1 | Huawei | cpu (navy) + scale (green) |
| 2 | Hormuz | ship (navy) + bomb (ink) |
| 3 | ICJ | landmark (navy) |
| 4 | Riyadh | building (navy) + sun (orange) |
| 8 | Finland | ship (navy) + life-buoy (blue) |
| 12 | Colombia | store (magenta) |
| 15 | DR Congo | mountain (navy) + plane (red) |
| 16 | Vietnam | soup (green) |
| 20 | S. Korea | plane-takeoff (navy) + radar (green) |
| 22 | USA | building (navy) + flag (purple) |
| 24 | Mexico | drone (purple) |
| 28 | Ukraine | flag (blue) + handshake (blue) |
| 30 | Nepal | mountain (navy) + activity (red) |

### What changed from v3
| | v3 | v4 |
|---|---|---|
| Scene artwork | hand-drawn geometric shapes (`SCENES` dict) | Lucide icons (`ICON_SCENES` + `icon_g()`, `icons/`) |
| Footer sources strip | "PICTURES AND MAP DRAWN IN CODE, NOT PHOTOS" | "ICONS: LUCIDE (ISC) • MAP DRAWN IN CODE, NOT PHOTOS" |
| Everything else | — | unchanged: v2/v3 design system, 32 stories, map, ALSO list |

### Fixes found in the first v4 render (one iteration round)
1. **Riyadh sun too small** (14px vs its 19px building partner) →
   enlarged to 16px and nudged up. Re-rendered; the sun now reads at
   feature size.
2. Everything else passed first time: all 13 icons legible and
   relevant at full size and 2× zoom (leads + both feature rows), no
   clipped text, ALSO list complete, footer on one line.

## Verification (v4)
- PNG 1024×1024, 277,280 bytes (< 1 MiB). ✔
- `main.ts` run twice (two output dirs) → identical SHA-256
  `2a82328ae8e62ea28f539b9b614f1058e97a4c48323235364f93277d8f5589ab`,
  matching entry.png. Deterministic. ✔
- Visual inspection at full size, 2× leads zoom, 2× features zooms:
  all 13 Lucide icons legible and relevant; stat ribbons readable
  inside every scene; map is real world outlines with all 32 badges
  legible; ALSO list complete above the footer. ✔

## Files
- `entry.png` — v5, the image for Hap to grade.
- `entry-v4.png` — v4 archive (SHA `2a82328ae8e62ea28f539b9b614f1058e97a4c48323235364f93277d8f5589ab`).
- `entry-v3.png` — v3 archive (SHA `e46a5170e938a17a121ec11d6573425ed733a368b0cbef9e7ab45a0f62e73009`).
- `entry-v2.png` — v2 archive (SHA `990278d8078bd26d07fac158a285b317deb8e3606c63865dfb12a7c2fb81d437`).
- `entry-v1.png` — v1 archive (for comparison).
- `render.html`, `render.mjs`, `main.ts`, `news.md`, `DESIGN.md`,
  `TESTS.md`, `LICENSE`, `README.md`
- `tools/gen_entry.py` — builds render.html from story data
  (now imports `scene_svg` from `tools/scenes_v5.py`)
- `tools/scenes_v5.py` — the 13 rich vector scenes (one function per
  scene + `cloud`/`bird`/`sun`/`waves` helpers)
- `tools/scene-hormuz-preview.html` / `.md` / `.png` — the approved
  Hormuz example scene (Hormuz lead art reused verbatim in v5)
- `tools/gen_map.py`, `tools/render_template.html` — inherited from 23 Nov
- `fonts/` — PlayfairDisplay-700.woff2, LibreFranklin-400.woff2,
  Oswald-600.woff2 (SIL OFL)
- `icons/` — 18 Lucide SVGs from v4, no longer used (kept, not deleted)
- `tools/gen_map.py`, `tools/render_template.html` — inherited from 23 Nov
- `fonts/` — PlayfairDisplay-700.woff2, LibreFranklin-400.woff2,
  Oswald-600.woff2 (SIL OFL)
- `icons/` — 18 Lucide SVGs from v4, no longer used (kept, not deleted)

## v5 — rich vector illustrations drawn in code (25 Nov 2026, night)

Hap graded v4 "lumayan" but pointed out the Lucide pictures are
only icons, not illustrations — and asked how I would draw the
illustrations myself and what skill that needs. He chose the
"rich vector (code)" route, approved one example scene (Hormuz),
then said to continue to all 13 scenes (v5).

**What changed v4 → v5:** the 13 Lucide-icon scenes are replaced by
full layered flat-vector scenes drawn in code, in the approved
Hormuz-example style: environment background + 2–4 layered elements
with scale contrast + one small detail + the stat ribbon inside the
scene. Lead 2 (Hormuz) is reused verbatim from the approved example;
the other 12 are new, one per card (see DESIGN.md for the layer list
of each). The generator moved to `tools/scenes_v5.py` (one function
per scene + `cloud`/`bird`/`sun`/`waves` helpers); `gen_entry.py`
only imports `scene_svg` through a thin wrapper, and the whole V4
Lucide block was removed. Footer now reads "PICTURES AND MAP DRAWN
IN CODE, NOT PHOTOS" (no more Lucide credit). Everything else is
unchanged: navy header, red DATE CHECK footer, box frames, region
colours, three fonts, "SCENES 1–13" map label, and the same 32
stories (`news.md` untouched).

**Similar scenes kept apart on purpose:** Hormuz vs Finland (warm
sky + navy tanker + deck tanks + bow explosion + mines vs cold pale
sky + grey container ship + gulls, no explosion/mine); Huawei vs
ICJ (green courtroom wall + big chip + tilted scales vs pale-blue
sky + grand courthouse + gavel); Korea vs Congo (angular fighter
jets + radar arcs vs civil plane + dashed flight path + mountains);
Nepal vs Congo (snow caps + house + red seismic zigzag vs green
valley + flight path).

**Fixes during the build:** (1) a SyntaxError from mixing implicit
string concatenation with `+` inside the scene `return (...)`
blocks — fixed by adding the missing `+` operators (script
/tmp/fix_concat.py) and noted in DESIGN.md; (2) chairs/flag poles
in the Ukraine scene are drawn before the table so their legs hide
behind it. No render-iteration fix was needed after the first v5
render: the first render already passed visual inspection.

## Verification (v5)
- PNG 1024×1024, 292,537 bytes (< 1 MiB). ✔
- `main.ts` run twice (two output dirs) → identical SHA-256
  `866d0d070baf213b15c58d622f1af28dd8c81469b7fc679b8319ac679a705733`,
  matching entry.png. Deterministic. ✔
- `python3 tools/gen_entry.py` → render.html 101,769 bytes; badge
  check: no badge pair < 15px apart. ✔
- Visual inspection at full size + 2× leads zoom + 2× features
  zooms: all 13 scenes legible and relevant; similar pairs read as
  different scenes (Hormuz vs Finland, Huawei vs ICJ, Korea vs
  Congo, Nepal vs Congo); stat ribbons readable inside every scene;
  no clipped or colliding text; map is real world outlines with all
  32 badges legible; ALSO list complete above the footer. ✔
