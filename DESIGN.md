# Design system — THE WORLD TODAY, 24 November 2026 (v1)

Evolved from the 23 Nov entry (approved by Hap). Same tokens, same 8px
rhythm, same layout. Changes in v1: Google Fonts (Playfair Display +
Libre Franklin, SIL OFL) replace Liberation as the primary typefaces;
map dots/badges unified from inline #b91c1c to the accent token #a31621.

## Palet (kontras dihitung terhadap kertas #f7f1de)
| Token | Nilai | Pakai untuk | Kontras vs kertas |
|---|---|---|---|
| `--paper` | #f7f1de | latar halaman | — |
| `--ink` | #141414 | judul, angka, garis pemisah | ~15.5 : 1 |
| `--body` | #262626 | teks isi | ~13 : 1 |
| `--muted` | #5c5540 | label benua di peta | ~5.5 : 1 |
| `--accent` | #a31621 | kicker, angka penting, dot peta | ~7 : 1 |
| `--land` | #c9bd93 | daratan peta | — |
| `--mapbg` | #ece5cb | laut peta | — |
| `--hairline` | #cfc7a4 | pemisah kolom & antar-cerita | — |

Aturan: aksen merah **hanya** untuk label/angka/dot, tidak pernah untuk
teks isi. Teks kecil (8–9px) selalu `--body`/`--accent` di atas kertas
terang, tidak pernah abu-abu pudar.

## Skala tipografi (serif = headline, sans = label/isi)
| Level | Elemen | Ukuran / line-height / weight |
|---|---|---|
| 1 | Masthead `THE WORLD TODAY` | 50px / 1.0 / 900 serif |
| 1b | Dateline | 11px / 1.4 / 700 sans, letterspacing 3px |
| 2 | Kicker lead | 9.5px / — / 700 sans, letterspacing 2px |
| 2 | Headline lead | 16.5px / 1.16 / 700 serif |
| 2 | Body lead | 10.5px / 1.35 sans |
| 3 | Judul peta | 10.5px / — / 700 sans, letterspacing 3px |
| 3 | Label benua | 9px sans, letterspacing 1.5px |
| 4 | Kicker cerita | 8px / — / 700 sans, letterspacing 1.5px |
| 4 | Headline cerita | 10.5px / 1.20 / 700 serif, maks. 2 baris |
| 4 | Body cerita | 8.8px / 1.28 sans, maks. 2 baris |
| 5 | Footer | 9px / 1.4 sans, letterspacing 1px |

- Serif: "Playfair Display" (variable font, wght 700–900), fallback
  Liberation Serif, DejaVu Serif.
- Sans: "Libre Franklin" (variable font, wght 400–700), fallback
  Liberation Sans, DejaVu Sans.
- Keduanya Google Fonts di bawah SIL Open Font License 1.1 (gratis untuk
  penggunaan komersial), diunduh sebagai woff2 lokal ke `fonts/` — tidak
  ada network saat render. File: `PlayfairDisplay-700.woff2` (variable
  700–900), `LibreFranklin-400.woff2` (variable 400–700). Di-load lewat
  `@font-face` dengan `font-weight: 700 900` / `400 700`.
- Headline dan body di-clamp 2 baris (`-webkit-line-clamp`) supaya tidak
  ada teks yang terpotong di tepi halaman.

## Jarak (spacing)
- Padding halaman: 10px atas, 8px bawah, 20px kiri/kanan.
- Gutter antar kolom: 16px; garis pemisah kolom 1px `--hairline`.
- Cerita: margin-bawah 4px + padding-bawah 4px + hairline 1px di bawahnya
  (kecuali cerita terakhir tiap kolom). "Also today" diberi latar
  #efe8cc dan padding 5px 7px supaya terpisah dari grid biasa.
- Lead: padding 8px vertikal; peta: padding 7px atas, 8px bawah.
- Hirarki pemisah: masthead 4px double, lead & peta 2px solid, footer 3px solid.

## Hirarki visual
Masthead (terbesar, tengah) → lead 3 kolom (headline terbesar kedua) →
peta (satu-satunya elemen visual besar) → grid 4 kolom (cerita bernomor,
makin ke bawah makin kecil) → footer. Mata diarahkan dari atas ke bawah
tanpa ada elemen yang bersaing dengan masthead.

