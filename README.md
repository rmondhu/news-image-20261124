# news-image-20261124 — "The World Today"

Entry for make.fun bounty `news-image-20261124` — sum up the world's news of
Tuesday 24 November 2026 in one image. Account: @rmondhu.

- Prize: $100 total, 50 paid places, $20 for 1st. No entry fee. Entries close
  2026-11-26 00:00 UTC (07:00 WIB, 26 Nov 2026).
- Image: `entry.png`, 1024×1024 PNG, 292,537 bytes (limit: ≤1 MiB, ≤1024×1024).
  A front page: navy header band, 3 lead stories, 10 feature stories, a world
  map with numbered locations ("SCENES 1–13"), 32 stories across 6 continents,
  plus 19 more briefs. Sources listed on the page: AP, Reuters, BBC, Daily
  Summary of World (DSO), The Global Eye, One Turn, Astrova News, Horizon.
- Design: each of the 13 top stories (3 lead + 10 feature) has a flat
  vector-scene illustration drawn in code (SVG, no photos, no AI images),
  paired with a stat band — the device the winning entries of earlier
  news-image editions use. See `DESIGN.md` and `REPORT.md` for the full
  v1–v5 progression (v5 was judged "Perfect" by Hap).
- Program: `main.ts` (Node 22, stdlib only) copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png` (or `/output/entry.png`) — the pattern the
  kit's own starter uses. No network, no randomness, no timestamps at run time,
  so two runs write byte-identical output (verified: same SHA-256 twice,
  `866d0d070baf213b15c58d622f1af28dd8c81469b7fc679b8319ac679a705733`).
- The image itself was drawn locally with Playwright + Chromium installed in
  home (`~/workspace/makefun/tools`, Chromium 140, `~/.cache/ms-playwright`).
  `render.html` is the generated source layout, built by `tools/gen_entry.py`
  from the story data plus `tools/scenes_v5.py` (the 13 vector scenes);
  `render.mjs` screenshots it at 1024×1024. Fonts are Google Fonts (Playfair
  Display, Libre Franklin, Oswald — SIL OFL 1.1) in `fonts/` as local woff2
  files; they are needed only to re-render, not to run `main.ts`.
- News research: see `news.md` (32 stories + alternates, with sources).
  All events happened, or were first reported, on Tuesday 24 November 2026.

## Local test
```
mkdir -p out1 out2
MAKEFUN_OUTPUT_DIR=out1 node main.ts
MAKEFUN_OUTPUT_DIR=out2 node main.ts
sha256sum out1/entry.png out2/entry.png   # identical
python3 -c "from PIL import Image; im=Image.open('out1/entry.png'); print(im.size, im.format)"
```

## Status
Repo created 25 Nov 2026 (WIB): https://github.com/rmondhu/news-image-20261124
Entry v5 approved by Hap as "Perfect". Submission to bounty
`news-image-20261124` in progress with Hap's explicit approval.
