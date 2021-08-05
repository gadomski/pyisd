from typing import List

from isd.record import Record, RecordLite


def read(path: str) -> List[Record]:
    """Reads records from a filesystem path."""
    with open(path) as f:
        records = [Record.parse(line) for line in f]
    return records


__all__ = ["Record", "RecordLite"]