## Peta — kenapa terlihat seperti peta dunia
- **Bukan digambar tangan.** Outline berasal dari data negara nyata
  (Natural Earth, 180 negara) yang diproyeksikan equirectangular dan
  disederhanakan (Douglas–Peucker 0.45°) oleh `tools/gen_map.py` pada
  edisi 23 Nov. `render.html` meng-embed 251 path hasilnya verbatim —
  program entry tidak butuh network saat run.
- Proyeksi: lon −180…180 → x 0…984; lat 75…−52 → y 0…144
  (vertikal sedikit dipadatkan agar muat di strip; bentuk benua tetap benar).
- Garis lintang putus-putus (khatulistiwa & garis balik) membantu mata
  membaca peta sebagai peta, bukan gumpalan.
- Dot bernomor diletakkan di lat/lon asli tiap cerita. Karena ~15 cerita
  menumpuk di Eropa/Timur Tengah, dot yang berdekatan digeser dengan
  **leader line** (garis tipis merah dari titik asli ke badge bernomor)
  dan badge diberi outline putih agar tetap terpisah satu sama lain.
  Posisi badge dicek otomatis oleh generator (tiap pasangan ≥ 15px).
  Keterbatasan jujur: di skala 984px, klaster Eropa/Timur Tengah tetap
  padat — semua nomor masih terbaca, tapi wilayah itu terlihat ramai.
  Itu harga dari 15 cerita di wilayah sekecil itu, bukan kesalahan bentuk benua.
- Label benua diletakkan di laut/daratan kosong (N. AMERICA, S. AMERICA,
  EUROPE di Atlantik, AFRICA, ASIA, AUSTRALIA) agar tidak tertutup dot.

## Yang berubah dari edisi 23 Nov
- Font utama: Liberation Serif/Sans → Playfair Display / Libre Franklin
  (Google Fonts, SIL OFL). Masthead kini Playfair Black 900 — lebih
  berkarakter koran klasik.
- Dot/badge peta: inline #b91c1c → token aksen #a31621 (satu merah saja).
- `render.html` kini di-generate oleh `tools/gen_entry.py` (data cerita +
  posisi badge hidup di sana; poligon daratan disalin verbatim dari file
  23 Nov). Tanggal/judul diperbarui ke Selasa 24 November 2026.
- Isi berita baru: 32 cerita 24 Nov (lihat `news.md`).

---

# v2 — desain ulang dari visual pemenang (25 Nov 2026, malam)

Setelah Hap menilai v1 "lumayan" dan mendeskripsikan entry pemenang,
tiga gambar pemenang asli dibaca secara visual (regian 84.07%,
pandya 83.29%, gentle-meteor-30 85.9%) dan faktor-faktor di bawah ini
ditentukan sendiri dari gambarnya, bukan dari teori.

## Palet v2 — warna kontras di tepi, kertas di tengah
| Token | Nilai | Pakai untuk | Kontras vs kertas |
|---|---|---|---|
| `--navy` | #14264d | header band, footer strip, World & Space | — |
| `--gold` | #d8b45a | kicker header, garis bawah masthead | — |
| `--accent` | #a31621 | strip headline merah, DATE CHECK box, pil REPORTED | ~7 : 1 |
| `--card` | #fffdf4 | latar kartu | — |
| `--frame` | #d8cfb0 | border kartu & panel peta | — |
| `--paper` / `--ink` / `--body` | #f7f1de / #141414 / #262626 | (tetap dari v1) | — |

**Sistem warna per region (dipakai di chips, stat band, kicker, badge
peta, dot peta, legenda):**
| Region | Warna | Cerita |
|---|---|---|
| Middle East | #c96a1e oranye | 6 |
| Europe | #1f5fa8 biru | 5 |
| Africa | #c0392b merah | 4 |
| Asia | #1e8a4c hijau | 10 |
| N. America | #6a4fa3 ungu | 3 |
| S. America | #b03a7d magenta | 2 |
| Oceania | #0e7d8c teal | 1 |
| World & Space | #14264d navy | 1 |

Alasan: warna adalah sistem navigasi halaman — pembaca melihat warna
dan tahu regionnya tanpa membaca label. Satu warna per region, dipakai
di semua tempat yang sama, supaya tidak ada warna "sekali pakai".

