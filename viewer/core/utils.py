from __future__ import annotations

import os
from datetime import datetime


def get_path(path: str) -> str:
    return os.path.expanduser(path)


def str_to_datetime(date: str):
    result = None
    if date:
        try:
            result = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            result = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
    return result
