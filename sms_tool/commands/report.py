"""Generate a daily markdown report."""

import argparse
import os

from sms_tool.storage import load
from sms_tool.util import today


def add_parser(sub):
    p = sub.add_parser("report", help="generate a daily report")
    p.add_argument("--out-dir", default="reports", help="output directory")
    p.set_defaults(func=run)


def run(args):
    items = load()["opportunities"]
    date = today()
    os.makedirs(args.out_dir, exist_ok=True)
    path = os.path.join(args.out_dir, f"{date}.md")

    lines = [f"# Report {date}", ""]
    lines.append(f"Total: {len(items)}")
    for status in ("open", "watching", "done"):
        count = sum(1 for v in items.values() if v["status"] == status)
        lines.append(f"{status}: {count}")
    lines.append("")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"report: {os.path.abspath(path)}")
    return 0
