import os.path

import pytest

import isd


def test_read(data_file_path):
    records = isd.read(data_file_path)
    assert len(records) == 500


@pytest.fixture
def data_file_path():
    return os.path.join(os.path.dirname(__file__), "data", "720538-00164-2021")
