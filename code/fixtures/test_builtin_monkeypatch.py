import os
import sys
import getpass
import pytest


def print_info():
    path = os.environ.get("PATH", "")
    print(f"platform: {sys.platform}")
    print(f"PATH: {path}")

def test_a(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(sys, "platform", "MonkeyOS")
    monkeypatch.setenv("PATH", "/zoo")
    print_info()
    assert False

def test_b():
    print_info()
    assert False


def get_folder_name() -> str:
    user = getpass.getuser()
    return f"pytest-of-{user}"

def fake_getuser() -> str:
    return "fakeuser"

def test_get_folder_name(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(
        getpass, "getuser",  # target, "name"
        fake_getuser         # value
    )
    assert get_folder_name() == "pytest-of-fakeuser"


def test_get_folder_name_lambda(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(getpass, "getuser", lambda: "fakeuser")
    assert get_folder_name() == "pytest-of-fakeuser"
