"""Justerer AI-genererte illustrasjoner til Husorden-paletten.

Rosa toner trekkes mot håndklærosa (#F7A1B5) og mint mot maskinmint (#8EE3C8).
Mørke konturer, hud, gult og hvitt røres ikke.

Bruk:  python3 verktoy/fargejuster.py inn.png ut.png [størrelse]
Krever: pip install pillow numpy
"""
import sys
import numpy as np
from PIL import Image


def juster(im):
    a = np.array(im.convert("RGBA")).astype(float) / 255
    rgb = a[..., :3]
    mx, mn = rgb.max(-1), rgb.min(-1)
    d = mx - mn + 1e-9
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    h = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
    s = np.where(mx > 0, d / (mx + 1e-9), 0)
    v = mx
    rosa = ((h > 320) | (h < 8)) & (s > 0.25) & (v > 0.55)
    mint = (h > 145) & (h < 180) & (s > 0.2) & (v > 0.6)
    s2, v2, h2 = s.copy(), v.copy(), h.copy()
    s2[rosa] = np.minimum(s[rosa] * 0.62, 0.42)
    v2[rosa] = np.minimum(1, v[rosa] * 1.03)
    h2[rosa] = 346
    s2[mint] = s[mint] * 0.72
    c = v2 * s2
    hp = (h2 % 360) / 60
    x = c * (1 - abs(hp % 2 - 1))
    m = v2 - c
    z = np.zeros_like(c)
    vilk = [hp < 1, hp < 2, hp < 3, hp < 4, hp < 5, hp >= 5]
    verdi = [(c, x, z), (x, c, z), (z, c, x), (z, x, c), (x, z, c), (c, z, x)]
    R = np.select(vilk, [t[0] for t in verdi])
    G = np.select(vilk, [t[1] for t in verdi])
    B = np.select(vilk, [t[2] for t in verdi])
    ut = np.stack([R + m, G + m, B + m, a[..., 3]], -1)
    return Image.fromarray((np.clip(ut, 0, 1) * 255).astype("uint8"), "RGBA")


if __name__ == "__main__":
    inn, ut = sys.argv[1], sys.argv[2]
    bilde = juster(Image.open(inn))
    if len(sys.argv) > 3:
        n = int(sys.argv[3])
        bilde = bilde.resize((n, n), Image.LANCZOS)
    bilde.save(ut)
    print("Lagret", ut)
