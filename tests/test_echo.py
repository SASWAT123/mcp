import sys
import os

sys.path.append(
    os.path.join(os.path.dirname(__file__), "..", "servers", "mcp-hello", "src")
)
from server import echo, health


def test_echo_has_fields():
    out = echo("hi")
    assert out["text"] == "hi"
    assert "timestamp" in out and "request_id" in out


def test_health_ok():
    assert health()["status"] == "ok"
