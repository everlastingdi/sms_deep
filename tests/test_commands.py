"""Tests for command modules."""

import pytest

from sms_tool.commands import add as add_cmd
from sms_tool.commands import export as export_cmd
from sms_tool.commands import list as list_cmd
from sms_tool.storage import load


class Args:
    pass


@pytest.fixture(autouse=True)
def isolated_data_dir(tmp_path, monkeypatch):
    monkeypatch.setenv("SMS_TOOL_DIR", str(tmp_path))


def test_add_then_list(capsys):
    a = Args()
    a.name = "project-x"
    a.chain = "ethereum"
    a.category = "airdrop"
    a.link = "https://example.com"
    a.note = "research"
    assert add_cmd.run(a) == 0

    l = Args()
    l.status = ""
    l.chain = ""
    assert list_cmd.run(l) == 0
    out = capsys.readouterr().out
    assert "project-x" in out


def test_add_persists():
    a = Args()
    a.name = "project-y"
    a.chain = ""
    a.category = ""
    a.link = ""
    a.note = ""
    add_cmd.run(a)
    store = load()
    assert "project-y" in store["opportunities"]


def test_export_markdown(capsys):
    a = Args()
    a.name = "project-z"
    a.chain = "solana"
    a.category = ""
    a.link = ""
    a.note = ""
    add_cmd.run(a)

    e = Args()
    e.fmt = "md"
    e.out = ""
    export_cmd.run(e)
    out = capsys.readouterr().out
    assert "# Opportunities" in out
    assert "project-z" in out
