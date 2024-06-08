from __future__ import annotations

from datetime import timedelta
from typing import MutableSequence


class Instance:
    def __init__(self, start: timedelta, end: timedelta):
        self.start: timedelta = start
        self.end: timedelta = end

    def get_exec(self) -> timedelta:
        return self.end - self.start


class Step:
    def __init__(self, name: str, instances: MutableSequence[Instance]):
        self.name: str = name
        self.instances: MutableSequence[Instance] = instances

    def get_start(self) -> timedelta:
        return min(instance.start for instance in self.instances)

    def get_end(self) -> timedelta:
        return max(instance.end for instance in self.instances)

    def get_exec(self) -> timedelta:
        return self.get_end() - self.get_start()
