"""Clean up and export Balai Taltalon photos for the web.

Pipeline per image (kept deliberately light so the place still looks like itself):
  1. gentle gray-world white balance (blended 35% so warm timber stays warm)
  2. light chroma/luma denoise to clean phone/JPEG artifacts
  3. mild local contrast (CLAHE on L channel, low clip)
  4. small warmth + saturation trim toward the site's "Pine & Ember" mood
  5. unsharp mask after resizing
  6. export WebP + JPG at 640 / 1280 / 1920 widths (never upscaled past 1.0x of source,
     except where a source is narrower than 1280; then Lanczos upscale is used)

Run:  .tools/Scripts/python tools/process_images.py
"""
import os, sys
import numpy as np
import cv2
from PIL import Image, ImageFilter, ImageEnhance

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets", "originals")
OUT = os.path.join(ROOT, "assets", "img")
os.makedirs(OUT, exist_ok=True)

# output name -> (source file, optional crop box as fractions l,t,r,b, widths)
W3 = (640, 1280, 1920)
W2 = (640, 1280)
MAP = {
    "hero":            ("airbnb/ab60", None, W3),
    "aerial-grounds":  ("airbnb/ab63", None, W3),
    "veranda-flowers": ("airbnb/ab13", None, W2),
    "cabin-exterior":  ("airbnb/ab58", None, W3),
    "cabin-bedroom":   ("airbnb/ab10", None, W2),
    "cabin-mezzanine": ("airbnb/ab37", None, W2),
    "cabin-bath":      ("airbnb/ab45", None, W2),
    "wing-exterior":   ("airbnb/ab47", None, W3),
    "wing-bedroom":    ("airbnb/ab06", None, W2),
    "wing-bedroom-2":  ("airbnb/ab32", None, W2),
    "kitchen":         ("airbnb/ab09", None, W3),
    "alfresco":        ("airbnb/ab01", None, W2),
    "living":          ("airbnb/ab07", None, W2),
    "karaoke":         ("airbnb/ab20", None, W2),
    "pool":            ("airbnb/ab02", None, W3),
    "pool-2":          ("airbnb/ab90", None, W2),
    "pines":           ("airbnb/ab83", None, W3),
    "pines-2":         ("airbnb/ab70", None, W2),
    "bonfire":         ("airbnb/ab89", None, W3),
    "bonfire-2":       ("airbnb/ab84", None, W2),
    "hammock":         ("airbnb/ab51", None, W2),
    "hammock-cottage": ("airbnb/ab66", None, W2),
    "fishpond":        ("airbnb/ab72", None, W2),
    "fishpond-aerial": ("airbnb/ab62", None, W2),
    "court":           ("airbnb/ab76", None, W2),
    "bikes":           ("airbnb/ab59", None, W2),
    "pavilion-sunset": ("airbnb/ab75", None, W3),
    "pavilion":        ("airbnb/ab85", None, W3),
    "camping":         ("airbnb/ab69", None, W2),
    "gate":            ("airbnb/ab15", None, W2),
    "path":            ("airbnb/ab65", None, W2),
    "bougainvillea":   ("airbnb/ab73", None, W2),
    "mountain-view":   ("airbnb/ab71", None, W2),
    "garden-arch":     ("airbnb/ab48", None, W2),
    "mango-lawn":      ("airbnb/ab54", None, W2),
    "veranda-dining":  ("airbnb/ab04", None, W2),
    # stock (Unsplash, free licence) - light touch only
    "near-cove":       ("stock/unsplash-Yf-1Exqwkxs", None, W2),
    # "near-bangka" (unsplash-tPRgXGLX0-M) downloaded but not used
    "near-island":     ("stock/unsplash-LmrGU2tVWLo", None, W2),
    "near-beach":      ("stock/unsplash-8mzOhT8cDlo", None, W2),
}


def find_src(stem):
    base = os.path.join(SRC, stem)
    for ext in (".jpeg", ".jpg", ".png", ".webp"):
        if os.path.exists(base + ext):
            return base + ext
    raise FileNotFoundError(stem)


NIGHT = {"bonfire", "bonfire-2"}


