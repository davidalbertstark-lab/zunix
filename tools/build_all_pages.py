import re
import os

ZUNIX_DIR = "/home/stark/zunix"
PAGES_DIR = os.path.join(ZUNIX_DIR, "pages")
os.makedirs(PAGES_DIR, exist_ok=True)

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Wrote {os.path.basename(path)} successfully ({len(content)} bytes)")

def extract_between(text, start_pattern, end_pattern):
    m_start = re.search(start_pattern, text, re.DOTALL | re.IGNORECASE)
    m_end = re.search(end_pattern, text, re.DOTALL | re.IGNORECASE)
    if m_start and m_end:
        return text[m_start.end():m_end.start()]
    elif m_start:
        return text[m_start.end():]
    return text

def make_head(title, extra_css=[]):
    css_links = "\n".join([f'  <link rel="stylesheet" href="../src/styles/{c}" />' for c in extra_css])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <link rel="icon" href="../src/img/favicon-32x32.png" type="image/png" sizes="32x32" />
  <link rel="icon" href="../src/img/favicon-16x16.png" type="image/png" sizes="16x16" />
  <link rel="apple-touch-icon" href="../src/img/apple-touch-icon.png" sizes="180x180" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../src/styles/theme.css" />
  <link rel="stylesheet" href="../src/styles/Header.css" />
{css_links}
  <style>
    body {{ padding-top: 80px; }}
  </style>
</head>
<body class="body-bg">
"""

def make_header(active=""):
    def is_act(name):
        return ' style="color: var(--accent-emerald); font-weight: 700;" class="active"' if active == name else ''

    return f"""  <header class="header">
    <div class="logo">
      <a href="../index.html">
        <img src="../src/img/favicon-32x32.png" alt="Zunix Logo" />
        <span>Zunix</span>
      </a>
    </div>

    <input type="checkbox" id="nav-toggle" class="nav-toggle" />

    <nav class="nav">
      <ul>
        <li><a href="features.html"{is_act('features')} data-i18n="nav_features">Features</a></li>
        <li><a href="rewards.html"{is_act('rewards')} data-i18n="nav_rewards">Rewards</a></li>
        <li><a href="programs.html"{is_act('programs')} data-i18n="nav_programs">Programs</a></li>
        <li><a href="events.html"{is_act('events')} data-i18n="nav_events">Events</a></li>
        <li><a href="communities.html"{is_act('communities')} data-i18n="nav_communities">Communities</a></li>
      </ul>

      <div class="header-actions">
        <!-- Language Picker -->
        <div class="header-lang-picker">
          <details>
            <summary>
              <span class="lang-flag-icon current-lang-flag" style="background-image: url('https://flagcdn.com/w40/gb.png');"></span>
              <span class="current-lang-label">EN</span>
            </summary>
            <div class="lang-menu-dropdown">
              <a href="#" data-switch-lang="en"><span class="lang-flag-icon" style="background-image: url('https://flagcdn.com/w40/gb.png');"></span> English</a>
              <a href="#" data-switch-lang="de"><span class="lang-flag-icon" style="background-image: url('https://flagcdn.com/w40/de.png');"></span> Deutsch</a>
              <a href="#" data-switch-lang="fr"><span class="lang-flag-icon" style="background-image: url('https://flagcdn.com/w40/fr.png');"></span> Français</a>
              <a href="#" data-switch-lang="ar"><span class="lang-flag-icon" style="background-image: url('https://flagcdn.com/w40/sa.png');"></span> العربية</a>
            </div>
          </details>
        </div>

        <!-- Theme Switcher -->
        <button class="theme-toggle-btn" aria-label="Toggle Theme" title="Toggle Dark/Light Mode">
          <span class="theme-icon">☀️</span>
        </button>

        <!-- CTA Buttons -->
        <div class="cta-buttons">
          <a href="login.html#loginBox" class="header-btn header-btn-login" data-i18n="nav_login">Log In</a>
          <a href="login.html#signupBox" class="header-btn header-btn-signup" data-i18n="nav_signup">Sign Up</a>
        </div>
      </div>
    </nav>

    <label for="nav-toggle" class="nav-toggle-label" aria-label="Toggle navigation menu">
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </label>
  </header>
