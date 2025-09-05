from __future__ import annotations
import json
import sys
import time
import uuid
from typing import Any, Dict


# Tool: echo
def echo(text: str) -> Dict[str, Any]:
    """Echo back text with timestamp + request ID"""
    return {
        "text": text,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "request_id": str(uuid.uuid4())
    }


# Tool: health
def health() -> Dict[str, str]:
    """Return server health info"""
    return {"status": "ok", "version": "0.1.0"}


# Very simple MCP-like harness (simulate request/response)
def main():
    if len(sys.argv) < 2:
        print("Usage: server.py [tool] [args...]")
        sys.exit(1)

    tool = sys.argv[1]

    if tool == "echo":
        text = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
        print(json.dumps(echo(text)))
    elif tool == "health":
        print(json.dumps(health()))
    else:
        sys.exit(f"Unknown tool: {tool}")


if __name__ == "__main__":
    main()
