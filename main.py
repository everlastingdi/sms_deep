#!/usr/bin/env python3
"""sms_tool - track crypto / airdrop opportunities from the terminal."""

import argparse
import importlib
import pkgutil
import sys

from sms_tool import VERSION


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sms_tool",
        description="Track crypto / airdrop opportunities from the terminal.",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {VERSION}"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # Auto-discover every command module in sms_tool.commands.
    import sms_tool.commands as commands_pkg

    for mod in pkgutil.iter_modules(commands_pkg.__path__):
        if mod.name.startswith("_"):
            continue
        module = importlib.import_module("sms_tool.commands." + mod.name)
        if hasattr(module, "add_parser"):
            module.add_parser(sub)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
