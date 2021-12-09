import datetime
from typing import Iterable, Iterator, Optional

from isd.record import Record


def filter_by_datetime(
    records: Iterable[Record],
    start: Optional[datetime.datetime] = None,
    end: Optional[datetime.datetime] = None,
) -> Iterator[Record]:
    """Returns an iterator over records filtered by start and end datetimes (both optional)."""
    return (
        record
        for record in records
        if (not start or record.datetime() >= start)
        and (not end or record.datetime() < end)
    )
