import datetime
import gzip
import os.path
from contextlib import contextmanager
from typing import Generator, Iterable, Optional

from pandas import DataFrame

from . import pandas as isd_pandas
from .record import Record

builtin_open = open


@contextmanager
def open(path: str) -> Generator[Iterable[Record], None, None]:
    """Opens a local ISD file and returns an iterator over its records.

    If the path has a .gz extension, this function will assume it has gzip
    compression and will attempt to open it using `gzip.open`.
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


def read_to_data_frame(
    path: str, since: Optional[datetime.datetime] = None
) -> DataFrame:
    """Reads a local ISD file into a DataFrame."""
    with open(path) as file:
        return isd_pandas.data_frame(file, since=since)
