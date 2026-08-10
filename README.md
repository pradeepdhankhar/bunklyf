# bunklyf.com

The bunklyf landing page. Static HTML, no build step, no dependencies — GitHub Pages serves these files exactly as they are.

## What's in here

```
index.html            the landing page (all CSS and JS inline)
404.html              not-found page, served automatically by GitHub Pages
CNAME                 tells GitHub Pages to serve the site at bunklyf.com
.nojekyll             stops Jekyll from touching the files
robots.txt            allows crawling, points to the sitemap
sitemap.xml           one entry, for the home page
site.webmanifest      name, colours and icons for "add to home screen"
make_assets.py        regenerates the icons and social image (optional, see below)
assets/
  favicon.svg         scalable favicon: the tilted k from the wordmark
  favicon-16.png      browser tab
  favicon-32.png      browser tab, retina
  apple-touch-icon.png  180px, iOS home screen
  icon-192.png        manifest icon
  icon-512.png        manifest icon
  icon-maskable-512.png  Android adaptive icon, with safe-zone padding
  og-image.png        1200x630 social preview card
  og-image.svg        the source for the above
  zooroll/            zooRoll's mark and character, SVG plus a PNG set
```

## Putting it live

**1. Create the repo.** Name it anything — `bunklyf-site` is fine. It does *not* need to be named `bunklyf.github.io` since you're using a custom domain.

**2. Push these files to the root of the `main` branch.** Not into a subfolder. `index.html` must sit at the top level.

```bash
git init
git add .
git commit -m "bunklyf landing page"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/bunklyf-site.git
git push -u origin main
```

**3. Turn on Pages.** Repo → **Settings → Pages** → under *Build and deployment*, set **Source: Deploy from a branch**, **Branch: `main`**, **Folder: `/ (root)`**. Save. First deploy takes a minute or two.

**4. Point the domain at GitHub.** In your DNS provider (wherever you bought bunklyf.com), add these records:

| Type  | Name  | Value |
|-------|-------|-------|
| A     | `@`   | `185.199.108.153` |
| A     | `@`   | `185.199.109.153` |
| A     | `@`   | `185.199.110.153` |
| A     | `@`   | `185.199.111.153` |
| CNAME | `www` | `YOUR-USERNAME.github.io.` |

Delete any existing A records on `@` first, or they'll conflict.

**5. Set the custom domain.** Back in **Settings → Pages**, enter `bunklyf.com` under *Custom domain*. The `CNAME` file in this repo already says so, so it should populate itself. Wait for the DNS check to pass (minutes to a few hours), then tick **Enforce HTTPS**.

## Before you announce it

Three things in `index.html` are still placeholders:

1. **Chrome Web Store links.** Search the file for `href="#"` — every "Add to Chrome" and "How it works" button needs a real URL. There's a `TODO` comment marking the first one.
2. **The product copy.** I wrote the descriptions from the app names alone. zooRoll's especially may not match what it actually does — rewrite the paragraph in each `<article class="app">`.
3. **The email form.** It validates the address but sends nowhere. Point it at Buttondown, Mailchimp, ConvertKit, or a Google Form — most of them give you an `action` URL you can drop straight onto the `<form>` tag. The JavaScript handler at the bottom of the file intercepts submits, so delete that listener once a real endpoint is wired up.

Also worth doing: replace `hello@bunklyf.com` in the footer if that isn't your address, and add real Privacy and Terms pages — the Chrome Web Store asks for a privacy policy URL when you publish an extension.

## Adding the fourth app

The design expects to grow. When something new ships:

1. **Crew lineup** — find `<span class="member ghost">` in the `#crew` section and swap one ghost for a real character. Copy the structure of an existing `<button class="member">`: it needs `data-go="#your-app-id"`, a `<svg class="toon">`, and a `<span class="tag">` with the name. Give the eyes a `data-eye` group with a `.pupil` circle inside and the cursor-tracking works automatically.
2. **Product card** — copy an `<article class="app">` block, change the `id`, art, and copy. Add a `.app:nth-child(4) .app-art{background:var(--sun);}` rule so the tile gets its own colour.
3. **The shelf** — delete the matching `.slot` in `#next`, or renumber the rest.

## Regenerating the icons

Only needed if you want to change colours or shapes. Requires Python with `cairosvg`, plus the Bricolage Grotesque and DM Mono fonts installed locally for the social image text.

```bash
pip install cairosvg
python3 make_assets.py
```

## Colours

| Token     | Hex       | Used for |
|-----------|-----------|----------|
| `--ink`   | `#1B1033` | text, every outline |
| `--paper` | `#FFF1D6` | background |
| `--pop`   | `#FF4D6D` | primary accent, buttons |
| `--zap`   | `#2ED3B7` | crew band, EyeWise |
| `--sun`   | `#FFC93C` | highlights, favicon |
| `--grape` | `#7B4BFF` | workshop section |
| `--zoo`   | `#8348D6` | zooRoll's brand purple, from its icon |

Type: **Bricolage Grotesque** (display), **Instrument Sans** (body), **DM Mono** (labels), all loaded from Google Fonts.
