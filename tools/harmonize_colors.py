import re

# 1. Harmonize Hero.css
hero_path = "/home/stark/zunix/src/styles/Hero.css"
with open(hero_path, "r", encoding="utf-8") as f:
    hero = f.read()

# Replace hero background
hero = re.sub(
    r'background:\s*linear-gradient\(to right,\s*#00b050,\s*#01360d,\s*#d4e3ff\);',
    'background: radial-gradient(ellipse at 50% 30%, rgba(0, 255, 153, 0.12) 0%, var(--bg-base, #0a0d14) 75%);',
    hero
)
# Replace headline color with brand gradient
hero = re.sub(
    r'(\.headline\s*\{[^}]*?)color:\s*#33fff3;',
    r'\1background: linear-gradient(135deg, var(--accent-emerald, #00ff99), var(--accent-cyan, #00f0ff));\n  -webkit-background-clip: text;\n  -webkit-text-fill-color: transparent;',
    hero
)
# Replace subtext color
hero = hero.replace('color: #ccf5dd;', 'color: var(--text-secondary, #94a3b8);')
# Replace baby blue blob with subtle gold
hero = hero.replace('background: #b5cfff;', 'background: rgba(255, 204, 0, 0.2);')
hero = hero.replace('background: #c3ffe2;', 'background: rgba(0, 240, 255, 0.2);')
hero = hero.replace('background: #00b050;\n  top: 10%;', 'background: rgba(0, 255, 153, 0.25);\n  top: 10%;')

with open(hero_path, "w", encoding="utf-8") as f:
    f.write(hero)
print("Harmonized Hero.css")

# 2. Harmonize FeatureSection.css
feat_path = "/home/stark/zunix/src/styles/FeatureSection.css"
with open(feat_path, "r", encoding="utf-8") as f:
    feat = f.read()

feat = feat.replace('background: #FFFFFF; /* Clean luxury white */', 'background: var(--bg-surface, #111625);')
feat = feat.replace('color: #1A1A1A; /* Deep black for text contrast */', 'color: var(--text-primary, #f0f6fc);')
feat = feat.replace('background: linear-gradient(90deg, #0ecb81, #0b9e65);', 'background: linear-gradient(90deg, var(--accent-emerald, #00ff99), var(--accent-cyan, #00f0ff));')
feat = feat.replace('color: #4A4A4A;', 'color: var(--text-secondary, #94a3b8);')
feat = feat.replace('background: linear-gradient(135deg, #f9f9f9, #eaeaea);', 'background: var(--bg-glass-card, #161c2e); border: 1px solid var(--border-glass, rgba(0,255,200,0.18));')
feat = feat.replace('color: #333333;', 'color: var(--text-primary, #f0f6fc);')

with open(feat_path, "w", encoding="utf-8") as f:
    f.write(feat)
print("Harmonized FeatureSection.css")

# 3. Harmonize HowItWorks.css
how_path = "/home/stark/zunix/src/styles/HowItWorks.css"
with open(how_path, "r", encoding="utf-8") as f:
    how = f.read()

how = re.sub(r'background:\s*#01360d;', 'background: var(--bg-base, #0a0d14);', how)
how = how.replace('color: #d4e3ff;', 'color: var(--text-primary, #f0f6fc);')
how = how.replace('background-color: #000;\n  padding: 15px 0;', 'background-color: var(--bg-surface, #111625);\n  border-bottom: 1px solid var(--border-glass, rgba(0,255,200,0.2));\n  padding: 15px 0;')
how = how.replace('color: #33fff3;', 'color: var(--accent-emerald, #00ff99);')
how = how.replace('background: #0a2e13;', 'background: var(--bg-glass-card, #161c2e);')
how = how.replace('border: 2px solid #00f2fe;', 'border: 1px solid var(--border-glass, rgba(0,255,200,0.3));')
how = how.replace('box-shadow: 0 14px 40px rgba(0, 242, 254, 0.5);', 'box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);')
how = how.replace('background-color: #002611;', 'background-color: var(--bg-surface-alt, #1a2238);')
how = how.replace('linear-gradient(90deg, #33fff3 0%, #00b050 100%)', 'linear-gradient(90deg, var(--accent-emerald, #00ff99) 0%, var(--accent-cyan, #00f0ff) 100%)')
how = how.replace('color: #00f2fe;', 'color: var(--accent-emerald, #00ff99);')
how = how.replace('color: #99e7cc;', 'color: var(--text-secondary, #94a3b8);')
how = how.replace('color: #a0f0d1;', 'color: var(--text-secondary, #94a3b8);')
how = how.replace('color: #ccf5dd;', 'color: var(--text-secondary, #94a3b8);')
how = how.replace('background: #004a26;', 'background: var(--bg-surface-alt, #161c2e);')
how = how.replace('background-color: #006633;', 'background-color: var(--bg-surface-alt, #161c2e);')

with open(how_path, "w", encoding="utf-8") as f:
    f.write(how)
print("Harmonized HowItWorks.css")

