#!/usr/bin/env python3
"""V5 rich vector scenes for news-image-20261124 (drawn in code).

Every top-13 card (3 leads + 10 features) gets a full layered flat-vector
scene, in the style of the approved Hormuz example (tools/scene-hormuz-
preview.html): an environment background + 2-4 layered elements with
scale contrast (one big motif up front, one small motif far away) + one
small detail (sun, cloud, bird, smoke, foam) + the stat ribbon inside
the scene (pandya's device). Flat colours only — no gradients, no
photos, no AI images, no icon libraries.

Lead scenes: viewBox 320x56, artwork y 0..33, ribbon y 33..56.
Feature scenes: viewBox 190x40, artwork y 0..23, ribbon y 23..40.
scene_svg() is called from gen_entry.py with REGIONS/TINTS passed in.
"""
NAVY = '#14264d'
INK = '#141414'
WHITE = '#fffdf4'
GOLD = '#d8b45a'
RED = '#a31621'


def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
             .replace('"', '&quot;'))


def cloud(cx, cy, s=1.0):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{14 * s:.1f}" ry="{4 * s:.1f}" fill="{WHITE}"/>'
            f'<ellipse cx="{cx + 16 * s:.1f}" cy="{cy - 2 * s:.1f}" rx="{10 * s:.1f}" '
            f'ry="{3.5 * s:.1f}" fill="{WHITE}"/>')


def bird(cx, cy, s=1.0, col=NAVY):
    return (f'<path d="M{cx} {cy} q{3 * s:.1f} {-3 * s:.1f} {6 * s:.1f} 0 '
            f'q{3 * s:.1f} {-3 * s:.1f} {6 * s:.1f} 0" fill="none" '
            f'stroke="{col}" stroke-width="1"/>')


def sun(cx, cy, r, fill=GOLD):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>'


