# Minimal MCP server skeleton (stdio)

A bare-bones [Model Context Protocol](https://modelcontextprotocol.io) server
written in Python that speaks JSON-RPC over standard input/output. It implements
`initialize`, `tools/list`, and `tools/call` and exposes one sample tool. It is
a starting point you can copy and extend — it connects to no real services and
holds no secrets.

## What MCP is (plain English)

MCP is like a USB port for AI: one standard way for an AI assistant to connect
to tools and data you already use, instead of building a separate plug-in for
every tool. A small business might eventually use MCP to let an AI read local
files or a calendar, but you should never connect it to bank accounts, email
passwords, or real customer data.

## How to run

The skeleton speaks on stdin/stdout, so it is meant to be launched by an MCP
client (for example, a desktop AI app that supports MCP). To try it directly:

```
python3 tools/mcp-server-template/mcp_server.py
```

Then type JSON-RPC requests, one per line, ending each with Enter:

```json
{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{}}}
{"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}
{"jsonrpc":"2.0","id":3,"method":"tools/call","params":{"name":"echo_business_info","arguments":{"text":"Hello from Asdale Dynamics"}}}
```

Press Ctrl-D to quit.

## Sample tool: `echo_business_info`

The only tool included echoes back a short string. It demonstrates the request/
response shape without touching any real data. Replace it with your own tools
that read only local, non-sensitive files.

## Safety

- Never wire this server to a bank account, email password, customer database,
  or any system holding real customer or financial data.
- Use only fake or public data when developing tools against it.
- Review any tool's code before exposing it to an AI client.

## Credit

Copyright (c) 2026 Asdale Dynamics, LLC. Open-source template — free to use,
modify, and share.