# 4. Harmonize ShowcaseSection.css
show_path = "/home/stark/zunix/src/styles/ShowcaseSection.css"
with open(show_path, "r", encoding="utf-8") as f:
    show = f.read()

show = show.replace('background: linear-gradient(135deg, #01360d, #001e0d);', 'background: var(--bg-surface, #111625);')
show = show.replace('background: rgba(1, 54, 13, 0.75);', 'background: var(--bg-glass-card, rgba(22, 28, 46, 0.85));')
show = show.replace('color: #33fff3;', 'color: var(--accent-emerald, #00ff99);')
show = show.replace('color: #ccf5dd;', 'color: var(--text-secondary, #94a3b8);')
show = show.replace('color: #c3ffe2;', 'color: var(--text-secondary, #94a3b8);')
show = show.replace('box-shadow:\n    0 0 10px 2px #33fff3,\n    inset 0 0 20px 2px #00b050;', 'box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), inset 0 0 15px rgba(0, 255, 153, 0.15); border: 1px solid var(--border-glass, rgba(0,255,200,0.25));')

with open(show_path, "w", encoding="utf-8") as f:
    f.write(show)
print("Harmonized ShowcaseSection.css")

# 5. Harmonize PreFooter.css
pref_path = "/home/stark/zunix/src/styles/PreFooter.css"
with open(pref_path, "r", encoding="utf-8") as f:
    pref = f.read()

pref = pref.replace('background: #f4f4f9;', 'background: var(--bg-base, #0a0d14);')
pref = pref.replace('color: #000;', 'color: var(--text-primary, #f0f6fc);')
pref = pref.replace('border-top: 2px solid #333;', 'border-top: 1px solid var(--border-subtle, rgba(255,255,255,0.08));')
pref = pref.replace('color: #444;', 'color: var(--text-primary, #f0f6fc);')
pref = pref.replace('background: #eef1f5;', 'background: var(--bg-surface, #111625);')
pref = pref.replace('background-color: #f7f7f7;', 'background-color: var(--bg-glass-card, #161c2e);')
pref = pref.replace('color: #333;', 'color: var(--text-primary, #f0f6fc);')
pref = pref.replace('color: #222;', 'color: var(--text-primary, #f0f6fc);')
pref = pref.replace('border-bottom: 1px solid #ddd;', 'border-bottom: 1px solid var(--border-subtle, rgba(255,255,255,0.08));')
pref = pref.replace('background: linear-gradient(to right, #e2e2e2, #c8f5dc);', 'background: linear-gradient(to right, var(--bg-surface-alt, #161c2e), var(--bg-surface, #111625)); border: 1px solid var(--border-glass, rgba(0,255,200,0.2));')

with open(pref_path, "w", encoding="utf-8") as f:
    f.write(pref)
print("Harmonized PreFooter.css")

# 6. Harmonize Footer.css
foot_path = "/home/stark/zunix/src/styles/Footer.css"
with open(foot_path, "r", encoding="utf-8") as f:
    foot = f.read()

foot = foot.replace('background: linear-gradient(to right, #000000, #01360d);', 'background: var(--bg-surface, #111625); border-top: 1px solid var(--border-subtle, rgba(255,255,255,0.08));')
foot = foot.replace('border: 1px solid #2d0b00;', 'border: 1px solid var(--border-glass, rgba(0,255,200,0.25));')
foot = foot.replace('background-color: #2d0b00;', 'background-color: var(--bg-glass-subtle, rgba(255,255,255,0.05));')
foot = foot.replace('background-color: #fff;\n      border: 1px solid #ddd;', 'background-color: var(--bg-surface, #111625);\n      border: 1px solid var(--border-glass, rgba(0,255,200,0.25));')
foot = foot.replace('color: #333;', 'color: var(--text-primary, #f0f6fc);')
foot = foot.replace('background-color: #f5f5f5;', 'background-color: rgba(0,255,153,0.12);')

with open(foot_path, "w", encoding="utf-8") as f:
    f.write(foot)
print("Harmonized Footer.css")

# 7. Harmonize AboutUs.css
about_path = "/home/stark/zunix/src/styles/AboutUs.css"
with open(about_path, "r", encoding="utf-8") as f:
    about = f.read()

about = about.replace('background-color: #f9f9f9;', 'background-color: var(--bg-base, #0a0d14);')
about = about.replace('color: #222;', 'color: var(--text-primary, #f0f6fc);')
about = about.replace('background-color: #01360d;', 'background-color: var(--bg-surface, #111625);')
about = about.replace('background: #f0f0f0;', 'background: var(--bg-glass-card, #161c2e);')
about = about.replace('background: #e9e9e9;', 'background: var(--bg-surface-alt, #161c2e);')
about = about.replace('background: #f7f7f7;', 'background: var(--bg-glass-card, #161c2e);')
about = about.replace('border: 1px solid #ddd;', 'border: 1px solid var(--border-glass, rgba(0,255,200,0.2));')

with open(about_path, "w", encoding="utf-8") as f:
    f.write(about)
print("Harmonized AboutUs.css")
