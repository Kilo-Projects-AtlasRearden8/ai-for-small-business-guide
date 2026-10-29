# STATUS

## What was built

A beginner manual and static HTML site on AI for small businesses and LLCs,
built for Asdale Dynamics, LLC (Indiana, formed October 2026), founded by Dylan
Asdale (registered nurse, AI author, *The Massive AI Manual*, dylanasdale.github.io).

### `docs/` — 20 Markdown manuals (plain English, step by step)

00-index, 01-getting-started, 02-llc-small-business, 03-admin-help,
04-marketing, 05-customer-emails, 06-bookkeeping, 07-privacy-safety,
08-free-models, 09-printable-planners, 10-agents-mcp, 11-local-ai,
12-free-coding-github, 13-automation, 14-healthcare-worker-ai,
15-kdp-publishing, 16-reselling, 17-gaming-chess, appendix-glossary,
appendix-resources.

Topics: AI tools, free models, admin help, marketing, customer email templates,
bookkeeping basics, privacy and safety, agents/MCP, local AI, free AI coding,
GitHub, automation, KDP/publishing, reselling (eBay/Amazon), healthcare-worker
education aids, FFXIV/chess extras, printable planners, glossary, resources.

### `static/` — polished static HTML site (no build step)

- `static/index.html` — landing page with topic cards and golden rules
- `static/docs/*.html` — one HTML page per manual, with shared nav and print button
- `static/planners/` — 5 print-ready planner pages + index: budget sheet,
  paperwork tracker, low-energy day (ADHD-friendly), customer email worksheet,
  marketing week
- `static/css/style.css` — warm print-friendly styles with `@media print`
- `static/js/app.js` — print button and focus styles

### Other files

- `LICENSE` — MIT, copyright line exactly `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — project description crediting Asdale Dynamics, LLC
- `STATUS.md` — this file

## How to run it

No install, no build step, no server required:

1. Open `static/index.html` in any web browser, or open any
   `static/docs/*.html` or `static/planners/*.html` file directly.
2. To print a planner or manual page, press Ctrl+P (Cmd+P on Mac) or use the
   "Print this page" button. Print styles hide headers/navigation and keep
   planner forms clean.
3. Markdown sources in `docs/` can be read in any text editor or rendered by
   any Markdown viewer.

## Verification results

- Custom checker (`/tmp/kilo/verify.py`, not committed): all 27 HTML files
  parse with no mismatched or unclosed tags.
- All internal links resolve to existing files.
- `LICENSE` contains the exact copyright line `Copyright (c) 2026 Asdale Dynamics, LLC`.
- `README.md` and every HTML page credit Asdale Dynamics, LLC.
- No `.github/workflows` files; no secrets, API keys, or personal data in any file.
- CSS brace count balanced; `@media print` present.
- Every Markdown doc starts with a heading and ends with the copyright line.

## Known gaps

- No automated test suite or lint tooling in the repo; verification was done
  with the one-off HTML/link checker. Static HTML has no build to break.
- Free AI tiers and model availability change over time; model/service mentions
  reflect the time of writing (October 2026) and should be re-checked before
  relying on them.
- No site search; navigation is via the shared menu and landing-page cards.
- Local AI section names example apps (Ollama, LM Studio, Jan) but does not
  cover every operating system in detail.
- Educational healthcare content is explicitly not medical advice; tax and
  bookkeeping content is not professional advice. Disclaimers appear in the
  relevant chapters and the footer.

## Git

Initialized with `git init`. One commit, plain message, existing git identity,
no `Co-authored-by` trailers. Not pushed, no remote created, nothing published.
