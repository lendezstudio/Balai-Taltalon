# Asset sources

All photos of the property are **Balai Taltalon's own**, published by the host on their Airbnb listings. Downloaded 19 Nov 2026 at the largest size Airbnb serves (2560px wide; Airbnb's CDN upscales from about 1200px, so the 1920px exports are slightly upscaled).

- Airbnb listing A, *Villa and Guest Wing*: https://www.airbnb.com/rooms/1642751418516243443
- Airbnb listing B, *Villa and Pool*: https://www.airbnb.com/rooms/1657266934878093132
- Logo: the public Facebook profile picture of https://www.facebook.com/balaitaltalonnatureresort/ (`originals/fb-logo.jpg`)

## Processing

`tools/process_images.py` applies light denoising, mild local contrast (CLAHE on the L channel, 30% blend), a slight warmth shift, a 5% saturation trim (none on night shots), Lanczos resizing and an unsharp mask. It exports WebP and JPG at 640, 1280 and 1920 widths into `assets/img/`. Nothing is added or removed from any scene: no sky swaps and no retouching of the property.

**Overlays:** none of the photos used on the site had text, stickers or frames, so no inpainting was needed. These images were **not used** because their overlays can't be removed cleanly or they aren't photographs:
- `ab16`: promo poster with logo, phone numbers and icons
- `ab64`: illustrated location map (a graphic, not a photo)
- `ab55`, `ab80`: guest faces covered by emoji stickers
- Facebook promo posters (rate and tagline graphics) were not downloaded

## Photos used on the site

