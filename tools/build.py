"""Expand {{img ...}} tokens in src/index.template.html into responsive <picture> tags.

Token syntax (pipe separated):
  {{img name | alt text | sizes | extra classes | eager}}
- name: base name in assets/img (expects name-640/1280[/1920].webp + .jpg)
- sizes: the <img sizes> value (default 100vw)
- eager: put the word "eager" to skip lazy-loading (hero only)

Run:  .tools/Scripts/python tools/build.py
"""
import os, re, html
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "assets", "img")
SRC = os.path.join(ROOT, "src", "index.template.html")
OUT = os.path.join(ROOT, "index.html")


def widths(name):
    return [w for w in (640, 1280, 1920) if os.path.exists(os.path.join(IMG, f"{name}-{w}.webp"))]


def picture(m):
    parts = [p.strip() for p in m.group(1).split("|")]
    name = parts[0]
    alt = parts[1] if len(parts) > 1 else ""
    sizes = parts[2] if len(parts) > 2 and parts[2] else "100vw"
    cls = parts[3] if len(parts) > 3 else ""
    eager = len(parts) > 4 and parts[4] == "eager"
    ws = widths(name)
    if not ws:
        raise SystemExit(f"missing image: {name}")
    mid = 1280 if 1280 in ws else ws[-1]
    w, h = Image.open(os.path.join(IMG, f"{name}-{mid}.jpg")).size
    webp = ", ".join(f"assets/img/{name}-{x}.webp {x}w" for x in ws)
    jpg = ", ".join(f"assets/img/{name}-{x}.jpg {x}w" for x in ws)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (
        f'<picture class="{cls}">'
        f'<source type="image/webp" srcset="{webp}" sizes="{sizes}">'
        f'<img src="assets/img/{name}-{mid}.jpg" srcset="{jpg}" sizes="{sizes}" '
        f'width="{w}" height="{h}" alt="{html.escape(alt, quote=True)}" {load}>'
        f"</picture>"
    )


def main():
    with open(SRC, encoding="utf-8") as f:
        t = f.read()
    t = re.sub(r"\{\{img (.+?)\}\}", picture, t)
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    print("wrote", OUT, len(t), "bytes")


if __name__ == "__main__":
    main()
