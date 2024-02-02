import datetime
import json

import pytest

from isd import Batch


def test_batch_from_uncompressed(uncompressed_path: str) -> None:
    batch = Batch.from_path(uncompressed_path)
    assert len(batch) == 500


def test_batch_from_compressed(compressed_path: str) -> None:
    batch = Batch.from_path(compressed_path)
    assert len(batch) == 24252


def test_batch_from_string(uncompressed_path: str) -> None:
    with open(uncompressed_path) as file:
        batch = Batch.parse(file.read())
    assert len(batch) == 500


def test_batch_filter_by_datetime(batch: Batch) -> None:
    batch_filtered = batch.filter_by_datetime(
        start_date=datetime.datetime(2021, 1, 1, 3, 30)
    )
    assert len(batch_filtered) == 490

    batch_filtered = batch.filter_by_datetime(
        end_date=datetime.datetime(2021, 1, 1, 3, 30)
    )
    assert len(batch_filtered) == 10

    batch_filtered = batch.filter_by_datetime(
        start_date=datetime.datetime(2021, 1, 1, 3, 30),
        end_date=datetime.datetime(2021, 1, 1, 3, 55),
    )
    assert len(batch_filtered) == 1

    batch_filtered = batch.filter_by_datetime(
        start_date=datetime.datetime(2021, 1, 1, 3, 30),
        end_date=datetime.datetime(2021, 1, 1, 3, 56),
    )
    assert len(batch_filtered) == 2


def test_batch_to_dict(batch: Batch) -> None:
    first = batch.to_dict()[0]
    assert first["usaf_id"] == "720538"
    assert first["ncei_id"] == "00164"
    assert first["datetime"] == datetime.datetime(2021, 1, 1, 0, 15)


def test_batch_to_json(batch: Batch) -> None:
    json_string = batch.to_json()
    data = json.loads(json_string)
    assert len(data) == 500
    first = data[0]
    assert first["usaf_id"] == "720538"
    assert first["ncei_id"] == "00164"
    assert first["datetime"] == "2021-01-01T00:15:00"


@pytest.mark.pandas  # type: ignore
def test_batch_to_df(batch: Batch) -> None:
    pytest.importorskip("pandas")

    datetime_min = datetime.datetime(2021, 1, 5)
    df = batch.to_data_frame()
    df = df[df["datetime"] >= datetime_min]
    assert len(df) == 212
