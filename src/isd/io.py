import gzip
import os.path
from contextlib import contextmanager
from typing import Generator, Iterable

from isd.record import Record

builtin_open = open


@contextmanager
def open(path: str) -> Generator[Iterable[Record], None, None]:
    """Opens a local ISD file and returns an iterator over its records.

    If the path has a .gz compression, assumes that it is gzip compressed.
    """
    if os.path.splitext(path)[1] == ".gz":
        with gzip.open(path) as gzip_file:
            yield (Record.parse(gzip_line.decode("utf-8")) for gzip_line in gzip_file)
    else:
        with builtin_open(path) as uncompressed_file:
            yield (
                Record.parse(uncompressed_line)
                for uncompressed_line in uncompressed_file
            )