## Tipografi v2 — tiga font, tiga tugas
| Font | Tugas | Ukuran |
|---|---|---|
| Playfair Display 900 | masthead (48px), headline lead 15.5px, headline kartu | serif hitam klasik |
| Libre Franklin | label, body, kicker, footer | grotesque bersih |
| **Oswald 600** (baru) | **angka & label di stat band** | 21px lead / 15px feature, condensed |

Oswald (Google Fonts, SIL OFL 1.1) diunduh lokal sebagai
`fonts/Oswald-600.woff2` (21,472 bytes). Alasan: angka stat band
pemenang terlihat condensed/tinggi — Oswald memberi kesan itu tanpa
harus men-stretch font lain.

## Frame & layout v2 — alasan di tiap keputusan
- **Header band navy penuh + kicker emas + garis emas:** halaman
  "dibingkai" warna kuat di atas (pemenang: gentle-meteor-30).
  Masthead 52→48px supaya band tidak terlalu tinggi.
- **Footer dua band kontras:** kotak DATE CHECK merah `#a31621`
  (teks putih) di atas strip sumber navy (teks putih) — cerminan
  header; halaman terasa selesai, bukan terpotong (pemenang:
  regian/pandya).
- **Tiap cerita dalam frame kotak:** border 1px `--frame`, latar
  `--card`, padding konsisten — 3 lead + 10 feature + 19 brief +
  2 ALSO TODAY. Tidak ada lagi cerita di atas kertas polos.
- **Stat band berwarna di tiap kartu:** band region-colored dengan
  angka besar Oswald + label pendek ("10 OF 12", "4 TANKERS",
  "41.9%") — satu elemen yang sekaligus mewarnai halaman, membuat
  kartu scannable, dan membawa satu fakta yang bisa dihitung
  (pemenang: regian "60 BANKS · 70 TANKERS", pandya "74 LASHES").
- **Pil verifikasi di tiap kartu:** OFFICIAL hijau `#1e7a46`,
  CONFIRMED biru `#1f5fa8`, REPORTED merah `#a31621`, CLAIM amber
  `#b7791f` — ditetapkan jujur dari sumber tiap cerita; DSO =
  Daily Summary Of, didefinisikan di footer.
- **Grid feature 5×2** di bawah label "THE DAY IN 10 MORE" (bukan
  4×4 tanpa judul) — mengikuti regian ("10 feature cards") dan
  pandya ("THE DAY IN 8 MORE").
- **ALSO list 3 kolom bernomor** (bukan 4 kolom mengalir) — mengikuti
  pandya; tiap baris satu baris teks, sumber singkat di kanan.
- **Isi berita tetap 32 cerita yang sama** (`news.md` tidak berubah)
  supaya v1 dan v2 bisa dibandingkan murni dari desain.

## Pelajaran dari bug v2 (dicatat supaya tidak terulang)
- `.bs` (sumber brief) memakai `white-space:nowrap` — sumber yang
  panjang akan menekan headline ke lebar nol dan meledakkan tinggi
  kolom (brief 109–134px, 10 brief tersembunyi di balik footer).
  **Aturan: sumber di brief harus satu token pendek.**
- `.also` memakai `flex:1` dan konten `.briefs` tidak bisa menyusut
  di bawah tinggi kontennya — kalau halaman kepenuhan, brief-lah
  yang meluber ke balik footer, bukan footer yang turun. Selalu ukur
  tinggi tiap seksi dengan Playwright sebelum menyerahkan (skrip
  `/tmp/measure2.mjs`), bukan hanya melihat gambar.
- Lead body harus ≤ ~110 karakter agar muat 2 baris tanpa terpotong
  di tengah kata.

---

# v3 — ilustrasi (25 Nov 2026, malam)

Hap menilai v2 "udah rapi" tapi menanyakan ilustrasinya dan menyuruh
mempelajari desain top 1 dari segi data dan visual. Gambar pemenang
dibaca ulang khusus untuk ilustrasinya.

## Pelajaran dari ilustrasi pemenang
- **Data:** hanya 13 cerita teratas yang berilustrasi (3 lead + 10
  feature); sisanya brief teks saja. regian memberi label peta
  "SCENES 1–13". Ilustrasi adalah sumber daya langka yang dipakai
  untuk 13 cerita terpenting, bukan disebar ke semua cerita.
