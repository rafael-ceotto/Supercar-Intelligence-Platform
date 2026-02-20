import sys
import os

# Ensure project root is on sys.path for imports when running pytest
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.main import ask, AskRequest


def test_ask_mock_response():
    req = AskRequest(question="Qual a velocidade máxima?")
    resp = ask(req)
    assert isinstance(resp, dict)
    assert resp.get("question") == req.question
    assert "Mock answer" in resp.get("answer", "")
