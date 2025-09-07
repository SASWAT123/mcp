from __future__ import annotations
import asyncio
import os
import time
import uuid
from typing import Any, Dict

from mcp.server.fastmcp import FastMCP, Context

app = FastMCP("mcp-hello")

@app.tool()
async def echo(text: str) -> Dict[str, Any]:
    """
    Echo the given text back with metadata.
    """
    return {
        "text": text,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "request_id": str(uuid.uuid4()),
    }

@app.tool()
async def health() -> Dict[str, str]:
    """
    Basic server health.
    """
    return {"status": "ok", "version": os.getenv("MCP_HELLO_VERSION", "0.1.0")}

# Optional: show how to use per-call context (logging, tracing, auth etc.)
@app.tool()
async def whoami(ctx: Context) -> Dict[str, str]:
    """
    Returns connection metadata from the MCP context (if provided by client).
    """
    return {"client": ctx.client or "unknown"}

if __name__ == "__main__":
    # Start a stdio server so MCP clients can launch us as a subprocess.
    # You can also expose SSE/HTTP transports; stdio is the most universal.
    asyncio.run(app.run_stdio_async())
