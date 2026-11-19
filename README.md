# Balai Taltalon Nature Resort: website concept

A static concept site in plain HTML, CSS and JS for Balai Taltalon Nature Resort, San Antonio, Zambales.
It's built for GitHub Pages at `https://lendezstudio.github.io/Balai-Taltalon/`.

## Structure

```
index.html              built page (generated, don't edit by hand)
src/index.template.html page source with {{img ...}} tokens
css/style.css           all styles (mobile-first)
js/main.js              menu, reveal, lightbox, ready-made inquiry message
assets/img/             web images (WebP + JPG, 640/1280/1920)
assets/originals/       untouched source photos and logo
assets/SOURCES.md       where every image came from
tools/process_images.py photo clean-up + export
tools/build.py          expands image tokens into <picture> tags
DESIGN-BRIEF.md         research and design direction
```

## Editing

1. Edit `src/index.template.html`, `css/style.css` or `js/main.js`.
2. Rebuild the page with `python tools/build.py`. This needs Pillow.
3. To add or change photos, add an entry to `MAP` in `tools/process_images.py` and run `python tools/process_images.py <name>`.

Local tools live in `.tools/`, a Python venv with Pillow and OpenCV. It's git-ignored.

Preview locally: `python -m http.server 8765`, then open http://127.0.0.1:8765/

## Notes

- There's no booking engine or payment flow. Every call to action goes to Messenger, a phone call, an SMS, or the listings on Airbnb, Booking.com and Agoda.
- Details that are guessed or need confirming are marked with HTML comments in `src/index.template.html`.
