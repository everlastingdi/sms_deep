"""Initialize the data directory."""

import argparse

from sms_tool.config import data_dir
from sms_tool.storage import save


def add_parser(sub):
    p = sub.add_parser("init", help="initialize the data directory")
    p.set_defaults(func=run)


def run(args):
    save({"opportunities": {}})
    print(f"initialized data dir: {data_dir()}")
    return 0