- **Visual:** tiap kartu berilustrasi punya pita adegan vektor datar
  di atas kartu — bentuk geometris sederhana, 2–4 warna datar per
  adegan (warna region + navy/hitam + putih, latar tint terang),
  tanpa gradien, tanpa foto. Satu motif kuat per adegan (kapal, bank,
  drone, satelit, grafik, trofi, gembok, bendera). Adegan selalu
  dipasangkan dengan stat band: regian menaruh banner stat merah di
  bawah adegan, pandya menaruh angka besar *di dalam* adegan.
  Footer pandya: "pictures and map drawn in code, not photos".

## Sistem ilustrasi v3
- **Pita adegan + stat ribbon menyatu (cara pandya):** ribbon stat
  di-overlay di bawah adegan SVG, jadi adegan menggantikan stat band
  v2 dan kartu hanya tumbuh setinggi artwork: +27px baris lead,
  +18px per baris feature (+63px total). Dibayar dengan mengetatkan:
  peta 141→126px, padding chips/seclab/brief, padding panel peta.
- **Satu motif per kartu, digambar pakai kode** (SVG inline di
  `tools/gen_entry.py`, dict `SCENES` + fungsi `scene_svg()`; tanpa
  foto, tanpa gambar AI, tanpa aset luar): chip + timbangan (Huawei),
  tanker + ranjau (Hormuz), gedung pengadilan (ICJ), menara + matahari
  (Riyadh), kapal + pelampung (Finland), etalase + awning garis
  (Colombia), pesawat + garis putus-putus + gunung (DR Congo),
  hot-pot + sumpit + uap (Vietnam), jet + busur radar (S. Korea),
  Pentagon + bendera (USA), drone + kaktus (Mexico), bendera Ukraina
  + EU + meja (Ukraine), gunung bersalju + zigzag seismik (Nepal).
- **Latar adegan:** tint terang dari warna region kartu (`TINTS`) —
  adegan diwarnai sistem navigasi yang sama dengan chips, band, badge
  peta, dan legenda.
- **Ukuran adegan:** lead viewBox 320×56 (artwork y 0–33, ribbon
  23px), feature 190×40 (artwork y 0–23, ribbon 17px). Teks stat
  di dalam SVG memakai Oswald (font sudah di-load halaman).
- **Judul peta** jadi "WHERE IT HAPPENED — SCENES 1–13" seperti regian.
- **Yang lain tetap dari v2** (header navy, footer DATE CHECK merah,
  frame kotak, warna region, tiga font) dan 32 cerita sama.

## Pelajaran dari bug v3 (dicatat supaya tidak terulang)
- Menambah adegan menggeser halaman ke bawah: brief 18 membungkus
  2 baris dan baris brief terakhir tersembunyi di balik footer
  (10px). Perbaiki dengan memendekkan brief yang membungkus dan
  mengecilkan peta — jangan menambah tinggi halaman tanpa mengukur
  ulang.
- Adegan kecil harus satu motif besar dan sederhana; menara Riyadh
  yang kecil dan abstrak tidak terbaca — diperbesar dan dipusatkan.
  Pesawat DR Congo yang kecil juga diperbesar.

---

# v4 — ilustrasi dari ikon SVG gratis (25 Nov 2026, malam)

Hap menilai v3 "lumayan" tapi meminta ilustrasi memakai ikon SVG
gratis dari luar, yang lisensinya bebas komersial. Adegan gambar-tangan
v3 diganti dengan ikon dari satu library.

