from __future__ import annotations
import json
import time
import uuid
from typing import Any, Dict

# Placeholder "MCP-like" harness to keep Stage 0 focused.
# Later stages: swap in your chosen MCP SDK server class and tool registration.


def echo(text: str) -> Dict[str, Any]:
    return {
        "text": text,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "request_id": str(uuid.uuid4()),
    }


def health() -> Dict[str, str]:
    return {"status": "ok", "version": "0.1.0"}


def main():
    # naïve CLI harness: `python server.py echo "hello"`
    import sys

    if len(sys.argv) < 2:
        print("usage: server.py [echo|health] [args...]")
        raise SystemExit(2)

    cmd = sys.argv[1]
    if cmd == "echo":
        text = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
        print(json.dumps(echo(text)))
    elif cmd == "health":
        print(json.dumps(health()))
    else:
        raise SystemExit(f"unknown command: {cmd}")


if __name__ == "__main__":
    main()
