import os
import re
from urllib.parse import urlparse

ZUNIX_DIR = "/home/stark/zunix"

broken_links = []
total_checked = 0

html_files = []
for root, dirs, files in os.walk(ZUNIX_DIR):
    if ".git" in root:
        continue
    for f in files:
        if f.endswith(".html"):
            html_files.append(os.path.join(root, f))

print(f"Checking {len(html_files)} HTML files for broken references...")

for file_path in html_files:
    rel_file = os.path.relpath(file_path, ZUNIX_DIR)
    file_dir = os.path.dirname(file_path)

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Find all href and src
    matches = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
    for target in matches:
        total_checked += 1
        # Skip external, hash-only, mailto, tel, javascript
        if target.startswith(("http://", "https://", "mailto:", "tel:", "javascript:", "#", "data:")):
            continue

        # Strip anchor and query
        clean_target = target.split("#")[0].split("?")[0]
        if not clean_target:
            continue

        # Resolve path
        resolved_path = os.path.normpath(os.path.join(file_dir, clean_target))

        if not os.path.exists(resolved_path):
            broken_links.append({
                "file": rel_file,
                "ref": target,
                "resolved": os.path.relpath(resolved_path, ZUNIX_DIR)
            })

print(f"Total links/assets checked: {total_checked}")
if broken_links:
    print(f"FOUND {len(broken_links)} BROKEN REFERENCES:")
    for b in broken_links:
        print(f"  [{b['file']}] -> '{b['ref']}' (looked for: {b['resolved']})")
else:
    print("SUCCESS: 0 BROKEN REFERENCES FOUND! ALL LINKS & ASSETS RESOLVE CLEANLY!")