def waves(y, w, color, op=0.55, ph=0):
    """One row of wave lines across width w (q/t pattern, like Hormuz)."""
    n = int(w // 20) + 2
    d = f'M{-10 + ph} {y} q10 -3 20 0 ' + 't20 0 ' * n
    return (f'<path d="{d}" fill="none" stroke="{color}" '
            f'stroke-width="1.1" opacity="{op}"/>')


# ---------------------------------------------------------------------------
# LEAD 1 — Huawei verdict: big chip + tilted scales of justice (tech trial).
# Courtroom wall, floor, court papers, gold sparkles. The beam tilts —
# the guilty side hangs lower.
# ---------------------------------------------------------------------------
def art_huawei():
    pins_t = ''.join(f'<rect x="{x}" y="4" width="3" height="3" fill="{NAVY}"/>'
                     for x in (30, 42, 54, 66))
    pins_b = ''.join(f'<rect x="{x}" y="27" width="3" height="3" fill="{NAVY}"/>'
                     for x in (30, 42, 54, 66))
    return (
        f'<rect width="320" height="33" fill="#e9f0e2"/>'
        + f'<rect x="0" y="28" width="320" height="5" fill="#c9d8bd"/>'
        # chip, left
        + f'<rect x="26" y="7" width="46" height="20" fill="{NAVY}"/>'
        + f'<rect x="34" y="11" width="30" height="12" fill="#1e8a4c"/>'
        + f'<rect x="44" y="15" width="10" height="4" fill="{GOLD}"/>'
        + pins_t + pins_b
        # court papers, centre
        + f'<rect x="118" y="22" width="20" height="6" fill="{WHITE}" stroke="{NAVY}" stroke-width="0.8"/>'
        + f'<rect x="142" y="22" width="20" height="6" fill="{WHITE}" stroke="{NAVY}" stroke-width="0.8"/>'
        + f'<line x1="121" y1="24.5" x2="135" y2="24.5" stroke="{NAVY}" stroke-width="0.7"/>'
        + f'<line x1="121" y1="26.5" x2="132" y2="26.5" stroke="{NAVY}" stroke-width="0.7"/>'
        # scales of justice, right — beam tilted, guilty side down
        + f'<rect x="248" y="7" width="4" height="21" fill="{NAVY}"/>'
        + f'<circle cx="250" cy="5" r="2.5" fill="{GOLD}"/>'
        + f'<line x1="222" y1="9" x2="280" y2="13" stroke="{NAVY}" stroke-width="2"/>'
        + f'<line x1="222" y1="9" x2="222" y2="14" stroke="{NAVY}" stroke-width="1"/>'
        + f'<polygon points="213,14 231,14 222,23" fill="{GOLD}" stroke="{NAVY}" stroke-width="0.8"/>'
        + f'<line x1="280" y1="13" x2="280" y2="18" stroke="{NAVY}" stroke-width="1"/>'
        + f'<polygon points="271,18 289,18 280,27" fill="{GOLD}" stroke="{NAVY}" stroke-width="0.8"/>'
        + f'<circle cx="86" cy="6" r="1.2" fill="{GOLD}"/>'
        + f'<circle cx="92" cy="3" r="1" fill="{GOLD}"/>'
    )


# ---------------------------------------------------------------------------
# LEAD 2 — Hormuz: verbatim from the approved example
# (tools/scene-hormuz-preview.html). Sky + sun/clouds/birds, far sea with
# a small escort ship, waves, front sea, big tanker, bow explosion,
# spiked mines up front.
# ---------------------------------------------------------------------------
def art_hormuz():
    return (
        # LAPIS 1 — langit
        f'<rect width="320" height="33" fill="#fbeed3"/>'
        + f'<circle cx="26" cy="9" r="6" fill="#d8b45a"/>'
        + f'<ellipse cx="118" cy="7" rx="14" ry="4" fill="#fffdf4"/>'
        + f'<ellipse cx="148" cy="5" rx="10" ry="3.5" fill="#fffdf4"/>'
        + f'<ellipse cx="212" cy="5" rx="11" ry="3.5" fill="#fffdf4"/>'
        + f'<path d="M196 9 q3 -3 6 0 q3 -3 6 0" fill="none" stroke="#14264d" stroke-width="1"/>'
        + f'<path d="M226 6 q2.5 -2.5 5 0 q2.5 -2.5 5 0" fill="none" stroke="#14264d" stroke-width="1"/>'
        # LAPIS 2 — laut jauh + kapal escort kecil
        + f'<rect x="0" y="16" width="320" height="11" fill="#7fa8b8"/>'
        + f'<path d="M240 16 L242 12.5 L272 12.5 L274 16 Z" fill="#14264d"/>'
        + f'<rect x="254" y="9.5" width="7" height="3" fill="#14264d"/>'
        + f'<line x1="236" y1="16.8" x2="278" y2="16.8" stroke="#fffdf4" stroke-width="0.8" opacity="0.6"/>'
        + f'<path d="M0 20 q10 -3.5 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0" fill="none" stroke="#fffdf4" stroke-width="1.2" opacity="0.55"/>'
        + f'<path d="M-10 24.5 q10 -3 20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0 t20 0" fill="none" stroke="#fffdf4" stroke-width="1" opacity="0.45"/>'
        # LAPIS 3 — laut depan + buih
        + f'<rect x="0" y="27" width="320" height="6" fill="#2a6f97"/>'
        + f'<circle cx="12" cy="28.5" r="1.6" fill="#fffdf4" opacity="0.8"/>'
        + f'<circle cx="40" cy="29.5" r="1.6" fill="#fffdf4" opacity="0.8"/>'
        + f'<circle cx="210" cy="28.5" r="1.6" fill="#fffdf4" opacity="0.8"/>'
        + f'<circle cx="250" cy="29.5" r="1.6" fill="#fffdf4" opacity="0.8"/>'
        # LAPIS 4 — kapal tanker besar
        + f'<rect x="163" y="9" width="7" height="13" fill="#c96a1e"/>'
        + f'<rect x="163" y="9" width="7" height="3" fill="#14264d"/>'
        + f'<circle cx="166" cy="6.5" r="2" fill="#b9b3a4" opacity="0.9"/>'
        + f'<circle cx="169" cy="3.8" r="2.4" fill="#b9b3a4" opacity="0.9"/>'
        + f'<circle cx="173" cy="1.4" r="2" fill="#b9b3a4" opacity="0.9"/>'
        + f'<rect x="80" y="12" width="24" height="10" rx="2.5" fill="#fffdf4" stroke="#14264d" stroke-width="1"/>'
        + f'<rect x="110" y="12" width="24" height="10" rx="2.5" fill="#fffdf4" stroke="#14264d" stroke-width="1"/>'
        + f'<rect x="140" y="12" width="24" height="10" rx="2.5" fill="#fffdf4" stroke="#14264d" stroke-width="1"/>'
        + f'<line x1="92" y1="13" x2="92" y2="21" stroke="#14264d" stroke-width="0.8" opacity="0.5"/>'
        + f'<line x1="122" y1="13" x2="122" y2="21" stroke="#14264d" stroke-width="0.8" opacity="0.5"/>'
        + f'<line x1="152" y1="13" x2="152" y2="21" stroke="#14264d" stroke-width="0.8" opacity="0.5"/>'
        + f'<circle cx="92" cy="11" r="1" fill="#14264d"/>'
        + f'<circle cx="122" cy="11" r="1" fill="#14264d"/>'
        + f'<circle cx="152" cy="11" r="1" fill="#14264d"/>'
        + f'<rect x="170" y="8" width="16" height="14" fill="#fffdf4" stroke="#14264d" stroke-width="1"/>'
        + f'<rect x="169" y="7" width="18" height="1.5" fill="#14264d"/>'
        + f'<rect x="172.5" y="11" width="3" height="3.5" fill="#14264d"/>'
        + f'<rect x="176.5" y="11" width="3" height="3.5" fill="#14264d"/>'
        + f'<rect x="180.5" y="11" width="3" height="3.5" fill="#14264d"/>'
        + f'<line x1="70" y1="22" x2="70" y2="13" stroke="#14264d" stroke-width="1.2"/>'
        + f'<path d="M70 13 L70 17.5 L77 15.2 Z" fill="#c96a1e"/>'
        + f'<rect x="66" y="21" width="126" height="1.5" fill="#14264d"/>'
        + f'<polygon points="62,22 194,22 189,31 67,31" fill="#14264d"/>'
        + f'<polygon points="65,28.5 191,28.5 189,31 67,31" fill="#a31621"/>'
        + f'<path d="M56 31 q4 -2.5 8 0" fill="none" stroke="#fffdf4" stroke-width="1.2"/>'
        + f'<path d="M52 32.5 q4 -2 8 0" fill="none" stroke="#fffdf4" stroke-width="1" opacity="0.7"/>'
        + f'<path d="M192 31 q6 -2.5 12 0" fill="none" stroke="#fffdf4" stroke-width="1.2"/>'
        # LAPIS 5 — ledakan di haluan
        + f'<polygon points="65,28 60.1,26.7 62.7,22.3 58.3,25.4 57,20 55.7,25.4 51.3,22.3 53.9,26.7 49,28 53.9,29.3 51.3,33.7 55.7,30.6 57,36 58.3,30.6 62.7,33.7 60.1,29.3" fill="#e8a020" stroke="#a31621" stroke-width="0.8"/>'
        + f'<circle cx="48" cy="22" r="1" fill="#e8a020"/>'
        + f'<circle cx="52" cy="19.5" r="0.9" fill="#e8a020"/>'
        # LAPIS 6 — ranjau laut di depan
        + f'<polygon points="288,29 282.2,27.3 285.1,21.9 279.7,24.8 278,19 276.3,24.8 270.9,21.9 273.8,27.3 268,29 273.8,30.7 270.9,36.1 276.3,33.2 278,39 279.7,33.2 285.1,36.1 282.2,30.7" fill="#141414"/>'
        + f'<circle cx="278" cy="29" r="6" fill="#1e1e1e"/>'
        + f'<circle cx="276" cy="27" r="1.5" fill="#ffffff" opacity="0.25"/>'
        + f'<line x1="278" y1="19" x2="278" y2="16.5" stroke="#141414" stroke-width="1"/>'
        + f'<circle cx="278" cy="16" r="1.2" fill="#a31621"/>'
        + f'<path d="M266 31.5 q6 -3 12 0" fill="none" stroke="#fffdf4" stroke-width="1.2"/>'
        + f'<circle cx="268" cy="24" r="1" fill="#fffdf4" opacity="0.8"/>'
        + f'<circle cx="288" cy="24.5" r="1.2" fill="#fffdf4" opacity="0.8"/>'
        + f'<circle cx="284" cy="21" r="0.9" fill="#fffdf4" opacity="0.8"/>'
        + f'<polygon points="314,30 310.8,28.9 312.2,25.8 309.2,27.2 308,24 306.8,27.2 303.8,25.8 305.2,28.9 302,30 305.2,31.1 303.8,34.2 306.8,32.8 308,36 309.2,32.8 312.2,34.2 310.8,31.1" fill="#141414"/>'
        + f'<circle cx="308" cy="30" r="3.5" fill="#1e1e1e"/>'
    )


# ---------------------------------------------------------------------------
# LEAD 3 — ICJ: grand courthouse + gavel up front. Differs from Huawei
# (chip + scales, green courtroom wall) by the building + gavel motif and
# a pale-blue sky.
# ---------------------------------------------------------------------------
def art_icj():
    cols = ''.join(
        f'<rect x="{x}" y="14" width="7" height="12" fill="#e8ecf0" stroke="{NAVY}" stroke-width="0.8"/>'
        for x in (102, 128, 184, 210))
    return (
        f'<rect width="320" height="33" fill="#dce9f5"/>'
        + sun(28, 8, 5) + cloud(60, 6, 0.8) + cloud(280, 5, 0.9) + bird(250, 9, 0.9)
        # small flag, left
        + f'<line x1="70" y1="10" x2="70" y2="26" stroke="{NAVY}" stroke-width="1"/>'
        + f'<rect x="70" y="10" width="10" height="6" fill="#1e8a4c"/>'
        # courthouse
        + f'<rect x="78" y="29" width="164" height="4" fill="#8a97a8"/>'
        + f'<rect x="84" y="26" width="152" height="3" fill="#aab6c4"/>'
        + f'<rect x="92" y="13" width="136" height="13" fill="{WHITE}" stroke="{NAVY}" stroke-width="1"/>'
        + f'<polygon points="86,13 234,13 160,2" fill="{NAVY}"/>'
        + f'<circle cx="160" cy="8" r="2.5" fill="{GOLD}"/>'
        + cols
        + f'<rect x="152" y="18" width="16" height="8" fill="{NAVY}"/>'
        # gavel, foreground right
        + f'<rect x="252" y="29" width="20" height="3" fill="#8a5a2b"/>'
        + f'<line x1="262" y1="29" x2="274" y2="18" stroke="#8a5a2b" stroke-width="3"/>'
        + f'<g transform="rotate(-30 274 15)">'
        + f'<rect x="265" y="11" width="18" height="8" rx="1.5" fill="#8a5a2b" stroke="{INK}" stroke-width="0.8"/>'
        + f'</g>'
    )


# ---------------------------------------------------------------------------
# FEATURE 4 — Riyadh: dusk skyline, PIF tower centre, low sun, birds.
# ---------------------------------------------------------------------------
def art_riyadh():
    tower_lights = ''.join(
        f'<rect x="{x}" y="{y}" width="1.6" height="2" fill="{GOLD}"/>'
        for x, y in ((92, 9), (96, 9), (92, 14), (96, 14), (94, 18)))
    return (
        f'<rect width="190" height="23" fill="#f6cf9a"/>'
        + sun(24, 8, 5) + bird(140, 6, 0.8) + bird(158, 9, 0.7)
        + f'<circle cx="70" cy="4" r="0.9" fill="{GOLD}"/>'
        + f'<circle cx="120" cy="3" r="0.9" fill="{GOLD}"/>'
        + f'<rect x="0" y="14" width="18" height="9" fill="{NAVY}"/>'
        + f'<rect x="22" y="11" width="14" height="12" fill="{NAVY}"/>'
        + f'<rect x="40" y="15" width="16" height="8" fill="{NAVY}"/>'
        + f'<rect x="150" y="12" width="16" height="11" fill="{NAVY}"/>'
        + f'<rect x="170" y="15" width="20" height="8" fill="{NAVY}"/>'
        + f'<polygon points="86,23 90,4 100,4 104,23" fill="{NAVY}"/>'
        + f'<rect x="90" y="2" width="10" height="2" fill="{GOLD}"/>'
        + tower_lights
        + f'<rect x="26" y="14" width="2" height="2" fill="{GOLD}"/>'
        + f'<rect x="30" y="18" width="2" height="2" fill="{GOLD}"/>'
        + f'<rect x="154" y="15" width="2" height="2" fill="{GOLD}"/>'
    )


# ---------------------------------------------------------------------------
# FEATURE 8 — Finland: cold northern sea, grey cargo ship with containers,
# gulls, pale sun. Differs from Hormuz: grey ship, cold palette, no mine,
# no explosion, no tanker tanks.
# ---------------------------------------------------------------------------
def art_finland():
    return (
        f'<rect width="190" height="23" fill="#dfe9f0"/>'
        + f'<rect x="0" y="10" width="190" height="7" fill="#7fa8b8"/>'
        + f'<rect x="0" y="17" width="190" height="6" fill="#2a6f97"/>'
        + f'<circle cx="168" cy="5" r="4" fill="{WHITE}" opacity="0.85"/>'
        + bird(20, 5, 0.8) + bird(34, 7, 0.7)
        + waves(13, 190, WHITE, 0.5) + waves(19.5, 190, WHITE, 0.45, 6)
        + f'<polygon points="52,17 138,17 132,23 58,23" fill="#5a6b7a"/>'
        + f'<rect x="104" y="10" width="16" height="7" fill="#e8ecf0" stroke="{NAVY}" stroke-width="0.8"/>'
        + f'<rect x="108" y="12" width="3" height="2.5" fill="{NAVY}"/>'
        + f'<rect x="113" y="12" width="3" height="2.5" fill="{NAVY}"/>'
        + f'<rect x="60" y="12" width="12" height="5" fill="#c96a1e"/>'
        + f'<rect x="74" y="12" width="12" height="5" fill="#1e8a4c"/>'
        + f'<rect x="88" y="12" width="12" height="5" fill="#d8b45a"/>'
        + f'<line x1="128" y1="17" x2="128" y2="8" stroke="{NAVY}" stroke-width="1"/>'
        + f'<path d="M140 22 q5 -2 10 0" fill="none" stroke="{WHITE}" stroke-width="1"/>'
        + f'<path d="M46 22 q4 -2 8 0" fill="none" stroke="{WHITE}" stroke-width="1"/>'
    )


# ---------------------------------------------------------------------------
# FEATURE 12 — Colombia: street + supermarket storefront, striped awning,
# police tape across the door (no graphic violence).
# ---------------------------------------------------------------------------
def art_colombia():
    stripes = ''.join(
        f'<rect x="{38 + i * 11.8:.1f}" y="10" width="11.8" height="4" '
        f'fill="{("#b03a7d" if i % 2 == 0 else WHITE)}"/>' for i in range(10))
    tape = ''.join(
        f'<line x1="{44 + i * 12}" y1="19.5" x2="{40 + i * 12}" y2="21.1" '
        f'stroke="{INK}" stroke-width="0.8"/>' for i in range(10))
    return (
        f'<rect width="190" height="23" fill="#fbeed3"/>'
        + sun(16, 6, 4) + cloud(150, 5, 0.8)
        + f'<rect x="0" y="8" width="30" height="15" fill="#e8a0b8"/>'
        + f'<rect x="4" y="11" width="6" height="5" fill="{WHITE}" stroke="{NAVY}" stroke-width="0.7"/>'
        + f'<rect x="14" y="11" width="6" height="5" fill="{WHITE}" stroke="{NAVY}" stroke-width="0.7"/>'
        + f'<rect x="162" y="6" width="28" height="17" fill="#f3dbe9"/>'
        + f'<rect x="166" y="9" width="6" height="5" fill="{WHITE}" stroke="{NAVY}" stroke-width="0.7"/>'
        + f'<rect x="176" y="9" width="6" height="5" fill="{WHITE}" stroke="{NAVY}" stroke-width="0.7"/>'
        + f'<rect x="38" y="10" width="118" height="13" fill="{WHITE}" stroke="{NAVY}" stroke-width="1"/>'
        + stripes
        + f'<rect x="38" y="14" width="118" height="1" fill="{NAVY}" opacity="0.4"/>'
        + f'<rect x="88" y="16" width="14" height="7" fill="{NAVY}"/>'
        + f'<rect x="48" y="16" width="14" height="6" fill="#7fa8b8" stroke="{NAVY}" stroke-width="0.7"/>'
        + f'<rect x="128" y="16" width="14" height="6" fill="#7fa8b8" stroke="{NAVY}" stroke-width="0.7"/>'
        + f'<rect x="80" y="5" width="30" height="4" fill="#b03a7d"/>'
        + f'<rect x="0" y="21" width="190" height="2" fill="#8a97a8"/>'
        + f'<rect x="38" y="19.5" width="118" height="1.6" fill="#f5d020"/>'
        + tape
    )


# ---------------------------------------------------------------------------
# FEATURE 15 — DR Congo: sky + two mountain ranges with snow caps + plane
# on a dashed flight path + green valley.
# ---------------------------------------------------------------------------
def art_congo():
    return (
        f'<rect width="190" height="23" fill="#dcebf5"/>'
        + sun(14, 6, 4) + cloud(120, 5, 0.8)
        + f'<polygon points="0,23 32,7 64,23" fill="#7fa8b8"/>'
        + f'<polygon points="27,11 32,7 37,11" fill="{WHITE}"/>'
        + f'<polygon points="44,23 96,3 148,23" fill="#2a6f97"/>'
        + f'<polygon points="89,8 96,3 103,8" fill="{WHITE}"/>'
        + f'<path d="M8 20 q50 -12 104 -11" fill="none" stroke="{NAVY}" stroke-width="0.9" stroke-dasharray="3 3" opacity="0.7"/>'
        + f'<g transform="translate(118 4)">'
        + f'<polygon points="0,3 20,3 26,5 20,7 0,7" fill="{NAVY}"/>'
        + f'<polygon points="8,3 14,-2 18,-2 13,3" fill="{NAVY}"/>'
        + f'<polygon points="2,3 -2,-1 1,-1 4,3" fill="{NAVY}"/>'
        + f'</g>'
        + f'<rect x="0" y="21" width="190" height="2" fill="#1e8a4c"/>'
    )


# ---------------------------------------------------------------------------
# FEATURE 16 — Vietnam: restaurant wall + red lantern + table + steaming
# hot-pot + bowl with chopsticks + small plant.
# ---------------------------------------------------------------------------
def art_vietnam():
    return (
        f'<rect width="190" height="23" fill="#f7e3cd"/>'
        + f'<line x1="168" y1="0" x2="168" y2="3" stroke="{INK}" stroke-width="0.8"/>'
        + f'<circle cx="168" cy="8" r="6" fill="#c0392b"/>'
        + f'<rect x="165" y="1.5" width="6" height="1.5" fill="{GOLD}"/>'
        + f'<rect x="165" y="13.5" width="6" height="1.5" fill="{GOLD}"/>'
        + f'<line x1="168" y1="15" x2="168" y2="17" stroke="{GOLD}" stroke-width="0.8"/>'
        + f'<rect x="0" y="16" width="190" height="7" fill="#8a5a2b"/>'
        + f'<rect x="0" y="16" width="190" height="1" fill="#6e4520"/>'
        + f'<path d="M88 6 q2 -3 0 -5 M96 6 q-2 -3 0 -5 M104 6 q2 -3 0 -5" fill="none" stroke="{WHITE}" stroke-width="1.2" opacity="0.85"/>'
        + f'<ellipse cx="96" cy="8" rx="18" ry="3" fill="#5a5a5a"/>'
        + f'<rect x="78" y="8" width="36" height="8" fill="#3a3a3a"/>'
        + f'<rect x="74" y="10" width="4" height="3" fill="#3a3a3a"/>'
        + f'<rect x="114" y="10" width="4" height="3" fill="#3a3a3a"/>'
        + f'<path d="M40 12 h18 l-3 4 h-12 z" fill="{WHITE}" stroke="{NAVY}" stroke-width="0.8"/>'
        + f'<line x1="46" y1="10" x2="62" y2="5" stroke="{INK}" stroke-width="1"/>'
        + f'<line x1="49" y1="11" x2="64" y2="6" stroke="{INK}" stroke-width="1"/>'
        + f'<rect x="136" y="12" width="8" height="4" fill="#c96a1e"/>'
        + f'<path d="M140 12 q-3 -5 -6 -5 M140 12 q0 -6 2 -7 M140 12 q3 -5 6 -4" fill="none" stroke="#1e8a4c" stroke-width="1.2"/>'
    )


# ---------------------------------------------------------------------------
# FEATURE 20 — S. Korea: sky + two fighter jets with contrails + radar
# arcs bottom-left. Differs from the Congo plane: angular jets + radar.
# ---------------------------------------------------------------------------
def _jet(x, y, s):
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<polygon points="0,3 20,3 26,5 20,7 0,7" fill="{NAVY}"/>'
            f'<polygon points="8,3 14,-3 19,-3 13,3" fill="{NAVY}"/>'
            f'<polygon points="3,3 -1,-2 2,-2 5,3" fill="{NAVY}"/>'
            f'</g>')


