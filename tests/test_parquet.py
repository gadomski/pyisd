import os.path
from tempfile import TemporaryDirectory
from typing import List

import isd.parquet


def test_write_then_read(paths: List[str]) -> None:
    with TemporaryDirectory() as temporary_directory:
        directory = os.path.join(temporary_directory, "isd")
        isd.parquet.write(paths, directory)
        isd.parquet.read(directory).compute()


def test_append(half_path: str, uncompressed_path: str) -> None:
    with TemporaryDirectory() as temporary_directory:
        directory = os.path.join(temporary_directory, "isd")
        isd.parquet.write([half_path], directory)
        isd.parquet.write([uncompressed_path], directory, append=True)
        data_frame = isd.parquet.read(directory).compute()
    assert len(data_frame) == 500
