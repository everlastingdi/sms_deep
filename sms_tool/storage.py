"""JSON-backed storage for opportunities."""

import json
import os

from sms_tool.config import data_dir


def store_path():
    return os.path.join(data_dir(), "opportunities.json")


def load():
    """Load the store; returns {"opportunities": {...}}."""
    path = store_path()
    if not os.path.exists(path):
        return {"opportunities": {}}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save(store):
    """Persist the store to disk."""
    os.makedirs(data_dir(), exist_ok=True)
    with open(store_path(), "w", encoding="utf-8") as f:
        json.dump(store, f, ensure_ascii=False, indent=2)