| Web name (`assets/img/`) | Original file | Source |
|---|---|---|
| alfresco | `originals/airbnb/ab01.jpeg` | Airbnb listing B (Villa+Pool listing cover): https://a0.muscache.com/im/pictures/hosting/Hosting-1657266934878093132/original/c16cab14-ff41-4e17-b283-04a795b60689.jpeg |
| pool | `originals/airbnb/ab02.jpeg` | Airbnb listing A: https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/898034f0-cde7-4a2b-87f4-d3a4b9c99c0e.jpeg |
| veranda-dining | `originals/airbnb/ab04.jpeg` | Airbnb listing A: https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/ca99ff80-bbfc-4a77-b0f0-aaa9c7ba3430.jpeg |
| wing-bedroom | `originals/airbnb/ab06.jpeg` | Airbnb listing A: https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/f9d15a42-24fd-46d4-b386-96e7b301be05.jpeg |
| living | `originals/airbnb/ab07.jpeg` | Airbnb listing A (Living room 1): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/ecd38dd9-f6a6-4664-9026-ffc2e4abd7af.jpeg |
| kitchen | `originals/airbnb/ab09.jpeg` | Airbnb listing A (Alfresco dining area): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/372f43e0-5cdf-4086-b1b5-e059dba0104b.jpeg |
| cabin-bedroom | `originals/airbnb/ab10.jpeg` | Airbnb listing A (Bedroom 2 1): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/3841cd49-3112-4e01-bd59-7186639ec6b4.jpeg |
| veranda-flowers | `originals/airbnb/ab13.png` | Airbnb listing A (Exterior 1 1): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/f86bc5d7-34e1-46ad-8e1e-a0ca3af26220.png |
| gate | `originals/airbnb/ab15.png` | Airbnb listing A (Exterior 3 1): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/29a094ab-76c9-4f7a-90b0-71f6e754bc0c.png |
| karaoke | `originals/airbnb/ab20.jpeg` | Airbnb listing A (Living room 5): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/00f8b388-dae8-4e64-bafa-8d0b011c27d4.jpeg |
| wing-bedroom-2 | `originals/airbnb/ab32.jpeg` | Airbnb listing A (Bedroom 1 8): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/188de14a-b229-4464-8117-4c67cd46d5dc.jpeg |
| cabin-mezzanine | `originals/airbnb/ab37.jpeg` | Airbnb listing A (Bedroom 3 2): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/0743aa68-aeab-47be-b135-be7054b8bdcb.jpeg |
| cabin-bath | `originals/airbnb/ab45.jpeg` | Airbnb listing A (Full bathroom 2 3): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/557ce9f1-f400-4601-9d94-5b72454640b8.jpeg |
| wing-exterior | `originals/airbnb/ab47.jpeg` | Airbnb listing A (Exterior 1 3): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/20b36ccf-9661-4b71-9e64-883e01318992.jpeg |
| garden-arch | `originals/airbnb/ab48.jpeg` | Airbnb listing A (Exterior 1 4): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/53890e09-20af-4112-a524-659273bd1def.jpeg |
| hammock | `originals/airbnb/ab51.jpeg` | Airbnb listing A (Exterior 1 8): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/072c42c8-775e-44e1-ac23-5a2c36cdf76c.jpeg |
| mango-lawn | `originals/airbnb/ab54.jpeg` | Airbnb listing A (Exterior 1 10): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/3af7a125-c449-465f-a615-f4b84c53f8a6.jpeg |
| cabin-exterior | `originals/airbnb/ab58.jpeg` | Airbnb listing A (Exterior 1 14): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/84115480-5311-4aac-a65c-54914ff55234.jpeg |
| bikes | `originals/airbnb/ab59.jpeg` | Airbnb listing A (Exterior 1 15): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/56b941eb-f9e0-4b0d-9950-3a3794771d9e.jpeg |
| hero | `originals/airbnb/ab60.png` | Airbnb listing A (Exterior 2 2): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/482617db-98fd-42db-b49c-603459ef7163.png |
| fishpond-aerial | `originals/airbnb/ab62.png` | Airbnb listing A (Exterior 2 4): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/4d65f075-5a82-4c94-950e-ab27a1df4af0.png |
| aerial-grounds | `originals/airbnb/ab63.png` | Airbnb listing A (Exterior 2 6): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/413aaff0-5d0b-4c7e-b147-26a8632cff27.png |
| path | `originals/airbnb/ab65.png` | Airbnb listing A (Exterior 3 2): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/8a739c06-1475-4344-996e-ebd71742083b.png |
| hammock-cottage | `originals/airbnb/ab66.jpeg` | Airbnb listing A (Cottages by the fishpond): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/0df20461-2673-400d-8c0d-ac9b370e86af.jpeg |
| camping | `originals/airbnb/ab69.png` | Airbnb listing A (Exterior 3 6): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/04c81d0e-673e-411d-ab68-9e557e203a0c.png |
| pines-2 | `originals/airbnb/ab70.jpeg` | Airbnb listing A (Exterior 3 7): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/31b9a861-b9fc-442d-96d7-daae52fd6c2c.jpeg |
| mountain-view | `originals/airbnb/ab71.jpeg` | Airbnb listing A (Exterior 3 8): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/a4a8d1a2-04b2-4497-8040-75e301a25349.jpeg |
| fishpond | `originals/airbnb/ab72.png` | Airbnb listing A (Exterior 3 9): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/f332affb-ffed-4223-ba51-4caa500ebca1.png |
| bougainvillea | `originals/airbnb/ab73.jpeg` | Airbnb listing A (Exterior 3 10): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/2989c73e-3bd2-44e2-8ea2-9182ffa5223b.jpeg |
| pavilion-sunset | `originals/airbnb/ab75.png` | Airbnb listing A (Exterior 3 12): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/fa596fbe-96a3-416a-bf94-b2cffc3aff8e.png |
| court | `originals/airbnb/ab76.jpeg` | Airbnb listing A (Exterior 3 13): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/b8219af9-c815-4206-9181-2c41c52acf02.jpeg |
| pines | `originals/airbnb/ab83.jpeg` | Airbnb listing A (Exterior 3 19): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/0097b5ee-ec34-4208-bf5a-290b264dde73.jpeg |
| bonfire-2 | `originals/airbnb/ab84.jpeg` | Airbnb listing A (Exterior 3 21): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/e9dbc809-adb3-4717-8336-247949242d35.jpeg |
| pavilion | `originals/airbnb/ab85.png` | Airbnb listing A (Exterior 3 22): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/1b33706e-d84d-421a-9591-111923517dab.png |
| bonfire | `originals/airbnb/ab89.png` | Airbnb listing A (Exterior 3 25): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/f9b175c0-964b-4292-93fd-248e8de4be63.png |
| pool-2 | `originals/airbnb/ab90.jpeg` | Airbnb listing A (Pool 2): https://a0.muscache.com/im/pictures/hosting/Hosting-1642751418516243443/original/6862fd9c-a454-4021-9e7b-bc3785cb223f.jpeg |

## Stock photos (gap fill: Explore nearby)

Free to use under the Unsplash License (https://unsplash.com/license). Attribution isn't required but is given here. All are tagged *Zambales* on Unsplash. No photos come from the reference site, competitors or other websites.

| Web name | Original file | Photographer | Source |
|---|---|---|---|
| near-cove | `originals/stock/unsplash-Yf-1Exqwkxs.jpg` | Lyndon Jeff Ebue (@jeffebue) | https://unsplash.com/photos/Yf-1Exqwkxs |
| near-bangka *(downloaded, not currently used)* | `originals/stock/unsplash-tPRgXGLX0-M.jpg` | @jeffebue | https://unsplash.com/photos/tPRgXGLX0-M |
| near-island | `originals/stock/unsplash-LmrGU2tVWLo.jpg` | @_extramile | https://unsplash.com/photos/LmrGU2tVWLo |
| near-beach | `originals/stock/unsplash-8mzOhT8cDlo.jpg` | @johnwolf3 | https://unsplash.com/photos/8mzOhT8cDlo |

## Other originals

`originals/airbnb/` holds the full set of 90 listing photos (`ab01` to `ab90`), and `originals/_airbnb_list.txt` maps each one to its URL and Airbnb room label. Only the files listed above appear on the site.

## Videos

No video is used. The only video found was a Facebook "Video and Pictures Tour" post. Downloading it would need Facebook's own tools, and it doesn't add enough over the photos. It can be added later as a lazy-loaded embed if Balai wants it.
