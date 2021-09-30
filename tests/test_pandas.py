from typing import List

import isd.pandas
from isd import Record


def test_data_frame(records: List[Record]) -> None:
    isd.pandas.data_frame(records)
