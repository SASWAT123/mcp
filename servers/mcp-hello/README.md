# MCP Hello Server (Stage 0)

A minimal MCP server skeleton in Python.

## Tools

- **echo(text)** → returns `{ text, timestamp, request_id }`
- **health()** → returns `{ status: ok, version }`

## Run

```bash
python servers/mcp-hello/src/server.py health
python servers/mcp-hello/src/server.py echo "Hello MCP"
```
