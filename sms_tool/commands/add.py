"""Add a new opportunity."""

import argparse

from sms_tool.models import Opportunity
from sms_tool.storage import load, save
from sms_tool.util import now


def add_parser(sub):
    p = sub.add_parser("add", help="add a new opportunity")
    p.add_argument("name", help="name of the opportunity")
    p.add_argument("--chain", default="", help="chain, e.g. ethereum")
    p.add_argument("--category", default="", help="category, e.g. airdrop")
    p.add_argument("--link", default="", help="project url")
    p.add_argument("--note", default="", help="initial note")
    p.set_defaults(func=run)


def run(args):
    notes = [args.note] if args.note else []
    opp = Opportunity(
        name=args.name,
        chain=args.chain,
        category=args.category,
        link=args.link,
        notes=notes,
    )
    opp.created = now()
    opp.updated = now()
    store = load()
    store["opportunities"][args.name] = opp.to_dict()
    save(store)
    print(f"added: {args.name}")
    return 0