def art_korea():
    return (
        f'<rect width="190" height="23" fill="#dcebf5"/>'
        + sun(170, 6, 4) + cloud(40, 5, 0.8) + cloud(130, 4, 0.7)
        + f'<line x1="8" y1="8" x2="34" y2="8" stroke="{WHITE}" stroke-width="1" opacity="0.8"/>'
        + f'<line x1="96" y1="17" x2="118" y2="17" stroke="{WHITE}" stroke-width="1" opacity="0.8"/>'
        + _jet(36, 5, 1.0) + _jet(120, 14, 0.75)
        + f'<path d="M14 23 a9 9 0 0 1 9 -9" fill="none" stroke="#1e8a4c" stroke-width="1"/>'
        + f'<path d="M14 23 a14 14 0 0 1 14 -14" fill="none" stroke="#1e8a4c" stroke-width="1" opacity="0.6"/>'
        + f'<circle cx="14" cy="23" r="1.6" fill="#1e8a4c"/>'
    )


# ---------------------------------------------------------------------------
# FEATURE 22 — USA: Pentagon building + US flag + lawn + trees.
# ---------------------------------------------------------------------------
def art_usa():
    windows = ''.join(
        f'<rect x="{x}" y="15" width="4" height="3" fill="{NAVY}"/>'
        for x in (64, 74, 84, 102, 112, 122))
    stripes = ''.join(
        f'<rect x="156" y="{4 + i * 2.2:.1f}" width="17" height="1.1" '
        f'fill="{("#a31621" if i % 2 == 0 else WHITE)}"/>' for i in range(4))
    return (
        f'<rect width="190" height="23" fill="#dce9f2"/>'
        + sun(20, 6, 4) + cloud(60, 5, 0.8) + cloud(140, 4, 0.7)
        + f'<polygon points="55,23 55,12 95,6 135,12 135,23" fill="#c9cfd6" stroke="{NAVY}" stroke-width="1"/>'
        + windows
        + f'<rect x="92" y="18" width="6" height="5" fill="{NAVY}"/>'
        + f'<line x1="156" y1="4" x2="156" y2="23" stroke="{NAVY}" stroke-width="1.2"/>'
        + stripes
        + f'<rect x="156" y="4" width="7" height="4.4" fill="{NAVY}"/>'
        + f'<rect x="0" y="21" width="190" height="2" fill="#1e8a4c"/>'
        + f'<circle cx="36" cy="17" r="3.5" fill="#1e8a4c"/>'
        + f'<rect x="35" y="20" width="2" height="3" fill="#8a5a2b"/>'
        + f'<circle cx="176" cy="17" r="3" fill="#1e8a4c"/>'
        + f'<rect x="175" y="20" width="2" height="3" fill="#8a5a2b"/>'
    )


