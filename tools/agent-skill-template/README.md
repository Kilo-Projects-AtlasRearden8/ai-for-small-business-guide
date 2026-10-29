# Agent skill template

An "agent skill" is a discrete, testable task an AI assistant can perform on
your behalf — for example, drafting an invoice-reminder email. This folder is a
template you can copy to build your own skills. It contains a skill manifest
and a sample skill that drafts an invoice reminder from safe (fake) inputs.

## What goes in a skill

- A clear name and one-sentence description
- Defined inputs (what the agent needs to know) and outputs (what it produces)
- A short implementation (a script or prompt template)
- A safety note: never use real customer names, addresses, payment details, or
  tax numbers

## Sample skill: draft invoice reminder

`draft_invoice_reminder.py` takes a fake customer name, invoice number, due
date, and amount, and returns a short, polite reminder email. It is a template
— replace the inputs with your own fields and connect it to an agent or run it
manually.

### Example

```
python3 tools/agent-skill-template/draft_invoice_reminder.py \
  --customer "Customer A" --invoice "INV-0001" --due "2026-11-15" --amount "120.00"
```

Outputs a draft email body you can review and paste into your own email
program.

### Manifest

`skill_manifest.json` describes the skill so an agent framework can discover
it. Edit the name, description, and input schema to match your skill.

## Safety

- This skill handles example/fake data only.
- Never feed real customer or financial data into an agent skill.
- Review the drafted output yourself before sending it to anyone.

## Credit

Copyright (c) 2026 Asdale Dynamics, LLC. Open-source template — free to use,
modify, and share.
