from __future__ import annotations

import os
from datetime import datetime


def get_path(path: str) -> str:
    return os.path.expanduser(path)


def str_to_datetime(date: str):
    result = None
    formats = ["%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"]
    if date:
        for format in formats:
            try:
                return datetime.strptime(date, format)
            except ValueError:
                pass
        raise Exception("Not a valid date format")
    return result
