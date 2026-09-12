import re
import os

PAGES_DIR = "/home/stark/zunix/pages"
files_to_fix = ["profile-card.html", "setup-student.html", "login.html"]

for fname in files_to_fix:
    fpath = os.path.join(PAGES_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace ../../ with ../
    fixed = content.replace("../../", "../")

    with open(fpath, "w", encoding="utf-8") as f:
        f.write(fixed)
    print(f"Fixed {fname}")

