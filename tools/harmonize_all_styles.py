import re
import os

STYLES_DIR = "src/styles"

def update_file(filename, fn):
    path = os.path.join(STYLES_DIR, filename)
    if not os.path.exists(path):
        print(f"File {filename} does not exist, skipping.")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = fn(content)
    if new_content != content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Harmonized {filename}")
    else:
        print(f"No changes needed for {filename}")

# 1. Rewards.css
def fix_rewards(text):
    text = re.sub(r'--primary-green:\s*#01360d;', '--primary-green: var(--bg-surface, #111625);', text)
    text = re.sub(r'--accent-green:\s*#00b050;', '--accent-green: var(--accent-emerald, #00ff99);', text)
    text = re.sub(r'--light-green:\s*#c3ffe2;', '--light-green: var(--bg-surface-alt, #161c2e);', text)
    text = re.sub(r'--light-blue:\s*#d4e3ff;', '--light-blue: rgba(0, 240, 255, 0.15);', text)
    text = re.sub(r'--yellow:\s*#ffca28;', '--yellow: var(--accent-gold, #ffcc00);', text)
    text = re.sub(r'--yellow-dark:\s*#fbc02d;', '--yellow-dark: #e6b800;', text)
    text = re.sub(r'--note-bg:\s*#fff9c4;', '--note-bg: var(--bg-surface-alt, #161c2e);', text)
    text = re.sub(r'--note-border:\s*#fbc02d;', '--note-border: var(--border-glass, rgba(0, 255, 200, 0.25));', text)
    text = re.sub(r'--note-text:\s*#795548;', '--note-text: var(--text-primary, #f0f6fc);', text)
    text = re.sub(r'--neutral-text:\s*#333;', '--neutral-text: var(--text-primary, #f0f6fc);', text)
    text = re.sub(r'--progress-bg:\s*#e0f2f1;', '--progress-bg: rgba(255, 255, 255, 0.08);', text)
    text = re.sub(r'linear-gradient\(to bottom right,\s*var\(--light-green\),\s*var\(--light-blue\)\)', 'var(--bg-base, #0a0d14)', text)
    text = text.replace('background-color: var(--primary-green);', 'background-color: var(--bg-surface, #111625); border-right: 1px solid var(--border-glass, rgba(0,255,200,0.15));')
    text = text.replace('color: #000;\n  padding: 1rem 1.25rem;', 'color: #000;\n  background: linear-gradient(135deg, var(--accent-emerald, #00ff99), var(--accent-cyan, #00f0ff));\n  padding: 1rem 1.25rem;')
    return text

update_file("Rewards.css", fix_rewards)

# 2. Features.css
def fix_features(text):
    text = re.sub(r'background-color:\s*#f4f4f9;', 'background-color: var(--bg-base, #0a0d14);', text)
    text = re.sub(r'color:\s*#000;', 'color: var(--text-primary, #f0f6fc);', text)
    text = re.sub(r'color:\s*#01360d;', 'color: var(--text-primary, #f0f6fc);', text)
    text = re.sub(r'color:\s*#00b050;', 'color: var(--accent-emerald, #00ff99);', text)
    text = re.sub(r'background-color:\s*#00b050;', 'background-color: var(--accent-emerald, #00ff99);', text)
    text = re.sub(r'background:\s*#ffffff;', 'background: var(--bg-surface, #111625);', text)
    text = re.sub(r'background:\s*#f4f4f4;', 'background: var(--bg-glass-card, #161c2e); border: 1px solid var(--border-glass, rgba(0, 255, 200, 0.18));', text)
    text = re.sub(r'color:\s*#333;', 'color: var(--text-secondary, #94a3b8);', text)
    text = re.sub(r'color:\s*#444;', 'color: var(--text-secondary, #94a3b8);', text)
    text = re.sub(r'border:\s*2px solid #00b050;', 'border: 1px solid var(--border-glass, rgba(0, 255, 200, 0.3));', text)
    text = text.replace('background-color: #036A32;', 'background-color: var(--accent-emerald, #00ff99); opacity: 0.9;')
    text = text.replace('background-color: rgba(91, 104, 127, 0.5);', 'background-color: rgba(10, 13, 20, 0.7);')
    return text

