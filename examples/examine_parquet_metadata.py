"""Given a list of one or more parquet files, examine the metadata that would be produced by writing them to parquet using this library.

The data in the provided files is repartioned by a default interval.
"""

import os.path
import sys
from tempfile import TemporaryDirectory
from typing import Any, List

import pandas
import pyarrow.parquet
from pyarrow import Table

import isd.io

paths = sys.argv[1:]
data_frames = [isd.io.read_to_data_frame(path) for path in paths]
data_frame = pandas.concat(data_frames)
data_frame = data_frame.set_index(["timestamp", "usaf_id", "ncei_id"])
table = Table.from_pandas(data_frame)

metadata_collector: List[Any] = []
with TemporaryDirectory() as temporary_directory:
    directory = os.path.join(temporary_directory, "isd")
    pyarrow.parquet.write_to_dataset(
        table, directory, metadata_collector=metadata_collector
    )

print(metadata_collector)
