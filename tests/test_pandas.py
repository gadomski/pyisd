from typing import List

import isd.pandas
from isd import Record


def test_data_frame(records: List[Record]) -> None:
    isd.pandas.data_frame(records)


def test_geo_data_frame(records: List[Record]) -> None:
    isd.pandas.geo_data_frame(records)