update_file("Features.css", fix_features)

# 3. Programs.css
def fix_programs(text):
    text = re.sub(r'background-color:\s*#ffffff;', 'background-color: var(--bg-base, #0a0d14);', text)
    text = re.sub(r'color:\s*#333;', 'color: var(--text-primary, #f0f6fc);', text)
    text = re.sub(r'background-color:\s*#EBEBEB;', 'background-color: var(--bg-glass-card, #161c2e); border: 1px solid var(--border-glass, rgba(0, 255, 200, 0.18));', text)
    text = re.sub(r'color:\s*#00b050;', 'color: var(--accent-emerald, #00ff99);', text)
    text = re.sub(r'border:\s*2px solid #00b050;', 'border: 1px solid var(--accent-emerald, #00ff99);', text)
    text = re.sub(r'background-color:\s*#f8f9fa;', 'background-color: var(--bg-surface-alt, #161c2e);', text)
    text = re.sub(r'color:\s*#5f6368;', 'color: var(--text-secondary, #94a3b8);', text)
    text = re.sub(r'color:\s*#3c4043;', 'color: var(--text-primary, #f0f6fc);', text)
    return text

update_file("Programs.css", fix_programs)

# 4. Events.css
def fix_events(text):
    text = re.sub(r'background:\s*#f9f9f9;', 'background: var(--bg-base, #0a0d14);', text)
    text = re.sub(r'color:\s*#333;', 'color: var(--text-primary, #f0f6fc);', text)
    text = re.sub(r'background:\s*#fff;', 'background: var(--bg-glass-card, #161c2e); border: 1px solid var(--border-glass, rgba(0, 255, 200, 0.18));', text)
    text = re.sub(r'background:\s*#00b050;', 'background: linear-gradient(135deg, var(--accent-emerald, #00ff99), var(--accent-cyan, #00f0ff)); color: #000;', text)
    text = re.sub(r'color:\s*#00b050;', 'color: var(--accent-emerald, #00ff99);', text)
    text = re.sub(r'border:\s*2px solid #00b050;', 'border: 1px solid var(--accent-emerald, #00ff99);', text)
    text = text.replace('background-color: #e9ffe9;', 'background-color: rgba(0, 255, 153, 0.1);')
    text = text.replace('background-color: #fffbe6;', 'background-color: rgba(255, 204, 0, 0.1);')
    text = text.replace('background-color: #eeeeee;', 'background-color: var(--bg-surface-alt, #161c2e);')
    return text

update_file("Events.css", fix_events)

# 5. Communities.css
def fix_communities(text):
    text = re.sub(r'background:\s*#f9f9f9;', 'background: var(--bg-base, #0a0d14);', text)
    text = re.sub(r'color:\s*#222;', 'color: var(--text-primary, #f0f6fc);', text)
    text = re.sub(r'background:\s*#fff;', 'background: var(--bg-glass-card, #161c2e); border: 1px solid var(--border-glass, rgba(0, 255, 200, 0.18));', text)
    text = re.sub(r'background:\s*#00b050;', 'background: linear-gradient(135deg, var(--accent-emerald, #00ff99), var(--accent-cyan, #00f0ff)); color: #000;', text)
    text = re.sub(r'color:\s*#00b050;', 'color: var(--accent-emerald, #00ff99);', text)
    return text

update_file("Communities.css", fix_communities)

