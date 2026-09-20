"""Configuration helpers."""

import os


def data_dir():
    """Directory used to store tool data.

    Override with the SMS_TOOL_DIR environment variable.
    """
    return os.environ.get("SMS_TOOL_DIR") or os.path.join(
        os.path.expanduser("~"), ".sms_tool"
    )