# ---------------------------------------------------------------------------
# FEATURE 24 — Mexico: desert + mesas + cacti + quadcopter drone + sun.
# ---------------------------------------------------------------------------
def art_mexico():
    return (
        f'<rect width="190" height="23" fill="#fbeed3"/>'
        + sun(166, 7, 6)
        + f'<polygon points="0,16 18,10 48,10 66,16" fill="#d8a86a"/>'
        + f'<polygon points="118,16 138,11 168,11 188,16" fill="#c98f4e"/>'
        + f'<rect x="0" y="16" width="190" height="7" fill="#e8c88f"/>'
        + f'<rect x="16" y="8" width="5" height="10" fill="#1e8a4c"/>'
        + f'<rect x="11" y="11" width="5" height="2.5" fill="#1e8a4c"/>'
        + f'<rect x="11" y="11" width="2.5" height="5" fill="#1e8a4c"/>'
        + f'<rect x="21" y="12" width="5" height="2.5" fill="#1e8a4c"/>'
        + f'<rect x="23.5" y="12" width="2.5" height="4" fill="#1e8a4c"/>'
        + f'<rect x="146" y="12" width="4" height="6" fill="#1e8a4c"/>'
        + f'<ellipse cx="95" cy="7" rx="9" ry="3" fill="{NAVY}"/>'
        + f'<ellipse cx="82" cy="4.5" rx="6" ry="1.2" fill="{NAVY}" opacity="0.7"/>'
        + f'<ellipse cx="108" cy="4.5" rx="6" ry="1.2" fill="{NAVY}" opacity="0.7"/>'
        + f'<line x1="88" y1="9" x2="86" y2="13" stroke="{NAVY}" stroke-width="1"/>'
        + f'<line x1="102" y1="9" x2="104" y2="13" stroke="{NAVY}" stroke-width="1"/>'
        + f'<circle cx="95" cy="7" r="1.2" fill="{RED}"/>'
        + f'<ellipse cx="60" cy="20" rx="5" ry="1.8" fill="#b9b3a4"/>'
        + f'<ellipse cx="130" cy="21" rx="4" ry="1.5" fill="#b9b3a4"/>'
    )


