# STATUS

## What was built

A beginner manual and static HTML site on AI for small businesses and LLCs,
built for **Asdale Dynamics, LLC** (Indiana, formed October 2026), founded by
Dylan Asdale (registered nurse, AI author, *The Massive AI Manual*,
dylanasdale.github.io).

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
- `static/docs/*.html` — one HTML page per manual, shared nav, print button
- `static/planners/` — 5 print-ready planners + index: budget sheet,
  paperwork tracker, low-energy day (ADHD-friendly), customer email worksheet,
  marketing week
- `static/css/style.css` — warm print-friendly styles with `@media print`
- `static/js/app.js` — print button and focus styles

### `tools/` — open-source apps and templates (new, fills the apps/templates gap)

- `tools/prompt-tool/index.html` — client-side AI prompt builder (no backend,
  no API key; prompt assembled in the browser)
- `tools/prompt-tool/README.md`
- `tools/local-llm-cli/ollama_chat.py` — chat with a model running locally via
  Ollama's `localhost:11434` API (no cloud, no API key)
- `tools/local-llm-cli/README.md`
- `tools/mcp-server-template/mcp_server.py` — minimal stdio MCP server
  skeleton (initialize, tools/list, tools/call, one sample tool)
- `tools/mcp-server-template/README.md`
- `tools/agent-skill-template/draft_invoice_reminder.py` — sample agent skill
  that drafts an invoice-reminder email from example (fake) inputs
- `tools/agent-skill-template/skill_manifest.json`
- `tools/agent-skill-template/README.md`
- `tools/README.md` — tool index

### `scripts/`
- `scripts/verify.py` — in-repo verification (HTML parse, internal links,
  LICENSE/README credits, no workflows/secrets, Python compile)

### Other files

- `LICENSE` — MIT, copyright line exactly
  `Copyright (c) 2026 Asdale Dynamics, LLC`
- `README.md` — warm, structured, credits Asdale Dynamics, LLC
- `STATUS.md` — this file

## How to run it

No install, no build step, no server required:

1. Open `static/index.html` in any web browser, or open any
   `static/docs/*.html` or `static/planners/*.html` file directly.
2. To print a planner or manual page, press Ctrl+P (Cmd+P on Mac) or use the
   "Print this page" button. Print styles hide headers/navigation.
3. Read Markdown sources in `docs/` in any text editor or Markdown viewer.
4. Tools: open `tools/prompt-tool/index.html` in a browser; run
   `python3 tools/local-llm-cli/ollama_chat.py "..."` (requires local Ollama);
   run `python3 tools/mcp-server-template/mcp_server.py` and send JSON-RPC
   lines on stdin; run
   `python3 tools/agent-skill-template/draft_invoice_reminder.py --customer
   "..." --invoice "..." --due "..." --amount "..."`.

## Verification results

Run `python3 scripts/verify.py`:

- All 27 HTML files parse with no mismatched or unclosed tags.
- All internal links resolve to existing files (css, js, html, directories).
- `LICENSE` contains the exact copyright line once.
- `README.md` and every HTML page credit Asdale Dynamics, LLC.
- No `.github/workflows` files.
- No secrets/API-key patterns (sk-, AKIA, ghp_, api_key=, secret=) in
  committed files.
- 3 Python tools compile cleanly; agent skill and CLI smoke-tested.

## Known gaps

- Free AI tiers and model availability change over time; model/service mentions
  reflect the time of writing (October 2026) and should be re-checked before
  relying on them.
- Local AI section names example apps (Ollama, LM Studio, Jan) but does not
  cover every operating system in detail.
- No site search; navigation is via the shared menu and landing-page cards.
- The MCP skeleton and agent skill are templates to extend, not turn-key
  integrations with real services.
- Educational healthcare content is explicitly not medical advice; tax and
  bookkeeping content is not professional advice. Disclaimers appear in the
  relevant chapters and the footer.

## Git

Initialized with `git init`. Commits use the existing git identity, plain
messages, no `Co-authored-by` trailers. Not pushed, no remote created,
nothing published.