## Library — Lucide (ISC)
- **Lucide** (https://lucide.dev,
  https://github.com/lucide-icons/lucide): 1.500+ ikon, satu gaya
  konsisten — outline 24×24, stroke-width 2, round caps/joins.
  **Lisensi ISC**: boleh dipakai, disalin, dimodifikasi, dan
  didistribusikan untuk tujuan apa pun, dengan atau tanpa biaya —
  bebas komersial, atribusi tidak wajib. Diverifikasi dari file
  LICENSE resmi repo (disalin ke `icons/LICENSE`). Dipilih atas
  Heroicons/Tabler/Phosphor (sama-sama MIT): Lucide punya semua ikon
  yang dibutuhkan dalam gaya outline yang sama (termasuk `drone`,
  `soup`, `plane-takeoff`, `handshake`, `life-buoy`); satu-satunya
  yang tidak ada adalah `building-2` (404) — diganti `building`.
  Satu set saja, tidak campur library.
- **Diunduh lokal** ke `icons/` (18 file SVG, masing-masing 248–645
  byte) dan di-inline saat build — tanpa hotlink CDN, render tetap
  deterministik tanpa network.
- **Pewarnaan ulang:** ikon Lucide hanya stroke (`fill="none"`,
  `stroke="currentColor"`); generator membungkus path dalam `<g>`
  dengan warna palet kartu (navy + warna region + tinta),
  stroke-width 2.2 — ikon jadi bagian desain, bukan clip-art tempelan.

## Sistem ilustrasi v4
- **Satu motif per kartu, 1–2 ikon** (dict `ICON_SCENES` + fungsi
  `icon_g()` di `tools/gen_entry.py`; fungsi `_icon_inner()`
  mengambil isi SVG lokal). Penempatan per adegan ditentukan manual
  dalam koordinat viewBox scene (lead 320×56, feature 190×40):
  ikon lead ~29px, ikon feature ~19–21px, stroke-width 2.2
  (efektif ~2.7 lead / ~1.8 feature setelah skala).
- **Daftar ikon per kartu:** cpu + scale (Huawei), ship + bomb
  (Hormuz), landmark (ICJ), building + sun (Riyadh), ship + life-buoy
  (Finland), store (Colombia), mountain + plane (DR Congo), soup
  (Vietnam), plane-takeoff + radar (S. Korea), building + flag (USA),
  drone (Mexico), flag + handshake (Ukraine), mountain + activity
  (Nepal).
- **Footer:** strip sumber kini menulis "ICONS: LUCIDE (ISC) • MAP
  DRAWN IN CODE, NOT PHOTOS" — atribusi sukarela di gambar, lisensi
  lengkap di `icons/LICENSE`.
- **Yang lain tetap dari v3** (header navy, footer DATE CHECK merah,
  frame kotak, warna region, tiga font, stat ribbon di dalam adegan,
  label peta "SCENES 1–13") dan 32 cerita sama.

## Pelajaran dari bug v4 (dicatat supaya tidak terulang)
- Ikon pendamping yang jauh lebih kecil dari ikon utama terlihat
  seperti noda (sun 14px vs building 19px) — samakan skala ikon
  dalam satu adegan (sun dibesarkan ke 16px).
- Ikon stroke di ukuran kecil butuh stroke-width sedikit lebih tebal
  (2.2, bukan 2.0) supaya tetap terbaca setelah di-scale ke bawah.

## Sistem ilustrasi v5 — adegan kaya, digambar pakai kode
- **Kenapa v5:** Hap menilai ikon v4 "cuman icon aja, bukan illustrasi".
  v5 kembali ke cara pemenang (adegan digambar pakai kode, "drawn in
  code, not photos") tapi dengan kekayaan adegan contoh Hormuz yang
  sudah disetujui Hap (tools/scene-hormuz-preview.html): tiap adegan
  adalah satu adegan utuh berlapis, bukan satu simbol.
- **Resep per adegan** (gaya contoh Hormuz): latar lingkungan utuh
  (langit/laut/dinding) + 2–4 elemen berlapis dengan skala kontras
  (motif besar di depan, motif kecil di kejauhan) + satu detail kecil
  (matahari, awan, burung, asap, buih, percikan) + stat ribbon di
  dalam adegan. Palet datar 2–4 warna per adegan (warna region +
  navy + putih + satu warna suasana), tanpa gradien.
- **Implementasi:** `tools/scenes_v5.py` — satu fungsi per adegan
  (`art_huawei`, `art_hormuz`, …) + helper `cloud()`, `bird()`,
  `sun()`, `waves()` + `scene_svg(n, reg, stat, label, lead, regions,
  tints)`. `tools/gen_entry.py` hanya mengimpor `scene_svg` lewat
  wrapper tipis (blok V4/Lucide dihapus). Adegan Hormuz dipakai ulang
  verbatim dari contoh yang disetujui.
- **Daftar adegan per kartu (lapisan belakang → depan):**
  - 1 Huawei (sidang teknologi): dinding hijau pucat + lantai →
    chip navy besar + pin → berkas sidang → timbangan keadilan,
    balok miring (sisi bersalah lebih rendah) + kilau emas.
  - 2 Hormuz: persis contoh (langit hangat + matahari/awan/burung →
    laut jauh + kapal escort → ombak → laut depan → tanker besar →
    ledakan di haluan → ranjau berduri di depan).
  - 3 ICJ (gedung pengadilan): langit biru pucat + matahari/awan →
    bendera kecil → gedung pengadilan (pedimen navy + 4 kolom +
    pintu) + tangga → palu sidang + alas di depan kanan.
  - 4 Riyadh: langit senja oranye + matahari + burung + bintang →
    siluet skyline navy → menara PIF meruncing + mahkota emas +
    jendela menyala.
  - 8 Finland: langit dingin pucat + matahari pucat + camar → laut
    dua tingkat + ombak → kapal kargo abu-abu + 3 kontainer warna +
    anjungan + tiang → buih haluan/buritan.
  - 12 Colombia: langit hangat + matahari + awan → gedung samping
    → etalase putih + awning garis magenta/putih + pintu + jendela
    + papan nama → pita polisi kuning di depan pintu.
  - 15 DR Congo: langit + matahari + awan → dua pegunungan (tudung
    salju) → garis terbang putus-putus → pesawat → lembah hijau.
  - 16 Vietnam: dinding hangat + lampion merah → meja kayu → panci
    beruap + tutup → mangkuk + sumpit → tanaman kecil.
  - 20 S. Korea: langit + matahari + awan → dua jet tempur + jejak
    asap → busur radar hijau di kiri bawah.
  - 22 USA: langit + matahari + awan → gedung Pentagon (jendela +
    pintu) → bendera AS (garis + kanton) → halaman + dua pohon.
  - 24 Mexico: langit + matahari besar → mesa → gurun → kaktus →
    drone quadcopter + baling-baling → batu.
  - 28 Ukraine: dinding + jendela terang → bendera Ukraina +
    bendera EU (bintang emas) → kursi → meja + dokumen (kursi dan
    tiang bendera digambar SEBELUM meja supaya kakinya tersembunyi).
  - 30 Nepal: langit + matahari + burung → dua gunung bersalju →
    garis seismik zigzag merah → tanah hijau → rumah kecil beratap
    merah.
- **Adegan mirip dibedakan dengan sengaja:** Hormuz vs Finland —
  Hormuz langit hangat + tanker navy + tangki dek putih + ledakan +
  ranjau; Finland langit dingin + kapal kargo abu-abu + kontainer
  warna + camar, tanpa ledakan/ranjau. Huawei vs ICJ — Huawei dinding
  hijau + chip besar + timbangan miring; ICJ langit biru + gedung
  pengadilan besar + palu. Korea vs Congo — jet tempur bersudut +
  radar vs pesawat sipil + garis terbang putus-putus + pegunungan.
  Nepal vs Congo — tudung salju + rumah + zigzag merah vs lembah
  hijau + garis terbang.
- **Footer:** strip sumber kini menulis "PICTURES AND MAP DRAWN IN
  CODE, NOT PHOTOS" (tanpa menyebut Lucide — ikon sudah tidak
  dipakai). Folder `icons/` v4 dibiarkan tak terpakai, tidak dihapus.
- **Yang lain tetap dari v2/v3/v4** (header navy, footer DATE CHECK
  merah, frame kotak, warna region, tiga font, stat ribbon di dalam
  adegan, label peta "SCENES 1–13") dan 32 cerita sama.

## Pelajaran dari bug v5 (dicatat supaya tidak terulang)
- Jangan campur implicit string concatenation dengan operator `+`
  dalam satu ekspresi `return (...)`: `f'a' + f'b'` lalu baris
  berikutnya `f'c'` tanpa operator adalah SyntaxError. Aturannya:
  dalam satu blok return, tiap baris lanjutan harus diawali `+`
  ATAU baris sebelumnya diakhiri `+` — atau pakai implicit
  concatenation murni tanpa `+` sama sekali. (Diperbaiki dengan
  script /tmp/fix_concat.py yang menambahkan `+` di depan baris
  literal yang kehilangan operator.)
- Elemen yang harus tersembunyi di balik meja (kaki kursi, tiang
  bendera) harus digambar SEBELUM meja, bukan sesudahnya — kalau
  tidak, kakinya menembus permukaan meja.
