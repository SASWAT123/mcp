import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
import server


def test_echo_contains_fields():
    result = server.echo("hi")
    assert result["text"] == "hi"
    assert "timestamp" in result
    assert "request_id" in result


def test_health_ok():
    result = server.health()
    assert result["status"] == "ok"
    assert result["version"] == "0.1.0"
