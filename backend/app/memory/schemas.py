from __future__ import annotations

from enum import Enum


class MemoryType(str, Enum):
    LONG_TERM = "long_term"
    SHORT_TERM = "short_term"


class MemoryQuery:
    pass
