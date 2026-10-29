#!/usr/bin/env python3
"""Draft a short, polite invoice-reminder email from example (fake) inputs.

This is a template agent skill. Replace the fields with your own and run it
manually or wire it into an agent. Never use real customer or financial data.
"""
from __future__ import annotations

import argparse


def draft(customer: str, invoice: str, due: str, amount: str) -> str:
    subject = "Friendly reminder: invoice " + invoice
    body = (
        "Hi " + customer + ",\n\n"
        + "This is a friendly reminder that invoice " + invoice + " for "
        + amount + " was due on " + due + ".\n\n"
        + "If you have already sent the payment, please disregard this message.\n"
        + "Otherwise, you can pay here: [your payment link]\n\n"
        + "Thanks,\n"
        + "[Your Name]\n"
        + "[Your Business Name]"
    )
    return "Subject: " + subject + "\n\n" + body


def main() -> None:
    parser = argparse.ArgumentParser(description="Draft an invoice reminder email (example data only).")
    parser.add_argument("--customer", required=True, help="Fake customer name.")
    parser.add_argument("--invoice", required=True, help="Example invoice number.")
    parser.add_argument("--due", required=True, help="Due date, e.g. 2026-11-15.")
    parser.add_argument("--amount", required=True, help="Amount owed, e.g. 120.00.")
    args = parser.parse_args()
    print(draft(args.customer, args.invoice, args.due, args.amount))


if __name__ == "__main__":
    main()
