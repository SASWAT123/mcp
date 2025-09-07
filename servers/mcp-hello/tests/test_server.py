from servers.mcp_hello.src.server import echo, health
import asyncio

def test_echo_contains_fields():
    result = asyncio.run(echo("hi"))
    assert result["text"] == "hi"
    assert "timestamp" in result and "request_id" in result

def test_health_ok():
    result = asyncio.run(health())
    assert result["status"] == "ok"
