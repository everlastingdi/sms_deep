"""Shared helper utilities."""

from datetime import datetime


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def today():
    return datetime.now().strftime("%Y-%m-%d")


def color(text, code):
    return f"\033[{code}m{text}\033[0m"
