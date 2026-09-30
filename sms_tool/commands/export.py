"""Export opportunities to csv or markdown."""

import argparse
import csv
import os

from sms_tool.storage import load


def add_parser(sub):
    p = sub.add_parser("export", help="export opportunities")
    p.add_argument("--format", dest="fmt", default="md",
                   choices=["csv", "md"], help="output format")
    p.add_argument("--out", default="", help="output file (default: stdout)")
    p.set_defaults(func=run)


def run(args):
    items = load()["opportunities"]

    if args.fmt == "csv":
        text = _to_csv(items)
    else:
        text = _to_md(items)

    if args.out:
        with open(args.out, "w", encoding="utf-8", newline="") as f:
            f.write(text)
        print(f"exported: {os.path.abspath(args.out)}")
    else:
        print(text)
    return 0


def _to_csv(items):
    import io

    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(["name", "status", "chain", "category", "link"])
    for name in sorted(items):
        v = items[name]
        writer.writerow([name, v["status"], v.get("chain", ""),
                         v.get("category", ""), v.get("link", "")])
    return buf.getvalue()


def _to_md(items):
    lines = ["# Opportunities", ""]
    for name in sorted(items):
        v = items[name]
        lines.append(f"- **{name}** [{v['status']}] "
                     f"{v.get('chain', '')} {v.get('link', '')}")
    return "\n".join(lines) + "\n"
