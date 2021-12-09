import datetime

import isd.io


def test_open_uncompressed(uncompressed_path: str) -> None:
    with isd.io.open(uncompressed_path) as generator:
        records = list(generator)
    assert len(records) == 500


def test_open_compressed(compressed_path: str) -> None:
    with isd.io.open(compressed_path) as generator:
        records = list(generator)
    assert len(records) == 24252


def test_read_to_data_frame_since(uncompressed_path: str) -> None:
    data_frame = isd.io.read_to_data_frame(
        uncompressed_path, since=datetime.datetime(2021, 1, 5)
    )
    assert len(data_frame) == 212


def test_from_text_io(uncompressed_path: str) -> None:
    with open(uncompressed_path) as file:
        records = list(isd.io.from_text_io(file))
        assert len(records) == 500
