import os.path
import pytest


@pytest.fixture
def data_file_path() -> str:
    return os.path.join(os.path.dirname(__file__), "data", "720538-00164-2021")


@pytest.fixture
def record_line(data_file_path: str) -> str:
    with open(data_file_path) as f:
        line = next(f)
    return line