# 6. Faq.css
def fix_faq(text):
    text = re.sub(r'background-color:\s*#fefefe;', 'background-color: var(--bg-base, #0a0d14);', text)
    text = re.sub(r'color:\s*#111;', 'color: var(--text-primary, #f0f6fc);', text)
    text = re.sub(r'background:\s*#eef1f5;', 'background: var(--bg-base, #0a0d14);', text)
    text = re.sub(r'background:\s*#fff;', 'background: var(--bg-glass-card, #161c2e); border: 1px solid var(--border-glass, rgba(0, 255, 200, 0.18));', text)
    text = re.sub(r'background-color:\s*#ffffff;', 'background-color: var(--bg-glass-card, #161c2e);', text)
    text = re.sub(r'color:\s*#333;', 'color: var(--text-secondary, #94a3b8);', text)
    text = re.sub(r'color:\s*#00b050;', 'color: var(--accent-emerald, #00ff99);', text)
    text = re.sub(r'background-color:\s*#e3f9ec;', 'background-color: rgba(0, 255, 153, 0.1);', text)
    text = re.sub(r'background-color:\s*#eaeaea;', 'background-color: var(--bg-surface-alt, #161c2e);', text)
    text = re.sub(r'background-color:\s*#f7f7f7;', 'background-color: var(--bg-surface-alt, #161c2e);', text)
    return text

update_file("Faq.css", fix_faq)

# 7. Partners.css
def fix_partners(text):
    text = text.replace('--brand: #00b050;', '--brand: var(--accent-emerald, #00ff99);')
    text = text.replace('--light: #fafafa;', '--light: var(--bg-base, #0a0d14);')
    text = text.replace('--dark: #101010;', '--dark: var(--text-primary, #f0f6fc);')
    text = text.replace('background: #fff;', 'background: var(--bg-glass-card, #161c2e); border: 1px solid var(--border-glass, rgba(0, 255, 200, 0.18));')
    return text

update_file("Partners.css", fix_partners)

# 8. Policies (CookiePolicy, CopyrightPolicy, PrivacyPolicy, Terms)
def fix_policy(text):
    text = re.sub(r'background(?:-color)?:\s*(?:#f9f9f9|#ffffff|#fefefe);', 'background-color: var(--bg-base, #0a0d14);', text)
    text = re.sub(r'color:\s*(?:#111|#222);', 'color: var(--text-primary, #f0f6fc);', text)
    text = re.sub(r'background(?:-color)?:\s*(?:#fff|#eaeaea|#eefaf1);', 'background: var(--bg-surface, #111625); border: 1px solid var(--border-glass, rgba(0, 255, 200, 0.2));', text)
    text = re.sub(r'color:\s*#00b050;', 'color: var(--accent-emerald, #00ff99);', text)
    text = re.sub(r'color:\s*#666;', 'color: var(--text-secondary, #94a3b8);', text)
    return text

update_file("CookiePolicy.css", fix_policy)
update_file("CopyrightPolicy.css", fix_policy)
update_file("PrivacyPolicy.css", fix_policy)
update_file("Terms.css", fix_policy)

# 9. ContactUsPage.css
def fix_contact(text):
    text = text.replace('background: linear-gradient(to right, #002f2f, #01360d);', 'background: radial-gradient(ellipse at 50% 30%, rgba(0, 255, 153, 0.08) 0%, var(--bg-base, #0a0d14) 75%);')
    text = text.replace('#00b050', 'var(--accent-emerald, #00ff99)')
    text = text.replace('#33fff3', 'var(--accent-cyan, #00f0ff)')
    text = text.replace('color: #ccf5dd;', 'color: var(--text-secondary, #94a3b8);')
    text = text.replace('background: #f0fff4;', 'background: var(--bg-surface, #111625);')
    return text

update_file("ContactUsPage.css", fix_contact)

# 10. setup-student.css
def fix_setup(text):
    text = text.replace('#00b050', 'var(--accent-emerald, #00ff99)')
    text = text.replace('background-color: #121212;', 'background-color: var(--bg-base, #0a0d14);')
    text = text.replace('background: #1a1a1a;', 'background: var(--bg-surface, #111625); border: 1px solid var(--border-glass, rgba(0, 255, 200, 0.2));')
    return text

update_file("setup-student.css", fix_setup)

# 11. AboutUs.css
def fix_about(text):
    text = text.replace('#00b050', 'var(--accent-emerald, #00ff99)')
    text = text.replace('background-color: #fff;', 'background-color: var(--bg-glass-card, #161c2e); border: 1px solid var(--border-glass, rgba(0,255,200,0.18));')
    return text

update_file("AboutUs.css", fix_about)

print("Finished color harmonization across all stylesheets.")
