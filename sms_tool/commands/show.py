"""Show details of one opportunity."""

import argparse

from sms_tool.storage import load


def add_parser(sub):
    p = sub.add_parser("show", help="show details of an opportunity")
    p.add_argument("name", help="name of the opportunity")
    p.set_defaults(func=run)


def run(args):
    items = load()["opportunities"]
    v = items.get(args.name)
    if v is None:
        print(f"not found: {args.name}")
        return 1
    print(f"name    : {v['name']}")
    print(f"status  : {v['status']}")
    print(f"chain   : {v.get('chain', '')}")
    print(f"category: {v.get('category', '')}")
    print(f"link    : {v.get('link', '')}")
    print(f"created : {v.get('created', '')}")
    print(f"updated : {v.get('updated', '')}")
    for note in v.get("notes", []):
        print(f"note    : {note}")
    return 0
