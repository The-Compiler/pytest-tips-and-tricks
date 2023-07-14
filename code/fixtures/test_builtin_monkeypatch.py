import os
import sys
import pytest

# fixtures/test_builtin_monkeypatch.py
def print_info():
    path = os.environ.get("PATH", "")
    print(f"platform: {sys.platform}")
    print(f"PATH: {path}")

def test_one(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(sys, "platform", "MonkeyOS")
    monkeypatch.setenv("PATH", "/zoo")
    print_info()
    assert False

def test_two():
    print_info()
    assert False