"""

def make_footer():
    return """  <footer class="footer" style="padding: 40px 24px; text-align: center; border-top: 1px solid var(--border-subtle); background: var(--bg-surface); margin-top: 60px;">
    <div style="max-width: 1200px; margin: 0 auto; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 20px;">
      <div style="display: flex; align-items: center; gap: 12px;">
        <img src="../src/img/favicon-32x32.png" alt="Zunix Logo" style="width: 28px; height: 28px;" />
        <span style="font-weight: 700; color: var(--accent-emerald);">Zunix</span>
        <span style="color: var(--text-muted);">© 2025</span>
      </div>

      <div style="display: flex; gap: 20px; flex-wrap: wrap; font-size: 0.9rem;">
        <a href="about.html" style="color: var(--text-secondary);">About</a>
        <a href="faq.html" style="color: var(--text-secondary);">FAQ</a>
        <a href="partners.html" style="color: var(--text-secondary);">Partners</a>
        <a href="contact.html" style="color: var(--text-secondary);">Contact</a>
        <a href="terms.html" style="color: var(--text-secondary);">Terms</a>
        <a href="privacy.html" style="color: var(--text-secondary);">Privacy</a>
        <a href="cookies.html" style="color: var(--text-secondary);">Cookies</a>
        <a href="copyright.html" style="color: var(--text-secondary);">Copyright</a>
      </div>

      <div style="color: var(--text-muted); font-size: 0.85rem;" data-i18n="footer_rights">
        All rights reserved
      </div>
    </div>
  </footer>
