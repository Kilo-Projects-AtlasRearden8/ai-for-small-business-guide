# Local LLM chat helper (Ollama)

A small, dependency-free Python script that chats with a model running on your
own computer through Ollama's local HTTP API (`http://localhost:11434`). Nothing
is sent to a cloud provider and no API key is required.

## Requirements

- Python 3
- [Ollama](https://ollama.com) installed and running on your computer
- A model downloaded, e.g. `ollama run llama3.2` (once, then it works offline)

## How to use

1. Start Ollama if it is not already running.
2. In a terminal, run:

   ```
   python3 tools/local-llm-cli/ollama_chat.py --model llama3.2 "Draft a short welcome email for a new customer of a small cleaning LLC."
   ```

3. The script sends your message to the local model and prints the reply.
4. To see which models you have downloaded:

   ```
   python3 tools/local-llm-cli/ollama_chat.py --list
   ```

## Safety

- This talks to `localhost` only. No data leaves your machine.
- Still never paste real customer names, addresses, payment details, or tax
  numbers into the prompt. Use fake examples.
- Read the model's reply before using it — local models can still make things
  up.

## Credit

Copyright (c) 2026 Asdale Dynamics, LLC. Open-source utility — free to use,
modify, and share.
