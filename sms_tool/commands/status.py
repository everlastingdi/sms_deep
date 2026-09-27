"""Change the status of an opportunity."""

import argparse

from sms_tool.models import STATUSES
from sms_tool.storage import load, save
from sms_tool.util import now


def add_parser(sub):
    p = sub.add_parser("status", help="set the status of an opportunity")
    p.add_argument("name", help="name of the opportunity")
    p.add_argument("--set", dest="new_status", required=True,
                   help="new status: " + ", ".join(STATUSES))
    p.set_defaults(func=run)


def run(args):
    if args.new_status not in STATUSES:
        print(f"invalid status: {args.new_status} (use {', '.join(STATUSES)})")
        return 1
    store = load()
    items = store["opportunities"]
    if args.name not in items:
        print(f"not found: {args.name}")
        return 1
    items[args.name]["status"] = args.new_status
    items[args.name]["updated"] = now()
    save(store)
    print(f"{args.name} -> {args.new_status}")
    return 0
