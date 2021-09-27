import os.path
from contextlib import contextmanager
from io import TextIOWrapper
from typing import Generator, cast

import pytest

VANCE_BRAND_FILE_NAME = "720538-00164-2021"


def data_file_path(file_name: str) -> str:
    return os.path.join(os.path.dirname(__file__), "data", file_name)


@contextmanager
def open_data_file(file_name: str) -> Generator[TextIOWrapper, None, None]:
    with open(data_file_path(file_name)) as f:
        yield cast(TextIOWrapper, f)


@pytest.fixture
def record_line() -> str:
    with open_data_file(VANCE_BRAND_FILE_NAME) as f:
        line = next(f)
    return line
