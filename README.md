# AI for Small Businesses and LLCs

A beginner-friendly manual and static HTML site that explains how small
businesses and LLCs can use free AI models for admin work, marketing, customer
emails, and bookkeeping — plain English, step by step, with printable planners
and open-source tools.

## Who this is for

This project was built for **Asdale Dynamics, LLC** (Indiana, formed October
2026) and its founder, Dylan Asdale — a registered nurse turned AI author — and
for anyone running a small business, side hustle, or author/publishing LLC who
wants practical, local-first AI help without spending money on subscriptions.

It supports the work behind Dylan Asdale's book **The Massive AI Manual** and
the hub site **dylanasdale.github.io**, where AI is explained "like a friend
would": plain English, step by step, never condescending.

## What's inside

- `docs/` — 20 substantive beginner manuals in Markdown:
  - Getting started with AI and free models
  - AI for LLCs and small businesses
  - Admin help, marketing help, customer email templates, bookkeeping basics
  - Privacy and safety (never paste real customer or financial data)
  - Agents, MCP, local AI, free AI coding, GitHub, automation
  - KDP/book publishing, reselling (eBay/Amazon), healthcare-worker aids,
    gaming (FFXIV) and chess tools
  - Printable planners, glossary, resources
- `static/` — a polished, static HTML version of the manuals with print-ready
  planner pages. No build step required; open any `.html` file in a browser.
- `tools/` — open-source apps and templates the LLC can publish or share:
  - `prompt-tool/` — client-side AI prompt builder
  - `local-llm-cli/` — chat with a model running locally via Ollama
  - `mcp-server-template/` — minimal stdio MCP server skeleton
  - `agent-skill-template/` — sample agent skill plus manifest

## How to use it

1. **Read the manuals.** Start with `docs/01-getting-started.md` or open
   `static/index.html` in a browser and work through the topic cards.
2. **Print the planners.** Open any page under `static/planners/` and press
   Ctrl+P (Cmd+P on Mac) to print a paper planner — budget sheet, paperwork
   tracker, low-energy day, email worksheet, marketing week.
3. **Try the tools.** Open `tools/prompt-tool/index.html` to build a prompt,
   or run `tools/local-llm-cli/ollama_chat.py` to chat with a local model.
   Nothing is sent to a server and no API key is required.

## Golden rules

- **Never paste real customer names, addresses, payment details, or tax numbers
  into an AI tool.** Use fake examples instead.
- **AI is a helper, not an accountant or a lawyer.** Always double-check math
  and legal paperwork yourself.
- **Start small.** One task, one chat, one free model.
- **Keep a human in the loop.** Read and approve everything before it goes to a
  customer or the government.

## Credit

Copyright (c) 2026 Asdale Dynamics, LLC. Written and maintained by Asdale
Dynamics, LLC (Dylan Asdale, founder).

## License

MIT License. See `LICENSE` for details.
