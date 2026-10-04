# sms_tool

A small command-line tool to track crypto / airdrop opportunities from the
terminal. Keep a local list of projects, chains, links and notes, and export
them to CSV or Markdown whenever you need to.

## Install

```bash
git clone https://github.com/everlastingdi/sms_deep.git
cd sms_deep
pip install -e .
```

## Quick start

```bash
sms-tool init                     # create the data directory
sms-tool add project-x --chain ethereum --category airdrop --link https://...
sms-tool list                     # list everything
sms-tool list --status open       # filter by status
sms-tool show project-x           # show details and notes
sms-tool note project-x "did the quest"
sms-tool status project-x --set done
sms-tool export --format csv --out opportunities.csv
sms-tool report                   # generate a daily markdown report
```

Data is stored as JSON under `~/.sms_tool/` (override with `SMS_TOOL_DIR`).

## Commands

| command  | description                          |
|----------|--------------------------------------|
| `init`   | initialize the data directory        |
| `add`    | add a new opportunity                |
| `list`   | list opportunities (with filters)    |
| `show`   | show details of one opportunity      |
| `status` | change status (open / watching / done) |
| `note`   | append a note                        |
| `delete` | remove an opportunity                |
| `export` | export to csv or markdown            |
| `report` | generate a daily report              |

## Development

```bash
pip install -e .[dev]
python -m pytest tests -q
```

## License

MIT
