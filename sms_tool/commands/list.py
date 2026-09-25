"""List opportunities."""

import argparse

from sms_tool.storage import load


def add_parser(sub):
    p = sub.add_parser("list", help="list opportunities")
    p.add_argument("--status", default="", help="filter by status")
    p.add_argument("--chain", default="", help="filter by chain")
    p.set_defaults(func=run)


def run(args):
    items = load()["opportunities"]
    if args.status:
        items = {k: v for k, v in items.items() if v["status"] == args.status}
    if args.chain:
        items = {k: v for k, v in items.items() if v["chain"] == args.chain}
    if not items:
        print("no opportunities")
        return 0
    for name in sorted(items):
        v = items[name]
        print(f"{name} [{v['status']}] {v.get('chain', '')} {v.get('link', '')}")
    return 0