"""

def make_scripts(extra=[]):
    tags = "\n".join([f'  <script type="module" src="{s}"></script>' for s in extra])
    return f"""  <script type="module" src="../src/js/theme.js"></script>
  <script type="module" src="../src/js/i18n.js"></script>
{tags}
</body>
</html>
"""

def replace_links_and_assets(html):
    html = re.sub(r'(src|href)=["\']src/', r'\1="../src/', html)
    html = re.sub(r'(src|href)=["\']data/', r'\1="../data/', html)
    html = re.sub(r'(src|href)=["\']json/', r'\1="../json/', html)
    
    link_map = {
        'index.html': '../index.html',
        'Features.html': 'features.html',
        'Rewards.html': 'rewards.html',
        'Programs.html': 'programs.html',
        'Events.html': 'events.html',
        'Communities.html': 'communities.html',
        'AboutUs.html': 'about.html',
        'ContactUsPage.html': 'contact.html',
        'Faq.html': 'faq.html',
        'Partners.html': 'partners.html',
        'Terms.html': 'terms.html',
        'PrivacyPolicy.html': 'privacy.html',
        'CookiePolicy.html': 'cookies.html',
        'CopyrightPolicy.html': 'copyright.html',
        'LoginPage.html': 'login.html',
        'setup-student.html': 'setup-student.html',
        'profile-card.html': 'profile-card.html'
    }
    for old, new in link_map.items():
        html = re.sub(rf'href=["\']{re.escape(old)}(#[^"\']*)?["\']', lambda m: f'href="{new}{m.group(1) or ""}"', html)
    return html

# -------------------------------------------------------------
# 1. BUILD features.html
# -------------------------------------------------------------
feat_raw = read_file(os.path.join(ZUNIX_DIR, "Features.html"))
feat_body = extract_between(feat_raw, r'</header>', r'<footer')
feat_body = replace_links_and_assets(feat_body)
write_file(os.path.join(PAGES_DIR, "features.html"),
    make_head("Zunix Features — The Student Operating System", ["Features.css"]) +
    make_header("features") +
    feat_body +
    make_footer() +
    make_scripts()
)

# -------------------------------------------------------------
# 2. BUILD rewards.html (WITH INTERACTIVE XP SIMULATOR)
# -------------------------------------------------------------
rew_raw = read_file(os.path.join(ZUNIX_DIR, "Rewards.html"))
rew_body = extract_between(rew_raw, r'</header>', r'<footer')
rew_body = replace_links_and_assets(rew_body)

# Replace the static sidebar with the interactive live simulator widget
old_sidebar_pattern = r'<aside class="sidebar">.*?</aside>'
new_sidebar = """<aside class="sidebar">
      <h2 class="sidebar-title"><i class="fas fa-gamepad"></i> Your Progress</h2>
      <div class="score-box">
        <p class="score-label"><i class="fas fa-chart-line"></i> Engagement Score</p>
        <h1 class="score-value"><span id="simScoreValue">845</span> <span class="score-unit">ZP</span></h1>
        <div id="simRankBadge" class="rank-badge" style="display:inline-block;padding:4px 12px;border-radius:20px;font-size:0.8rem;font-weight:700;border:1px solid #00ff99;margin-bottom:12px;color:#00ff99;">⚡ Campus Innovator</div>
        <div class="progress-bar">
          <div class="progress-fill" id="simProgressFill" style="width: 70%;"></div>
        </div>
        <p id="simNextTarget" style="font-size:0.75rem;color:var(--text-muted);margin-top:8px;">355 ZP until next rank</p>
      </div>

      <!-- Live Gamification Simulator Controls -->
      <div class="sim-actions" style="margin-top:20px;display:flex;flex-direction:column;gap:8px;">
        <p style="font-size:0.82rem;font-weight:700;color:var(--accent-emerald);text-transform:uppercase;letter-spacing:0.5px;margin:0 0 4px;"><i class="fas fa-bolt"></i> Live XP Simulator</p>
        <button type="button" id="btnDailyBonus" class="zbtn zbtn-secondary" style="font-size:0.82rem;padding:8px 12px;justify-content:flex-start;border-radius:8px;">
          <i class="fas fa-calendar-check" style="color:#00ff99;"></i> Daily Check-in (+150 ZP)
        </button>
        <button type="button" id="btnPeerReview" class="zbtn zbtn-secondary" style="font-size:0.82rem;padding:8px 12px;justify-content:flex-start;border-radius:8px;">
          <i class="fas fa-code" style="color:#00f0ff;"></i> Peer Review (+250 ZP)
        </button>
        <button type="button" id="btnHackathon" class="zbtn zbtn-secondary" style="font-size:0.82rem;padding:8px 12px;justify-content:flex-start;border-radius:8px;">
          <i class="fas fa-trophy" style="color:#ffcc00;"></i> Win Hackathon (+500 ZP)
        </button>
        <button type="button" id="btnResetXP" class="zbtn" style="background:transparent;border:1px dashed var(--border-subtle);font-size:0.75rem;padding:6px;color:var(--text-muted);border-radius:6px;margin-top:4px;">
          <i class="fas fa-undo"></i> Reset XP State
        </button>
      </div>

      <button class="join-button" onclick="window.location.href='login.html#signupBox'" style="margin-top:18px;">
        <i class="fas fa-rocket"></i> Claim Real Rewards
      </button>
    </aside>"""

rew_body = re.sub(old_sidebar_pattern, new_sidebar, rew_body, flags=re.DOTALL)

write_file(os.path.join(PAGES_DIR, "rewards.html"),
    make_head("Zunix Rewards — Earn Real Perks, Cash & Recognition", ["Rewards.css"]) +
    make_header("rewards") +
    rew_body +
    make_footer() +
    make_scripts(["../src/js/rewards-sim.js"])
)

# -------------------------------------------------------------
# 3. BUILD programs.html (WITH REAL-TIME SEARCH & FILTER)
# -------------------------------------------------------------
prog_raw = read_file(os.path.join(ZUNIX_DIR, "Programs.html"))
prog_body = extract_between(prog_raw, r'</header>', r'<footer')
prog_body = replace_links_and_assets(prog_body)

# Filter bar HTML
filter_bar = """
  <div class="programs-filter-bar" style="max-width: 1200px; margin: 30px auto 20px; padding: 0 20px;">
    <div style="display: flex; flex-wrap: wrap; gap: 15px; align-items: center; justify-content: space-between; background: var(--bg-glass-card); border: 1px solid var(--border-glass); border-radius: 16px; padding: 16px 22px; backdrop-filter: blur(12px);">
      <div style="flex: 1; min-width: 260px; position: relative;">
        <i class="fas fa-search" style="position: absolute; left: 14px; top: 50%; transform: translateY(-50%); color: var(--text-muted);"></i>
        <input type="text" id="programSearchInput" placeholder="Search tracks, programs or skills (e.g., freelance, tech, ambassador)..." style="width: 100%; padding: 10px 14px 10px 40px; border-radius: 30px; border: 1px solid var(--border-subtle); background: var(--bg-surface-alt); color: var(--text-primary); font-size: 0.9rem; outline: none;" />
      </div>
      <div style="display: flex; gap: 8px; flex-wrap: wrap;" class="filter-pills-container">
        <button class="prog-filter-pill active" data-filter="all" style="padding: 6px 14px; border-radius: 20px; border: 1px solid var(--border-glass); background: var(--accent-emerald); color: #000; font-size: 0.82rem; font-weight: 700; cursor: pointer;">All Tracks</button>
        <button class="prog-filter-pill" data-filter="engagement" style="padding: 6px 14px; border-radius: 20px; border: 1px solid var(--border-subtle); background: var(--bg-glass-subtle); color: var(--text-secondary); font-size: 0.82rem; font-weight: 600; cursor: pointer;">Engagement</button>
        <button class="prog-filter-pill" data-filter="freelance" style="padding: 6px 14px; border-radius: 20px; border: 1px solid var(--border-subtle); background: var(--bg-glass-subtle); color: var(--text-secondary); font-size: 0.82rem; font-weight: 600; cursor: pointer;">Freelancers</button>
        <button class="prog-filter-pill" data-filter="sellers" style="padding: 6px 14px; border-radius: 20px; border: 1px solid var(--border-subtle); background: var(--bg-glass-subtle); color: var(--text-secondary); font-size: 0.82rem; font-weight: 600; cursor: pointer;">Sellers</button>
        <button class="prog-filter-pill" data-filter="ambassador" style="padding: 6px 14px; border-radius: 20px; border: 1px solid var(--border-subtle); background: var(--bg-glass-subtle); color: var(--text-secondary); font-size: 0.82rem; font-weight: 600; cursor: pointer;">Ambassadors</button>
        <button class="prog-filter-pill" data-filter="academic" style="padding: 6px 14px; border-radius: 20px; border: 1px solid var(--border-subtle); background: var(--bg-glass-subtle); color: var(--text-secondary); font-size: 0.82rem; font-weight: 600; cursor: pointer;">Academic</button>
      </div>
    </div>
    <div id="programCountBadge" style="font-size: 0.82rem; color: var(--text-muted); margin-top: 10px; margin-left: 10px;">
      Showing 7 of 7 programs
    </div>
  </div>
