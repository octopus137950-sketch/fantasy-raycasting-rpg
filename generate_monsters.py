#!/usr/bin/env python3
"""Generate pixel-art style monster icons as SVG -> PNG using ImageMagick."""
import subprocess, os, sys

OUT = os.path.join(os.path.dirname(__file__), "images")
os.makedirs(OUT, exist_ok=True)

def hex_to_rgb(h):
    h = h.lstrip('#')
    return f"rgb({int(h[0:2],16)},{int(h[2:4],16)},{int(h[4:6],16)})"

def darken(h, f=0.6):
    h = h.lstrip('#')
    r, g, b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    r, g, b = int(r*f), int(g*f), int(b*f)
    return f"rgb({r},{g},{b})"

def lighten(h, f=1.3):
    h = h.lstrip('#')
    r, g, b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    r, g, b = min(255,int(r*f)), min(255,int(g*f)), min(255,int(b*f))
    return f"rgb({r},{g},{b})"

def svg_wrap(content, bg="rgba(0,0,0,0)"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">
<rect width="64" height="64" fill="{bg}"/>
{content}
</svg>'''

# Each monster: (id, color, svg_inner)
monsters = []

def m(id, color, svg):
    monsters.append((id, color, svg))

# --- TIER 1 ---

m("slime", "#44ddff", '''
<ellipse cx="32" cy="40" rx="22" ry="18" fill="{c}" stroke="#116688" stroke-width="2"/>
<circle cx="25" cy="36" r="4" fill="#fff"/><circle cx="25" cy="36" r="2" fill="#000"/>
<circle cx="39" cy="36" r="4" fill="#fff"/><circle cx="39" cy="36" r="2" fill="#000"/>
<path d="M24 46 Q32 52 40 46" fill="none" stroke="#116688" stroke-width="2" stroke-linecap="round"/>
<ellipse cx="32" cy="26" rx="10" ry="4" fill="{lc}" opacity="0.5"/>
''')

m("slime_ice", "#aaeeff", '''
<ellipse cx="32" cy="40" rx="22" ry="18" fill="{c}" stroke="#4488aa" stroke-width="2"/>
<circle cx="25" cy="36" r="4" fill="#fff"/><circle cx="25" cy="36" r="2" fill="#000"/>
<circle cx="39" cy="36" r="4" fill="#fff"/><circle cx="39" cy="36" r="2" fill="#000"/>
<path d="M24 46 Q32 52 40 46" fill="none" stroke="#4488aa" stroke-width="2" stroke-linecap="round"/>
<polygon points="20,24 24,20 28,24 24,28" fill="#fff" opacity="0.7"/>
<polygon points="38,22 42,18 46,22 42,26" fill="#fff" opacity="0.7"/>
''')

m("wolf", "#889999", '''
<path d="M14 30 L14 20 L20 24 L32 18 L44 24 L50 20 L50 30 L48 44 Q32 52 16 44 Z" fill="{c}" stroke="#445566" stroke-width="2"/>
<polygon points="14,20 10,12 18,18" fill="{c}" stroke="#445566" stroke-width="1.5"/>
<polygon points="50,20 54,12 46,18" fill="{c}" stroke="#445566" stroke-width="1.5"/>
<circle cx="25" cy="32" r="3" fill="#ffcc00"/><circle cx="39" cy="32" r="3" fill="#ffcc00"/>
<circle cx="25" cy="32" r="1.5" fill="#000"/><circle cx="39" cy="32" r="1.5" fill="#000"/>
<path d="M28 40 L32 44 L36 40" fill="#221100" stroke="#221100" stroke-width="1.5" stroke-linecap="round"/>
<path d="M30 42 L32 46 L34 42" fill="none" stroke="#221100" stroke-width="1.5"/>
''')

m("bat", "#553355", '''
<ellipse cx="32" cy="34" rx="12" ry="14" fill="{c}" stroke="#221122" stroke-width="2"/>
<path d="M20 30 Q8 18 4 30 Q8 36 20 34 Z" fill="{c}" stroke="#221122" stroke-width="2"/>
<path d="M44 30 Q56 18 60 30 Q56 36 44 34 Z" fill="{c}" stroke="#221122" stroke-width="2"/>
<polygon points="24,22 22,16 28,20" fill="{c}" stroke="#221122" stroke-width="1.5"/>
<polygon points="40,22 42,16 36,20" fill="{c}" stroke="#221122" stroke-width="1.5"/>
<circle cx="27" cy="32" r="3" fill="#ff3333"/><circle cx="37" cy="32" r="3" fill="#ff3333"/>
<circle cx="27" cy="32" r="1.5" fill="#000"/><circle cx="37" cy="32" r="1.5" fill="#000"/>
<path d="M28 40 L30 42 L32 40 L34 42 L36 40" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round"/>
''')

m("goblin", "#44aa44", '''
<ellipse cx="32" cy="36" rx="16" ry="18" fill="{c}" stroke="#226622" stroke-width="2"/>
<polygon points="18,24 12,16 22,22" fill="{c}" stroke="#226622" stroke-width="1.5"/>
<polygon points="46,24 52,16 42,22" fill="{c}" stroke="#226622" stroke-width="1.5"/>
<circle cx="26" cy="34" r="4" fill="#fff"/><circle cx="26" cy="34" r="2" fill="#cc0000"/>
<circle cx="38" cy="34" r="4" fill="#fff"/><circle cx="38" cy="34" r="2" fill="#cc0000"/>
<path d="M26 44 L30 42 L32 44 L34 42 L38 44" fill="none" stroke="#226622" stroke-width="2" stroke-linecap="round"/>
<rect x="28" y="46" width="3" height="4" fill="#fff" rx="1"/>
<rect x="33" y="46" width="3" height="4" fill="#fff" rx="1"/>
''')

m("bird", "#66ccff", '''
<ellipse cx="32" cy="34" rx="14" ry="16" fill="{c}" stroke="#3388bb" stroke-width="2"/>
<path d="M18 30 Q8 24 6 32 Q12 36 20 34 Z" fill="{c}" stroke="#3388bb" stroke-width="2"/>
<path d="M46 30 Q56 24 58 32 Q52 36 44 34 Z" fill="{c}" stroke="#3388bb" stroke-width="2"/>
<polygon points="32,18 28,10 36,10" fill="{c}" stroke="#3388bb" stroke-width="1.5"/>
<polygon points="32,42 28,50 36,50" fill="{dd}" stroke="#3388bb" stroke-width="1.5"/>
<circle cx="27" cy="32" r="3" fill="#fff"/><circle cx="27" cy="32" r="1.5" fill="#000"/>
<circle cx="37" cy="32" r="3" fill="#fff"/><circle cx="37" cy="32" r="1.5" fill="#000"/>
<polygon points="30,40 32,46 34,40" fill="#ff9900" stroke="#cc6600" stroke-width="1"/>
''')

m("turtle", "#669955", '''
<ellipse cx="32" cy="38" rx="20" ry="14" fill="{dd}" stroke="#334422" stroke-width="2"/>
<polygon points="32,24 18,30 18,42 32,48 46,42 46,30" fill="{c}" stroke="#334422" stroke-width="2"/>
<line x1="32" y1="24" x2="32" y2="48" stroke="#334422" stroke-width="1.5"/>
<line x1="18" y1="30" x2="46" y2="30" stroke="#334422" stroke-width="1.5"/>
<line x1="18" y1="42" x2="46" y2="42" stroke="#334422" stroke-width="1.5"/>
<circle cx="14" cy="36" r="5" fill="{dd}" stroke="#334422" stroke-width="1.5"/>
<circle cx="12" cy="35" r="1.5" fill="#000"/>
<ellipse cx="50" cy="44" rx="4" ry="3" fill="{dd}" stroke="#334422" stroke-width="1"/>
<ellipse cx="50" cy="30" rx="4" ry="3" fill="{dd}" stroke="#334422" stroke-width="1"/>
''')

m("fire_spirit", "#ff6633", '''
<path d="M32 8 Q20 20 22 34 Q18 44 26 50 Q20 52 24 56 Q32 54 32 48 Q32 54 40 56 Q44 52 38 50 Q46 44 42 34 Q44 20 32 8 Z" fill="{c}" stroke="#cc2200" stroke-width="2"/>
<circle cx="27" cy="34" r="3" fill="#fff"/><circle cx="27" cy="34" r="1.5" fill="#000"/>
<circle cx="37" cy="34" r="3" fill="#fff"/><circle cx="37" cy="34" r="1.5" fill="#000"/>
<path d="M28 42 Q32 46 36 42" fill="none" stroke="#cc2200" stroke-width="2" stroke-linecap="round"/>
<circle cx="32" cy="24" r="3" fill="{lc}" opacity="0.6"/>
''')

m("shadow_essence", "#445588", '''
<path d="M32 10 Q14 18 16 34 Q12 48 24 52 Q32 50 32 44 Q32 50 40 52 Q52 48 48 34 Q50 18 32 10 Z" fill="{c}" stroke="#221144" stroke-width="2"/>
<ellipse cx="26" cy="32" rx="4" ry="6" fill="#000"/>
<ellipse cx="38" cy="32" rx="4" ry="6" fill="#000"/>
<circle cx="26" cy="30" r="1.5" fill="{lc}"/>
<circle cx="38" cy="30" r="1.5" fill="{lc}"/>
<path d="M26 42 Q32 46 38 42" fill="none" stroke="#000" stroke-width="2" stroke-linecap="round"/>
''')

m("cat", "#aabb88", '''
<path d="M16 30 L16 22 L22 26 L32 20 L42 26 L48 22 L48 30 L46 42 Q32 50 18 42 Z" fill="{c}" stroke="#667744" stroke-width="2"/>
<polygon points="16,22 12,14 20,20" fill="{c}" stroke="#667744" stroke-width="1.5"/>
<polygon points="48,22 52,14 44,20" fill="{c}" stroke="#667744" stroke-width="1.5"/>
<polygon points="20,18 18,12 24,16" fill="#fff" opacity="0.5"/>
<ellipse cx="26" cy="33" rx="3" ry="5" fill="#ffcc00"/>
<ellipse cx="38" cy="33" rx="3" ry="5" fill="#ffcc00"/>
<circle cx="26" cy="33" r="1.5" fill="#000"/>
<circle cx="38" cy="33" r="1.5" fill="#000"/>
<polygon points="30,40 32,38 34,40 32,42" fill="#ff6699" stroke="#cc3377" stroke-width="1"/>
<path d="M28 42 Q24 44 22 42" fill="none" stroke="#667744" stroke-width="1.5"/>
<path d="M36 42 Q40 44 42 42" fill="none" stroke="#667744" stroke-width="1.5"/>
''')

m("rat", "#997755", '''
<ellipse cx="28" cy="36" rx="16" ry="14" fill="{c}" stroke="#554433" stroke-width="2"/>
<path d="M44 36 Q56 32 58 40 Q54 44 44 40 Z" fill="{dd}" stroke="#554433" stroke-width="2"/>
<circle cx="22" cy="28" r="5" fill="{dd}" stroke="#554433" stroke-width="1.5"/>
<circle cx="34" cy="28" r="5" fill="{dd}" stroke="#554433" stroke-width="1.5"/>
<circle cx="22" cy="28" r="2" fill="{dd}"/>
<circle cx="34" cy="28" r="2" fill="{dd}"/>
<circle cx="24" cy="34" r="2.5" fill="#ff3333"/>
<circle cx="34" cy="34" r="2.5" fill="#ff3333"/>
<circle cx="24" cy="34" r="1" fill="#000"/>
<circle cx="34" cy="34" r="1" fill="#000"/>
<polygon points="30,40 32,44 34,40" fill="#fff" stroke="#554433" stroke-width="1"/>
<path d="M20 42 Q16 44 18 46" fill="none" stroke="{dd}" stroke-width="2"/>
''')

m("mushroom", "#cc4488", '''
<rect x="28" y="34" width="8" height="18" rx="3" fill="#eeddcc" stroke="#aa9988" stroke-width="2"/>
<path d="M12 34 Q12 16 32 14 Q52 16 52 34 Z" fill="{c}" stroke="#882266" stroke-width="2"/>
<circle cx="22" cy="26" r="4" fill="#fff" opacity="0.8"/>
<circle cx="38" cy="24" r="3" fill="#fff" opacity="0.8"/>
<circle cx="42" cy="30" r="2.5" fill="#fff" opacity="0.8"/>
<circle cx="28" cy="30" r="2" fill="#fff" opacity="0.8"/>
<circle cx="26" cy="40" r="1.5" fill="#000"/>
<circle cx="38" cy="40" r="1.5" fill="#000"/>
<path d="M28 46 Q32 48 36 46" fill="none" stroke="#aa9988" stroke-width="1.5"/>
''')

m("bee", "#ffbb00", '''
<ellipse cx="32" cy="34" rx="16" ry="14" fill="{c}" stroke="#cc8800" stroke-width="2"/>
<path d="M16 28 Q6 20 8 30 Q12 34 18 32 Z" fill="{lc}" stroke="#cc8800" stroke-width="1.5" opacity="0.7"/>
<path d="M48 28 Q58 20 56 30 Q52 34 46 32 Z" fill="{lc}" stroke="#cc8800" stroke-width="1.5" opacity="0.7"/>
<rect x="20" y="28" width="4" height="12" fill="#553300" rx="1"/>
<rect x="28" y="28" width="4" height="12" fill="#553300" rx="1"/>
<rect x="36" y="28" width="4" height="12" fill="#553300" rx="1"/>
<rect x="44" y="28" width="4" height="12" fill="#553300" rx="1"/>
<circle cx="26" cy="32" r="3" fill="#000"/><circle cx="26" cy="32" r="1" fill="#fff"/>
<circle cx="38" cy="32" r="3" fill="#000"/><circle cx="38" cy="32" r="1" fill="#fff"/>
<ellipse cx="32" cy="48" rx="4" ry="3" fill="{dd}" stroke="#cc8800" stroke-width="1.5"/>
''')

m("frog", "#44cc66", '''
<ellipse cx="32" cy="40" rx="22" ry="16" fill="{c}" stroke="#228844" stroke-width="2"/>
<circle cx="22" cy="26" r="8" fill="{c}" stroke="#228844" stroke-width="2"/>
<circle cx="42" cy="26" r="8" fill="{c}" stroke="#228844" stroke-width="2"/>
<circle cx="22" cy="26" r="4" fill="#fff"/><circle cx="22" cy="26" r="2" fill="#000"/>
<circle cx="42" cy="26" r="4" fill="#fff"/><circle cx="42" cy="26" r="2" fill="#000"/>
<path d="M22 42 Q32 48 42 42" fill="none" stroke="#228844" stroke-width="2" stroke-linecap="round"/>
<circle cx="26" cy="44" r="1.5" fill="{dd}"/>
<circle cx="38" cy="44" r="1.5" fill="{dd}"/>
''')

# --- TIER 1 LOCKED ---

m("skeleton", "#eeeedd", '''
<circle cx="32" cy="26" r="12" fill="{c}" stroke="#999988" stroke-width="2"/>
<ellipse cx="27" cy="26" rx="3" ry="4" fill="#000"/>
<ellipse cx="37" cy="26" rx="3" ry="4" fill="#000"/>
<path d="M28 32 L30 34 L32 32 L34 34 L36 32" fill="none" stroke="#999988" stroke-width="1.5"/>
<rect x="28" y="38" width="8" height="4" fill="none" stroke="#999988" stroke-width="1.5"/>
<line x1="30" y1="38" x2="30" y2="42" stroke="#999988" stroke-width="1"/>
<line x1="34" y1="38" x2="34" y2="42" stroke="#999988" stroke-width="1"/>
<rect x="22" y="42" width="20" height="14" fill="none" stroke="#999988" stroke-width="2" rx="2"/>
<line x1="27" y1="42" x2="27" y2="56" stroke="#999988" stroke-width="1"/>
<line x1="32" y1="42" x2="32" y2="56" stroke="#999988" stroke-width="1"/>
<line x1="37" y1="42" x2="37" y2="56" stroke="#999988" stroke-width="1"/>
''')

m("plant", "#33aa22", '''
<rect x="28" y="40" width="8" height="16" fill="#8B4513" stroke="#553311" stroke-width="2" rx="2"/>
<path d="M32 40 Q16 30 12 18 Q22 22 32 32 Q42 22 52 18 Q48 30 32 40 Z" fill="{c}" stroke="#117711" stroke-width="2"/>
<circle cx="22" cy="26" r="4" fill="{lc}" opacity="0.7"/>
<circle cx="42" cy="26" r="4" fill="{lc}" opacity="0.7"/>
<circle cx="32" cy="20" r="5" fill="{lc}" opacity="0.7"/>
<circle cx="32" cy="32" r="2" fill="#ff6699"/>
<circle cx="24" cy="28" r="1.5" fill="#ff6699"/>
<circle cx="40" cy="28" r="1.5" fill="#ff6699"/>
''')

m("spider", "#772288", '''
<circle cx="32" cy="34" r="14" fill="{c}" stroke="#440044" stroke-width="2"/>
<circle cx="27" cy="30" r="4" fill="#fff"/><circle cx="27" cy="30" r="2" fill="#000"/>
<circle cx="37" cy="30" r="4" fill="#fff"/><circle cx="37" cy="30" r="2" fill="#000"/>
<path d="M20 28 L8 18 M18 34 L6 32 M18 40 L8 48" stroke="#440044" stroke-width="2.5" stroke-linecap="round" fill="none"/>
<path d="M44 28 L56 18 M46 34 L58 32 M46 40 L56 48" stroke="#440044" stroke-width="2.5" stroke-linecap="round" fill="none"/>
<path d="M28 40 Q32 44 36 40" fill="none" stroke="#440044" stroke-width="2" stroke-linecap="round"/>
<polygon points="30,38 28,34 32,36" fill="#fff"/>
<polygon points="34,38 36,34 32,36" fill="#fff"/>
''')

m("zombie", "#557755", '''
<ellipse cx="32" cy="24" rx="12" ry="10" fill="{c}" stroke="#334433" stroke-width="2"/>
<path d="M18 30 L18 50 Q32 56 46 50 L46 30 Z" fill="{c}" stroke="#334433" stroke-width="2"/>
<rect x="20" y="22" width="6" height="3" fill="#000" rx="1"/>
<rect x="38" y="22" width="6" height="3" fill="#000" rx="1"/>
<circle cx="23" cy="24" r="2" fill="#ff3333"/>
<circle cx="41" cy="24" r="2" fill="#ff3333"/>
<path d="M26 30 L28 28 L30 30 L32 28 L34 30 L36 28 L38 30" fill="none" stroke="#334433" stroke-width="1.5"/>
<rect x="28" y="36" width="3" height="3" fill="{dd}" stroke="#334433" stroke-width="1"/>
<rect x="33" y="40" width="3" height="3" fill="{dd}" stroke="#334433" stroke-width="1"/>
<path d="M24 44 L28 46 L24 48" fill="none" stroke="#334433" stroke-width="1.5"/>
''')

m("lizard", "#66aa88", '''
<ellipse cx="32" cy="36" rx="18" ry="10" fill="{c}" stroke="#447766" stroke-width="2"/>
<path d="M14 36 Q6 30 4 34 Q6 38 14 38 Z" fill="{c}" stroke="#447766" stroke-width="2"/>
<path d="M50 36 Q58 32 60 36 Q58 40 50 38 Z" fill="{c}" stroke="#447766" stroke-width="2"/>
<circle cx="24" cy="32" r="3" fill="#fff"/><circle cx="24" cy="32" r="1.5" fill="#000"/>
<circle cx="36" cy="32" r="3" fill="#fff"/><circle cx="36" cy="32" r="1.5" fill="#000"/>
<path d="M14 36 L16 34 M14 38 L16 40" stroke="#447766" stroke-width="1.5"/>
<polygon points="50,36 54,34 54,38" fill="#ff6666"/>
<circle cx="28" cy="38" r="1" fill="{dd}"/>
<circle cx="34" cy="38" r="1" fill="{dd}"/>
<circle cx="40" cy="38" r="1" fill="{dd}"/>
''')

m("golem_stone", "#888888", '''
<rect x="14" y="20" width="36" height="36" fill="{c}" stroke="#555555" stroke-width="2" rx="4"/>
<rect x="18" y="14" width="28" height="10" fill="{c}" stroke="#555555" stroke-width="2" rx="3"/>
<rect x="20" y="26" width="8" height="6" fill="#555" rx="1"/>
<rect x="36" y="26" width="8" height="6" fill="#555" rx="1"/>
<rect x="22" y="28" width="3" height="3" fill="{lc}"/>
<rect x="38" y="28" width="3" height="3" fill="{lc}"/>
<rect x="24" y="38" width="16" height="4" fill="#555" rx="1"/>
<line x1="28" y1="38" x2="28" y2="42" stroke="#555" stroke-width="1"/>
<line x1="32" y1="38" x2="32" y2="42" stroke="#555" stroke-width="1"/>
<line x1="36" y1="38" x2="36" y2="42" stroke="#555" stroke-width="1"/>
<rect x="20" y="46" width="8" height="8" fill="{dd}" stroke="#555" stroke-width="1.5" rx="2"/>
<rect x="36" y="46" width="8" height="8" fill="{dd}" stroke="#555" stroke-width="1.5" rx="2"/>
''')

m("fairy", "#ff88cc", '''
<ellipse cx="32" cy="36" rx="12" ry="14" fill="{c}" stroke="#cc5599" stroke-width="2"/>
<path d="M20 28 Q8 16 14 28 Q18 32 22 30 Z" fill="{lc}" stroke="#cc5599" stroke-width="1.5" opacity="0.7"/>
<path d="M44 28 Q56 16 50 28 Q46 32 42 30 Z" fill="{lc}" stroke="#cc5599" stroke-width="1.5" opacity="0.7"/>
<polygon points="28,18 26,10 34,14" fill="{c}" stroke="#cc5599" stroke-width="1.5"/>
<polygon points="36,18 38,10 30,14" fill="{c}" stroke="#cc5599" stroke-width="1.5"/>
<circle cx="27" cy="34" r="3" fill="#fff"/><circle cx="27" cy="34" r="1.5" fill="#663399"/>
<circle cx="37" cy="34" r="3" fill="#fff"/><circle cx="37" cy="34" r="1.5" fill="#663399"/>
<path d="M28 42 Q32 44 36 42" fill="none" stroke="#cc5599" stroke-width="1.5" stroke-linecap="round"/>
<circle cx="32" cy="50" r="3" fill="{lc}" opacity="0.5"/>
<circle cx="20" cy="48" r="2" fill="{lc}" opacity="0.4"/>
<circle cx="44" cy="48" r="2" fill="{lc}" opacity="0.4"/>
''')

m("ghost", "#88ddff", '''
<path d="M16 30 Q16 14 32 12 Q48 14 48 30 L48 50 L42 46 L36 50 L32 46 L28 50 L22 46 L16 50 Z" fill="{c}" stroke="#4488aa" stroke-width="2" opacity="0.85"/>
<circle cx="26" cy="28" r="3" fill="#000"/>
<circle cx="38" cy="28" r="3" fill="#000"/>
<circle cx="26" cy="27" r="1" fill="#fff"/>
<circle cx="38" cy="27" r="1" fill="#fff"/>
<path d="M28 36 Q32 40 36 36" fill="none" stroke="#4488aa" stroke-width="2" stroke-linecap="round"/>
''')

m("crab", "#ff7744", '''
<ellipse cx="32" cy="38" rx="18" ry="12" fill="{c}" stroke="#cc4422" stroke-width="2"/>
<path d="M14 34 Q4 28 6 36 Q10 38 14 36 Z" fill="{c}" stroke="#cc4422" stroke-width="2"/>
<path d="M50 34 Q60 28 58 36 Q54 38 50 36 Z" fill="{c}" stroke="#cc4422" stroke-width="2"/>
<circle cx="24" cy="30" r="3" fill="#fff"/><circle cx="24" cy="30" r="1.5" fill="#000"/>
<circle cx="40" cy="30" r="3" fill="#fff"/><circle cx="40" cy="30" r="1.5" fill="#000"/>
<path d="M18 44 L14 50 M24 46 L22 54 M40 46 L42 54 M46 44 L50 50" stroke="#cc4422" stroke-width="2" stroke-linecap="round"/>
<path d="M28 36 Q32 40 36 36" fill="none" stroke="#cc4422" stroke-width="1.5" stroke-linecap="round"/>
<polygon points="24,26 20,22 28,24" fill="{c}" stroke="#cc4422" stroke-width="1.5"/>
<polygon points="40,26 44,22 36,24" fill="{c}" stroke="#cc4422" stroke-width="1.5"/>
''')

# Generate
for mid, color, svg_template in monsters:
    c = hex_to_rgb(color)
    lc = lighten(color, 1.3)
    dd = darken(color, 0.6)
    svg_content = svg_template.format(c=c, lc=lc, dd=dd)
    svg = svg_wrap(svg_content)
    svg_path = os.path.join(OUT, f"{mid}.svg")
    png_path = os.path.join(OUT, f"{mid}.png")
    with open(svg_path, "w") as f:
        f.write(svg)
    result = subprocess.run(
        ["convert", "-background", "transparent", svg_path, "-resize", "64x64", png_path],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"FAIL {mid}: {result.stderr.strip()}")
    else:
        print(f"OK   {mid}.png")
    os.remove(svg_path)

print(f"\nGenerated {len(monsters)} monster images.")
