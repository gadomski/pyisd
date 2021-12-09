import datetime
from typing import List

import isd.utils
from isd.record import Record


def test_filter_by_datetime(records: List[Record]) -> None:
    assert (
        len(
            list(
                isd.utils.filter_by_datetime(
                    records, start=datetime.datetime(2021, 1, 1, 3, 30)
                )
            )
        )
        == 490
    )
    assert (
        len(
            list(
                isd.utils.filter_by_datetime(
                    records, end=datetime.datetime(2021, 1, 1, 3, 30)
                )
            )
        )
        == 10
    )
    assert (
        len(
            list(
                isd.utils.filter_by_datetime(
                    records,
                    start=datetime.datetime(2021, 1, 1, 3, 30),
                    end=datetime.datetime(2021, 1, 1, 3, 55),
                )
            )
        )
        == 1
    )
    assert (
        len(
            list(
                isd.utils.filter_by_datetime(
                    records,
                    start=datetime.datetime(2021, 1, 1, 3, 30),
                    end=datetime.datetime(2021, 1, 1, 3, 56),
                )
            )
        )
        == 2
    )
