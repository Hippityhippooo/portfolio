#!/usr/bin/env python3
"""Copy the canonical shared blocks (src/base.css, src/chrome.html, src/docs.js) into every page between marker comments.
Not a build step: the pages are complete files at all times. Run after editing a canonical file:  python3 tools/sync.py
"""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
def block(text, start, end):
    i, j = text.find(start), text.find(end)
    if i < 0 or j < 0: raise SystemExit(f"marker missing: {start} / {end}")
    return text[i:j + len(end)]
base = block((root / "src/base.css").read_text(), "/* BASE v1 start */", "/* BASE v1 end */")
chrome_src = (root / "src/chrome.html").read_text()
head = block(chrome_src, "<!-- HEAD v1 start -->", "<!-- HEAD v1 end -->")
chrome = block(chrome_src, "<!-- CHROME v1 start -->", "<!-- CHROME v1 end -->")
foot = block(chrome_src, "<!-- FOOT v1 start -->", "<!-- FOOT v1 end -->")
docs = block((root / "src/docs.js").read_text(), "/* DOCS v1 start */", "/* DOCS v1 end */")
pairs = [("/* BASE v1 start */", "/* BASE v1 end */", base), ("<!-- HEAD v1 start -->", "<!-- HEAD v1 end -->", head),
         ("<!-- CHROME v1 start -->", "<!-- CHROME v1 end -->", chrome), ("<!-- FOOT v1 start -->", "<!-- FOOT v1 end -->", foot),
         ("/* DOCS v1 start */", "/* DOCS v1 end */", docs)]
pages = [p for p in root.glob("*.html")] + [root / "src/skeleton.html"]
bad = 0
for page in sorted(pages):
    text = page.read_text(); new = text; found = []
    for s, e, canon in pairs:
        i, j = new.find(s), new.find(e)
        if i < 0 and j < 0: continue
        if i < 0 or j < 0: print(f"{page.name}: unmatched marker {s}"); bad += 1; continue
        new = new[:i] + canon + new[j + len(e):]; found.append(s.split()[1])
    if not found: print(f"{page.name}: no markers (left alone)"); continue
    if new != text: page.write_text(new); print(f"{page.name}: updated {', '.join(found)}")
    else: print(f"{page.name}: in sync ({', '.join(found)})")
sys.exit(1 if bad else 0)
