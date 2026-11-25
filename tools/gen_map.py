#!/usr/bin/env python3
"""Generate an accurate equirectangular world-map SVG fragment from real
country coastline data (Natural Earth via johan/world.geo.json, 110m-ish).
Build-time only: the finished render.html embeds the paths, so the entry
program itself needs no network. Output: map.svg (fragment) in this dir."""
import json, math

W, H = 984, 144
LON0, LON1 = -180.0, 180.0
LAT0, LAT1 = 75.0, -52.0  # top, bottom
SX = W / (LON1 - LON0)
SY = H / (LAT0 - LAT1)

def proj(lon, lat):
    return ((lon - LON0) * SX, (LAT0 - lat) * SY)

def dp(pts, tol):
    """Douglas-Peucker on (lon, lat) points, tol in degrees."""
    if len(pts) <= 2:
        return pts
    ax, ay = pts[0]; bx, by = pts[-1]
    dx, dy = bx - ax, by - ay
    L = math.hypot(dx, dy) or 1.0
    worst, idx = 0.0, -1
    for i in range(1, len(pts) - 1):
        x, y = pts[i]
        d = abs(dy * x - dx * y + bx * ay - by * ax) / L
        if d > worst:
            worst, idx = d, i
    if worst > tol:
        return dp(pts[:idx + 1], tol)[:-1] + dp(pts[idx:], tol)
    return [pts[0], pts[-1]]

def ring_path(ring):
    # clip lat, drop Antarctica, simplify, project, emit path
    pts = [(lon, max(min(lat, LAT0), LAT1)) for lon, lat in ring]
    if len(pts) > 1 and pts[0] == pts[-1]:
        pts = pts[:-1]  # closed ring: first==last breaks Douglas-Peucker (zero baseline)
    pts = dp(pts, 0.45)
    if len(pts) < 3:
        return ""
    xy = [proj(lon, lat) for lon, lat in pts]
    d = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in xy) + " Z"
    return d

data = json.load(open("countries.geo.json"))
paths = []
for feat in data["features"]:
    g = feat["geometry"]
    if g["type"] == "Polygon":
        rings = g["coordinates"]
    elif g["type"] == "MultiPolygon":
        rings = [r for poly in g["coordinates"] for r in poly]
    else:
        continue
    for ring in rings:
        # skip Antarctica (all lat < -52)
        if all(lat < -52 for _, lat in ring):
            continue
        d = ring_path(ring)
        if d:
            paths.append(d)

print(f"countries polygons: {len(paths)}")

# --- story dots: (n, lat, lon, badge_dx, badge_dy) badge offset in px, (0,0)=true position
dots = [
    (1, 32.0, 53.0, 0, 0), (2, 36.9, 30.7, 16, 20), (3, 37.4, -122.0, 0, 0),
    (4, 26.2, 50.6, 0, 0), (5, 26.5, 56.3, 18, -16), (6, 26.0, 56.0, 18, 18),
    (7, 38.9, -77.0, 0, 0), (8, 31.5, 34.5, -30, 22), (9, 31.5, 34.5, 6, 30),
    (10, 31.9, 35.2, 26, -20), (11, 32.1, 34.8, 28, 14),
    (12, 15.4, 44.2, 12, 14), (13, 32.1, 20.1, 0, 0), (14, 15.6, 32.5, -14, 16),
    (15, 47.9, 33.4, -24, -14), (16, 50.8, 30.3, 10, -16), (17, 32.5, 19.5, -22, 20),
    (18, 59.0, 21.0, -14, -8), (19, 52.2, 21.0, 14, 14), (20, 55.7, 12.6, 0, 0),
    (21, 55.7, 37.6, 24, -10), (22, 35.8, -80.8, -19, 17), (23, 40.7, -74.0, 20, -14),
    (24, 33.7, -84.4, -21, -16), (25, 24.8, -107.4, 0, 0), (26, 47.6, -122.3, -16, -11),
    (27, -4.3, 15.3, 0, 0), (28, 38.9, -77.0, 21, 17), (29, 37.5, 127.0, 0, 0),
    (30, 23.8, 90.4, 0, 0), (31, -41.3, 174.8, 0, 0), (32, -34.6, -58.4, 0, 0),
]
labels = [
    ("N. AMERICA", 185, 14), ("S. AMERICA", 335, 118), ("EUROPE", 470, 35),
    ("AFRICA", 570, 100), ("ASIA", 795, 28), ("AUSTRALIA", 862, 128),
]
out = []
out.append(f'<svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">')
out.append(f'<rect width="{W}" height="{H}" fill="#e9e2c8"/>')
out.append('<g fill="#c9bd93" stroke="#a89a6c" stroke-width="0.6">')
for d in paths:
    out.append(f'<path d="{d}"/>')
out.append('</g>')
# graticule: equator + tropics, faint, helps the map read as a map
for lat, name in [(0, "equator"), (23.4, "tropic"), (-23.4, "tropic")]:
    y = (LAT0 - lat) * SY
    out.append(f'<line x1="0" y1="{y:.1f}" x2="{W}" y2="{y:.1f}" stroke="#b7ab7d" stroke-width="0.5" stroke-dasharray="3 4"/>')
for (txt, x, y) in labels:
    out.append(f'<text x="{x}" y="{y}" font-family="DejaVu Sans" font-size="9" letter-spacing="1.5" fill="#6b5f33" text-anchor="middle">{txt}</text>')
# leader lines first, then badges on top
for n, lat, lon, dx, dy in dots:
    if dx or dy:
        ax, ay = proj(lon, lat)
        out.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{ax+dx:.1f}" y2="{ay+dy:.1f}" stroke="#b91c1c" stroke-width="1"/>')
        out.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="2.4" fill="#b91c1c"/>')
for n, lat, lon, dx, dy in dots:
    ax, ay = proj(lon, lat)
    bx, by = ax + dx, ay + dy
    out.append(f'<g font-family="DejaVu Sans" font-size="9.5" font-weight="bold" text-anchor="middle">'
               f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="7.5" fill="#b91c1c" stroke="#fff" stroke-width="1.4"/>'
               f'<text x="{bx:.1f}" y="{by+3.5:.1f}" fill="#fff">{n}</text></g>')
out.append('</svg>')
open("map.svg", "w").write("\n".join(out))
print("wrote map.svg", len("\n".join(out)), "bytes")
for n, lat, lon, dx, dy in dots:
    ax, ay = proj(lon, lat)
    print(n, f"anchor=({ax:.0f},{ay:.0f}) badge=({ax+dx:.0f},{ay+dy:.0f})")
