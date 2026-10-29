#!/usr/bin/env python3
"""Verify the AI for Small Businesses and LLCs project.

Checks:
  * LICENSE contains the exact copyright line
  * README credits Asdale Dynamics, LLC
  * every HTML file parses with no mismatched/unclosed tags
  * every internal link resolves to an existing file
  * no .github/workflows files
  * no secrets / API-key patterns in committed files
  * Python tools compile cleanly
Run: python3 scripts/verify.py
"""
from __future__ import annotations

import html.parser
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC = os.path.join(ROOT, "static")
TOOLS = os.path.join(ROOT, "tools")

errors = []

VOID_TAGS = {
    "area", "base", "br", "col", "embed", "hr", "img", "input",
    "link", "meta", "param", "source", "track", "wbr",
}

EXPECTED_COPYRIGHT = "Copyright (c) 2026 Asdale Dynamics, LLC"


class HTMLChecker(html.parser.HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.stack = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID_TAGS:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in VOID_TAGS:
            return
        if not self.stack or self.stack[-1] != tag:
            errors.append(
                f"{self.path}: mismatched close tag </{tag}> (open tail: {self.stack[-3:]})"
            )
        else:
            self.stack.pop()

    def finish(self):
        if self.stack:
            errors.append(f"{self.path}: unclosed tags {self.stack}")


class LinkFinder(html.parser.HTMLParser):
    def __init__(self, path, base_dir, existing):
        super().__init__()
        self.path = path
        self.base_dir = base_dir
        self.existing = existing

    def     handle_starttag(self, tag, attrs):
        for attr, val in attrs:
            if attr in ("href", "src") and val and not val.startswith(
                ("http://", "https://", "mailto:", "#")
            ):
                target = os.path.normpath(os.path.join(self.base_dir, val.lstrip("/")))
                if not os.path.exists(target):
                    errors.append(f"{self.path}: broken link {val} -> {target}")


def read(path):
    with open(path, "r", encoding="utf-8") as fh:
        return fh.read()


# --- Collect HTML files -----------------------------------------------------
html_files = []
for dirpath, _dirnames, filenames in os.walk(STATIC):
    for fn in filenames:
        if fn.endswith(".html"):
            html_files.append(os.path.join(dirpath, fn))

existing = set(os.path.normpath(p) for p in html_files)

# --- LICENSE ----------------------------------------------------------------
license_text = read(os.path.join(ROOT, "LICENSE"))
if license_text.count(EXPECTED_COPYRIGHT) != 1:
    errors.append("LICENSE must contain the exact line once: " + EXPECTED_COPYRIGHT)

# --- README -----------------------------------------------------------------
readme = read(os.path.join(ROOT, "README.md"))
if "Asdale Dynamics, LLC" not in readme:
    errors.append("README missing Asdale Dynamics, LLC credit")
if EXPECTED_COPYRIGHT not in readme:
    errors.append("README missing exact copyright line")

# --- Scan all text-like files (workflows + secrets) -------------------------
for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d != ".git"]
    for fn in filenames:
        path = os.path.join(dirpath, fn)
        rel = os.path.relpath(path, ROOT)
        if ".github/workflows" in rel:
            errors.append(f"{rel}: .github/workflows file present (not allowed)")
        try:
            text = read(path)
        except Exception:
            continue
        if rel == "scripts/verify.py":
            continue
        secret_patterns = [
            (r"sk-[A-Za-z0-9]{16,}", "sk-"),
            (r"AKIA[A-Z0-9]{12,}", "AKIA"),
            (r"ghp_[A-Za-z0-9]{16,}", "ghp_"),
            (r"api_key\s*[:=]\s*[\"']?[A-Za-z0-9]", "api_key"),
            (r"secret\s*[:=]\s*[\"']?[A-Za-z0-9]", "secret"),
        ]
        for pat, label in secret_patterns:
            if re.search(pat, text, re.IGNORECASE):
                errors.append(f'{rel}: possible secret pattern "{label}"')

# --- HTML parse + links -----------------------------------------------------
for p in sorted(html_files):
    content = read(p)
    checker = HTMLChecker(p)
    checker.feed(content)
    checker.finish()

    base_dir = os.path.dirname(p)
    finder = LinkFinder(p, base_dir, existing)
    finder.feed(content)

# --- Python tools compile ---------------------------------------------------
py_count = 0
for dirpath, _dirnames, filenames in os.walk(TOOLS):
    for fn in filenames:
        if fn.endswith(".py"):
            py_count += 1
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, ROOT)
            try:
                compile(read(path), path, "exec")
            except SyntaxError as exc:
                errors.append(f"{rel}: Python syntax error: {exc}")

# --- Report -----------------------------------------------------------------
print("HTML files checked:", len(html_files))
print("Python tools checked:", py_count)

if errors:
    print("ERRORS:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print("All checks passed: HTML parses, internal links resolve, credits present, "
      "no workflows/secrets, Python tools compile.")