# ---------------------------------------------------------------------------
# FEATURE 28 — Ukraine: window with light + Ukrainian and EU flags +
# table with documents + chairs (chairs/flags drawn before the table so
# their legs/poles hide behind it).
# ---------------------------------------------------------------------------
def art_ukraine():
    stars = ''.join(
        f'<circle cx="{x}" cy="{y}" r="0.8" fill="{GOLD}"/>'
        for x, y in ((162, 7), (167, 6), (172, 7), (164, 11), (170, 11)))
    return (
        f'<rect width="190" height="23" fill="#dde3f0"/>'
        + f'<rect x="72" y="3" width="46" height="12" fill="#bcd6ea" stroke="{NAVY}" stroke-width="1"/>'
        + f'<line x1="95" y1="3" x2="95" y2="15" stroke="{NAVY}" stroke-width="0.8"/>'
        + f'<line x1="72" y1="9" x2="118" y2="9" stroke="{NAVY}" stroke-width="0.8"/>'
        + f'<circle cx="80" cy="6" r="2" fill="{GOLD}"/>'
        # flags (behind the table)
        + f'<line x1="30" y1="4" x2="30" y2="17" stroke="{NAVY}" stroke-width="1"/>'
        + f'<rect x="30" y="4" width="18" height="5" fill="#1f5fa8"/>'
        + f'<rect x="30" y="9" width="18" height="5" fill="{GOLD}"/>'
        + f'<line x1="158" y1="4" x2="158" y2="17" stroke="{NAVY}" stroke-width="1"/>'
        + f'<rect x="158" y="4" width="18" height="10" fill="#1f3a8a"/>'
        + stars
        # chairs (backs above the table, legs hidden behind it)
        + f'<rect x="52" y="11" width="12" height="5" fill="#5a6b7a"/>'
        + f'<rect x="54" y="16" width="2" height="7" fill="#5a6b7a"/>'
        + f'<rect x="60" y="16" width="2" height="7" fill="#5a6b7a"/>'
        + f'<rect x="126" y="11" width="12" height="5" fill="#5a6b7a"/>'
        + f'<rect x="128" y="16" width="2" height="7" fill="#5a6b7a"/>'
        + f'<rect x="134" y="16" width="2" height="7" fill="#5a6b7a"/>'
        # table + documents
        + f'<rect x="18" y="16" width="154" height="7" fill="#8a5a2b"/>'
        + f'<rect x="18" y="16" width="154" height="1" fill="#6e4520"/>'
        + f'<rect x="82" y="13.5" width="12" height="2.5" fill="{WHITE}" stroke="{NAVY}" stroke-width="0.6"/>'
        + f'<rect x="98" y="13.5" width="12" height="2.5" fill="{WHITE}" stroke="{NAVY}" stroke-width="0.6"/>'
    )