"""

# Insert filter bar before first section
prog_body = filter_bar + prog_body

# Tag categories on section IDs
prog_body = prog_body.replace('id="monthly-engagement"', 'id="monthly-engagement" data-category="engagement"')
prog_body = prog_body.replace('id="freelancers"', 'id="freelancers" data-category="freelance"')
prog_body = prog_body.replace('id="sellers"', 'id="sellers" data-category="sellers"')
prog_body = prog_body.replace('id="campus-ambassador"', 'id="campus-ambassador" data-category="ambassador"')
prog_body = prog_body.replace('id="creators-writers"', 'id="creators-writers" data-category="creators"')
prog_body = prog_body.replace('id="academic-help"', 'id="academic-help" data-category="academic"')
prog_body = prog_body.replace('id="events-promo"', 'id="events-promo" data-category="events"')

write_file(os.path.join(PAGES_DIR, "programs.html"),
    make_head("Zunix Programs — Accelerate Your Career & Craft", ["Programs.css"]) +
    make_header("programs") +
    prog_body +
    make_footer() +
    make_scripts(["../src/js/programs-filter.js"])
)

# -------------------------------------------------------------
# 4. BUILD events.html
# -------------------------------------------------------------
ev_raw = read_file(os.path.join(ZUNIX_DIR, "Events.html"))
ev_body = extract_between(ev_raw, r'</header>', r'<footer')
ev_body = replace_links_and_assets(ev_body)
write_file(os.path.join(PAGES_DIR, "events.html"),
    make_head("Zunix Events — Plug Into Campus Culture", ["Events.css"]) +
    make_header("events") +
    ev_body +
    make_footer() +
    make_scripts()
)

# -------------------------------------------------------------
# 5. BUILD communities.html
# -------------------------------------------------------------
com_raw = read_file(os.path.join(ZUNIX_DIR, "Communities.html"))
com_body = extract_between(com_raw, r'</header>', r'</body>')
com_body = replace_links_and_assets(com_body)
write_file(os.path.join(PAGES_DIR, "communities.html"),
    make_head("Zunix Communities — Where Students Belong", ["Communities.css"]) +
    make_header("communities") +
    com_body +
    make_footer() +
    make_scripts()
)

# -------------------------------------------------------------
# 6. BUILD about.html
# -------------------------------------------------------------
ab_raw = read_file(os.path.join(ZUNIX_DIR, "AboutUs.html"))
ab_body = extract_between(ab_raw, r'</header>', r'</body>')
ab_body = replace_links_and_assets(ab_body)
write_file(os.path.join(PAGES_DIR, "about.html"),
    make_head("About Zunix — The Mission & Architecture", ["AboutUs.css"]) +
    make_header("") +
    ab_body +
    make_footer() +
    make_scripts()
)

# -------------------------------------------------------------
# 7. BUILD contact.html
# -------------------------------------------------------------
con_raw = read_file(os.path.join(ZUNIX_DIR, "ContactUsPage.html"))
con_body = extract_between(con_raw, r'</header>', r'</body>')
con_body = replace_links_and_assets(con_body)
write_file(os.path.join(PAGES_DIR, "contact.html"),
    make_head("Contact Us — Zunix Team", ["ContactUsPage.css"]) +
    make_header("") +
    con_body +
    make_footer() +
    make_scripts()
)

# -------------------------------------------------------------
# 8. BUILD faq.html
# -------------------------------------------------------------
faq_raw = read_file(os.path.join(ZUNIX_DIR, "Faq.html"))
faq_body = extract_between(faq_raw, r'</header>', r'</body>')
faq_body = replace_links_and_assets(faq_body)
write_file(os.path.join(PAGES_DIR, "faq.html"),
    make_head("FAQ — Zunix Knowledge Base", ["Faq.css"]) +
    make_header("") +
    faq_body +
    make_footer() +
    make_scripts()
)

# -------------------------------------------------------------
# 9. BUILD partners.html
# -------------------------------------------------------------
part_raw = read_file(os.path.join(ZUNIX_DIR, "Partners.html"))
part_body = extract_between(part_raw, r'</header>', r'</body>')
part_body = replace_links_and_assets(part_body)
write_file(os.path.join(PAGES_DIR, "partners.html"),
    make_head("Partner With Zunix", ["Partners.css"]) +
    make_header("") +
    part_body +
    make_footer() +
    make_scripts()
)

# -------------------------------------------------------------
# 10. BUILD terms.html, privacy.html, cookies.html, copyright.html
# -------------------------------------------------------------
legal_pages = [
    ("Terms.html", "terms.html", "Terms of Service — Zunix", "Terms.css"),
    ("PrivacyPolicy.html", "privacy.html", "Privacy Policy — Zunix", "PrivacyPolicy.css"),
    ("CookiePolicy.html", "cookies.html", "Cookie Policy — Zunix", "CookiePolicy.css"),
    ("CopyrightPolicy.html", "copyright.html", "Copyright Policy — Zunix", "CopyrightPolicy.css")
]

for src_name, dst_name, title, css in legal_pages:
    raw = read_file(os.path.join(ZUNIX_DIR, src_name))
    body = extract_between(raw, r'</header>' if '</header>' in raw else r'<body[^>]*>', r'</body>')
    body = replace_links_and_assets(body)
    write_file(os.path.join(PAGES_DIR, dst_name),
        make_head(title, [css]) +
        make_header("") +
        body +
        make_footer() +
        make_scripts()
    )

# -------------------------------------------------------------
# 11. BUILD profile-card.html (WITH 3D TILT & CANVAS PNG DOWNLOAD)
# -------------------------------------------------------------
card_raw = read_file(os.path.join(ZUNIX_DIR, "profile-card.html"))
# Replace links and assets
card_processed = replace_links_and_assets(card_raw)
# Replace CSS link
card_processed = card_processed.replace('src/styles/step6.css', '../src/styles/step6.css')
card_processed = card_processed.replace('src/styles/Header.css', '../src/styles/Header.css')
# Add theme.css
card_processed = card_processed.replace('<link rel="stylesheet" href="../src/styles/step6.css" />',
    '<link rel="stylesheet" href="../src/styles/theme.css" />\n  <link rel="stylesheet" href="../src/styles/step6.css" />')

# Replace header in profile-card.html with our standard header
card_processed = re.sub(r'<header class="header">.*?</header>', make_header(""), card_processed, flags=re.DOTALL)

# Add Download PNG button to actions
old_actions = r'<div class="card-actions">.*?</div>'
new_actions = """<div class="card-actions" style="display:flex;flex-direction:column;gap:10px;margin-top:1.5rem;">
        <button type="button" class="action-btn share" id="downloadCardBtn" style="background: linear-gradient(135deg, #00ff99, #00f0ff); color: #000; font-weight: 800;">
          📥 Download ID Badge (PNG)
        </button>
        <div style="display:flex;gap:10px;">
          <button type="button" class="action-btn" onclick="copyCardInfo()" style="flex:1;background:var(--bg-glass-subtle);color:var(--text-primary);border:1px solid var(--border-glass);">📋 Copy Data</button>
          <a href="setup-student.html" class="action-btn onboard" style="flex:1;text-decoration:none;">🚀 Setup Account</a>
        </div>
      </div>"""
card_processed = re.sub(old_actions, new_actions, card_processed, flags=re.DOTALL)

# Add scripts before </body>
card_processed = card_processed.replace('</body>',
    """  <script type="module" src="../src/js/theme.js"></script>
  <script type="module" src="../src/js/i18n.js"></script>
  <script type="module" src="../src/js/card-generator.js"></script>
