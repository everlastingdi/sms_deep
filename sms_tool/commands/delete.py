"""Delete an opportunity."""

import argparse

from sms_tool.storage import load, save


def add_parser(sub):
    p = sub.add_parser("delete", help="delete an opportunity")
    p.add_argument("name", help="name of the opportunity")
    p.set_defaults(func=run)


def run(args):
    store = load()
    items = store["opportunities"]
    if args.name not in items:
        print(f"not found: {args.name}")
        return 1
    del items[args.name]
    save(store)
    print(f"deleted: {args.name}")
    return 0
