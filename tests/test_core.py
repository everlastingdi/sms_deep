"""Tests for the core storage and model modules."""

import pytest

from sms_tool import models, storage


@pytest.fixture(autouse=True)
def isolated_data_dir(tmp_path, monkeypatch):
    monkeypatch.setenv("SMS_TOOL_DIR", str(tmp_path))


def test_load_returns_empty_store_when_missing():
    store = storage.load()
    assert store == {"opportunities": {}}


def test_save_and_load_roundtrip():
    storage.save({"opportunities": {"x": {"name": "x"}}})
    store = storage.load()
    assert store["opportunities"]["x"]["name"] == "x"


def test_opportunity_roundtrip():
    opp = models.Opportunity(name="test", chain="ethereum", notes=["a"])
    opp.created = "2026-01-01 00:00:00"
    data = opp.to_dict()
    restored = models.Opportunity.from_dict(data)
    assert restored.name == "test"
    assert restored.chain == "ethereum"
    assert restored.notes == ["a"]


def test_opportunity_requires_name():
    with pytest.raises(ValueError):
        models.Opportunity(name="")


def test_opportunity_rejects_bad_status():
    with pytest.raises(ValueError):
        models.Opportunity(name="x", status="nope")
