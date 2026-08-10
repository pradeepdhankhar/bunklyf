import cairosvg, re

INK    = "#1B1033"
PAPER  = "#FFF1D6"
POP    = "#FF4D6D"
ZAP    = "#2ED3B7"
SUN    = "#FFC93C"
ZOO    = "#8348D6"
LILAC  = "#CFC3F2"
LILAC2 = "#B9A7E8"

# ---------------------------------------------------------------- favicon ---
# The wordmark's tilted "k", drawn as geometry so it needs no font to render.
FAVICON = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect width="64" height="64" rx="15" fill="{INK}"/>
  <g transform="rotate(-13 32 34)" fill="none" stroke="{SUN}" stroke-width="8"
     stroke-linecap="round" stroke-linejoin="round">
    <path d="M23 12 L23 51"/>
    <path d="M45 24 L23 38 L47 52"/>
  </g>
</svg>'''

# ------------------------------------------------------------- characters ---
ZOOROLL_BLOOM = ("M60.0 44.0L64.3 43.9L66.5 43.1L68.2 41.6L71.5 37.5L74.6 31.3L77.3 24.5L73.5 18.3"
  "L65.9 22.5L60.0 14.0L54.1 22.5L46.5 18.3L42.7 24.5L45.4 31.3L48.5 37.5L51.8 41.6L53.5 43.1"
  "L55.7 43.9ZM73.8 52.0L76.1 55.7L77.9 57.2L80.1 57.9L85.3 58.7L92.2 58.3L99.4 57.2L102.9 50.9"
  "L95.4 46.4L99.8 37.0L89.5 36.1L89.3 27.4L82.1 27.3L77.5 33.0L73.8 38.8L71.9 43.7L71.4 45.9"
  "L71.8 48.2ZM73.8 68.0L71.8 71.8L71.4 74.1L71.9 76.3L73.8 81.2L77.5 87.0L82.1 92.7L89.3 92.6"
  "L89.5 83.9L99.8 83.0L95.4 73.6L102.9 69.1L99.4 62.8L92.2 61.7L85.3 61.3L80.1 62.1L77.9 62.8"
  "L76.1 64.3ZM60.0 76.0L55.7 76.1L53.5 76.9L51.8 78.4L48.5 82.5L45.4 88.7L42.7 95.5L46.5 101.7"
  "L54.1 97.5L60.0 106.0L65.9 97.5L73.5 101.7L77.3 95.5L74.6 88.7L71.5 82.5L68.2 78.4L66.5 76.9"
  "L64.3 76.1ZM46.2 68.0L43.9 64.3L42.1 62.8L39.9 62.1L34.7 61.3L27.8 61.7L20.6 62.8L17.1 69.1"
  "L24.6 73.6L20.2 83.0L30.5 83.9L30.7 92.6L37.9 92.7L42.5 87.0L46.2 81.2L48.1 76.3L48.6 74.1"
  "L48.2 71.8ZM46.2 52.0L48.2 48.2L48.6 45.9L48.1 43.7L46.2 38.8L42.5 33.0L37.9 27.3L30.7 27.4"
  "L30.5 36.1L20.2 37.0L24.6 46.4L17.1 50.9L20.6 57.2L27.8 58.3L34.7 58.7L39.9 57.9L42.1 57.2"
  "L43.9 55.7Z")

ZOOROLL = f'''<path d="{ZOOROLL_BLOOM}" fill="{ZOO}" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>
<circle cx="60" cy="60" r="21" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>
<circle cx="52" cy="57.5" r="6.6" fill="{PAPER}" stroke="{INK}" stroke-width="3.4"/>
<circle cx="52" cy="57.5" r="3" fill="{INK}"/>
<circle cx="68" cy="57.5" r="6.6" fill="{PAPER}" stroke="{INK}" stroke-width="3.4"/>
<circle cx="68" cy="57.5" r="3" fill="{INK}"/>
<path d="M52.5 69.5 Q60 76 67.5 69.5" fill="none" stroke="{INK}" stroke-width="3.6" stroke-linecap="round"/>'''

EYEWISE = f'''<rect x="14" y="26" width="92" height="80" rx="26" fill="{ZAP}" stroke="{INK}" stroke-width="5"/>
<path d="M40 26 L36 8 M80 26 L86 10" stroke="{INK}" stroke-width="5" stroke-linecap="round"/>
<circle cx="36" cy="8" r="5" fill="{POP}" stroke="{INK}" stroke-width="4"/>
<circle cx="86" cy="10" r="5" fill="{POP}" stroke="{INK}" stroke-width="4"/>
<ellipse cx="60" cy="62" rx="30" ry="22" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>
<circle cx="60" cy="62" r="10.5" fill="{INK}"/>
<path d="M42 92 Q60 100 78 92" fill="none" stroke="{INK}" stroke-width="4.5" stroke-linecap="round"/>'''

KOO = f'''<circle cx="20" cy="46" r="18" fill="{LILAC2}" stroke="{INK}" stroke-width="5"/>
<circle cx="100" cy="46" r="18" fill="{LILAC2}" stroke="{INK}" stroke-width="5"/>
<circle cx="60" cy="64" r="40" fill="{LILAC}" stroke="{INK}" stroke-width="5"/>
<circle cx="46" cy="58" r="9" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>
<circle cx="46" cy="58" r="4" fill="{INK}"/>
<circle cx="74" cy="58" r="9" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>
<circle cx="74" cy="58" r="4" fill="{INK}"/>
<ellipse cx="60" cy="76" rx="13" ry="10" fill="{INK}"/>
<path d="M52 92 Q60 98 68 92" fill="none" stroke="{INK}" stroke-width="4.5" stroke-linecap="round"/>'''

def toon(body, x, y, scale, rot=0):
    return (f'<g transform="translate({x},{y}) scale({scale}) rotate({rot} 60 60)">{body}</g>')

# --------------------------------------------------------- social preview ---
DOTS = (f'<pattern id="dots" width="26" height="26" patternUnits="userSpaceOnUse">'
        f'<circle cx="2" cy="2" r="1.6" fill="{INK}" opacity="0.13"/></pattern>')

OG = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630">
<defs>{DOTS}</defs>
<rect width="1200" height="630" fill="{PAPER}"/>
<rect width="1200" height="630" fill="url(#dots)"/>
<rect x="0" y="0" width="1200" height="18" fill="{INK}"/>
<rect x="0" y="612" width="1200" height="18" fill="{INK}"/>

<text x="80" y="145" font-family="DM Mono" font-size="26" letter-spacing="5" fill="{INK}">BUNKLYF.COM</text>
<text x="76" y="270" font-family="Bricolage Grotesque" font-weight="800" font-size="80"
      letter-spacing="-4" fill="{INK}">We make small</text>
<text x="76" y="360" font-family="Bricolage Grotesque" font-weight="800" font-size="80"
      letter-spacing="-4" fill="{INK}">things that make</text>
<text x="76" y="450" font-family="Bricolage Grotesque" font-weight="800" font-size="80"
      letter-spacing="-4" fill="{POP}">big days easier.</text>
<text x="80" y="556" font-family="DM Mono" font-size="26" fill="{INK}">zooRoll  ·  EyeWise  ·  Koo the Koala  ·  more in the oven</text>

{toon(ZOOROLL, 870, 95, 1.55, -8)}
{toon(EYEWISE, 715, 300, 1.15, 5)}
{toon(KOO, 950, 320, 1.15, -4)}
</svg>'''

# ------------------------------------------------------------------ write ---
open("assets/favicon.svg", "w").write(FAVICON)
open("assets/og-image.svg", "w").write(OG)

for size, name in ((16, "favicon-16.png"), (32, "favicon-32.png"),
                   (180, "apple-touch-icon.png"), (192, "icon-192.png"),
                   (512, "icon-512.png")):
    cairosvg.svg2png(url="assets/favicon.svg", write_to="assets/" + name,
                     output_width=size, output_height=size)

cairosvg.svg2png(url="assets/og-image.svg", write_to="assets/og-image.png",
                 output_width=1200, output_height=630)

# maskable icon: same k on ink, with safe-zone padding for Android
MASK = FAVICON.replace('viewBox="0 0 64 64"', 'viewBox="-10 -10 84 84"').replace('rx="15"', 'rx="0"')
MASK = MASK.replace('<rect width="64" height="64"', '<rect x="-10" y="-10" width="84" height="84"')
open("assets/icon-maskable.svg", "w").write(MASK)
cairosvg.svg2png(url="assets/icon-maskable.svg", write_to="assets/icon-maskable-512.png",
                 output_width=512, output_height=512)

print("assets built")
