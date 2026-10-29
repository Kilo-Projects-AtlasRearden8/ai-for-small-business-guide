#!/usr/bin/env python3
"""Chat with a local Ollama model over HTTP (localhost:11434).

No API key, no cloud. Nothing you type leaves your machine.
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request

BASE = "http://localhost:11434"


def api_get(path: str) -> object:
    with urllib.request.urlopen(BASE + path, timeout=10) as resp:
        return json.loads(resp.read().decode("utf-8"))


def api_post(path: str, payload: dict) -> object:
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        BASE + path,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def list_models() -> None:
    try:
        data = api_get("/api/tags")
    except Exception as exc:
        print(f"Could not reach Ollama at {BASE}. Is it running? ({exc})")
        sys.exit(1)
    models = data.get("models", [])
    if not models:
        print("No models downloaded yet. Run: ollama run llama3.2")
        return
    print("Local models:")
    for m in models:
        print(" - " + m.get("name", "unknown"))


def chat(model: str, message: str) -> None:
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful, plain-spoken assistant for a small business owner. Be concise, warm, and never present opinion as fact.",
            },
            {"role": "user", "content": message},
        ],
        "stream": False,
    }
    try:
        data = api_post("/api/chat", payload)
    except Exception as exc:
        print(f"Could not chat with Ollama at {BASE}. Is it running and is '{model}' downloaded? ({exc})")
        sys.exit(1)
    print(data.get("message", {}).get("content", "(no reply)"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Chat with a local Ollama model.")
    parser.add_argument("message", nargs="?", help="Message to send to the model.")
    parser.add_argument("--model", default="llama3.2", help="Local model name (default: llama3.2).")
    parser.add_argument("--list", action="store_true", help="List downloaded models.")
    args = parser.parse_args()

    if args.list:
        list_models()
        return
    if not args.message:
        parser.print_help()
        sys.exit(2)
    chat(args.model, args.message)


if __name__ == "__main__":
    main()