# ---------------------------------------------------------------------------
# FEATURE 30 — Nepal: snowy mountains + red seismic zigzag + small house
# at the base. Differs from the Congo mountains: snow caps + house +
# the zigzag line as the main event.
# ---------------------------------------------------------------------------
def art_nepal():
    return (
        f'<rect width="190" height="23" fill="#dcebf5"/>'
        + sun(160, 6, 4) + bird(30, 6, 0.8)
        + f'<polygon points="0,23 62,2 124,23" fill="#8a97a8"/>'
        + f'<polygon points="50,9 62,2 74,9 70,11 62,8 54,11" fill="{WHITE}"/>'
        + f'<polygon points="84,23 142,6 190,23" fill="#5a6b7a"/>'
        + f'<polygon points="134,11 142,6 150,11 147,12.5 142,10.5 137,12.5" fill="{WHITE}"/>'
        + f'<polyline points="8,16 18,12 28,19 38,13 48,18 58,12 68,18 78,13 88,18 98,12 108,18 118,13 128,18 138,12 148,18 158,13 168,18 178,14" fill="none" stroke="{RED}" stroke-width="1.2"/>'
        + f'<rect x="0" y="21" width="190" height="2" fill="#1e8a4c"/>'
        + f'<rect x="86" y="17" width="16" height="6" fill="{WHITE}" stroke="{NAVY}" stroke-width="0.8"/>'
        + f'<polygon points="84,17 104,17 94,12" fill="{RED}"/>'
        + f'<rect x="92" y="19" width="4" height="4" fill="{NAVY}"/>'
    )


