# Contoh ilustrasi vektor kaya — Selat Hormuz (lead 2)

**File preview:** `tools/scene-hormuz-preview.png` (1680×1219, render 2× dari halaman 840px)
**Sumber:** `tools/scene-hormuz-preview.html` · render: `tools/render-preview.mjs`
**Status:** CONTOH untuk dinilai Hap. `entry.png`, `news.md`, dan `tools/gen_entry.py`
TIDAK disentuh (entry.png masih v4, SHA `2a82328a…`).

## Apa yang dipelajari dari pemenang (gambar regian + pandya dibaca ulang)

Diunduh ulang dari API make.fun ke `/tmp/winners/` (leaderboard
`news-image-20261123`, artifact webp → PNG) dan dibaca + di-zoom 2×.
Kekayaan adegan pemenang bukan dari detail realistis, melainkan dari:

- **Latar lingkungan yang utuh** — langit/malam + laut + cakrawala, bukan latar
  polos. Pandya lead 1: langit malam navy + bulan + laut dua warna + kapal
  perang siluet + ledakan oranye. Regian lead 3: langit pucat + drone +
  garis terbang putus-putus + menara kilang + asap + ledakan starburst.
- **2–4 elemen berlapis dengan skala kontras** — satu motif besar di depan,
  satu-dua motif kecil di kejauhan (kedalaman), plus satu detail kecil
  (bulan, awan, asap, buih, burung).
- **Stat banner menempel di dalam adegan** (pandya: angka besar di atas
  adegan; regian: banner merah di bawah adegan), bukan pita terpisah.
- **Palet datar 2–4 warna per adegan**, tanpa gradien, tanpa foto.

## Apa yang membuat adegan ini "kaya" dibanding v3 dan v4

- **v3 (bentuk tangan):** 1–2 bentuk di atas latar polos — kapal + ranjau saja,
  tanpa langit, tanpa laut, tanpa kedalaman. Terasa seperti diagram.
- **v4 (ikon Lucide):** 1–2 ikon garis di atas tint polos — rapi dan konsisten,
  tapi tetap satu simbol, bukan adegan.
- **Contoh ini:** satu adegan utuh dengan 6 lapisan — ada langit, ada laut
  dua tingkat, ada kapal kecil di kejauhan, ada kapal besar di tengah, ada
  ledakan yang menceritakan kejadiannya, ada ranjau di depan sebagai motif
  terdekat. Pembaca "membaca" cerita (tanker kena ranjau di selat), bukan
  sekadar mengenali satu simbol.

## Lapisan adegan (belakang → depan)

1. **Langit** — latar hangat `#fbeed3`, matahari emas `#d8b45a`, 3 awan putih,
   2 burung.
2. **Laut jauh + kapal escort kecil** — laut `#7fa8b8`, siluet kapal navy
   kecil di cakrawala (kedalaman) + garis buih.
3. **Ombak + laut depan** — dua garis ombak putih, laut depan `#2a6f97`
   (lebih gelap), buih putih.
4. **Tanker besar** — lambung navy `#14264d` + garis merah `#a31621`,
   3 tangki dek putih di garis dek (ada garis jahit silinder), anjungan putih
   + 3 jendela, cerobong oranye + asap abu-abu, tiang haluan + bendera oranye,
   buih haluan/buritan.
5. **Ledakan di haluan** — starburst 8 titik oranye `#e8a020` bertepi merah,
   + 2 percikan. Menandai "kena ranjau".
6. **Ranjau di depan** — bola berduri hitam `#141414` + antena ujung merah
   (paling dekat dengan pembaca), percikan putih, + ranjau kedua yang lebih
   kecil di tepi kanan (kedalaman).
7. **Pita stat** — oranye Timur Tengah `#c96a1e`, "4 TANKERS" / "HIT BY MINES"
   (Oswald, seperti v4).

## Palet

Oranye region `#c96a1e` · navy `#14264d` · laut `#7fa8b8` / `#2a6f97` ·
langit hangat `#fbeed3` · matahari emas `#d8b45a` · merah aksen `#a31621` ·
tinta `#141414`. Tanpa gradien, tanpa foto, tanpa ikon library.

## Geometri

Sama dengan scene lead v4 supaya bisa langsung dipakai: viewBox `0 0 320 56`,
artwork y 0–33, pita stat y 33–56. Preview menampilkan adegan yang sama dalam
dua ukuran: besar 760px dan mock kartu lead ukuran asli (~321px, markup kartu
persis v4: badge 2, kicker HORMUZ — LEAD, pill REPORTED, headline, body,
sumber IRGC · JMIC).

## Perbaikan dari putaran verifikasi

Render pertama: tangki dek terlihat "melayang" di atas lambung; cerobong
hampir tak terlihat; ujung antena ranjau (titik merah) melayang jauh di langit;
kapal escort bertabrakan dengan awan. Diperbaiki: garis dek navy di bawah
tangki + garis jahit silinder, cerobong diperbesar (oranye + pita navy + asap
lebih besar), antena dipendekkan (titik merah menempel di ujung duri),
kapal escort digeser ke kiri dan awan dipindah. Render kedua diverifikasi:
adegan terbaca sebagai "selat + tanker + ranjau" di ukuran besar maupun
ukuran kartu.
