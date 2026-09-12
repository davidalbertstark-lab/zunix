import os

ZUNIX_DIR = "/home/stark/zunix"

stubs = {
    "Features.html": ("pages/features.html", "Zunix Features"),
    "Rewards.html": ("pages/rewards.html", "Zunix Rewards"),
    "Programs.html": ("pages/programs.html", "Zunix Programs"),
    "Events.html": ("pages/events.html", "Zunix Events"),
    "Communities.html": ("pages/communities.html", "Zunix Communities"),
    "AboutUs.html": ("pages/about.html", "About Zunix"),
    "ContactUsPage.html": ("pages/contact.html", "Contact Zunix"),
    "Faq.html": ("pages/faq.html", "Zunix FAQ"),
    "Partners.html": ("pages/partners.html", "Zunix Partners"),
    "Terms.html": ("pages/terms.html", "Zunix Terms of Service"),
    "PrivacyPolicy.html": ("pages/privacy.html", "Zunix Privacy Policy"),
    "CookiePolicy.html": ("pages/cookies.html", "Zunix Cookie Policy"),
    "CopyrightPolicy.html": ("pages/copyright.html", "Zunix Copyright Policy"),
    "LoginPage.html": ("pages/login.html", "Zunix Login"),
    "setup-student.html": ("pages/setup-student.html", "Zunix Student Setup"),
    "profile-card.html": ("pages/profile-card.html", "Zunix Student ID Card")
}

for filename, (target, title) in stubs.items():
    filepath = os.path.join(ZUNIX_DIR, filename)
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="refresh" content="0; url={target}" />
  <title>Redirecting to {title}...</title>
  <script>location.replace('{target}' + (location.hash || ''));</script>
</head>
<body style="font-family:sans-serif;text-align:center;padding:50px;background:#0a0d14;color:#f0f6fc;">
  <p>Redirecting to <a href="{target}" style="color:#00ff99;">{title}</a>...</p>
</body>
</html>
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print("Updated all root redirect stubs with location.hash forwarding!")