ART = {
    1: art_huawei, 2: art_hormuz, 3: art_icj,
    4: art_riyadh, 8: art_finland, 12: art_colombia, 15: art_congo,
    16: art_vietnam, 20: art_korea, 22: art_usa, 24: art_mexico,
    28: art_ukraine, 30: art_nepal,
}


def scene_svg(n, reg, stat, label, lead, regions, tints):
    """Full scene SVG for a top-13 card: layered vector artwork with the
    region-coloured stat ribbon at the bottom (pandya's device).
    Lead scenes: viewBox 320x56, artwork y 0..33, ribbon y 33..56.
    Feature scenes: viewBox 190x40, artwork y 0..23, ribbon y 23..40."""
    col = regions[reg][1]
    tint = tints[reg]
    art = ART[n]()
    if lead:
        w, h, ry, rh = 320, 56, 33, 23
        fs_num, fs_lab, y_txt, x_num, x_lab = 19, 9, 50, 8, 312
    else:
        w, h, ry, rh = 190, 40, 23, 17
        fs_num, fs_lab, y_txt, x_num, x_lab = 13, 7, 36, 6, 184
    return (
        f'<svg class="scene" viewBox="0 0 {w} {h}" width="100%" '
        + f'preserveAspectRatio="xMidYMid meet" aria-hidden="true">'
        + f'<rect width="{w}" height="{h}" fill="{tint}"/>'
        + f'{art}'
        + f'<rect x="0" y="{ry}" width="{w}" height="{rh}" fill="{col}"/>'
        + f'<text x="{x_num}" y="{y_txt}" font-family="Oswald" font-weight="600" '
        + f'font-size="{fs_num}" fill="#fff" letter-spacing="0.5">{esc(stat)}</text>'
        + f'<text x="{x_lab}" y="{y_txt}" font-family="Oswald" font-weight="500" '
        + f'font-size="{fs_lab}" fill="#fff" letter-spacing="1.5" '
        + f'text-anchor="end">{esc(label)}</text></svg>')
