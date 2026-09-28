"""Append a note to an opportunity."""

import argparse

from sms_tool.storage import load, save
from sms_tool.util import now


def add_parser(sub):
    p = sub.add_parser("note", help="append a note to an opportunity")
    p.add_argument("name", help="name of the opportunity")
    p.add_argument("text", help="note text")
    p.set_defaults(func=run)


def run(args):
    store = load()
    items = store["opportunities"]
    if args.name not in items:
        print(f"not found: {args.name}")
        return 1
    items[args.name].setdefault("notes", []).append(args.text)
    items[args.name]["updated"] = now()
    save(store)
    print(f"note added: {args.name}")
    return 0
