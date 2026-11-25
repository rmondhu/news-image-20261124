# Test notes — news-image-20261124 v5 (practice, 25 Nov 2026)

## Render checks (v5, done)
- `python3 tools/gen_entry.py` → render.html 101,769 bytes; badge check:
  no badge pair < 15px apart. ✔
- `node render.mjs` → entry.png 292,537 bytes, PNG 1024×1024 RGB, < 1 MiB. ✔
- `main.ts` run twice (two output dirs) → identical SHA-256
  `866d0d070baf213b15c58d622f1af28dd8c81469b7fc679b8319ac679a705733`,
  matching entry.png. Deterministic. ✔
- Scenes: 13 rich vector scenes from tools/scenes_v5.py (code-drawn,
  no photos/AI/icons); Hormuz lead reused verbatim from the approved
  example. Render needs no network. ✔

## Visual inspection (v5, done, 25 Nov 2026)
- All 13 scenes legible and relevant at full size and 2× zoom
  (chip+tilted scales, tanker+mines+explosion, courthouse+gavel,
  dusk skyline+PIF tower, grey container ship, storefront+police
  tape, mountains+plane+dashed path, hot-pot+lantern, jets+radar,
  Pentagon+flag, desert+drone, flags+table, snowy peaks+seismic
  zigzag+house); stat ribbons readable inside every scene. ✔
- Similar pairs read as different scenes (Hormuz vs Finland, Huawei
  vs ICJ, Korea vs Congo, Nepal vs Congo). ✔
- Map is a recognisable real world map (Natural Earth outlines); all 32
  numbered badges legible; "SCENES 1–13" label. Footer: red DATE
  CHECK box + navy sources strip with "PICTURES AND MAP DRAWN IN
  CODE, NOT PHOTOS". ✔
- No render-iteration fix needed after the first v5 render. Build
  fixes: mixed implicit-concat/`+` SyntaxError fixed (see DESIGN.md);
  Ukraine chairs/flag poles drawn before the table. ✔
- ALSO list: 3 even columns, all 21 items visible. ✔

## Render checks (v4, done)
- `python3 tools/gen_entry.py` → render.html 89,000 bytes; badge check:
  no badge pair < 15px apart. ✔
- `node render.mjs` → entry.png 277,280 bytes, PNG 1024×1024 RGB, < 1 MiB. ✔
- `main.ts` run twice (two output dirs) → identical SHA-256
  `2a82328ae8e62ea28f539b9b614f1058e97a4c48323235364f93277d8f5589ab`,
  matching entry.png. Deterministic. ✔
- Icons: 18 local Lucide SVGs in icons/ + icons/LICENSE (ISC) — render
  needs no network. ✔

## Visual inspection (v4, done, 25 Nov 2026)
- All 13 Lucide icons legible and relevant at full size and 2× zoom
  (cpu+scale, ship+bomb, landmark, building+sun, ship+life-buoy,
  store, mountain+plane, soup, plane-takeoff+radar, building+flag,
  drone, flag+handshake, mountain+activity); stat ribbons readable
  inside every scene. ✔
- Map is a recognisable real world map (Natural Earth outlines); all 32
  numbered badges legible; "SCENES 1–13" label. Footer: red DATE
  CHECK box + navy sources strip with "ICONS: LUCIDE (ISC)". ✔
- Fix applied after first v4 render: Riyadh sun enlarged 14→16px. ✔
- ALSO list: 3 even columns, all 21 items visible. ✔

## Render checks (v3, done)
- `python3 tools/gen_entry.py` → render.html 87,883 bytes; badge check:
  no badge pair < 15px apart. ✔
- `node render.mjs` → entry.png 278,859 bytes, PNG 1024×1024 RGB, < 1 MiB. ✔
- `main.ts` run twice (two output dirs) → identical SHA-256
  `e46a5170e938a17a121ec11d6573425ed733a368b0cbef9e7ab45a0f62e73009`,
  matching entry.png. Deterministic. ✔
- Fonts: PlayfairDisplay-700.woff2 + LibreFranklin-400.woff2 +
  Oswald-600.woff2 (all SIL OFL, local) — render needs no network. ✔