</body>""")

write_file(os.path.join(PAGES_DIR, "profile-card.html"), card_processed)

# -------------------------------------------------------------
# 12. BUILD setup-student.html
# -------------------------------------------------------------
setup_raw = read_file(os.path.join(ZUNIX_DIR, "setup-student.html"))
setup_processed = replace_links_and_assets(setup_raw)
setup_processed = setup_processed.replace('src/styles/setup-student.css', '../src/styles/setup-student.css')
setup_processed = setup_processed.replace('src/styles/step6.css', '../src/styles/step6.css')
setup_processed = setup_processed.replace('<head>', '<head>\n  <link rel="stylesheet" href="../src/styles/theme.css" />')

# Replace script at bottom to use relative path
setup_processed = setup_processed.replace('src/js/main.js', '../src/js/main.js')
setup_processed = setup_processed.replace('</body>',
    """  <script type="module" src="../src/js/theme.js"></script>
  <script type="module" src="../src/js/i18n.js"></script>
</body>""")

write_file(os.path.join(PAGES_DIR, "setup-student.html"), setup_processed)

# -------------------------------------------------------------
# 13. BUILD login.html
# -------------------------------------------------------------
login_raw = read_file(os.path.join(ZUNIX_DIR, "LoginPage.html"))
login_processed = replace_links_and_assets(login_raw)
login_processed = login_processed.replace('src/styles/AccessPage.css', '../src/styles/AccessPage.css')
login_processed = login_processed.replace('<head>', '<head>\n  <link rel="stylesheet" href="../src/styles/theme.css" />\n  <link rel="stylesheet" href="../src/styles/Header.css" />')
login_processed = login_processed.replace('src/js/auth.js', '../src/js/auth.js')

# Add a top navigation bar with back to home
top_bar = """  <div style="position:fixed;top:0;left:0;right:0;padding:16px 28px;display:flex;align-items:center;justify-content:space-between;background:var(--header-bg);border-bottom:1px solid var(--header-border);backdrop-filter:blur(14px);z-index:1000;">
    <a href="../index.html" style="display:flex;align-items:center;gap:10px;text-decoration:none;font-weight:800;color:var(--accent-emerald);">
      <img src="../src/img/favicon-32x32.png" alt="Zunix Logo" style="width:28px;height:28px;" />
      <span>Zunix</span>
    </a>
    <div style="display:flex;align-items:center;gap:12px;">
      <a href="../index.html" style="color:var(--text-secondary);font-size:0.88rem;font-weight:600;text-decoration:none;">← Return Home</a>
      <button class="theme-toggle-btn" aria-label="Toggle Theme" title="Toggle Dark/Light Mode" style="width:32px;height:32px;font-size:0.9rem;">
        <span class="theme-icon">☀️</span>
      </button>
    </div>
  </div>
"""
login_processed = login_processed.replace('<body class="access-body">', f'<body class="access-body" style="padding-top:70px;">\n{top_bar}')
login_processed = login_processed.replace('</body>',
    """  <script type="module" src="../src/js/theme.js"></script>
  <script type="module" src="../src/js/i18n.js"></script>
</body>""")

write_file(os.path.join(PAGES_DIR, "login.html"), login_processed)

print("\nALL 16 SUBPAGES GENERATED IN pages/ SUCCESSFULLY!")
