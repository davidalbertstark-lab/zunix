import re

path = "/home/stark/zunix/index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Ensure theme.css is loaded in head
if "src/styles/theme.css" not in html:
    html = html.replace('<link rel="stylesheet" href="src/styles/index.css"/>',
        '<link rel="stylesheet" href="src/styles/theme.css" />\n  <link rel="stylesheet" href="src/styles/index.css" />')

# 2. Universal Header replacement
new_header = """<header class="header">
    <div class="logo">
      <a href="index.html">
        <img src="src/img/favicon-32x32.png" alt="Zunix Logo" />
        <span>Zunix</span>
      </a>
    </div>

    <input type="checkbox" id="nav-toggle" class="nav-toggle" />

    <nav class="nav">
      <ul>
        <li><a href="pages/features.html" data-i18n="nav_features">Features</a></li>
        <li><a href="pages/rewards.html" data-i18n="nav_rewards">Rewards</a></li>
        <li><a href="pages/programs.html" data-i18n="nav_programs">Programs</a></li>
        <li><a href="pages/events.html" data-i18n="nav_events">Events</a></li>
        <li><a href="pages/communities.html" data-i18n="nav_communities">Communities</a></li>
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
          <a href="pages/login.html#loginBox" class="header-btn header-btn-login" data-i18n="nav_login">Log In</a>
          <a href="pages/login.html#signupBox" class="header-btn header-btn-signup" data-i18n="nav_signup">Sign Up</a>
        </div>
      </div>
    </nav>

    <label for="nav-toggle" class="nav-toggle-label" aria-label="Toggle navigation menu">
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </label>
  </header>"""

html = re.sub(r'<header class="header">.*?</header>', new_header, html, flags=re.DOTALL)

# 3. Hero content i18n & links
html = re.sub(r'<h1 class="headline">.*?</h1>', '<h1 class="headline" data-i18n="hero_headline">Empower Your Student Journey with Zunix</h1>', html, flags=re.DOTALL)
html = re.sub(r'<p class="subtext">.*?</p>', '<p class="subtext" data-i18n="hero_subtext">Access study tools, launch side hustles, earn real rewards, and level up your campus game, all from one do-it-all hub made for students who want more.</p>', html, flags=re.DOTALL)

# Hero CTA buttons
hero_cta = """<div class="cta-button" style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin-top:24px;">
      <a href="pages/login.html#signupBox" class="btns primary-btn" data-i18n="btn_join_now">Join Now</a>
      <a href="pages/features.html" class="btns secondary-btn" data-i18n="btn_explore">Explore Hub</a>
      <a href="pages/profile-card.html" class="btns" style="background:rgba(255,255,255,0.06);border:1px solid var(--border-glass);color:var(--accent-cyan);font-weight:700;">🪪 Student ID Card</a>
      <a href="pages/rewards.html" class="btns" style="background:rgba(255,255,255,0.06);border:1px solid var(--border-glass);color:var(--accent-gold);font-weight:700;">⚡ XP Simulator</a>
    </div>"""
html = re.sub(r'<div class="cta-button">.*?</div>', hero_cta, html, flags=re.DOTALL)

# Hero Badges
html = html.replace('<span class="label">Learn</span>', '<span class="label" data-i18n="badge_learn">Learn</span>')
html = html.replace('<span class="label">Earn</span>', '<span class="label" data-i18n="badge_earn">Earn</span>')
html = html.replace('<span class="label">Grow</span>', '<span class="label" data-i18n="badge_grow">Grow</span>')
html = html.replace('<span class="label">Connect</span>', '<span class="label" data-i18n="badge_connect">Connect</span>')

# 4. Feature Section Heading
html = html.replace('<h2>Designed for the Modern Student</h2>', '<h2 data-i18n="feat_title">Engineered for Student Excellence</h2>')

# 5. How It Works Heading
html = html.replace('<h1>How It Works</h1>', '<h1 data-i18n="how_title">How Zunix Works</h1>')

# 6. PreFooter links
html = html.replace('href="ContactUsPage.html"', 'href="pages/contact.html"')
html = html.replace('href="Faq.html"', 'href="pages/faq.html"')

# 7. Footer links
footer_links_map = {
    'href="Partners.html"': 'href="pages/partners.html"',
    'href="PrivacyPolicy.html"': 'href="pages/privacy.html"',
    'href="CopyrightPolicy.html"': 'href="pages/copyright.html"',
    'href="Terms.html"': 'href="pages/terms.html"',
    'href="AboutUs.html"': 'href="pages/about.html"',
    'href="CookiePolicy.html"': 'href="pages/cookies.html"'
}
for old_f, new_f in footer_links_map.items():
    html = html.replace(old_f, new_f)

# 8. Footer language switcher data-switch-lang
html = html.replace('data-key="lang-option-de"', 'data-switch-lang="de" data-key="lang-option-de"')
html = html.replace('data-key="lang-option-en"', 'data-switch-lang="en" data-key="lang-option-en"')
html = html.replace('data-key="lang-option-fr"', 'data-switch-lang="fr" data-key="lang-option-fr"')
html = html.replace('data-key="lang-option-ar"', 'data-switch-lang="ar" data-key="lang-option-ar"')

# 9. Scripts at bottom
if "src/js/i18n.js" not in html:
    html = html.replace('</body>',
        '  <script type="module" src="src/js/theme.js"></script>\n  <script type="module" src="src/js/i18n.js"></script>\n</body>')

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html successfully")