- Layout measurement (Playwright, all sections in-bounds): head 79,
  strip 27, chips 28, leads 178, feats 292, map 173, also 158, foot 49;
  all 21 ALSO briefs visible, max brief bottom y=975 = footer top. ✔

## Visual inspection (v3, done, 25 Nov 2026)
- All 13 flat vector scenes legible and relevant at full size and 2×
  zoom (chip+scales, tanker+mine, courthouse, tower, ship+ring,
  storefront, plane, hot-pot, jets, Pentagon, drone, flags,
  mountains+seismic); stat ribbons readable inside every scene. ✔
- Map is a recognisable real world map (Natural Earth outlines); all 32
  numbered badges legible, leader lines clear; "SCENES 1–13" label. ✔
- Fixes applied after first v3 render: ALSO overflow (last brief row
  hidden behind footer) fixed by shortening brief 18 to one line and
  shrinking map SVG 134→126px; Riyadh tower enlarged/centred; DR Congo
  plane enlarged. ✔
- ALSO list: 3 even columns, all 21 items visible. Footer: red DATE
  CHECK box + navy sources strip. ✔

## Render checks (v2, done)
- `python3 tools/gen_entry.py` → render.html 75,330 bytes; badge check:
  no badge pair < 15px apart. ✔
- `node render.mjs` → entry.png 281,383 bytes, PNG 1024×1024 RGB, < 1 MiB. ✔
- `main.ts` run twice (two output dirs) → identical SHA-256
  `990278d8078bd26d07fac158a285b317deb8e3606c63865dfb12a7c2fb81d437`,
  matching entry.png. Deterministic. ✔
- Fonts: PlayfairDisplay-700.woff2 + LibreFranklin-400.woff2 +
  Oswald-600.woff2 (all SIL OFL, local) — render needs no network. ✔
- Layout measurement (Playwright, all sections in-bounds): head 79,
  strip 27, chips 30, leads 153, feats 258, map 190, also 196, foot 49;
  all 21 ALSO briefs visible, max brief bottom y=975 = footer top. ✔

## Visual inspection (v2, done, 25 Nov 2026)
- Navy header band + gold kicker + white masthead; red headline strip;
  region chips row; all 13 cards in neat 1px frames with region-colored
  stat bands; verification pills on every card. ✔
- Map is a recognisable real world map (Natural Earth outlines); all 32
  numbered badges legible, leader lines clear. ✔
- Fixes applied after first v2 render: 3 lead bodies trimmed so none
  clips mid-word; ALSO TODAY items made one-line (long nowrap source
  had blown the columns to ~360px and hidden 10 briefs behind the
  footer); briefs 17 & 31 shortened to one line; ~55px of vertical
  space recovered (masthead 52→48px, tighter paddings, briefs 9.3px). ✔
- ALSO list: 3 even columns, all 21 items visible. Footer: red DATE
  CHECK box + navy sources strip. ✔

## v1 checks (kept for the record)
- `python3 tools/gen_entry.py` → render.html 67,175 bytes; badge check:
  no badge pair < 15px apart. ✔
- `node render.mjs` → entry-v1.png 286,617 bytes, PNG 1024×1024 RGB. ✔
- `main.ts` run twice → identical SHA-256
  `995ba009bcaa345cc958321ff381e3ac392845c536dfb7ba6160e855d555b73b`. ✔
- Fixes applied after first v1 render: badge 15 (DR Congo) moved
  538,114 → 530,116 so its leader line no longer crosses the "AFRICA"
  label; story 22 headline reworded ("…over defence and F-35s" →
  "…over defence spending") to avoid the "F- / 35s" line break. ✔
- Grid: 4 columns end at the same height; no overflow, no clipped text;
  every headline ≤ 2 lines, every body ≤ 2 lines. ✔
- Footer sources + date on one line. ✔

## Not done (practice only — by design)
- No GitHub repo created, nothing pushed, nothing submitted to make.fun.
- No transcript bundle built (would be needed only for a real submission).
