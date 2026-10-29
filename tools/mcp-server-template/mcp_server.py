#!/usr/bin/env python3
"""Minimal stdio-based MCP (Model Context Protocol) server skeleton.

Speaks JSON-RPC 2.0 over stdin/stdout. Implements initialize, tools/list, and
tools/call. Exposes one harmless sample tool. Intended as a template to copy
and extend with your own local, non-sensitive tools.
"""
from __future__ import annotations

import json
import sys
from typing import Any, Dict, Optional

PROTOCOL_VERSION = "2024-11-05"


def make_response(id_: Any, result: Optional[Dict[str, Any]] = None, error: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    resp: Dict[str, Any] = {"jsonrpc": "2.0", "id": id_}
    if error is not None:
        resp["error"] = error
    else:
        resp["result"] = result if result is not None else {}
    return resp


def tool_echo_business_info(arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Sample tool: safely echoes back a short string. No real data is used."""
    text = arguments.get("text", "")
    return {"content": [{"type": "text", "text": "Echo: " + str(text)}]}


TOOLS = {
    "echo_business_info": {
        "name": "echo_business_info",
        "description": "Echoes back a short string. Sample tool only; replace with your own local, non-sensitive tool.",
        "inputSchema": {
            "type": "object",
            "properties": {"text": {"type": "string", "description": "Text to echo back"}},
            "required": ["text"],
        },
        "handler": tool_echo_business_info,
    }
}


def handle_initialize(params: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "protocolVersion": PROTOCOL_VERSION,
        "capabilities": {"tools": {}},
        "serverInfo": {"name": "asdale-mcp-skeleton", "version": "0.1.0"},
    }


def handle_tools_list(params: Dict[str, Any]) -> Dict[str, Any]:
    return {"tools": [
        {"name": t["name"], "description": t["description"], "inputSchema": t["inputSchema"]}
        for t in TOOLS.values()
    ]}


def handle_tools_call(params: Dict[str, Any]) -> Dict[str, Any]:
    name = params.get("name")
    arguments = params.get("arguments", {})
    tool = TOOLS.get(name)
    if tool is None:
        raise ValueError(f"Unknown tool: {name}")
    return tool["handler"](arguments)


METHODS = {
    "initialize": handle_initialize,
    "tools/list": handle_tools_list,
    "tools/call": handle_tools_call,
}


def process(line: str) -> Optional[str]:
    line = line.strip()
    if not line:
        return None
    try:
        req = json.loads(line)
    except json.JSONDecodeError:
        return json.dumps(make_response(None, error={"code": -32700, "message": "Parse error"}))
    rid = req.get("id")
    method = req.get("method")
    params = req.get("params", {})
    handler = METHODS.get(method)
    if handler is None:
        return json.dumps(make_response(rid, error={"code": -32601, "message": f"Method not found: {method}"}))
    try:
        result = handler(params)
        return json.dumps(make_response(rid, result=result))
    except Exception as exc:  # keep the server alive on tool errors
        return json.dumps(make_response(rid, error={"code": -32603, "message": str(exc)}))


def main() -> None:
    for line in sys.stdin:
        out = process(line)
        if out is not None:
            sys.stdout.write(out + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