def enhance(img_rgb: np.ndarray, stock=False, night=False) -> np.ndarray:
    # NOTE: an automatic gray-world white balance was tried first and removed:
    # it stripped the natural warmth of timber interiors and firelight.
    img = img_rgb.copy()
    # 1. denoise (stronger for low-light phone shots)
    if not stock:
        h = 6 if night else 3
        img = cv2.fastNlMeansDenoisingColored(img, None, h, h + 1, 7, 21)
    # 2. local contrast, lightly blended
    lab = cv2.cvtColor(img, cv2.COLOR_RGB2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=1.3, tileGridSize=(8, 8))
    l2 = clahe.apply(l)
    l = cv2.addWeighted(l, 0.7, l2, 0.3, 0)
    # 3. a touch of warmth (b channel toward yellow)
    if not stock and not night:
        b = cv2.add(b, 1)
    img = cv2.cvtColor(cv2.merge([l, a, b]), cv2.COLOR_LAB2RGB)
    return img


def main():
    only = set(sys.argv[1:])
    for name, (stem, crop, widths) in MAP.items():
        if only and name not in only:
            continue
        path = find_src(stem)
        im = Image.open(path).convert("RGB")
        if crop:
            w, h = im.size
            im = im.crop((int(crop[0]*w), int(crop[1]*h), int(crop[2]*w), int(crop[3]*h)))
        arr = enhance(np.array(im), stock=stem.startswith("stock"), night=name in NIGHT)
        im = Image.fromarray(arr)
        # gentle saturation trim to keep phone HDR from looking neon
        if name not in NIGHT:
            im = ImageEnhance.Color(im).enhance(0.95)
        sw, sh = im.size
        for w in widths:
            tw = w  # sources are 2400-2560px wide, so this only ever downsizes
            if sw < w:
                print(f"  ! {name}: source {sw}px < {w}px, Lanczos upscale")
            th = round(sh * tw / sw)
            r = im.resize((tw, th), Image.LANCZOS)
            r = r.filter(ImageFilter.UnsharpMask(radius=1.1, percent=55 if tw < 1000 else 70, threshold=2))
            q = 68 if name in NIGHT else 74
            r.save(os.path.join(OUT, f"{name}-{w}.webp"), "WEBP", quality=q, method=6)
            r.save(os.path.join(OUT, f"{name}-{w}.jpg"), "JPEG", quality=q + 4, optimize=True, progressive=True)
        print(f"{name:18s} <- {os.path.basename(path)} {sw}x{sh}")

    # logo: the full plaque (their FB profile image) for the footer, unaltered apart from resizing
    logo = Image.open(os.path.join(SRC, "fb-logo.jpg")).convert("RGB")
    plaque = logo.resize((320, 320), Image.LANCZOS)
    plaque.save(os.path.join(OUT, "logo-plaque-320.webp"), "WEBP", quality=86)
    plaque.save(os.path.join(OUT, "logo-plaque-320.jpg"), quality=86)
    # favicon / touch icon: circular crop of the hut-and-hammock emblem only
    cx, cy, r = 388, 378, 140
    box = logo.crop((cx - r, cy - r, cx + r, cy + r)).resize((512, 512), Image.LANCZOS)
    mask = Image.new("L", (512, 512), 0)
    from PIL import ImageDraw
    ImageDraw.Draw(mask).ellipse((0, 0, 511, 511), fill=255)
    badge = Image.new("RGBA", (512, 512), (0, 0, 0, 0))
    badge.paste(box, (0, 0), mask)
    badge.resize((180, 180), Image.LANCZOS).save(os.path.join(ROOT, "apple-touch-icon.png"))
    badge.resize((48, 48), Image.LANCZOS).save(os.path.join(ROOT, "favicon.png"))
    # social share image
    og = Image.open(os.path.join(OUT, "hero-1280.jpg"))
    og = og.resize((1200, round(og.height * 1200 / og.width)), Image.LANCZOS)
    top = max(0, (og.height - 630) // 2)
    og.crop((0, top, 1200, top + 630)).save(os.path.join(OUT, "og-image.jpg"), quality=82)
    print("logo + favicon + og done")


if __name__ == "__main__":
    main()
